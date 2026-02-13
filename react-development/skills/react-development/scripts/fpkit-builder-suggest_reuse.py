#!/usr/bin/env python3
"""
Component Reuse Suggestion Engine for fpkit

Analyzes requested component names against the existing component catalog to suggest
opportunities for reuse through composition or extension.

Usage:
    python3 suggest_reuse.py <ComponentName> [--catalog <file>] [--threshold <0-100>]

Options:
    --catalog      Path to component catalog JSON (default: auto-generate)
    --threshold    Minimum similarity score to report (default: 30)
    --verbose      Show detailed analysis
"""

import os
import re
import json
import argparse
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Set
import difflib


class ComponentReuseSuggester:
    """Suggests component reuse opportunities based on name analysis and catalog lookup."""

    # Common UI primitives that are frequently composable
    UI_PRIMITIVES = {
        'UI', 'Button', 'Badge', 'Icon', 'Link', 'Text', 'Heading', 'Title',
        'Image', 'List', 'ListItem', 'Nav', 'Tag'
    }

    # Common component patterns and their typical building blocks
    COMPOSITE_PATTERNS = {
        'Dialog': ['Modal', 'Card'],
        'Modal': ['Dialog', 'Overlay'],
        'Dropdown': ['Button', 'List', 'Popover'],
        'Menu': ['Nav', 'List'],
        'Toast': ['Alert', 'Badge'],
        'Notification': ['Alert', 'Icon'],
        'Card': ['Title', 'Content', 'Footer'],
        'Form': ['Input', 'Button', 'Label'],
    }

    def __init__(self, catalog: Dict, verbose: bool = False):
        self.catalog = catalog
        self.verbose = verbose
        self.components = catalog.get('components', {})

    def log(self, message: str):
        """Print message if verbose mode is enabled."""
        if self.verbose:
            print(f"[Suggester] {message}")

    def suggest_reuse(self, component_name: str, threshold: int = 30) -> Dict:
        """Analyze component name and suggest reuse opportunities."""
        self.log(f"Analyzing: {component_name}")

        suggestions = {
            "requested": component_name,
            "exact_match": self._check_exact_match(component_name),
            "similar_components": self._find_similar_components(component_name, threshold),
            "composite_parts": self._detect_composite_parts(component_name),
            "recommended_building_blocks": self._recommend_building_blocks(component_name),
            "ui_primitives": self._suggest_ui_primitives(),
            "summary": {}
        }

        # Generate summary
        suggestions["summary"] = self._generate_summary(suggestions)

        return suggestions

    def _check_exact_match(self, component_name: str) -> Optional[Dict]:
        """Check if a component with this exact name already exists."""
        if component_name in self.components:
            self.log(f"✓ Exact match found: {component_name}")
            return {
                "exists": True,
                "component": self.components[component_name],
                "recommendation": "extend_existing"
            }
        return {"exists": False}

    def _find_similar_components(self, component_name: str, threshold: int) -> List[Dict]:
        """Find components with similar names using string similarity."""
        similar = []

        for existing_name, metadata in self.components.items():
            # Calculate similarity score
            ratio = difflib.SequenceMatcher(None, component_name.lower(), existing_name.lower()).ratio()
            score = int(ratio * 100)

            if score >= threshold and score < 100:  # Exclude exact matches
                similar.append({
                    "name": existing_name,
                    "similarity_score": score,
                    "path": metadata.get("path"),
                    "complexity": metadata.get("complexity"),
                    "variants": metadata.get("variants", [])
                })

        # Sort by similarity score
        similar.sort(key=lambda x: x["similarity_score"], reverse=True)

        self.log(f"Found {len(similar)} similar components")
        return similar

    def _detect_composite_parts(self, component_name: str) -> List[Dict]:
        """Detect if the component name is a composite of existing components."""
        parts = []

        # Split camelCase/PascalCase into words
        words = self._split_component_name(component_name)
        self.log(f"Split into words: {words}")

        # Check each word against existing components
        for word in words:
            if word in self.components:
                parts.append({
                    "word": word,
                    "component": self.components[word],
                    "confidence": "high"
                })
            else:
                # Check for partial matches
                for existing_name in self.components.keys():
                    if word.lower() in existing_name.lower():
                        parts.append({
                            "word": word,
                            "component": self.components[existing_name],
                            "confidence": "medium"
                        })
                        break

        return parts

    def _recommend_building_blocks(self, component_name: str) -> List[Dict]:
        """Recommend existing components that could be building blocks."""
        recommendations = []

        # Check composite patterns
        for pattern, typical_blocks in self.COMPOSITE_PATTERNS.items():
            if pattern.lower() in component_name.lower():
                for block in typical_blocks:
                    if block in self.components:
                        recommendations.append({
                            "component": block,
                            "reason": f"Typically used in {pattern} components",
                            "metadata": self.components[block],
                            "confidence": "high"
                        })

        # Check for UI primitives
        for primitive in self.UI_PRIMITIVES:
            if primitive in self.components and primitive not in [r["component"] for r in recommendations]:
                # Suggest common primitives as potential building blocks
                recommendations.append({
                    "component": primitive,
                    "reason": "Common UI primitive for composition",
                    "metadata": self.components[primitive],
                    "confidence": "medium"
                })

        # Remove duplicates and limit to top recommendations
        seen = set()
        unique_recommendations = []
        for rec in recommendations:
            if rec["component"] not in seen:
                seen.add(rec["component"])
                unique_recommendations.append(rec)

        return unique_recommendations[:8]  # Limit to top 8

    def _suggest_ui_primitives(self) -> List[str]:
        """Return list of available UI primitives."""
        primitives = []
        for name in self.components.keys():
            if name in self.UI_PRIMITIVES:
                primitives.append(name)
        return primitives

    def _split_component_name(self, name: str) -> List[str]:
        """Split PascalCase/camelCase component name into words."""
        # Insert space before uppercase letters
        spaced = re.sub(r'([A-Z])', r' \1', name).strip()
        # Split on spaces
        words = spaced.split()
        return words

    def _generate_summary(self, suggestions: Dict) -> Dict:
        """Generate actionable summary of suggestions."""
        summary = {
            "action": "create_new",
            "confidence": "low",
            "reasoning": [],
            "next_steps": []
        }

        # Check exact match
        if suggestions["exact_match"]["exists"]:
            summary["action"] = "extend_existing"
            summary["confidence"] = "high"
            summary["reasoning"].append(f"Component '{suggestions['requested']}' already exists")
            summary["next_steps"].append(f"Consider adding variant or extending existing component")
            return summary

        # Check composite parts
        if len(suggestions["composite_parts"]) >= 2:
            summary["action"] = "compose"
            summary["confidence"] = "high"
            components = [p["word"] for p in suggestions["composite_parts"]]
            summary["reasoning"].append(f"Name suggests composition of: {', '.join(components)}")
            summary["next_steps"].append(f"Import and compose: {', '.join(components)}")

        # Check similar components
        if suggestions["similar_components"] and suggestions["similar_components"][0]["similarity_score"] > 70:
            similar = suggestions["similar_components"][0]
            summary["action"] = "review_similar"
            summary["confidence"] = "medium"
            summary["reasoning"].append(f"Similar component exists: {similar['name']} ({similar['similarity_score']}% match)")
            summary["next_steps"].append(f"Review {similar['name']} before creating new component")

        # Check building blocks
        if suggestions["recommended_building_blocks"]:
            high_confidence = [b for b in suggestions["recommended_building_blocks"] if b["confidence"] == "high"]
            if high_confidence:
                summary["action"] = "compose_with_recommendations"
                summary["confidence"] = "medium"
                components = [b["component"] for b in high_confidence[:3]]
                summary["reasoning"].append(f"Recommended building blocks: {', '.join(components)}")
                summary["next_steps"].append(f"Consider composing with: {', '.join(components)}")

        # Default to create new if no strong suggestions
        if summary["confidence"] == "low":
            summary["reasoning"].append("No existing components found for reuse")
            summary["next_steps"].append("Scaffold new component using templates")
            if suggestions["ui_primitives"]:
                summary["next_steps"].append(f"Consider using UI primitive as base")

        return summary


def load_catalog(catalog_path: Optional[Path] = None) -> Dict:
    """Load component catalog from file or generate it."""
    if catalog_path and catalog_path.exists():
        return json.loads(catalog_path.read_text())

    # Try to generate catalog on the fly
    from pathlib import Path
    import subprocess
    import sys

    analyzer_script = Path(__file__).parent / "analyze_components.py"

    if analyzer_script.exists():
        print("[Suggester] Generating component catalog...")
        result = subprocess.run(
            [sys.executable, str(analyzer_script)],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            return json.loads(result.stdout)

    # Return empty catalog if generation fails
    return {"total_components": 0, "components": {}}


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Suggest component reuse opportunities"
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
        "--threshold",
        type=int,
        default=30,
        help="Minimum similarity score (0-100, default: 30)"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show detailed analysis"
    )

    args = parser.parse_args()

    # Load catalog
    catalog = load_catalog(args.catalog)

    # Create suggester and analyze
    suggester = ComponentReuseSuggester(catalog, verbose=args.verbose)
    suggestions = suggester.suggest_reuse(args.component_name, args.threshold)

    # Output results
    print(json.dumps(suggestions, indent=2))


if __name__ == "__main__":
    main()
