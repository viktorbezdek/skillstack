#!/usr/bin/env python3
"""
Validate CSS variable naming conventions and rem units in SCSS files.

This script checks fpkit component styles for:
- Proper CSS variable naming: --{component}-{property}
- rem units only (no px)
- Logical properties (padding-inline/block, margin-inline/block)
- No forbidden abbreviations (px/py, w/h, cl, dsp, bdr)

Usage:
    python3 validate_css_vars.py <file.scss> [--fix]

Example:
    python3 validate_css_vars.py ./components/alert/alert.scss
    python3 validate_css_vars.py ./components/**/*.scss --fix
"""

import argparse
import re
import sys
from pathlib import Path
from typing import List, Tuple


# Approved abbreviations
APPROVED_ABBR = {'bg', 'fs', 'fw', 'radius', 'gap'}

# Forbidden abbreviations
FORBIDDEN_ABBR = {
    'px': 'padding-inline',
    'py': 'padding-block',
    'w': 'width',
    'h': 'height',
    'cl': 'color',
    'dsp': 'display',
    'bdr': 'border',
}

# Pattern for CSS custom properties
CSS_VAR_PATTERN = re.compile(r'--([a-z0-9-]+)')

# Pattern for px units
PX_UNIT_PATTERN = re.compile(r':\s*[0-9.]+px')

# Pattern for forbidden property abbreviations
FORBIDDEN_PROP_PATTERN = re.compile(r'--[a-z]+-(?:px|py|w|h|cl|dsp|bdr)(?:-|$)')


class ValidationError:
    """Represents a validation error in a CSS file."""

    def __init__(self, line_num: int, line: str, message: str, suggestion: str = None):
        self.line_num = line_num
        self.line = line.strip()
        self.message = message
        self.suggestion = suggestion

    def __str__(self):
        result = f"Line {self.line_num}: {self.message}\n  {self.line}"
        if self.suggestion:
            result += f"\n  💡 Suggestion: {self.suggestion}"
        return result


def validate_css_variable_naming(var_name: str, line: str) -> Tuple[bool, str]:
    """
    Validate CSS variable naming convention.

    Returns:
        (is_valid, error_message)
    """
    parts = var_name.split('-')

    # Check minimum structure: --component-property
    if len(parts) < 2:
        return False, f"Variable '{var_name}' should follow --{{component}}-{{property}} pattern"

    # Check for forbidden abbreviations
    for part in parts:
        if part in FORBIDDEN_ABBR:
            return False, f"Forbidden abbreviation '{part}' (use '{FORBIDDEN_ABBR[part]}' instead)"

    # Variable is valid
    return True, ""


def validate_rem_units(line: str) -> Tuple[bool, str]:
    """
    Check if line uses px units instead of rem.

    Returns:
        (is_valid, error_message)
    """
    if PX_UNIT_PATTERN.search(line):
        # Check for exceptions (0px is ok, sometimes used in borders)
        if re.search(r':\s*0px', line):
            return True, ""
        return False, "Use rem units instead of px (px/16 = rem, e.g., 16px = 1rem)"

    return True, ""


def validate_logical_properties(line: str) -> Tuple[bool, str]:
    """
    Check if padding/margin use logical properties.

    Returns:
        (is_valid, error_message)
    """
    # Check for --component-px or --component-py patterns
    if re.search(r'--[a-z]+-p[xy](?:-|:|\s)', line):
        return False, "Use logical properties: padding-inline (not px), padding-block (not py)"

    # Check for --component-mx or --component-my patterns
    if re.search(r'--[a-z]+-m[xy](?:-|:|\s)', line):
        return False, "Use logical properties: margin-inline (not mx), margin-block (not my)"

    return True, ""


def validate_file(file_path: Path) -> List[ValidationError]:
    """Validate a single SCSS file."""
    errors = []

    try:
        content = file_path.read_text()
        lines = content.splitlines()

        for i, line in enumerate(lines, start=1):
            # Skip comments
            if line.strip().startswith('//'):
                continue

            # Check CSS variable naming
            for match in CSS_VAR_PATTERN.finditer(line):
                var_name = match.group(0)
                is_valid, error_msg = validate_css_variable_naming(var_name, line)
                if not is_valid:
                    errors.append(ValidationError(i, line, error_msg))

            # Check rem units
            is_valid, error_msg = validate_rem_units(line)
            if not is_valid:
                errors.append(ValidationError(i, line, error_msg))

            # Check logical properties
            is_valid, error_msg = validate_logical_properties(line)
            if not is_valid:
                errors.append(ValidationError(i, line, error_msg))

    except Exception as e:
        print(f"❌ Error reading {file_path}: {e}")
        sys.exit(1)

    return errors


def main():
    parser = argparse.ArgumentParser(
        description="Validate CSS variable naming and rem units in SCSS files"
    )
    parser.add_argument(
        "file_path",
        help="Path to SCSS file to validate"
    )
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Attempt to auto-fix common issues (not implemented yet)"
    )

    args = parser.parse_args()
    file_path = Path(args.file_path)

    if not file_path.exists():
        print(f"❌ File not found: {file_path}")
        sys.exit(1)

    if not file_path.suffix in ['.scss', '.css']:
        print(f"⚠️  Warning: {file_path} is not a CSS/SCSS file")

    print(f"\n🔍 Validating: {file_path}\n")

    errors = validate_file(file_path)

    if not errors:
        print("✅ No issues found! CSS variables follow fpkit conventions.\n")
        sys.exit(0)

    print(f"❌ Found {len(errors)} issue(s):\n")
    for error in errors:
        print(f"{error}\n")

    print(f"📖 Reference: See references/css-variable-guide.md for naming conventions\n")

    sys.exit(1)


if __name__ == "__main__":
    main()
