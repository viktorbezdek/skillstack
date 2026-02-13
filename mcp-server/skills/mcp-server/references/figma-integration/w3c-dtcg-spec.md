# W3C Design Tokens Community Group (DTCG) Specification Reference

This document provides a comprehensive reference for the W3C Design Tokens Format Module specification, which defines a standard format for design tokens to enable interoperability across design tools and development platforms.

## Overview

**Specification:** W3C Design Tokens Format Module
**MIME Type:** `application/design-tokens+json`
**File Extensions:** `.tokens` or `.tokens.json`
**JSON Schema:** `https://design-tokens.github.io/community-group/format.json`

## Basic Structure

Design tokens are represented as JSON objects with special properties prefixed by `$`:

```json
{
  "token-name": {
    "$value": "value-here",
    "$type": "color",
    "$description": "Optional description"
  }
}
```

## Required Properties

### `$value`

The only required property for a token. Contains the actual value of the design token.

**Example:**
```json
{
  "primary-color": {
    "$value": "#0066cc"
  }
}
```

## Optional Properties

### `$type`

Specifies the token's type (category). Can be specified at the token level or inherited from a parent group.

**Valid Types:**
- Scalar: `color`, `dimension`, `fontFamily`, `fontWeight`, `duration`, `cubicBezier`, `number`, `string`, `boolean`
- Composite: `typography`, `shadow`, `border`, `gradient`, `strokeStyle`

**Example:**
```json
{
  "colors": {
    "$type": "color",
    "primary": {
      "$value": "#0066cc"
    },
    "secondary": {
      "$value": "#6c757d"
    }
  }
}
```

### `$description`

Plain text description explaining the token's purpose or usage.

**Example:**
```json
{
  "spacing-large": {
    "$value": "24px",
    "$description": "Used for large gaps between major UI sections"
  }
}
```

### `$deprecated`

Indicates the token is deprecated. Can be a boolean or a string with deprecation message.

**Example:**
```json
{
  "old-color": {
    "$value": "#ff0000",
    "$deprecated": "Use primary-color instead"
  }
}
```

### `$extensions`

Vendor-specific metadata. Property names should use reverse domain notation.

**Example:**
```json
{
  "brand-color": {
    "$value": "#0066cc",
    "$extensions": {
      "com.figma": {
        "variableId": "abc123",
        "scopes": ["ALL_SCOPES"]
      }
    }
  }
}
```

## Token Types

### Scalar Types

#### `color`

Represents a color value.

**Supported Formats:**
1. Hex string: `"#RRGGBB"` or `"#RRGGBBAA"`
2. RGB/RGBA functions: `"rgb(255, 0, 0)"` or `"rgba(255, 0, 0, 0.5)"`
3. Color space object:

```json
{
  "$type": "color",
  "$value": {
    "colorSpace": "srgb",
    "components": [0, 0.4, 0.8],
    "alpha": 1.0
  }
}
```

**Supported Color Spaces:**
- `srgb` - Standard RGB
- `display-p3` - Display P3 wide gamut
- `a98-rgb` - Adobe RGB
- `prophoto-rgb` - ProPhoto RGB
- `rec2020` - Rec. 2020
- `oklch` - OKLab cylindrical
- `oklab` - OKLab
- `xyz-d50`, `xyz-d65` - CIE XYZ

**Examples:**
```json
{
  "colors": {
    "$type": "color",
    "primary": {
      "$value": "#0066cc"
    },
    "accent": {
      "$value": "rgb(255, 128, 0)"
    },
    "brand": {
      "$value": {
        "colorSpace": "display-p3",
        "components": [0, 0.5, 1],
        "alpha": 1.0
      }
    }
  }
}
```

#### `dimension`

Represents a size, distance, or length with a unit.

**Supported Units:**
- Absolute: `px`, `pt`, `pc`, `in`, `cm`, `mm`
- Relative: `rem`, `em`, `%`, `vh`, `vw`, `vmin`, `vmax`

**Format:** String with numeric value followed by unit

**Examples:**
```json
{
  "spacing": {
    "$type": "dimension",
    "small": {
      "$value": "8px"
    },
    "medium": {
      "$value": "1rem"
    },
    "large": {
      "$value": "5%"
    }
  }
}
```

#### `fontFamily`

Font family name(s).

**Format:** String or array of strings (with fallbacks)

**Examples:**
```json
{
  "fonts": {
    "$type": "fontFamily",
    "body": {
      "$value": "Inter"
    },
    "heading": {
      "$value": ["Helvetica Neue", "Helvetica", "Arial", "sans-serif"]
    }
  }
}
```

#### `fontWeight`

Font weight value.

**Format:** Number (1-1000) or string keyword

**Valid Keywords:**
- `thin` (100)
- `extra-light` (200)
- `light` (300)
- `normal` (400)
- `medium` (500)
- `semi-bold` (600)
- `bold` (700)
- `extra-bold` (800)
- `black` (900)

**Examples:**
```json
{
  "weights": {
    "$type": "fontWeight",
    "regular": {
      "$value": 400
    },
    "bold": {
      "$value": "bold"
    },
    "black": {
      "$value": 900
    }
  }
}
```

#### `duration`

Time duration for animations/transitions.

**Supported Units:** `ms` (milliseconds), `s` (seconds)

**Format:** String with numeric value followed by unit

**Examples:**
```json
{
  "durations": {
    "$type": "duration",
    "quick": {
      "$value": "100ms"
    },
    "normal": {
      "$value": "0.3s"
    },
    "slow": {
      "$value": "500ms"
    }
  }
}
```

#### `cubicBezier`

Cubic Bézier curve for animation easing.

**Format:** Array of 4 numbers `[x1, y1, x2, y2]`

**Examples:**
```json
{
  "easings": {
    "$type": "cubicBezier",
    "ease-in": {
      "$value": [0.42, 0, 1, 1]
    },
    "ease-out": {
      "$value": [0, 0, 0.58, 1]
    },
    "ease-in-out": {
      "$value": [0.42, 0, 0.58, 1]
    }
  }
}
```

#### `number`

Unitless numeric value.

**Format:** Number (integer or float)

**Examples:**
```json
{
  "numbers": {
    "$type": "number",
    "line-height-tight": {
      "$value": 1.2
    },
    "line-height-normal": {
      "$value": 1.5
    },
    "opacity-subtle": {
      "$value": 0.6
    }
  }
}
```

#### `string`

Arbitrary string value.

**Format:** String

**Examples:**
```json
{
  "content": {
    "$type": "string",
    "app-name": {
      "$value": "My Application"
    },
    "copyright": {
      "$value": "© 2025 Company Inc."
    }
  }
}
```

#### `boolean`

True/false value.

**Format:** Boolean

**Examples:**
```json
{
  "features": {
    "$type": "boolean",
    "dark-mode-enabled": {
      "$value": true
    },
    "beta-features": {
      "$value": false
    }
  }
}
```

### Composite Types

#### `typography`

Aggregates font-related properties.

**Properties:**
- `fontFamily` - Font family (required)
- `fontSize` - Font size (required)
- `fontWeight` - Font weight (optional)
- `letterSpacing` - Letter spacing (optional)
- `lineHeight` - Line height (optional)

**Example:**
```json
{
  "typography": {
    "$type": "typography",
    "heading-1": {
      "$value": {
        "fontFamily": "Helvetica Neue",
        "fontSize": "32px",
        "fontWeight": 700,
        "lineHeight": 1.2,
        "letterSpacing": "-0.5px"
      }
    },
    "body": {
      "$value": {
        "fontFamily": ["Inter", "sans-serif"],
        "fontSize": "16px",
        "fontWeight": 400,
        "lineHeight": 1.5
      }
    }
  }
}
```

#### `shadow`

Represents box shadows or drop shadows.

**Properties:**
- `offsetX` - Horizontal offset (required, dimension)
- `offsetY` - Vertical offset (required, dimension)
- `blur` - Blur radius (required, dimension)
- `spread` - Spread radius (optional, dimension)
- `color` - Shadow color (required, color)
- `inset` - Whether shadow is inset (optional, boolean)

**Example:**
```json
{
  "shadows": {
    "$type": "shadow",
    "card": {
      "$value": {
        "offsetX": "0px",
        "offsetY": "2px",
        "blur": "4px",
        "spread": "0px",
        "color": "rgba(0, 0, 0, 0.1)"
      }
    },
    "elevated": {
      "$value": {
        "offsetX": "0px",
        "offsetY": "8px",
        "blur": "16px",
        "spread": "0px",
        "color": "rgba(0, 0, 0, 0.15)"
      }
    }
  }
}
```

#### `border`

Represents border styling.

**Properties:**
- `width` - Border width (required, dimension)
- `style` - Border style (required, strokeStyle or string)
- `color` - Border color (required, color)

**Example:**
```json
{
  "borders": {
    "$type": "border",
    "thin": {
      "$value": {
        "width": "1px",
        "style": "solid",
        "color": "#e0e0e0"
      }
    },
    "focus": {
      "$value": {
        "width": "2px",
        "style": "solid",
        "color": "#0066cc"
      }
    }
  }
}
```

#### `gradient`

Represents color gradients.

**Format:** Array of gradient stops, each with:
- `color` - Stop color (required, color)
- `position` - Stop position (required, number 0-1)

**Example:**
```json
{
  "gradients": {
    "$type": "gradient",
    "primary": {
      "$value": [
        {
          "color": "#0066cc",
          "position": 0
        },
        {
          "color": "#0099ff",
          "position": 1
        }
      ]
    },
    "rainbow": {
      "$value": [
        { "color": "#ff0000", "position": 0 },
        { "color": "#00ff00", "position": 0.5 },
        { "color": "#0000ff", "position": 1 }
      ]
    }
  }
}
```

#### `strokeStyle`

Represents stroke/dash patterns.

**Properties:**
- `dashArray` - Array of dash lengths (required)
- `lineCap` - Line cap style (optional: "round", "butt", "square")

**Example:**
```json
{
  "strokes": {
    "$type": "strokeStyle",
    "dashed": {
      "$value": {
        "dashArray": ["4px", "4px"],
        "lineCap": "round"
      }
    },
    "dotted": {
      "$value": {
        "dashArray": ["1px", "3px"],
        "lineCap": "round"
      }
    }
  }
}
```

## References (Aliases)

Tokens can reference other tokens using the alias syntax: `{token.path}`

**Rules:**
- Reference paths use dot notation
- References must point to existing tokens
- Circular references are invalid
- Type compatibility should be maintained

**Examples:**
```json
{
  "color": {
    "$type": "color",
    "blue-500": {
      "$value": "#0066cc"
    },
    "primary": {
      "$value": "{color.blue-500}"
    },
    "link": {
      "$value": "{color.primary}"
    }
  }
}
```

**Multi-Level References:**
```json
{
  "primitives": {
    "blue": {
      "$type": "color",
      "$value": "#0066cc"
    }
  },
  "semantic": {
    "primary": {
      "$type": "color",
      "$value": "{primitives.blue}"
    }
  },
  "components": {
    "button-background": {
      "$type": "color",
      "$value": "{semantic.primary}"
    }
  }
}
```

## Groups and Nesting

Tokens can be organized into groups using nested objects.

**Type Inheritance:**
Groups can specify a `$type` that is inherited by all child tokens.

**Example:**
```json
{
  "colors": {
    "$type": "color",
    "primary": {
      "$value": "#0066cc"
    },
    "secondary": {
      "$value": "#6c757d"
    }
  },
  "spacing": {
    "$type": "dimension",
    "small": {
      "$value": "8px"
    },
    "medium": {
      "$value": "16px"
    }
  }
}
```

**Nested Groups:**
```json
{
  "color": {
    "$type": "color",
    "brand": {
      "primary": {
        "$value": "#0066cc"
      },
      "secondary": {
        "$value": "#6c757d"
      }
    },
    "feedback": {
      "success": {
        "$value": "#28a745"
      },
      "error": {
        "$value": "#dc3545"
      }
    }
  }
}
```

## Best Practices

### Token Naming

1. **Use descriptive names:** `color-primary` not `color1`
2. **Maintain hierarchy:** Use dots or hyphens for structure
3. **Semantic over literal:** `color-brand` not `color-blue`
4. **Consistent conventions:** Pick kebab-case, camelCase, or another and stick to it

### Token Organization

1. **Primitive tokens:** Base values (colors, sizes)
2. **Semantic tokens:** Context-specific values (primary, secondary)
3. **Component tokens:** Component-specific overrides

**Example Structure:**
```json
{
  "primitive": {
    "color": {
      "blue-500": { "$value": "#0066cc" }
    }
  },
  "semantic": {
    "color": {
      "primary": { "$value": "{primitive.color.blue-500}" }
    }
  },
  "component": {
    "button": {
      "background": { "$value": "{semantic.color.primary}" }
    }
  }
}
```

### Type Specification

1. **Always specify types:** Either at token or group level
2. **Use group-level types:** For categories with same type
3. **Override when needed:** Token-level type overrides group type

### References

1. **Reference primitives:** Build on base values
2. **Avoid deep chains:** Maximum 2-3 levels of references
3. **Document relationships:** Use `$description` to explain references
4. **Prevent cycles:** Validate for circular references

### Descriptions

1. **Explain purpose:** Why this token exists
2. **Document usage:** Where/when to use
3. **Note constraints:** Any limitations or requirements

## Common Patterns

### Theme Tokens

**Approach 1: Separate Files**
```
tokens-light.json
tokens-dark.json
```

**Approach 2: References**
```json
{
  "mode": {
    "light": {
      "background": { "$value": "#ffffff" }
    },
    "dark": {
      "background": { "$value": "#000000" }
    }
  },
  "current": {
    "background": { "$value": "{mode.light.background}" }
  }
}
```

### Responsive Scales

```json
{
  "spacing": {
    "$type": "dimension",
    "scale": {
      "1": { "$value": "4px" },
      "2": { "$value": "8px" },
      "3": { "$value": "12px" },
      "4": { "$value": "16px" },
      "5": { "$value": "24px" },
      "6": { "$value": "32px" },
      "7": { "$value": "48px" },
      "8": { "$value": "64px" }
    }
  }
}
```

### Brand Variants

```json
{
  "brand": {
    "acme": {
      "primary": { "$value": "#ff0000" }
    },
    "globex": {
      "primary": { "$value": "#0000ff" }
    }
  }
}
```

## Validation

Tokens should be validated for:

1. **Required properties:** All tokens have `$value`
2. **Type consistency:** Values match declared `$type`
3. **Reference validity:** All references resolve to existing tokens
4. **No circular references:** Detect and prevent cycles
5. **Format compliance:** Values match expected formats for types

## Further Reading

- **W3C Design Tokens Community Group:** https://www.designtokens.org/
- **Format Specification:** https://tr.designtokens.org/format/
- **GitHub Repository:** https://github.com/design-tokens/community-group
