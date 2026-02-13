#!/usr/bin/env python3
"""
Component Development Approach Recommender for fpkit

Analyzes component requests and recommends the best approach: compose, extend, or scaffold new.
Provides detailed reasoning and actionable next steps.

Usage:
    python3 recommend_approach.py <ComponentName> [--catalog <file>] [--format <text|json>]

Options:
    --catalog    Path to component catalog JSON (default: auto-generate)
    --format     Output format: text or json (default: text)
    --verbose    Show detailed analysis
"""

import os
import re
import json
import argparse
from pathlib import Path
from typing import Dict, List, Optional
import subprocess
import sys


class ApproachRecommender:
    """Recommends the best development approach for a component."""

    def __init__(self, catalog: Dict, verbose: bool = False):
        self.catalog = catalog
        self.verbose = verbose
        self.components = catalog.get('components', {})

    def log(self, message: str):
        """Print message if verbose mode is enabled."""
        if self.verbose:
            print(f"[Recommender] {message}", file=sys.stderr)

    def recommend(self, component_name: str) -> Dict:
        """Analyze component and recommend development approach."""
        self.log(f"Analyzing approach for: {component_name}")

        # Get suggestions from reuse analyzer
        suggestions = self._get_reuse_suggestions(component_name)

        # Apply decision heuristics
        recommendation = self._apply_heuristics(component_name, suggestions)

        # Enrich with actionable steps
        recommendation["steps"] = self._generate_steps(recommendation)

        # Add example code if composing
        if recommendation["approach"] == "compose":
            recommendation["example"] = self._generate_composition_example(
                component_name,
                recommendation.get("components_to_use", [])
            )

        return recommendation

    def _get_reuse_suggestions(self, component_name: str) -> Dict:
        """Get suggestions from suggest_reuse.py script."""
        script_path = Path(__file__).parent / "suggest_reuse.py"

        if not script_path.exists():
            self.log("Warning: suggest_reuse.py not found")
            return {"summary": {"action": "create_new"}}

        try:
            result = subprocess.run(
                [sys.executable, str(script_path), component_name],
                capture_output=True,
                text=True,
                timeout=10
            )

            if result.returncode == 0:
                return json.loads(result.stdout)
        except Exception as e:
            self.log(f"Error running suggest_reuse.py: {e}")

        return {"summary": {"action": "create_new"}}

    def _apply_heuristics(self, component_name: str, suggestions: Dict) -> Dict:
        """Apply decision heuristics to determine best approach."""
        summary = suggestions.get("summary", {})
        action = summary.get("action", "create_new")

        recommendation = {
            "component_name": component_name,
            "approach": "scaffold",  # Default
            "confidence": "low",
            "reasoning": [],
            "components_to_use": [],
            "warnings": [],
            "alternatives": []
        }

        # Heuristic 1: Exact match exists
        if suggestions.get("exact_match", {}).get("exists"):
            recommendation["approach"] = "extend"
            recommendation["confidence"] = "high"
            recommendation["reasoning"].append(
                f"⚠️  Component '{component_name}' already exists"
            )
            recommendation["reasoning"].append(
                "Consider adding a new variant or prop instead of duplicating"
            )
            recommendation["warnings"].append(
                "Creating a duplicate component may cause confusion"
            )
            recommendation["alternatives"] = [
                "Add variant to existing component",
                "Create subcomponent with different name",
                "Extend existing component with new features"
            ]
            return recommendation

        # Heuristic 2: Composite parts detected (2+ existing components in name)
        composite_parts = suggestions.get("composite_parts", [])
        if len(composite_parts) >= 2:
            recommendation["approach"] = "compose"
            recommendation["confidence"] = "high"
            components = [p["word"] for p in composite_parts[:3]]
            recommendation["components_to_use"] = components
            recommendation["reasoning"].append(
                f"✓ Component name suggests composition: {' + '.join(components)}"
            )
            recommendation["reasoning"].append(
                "These components already exist and can be combined"
            )
            return recommendation

        # Heuristic 3: High similarity to existing component
        similar = suggestions.get("similar_components", [])
        if similar and similar[0]["similarity_score"] > 75:
            similar_component = similar[0]
            recommendation["approach"] = "review_then_decide"
            recommendation["confidence"] = "medium"
            recommendation["reasoning"].append(
                f"⚠️  Very similar component exists: {similar_component['name']} "
                f"({similar_component['similarity_score']}% match)"
            )
            recommendation["reasoning"].append(
                "Review existing component before creating new one"
            )
            recommendation["alternatives"] = [
                f"Add variant to {similar_component['name']}",
                f"Extend {similar_component['name']}",
                "Create new component if truly different"
            ]
            return recommendation

        # Heuristic 4: Recommended building blocks found
        building_blocks = suggestions.get("recommended_building_blocks", [])
        high_confidence_blocks = [
            b for b in building_blocks
            if b.get("confidence") == "high"
        ]

        if high_confidence_blocks:
            recommendation["approach"] = "compose"
            recommendation["confidence"] = "medium"
            components = [b["component"] for b in high_confidence_blocks[:3]]
            recommendation["components_to_use"] = components
            recommendation["reasoning"].append(
                f"✓ Recommended building blocks: {', '.join(components)}"
            )
            for block in high_confidence_blocks[:3]:
                recommendation["reasoning"].append(
                    f"  - {block['component']}: {block['reason']}"
                )
            return recommendation

        # Heuristic 5: UI primitive available
        ui_primitives = suggestions.get("ui_primitives", [])
        if "UI" in ui_primitives:
            recommendation["approach"] = "scaffold"
            recommendation["confidence"] = "high"
            recommendation["components_to_use"] = ["UI"]
            recommendation["reasoning"].append(
                "✓ No existing components to reuse"
            )
            recommendation["reasoning"].append(
                "✓ Use UI primitive as base component"
            )
            recommendation["reasoning"].append(
                "Create new component with proper patterns"
            )
            return recommendation

        # Heuristic 6: No reuse opportunities (truly novel component)
        recommendation["approach"] = "scaffold"
        recommendation["confidence"] = "medium"
        recommendation["reasoning"].append(
            "✓ No existing components found for reuse"
        )
        recommendation["reasoning"].append(
            "Scaffold new component using best practices"
        )

        return recommendation

    def _generate_steps(self, recommendation: Dict) -> List[str]:
        """Generate actionable next steps based on recommendation."""
        approach = recommendation["approach"]
        component_name = recommendation["component_name"]
        components = recommendation.get("components_to_use", [])

        if approach == "extend":
            return [
                f"1. Review existing {component_name} component implementation",
                f"2. Identify what new feature/variant you need",
                f"3. Add new props or variant to existing component",
                f"4. Update types, styles, and tests",
                f"5. Document new variant in Storybook stories"
            ]

        elif approach == "compose":
            imports = ", ".join(components)
            return [
                f"1. Import required components: {imports}",
                f"2. Create new component file: {self._to_kebab(component_name)}.tsx",
                f"3. Compose using imported components",
                f"4. Add minimal custom styles if needed",
                f"5. Create Storybook story showing composition",
                f"6. Write tests for composed behavior"
            ]

        elif approach == "review_then_decide":
            return [
                f"1. Review the similar existing component",
                f"2. Determine if a variant would suffice",
                f"3. If truly different, proceed with scaffolding",
                f"4. Document why new component is needed"
            ]

        else:  # scaffold
            return [
                f"1. Run scaffold command with UI primitive",
                f"2. Implement component logic and props",
                f"3. Create SCSS with CSS variables (rem units)",
                f"4. Write comprehensive Storybook stories",
                f"5. Add accessibility tests (WCAG 2.1 AA)",
                f"6. Validate with linting and type-checking"
            ]

    def _generate_composition_example(self, component_name: str, components: List[str]) -> str:
        """Generate example code for composition."""
        kebab_name = self._to_kebab(component_name)
        imports = []
        for comp in components[:3]:
            kebab_comp = self._to_kebab(comp)
            # Guess the import path
            imports.append(f"import {{ {comp} }} from '../{kebab_comp}/{kebab_comp}'")

        imports_str = "\n".join(imports)

        return f"""// {kebab_name}.tsx
import * as React from 'react'
{imports_str}

export interface {component_name}Props {{
  children?: React.ReactNode
  // Add your custom props here
}}

/**
 * {component_name} - Composed from existing fpkit components
 *
 * This component combines {', '.join(components)} to create a new UI pattern.
 */
export const {component_name} = ({{ children, ...props }}: {component_name}Props) => {{
  return (
    <div data-{kebab_name} {{...props}}>
      {{/* Compose your component here using: {', '.join(components)} */}}
      {{children}}
    </div>
  )
}}

{component_name}.displayName = '{component_name}'
"""

    def _to_kebab(self, text: str) -> str:
        """Convert PascalCase to kebab-case."""
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1-\2', text)
        return re.sub('([a-z0-9])([A-Z])', r'\1-\2', s1).lower()

    def format_output(self, recommendation: Dict, format_type: str = "text") -> str:
        """Format recommendation for output."""
        if format_type == "json":
            return json.dumps(recommendation, indent=2)

        # Text format - human-readable
        lines = []
        lines.append("=" * 70)
        lines.append(f"  Component Development Recommendation: {recommendation['component_name']}")
        lines.append("=" * 70)
        lines.append("")

        # Approach
        approach_map = {
            "compose": "🔧 COMPOSE from existing components",
            "extend": "📝 EXTEND existing component",
            "scaffold": "⚡ SCAFFOLD new component",
            "review_then_decide": "👀 REVIEW FIRST, then decide"
        }
        lines.append(f"Recommended Approach: {approach_map.get(recommendation['approach'], recommendation['approach'])}")
        lines.append(f"Confidence: {recommendation['confidence'].upper()}")
        lines.append("")

        # Reasoning
        if recommendation["reasoning"]:
            lines.append("Reasoning:")
            for reason in recommendation["reasoning"]:
                lines.append(f"  {reason}")
            lines.append("")

        # Components to use
        if recommendation.get("components_to_use"):
            lines.append(f"Components to use: {', '.join(recommendation['components_to_use'])}")
            lines.append("")

        # Warnings
        if recommendation.get("warnings"):
            lines.append("⚠️  Warnings:")
            for warning in recommendation["warnings"]:
                lines.append(f"  {warning}")
            lines.append("")

        # Alternatives
        if recommendation.get("alternatives"):
            lines.append("Alternatives to consider:")
            for i, alt in enumerate(recommendation["alternatives"], 1):
                lines.append(f"  {i}. {alt}")
            lines.append("")

        # Next steps
        if recommendation.get("steps"):
            lines.append("Next Steps:")
            for step in recommendation["steps"]:
                lines.append(f"  {step}")
            lines.append("")

        # Example code
        if recommendation.get("example"):
            lines.append("Example Code:")
            lines.append("-" * 70)
            lines.append(recommendation["example"])
            lines.append("-" * 70)

        lines.append("")
        return "\n".join(lines)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Recommend component development approach"
    )
    parser.add_argument(
        "component_name",
        help="Name of the component to analyze"
    )
    parser.add_argument(
        "--catalog",
        type=Path,
        help="Path to component catalog JSON (default: auto-generate)"
    )
    parser.add_argument(
        "--format",
        choices=["text", "json"],
        default="text",
        help="Output format (default: text)"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show detailed analysis"
    )

    args = parser.parse_args()

    # Load catalog (reuse logic from suggest_reuse.py)
    catalog = {"total_components": 0, "components": {}}
    if args.catalog and args.catalog.exists():
        catalog = json.loads(args.catalog.read_text())

    # Create recommender and analyze
    recommender = ApproachRecommender(catalog, verbose=args.verbose)
    recommendation = recommender.recommend(args.component_name)

    # Output results
    output = recommender.format_output(recommendation, args.format)
    print(output)


if __name__ == "__main__":
    main()
