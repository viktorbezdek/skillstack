# Design Token Naming Conventions Reference

This document provides comprehensive guidance on naming conventions for design tokens, covering various patterns, best practices, and strategies for organizing tokens at scale.

## Overview

Good token naming is critical for:
- **Maintainability** - Easy to find and update tokens
- **Scalability** - Supports growth without reorganization
- **Communication** - Clear intent and usage
- **Automation** - Enables tooling and transformations

## Case Conventions

### kebab-case (Recommended)

**Format:** Lowercase words separated by hyphens

**Example:**
```
color-primary-500
spacing-medium
font-family-heading
```

**Pros:**
- Readable in URLs
- Compatible with CSS custom properties
- Clear word boundaries
- Widely adopted standard

**Cons:**
- Slightly longer than camelCase

**Usage:** CSS variables, file names, general purpose

### camelCase

**Format:** First word lowercase, subsequent words capitalized

**Example:**
```
colorPrimary500
spacingMedium
fontFamilyHeading
```

**Pros:**
- Compact
- Natural in JavaScript/TypeScript
- No special characters

**Cons:**
- Less readable for long names
- Not usable in CSS custom properties directly

**Usage:** JavaScript/TypeScript code, programmatic access

### snake_case

**Format:** Lowercase words separated by underscores

**Example:**
```
color_primary_500
spacing_medium
font_family_heading
```

**Pros:**
- Very readable
- Common in Python, Ruby
- Clear word boundaries

**Cons:**
- Not compatible with CSS custom properties (requires prefixing)
- Less common in web development

**Usage:** Python scripts, backend systems, JSON keys

### BEM (Block Element Modifier)

**Format:** Block__element--modifier

**Example:**
```
color__primary--500
spacing__vertical--medium
font__heading--bold
```

**Pros:**
- Clear hierarchy
- Borrowed from proven CSS methodology
- Explicit relationships

**Cons:**
- Verbose
- Less intuitive for non-CSS developers
- Awkward for deeply nested tokens

**Usage:** CSS-heavy projects, BEM-based architectures

### PascalCase

**Format:** All words capitalized

**Example:**
```
ColorPrimary500
SpacingMedium
FontFamilyHeading
```

**Pros:**
- Stands out visually
- Common for TypeScript types/interfaces

**Cons:**
- Not compatible with CSS
- Can be confused with class names

**Usage:** TypeScript type names, constants

## Token Hierarchy

### Flat Structure

**Pattern:** Category-name-variant

**Example:**
```
color-blue-500
color-red-500
spacing-small
spacing-medium
```

**Pros:**
- Simple to understand
- No nesting complexity
- Easy to search

**Cons:**
- Scales poorly
- No clear relationships
- Limited organization

**Best for:** Small projects, quick prototypes

### Nested Structure

**Pattern:** Category.subcategory.name.variant

**Example:**
```
color.brand.primary.500
color.feedback.error.base
spacing.layout.medium
spacing.component.gap
```

**Pros:**
- Clear hierarchy
- Scales well
- Logical grouping

**Cons:**
- Can become overly nested
- Requires consistent structure
- More verbose

**Best for:** Large design systems, enterprise projects

### Hybrid Structure

**Pattern:** Mix of flat and nested based on needs

**Example:**
```
color.primary-500
spacing.medium
typography.heading-1
```

**Pros:**
- Flexibility
- Optimizes for common cases
- Readable

**Cons:**
- Inconsistent patterns
- Requires documentation

**Best for:** Medium-sized projects, evolving systems

## Semantic vs Primitive Tokens

### Primitive Tokens (Literal Values)

Describe what they are, not how they're used.

**Examples:**
```
color.blue.500
color.gray.100
spacing.4
spacing.8
font-size.16
font-weight.700
```

**Characteristics:**
- Literal values
- No context
- Base layer
- Rarely changed directly
- Often use scales (100-900, 1-10)

**Naming Pattern:** `category.color-name.scale`

### Semantic Tokens (Contextual)

Describe their purpose or usage.

**Examples:**
```
color.primary
color.text-default
color.background-elevated
spacing.component-gap
spacing.section-margin
font-family.heading
font-size.body
```

**Characteristics:**
- Context-aware
- Intent-driven
- References primitives
- Frequently used in components
- Easier to theme

**Naming Pattern:** `category.purpose` or `category.context-purpose`

### Relationship

Semantic tokens reference primitive tokens:

**W3C DTCG Format:**
```json
{
  "primitive": {
    "blue": {
      "500": {
        "$type": "color",
        "$value": "#0066cc"
      }
    }
  },
  "semantic": {
    "primary": {
      "$type": "color",
      "$value": "{primitive.blue.500}"
    }
  }
}
```

**Best Practice:** Use 2-3 layers:
1. **Primitives** - Raw values
2. **Semantic** - Purpose-based
3. **Component** (optional) - Component-specific overrides

## Scale Naming

### Numeric Scales

**T-Shirt Sizes:** xs, sm, md, lg, xl, xxl

**Example:**
```
spacing-xs    (4px)
spacing-sm    (8px)
spacing-md    (16px)
spacing-lg    (24px)
spacing-xl    (32px)
```

**Pros:**
- Intuitive relative sizing
- Non-technical friendly

**Cons:**
- Limited precision
- Ambiguous absolute values
- Hard to insert intermediate sizes

**Best for:** Spacing, sizing, simple scales

### Number Scales (100-900)

**Example:**
```
color-blue-100  (lightest)
color-blue-500  (base)
color-blue-900  (darkest)
```

**Pros:**
- Industry standard (Material, Tailwind)
- Easy to add intermediate values
- Clear progression

**Cons:**
- Not immediately obvious what number means
- Requires documentation

**Best for:** Colors, shadows, large scales

### Sequential Numbers (1-N)

**Example:**
```
spacing-1   (4px)
spacing-2   (8px)
spacing-3   (12px)
spacing-4   (16px)
```

**Pros:**
- Simple
- Clear order
- Compact

**Cons:**
- Unintuitive values
- Hard to remember mappings

**Best for:** Consistent mathematical progressions

### Named Scales

**Example:**
```
font-size-caption
font-size-body
font-size-subheading
font-size-heading
font-size-display
```

**Pros:**
- Self-documenting
- Clear intent
- No memorization needed

**Cons:**
- Verbose
- Harder to systematize
- Limited flexibility

**Best for:** Typography, explicit hierarchies

## Automated Semantic Name Standardization

The `extract_tokens.py` script includes automated standardization capabilities to transform Figma token names into industry-standard semantic conventions.

### Color Name Standardization

**Implementation:** `utils.ColorNameStandardizer`

Maps common Figma color names to semantic standards based on intent and usage:

**Default Mappings:**

| Semantic Name | Figma Name Aliases |
|---------------|-------------------|
| `primary` | primary, main, brand, accent |
| `secondary` | secondary, alternate, alt |
| `tertiary` | tertiary, third |
| `success` | success, positive, green, ok, valid |
| `warning` | warning, caution, yellow, alert |
| `error` | error, danger, negative, red, invalid, critical |
| `info` | info, information, blue, notice |
| `neutral` | neutral, gray, grey, muted |
| `background` | background, bg, surface |
| `foreground` | foreground, fg, text |
| `accent` | accent, highlight, emphasis |
| `link` | link, anchor, hyperlink |

**Example Transformations:**
```
Brand Blue → primary
Red Background → error
Success Message → success
Gray Text → neutral
```

**Usage:**
```bash
python extract_tokens.py \
  --figma-data input.json \
  --output-path tokens.json \
  --standardize-names
```

**Custom Mappings:**
```json
{
  "colors": {
    "brand": ["brand", "company", "corporate"],
    "disabled": ["disabled", "inactive", "muted"],
    "destructive": ["destructive", "delete", "remove"]
  }
}
```

### Size Standardization (T-shirt Sizing)

**Implementation:** `utils.SizeStandardizer`

Normalizes size values to t-shirt scale: **xs, sm, md, lg, xl, 2xl, 3xl, 4xl**

**Two Standardization Modes:**

#### 1. Name-Based Standardization

Maps size names to t-shirt equivalents:

| T-shirt Size | Figma Name Aliases |
|--------------|-------------------|
| `xs` | extra-small, x-small, tiny, mini |
| `sm` | small, compact |
| `md` | medium, base, default, normal, regular |
| `lg` | large, big |
| `xl` | extra-large, x-large, huge |
| `2xl` | 2x-large, xxl, xx-large, jumbo |
| `3xl` | 3x-large, xxxl, xxx-large |
| `4xl` | 4x-large, xxxxl, xxxx-large |

**Example:**
```
Small Spacing → sm
Extra Large Gap → xl
Tiny Padding → xs
```

#### 2. Value-Based Standardization

Maps pixel values to t-shirt sizes based on category-specific breakpoints:

**Spacing Breakpoints:**
```
xs:  0-4px
sm:  4-8px
md:  8-16px
lg:  16-32px
xl:  32-64px
2xl: 64-128px
3xl: 128-256px
4xl: 256px+
```

**Border Radius Breakpoints:**
```
xs:  0-2px
sm:  2-4px
md:  4-8px
lg:  8-16px
xl:  16-32px
2xl: 32-64px
3xl: 64-128px
4xl: 128px+
```

**Font Size Breakpoints:**
```
xs:  0-12px
sm:  12-14px
md:  14-16px
lg:  16-20px
xl:  20-24px
2xl: 24-32px
3xl: 32-48px
4xl: 48px+
```

**Example:**
```
4px spacing → xs
16px gap → md
64px margin → 2xl
```

**Usage:**
```bash
python extract_tokens.py \
  --figma-data input.json \
  --output-path tokens.json \
  --standardize-names
```

**Custom Size Mappings:**
```json
{
  "sizes": {
    "tiny": ["tiny", "micro", "mini"],
    "huge": ["huge", "jumbo", "massive"],
    "compact": ["compact", "dense", "tight"]
  }
}
```

### Integration with Custom Mappings

Both color and size standardizers support custom mappings via JSON configuration:

```bash
python extract_tokens.py \
  --figma-data input.json \
  --output-path tokens.json \
  --standardize-names \
  --name-mappings custom-mappings.json
```

**custom-mappings.json:**
```json
{
  "colors": {
    "primary": ["brand", "main", "accent"],
    "destructive": ["delete", "remove", "danger"]
  },
  "sizes": {
    "xs": ["tiny", "micro"],
    "huge": ["huge", "jumbo"]
  }
}
```

### Benefits of Standardization

**Consistency:**
- Uniform naming across projects
- Reduces cognitive load
- Easier code reviews

**Semantic Clarity:**
- Intent-based naming (why vs what)
- Better component integration
- Improved maintainability

**Interoperability:**
- Compatible with design systems (Material, Bootstrap)
- Easier migration between frameworks
- Standard patterns for new team members

**Best Practices:**

1. **Start with defaults** - Built-in mappings cover 80% of use cases
2. **Customize gradually** - Add custom mappings as patterns emerge
3. **Document choices** - Explain custom semantic names in README
4. **Review regularly** - Audit generated names for consistency
5. **Team alignment** - Ensure designers and developers agree on semantics

## Category Prefixes

### Standard Categories

**Colors:**
```
color-*
background-*
border-*
text-*
```

**Spacing:**
```
spacing-*
margin-*
padding-*
gap-*
```

**Typography:**
```
font-family-*
font-size-*
font-weight-*
line-height-*
letter-spacing-*
```

**Effects:**
```
shadow-*
opacity-*
blur-*
```

**Layout:**
```
width-*
height-*
z-index-*
```

**Animation:**
```
duration-*
easing-*
```

### Abbreviated Prefixes

For brevity in code:

```
clr-*      (color)
sp-*       (spacing)
type-*     (typography)
fx-*       (effects)
```

**Trade-off:** Shorter but less intuitive

## Context-Based Naming

### Component Tokens

Prefix with component name:

```
button-background-default
button-background-hover
button-background-active
button-text-color
button-padding-horizontal
button-padding-vertical
button-border-radius
```

**Pattern:** `component-property-state`

### State Tokens

Include interaction states:

```
color-interactive-default
color-interactive-hover
color-interactive-active
color-interactive-disabled
color-interactive-focus
```

**States:**
- default
- hover
- active
- focus
- disabled
- loading
- error
- success

### Theme Tokens

Organize by theme:

```
theme-light-background
theme-light-text
theme-dark-background
theme-dark-text
```

Or use nested structure:
```
theme.light.background
theme.dark.background
```

## Multi-Brand Systems

### Separate Namespaces

**Pattern:** `brand-category-name`

```
acme-color-primary
acme-font-family-heading
globex-color-primary
globex-font-family-heading
```

### Separate Files

Maintain brand-specific token files:
```
tokens/acme.json
tokens/globex.json
```

Reference shared primitives:
```json
{
  "acme": {
    "primary": {
      "$value": "{primitive.blue.500}"
    }
  },
  "globex": {
    "primary": {
      "$value": "{primitive.green.600}"
    }
  }
}
```

## Responsive Tokens

### Breakpoint-Specific

```
spacing-mobile-small
spacing-tablet-small
spacing-desktop-small
```

### Fluid/Adaptive

```
spacing-responsive-small
font-size-fluid-body
```

## Anti-Patterns

### ❌ Generic Names

```
color-1
color-2
variable-a
temp-value
```

**Problem:** No meaning or intent

### ❌ Implementation Details

```
color-hex-0066cc
spacing-px-16
```

**Problem:** Couples value to format

### ❌ Overly Specific

```
header-navigation-dropdown-menu-item-hover-background-color-dark-mode
```

**Problem:** Too granular, unmaintainable

### ❌ Inconsistent Casing

```
colorPrimary
spacing-medium
Font_Size_Large
```

**Problem:** Confusing, error-prone

### ❌ Magic Numbers Without Context

```
z-index-9999
opacity-0.37
```

**Problem:** Why this specific value?

## Best Practices Summary

1. **Choose one case convention** and stick to it across the system
2. **Use semantic names** for tokens consumed by components
3. **Maintain primitive tokens** as the source of truth
4. **Document scale meanings** (what is "500"? what is "medium"?)
5. **Namespace component tokens** to avoid conflicts
6. **Include state** in interactive token names
7. **Keep hierarchy shallow** (3 levels maximum)
8. **Be consistent** - establish patterns and follow them
9. **Plan for themes** from the start if needed
10. **Version your tokens** and document breaking changes

## Examples by Use Case

### Small Website

**Convention:** kebab-case, flat structure, semantic

```
color-primary
color-secondary
color-text
color-background
spacing-small
spacing-medium
spacing-large
font-family-body
font-family-heading
```

### Design System

**Convention:** kebab-case, nested, primitive + semantic

```
primitive.color.blue.500
primitive.spacing.4
semantic.color.primary
semantic.spacing.component-gap
component.button.background
component.button.text
```

### Multi-Brand Enterprise

**Convention:** kebab-case, nested, brand namespaces

```
brand.acme.color.primary
brand.acme.font.heading
brand.globex.color.primary
brand.globex.font.heading
shared.spacing.medium
shared.shadow.elevated
```

### Mobile App

**Convention:** camelCase (Swift/Kotlin friendly)

```
colorPrimary
colorBackground
spacingSmall
spacingMedium
fontBody
fontHeading
```

## Tools and Automation

### Name Transformation

Convert between conventions programmatically:

**kebab-case → camelCase:**
```
color-primary-500 → colorPrimary500
```

**camelCase → kebab-case:**
```
colorPrimary500 → color-primary-500
```

Use the `transform_tokens.py` script with `--naming-convention` flag.

### Linting

Validate token names:
- Check case consistency
- Enforce naming patterns
- Prevent reserved words
- Detect typos

### Documentation Generation

Auto-generate docs from token names:
```
color-primary → "Primary brand color"
spacing-component-gap → "Gap between components"
```

## Further Reading

- **Naming Tokens in Design Systems:** https://medium.com/eightshapes-llc/naming-tokens-in-design-systems-9e86c7444676
- **Design Tokens W3C Spec:** https://tr.designtokens.org/format/
- **Material Design Color System:** https://m3.material.io/styles/color/system/overview
- **Tailwind CSS Scale:** https://tailwindcss.com/docs/customizing-spacing
