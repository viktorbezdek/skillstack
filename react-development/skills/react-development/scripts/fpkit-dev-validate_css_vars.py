#!/usr/bin/env python3
"""
Portable CSS Variable Validation Script for @fpkit/acss consumers

Validates CSS custom properties in SCSS files against fpkit naming conventions:
- Pattern: --{component}-{property} or --{component}-{variant}-{property}
- Units: rem only (not px)
- Approved abbreviations: bg, fs, fw, radius, gap
- Full words: padding, margin, color, border, display, width, height

Usage:
    python validate_css_vars.py [file_or_directory]
    python validate_css_vars.py styles/
    python validate_css_vars.py components/button.scss

Compatible with @fpkit/acss v1.x
"""

import re
import sys
from pathlib import Path
from typing import List, Tuple, Dict

# Approved abbreviations (fpkit convention)
APPROVED_ABBREVIATIONS = {'bg', 'fs', 'fw', 'radius', 'gap'}

# Forbidden abbreviations (should use full words)
FORBIDDEN_ABBREVIATIONS = {
    'px': 'padding-inline',
    'py': 'padding-block',
    'mx': 'margin-inline',
    'my': 'margin-block',
    'w': 'width',
    'h': 'height',
    'cl': 'color',
    'c': 'color',
    'dsp': 'display',
    'd': 'display',
    'bdr': 'border',
    'br': 'border',
}

# Valid property names (full words required)
VALID_FULL_WORDS = {
    'padding', 'padding-inline', 'padding-block',
    'margin', 'margin-inline', 'margin-block',
    'color', 'border', 'display', 'width', 'height',
    'font', 'text', 'line', 'letter',
    'outline', 'shadow', 'opacity', 'cursor',
    'transform', 'transition', 'animation',
    'flex', 'grid', 'gap', 'align', 'justify',
}

# Pattern for CSS variable declarations
CSS_VAR_PATTERN = re.compile(
    r'--([a-z][a-z0-9-]*)\s*:\s*([^;]+);',
    re.IGNORECASE
)

# Pattern for pixel values
PX_UNIT_PATTERN = re.compile(r'\b(\d+(?:\.\d+)?)px\b')

# Pattern for rem values
REM_UNIT_PATTERN = re.compile(r'\b(\d+(?:\.\d+)?)rem\b')


class ValidationError:
    """Represents a validation error"""
    def __init__(self, file_path: Path, line_num: int, var_name: str, message: str):
        self.file_path = file_path
        self.line_num = line_num
        self.var_name = var_name
        self.message = message

    def __str__(self):
        return f"{self.file_path}:{self.line_num} - {self.var_name}: {self.message}"


def validate_variable_name(var_name: str) -> List[str]:
    """
    Validate CSS variable naming convention

    Valid patterns:
    - --component-property (e.g., --btn-bg)
    - --component-variant-property (e.g., --btn-primary-bg)
    - --component-element-property (e.g., --card-header-bg)
    - --component-state-property (e.g., --btn-hover-bg)

    Returns list of error messages (empty if valid)
    """
    errors = []
    parts = var_name.split('-')

    # Must have at least 2 parts: component + property
    if len(parts) < 2:
        errors.append("Variable must follow pattern: --{component}-{property}")
        return errors

    component = parts[0]
    property_part = parts[-1]

    # Check for forbidden abbreviations
    for forbidden, replacement in FORBIDDEN_ABBREVIATIONS.items():
        if property_part == forbidden:
            errors.append(
                f"Use '{replacement}' instead of '{forbidden}' (forbidden abbreviation)"
            )

    # Check if using valid abbreviation or full word
    if property_part not in APPROVED_ABBREVIATIONS:
        # If not approved abbreviation, should be full word or compound
        is_valid_full_word = any(
            property_part.startswith(word) or property_part == word
            for word in VALID_FULL_WORDS
        )
        if not is_valid_full_word and len(property_part) <= 3:
            errors.append(
                f"Property '{property_part}' should be a full word or approved abbreviation"
            )

    return errors


def validate_variable_value(var_name: str, var_value: str) -> List[str]:
    """
    Validate CSS variable value

    Rules:
    - Should use rem units for spacing/sizing (not px)
    - Exception: 0px is ok, border widths (1px, 2px) are ok

    Returns list of error messages (empty if valid)
    """
    errors = []

    # Check for px units (excluding valid cases)
    px_matches = PX_UNIT_PATTERN.findall(var_value)
    for px_value in px_matches:
        px_float = float(px_value)

        # Allow 0px
        if px_float == 0:
            continue

        # Allow small px values for borders (1px, 2px)
        if 'border' in var_name and px_float <= 2:
            continue

        # Calculate rem equivalent
        rem_value = px_float / 16
        errors.append(
            f"Use rem units instead of px: {px_value}px = {rem_value}rem"
        )

    return errors


def validate_scss_file(file_path: Path) -> List[ValidationError]:
    """
    Validate all CSS variables in an SCSS file

    Returns list of ValidationError objects
    """
    errors = []

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"Error reading {file_path}: {e}", file=sys.stderr)
        return errors

    for line_num, line in enumerate(lines, start=1):
        # Skip comments
        if line.strip().startswith('//') or line.strip().startswith('/*'):
            continue

        # Find CSS variable declarations
        matches = CSS_VAR_PATTERN.finditer(line)
        for match in matches:
            var_name = match.group(1)
            var_value = match.group(2).strip()

            # Validate variable name
            name_errors = validate_variable_name(var_name)
            for error_msg in name_errors:
                errors.append(
                    ValidationError(file_path, line_num, f"--{var_name}", error_msg)
                )

            # Validate variable value
            value_errors = validate_variable_value(var_name, var_value)
            for error_msg in value_errors:
                errors.append(
                    ValidationError(file_path, line_num, f"--{var_name}", error_msg)
                )

    return errors


def find_scss_files(path: Path) -> List[Path]:
    """Find all SCSS files in path (file or directory)"""
    if path.is_file():
        if path.suffix in ['.scss', '.css']:
            return [path]
        else:
            return []
    elif path.is_dir():
        return list(path.rglob('*.scss')) + list(path.rglob('*.css'))
    else:
        return []


def main():
    """Main validation function"""
    # Get path from arguments or use current directory
    if len(sys.argv) > 1:
        target_path = Path(sys.argv[1])
    else:
        target_path = Path('.')

    if not target_path.exists():
        print(f"Error: Path '{target_path}' does not exist", file=sys.stderr)
        sys.exit(1)

    # Find SCSS files
    scss_files = find_scss_files(target_path)

    if not scss_files:
        print(f"No SCSS/CSS files found in {target_path}")
        sys.exit(0)

    print(f"Validating {len(scss_files)} file(s)...")
    print()

    # Validate each file
    all_errors = []
    for file_path in scss_files:
        file_errors = validate_scss_file(file_path)
        all_errors.extend(file_errors)

    # Report results
    if not all_errors:
        print("✓ All CSS variables are valid!")
        print()
        print("Validated against @fpkit/acss conventions:")
        print("  • Naming pattern: --{component}-{property}")
        print("  • Units: rem (not px)")
        print("  • Approved abbreviations: bg, fs, fw, radius, gap")
        print("  • Full words for: padding, margin, color, border, display, width, height")
        sys.exit(0)
    else:
        print(f"✗ Found {len(all_errors)} validation error(s):")
        print()

        # Group errors by file
        errors_by_file: Dict[Path, List[ValidationError]] = {}
        for error in all_errors:
            if error.file_path not in errors_by_file:
                errors_by_file[error.file_path] = []
            errors_by_file[error.file_path].append(error)

        # Print errors grouped by file
        for file_path, file_errors in sorted(errors_by_file.items()):
            print(f"\n{file_path}:")
            for error in file_errors:
                print(f"  Line {error.line_num}: {error.var_name}")
                print(f"    {error.message}")

        print()
        print("See @fpkit/acss documentation:")
        print("  https://github.com/shawn-sandy/acss/blob/main/packages/fpkit/docs/guides/css-variables.md")
        sys.exit(1)


if __name__ == '__main__':
    main()
