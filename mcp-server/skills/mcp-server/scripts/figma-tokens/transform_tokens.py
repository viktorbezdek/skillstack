#!/usr/bin/env python3
"""
Transform W3C DTCG Tokens to Multiple Output Formats

Converts W3C Design Tokens Community Group (DTCG) compliant JSON
to CSS custom properties, SCSS variables, JSON, TypeScript types,
and documentation.

Usage:
    python transform_tokens.py \\
        --input tokens.json \\
        --format css,scss,json,typescript,documentation \\
        --naming-convention kebab-case \\
        --output-dir ./output

Features:
    - CSS custom properties with :root selector
    - SCSS variables with $ prefix
    - Style Dictionary compatible JSON
    - TypeScript type definitions
    - Auto-generated documentation
    - Customizable naming conventions
    - File organization strategies
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# Import shared utilities
from utils import NamingConvention, ValueFormatter


class TokenTransformer:
    """Transform W3C DTCG tokens to various formats"""

    def __init__(self, naming_convention: str = 'kebab-case'):
        self.naming_convention = naming_convention
        self.tokens: Dict[str, Any] = {}

    def load_tokens(self, file_path: Path) -> Dict[str, Any]:
        """Load W3C DTCG tokens from JSON file"""
        with open(file_path, 'r', encoding='utf-8') as f:
            self.tokens = json.load(f)
        return self.tokens

    def to_css(self, organize_by_category: bool = False) -> Dict[str, str]:
        """
        Convert tokens to CSS custom properties

        Returns:
            Dictionary mapping filename to CSS content
        """
        if organize_by_category:
            return self._to_css_by_category()
        else:
            return {'tokens.css': self._generate_css(self.tokens)}

    def _to_css_by_category(self) -> Dict[str, str]:
        """Generate separate CSS files per category"""
        results = {}
        for category, category_tokens in self.tokens.items():
            if isinstance(category_tokens, dict):
                css_content = self._generate_css({category: category_tokens})
                results[f"{category}.css"] = css_content
        return results

    def _generate_css(self, tokens: Dict[str, Any], prefix: str = '') -> str:
        """Generate CSS custom properties"""
        lines = [
            '/**',
            ' * Design Tokens - CSS Custom Properties',
            ' * Generated from W3C DTCG format',
            ' */',
            '',
            ':root {'
        ]

        def process_token(path: str, token: Any, indent: int = 1):
            """Recursively process tokens"""
            if isinstance(token, dict):
                # Check if this is a token definition
                if '$value' in token:
                    var_name = NamingConvention.apply(path, self.naming_convention)
                    value = self._format_css_value(token['$value'])

                    # Add comment if description exists
                    if '$description' in token:
                        lines.append(f"{'  ' * indent}/* {token['$description']} */")

                    lines.append(f"{'  ' * indent}--{var_name}: {value};")
                else:
                    # Group or nested tokens
                    for key, val in token.items():
                        if not key.startswith('$'):
                            new_path = f"{path}.{key}" if path else key
                            process_token(new_path, val, indent)

        for category, category_tokens in tokens.items():
            if category.startswith('$'):
                continue

            lines.append(f"  /* {category.capitalize()} */")
            process_token(category, category_tokens)
            lines.append('')

        lines.append('}')
        return '\n'.join(lines)

    def _format_css_value(self, value: Any) -> str:
        """Format token value for CSS"""
        return ValueFormatter.to_css_value(value, self.naming_convention)

    def to_scss(self, organize_by_category: bool = False) -> Dict[str, str]:
        """
        Convert tokens to SCSS variables

        Returns:
            Dictionary mapping filename to SCSS content
        """
        if organize_by_category:
            return self._to_scss_by_category()
        else:
            return {'tokens.scss': self._generate_scss(self.tokens)}

    def _to_scss_by_category(self) -> Dict[str, str]:
        """Generate separate SCSS files per category"""
        results = {}
        for category, category_tokens in self.tokens.items():
            if isinstance(category_tokens, dict):
                scss_content = self._generate_scss({category: category_tokens})
                results[f"{category}.scss"] = scss_content
        return results

    def _generate_scss(self, tokens: Dict[str, Any]) -> str:
        """Generate SCSS variables"""
        lines = [
            '//',
            '// Design Tokens - SCSS Variables',
            '// Generated from W3C DTCG format',
            '//',
            ''
        ]

        def process_token(path: str, token: Any):
            """Recursively process tokens"""
            if isinstance(token, dict):
                if '$value' in token:
                    var_name = NamingConvention.apply(path, self.naming_convention)
                    value = self._format_scss_value(token['$value'])

                    if '$description' in token:
                        lines.append(f"// {token['$description']}")

                    lines.append(f"${var_name}: {value};")
                else:
                    for key, val in token.items():
                        if not key.startswith('$'):
                            new_path = f"{path}.{key}" if path else key
                            process_token(new_path, val)

        for category, category_tokens in tokens.items():
            if category.startswith('$'):
                continue

            lines.append(f"// {category.capitalize()}")
            process_token(category, category_tokens)
            lines.append('')

        return '\n'.join(lines)

    def _format_scss_value(self, value: Any) -> str:
        """Format token value for SCSS"""
        return ValueFormatter.to_scss_value(value, self.naming_convention)

    def to_json(self, organize_by_category: bool = False) -> Dict[str, str]:
        """
        Convert to Style Dictionary compatible JSON

        Returns:
            Dictionary mapping filename to JSON content
        """
        if organize_by_category:
            results = {}
            for category, category_tokens in self.tokens.items():
                if isinstance(category_tokens, dict):
                    results[f"{category}.json"] = json.dumps(
                        {category: category_tokens},
                        indent=2,
                        ensure_ascii=False
                    )
            return results
        else:
            return {'tokens.json': json.dumps(self.tokens, indent=2, ensure_ascii=False)}

    def to_typescript(self) -> Dict[str, str]:
        """
        Generate TypeScript type definitions

        Returns:
            Dictionary with tokens.ts file
        """
        lines = [
            '/**',
            ' * Design Tokens - TypeScript Definitions',
            ' * Generated from W3C DTCG format',
            ' */',
            ''
        ]

        # Generate type definitions
        for category, category_tokens in self.tokens.items():
            if category.startswith('$'):
                continue

            type_name = f"{category.capitalize()}Tokens"
            lines.append(f"export type {type_name} = {{")

            def process_token_types(path: str, token: Any, indent: int = 1):
                """Generate TypeScript types"""
                if isinstance(token, dict):
                    if '$value' in token:
                        var_name = NamingConvention.apply(path.split('.')[-1], self.naming_convention)
                        value = token['$value']

                        if isinstance(value, str):
                            lines.append(f"{'  ' * indent}{var_name}: '{value}';")
                        elif isinstance(value, (int, float)):
                            lines.append(f"{'  ' * indent}{var_name}: {value};")
                        else:
                            lines.append(f"{'  ' * indent}{var_name}: any;")
                    else:
                        for key, val in token.items():
                            if not key.startswith('$'):
                                new_path = f"{path}.{key}" if path else key
                                process_token_types(new_path, val, indent)

            process_token_types(category, category_tokens)
            lines.append('};')
            lines.append('')

        # Generate const object
        lines.append('export const tokens = {')

        for category, category_tokens in self.tokens.items():
            if category.startswith('$'):
                continue

            lines.append(f"  {category}: {{")

            def process_token_values(path: str, token: Any, indent: int = 2):
                """Generate token values"""
                if isinstance(token, dict):
                    if '$value' in token:
                        var_name = NamingConvention.apply(path.split('.')[-1], self.naming_convention)
                        value = token['$value']

                        if isinstance(value, str):
                            lines.append(f"{'  ' * indent}{var_name}: '{value}',")
                        else:
                            lines.append(f"{'  ' * indent}{var_name}: {json.dumps(value)},")
                    else:
                        for key, val in token.items():
                            if not key.startswith('$'):
                                new_path = f"{path}.{key}" if path else key
                                process_token_values(new_path, val, indent)

            process_token_values(category, category_tokens)
            lines.append('  },')

        lines.append('} as const;')

        return {'tokens.ts': '\n'.join(lines)}

    def to_documentation(self) -> Dict[str, str]:
        """
        Generate markdown documentation

        Returns:
            Dictionary with documentation.md file
        """
        lines = [
            '# Design Tokens Documentation',
            '',
            'Auto-generated from W3C DTCG format.',
            ''
        ]

        for category, category_tokens in self.tokens.items():
            if category.startswith('$'):
                continue

            lines.append(f"## {category.capitalize()}")
            lines.append('')
            lines.append('| Token Name | Value | Type | Description |')
            lines.append('|------------|-------|------|-------------|')

            def process_token_docs(path: str, token: Any):
                """Generate documentation table rows"""
                if isinstance(token, dict):
                    if '$value' in token:
                        var_name = NamingConvention.apply(path, self.naming_convention)
                        value = str(token['$value'])[:50]  # Truncate long values
                        token_type = token.get('$type', 'unknown')
                        description = token.get('$description', '')

                        lines.append(f"| `{var_name}` | `{value}` | {token_type} | {description} |")
                    else:
                        for key, val in token.items():
                            if not key.startswith('$'):
                                new_path = f"{path}.{key}" if path else key
                                process_token_docs(new_path, val)

            process_token_docs(category, category_tokens)
            lines.append('')

        # Add usage examples
        lines.extend([
            '## Usage Examples',
            '',
            '### CSS',
            '```css',
            '.element {',
            '  color: var(--color-primary);',
            '  margin: var(--spacing-medium);',
            '}',
            '```',
            '',
            '### SCSS',
            '```scss',
            '.element {',
            '  color: $color-primary;',
            '  margin: $spacing-medium;',
            '}',
            '```',
            '',
            '### TypeScript',
            '```typescript',
            "import { tokens } from './tokens';",
            '',
            'const styles = {',
            '  color: tokens.color.primary,',
            '  margin: tokens.spacing.medium,',
            '};',
            '```'
        ])

        return {'documentation.md': '\n'.join(lines)}


def main():
    parser = argparse.ArgumentParser(
        description='Transform W3C DTCG tokens to multiple output formats'
    )
    parser.add_argument(
        '--input',
        required=True,
        type=Path,
        help='Path to W3C DTCG JSON file'
    )
    parser.add_argument(
        '--format',
        default='css,scss,json,typescript,documentation',
        help='Comma-separated output formats (css, scss, json, typescript, documentation). Default: all'
    )
    parser.add_argument(
        '--naming-convention',
        default='kebab-case',
        choices=['kebab-case', 'camelCase', 'snake_case', 'bem'],
        help='Naming convention for tokens. Default: kebab-case'
    )
    parser.add_argument(
        '--output-dir',
        required=True,
        type=Path,
        help='Directory for output files'
    )
    parser.add_argument(
        '--organize-by-category',
        action='store_true',
        help='Generate separate files per token category'
    )

    args = parser.parse_args()

    # Validate input
    if not args.input.exists():
        print(f"Error: Input file not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    # Parse formats
    formats = [f.strip() for f in args.format.split(',')]

    try:
        # Load tokens
        transformer = TokenTransformer(naming_convention=args.naming_convention)
        transformer.load_tokens(args.input)

        # Create output directory
        args.output_dir.mkdir(parents=True, exist_ok=True)

        # Generate outputs
        total_files = 0

        if 'css' in formats:
            css_files = transformer.to_css(organize_by_category=args.organize_by_category)
            for filename, content in css_files.items():
                output_path = args.output_dir / filename
                output_path.write_text(content, encoding='utf-8')
                print(f"✓ Generated {output_path}")
                total_files += 1

        if 'scss' in formats:
            scss_files = transformer.to_scss(organize_by_category=args.organize_by_category)
            for filename, content in scss_files.items():
                output_path = args.output_dir / filename
                output_path.write_text(content, encoding='utf-8')
                print(f"✓ Generated {output_path}")
                total_files += 1

        if 'json' in formats:
            json_files = transformer.to_json(organize_by_category=args.organize_by_category)
            for filename, content in json_files.items():
                output_path = args.output_dir / filename
                output_path.write_text(content, encoding='utf-8')
                print(f"✓ Generated {output_path}")
                total_files += 1

        if 'typescript' in formats:
            ts_files = transformer.to_typescript()
            for filename, content in ts_files.items():
                output_path = args.output_dir / filename
                output_path.write_text(content, encoding='utf-8')
                print(f"✓ Generated {output_path}")
                total_files += 1

        if 'documentation' in formats:
            doc_files = transformer.to_documentation()
            for filename, content in doc_files.items():
                output_path = args.output_dir / filename
                output_path.write_text(content, encoding='utf-8')
                print(f"✓ Generated {output_path}")
                total_files += 1

        print(f"\n✓ Successfully generated {total_files} files in {args.output_dir}")

    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in input file: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
