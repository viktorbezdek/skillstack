#!/usr/bin/env python3
"""
Scaffold a new fpkit component with all required files.

This script generates the complete 5-file structure for a new component:
- component.tsx (main component file)
- component.types.ts (TypeScript type definitions)
- component.scss (styles with CSS variables)
- component.stories.tsx (Storybook stories)
- component.test.tsx (Vitest tests)

Supports three modes:
- new: Create brand new component (default)
- compose: Create component by composing existing components
- extend: Create component that extends existing component

Usage:
    python3 scaffold_component.py <ComponentName> [--path <output-directory>] [--mode <new|compose|extend>] [--uses <Component1,Component2>]

Examples:
    # New component
    python3 scaffold_component.py Alert --path ./packages/fpkit/src/components/alert

    # Composed component
    python3 scaffold_component.py StatusButton --mode compose --uses Badge,Button

    # Extended component
    python3 scaffold_component.py EnhancedAlert --mode extend --uses Alert
"""

import argparse
import os
import re
import sys
from pathlib import Path
from typing import List, Optional


def to_kebab_case(name: str) -> str:
    """Convert PascalCase to kebab-case."""
    result = []
    for i, char in enumerate(name):
        if char.isupper() and i > 0:
            result.append('-')
        result.append(char.lower())
    return ''.join(result)


def get_template_path(skill_dir: Path, template_name: str) -> Path:
    """Get the path to a template file."""
    return skill_dir / "assets" / "templates" / template_name


def read_template(skill_dir: Path, template_name: str) -> str:
    """Read a template file."""
    template_path = get_template_path(skill_dir, template_name)
    if not template_path.exists():
        raise FileNotFoundError(f"Template not found: {template_path}")
    return template_path.read_text()


def substitute_placeholders(
    content: str,
    component_name: str,
    mode: str = "new",
    uses_components: Optional[List[str]] = None
) -> str:
    """Replace template placeholders with actual component name and component dependencies."""
    kebab_name = to_kebab_case(component_name)

    replacements = {
        "{{ComponentName}}": component_name,
        "{{componentName}}": component_name[0].lower() + component_name[1:],
        "{{component-name}}": kebab_name,
        "{{COMPONENT_NAME}}": component_name.upper(),
    }

    for placeholder, value in replacements.items():
        content = content.replace(placeholder, value)

    # Additional substitutions for compose/extend modes
    if uses_components:
        content = substitute_component_imports(content, uses_components)
        content = substitute_component_list(content, uses_components)

    return content


def substitute_component_imports(content: str, components: List[str]) -> str:
    """Generate import statements for components to use."""
    imports = []
    for comp in components:
        kebab = to_kebab_case(comp)
        # Determine likely import path based on common fpkit structure
        if comp in ["Button"]:
            import_line = f"import {{ {comp}, type {comp}Props }} from '../buttons/button'"
        else:
            import_line = f"import {{ {comp}, type {comp}Props }} from '../{kebab}/{kebab}'"
        imports.append(import_line)

    import_block = "\n".join(imports)

    # Replace placeholder
    content = content.replace("// IMPORT_PLACEHOLDER: Add imports for existing fpkit components", import_block)
    content = content.replace("// IMPORT_BASE_COMPONENT_PLACEHOLDER", import_block)

    return content


def substitute_component_list(content: str, components: List[str]) -> str:
    """Replace placeholders with component list."""
    component_list = ", ".join(components)

    # Replace various placeholders
    replacements = {
        "COMPONENTS_LIST_PLACEHOLDER": component_list,
        "BASE_COMPONENT_PLACEHOLDER": components[0] if components else "BaseComponent",
        "NEW_FEATURE_1_PLACEHOLDER": "Additional functionality",
        "NEW_FEATURE_2_PLACEHOLDER": "Enhanced behavior",
        "NEW_FEATURE_3_PLACEHOLDER": "New variant options"
    }

    for placeholder, value in replacements.items():
        content = content.replace(placeholder, value)

    return content


def scaffold_component(
    component_name: str,
    output_dir: Path,
    skill_dir: Path,
    mode: str = "new",
    uses_components: Optional[List[str]] = None
):
    """Generate all component files from templates."""

    # Validate component name (should be PascalCase)
    if not component_name[0].isupper():
        print(f"⚠️  Warning: Component name should start with uppercase letter (PascalCase)")

    kebab_name = to_kebab_case(component_name)

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    # Select appropriate template based on mode
    if mode == "compose":
        component_template = "component.composed.template.tsx"
    elif mode == "extend":
        component_template = "component.extended.template.tsx"
    else:
        component_template = "component.template.tsx"

    # Template file mappings
    templates = {
        component_template: f"{kebab_name}.tsx",
        "component.template.types.ts": f"{kebab_name}.types.ts",
        "component.template.scss": f"{kebab_name}.scss",
        "component.template.stories.tsx": f"{kebab_name}.stories.tsx",
        "component.template.test.tsx": f"{kebab_name}.test.tsx",
    }

    # Mode-specific messaging
    mode_emoji = {
        "new": "⚡",
        "compose": "🔧",
        "extend": "📝"
    }
    mode_description = {
        "new": "Creating new component",
        "compose": f"Composing from: {', '.join(uses_components) if uses_components else 'components'}",
        "extend": f"Extending: {uses_components[0] if uses_components else 'base component'}"
    }

    print(f"\n{mode_emoji.get(mode, '🚀')} Scaffolding component: {component_name}")
    print(f"   Mode: {mode_description.get(mode, mode)}")
    print(f"   Output directory: {output_dir}\n")

    created_files = []

    for template_name, output_filename in templates.items():
        try:
            # Read template
            template_content = read_template(skill_dir, template_name)

            # Substitute placeholders
            output_content = substitute_placeholders(
                template_content,
                component_name,
                mode,
                uses_components
            )

            # Write output file
            output_path = output_dir / output_filename
            output_path.write_text(output_content)

            created_files.append(output_filename)
            print(f"✅ Created: {output_filename}")

        except FileNotFoundError as e:
            print(f"❌ Error: {e}")
            sys.exit(1)
        except Exception as e:
            print(f"❌ Error creating {output_filename}: {e}")
            sys.exit(1)

    print(f"\n✅ Successfully scaffolded {len(created_files)} files for {component_name}")

    # Mode-specific next steps
    if mode == "compose":
        print(f"\n📝 Next steps for composed component:")
        print(f"   1. Review imported components in {kebab_name}.tsx")
        print(f"   2. Implement composition logic (combine imported components)")
        print(f"   3. Define props interface in {kebab_name}.types.ts")
        print(f"   4. Add minimal custom styles in {kebab_name}.scss (reuse base styles)")
        print(f"   5. Document composition in Storybook stories")
        print(f"   6. Write integration tests for composed behavior")
    elif mode == "extend":
        print(f"\n📝 Next steps for extended component:")
        print(f"   1. Review base component import in {kebab_name}.tsx")
        print(f"   2. Implement extension logic (enhance base component)")
        print(f"   3. Add new props to {kebab_name}.types.ts (extend base props)")
        print(f"   4. Import base styles and add only new variants in {kebab_name}.scss")
        print(f"   5. Document what's new vs inherited in Storybook")
        print(f"   6. Test both base and extended features")
    else:
        print(f"\n📝 Next steps:")
        print(f"   1. Implement component logic in {kebab_name}.tsx")
        print(f"   2. Define props interface in {kebab_name}.types.ts")
        print(f"   3. Add styles with CSS variables in {kebab_name}.scss")
        print(f"   4. Create Storybook stories in {kebab_name}.stories.tsx")
        print(f"   5. Write tests in {kebab_name}.test.tsx")

    print(f"   7. Export component from src/index.ts")
    print(f"   8. Run validation: lint, type-check, tests")


def main():
    parser = argparse.ArgumentParser(
        description="Scaffold a new fpkit component with all required files"
    )
    parser.add_argument(
        "component_name",
        help="Component name in PascalCase (e.g., Alert, DataTable)"
    )
    parser.add_argument(
        "--path",
        default=None,
        help="Output directory path (default: ./components/<component-name>)"
    )
    parser.add_argument(
        "--mode",
        choices=["new", "compose", "extend"],
        default="new",
        help="Scaffolding mode: new (default), compose (from existing), or extend (existing component)"
    )
    parser.add_argument(
        "--uses",
        default=None,
        help="Comma-separated list of existing components to use (e.g., 'Badge,Button')"
    )

    args = parser.parse_args()

    # Parse uses components
    uses_components = None
    if args.uses:
        uses_components = [c.strip() for c in args.uses.split(',')]

    # Determine skill directory (parent of scripts/)
    skill_dir = Path(__file__).parent.parent

    # Determine output directory
    if args.path:
        output_dir = Path(args.path)
    else:
        kebab_name = to_kebab_case(args.component_name)
        output_dir = Path.cwd() / "components" / kebab_name

    # Scaffold the component
    scaffold_component(args.component_name, output_dir, skill_dir, args.mode, uses_components)


if __name__ == "__main__":
    main()
