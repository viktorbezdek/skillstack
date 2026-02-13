#!/usr/bin/env python3
"""Style improvement suggester."""
import sys
from pathlib import Path

def analyze_and_suggest(root_path):
    """Analyze styles and suggest improvements."""
    suggestions = []

    # Check for modern CSS features
    css_files = list(root_path.rglob('*.css'))
    if css_files:
        content = ''.join([f.read_text() for f in css_files[:10] if 'node_modules' not in str(f)])

        if 'float:' in content:
            suggestions.append("[TIP] Consider replacing float layouts with Flexbox or Grid")
        if 'px' in content and 'rem' not in content:
            suggestions.append("[TIP] Consider using rem units for better accessibility")
        if '@media' in content and '@container' not in content:
            suggestions.append("[TIP] Consider container queries for component-level responsiveness")
        if not re.search(r'--[\w-]+:', content):
            suggestions.append("[TIP] Consider using CSS custom properties for theming")

    return suggestions

def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else '.').resolve()
    print(" Analyzing for improvement opportunities...\n")

    suggestions = analyze_and_suggest(root)
    for s in suggestions:
        print(f"  {s}")

    if not suggestions:
        print("  [OK] No immediate improvements suggested!")

if __name__ == '__main__':
    main()
