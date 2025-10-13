#!/usr/bin/env python3
"""
Shared utilities for figma-design-tokens scripts

Provides common functionality used across extract, transform, and validate scripts:
- Naming convention transformations
- Value formatting
- Token path utilities
"""

import re
from typing import Any, Union


class NamingConvention:
    """Apply naming conventions to token names"""

    @staticmethod
    def to_kebab_case(name: str) -> str:
        """
        Convert to kebab-case: color-primary-500

        Args:
            name: Token name to convert

        Returns:
            kebab-case formatted name
        """
        name = re.sub(r'[./]', '-', name)
        name = re.sub(r'([a-z])([A-Z])', r'\1-\2', name)
        return name.lower()

    @staticmethod
    def to_camel_case(name: str) -> str:
        """
        Convert to camelCase: colorPrimary500

        Args:
            name: Token name to convert

        Returns:
            camelCase formatted name
        """
        name = re.sub(r'[./]', '-', name)
        parts = name.split('-')
        return parts[0].lower() + ''.join(p.capitalize() for p in parts[1:])

    @staticmethod
    def to_snake_case(name: str) -> str:
        """
        Convert to snake_case: color_primary_500

        Args:
            name: Token name to convert

        Returns:
            snake_case formatted name
        """
        name = re.sub(r'[./]', '_', name)
        name = re.sub(r'([a-z])([A-Z])', r'\1_\2', name)
        return name.lower()

    @staticmethod
    def to_bem(name: str) -> str:
        """
        Convert to BEM: color__primary--500

        Args:
            name: Token name to convert

        Returns:
            BEM formatted name
        """
        parts = name.replace('.', '-').replace('/', '-').split('-')
        if len(parts) >= 3:
            return f"{parts[0]}__{parts[1]}--{'-'.join(parts[2:])}"
        elif len(parts) == 2:
            return f"{parts[0]}__{parts[1]}"
        return parts[0]

    @classmethod
    def apply(cls, name: str, convention: str) -> str:
        """
        Apply specified naming convention

        Args:
            name: Token name to convert
            convention: Convention to apply (kebab-case, camelCase, snake_case, bem)

        Returns:
            Converted name using specified convention
        """
        conventions = {
            'kebab-case': cls.to_kebab_case,
            'camelCase': cls.to_camel_case,
            'snake_case': cls.to_snake_case,
            'bem': cls.to_bem,
        }
        converter = conventions.get(convention, cls.to_kebab_case)
        return converter(name)


class ValueFormatter:
    """Format token values for different output formats"""

    @staticmethod
    def to_css_value(value: Any, naming_convention: str = 'kebab-case') -> str:
        """
        Format token value for CSS

        Args:
            value: Token value to format
            naming_convention: Convention for reference names

        Returns:
            CSS-formatted value
        """
        if isinstance(value, str):
            # Handle references
            if value.startswith('{') and value.endswith('}'):
                ref_path = value[1:-1]
                var_name = NamingConvention.apply(ref_path, naming_convention)
                return f"var(--{var_name})"
            return value
        elif isinstance(value, dict):
            # Composite values - return as JSON for now
            import json
            return json.dumps(value)
        else:
            return str(value)

    @staticmethod
    def to_scss_value(value: Any, naming_convention: str = 'kebab-case') -> str:
        """
        Format token value for SCSS

        Args:
            value: Token value to format
            naming_convention: Convention for reference names

        Returns:
            SCSS-formatted value
        """
        if isinstance(value, str):
            # Handle references
            if value.startswith('{') and value.endswith('}'):
                ref_path = value[1:-1]
                var_name = NamingConvention.apply(ref_path, naming_convention)
                return f"${var_name}"
            return value
        elif isinstance(value, dict):
            import json
            return json.dumps(value)
        else:
            return str(value)


class ColorConverter:
    """Convert colors between different formats"""

    @staticmethod
    def rgb_to_hex(r: float, g: float, b: float, a: float = 1.0) -> str:
        """
        Convert RGB values (0-1 range) to hex color

        Args:
            r: Red component (0-1)
            g: Green component (0-1)
            b: Blue component (0-1)
            a: Alpha component (0-1)

        Returns:
            Hex color string (#RRGGBB or rgba())
        """
        # Convert to 0-255 range
        r_255 = round(r * 255)
        g_255 = round(g * 255)
        b_255 = round(b * 255)

        # Return hex if fully opaque, rgba if transparent
        if a == 1:
            return f"#{r_255:02x}{g_255:02x}{b_255:02x}"
        else:
            return f"rgba({r_255}, {g_255}, {b_255}, {a})"

    @staticmethod
    def normalize_color(value: Any) -> Union[str, None]:
        """
        Normalize color value to standard format

        Args:
            value: Color value (hex, rgb object, or string)

        Returns:
            Normalized color string or None if invalid
        """
        # Already a reference
        if isinstance(value, str) and value.startswith('{'):
            return value

        # Hex string
        if isinstance(value, str) and value.startswith('#'):
            return value

        # RGB object (Figma format: 0-1 range)
        if isinstance(value, dict) and 'r' in value:
            r = value.get('r', 0)
            g = value.get('g', 0)
            b = value.get('b', 0)
            a = value.get('a', 1)
            return ColorConverter.rgb_to_hex(r, g, b, a)

        # Fallback
        if isinstance(value, str):
            return value

        return None


class TokenPathUtils:
    """Utilities for working with token paths"""

    @staticmethod
    def sanitize_name(name: str) -> str:
        """
        Sanitize name for use in token paths

        Args:
            name: Name to sanitize

        Returns:
            Sanitized name suitable for token paths
        """
        # Convert to lowercase and replace spaces/special chars with hyphens
        name = name.lower()
        name = re.sub(r'[^\w\s-]', '', name)
        name = re.sub(r'[-\s]+', '-', name)
        return name.strip('-')

    @staticmethod
    def join_path(*parts: str) -> str:
        """
        Join token path parts with dots

        Args:
            *parts: Path parts to join

        Returns:
            Joined path string
        """
        return '.'.join(filter(None, parts))

    @staticmethod
    def split_path(path: str) -> list:
        """
        Split token path into parts

        Args:
            path: Token path to split

        Returns:
            List of path parts
        """
        return path.split('.')


class ColorNameStandardizer:
    """Standardize color names to semantic conventions"""

    # Default semantic color mappings
    DEFAULT_MAPPINGS = {
        # Primary colors
        'primary': ['primary', 'main', 'brand', 'accent'],
        'secondary': ['secondary', 'alternate', 'alt'],
        'tertiary': ['tertiary', 'third'],

        # State colors
        'success': ['success', 'positive', 'green', 'ok', 'valid'],
        'warning': ['warning', 'caution', 'yellow', 'alert'],
        'error': ['error', 'danger', 'negative', 'red', 'invalid', 'critical'],
        'info': ['info', 'information', 'blue', 'notice'],

        # Neutral colors
        'neutral': ['neutral', 'gray', 'grey', 'muted'],
        'background': ['background', 'bg', 'surface'],
        'foreground': ['foreground', 'fg', 'text'],

        # Special colors
        'accent': ['accent', 'highlight', 'emphasis'],
        'link': ['link', 'anchor', 'hyperlink'],
    }

    def __init__(self, custom_mappings: dict = None):
        """
        Initialize color name standardizer

        Args:
            custom_mappings: Optional custom color name mappings to override defaults
        """
        self.mappings = self.DEFAULT_MAPPINGS.copy()
        if custom_mappings:
            self.mappings.update(custom_mappings)

    def standardize(self, name: str) -> str:
        """
        Standardize color name to semantic convention

        Args:
            name: Original color name from Figma

        Returns:
            Standardized semantic color name, or original if no match found
        """
        # Normalize input for matching
        normalized = name.lower().strip()

        # Check each semantic name and its aliases
        for semantic_name, aliases in self.mappings.items():
            for alias in aliases:
                if alias in normalized:
                    return semantic_name

        # Return original name if no match found
        return name

    def get_standard_name(self, name: str, fallback: str = None) -> str:
        """
        Get standardized name with optional fallback

        Args:
            name: Original color name
            fallback: Fallback name if no standard match found

        Returns:
            Standardized name or fallback
        """
        standardized = self.standardize(name)
        if standardized == name and fallback:
            return fallback
        return standardized


class SizeStandardizer:
    """Standardize size values to t-shirt sizing convention"""

    # T-shirt size scale
    SIZE_SCALE = ['xs', 'sm', 'md', 'lg', 'xl', '2xl', '3xl', '4xl']

    # Default size value mappings (in pixels or relative units)
    DEFAULT_SIZE_MAPPINGS = {
        'xs': ['extra-small', 'x-small', 'tiny', 'mini'],
        'sm': ['small', 'compact'],
        'md': ['medium', 'base', 'default', 'normal', 'regular'],
        'lg': ['large', 'big'],
        'xl': ['extra-large', 'x-large', 'huge'],
        '2xl': ['2x-large', 'xxl', 'xx-large', 'jumbo'],
        '3xl': ['3x-large', 'xxxl', 'xxx-large'],
        '4xl': ['4x-large', 'xxxxl', 'xxxx-large'],
    }

    def __init__(self, custom_mappings: dict = None):
        """
        Initialize size standardizer

        Args:
            custom_mappings: Optional custom size name mappings to override defaults
        """
        self.mappings = self.DEFAULT_SIZE_MAPPINGS.copy()
        if custom_mappings:
            self.mappings.update(custom_mappings)

    def standardize(self, name: str) -> str:
        """
        Standardize size name to t-shirt convention

        Args:
            name: Original size name from Figma

        Returns:
            Standardized t-shirt size name, or original if no match found
        """
        # Normalize input for matching
        normalized = name.lower().strip()

        # Check each t-shirt size and its aliases
        for size_name, aliases in self.mappings.items():
            # Check if normalized name matches the size itself
            if size_name == normalized:
                return size_name

            # Check aliases
            for alias in aliases:
                if alias in normalized or normalized in alias:
                    return size_name

        # Check for numeric patterns (0-8 scale maps to xs-4xl)
        if normalized.isdigit():
            num = int(normalized)
            if 0 <= num < len(self.SIZE_SCALE):
                return self.SIZE_SCALE[num]

        # Return original name if no match found
        return name

    def standardize_by_value(self, value: float, category: str = 'spacing') -> str:
        """
        Standardize size name based on numeric value

        Args:
            value: Numeric size value (in pixels)
            category: Category for context (spacing, width, height, border-radius)

        Returns:
            T-shirt size name based on value range
        """
        # Default pixel-based breakpoints for different categories
        breakpoints = {
            'spacing': {
                'xs': (0, 4),
                'sm': (4, 8),
                'md': (8, 16),
                'lg': (16, 32),
                'xl': (32, 64),
                '2xl': (64, 128),
                '3xl': (128, 256),
                '4xl': (256, float('inf')),
            },
            'border-radius': {
                'xs': (0, 2),
                'sm': (2, 4),
                'md': (4, 8),
                'lg': (8, 16),
                'xl': (16, 32),
                '2xl': (32, 64),
                '3xl': (64, 128),
                '4xl': (128, float('inf')),
            },
            'font-size': {
                'xs': (0, 12),
                'sm': (12, 14),
                'md': (14, 16),
                'lg': (16, 20),
                'xl': (20, 24),
                '2xl': (24, 32),
                '3xl': (32, 48),
                '4xl': (48, float('inf')),
            },
        }

        # Default to spacing breakpoints if category not found
        category_breakpoints = breakpoints.get(category, breakpoints['spacing'])

        # Find matching size
        for size, (min_val, max_val) in category_breakpoints.items():
            if min_val <= value < max_val:
                return size

        # Fallback to md if no match
        return 'md'


def generate_value_hash(category: str, value: Any) -> str:
    """
    Generate hash for value deduplication

    Args:
        category: Token category (color, typography, spacing)
        value: Token value

    Returns:
        Hash string for deduplication
    """
    import json

    # Normalize value for comparison
    if isinstance(value, dict):
        # For colors in RGB format
        normalized = json.dumps(value, sort_keys=True)
    else:
        normalized = str(value)

    return f"{category}:{normalized}"
