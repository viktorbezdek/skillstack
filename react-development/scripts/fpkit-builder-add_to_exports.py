#!/usr/bin/env python3
"""
Add component exports to index.ts file.

This script adds proper export statements for new components to the main
index.ts file, following fpkit export patterns.

Usage:
    python3 add_to_exports.py <ComponentName> <component-path> [--index <index-path>]

Example:
    python3 add_to_exports.py Alert ./components/alert/alert --index ./src/index.ts

Export patterns supported:
- Simple component: export { Alert, type AlertProps } from "./components/alert/alert"
- Compound component: export { Card, Title as CardTitle, ... } from "./components/cards/card"
- Wildcard export: export * from "./components/layout/landmarks"
"""

import argparse
import re
import sys
from pathlib import Path
from typing import Optional


def to_kebab_case(name: str) -> str:
    """Convert PascalCase to kebab-case."""
    result = []
    for i, char in enumerate(name):
        if char.isupper() and i > 0:
            result.append('-')
        result.append(char.lower())
    return ''.join(result)


def format_export_statement(component_name: str, component_path: str, has_types: bool = True) -> str:
    """
    Format an export statement following fpkit conventions.

    Args:
        component_name: PascalCase component name
        component_path: Relative path to component file (without extension)
        has_types: Whether to include type export

    Returns:
        Formatted export statement
    """
    if has_types:
        return f'export {{ {component_name}, type {component_name}Props }} from "{component_path}";'
    else:
        return f'export {{ {component_name} }} from "{component_path}";'


def find_insert_position(lines: list[str], section_comment: str = None) -> int:
    """
    Find the appropriate position to insert the new export.

    Looks for section comments like "// Core UI components" or inserts
    before the last line.

    Args:
        lines: Lines of the index.ts file
        section_comment: Optional section comment to insert after

    Returns:
        Line index to insert at
    """
    if section_comment:
        for i, line in enumerate(lines):
            if section_comment in line:
                # Insert after the section comment
                return i + 1

    # Default: insert before the last non-empty line
    for i in range(len(lines) - 1, -1, -1):
        if lines[i].strip():
            return i + 1

    return len(lines)


def add_export_to_index(
    index_path: Path,
    component_name: str,
    component_path: str,
    section: Optional[str] = None,
    has_types: bool = True,
    dry_run: bool = False
) -> bool:
    """
    Add export statement to index.ts file.

    Args:
        index_path: Path to index.ts file
        component_name: Component name in PascalCase
        component_path: Relative path to component (from index.ts location)
        section: Optional section comment to insert after
        has_types: Whether component has a Props type to export
        dry_run: If True, print what would be done without modifying

    Returns:
        True if successful, False otherwise
    """
    if not index_path.exists():
        print(f"❌ Error: Index file not found: {index_path}")
        return False

    # Read current content
    content = index_path.read_text()
    lines = content.splitlines()

    # Check if export already exists
    export_pattern = re.compile(rf'export.*{component_name}.*from.*{component_path}')
    if any(export_pattern.search(line) for line in lines):
        print(f"⚠️  Export for {component_name} already exists in {index_path}")
        return True

    # Format the new export statement
    export_statement = format_export_statement(component_name, component_path, has_types)

    # Find insert position
    insert_pos = find_insert_position(lines, section)

    # Insert the export
    lines.insert(insert_pos, export_statement)

    if dry_run:
        print(f"\n📝 Would add to {index_path} at line {insert_pos + 1}:")
        print(f"   {export_statement}\n")
        return True

    # Write back to file
    try:
        index_path.write_text('\n'.join(lines) + '\n')
        print(f"✅ Added export to {index_path}")
        print(f"   {export_statement}\n")
        return True
    except Exception as e:
        print(f"❌ Error writing to {index_path}: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Add component export to index.ts file"
    )
    parser.add_argument(
        "component_name",
        help="Component name in PascalCase (e.g., Alert)"
    )
    parser.add_argument(
        "component_path",
        help="Relative path to component file without extension (e.g., ./components/alert/alert)"
    )
    parser.add_argument(
        "--index",
        default="./src/index.ts",
        help="Path to index.ts file (default: ./src/index.ts)"
    )
    parser.add_argument(
        "--section",
        default=None,
        help="Section comment to insert after (e.g., '// Core UI components')"
    )
    parser.add_argument(
        "--no-types",
        action="store_true",
        help="Don't export component Props type"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without modifying files"
    )

    args = parser.parse_args()

    index_path = Path(args.index)

    print(f"\n📦 Adding export for {args.component_name}")

    success = add_export_to_index(
        index_path,
        args.component_name,
        args.component_path,
        args.section,
        has_types=not args.no_types,
        dry_run=args.dry_run
    )

    if success:
        print("✅ Export added successfully")
        if not args.dry_run:
            print(f"\n💡 Remember to:")
            print(f"   - Import and use {args.component_name} in your application")
            print(f"   - Run 'npm run build' to verify the build")
            print(f"   - Run 'npm run lint' to check code style")
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
