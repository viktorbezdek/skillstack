#!/usr/bin/env python3
"""
Extract Design Tokens from Figma MCP Output

Transforms Figma variable data (from get_variable_defs MCP tool) into
W3C Design Tokens Community Group (DTCG) compliant JSON format.

Usage:
    python extract_tokens.py \\
        --figma-data <path-to-mcp-output.json> \\
        --output-path <output-tokens.json> \\
        --token-types colors,typography,spacing \\
        --mode light

Features:
    - Converts Figma COLOR variables to W3C color tokens (sRGB)
    - Converts Figma FLOAT variables to dimension/number tokens
    - Converts Figma STRING variables to fontFamily tokens
    - Resolves variable references to W3C alias syntax
    - Handles variable modes (light/dark themes)
    - Validates output against W3C DTCG spec
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

# Import shared utilities
from utils import (
    ColorConverter,
    TokenPathUtils,
    generate_value_hash,
    ColorNameStandardizer,
    SizeStandardizer
)


class FigmaTokenExtractor:
    """Extract and transform Figma variables to W3C DTCG tokens"""

    def __init__(
        self,
        mode: Optional[str] = None,
        standardize_names: bool = False,
        name_mappings: Optional[Dict[str, Any]] = None
    ):
        self.mode = mode
        self.standardize_names = standardize_names
        self.tokens: Dict[str, Any] = {}
        self.variable_map: Dict[str, str] = {}  # Figma ID -> token path
        self.seen_values: Dict[str, str] = {}  # Value hash -> token path (for deduplication)

        # Initialize standardizers if enabled
        if standardize_names:
            color_mappings = name_mappings.get('colors', {}) if name_mappings else {}
            size_mappings = name_mappings.get('sizes', {}) if name_mappings else {}
            self.color_standardizer = ColorNameStandardizer(color_mappings or None)
            self.size_standardizer = SizeStandardizer(size_mappings or None)
        else:
            self.color_standardizer = None
            self.size_standardizer = None

    def extract(self, figma_data: Dict[str, Any], token_types: List[str]) -> Dict[str, Any]:
        """
        Extract tokens from Figma MCP data

        Args:
            figma_data: Parsed JSON from Figma get_variable_defs tool or get_design_context
            token_types: List of token types to extract (colors, typography, spacing, all)

        Returns:
            W3C DTCG compliant token dictionary
        """
        # Handle both single file and collection structures
        variables = self._extract_variables(figma_data)

        if not variables:
            print("Warning: No variables found in Figma data", file=sys.stderr)
            print("Attempting to extract tokens from selection/node styles...", file=sys.stderr)
            # Fallback: Extract from node styles if available
            if self._extract_from_nodes(figma_data, token_types):
                return self.tokens
            return {}

        # Build variable map for reference resolution
        self._build_variable_map(variables)

        # Extract token types
        if 'all' in token_types:
            self._extract_all_tokens(variables)
        else:
            if 'colors' in token_types:
                self._extract_color_tokens(variables)
            if 'typography' in token_types:
                self._extract_typography_tokens(variables)
            if 'spacing' in token_types:
                self._extract_spacing_tokens(variables)

        return self.tokens

    def _extract_variables(self, data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Extract variables list from various Figma data structures"""
        # Try different data structures
        if 'variables' in data:
            return data['variables']
        elif 'collections' in data:
            # Flatten collections
            variables = []
            for collection in data['collections']:
                if 'variables' in collection:
                    variables.extend(collection['variables'])
            return variables
        elif isinstance(data, list):
            return data
        else:
            return []

    def _build_variable_map(self, variables: List[Dict[str, Any]]):
        """Build map of Figma variable IDs to token paths"""
        for var in variables:
            var_id = var.get('id', '')
            var_name = var.get('name', '')
            if var_id and var_name:
                # Convert Figma variable name to token path
                token_path = self._figma_name_to_token_path(var_name)
                self.variable_map[var_id] = token_path

    def _figma_name_to_token_path(self, name: str) -> str:
        """
        Convert Figma variable name to W3C token path

        Figma allows dots in names (e.g., 'color.primary.500')
        W3C DTCG uses dots for nesting, so we preserve them
        """
        # Replace invalid characters
        name = re.sub(r'[^\w.\-/]', '-', name)
        return name

    def _extract_color_tokens(self, variables: List[Dict[str, Any]]):
        """Extract color tokens from COLOR type variables"""
        color_tokens = {}

        for var in variables:
            if var.get('resolvedType') == 'COLOR' or var.get('type') == 'COLOR':
                token_path = self._figma_name_to_token_path(var['name'])
                value = self._get_variable_value(var)

                if value:
                    color_tokens[token_path] = {
                        '$type': 'color',
                        '$value': self._convert_color_to_w3c(value)
                    }

                    # Add description if available
                    if var.get('description'):
                        color_tokens[token_path]['$description'] = var['description']

        if color_tokens:
            self.tokens['color'] = color_tokens

    def _extract_typography_tokens(self, variables: List[Dict[str, Any]]):
        """Extract typography tokens from STRING and FLOAT variables"""
        font_family_tokens = {}
        font_size_tokens = {}
        font_weight_tokens = {}
        line_height_tokens = {}

        for var in variables:
            var_type = var.get('resolvedType') or var.get('type')
            var_name = var['name'].lower()
            token_path = self._figma_name_to_token_path(var['name'])
            value = self._get_variable_value(var)

            if not value:
                continue

            # Font family (STRING)
            if var_type == 'STRING' and ('font' in var_name or 'family' in var_name):
                font_family_tokens[token_path] = {
                    '$type': 'fontFamily',
                    '$value': value
                }

            # Font size (FLOAT)
            elif var_type == 'FLOAT' and ('font' in var_name or 'size' in var_name):
                font_size_tokens[token_path] = {
                    '$type': 'dimension',
                    '$value': f"{value}px"
                }

            # Font weight (FLOAT)
            elif var_type == 'FLOAT' and 'weight' in var_name:
                font_weight_tokens[token_path] = {
                    '$type': 'fontWeight',
                    '$value': int(value)
                }

            # Line height (FLOAT)
            elif var_type == 'FLOAT' and ('line' in var_name or 'leading' in var_name):
                line_height_tokens[token_path] = {
                    '$type': 'number',
                    '$value': value
                }

        # Add to tokens
        if font_family_tokens:
            self.tokens.setdefault('typography', {}).update(font_family_tokens)
        if font_size_tokens:
            self.tokens.setdefault('typography', {}).update(font_size_tokens)
        if font_weight_tokens:
            self.tokens.setdefault('typography', {}).update(font_weight_tokens)
        if line_height_tokens:
            self.tokens.setdefault('typography', {}).update(line_height_tokens)

    def _extract_spacing_tokens(self, variables: List[Dict[str, Any]]):
        """Extract spacing/dimension tokens from FLOAT variables"""
        spacing_tokens = {}

        for var in variables:
            var_type = var.get('resolvedType') or var.get('type')
            var_name = var['name'].lower()

            if var_type == 'FLOAT':
                # Check if it's spacing/dimension related
                spacing_keywords = ['spacing', 'margin', 'padding', 'gap', 'size', 'width', 'height']
                is_spacing = any(keyword in var_name for keyword in spacing_keywords)

                # Exclude typography-related dimensions
                typo_keywords = ['font', 'size', 'weight', 'line', 'leading']
                is_typography = any(keyword in var_name for keyword in typo_keywords)

                if is_spacing and not is_typography:
                    token_path = self._figma_name_to_token_path(var['name'])
                    value = self._get_variable_value(var)

                    if value:
                        spacing_tokens[token_path] = {
                            '$type': 'dimension',
                            '$value': f"{value}px"
                        }

                        if var.get('description'):
                            spacing_tokens[token_path]['$description'] = var['description']

        if spacing_tokens:
            self.tokens['spacing'] = spacing_tokens

    def _extract_all_tokens(self, variables: List[Dict[str, Any]]):
        """Extract all available token types"""
        self._extract_color_tokens(variables)
        self._extract_typography_tokens(variables)
        self._extract_spacing_tokens(variables)

        # Extract other types
        other_tokens = {}

        for var in variables:
            var_type = var.get('resolvedType') or var.get('type')
            var_name = var['name'].lower()
            token_path = self._figma_name_to_token_path(var['name'])

            # Skip already processed types
            if self._is_token_processed(token_path):
                continue

            value = self._get_variable_value(var)
            if not value:
                continue

            # Handle BOOLEAN
            if var_type == 'BOOLEAN':
                other_tokens[token_path] = {
                    '$type': 'boolean',
                    '$value': value
                }

            # Handle other FLOAT (as number)
            elif var_type == 'FLOAT':
                other_tokens[token_path] = {
                    '$type': 'number',
                    '$value': value
                }

            # Handle other STRING
            elif var_type == 'STRING':
                other_tokens[token_path] = {
                    '$type': 'string',
                    '$value': value
                }

        if other_tokens:
            self.tokens['other'] = other_tokens

    def _is_token_processed(self, token_path: str) -> bool:
        """Check if token has already been processed"""
        for category in self.tokens.values():
            if token_path in category:
                return True
        return False

    def _get_variable_value(self, var: Dict[str, Any]) -> Any:
        """
        Get variable value, respecting mode if specified

        Args:
            var: Variable dictionary from Figma

        Returns:
            Value for the current mode or default value
        """
        # Check for mode-specific values
        if self.mode and 'valuesByMode' in var:
            for mode_id, mode_value in var['valuesByMode'].items():
                mode_name = var.get('modes', {}).get(mode_id, {}).get('name', '')
                if mode_name.lower() == self.mode.lower():
                    return self._process_value(mode_value, var)

        # Fall back to default value
        if 'value' in var:
            return self._process_value(var['value'], var)
        elif 'valuesByMode' in var and var['valuesByMode']:
            # Use first mode if no mode specified
            first_mode_value = list(var['valuesByMode'].values())[0]
            return self._process_value(first_mode_value, var)

        return None

    def _process_value(self, value: Any, var: Dict[str, Any]) -> Any:
        """
        Process variable value, handling references

        Args:
            value: Raw value from Figma
            var: Variable dictionary for context

        Returns:
            Processed value or reference
        """
        # Handle variable references (alias)
        if isinstance(value, dict) and value.get('type') == 'VARIABLE_ALIAS':
            ref_id = value.get('id')
            if ref_id in self.variable_map:
                return f"{{{self.variable_map[ref_id]}}}"

        # Return raw value
        return value

    def _convert_color_to_w3c(self, value: Any) -> Union[str, Dict[str, Any]]:
        """
        Convert Figma color to W3C DTCG color format

        Figma colors can be:
        - Hex string: "#FF0000"
        - RGB object: {"r": 1.0, "g": 0.0, "b": 0.0, "a": 1.0}
        - Reference: "{color.primary}"

        Returns:
        - Hex string or W3C color object
        """
        normalized = ColorConverter.normalize_color(value)
        return normalized if normalized else str(value)

    def _extract_from_nodes(self, figma_data: Dict[str, Any], token_types: List[str]) -> bool:
        """
        Extract tokens from Figma node styles when no variables exist

        Args:
            figma_data: Figma data that may contain nodes with styles
            token_types: Token types to extract

        Returns:
            True if any tokens were extracted, False otherwise
        """
        nodes = self._extract_nodes(figma_data)

        if not nodes:
            print("Warning: No nodes found in Figma data", file=sys.stderr)
            return False

        # Extract tokens from node styles
        if 'all' in token_types or 'colors' in token_types:
            self._extract_colors_from_nodes(nodes)

        if 'all' in token_types or 'typography' in token_types:
            self._extract_typography_from_nodes(nodes)

        if 'all' in token_types or 'spacing' in token_types:
            self._extract_spacing_from_nodes(nodes)

        return len(self.tokens) > 0

    def _extract_nodes(self, data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Extract nodes from various Figma data structures"""
        nodes = []

        # Check for direct node structure
        if 'document' in data and 'children' in data['document']:
            nodes = self._flatten_node_tree(data['document'])
        elif 'children' in data:
            nodes = self._flatten_node_tree(data)
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, dict):
                    nodes.extend(self._flatten_node_tree(item))

        return nodes

    def _flatten_node_tree(self, node: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Recursively flatten Figma node tree"""
        nodes = [node]

        if 'children' in node:
            for child in node['children']:
                nodes.extend(self._flatten_node_tree(child))

        return nodes

    def _extract_colors_from_nodes(self, nodes: List[Dict[str, Any]]):
        """Extract color tokens from node fills and strokes"""
        color_tokens = {}

        for node in nodes:
            node_name = node.get('name', '')

            # Extract from fills
            if 'fills' in node:
                for i, fill in enumerate(node['fills']):
                    if fill.get('type') == 'SOLID' and 'color' in fill:
                        color_value = self._convert_color_to_w3c(fill['color'])
                        token_name = self._generate_color_token_name(node_name, 'fill', i)

                        if self._add_token_with_dedup('color', token_name, color_value, color_tokens):
                            color_tokens[token_name] = {
                                '$type': 'color',
                                '$value': color_value,
                                '$description': f'Extracted from {node_name}'
                            }

            # Extract from strokes
            if 'strokes' in node:
                for i, stroke in enumerate(node['strokes']):
                    if stroke.get('type') == 'SOLID' and 'color' in stroke:
                        color_value = self._convert_color_to_w3c(stroke['color'])
                        token_name = self._generate_color_token_name(node_name, 'stroke', i)

                        if self._add_token_with_dedup('color', token_name, color_value, color_tokens):
                            color_tokens[token_name] = {
                                '$type': 'color',
                                '$value': color_value,
                                '$description': f'Extracted from {node_name} stroke'
                            }

        if color_tokens:
            self.tokens['color'] = color_tokens
            print(f"✓ Extracted {len(color_tokens)} unique color tokens from selection", file=sys.stderr)

    def _extract_typography_from_nodes(self, nodes: List[Dict[str, Any]]):
        """Extract typography tokens from text nodes"""
        typography_tokens = {}

        for node in nodes:
            if node.get('type') == 'TEXT':
                node_name = node.get('name', '')
                style = node.get('style', {})

                # Font family
                if 'fontFamily' in style:
                    token_name = f"{self._sanitize_name(node_name)}-family"
                    font_value = style['fontFamily']

                    if self._add_token_with_dedup('typography', token_name, font_value, typography_tokens):
                        typography_tokens[token_name] = {
                            '$type': 'fontFamily',
                            '$value': font_value,
                            '$description': f'Extracted from {node_name}'
                        }

                # Font size
                if 'fontSize' in style:
                    token_name = f"{self._sanitize_name(node_name)}-size"
                    size_value = f"{style['fontSize']}px"

                    if self._add_token_with_dedup('typography', token_name, size_value, typography_tokens):
                        typography_tokens[token_name] = {
                            '$type': 'dimension',
                            '$value': size_value,
                            '$description': f'Extracted from {node_name}'
                        }

                # Font weight
                if 'fontWeight' in style:
                    token_name = f"{self._sanitize_name(node_name)}-weight"
                    weight_value = int(style['fontWeight'])

                    if self._add_token_with_dedup('typography', token_name, weight_value, typography_tokens):
                        typography_tokens[token_name] = {
                            '$type': 'fontWeight',
                            '$value': weight_value,
                            '$description': f'Extracted from {node_name}'
                        }

                # Line height
                if 'lineHeightPx' in style:
                    token_name = f"{self._sanitize_name(node_name)}-line-height"
                    lh_value = style['lineHeightPx']

                    if self._add_token_with_dedup('typography', token_name, lh_value, typography_tokens):
                        typography_tokens[token_name] = {
                            '$type': 'number',
                            '$value': lh_value,
                            '$description': f'Extracted from {node_name}'
                        }

        if typography_tokens:
            self.tokens['typography'] = typography_tokens
            print(f"✓ Extracted {len(typography_tokens)} unique typography tokens from selection", file=sys.stderr)

    def _extract_spacing_from_nodes(self, nodes: List[Dict[str, Any]]):
        """Extract spacing tokens from node dimensions and constraints"""
        spacing_tokens = {}

        for node in nodes:
            node_name = node.get('name', '')

            # Padding (from constraints)
            if 'paddingLeft' in node:
                for prop in ['paddingLeft', 'paddingRight', 'paddingTop', 'paddingBottom']:
                    if prop in node:
                        token_name = f"{self._sanitize_name(node_name)}-{prop.replace('padding', '').lower()}"
                        spacing_value = f"{node[prop]}px"

                        if self._add_token_with_dedup('spacing', token_name, spacing_value, spacing_tokens):
                            spacing_tokens[token_name] = {
                                '$type': 'dimension',
                                '$value': spacing_value,
                                '$description': f'Extracted from {node_name}'
                            }

            # Item spacing (for auto-layout)
            if 'itemSpacing' in node:
                token_name = f"{self._sanitize_name(node_name)}-gap"
                spacing_value = f"{node['itemSpacing']}px"

                if self._add_token_with_dedup('spacing', token_name, spacing_value, spacing_tokens):
                    spacing_tokens[token_name] = {
                        '$type': 'dimension',
                        '$value': spacing_value,
                        '$description': f'Gap spacing from {node_name}'
                    }

        if spacing_tokens:
            self.tokens['spacing'] = spacing_tokens
            print(f"✓ Extracted {len(spacing_tokens)} unique spacing tokens from selection", file=sys.stderr)

    def _generate_color_token_name(self, node_name: str, property_type: str, index: int) -> str:
        """Generate a descriptive token name for a color"""
        base_name = self._sanitize_name(node_name)

        # Apply color name standardization if enabled
        if self.standardize_names and self.color_standardizer:
            base_name = self.color_standardizer.standardize(base_name)

        if index == 0:
            return f"{base_name}-{property_type}"
        return f"{base_name}-{property_type}-{index}"

    def _generate_size_token_name(self, base_name: str, size_type: str, value: Optional[float] = None) -> str:
        """
        Generate a descriptive token name for a size/dimension

        Args:
            base_name: Base name from Figma node
            size_type: Type of size (gap, padding, width, etc.)
            value: Optional numeric value for value-based standardization

        Returns:
            Standardized token name
        """
        sanitized_base = self._sanitize_name(base_name)

        # Apply size name standardization if enabled
        if self.standardize_names and self.size_standardizer:
            # Try name-based standardization first
            standardized = self.size_standardizer.standardize(sanitized_base)

            # If value provided and name didn't match, try value-based standardization
            if standardized == sanitized_base and value is not None:
                # Determine category from size_type
                category = 'spacing'
                if 'radius' in size_type.lower():
                    category = 'border-radius'
                elif 'font' in size_type.lower() or 'size' in size_type.lower():
                    category = 'font-size'

                standardized = self.size_standardizer.standardize_by_value(value, category)

            return f"{standardized}-{size_type}"

        return f"{sanitized_base}-{size_type}"

    def _sanitize_name(self, name: str) -> str:
        """Sanitize name for token path"""
        return TokenPathUtils.sanitize_name(name)

    def _add_token_with_dedup(self, category: str, token_name: str, value: Any, token_dict: Dict[str, Any]) -> bool:
        """
        Add token with deduplication check

        Args:
            category: Token category (color, typography, spacing)
            token_name: Proposed token name
            value: Token value
            token_dict: Dictionary to add token to

        Returns:
            True if token should be added (not a duplicate), False if duplicate
        """
        # Generate value hash for deduplication
        value_hash = self._generate_value_hash(category, value)

        # Check if we've seen this value before
        if value_hash in self.seen_values:
            existing_token = self.seen_values[value_hash]
            print(f"  Skipping duplicate: {token_name} (same value as {existing_token})", file=sys.stderr)
            return False

        # Track this value
        self.seen_values[value_hash] = token_name
        return True

    def _generate_value_hash(self, category: str, value: Any) -> str:
        """Generate hash for value deduplication"""
        return generate_value_hash(category, value)


def main():
    parser = argparse.ArgumentParser(
        description='Extract design tokens from Figma MCP output to W3C DTCG format'
    )
    parser.add_argument(
        '--figma-data',
        required=True,
        type=Path,
        help='Path to JSON file from Figma get_variable_defs MCP tool'
    )
    parser.add_argument(
        '--output-path',
        required=True,
        type=Path,
        help='Path for output W3C DTCG JSON file'
    )
    parser.add_argument(
        '--token-types',
        default='all',
        help='Comma-separated token types to extract (colors, typography, spacing, all). Default: all'
    )
    parser.add_argument(
        '--mode',
        help='Figma variable mode to extract (e.g., light, dark). If omitted, uses default mode.'
    )
    parser.add_argument(
        '--pretty',
        action='store_true',
        help='Pretty-print JSON output with indentation'
    )
    parser.add_argument(
        '--standardize-names',
        action='store_true',
        help='Standardize token names to semantic conventions (e.g., primary, secondary, xs, sm, md)'
    )
    parser.add_argument(
        '--name-mappings',
        type=Path,
        help='Path to JSON file with custom name mappings for colors and sizes'
    )

    args = parser.parse_args()

    # Validate input file exists
    if not args.figma_data.exists():
        print(f"Error: Input file not found: {args.figma_data}", file=sys.stderr)
        sys.exit(1)

    # Parse token types
    token_types = [t.strip() for t in args.token_types.split(',')]

    # Load custom name mappings if provided
    name_mappings = None
    if args.name_mappings:
        if not args.name_mappings.exists():
            print(f"Error: Name mappings file not found: {args.name_mappings}", file=sys.stderr)
            sys.exit(1)
        try:
            with open(args.name_mappings, 'r', encoding='utf-8') as f:
                name_mappings = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON in name mappings file: {e}", file=sys.stderr)
            sys.exit(1)

    try:
        # Load Figma data
        with open(args.figma_data, 'r', encoding='utf-8') as f:
            figma_data = json.load(f)

        # Extract tokens
        extractor = FigmaTokenExtractor(
            mode=args.mode,
            standardize_names=args.standardize_names,
            name_mappings=name_mappings
        )
        tokens = extractor.extract(figma_data, token_types)

        if not tokens:
            print("Warning: No tokens extracted. Check input data and token types.", file=sys.stderr)

        # Write output
        args.output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(args.output_path, 'w', encoding='utf-8') as f:
            if args.pretty:
                json.dump(tokens, f, indent=2, ensure_ascii=False)
            else:
                json.dump(tokens, f, ensure_ascii=False)

        print(f"✓ Extracted {sum(len(v) for v in tokens.values())} tokens to {args.output_path}")
        print(f"  Categories: {', '.join(tokens.keys())}")

        if args.mode:
            print(f"  Mode: {args.mode}")

    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in input file: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
