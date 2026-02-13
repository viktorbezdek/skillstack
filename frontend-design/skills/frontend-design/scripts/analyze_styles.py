#!/usr/bin/env python3
"""
Style Master - Codebase Style Analyzer

Analyzes a frontend codebase to understand styling approach, extract design tokens,
identify patterns, and detect issues.

Usage:
    python analyze_styles.py [--path /path/to/project]
    python analyze_styles.py --detailed
    python analyze_styles.py --export report.json

Examples:
    python analyze_styles.py
    python analyze_styles.py --path ../my-app --detailed
"""

import os
import sys
import json
import re
import argparse
from pathlib import Path
from collections import Counter, defaultdict


def find_style_files(root_path):
    """Find all styling-related files in the project."""
    style_extensions = {
        '.css', '.scss', '.sass', '.less',
        '.module.css', '.module.scss',
        '.styled.js', '.styled.ts', '.styled.jsx', '.styled.tsx'
    }

    style_files = {
        'css': [],
        'scss': [],
        'sass': [],
        'less': [],
        'css_modules': [],
        'css_in_js': [],
        'tailwind_config': [],
        'other': []
    }

    for root, dirs, files in os.walk(root_path):
        # Skip common ignore directories
        dirs[:] = [d for d in dirs if d not in {'node_modules', '.git', 'dist', 'build', '.next', 'out'}]

        for file in files:
            file_path = Path(root) / file

            if file == 'tailwind.config.js' or file == 'tailwind.config.ts':
                style_files['tailwind_config'].append(file_path)
            elif file.endswith('.module.css') or file.endswith('.module.scss'):
                style_files['css_modules'].append(file_path)
            elif '.styled.' in file:
                style_files['css_in_js'].append(file_path)
            elif file.endswith('.css'):
                style_files['css'].append(file_path)
            elif file.endswith('.scss'):
                style_files['scss'].append(file_path)
            elif file.endswith('.sass'):
                style_files['sass'].append(file_path)
            elif file.endswith('.less'):
                style_files['less'].append(file_path)

    return style_files


def detect_styling_approach(style_files, root_path):
    """Detect the primary styling approach used."""
    approaches = []

    if style_files['tailwind_config']:
        approaches.append('Tailwind CSS')

    if style_files['css_in_js']:
        approaches.append('CSS-in-JS (Styled Components/Emotion)')

    if style_files['css_modules']:
        approaches.append('CSS Modules')

    if style_files['scss'] or style_files['sass']:
        approaches.append('Sass/SCSS')

    if style_files['less']:
        approaches.append('Less')

    if style_files['css'] and not style_files['css_modules']:
        approaches.append('Vanilla CSS')

    # Check for UI frameworks
    package_json = Path(root_path) / 'package.json'
    if package_json.exists():
        try:
            with open(package_json, 'r') as f:
                data = json.load(f)
                deps = {**data.get('dependencies', {}), **data.get('devDependencies', {})}

                if '@mui/material' in deps or '@material-ui/core' in deps:
                    approaches.append('Material UI')
                if '@chakra-ui/react' in deps:
                    approaches.append('Chakra UI')
                if 'styled-components' in deps:
                    approaches.append('Styled Components')
                if '@emotion/react' in deps or '@emotion/styled' in deps:
                    approaches.append('Emotion')
        except:
            pass

    return approaches if approaches else ['Unknown']


def extract_colors(content):
    """Extract color values from CSS content."""
    colors = []

    # Hex colors
    hex_pattern = r'#(?:[0-9a-fA-F]{3}){1,2}\b'
    colors.extend(re.findall(hex_pattern, content))

    # RGB/RGBA
    rgb_pattern = r'rgba?\([^)]+\)'
    colors.extend(re.findall(rgb_pattern, content))

    # HSL/HSLA
    hsl_pattern = r'hsla?\([^)]+\)'
    colors.extend(re.findall(hsl_pattern, content))

    # CSS custom properties with color-like names
    custom_prop_pattern = r'--(?:color|bg|background|border|text)[^:;\s]+:\s*([^;]+)'
    colors.extend(re.findall(custom_prop_pattern, content))

    return colors


def extract_spacing_values(content):
    """Extract spacing values (margin, padding, gap)."""
    spacing = []

    # Match spacing properties
    spacing_pattern = r'(?:margin|padding|gap)[^:]*:\s*([^;]+)'
    matches = re.findall(spacing_pattern, content)

    for match in matches:
        # Extract numeric values
        values = re.findall(r'\d+(?:\.\d+)?(?:px|rem|em|%|vh|vw)', match)
        spacing.extend(values)

    return spacing


def extract_css_custom_properties(content):
    """Extract CSS custom properties (variables)."""
    pattern = r'--([\w-]+):\s*([^;]+)'
    return dict(re.findall(pattern, content))


def analyze_file_content(file_path):
    """Analyze content of a single style file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        return {
            'colors': extract_colors(content),
            'spacing': extract_spacing_values(content),
            'custom_properties': extract_css_custom_properties(content),
            'size': len(content),
            'lines': content.count('\n') + 1
        }
    except Exception as e:
        return {'error': str(e)}


def generate_report(style_files, root_path, detailed=False):
    """Generate analysis report."""
    print("="*70)
    print(" Style Master - Codebase Analysis")
    print("="*70)
    print(f"\nAnalyzing: {root_path}\n")

    # Styling approach
    approaches = detect_styling_approach(style_files, root_path)
    print("## Styling Approach\n")
    for approach in approaches:
        print(f"  [CHECK] {approach}")
    print()

    # File counts
    total_files = sum(len(files) for files in style_files.values())
    print(f"## Files Found: {total_files}\n")
    for file_type, files in style_files.items():
        if files:
            print(f"   {file_type}: {len(files)}")
    print()

    # Detailed analysis
    if detailed:
        print("## Design Token Analysis\n")

        all_colors = []
        all_spacing = []
        all_custom_props = {}
        total_size = 0
        total_lines = 0

        # Analyze all CSS files
        for file_type, files in style_files.items():
            if file_type in {'css', 'scss', 'sass', 'less', 'css_modules'}:
                for file_path in files:
                    analysis = analyze_file_content(file_path)
                    if 'error' not in analysis:
                        all_colors.extend(analysis['colors'])
                        all_spacing.extend(analysis['spacing'])
                        all_custom_props.update(analysis['custom_properties'])
                        total_size += analysis['size']
                        total_lines += analysis['lines']

        # Color analysis
        if all_colors:
            color_counts = Counter(all_colors)
            print(f"**Colors Found**: {len(color_counts)} unique colors")
            print(f"\nMost used colors:")
            for color, count in color_counts.most_common(10):
                print(f"   {color}: used {count} times")
            print()

        # Spacing analysis
        if all_spacing:
            spacing_counts = Counter(all_spacing)
            print(f"**Spacing Values**: {len(spacing_counts)} unique values")
            print(f"\nMost used spacing:")
            for value, count in spacing_counts.most_common(10):
                print(f"   {value}: used {count} times")
            print()

        # Custom properties
        if all_custom_props:
            print(f"**CSS Custom Properties**: {len(all_custom_props)} defined")
            print("\nExamples:")
            for prop, value in list(all_custom_props.items())[:10]:
                print(f"   --{prop}: {value}")
            print()

        # Size stats
        print(f"**Total CSS Size**: {total_size:,} bytes ({total_size / 1024:.1f} KB)")
        print(f"**Total Lines**: {total_lines:,}")
        print()

    # Suggestions
    print("## Suggestions\n")

    suggestions = []

    if not any(style_files.values()):
        suggestions.append("[WARNING]  No style files found. Consider adding styling to your project.")

    if 'Tailwind CSS' not in approaches and 'CSS-in-JS' not in approaches:
        suggestions.append("[TIP] Consider modern approaches like Tailwind CSS or CSS-in-JS")

    if style_files['css'] and not style_files['css_modules']:
        suggestions.append("[TIP] Consider CSS Modules to avoid global namespace pollution")

    if not style_files['tailwind_config'] and len(all_colors) > 20:
        suggestions.append("[WARNING]  Many color values detected - consider establishing a color system")

    if len(all_spacing) > 30:
        suggestions.append("[WARNING]  Many spacing values - consider a consistent spacing scale")

    if detailed and not all_custom_props:
        suggestions.append("[TIP] No CSS custom properties found - consider using them for theming")

    for suggestion in suggestions:
        print(f"  {suggestion}")

    if not suggestions:
        print("  [OK] Styling approach looks good!")

    print("\n" + "="*70)

    return {
        'approaches': approaches,
        'file_counts': {k: len(v) for k, v in style_files.items()},
        'colors': len(all_colors) if detailed else None,
        'spacing_values': len(all_spacing) if detailed else None,
        'custom_properties': len(all_custom_props) if detailed else None,
        'suggestions': suggestions
    }


def main():
    parser = argparse.ArgumentParser(
        description='Analyze codebase styling',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        '--path',
        type=str,
        default='.',
        help='Path to project root (default: current directory)'
    )

    parser.add_argument(
        '--detailed',
        action='store_true',
        help='Perform detailed analysis (slower but more comprehensive)'
    )

    parser.add_argument(
        '--export',
        type=str,
        help='Export report to JSON file'
    )

    args = parser.parse_args()

    root_path = Path(args.path).resolve()

    if not root_path.exists():
        print(f"[ERROR] Error: Path does not exist: {root_path}")
        sys.exit(1)

    # Find style files
    style_files = find_style_files(root_path)

    # Generate report
    report_data = generate_report(style_files, root_path, args.detailed)

    # Export if requested
    if args.export:
        with open(args.export, 'w') as f:
            json.dump(report_data, f, indent=2)
        print(f"\n Report exported to: {args.export}")


if __name__ == '__main__':
    main()
