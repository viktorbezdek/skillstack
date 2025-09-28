#!/usr/bin/env python3
"""
Component Catalog Analyzer for fpkit

Scans the fpkit component library and builds a comprehensive catalog of available components,
their exports, features, and metadata for intelligent component reuse.

Usage:
    python3 analyze_components.py [--components-dir <path>] [--output <file>]

Options:
    --components-dir    Path to components directory (default: packages/fpkit/src/components)
    --output           Output JSON file (default: stdout)
    --verbose          Show detailed scanning progress
"""

import os
import re
import json
import argparse
from pathlib import Path
from typing import Dict, List, Optional, Set, Any


class ComponentAnalyzer:
    """Analyzes fpkit components and builds a searchable catalog."""

    def __init__(self, components_dir: Path, verbose: bool = False):
        self.components_dir = components_dir
        self.verbose = verbose
        self.catalog = {}

    def log(self, message: str):
        """Print message if verbose mode is enabled."""
        if self.verbose:
            print(f"[Analyzer] {message}")

    def scan_components(self) -> Dict[str, Any]:
        """Scan all components and build catalog."""
        self.log(f"Scanning components in: {self.components_dir}")

        if not self.components_dir.exists():
            raise FileNotFoundError(f"Components directory not found: {self.components_dir}")

        # Iterate through component directories
        for component_dir in sorted(self.components_dir.iterdir()):
            if not component_dir.is_dir() or component_dir.name.startswith('.'):
                continue

            component_name = self._infer_component_name(component_dir)
            if component_name:
                self.log(f"Analyzing: {component_name}")
                self.catalog[component_name] = self._analyze_component(component_dir, component_name)

        return {
            "total_components": len(self.catalog),
            "scan_path": str(self.components_dir),
            "components": self.catalog
        }

    def _infer_component_name(self, component_dir: Path) -> Optional[str]:
        """Infer component name from directory or main file."""
        # Try to find main component file
        tsx_files = list(component_dir.glob("*.tsx"))

        # Exclude stories and test files
        component_files = [
            f for f in tsx_files
            if not f.stem.endswith('.stories')
            and not f.stem.endswith('.test')
        ]

        if not component_files:
            return None

        # Use the directory name as base
        return self._to_pascal_case(component_dir.name)

    def _analyze_component(self, component_dir: Path, component_name: str) -> Dict[str, Any]:
        """Analyze a single component directory."""
        main_file = self._find_main_file(component_dir, component_name)

        metadata = {
            "name": component_name,
            "path": str(component_dir.relative_to(self.components_dir.parent.parent.parent)),
            "files": self._get_component_files(component_dir),
            "exports": [],
            "props_interface": None,
            "features": [],
            "variants": [],
            "complexity": "simple",
            "uses_ui_component": False,
            "sub_components": [],
            "dependencies": []
        }

        if main_file and main_file.exists():
            content = main_file.read_text()
            metadata.update(self._analyze_source_code(content, component_name))

        # Analyze SCSS for variants
        scss_file = component_dir / f"{component_dir.name}.scss"
        if scss_file.exists():
            scss_content = scss_file.read_text()
            metadata["variants"] = self._extract_scss_variants(scss_content)

        # Determine complexity
        metadata["complexity"] = self._determine_complexity(component_dir, metadata)

        return metadata

    def _find_main_file(self, component_dir: Path, component_name: str) -> Optional[Path]:
        """Find the main component file."""
        # Try exact name match
        exact_match = component_dir / f"{component_dir.name}.tsx"
        if exact_match.exists():
            return exact_match

        # Try lowercase
        lowercase = component_dir / f"{component_dir.name.lower()}.tsx"
        if lowercase.exists():
            return lowercase

        # Try finding any .tsx that's not stories/test
        for tsx_file in component_dir.glob("*.tsx"):
            if not tsx_file.stem.endswith(('.stories', '.test')):
                return tsx_file

        return None

    def _get_component_files(self, component_dir: Path) -> Dict[str, bool]:
        """Check which standard files exist."""
        base_name = component_dir.name
        return {
            "component": any(component_dir.glob(f"{base_name}*.tsx")),
            "types": (component_dir / f"{base_name}.types.ts").exists(),
            "styles": (component_dir / f"{base_name}.scss").exists(),
            "stories": (component_dir / f"{base_name}.stories.tsx").exists(),
            "tests": (component_dir / f"{base_name}.test.tsx").exists(),
            "readme": (component_dir / "README.mdx").exists() or (component_dir / "README.md").exists(),
            "accessibility": (component_dir / "ACCESSIBILITY.md").exists(),
            "has_views": (component_dir / "views").exists(),
            "has_elements": (component_dir / "elements").exists()
        }

    def _analyze_source_code(self, content: str, component_name: str) -> Dict[str, Any]:
        """Extract metadata from component source code."""
        metadata = {
            "exports": [],
            "props_interface": None,
            "features": [],
            "uses_ui_component": False,
            "sub_components": [],
            "dependencies": []
        }

        # Find exports
        export_pattern = r'export\s+(?:const|function|class|type|interface)\s+(\w+)'
        exports = re.findall(export_pattern, content)
        metadata["exports"] = list(set(exports))

        # Find props interface
        props_pattern = rf'(?:interface|type)\s+({component_name}Props)'
        props_match = re.search(props_pattern, content)
        if props_match:
            metadata["props_interface"] = props_match.group(1)

        # Check for UI component usage
        if re.search(r'from\s+[\'"]#components/ui[\'"]', content) or \
           re.search(r'<UI\s+', content):
            metadata["uses_ui_component"] = True

        # Extract JSDoc features
        jsdoc_pattern = r'/\*\*\s*\n\s*\*\s*@features?\s+(.*?)\n'
        features = re.findall(jsdoc_pattern, content)
        metadata["features"] = [f.strip() for f in features]

        # Find sub-components (capitalized imports from local files)
        local_import_pattern = r'import\s+\{([^}]+)\}\s+from\s+[\'"]\./'
        for match in re.finditer(local_import_pattern, content):
            imports = [i.strip() for i in match.group(1).split(',')]
            capitalized = [i for i in imports if i and i[0].isupper()]
            metadata["sub_components"].extend(capitalized)

        # Find external dependencies (from fpkit components)
        component_import_pattern = r'from\s+[\'"]\.\./(\w+)/'
        deps = re.findall(component_import_pattern, content)
        metadata["dependencies"] = list(set(deps))

        return metadata

    def _extract_scss_variants(self, scss_content: str) -> List[str]:
        """Extract variant names from SCSS attribute selectors."""
        variants = []

        # Match patterns like: [data-component~="primary"]
        variant_pattern = r'\[data-\w+~=[\'"]([\w-]+)[\'"]\]'
        matches = re.findall(variant_pattern, scss_content)
        variants.extend(matches)

        # Match CSS variable patterns that include variant names
        # e.g., --component-primary-bg
        var_variant_pattern = r'--\w+-(primary|secondary|success|error|warning|info|danger|light|dark)'
        var_matches = re.findall(var_variant_pattern, scss_content)
        variants.extend(var_matches)

        return list(set(variants))

    def _determine_complexity(self, component_dir: Path, metadata: Dict[str, Any]) -> str:
        """Determine component complexity level."""
        score = 0

        # Check for sub-directories
        if metadata["files"]["has_views"]:
            score += 2
        if metadata["files"]["has_elements"]:
            score += 2

        # Check for sub-components
        if metadata["sub_components"]:
            score += len(metadata["sub_components"])

        # Check for dependencies
        if metadata["dependencies"]:
            score += len(metadata["dependencies"])

        # Check for multiple exports
        if len(metadata["exports"]) > 3:
            score += 1

        # Check file count
        tsx_files = list(component_dir.glob("**/*.tsx"))
        if len(tsx_files) > 3:
            score += 1

        if score == 0:
            return "simple"
        elif score <= 3:
            return "moderate"
        else:
            return "complex"

    def _to_pascal_case(self, text: str) -> str:
        """Convert text to PascalCase."""
        # Split on hyphens, underscores, and spaces
        words = re.split(r'[-_\s]+', text)
        return ''.join(word.capitalize() for word in words if word)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Analyze fpkit components and build a catalog"
    )
    parser.add_argument(
        "--components-dir",
        type=Path,
        default=Path("packages/fpkit/src/components"),
        help="Path to components directory"
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Output JSON file (default: stdout)"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show detailed scanning progress"
    )

    args = parser.parse_args()

    # Resolve path relative to current working directory
    components_dir = args.components_dir
    if not components_dir.is_absolute():
        components_dir = Path.cwd() / components_dir

    # Create analyzer and scan
    analyzer = ComponentAnalyzer(components_dir, verbose=args.verbose)
    catalog = analyzer.scan_components()

    # Output results
    json_output = json.dumps(catalog, indent=2)

    if args.output:
        args.output.write_text(json_output)
        print(f"✓ Catalog saved to: {args.output}")
        print(f"✓ Found {catalog['total_components']} components")
    else:
        print(json_output)


if __name__ == "__main__":
    main()
