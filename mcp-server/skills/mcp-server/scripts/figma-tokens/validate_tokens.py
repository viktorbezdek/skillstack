#!/usr/bin/env python3
"""
Validate W3C DTCG Design Tokens

Validates design tokens against the W3C Design Tokens Community Group
(DTCG) specification and checks for common issues.

Usage:
    python validate_tokens.py \\
        --input tokens.json \\
        --report validation-report.md

Validations:
    - W3C DTCG specification compliance
    - Required properties ($value)
    - Token type consistency
    - Circular reference detection
    - Value format correctness
    - Group inheritance validation
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple


class TokenValidator:
    """Validate W3C DTCG design tokens"""

    # Valid W3C DTCG token types
    VALID_TYPES = {
        'color', 'dimension', 'fontFamily', 'fontWeight', 'duration',
        'cubicBezier', 'number', 'string', 'boolean',
        'typography', 'shadow', 'border', 'gradient', 'strokeStyle'
    }

    def __init__(self):
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.info: List[str] = []
        self.token_paths: Set[str] = set()
        self.references: Dict[str, List[str]] = {}  # token -> referenced tokens

    def validate(self, tokens: Dict[str, Any]) -> bool:
        """
        Validate token structure

        Args:
            tokens: W3C DTCG token dictionary

        Returns:
            True if valid, False if errors found
        """
        self._validate_structure(tokens, '')
        self._detect_circular_references()

        return len(self.errors) == 0

    def _validate_structure(self, obj: Any, path: str, parent_type: Optional[str] = None):
        """Recursively validate token structure"""
        if not isinstance(obj, dict):
            self.errors.append(f"{path}: Expected object, got {type(obj).__name__}")
            return

        # Check if this is a token definition
        if '$value' in obj:
            self._validate_token(obj, path, parent_type)
        else:
            # Check for group-level $type
            group_type = obj.get('$type')

            # Validate children
            for key, value in obj.items():
                # Skip special properties
                if key.startswith('$'):
                    if key == '$type' and value not in self.VALID_TYPES:
                        self.warnings.append(f"{path}.$type: Unknown type '{value}'")
                    continue

                # Validate child
                new_path = f"{path}.{key}" if path else key
                self._validate_structure(value, new_path, group_type)

    def _validate_token(self, token: Dict[str, Any], path: str, parent_type: Optional[str]):
        """Validate individual token"""
        self.token_paths.add(path)

        # Required: $value
        if '$value' not in token:
            self.errors.append(f"{path}: Missing required property '$value'")
            return

        value = token['$value']

        # Check token type
        token_type = token.get('$type') or parent_type
        if not token_type:
            self.warnings.append(f"{path}: No $type specified (not inherited from group)")

        # Validate value format
        if isinstance(value, str) and value.startswith('{') and value.endswith('}'):
            # This is a reference/alias
            ref_path = value[1:-1]
            if path not in self.references:
                self.references[path] = []
            self.references[path].append(ref_path)
            self.info.append(f"{path}: References {ref_path}")
        elif token_type:
            self._validate_value_by_type(value, token_type, path)

        # Validate optional properties
        if '$description' in token and not isinstance(token['$description'], str):
            self.errors.append(f"{path}.$description: Must be a string")

        if '$deprecated' in token:
            deprecated = token['$deprecated']
            if not isinstance(deprecated, (bool, str)):
                self.errors.append(f"{path}.$deprecated: Must be boolean or string")

        # Check for unknown properties
        known_props = {'$value', '$type', '$description', '$deprecated', '$extensions'}
        for prop in token.keys():
            if prop.startswith('$') and prop not in known_props:
                self.warnings.append(f"{path}.{prop}: Unknown property")

    def _validate_value_by_type(self, value: Any, token_type: str, path: str):
        """Validate value matches token type"""

        if token_type == 'color':
            self._validate_color(value, path)
        elif token_type == 'dimension':
            self._validate_dimension(value, path)
        elif token_type == 'fontFamily':
            self._validate_font_family(value, path)
        elif token_type == 'fontWeight':
            self._validate_font_weight(value, path)
        elif token_type == 'duration':
            self._validate_duration(value, path)
        elif token_type == 'cubicBezier':
            self._validate_cubic_bezier(value, path)
        elif token_type == 'number':
            if not isinstance(value, (int, float)):
                self.errors.append(f"{path}: number type must be numeric, got {type(value).__name__}")
        elif token_type == 'string':
            if not isinstance(value, str):
                self.errors.append(f"{path}: string type must be string, got {type(value).__name__}")
        elif token_type == 'boolean':
            if not isinstance(value, bool):
                self.errors.append(f"{path}: boolean type must be boolean, got {type(value).__name__}")
        elif token_type == 'typography':
            self._validate_typography(value, path)
        elif token_type == 'shadow':
            self._validate_shadow(value, path)
        elif token_type == 'border':
            self._validate_border(value, path)

    def _validate_color(self, value: Any, path: str):
        """Validate color value"""
        if isinstance(value, str):
            # Hex color
            if not (value.startswith('#') or value.startswith('rgb') or value.startswith('hsl')):
                self.warnings.append(f"{path}: Color string should be hex, rgb(), or hsl() format")
        elif isinstance(value, dict):
            # Color space object
            if 'colorSpace' not in value:
                self.errors.append(f"{path}: Color object missing 'colorSpace' property")
            if 'components' not in value:
                self.errors.append(f"{path}: Color object missing 'components' property")
            elif not isinstance(value['components'], list):
                self.errors.append(f"{path}: Color 'components' must be an array")
        else:
            self.errors.append(f"{path}: Color value must be string or object")

    def _validate_dimension(self, value: Any, path: str):
        """Validate dimension value"""
        if not isinstance(value, str):
            self.errors.append(f"{path}: Dimension must be a string with unit (e.g., '16px', '1rem')")
            return

        # Check for numeric value with unit
        import re
        if not re.match(r'^-?\d+(\.\d+)?(px|rem|em|%|vh|vw|vmin|vmax|pt|pc|in|cm|mm)$', value):
            self.warnings.append(f"{path}: Dimension value '{value}' doesn't match expected format")

    def _validate_font_family(self, value: Any, path: str):
        """Validate fontFamily value"""
        if isinstance(value, str):
            pass  # Valid
        elif isinstance(value, list):
            if not all(isinstance(f, str) for f in value):
                self.errors.append(f"{path}: fontFamily array must contain only strings")
        else:
            self.errors.append(f"{path}: fontFamily must be string or array of strings")

    def _validate_font_weight(self, value: Any, path: str):
        """Validate fontWeight value"""
        if isinstance(value, (int, float)):
            if not (1 <= value <= 1000):
                self.warnings.append(f"{path}: fontWeight {value} outside recommended range 1-1000")
        elif isinstance(value, str):
            valid_keywords = ['thin', 'extra-light', 'light', 'normal', 'medium', 'semi-bold', 'bold', 'extra-bold', 'black']
            if value.lower() not in valid_keywords:
                self.warnings.append(f"{path}: fontWeight '{value}' not a standard keyword")
        else:
            self.errors.append(f"{path}: fontWeight must be number or string")

    def _validate_duration(self, value: Any, path: str):
        """Validate duration value"""
        if not isinstance(value, str):
            self.errors.append(f"{path}: Duration must be a string with unit (e.g., '200ms', '0.5s')")
            return

        import re
        if not re.match(r'^\d+(\.\d+)?(ms|s)$', value):
            self.warnings.append(f"{path}: Duration value '{value}' doesn't match expected format")

    def _validate_cubic_bezier(self, value: Any, path: str):
        """Validate cubicBezier value"""
        if not isinstance(value, list):
            self.errors.append(f"{path}: cubicBezier must be an array of 4 numbers")
            return

        if len(value) != 4:
            self.errors.append(f"{path}: cubicBezier must have exactly 4 values")
        elif not all(isinstance(v, (int, float)) for v in value):
            self.errors.append(f"{path}: cubicBezier values must be numbers")

    def _validate_typography(self, value: Any, path: str):
        """Validate typography composite value"""
        if not isinstance(value, dict):
            self.errors.append(f"{path}: typography value must be an object")
            return

        # Check recommended properties
        recommended = ['fontFamily', 'fontSize', 'fontWeight', 'lineHeight']
        for prop in recommended:
            if prop not in value:
                self.warnings.append(f"{path}: typography missing recommended property '{prop}'")

    def _validate_shadow(self, value: Any, path: str):
        """Validate shadow composite value"""
        if not isinstance(value, dict):
            self.errors.append(f"{path}: shadow value must be an object")
            return

        required = ['offsetX', 'offsetY', 'blur', 'color']
        for prop in required:
            if prop not in value:
                self.errors.append(f"{path}: shadow missing required property '{prop}'")

    def _validate_border(self, value: Any, path: str):
        """Validate border composite value"""
        if not isinstance(value, dict):
            self.errors.append(f"{path}: border value must be an object")
            return

        required = ['width', 'style', 'color']
        for prop in required:
            if prop not in value:
                self.errors.append(f"{path}: border missing required property '{prop}'")

    def _detect_circular_references(self):
        """Detect circular references in token aliases"""

        def has_cycle(token: str, visited: Set[str], stack: Set[str]) -> Optional[List[str]]:
            """DFS to detect cycles"""
            visited.add(token)
            stack.add(token)

            if token in self.references:
                for ref in self.references[token]:
                    if ref not in visited:
                        cycle = has_cycle(ref, visited, stack)
                        if cycle:
                            return [token] + cycle
                    elif ref in stack:
                        return [token, ref]

            stack.remove(token)
            return None

        visited = set()
        for token in self.references.keys():
            if token not in visited:
                cycle = has_cycle(token, visited, set())
                if cycle:
                    cycle_str = ' -> '.join(cycle)
                    self.errors.append(f"Circular reference detected: {cycle_str}")

    def generate_report(self) -> str:
        """Generate markdown validation report"""
        lines = [
            '# Design Tokens Validation Report',
            '',
            f'**Total Tokens:** {len(self.token_paths)}',
            f'**Errors:** {len(self.errors)}',
            f'**Warnings:** {len(self.warnings)}',
            ''
        ]

        # Summary
        if len(self.errors) == 0:
            lines.append('✓ **Status: VALID** - No errors found')
        else:
            lines.append('✗ **Status: INVALID** - Errors must be fixed')

        # Errors
        if self.errors:
            lines.extend(['', '## Errors', ''])
            for i, error in enumerate(self.errors, 1):
                lines.append(f"{i}. {error}")

        # Warnings
        if self.warnings:
            lines.extend(['', '## Warnings', ''])
            for i, warning in enumerate(self.warnings, 1):
                lines.append(f"{i}. {warning}")

        # Info
        if self.info:
            lines.extend(['', '## Info', ''])
            for item in self.info[:10]:  # Limit to first 10
                lines.append(f"- {item}")
            if len(self.info) > 10:
                lines.append(f"- ... and {len(self.info) - 10} more")

        # Summary by type
        lines.extend(['', '## Token Summary', ''])
        token_types: Dict[str, int] = {}
        # This would require re-parsing, skip for now
        lines.append('(Type breakdown requires extended analysis)')

        return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(
        description='Validate W3C DTCG design tokens'
    )
    parser.add_argument(
        '--input',
        required=True,
        type=Path,
        help='Path to W3C DTCG JSON file'
    )
    parser.add_argument(
        '--report',
        type=Path,
        help='Path for validation report (markdown). If omitted, prints to stdout.'
    )
    parser.add_argument(
        '--strict',
        action='store_true',
        help='Treat warnings as errors'
    )

    args = parser.parse_args()

    # Validate input exists
    if not args.input.exists():
        print(f"Error: Input file not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    try:
        # Load tokens
        with open(args.input, 'r', encoding='utf-8') as f:
            tokens = json.load(f)

        # Validate
        validator = TokenValidator()
        is_valid = validator.validate(tokens)

        # Generate report
        report = validator.generate_report()

        # Output report
        if args.report:
            args.report.parent.mkdir(parents=True, exist_ok=True)
            args.report.write_text(report, encoding='utf-8')
            print(f"✓ Validation report written to {args.report}")
        else:
            print(report)

        # Print summary to stderr
        print(f"\n{'='*60}", file=sys.stderr)
        print(f"Validation Summary:", file=sys.stderr)
        print(f"  Tokens: {len(validator.token_paths)}", file=sys.stderr)
        print(f"  Errors: {len(validator.errors)}", file=sys.stderr)
        print(f"  Warnings: {len(validator.warnings)}", file=sys.stderr)
        print(f"{'='*60}", file=sys.stderr)

        # Exit code
        if not is_valid:
            print("✗ Validation failed with errors", file=sys.stderr)
            sys.exit(1)
        elif args.strict and validator.warnings:
            print("✗ Validation failed with warnings (strict mode)", file=sys.stderr)
            sys.exit(1)
        else:
            print("✓ Validation passed", file=sys.stderr)
            sys.exit(0)

    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in input file: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
