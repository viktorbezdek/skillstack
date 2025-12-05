#!/usr/bin/env python3
"""
Style Master - Style Guide Generator

Generates a living style guide based on codebase analysis.

Usage:
    python generate_styleguide.py [--path /path/to/project]
    python generate_styleguide.py --output STYLEGUIDE.md
    python generate_styleguide.py --format markdown|json

Examples:
    python generate_styleguide.py
    python generate_styleguide.py --output docs/STYLEGUIDE.md
"""

import os
import sys
import json
import argparse
from pathlib import Path
from datetime import datetime
import re
from collections import Counter


def load_template():
    """Load style guide template."""
    template_path = Path(__file__).parent.parent / 'References' / 'style-guide-template.md'

    if template_path.exists():
        with open(template_path, 'r') as f:
            return f.read()

    # Fallback basic template
    return """# {project_name} Style Guide

*Generated: {date}*

## Design Tokens

### Colors

{colors}

### Typography

{typography}

### Spacing

{spacing}

## Components

{components}

## Guidelines

{guidelines}

---

*This is a living document. Update as the design system evolves.*
"""


def detect_project_name(root_path):
    """Detect project name from package.json."""
    package_json = root_path / 'package.json'

    if package_json.exists():
        try:
            with open(package_json, 'r') as f:
                data = json.load(f)
                return data.get('name', root_path.name)
        except:
            pass

    return root_path.name


def extract_design_tokens_from_tailwind(root_path):
    """Extract design tokens from Tailwind config."""
    config_files = ['tailwind.config.js', 'tailwind.config.ts']

    for config_file in config_files:
        config_path = root_path / config_file
        if config_path.exists():
            try:
                with open(config_path, 'r') as f:
                    content = f.read()

                return {
                    'source': 'Tailwind Config',
                    'colors': 'See tailwind.config.js theme.extend.colors',
                    'spacing': 'Using Tailwind default spacing scale',
                    'typography': 'See tailwind.config.js theme.extend.fontFamily'
                }
            except:
                pass

    return None


def extract_css_variables(root_path):
    """Extract CSS custom properties from CSS files."""
    css_vars = {}

    for css_file in root_path.rglob('*.css'):
        if 'node_modules' in str(css_file):
            continue

        try:
            with open(css_file, 'r') as f:
                content = f.read()

            # Find CSS custom properties
            pattern = r'--([\w-]+):\s*([^;]+)'
            matches = re.findall(pattern, content)

            for var_name, var_value in matches:
                css_vars[var_name] = var_value.strip()
        except:
            continue

    return css_vars


def categorize_css_variables(css_vars):
    """Categorize CSS variables by type."""
    categorized = {
        'colors': {},
        'spacing': {},
        'typography': {},
        'other': {}
    }

    color_keywords = ['color', 'bg', 'background', 'border', 'text', 'primary', 'secondary', 'accent']
    spacing_keywords = ['spacing', 'margin', 'padding', 'gap', 'size']
    typo_keywords = ['font', 'text', 'heading', 'body', 'line-height', 'letter-spacing']

    for var_name, var_value in css_vars.items():
        var_lower = var_name.lower()

        if any(keyword in var_lower for keyword in color_keywords):
            categorized['colors'][var_name] = var_value
        elif any(keyword in var_lower for keyword in spacing_keywords):
            categorized['spacing'][var_name] = var_value
        elif any(keyword in var_lower for keyword in typo_keywords):
            categorized['typography'][var_name] = var_value
        else:
            categorized['other'][var_name] = var_value

    return categorized


def format_tokens_section(tokens_dict, title):
    """Format design tokens into markdown."""
    if not tokens_dict:
        return f"*No {title.lower()} tokens defined yet.*\n"

    output = ""
    for var_name, var_value in sorted(tokens_dict.items())[:20]:  # Limit to 20
        output += f"- `--{var_name}`: {var_value}\n"

    if len(tokens_dict) > 20:
        output += f"\n*...and {len(tokens_dict) - 20} more*\n"

    return output


def generate_guidelines(root_path):
    """Generate guidelines based on detected patterns."""
    guidelines = []

    # Check for Tailwind
    if (root_path / 'tailwind.config.js').exists() or (root_path / 'tailwind.config.ts').exists():
        guidelines.append("""
### Tailwind CSS Usage

- **Prefer Tailwind utilities** over custom CSS where possible
- **Use @apply sparingly** - only for frequently repeated patterns
- **Extend the theme** in tailwind.config.js for custom values
- **Use arbitrary values** (e.g., `w-[123px]`) only when necessary
        """)

    # Check for CSS Modules
    css_modules = list(root_path.rglob('*.module.css')) + list(root_path.rglob('*.module.scss'))
    if css_modules:
        guidelines.append("""
### CSS Modules

- **One module per component** - keep styles colocated
- **Use camelCase** for class names in modules
- **Avoid global styles** unless absolutely necessary
- **Compose classes** to avoid duplication
        """)

    # Default guidelines
    guidelines.append("""
### General Principles

- **Mobile-first**: Design for mobile, enhance for desktop
- **Accessibility**: Ensure WCAG AA compliance minimum
- **Performance**: Optimize for fast loading and rendering
- **Consistency**: Use design tokens and established patterns
- **Dark mode**: Support both light and dark themes where applicable
    """)

    return "\n".join(guidelines)


def generate_markdown_styleguide(root_path):
    """Generate markdown style guide."""
    project_name = detect_project_name(root_path)
    date = datetime.now().strftime('%Y-%m-%d')

    # Extract design tokens
    tailwind_tokens = extract_design_tokens_from_tailwind(root_path)
    css_vars = extract_css_variables(root_path)
    categorized = categorize_css_variables(css_vars)

    # Build sections
    colors_section = format_tokens_section(categorized['colors'], 'Colors')
    spacing_section = format_tokens_section(categorized['spacing'], 'Spacing')
    typography_section = format_tokens_section(categorized['typography'], 'Typography')

    if tailwind_tokens:
        colors_section = f"**Using Tailwind CSS**\n\nSee `tailwind.config.js` for the complete color palette.\n\n{colors_section}"

    components_section = """
### Button

*Component documentation to be added*

### Card

*Component documentation to be added*

### Form Elements

*Component documentation to be added*

*Add component documentation as your design system grows.*
    """

    guidelines_section = generate_guidelines(root_path)

    # Build full guide
    styleguide = f"""# {project_name} Style Guide

**Last Updated**: {date}

*This is a living document that evolves with the project.*

---

## Overview

This style guide documents the design system, patterns, and conventions used in {project_name}.

## Design Tokens

Design tokens are the visual design atoms of the design system. They define colors, typography, spacing, and other fundamental values.

### Colors

{colors_section}

### Typography

{typography_section}

### Spacing

{spacing_section}

## Components

Document common component patterns here.

{components_section}

## Guidelines

{guidelines_section}

## Accessibility

### Color Contrast

- Ensure all text has minimum 4.5:1 contrast ratio (WCAG AA)
- Large text (18pt+) requires minimum 3:1 contrast ratio

### Focus States

- All interactive elements must have visible focus indicators
- Focus indicators must have 3:1 contrast ratio with background

### Keyboard Navigation

- All functionality available via keyboard
- Logical tab order
- Skip links for main content

## Performance

### CSS Best Practices

- Remove unused styles in production
- Use CSS containment for complex layouts
- Optimize font loading with `font-display: swap`
- Minimize use of expensive properties in animations

## Resources

- [Design System Documentation](./docs/design-system.md)
- [Component Library](./src/components/)
- [Accessibility Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)

---

*Generated by Style Master on {date}*
"""

    return styleguide


def main():
    parser = argparse.ArgumentParser(
        description='Generate project style guide',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        '--path',
        type=str,
        default='.',
        help='Path to project root (default: current directory)'
    )

    parser.add_argument(
        '--output',
        type=str,
        default='STYLEGUIDE.md',
        help='Output file path (default: STYLEGUIDE.md)'
    )

    parser.add_argument(
        '--format',
        choices=['markdown', 'json'],
        default='markdown',
        help='Output format (default: markdown)'
    )

    args = parser.parse_args()

    root_path = Path(args.path).resolve()

    if not root_path.exists():
        print(f"[ERROR] Error: Path does not exist: {root_path}")
        sys.exit(1)

    print(f"[NOTE] Generating style guide for: {root_path}")

    # Generate style guide
    if args.format == 'markdown':
        styleguide = generate_markdown_styleguide(root_path)

        output_path = Path(args.output)
        with open(output_path, 'w') as f:
            f.write(styleguide)

        print(f"[OK] Style guide created: {output_path}")
        print(f"\n Review and customize the generated style guide")
        print(f"   Add component examples, update guidelines, refine tokens\n")
    else:
        # JSON format (for programmatic use)
        css_vars = extract_css_variables(root_path)
        categorized = categorize_css_variables(css_vars)

        data = {
            'project': detect_project_name(root_path),
            'generated': datetime.now().isoformat(),
            'tokens': categorized
        }

        output_path = Path(args.output).with_suffix('.json')
        with open(output_path, 'w') as f:
            json.dump(data, f, indent=2)

        print(f"[OK] Style guide data exported: {output_path}")


if __name__ == '__main__':
    main()
