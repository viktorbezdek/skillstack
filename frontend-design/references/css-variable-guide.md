# CSS Variable Reference Guide

## Introduction

The @fpkit/acss component library uses **CSS custom properties** (CSS variables) to provide flexible theming and customization. This guide explains how to discover, understand, and customize component styles using our standardized naming convention.

### Why CSS Variables?

CSS variables allow you to customize component appearance without modifying the library's source code:

```css
/* Override button colors globally */
:root {
  --btn-primary-bg: #0066cc;
  --btn-primary-color: white;
}

/* Or scope to specific contexts */
.dark-theme {
  --btn-primary-bg: #66b3ff;
  --btn-bg: #2d2d2d;
}
```

### Quick Start

1. **Discover variables**: Use your IDE's autocomplete - type `--btn-` to see all button variables
2. **Override in your CSS**: Define custom values in `:root` or scoped selectors
3. **Test in Storybook**: Changes reflect immediately in component stories

---

## Naming Convention Pattern

All CSS variables in @fpkit/acss follow a consistent hierarchical structure:

```
--{component}-{element}-{variant}-{property}-{modifier}
```

### Pattern Breakdown

| Segment | Required | Examples | Purpose |
|---------|----------|----------|---------|
| **component** | ✅ Yes | `btn`, `alert`, `card`, `nav` | Component namespace |
| **element** | ❌ Optional | `header`, `footer`, `title`, `icon` | Sub-component part |
| **variant** | ❌ Optional | `primary`, `error`, `success`, `warning` | Style or semantic variant |
| **property** | ✅ Yes | `bg`, `color`, `padding`, `border` | CSS property name |
| **modifier** | ❌ Optional | `offset`, `width`, `radius` | Property modifier |

### Pattern Examples

```scss
// Component base property
--btn-bg

// Variant-specific property
--btn-primary-bg

// State-specific property
--btn-hover-bg
--btn-focus-outline

// Element-specific property
--card-header-padding
--card-footer-bg

// State with modified property
--btn-focus-outline-offset

// Element with variant
--alert-icon-error-color
```

---

## Approved Abbreviations

To balance brevity with clarity, we use selective abbreviations:

### ✅ Abbreviated (Widely Recognized)

| Abbreviation | Full Name | Rationale |
|--------------|-----------|-----------|
| `bg` | background / background-color | Universal CSS convention |
| `fs` | font-size | Well-established in typography |
| `fw` | font-weight | Common in typography systems |
| `radius` | border-radius | Short enough, avoids ambiguity |
| `gap` | gap | Already one word |

**Example:**
```scss
--btn-bg: #0066cc;
--btn-fs: 1rem;
--btn-fw: 600;
--btn-radius: 0.375rem;
--btn-gap: 0.5rem;
```

### ✅ Full Words (For Clarity)

| Property | ❌ Don't Use | ✅ Use | Rationale |
|----------|--------------|--------|-----------|
| padding | `p`, `px`, `py` | `padding`, `padding-inline`, `padding-block` | Logical properties need clarity |
| margin | `m`, `mx`, `my` | `margin`, `margin-inline`, `margin-block` | Logical properties need clarity |
| color | `cl`, `c` | `color` | Too ambiguous when abbreviated |
| border | `bdr`, `br` | `border` | Avoid confusion with radius |
| display | `dsp`, `d` | `display` | Not universally recognized |
| width | `w` | `width` | Single letters harm clarity |
| height | `h` | `height` | Single letters harm clarity |

**Example:**
```scss
// ❌ Bad (old style)
--btn-px: 1.5rem;
--btn-py: 0.5rem;
--btn-cl: currentColor;
--btn-dsp: inline-flex;

// ✅ Good (standardized)
--btn-padding-inline: 1.5rem;
--btn-padding-block: 0.5rem;
--btn-color: currentColor;
--btn-display: inline-flex;
```

---

## rem Units Only

**All spacing and sizing must use rem units (not px).**

**Conversion formula:** `px / 16 = rem`

**Examples:**
- 11px = 0.6875rem
- 13px = 0.8125rem
- 15px = 0.9375rem
- 16px = 1rem
- 18px = 1.125rem
- 24px = 1.5rem

**Why rem units?**
- Respects user font size preferences (accessibility)
- Consistent scaling across breakpoints
- Better for responsive design
- Project standard (enforced in validation)

---

## Variant Organization

Variants represent different visual or semantic styles of a component.

### Pattern

```
--{component}-{variant}-{property}
```

### Semantic Variants

Used for UI states with meaning (alerts, messages):

```scss
// Error variant
--alert-error-bg: #f8d7da;
--alert-error-border: #f5c6cb;
--alert-error-color: #721c24;

// Success variant
--alert-success-bg: #d4edda;
--alert-success-border: #c3e6cb;
--alert-success-color: #155724;
```

### Style Variants

Used for visual hierarchy (buttons, badges):

```scss
// Primary button (high emphasis)
--btn-primary-bg: #0066cc;
--btn-primary-color: white;
--btn-primary-border: 1px solid #0066cc;

// Secondary button (medium emphasis)
--btn-secondary-bg: transparent;
--btn-secondary-color: #0066cc;
--btn-secondary-border: 1px solid currentColor;
```

---

## State Variables

States represent interactive or conditional component appearances.

### Pattern

```
--{component}-{state}-{property}
```

### Common States

| State | Description | Example Use |
|-------|-------------|-------------|
| `hover` | Mouse hover | `--btn-hover-bg` |
| `focus` | Keyboard focus | `--btn-focus-outline` |
| `active` | Active/pressed | `--btn-active-transform` |
| `disabled` | Disabled state | `--btn-disabled-opacity` |
| `visited` | Visited link | `--link-visited-color` |
| `checked` | Checked checkbox/radio | `--checkbox-checked-bg` |

### State Examples

```scss
// Hover state
--btn-hover-bg: #0052a3;
--btn-hover-transform: translateY(-1px);
--btn-hover-filter: brightness(1.1);

// Focus state
--btn-focus-outline: 2px solid currentColor;
--btn-focus-outline-offset: 2px;
--btn-focus-color: #0066cc;

// Disabled state
--btn-disabled-opacity: 0.6;
--btn-disabled-cursor: not-allowed;
--btn-disabled-bg: #e9ecef;
```

---

## Element-Specific Variables

Complex components with multiple visual sections use element scoping.

### Pattern

```
--{component}-{element}-{property}
```

### When to Use Element Scoping

✅ **Use when:**
- Component has distinct visual sections (header, footer, body)
- Each section can be styled independently
- Sub-elements have unique properties

❌ **Don't use when:**
- Simple components with no visual hierarchy (Badge, Tag)
- Elements are purely structural (no custom styling needed)

### Card Example

```scss
// Base card properties
--card-padding: 1rem;
--card-bg: white;
--card-radius: 0.5rem;
--card-border: 1px solid #e0e0e0;

// Card header
--card-header-padding: 1rem 1.5rem;
--card-header-bg: #f9f9f9;
--card-header-border-bottom: 1px solid #e0e0e0;
--card-header-fs: 1.25rem;
--card-header-fw: 600;

// Card footer
--card-footer-padding: 1rem 1.5rem;
--card-footer-bg: #f9f9f9;
--card-footer-border-top: 1px solid #e0e0e0;
```

---

## Best Practices

### ✅ Do

- **Use the naming pattern consistently** when creating custom variables
- **Use rem units only** (no px except for 0px or borders in special cases)
- **Use logical properties** (`padding-inline`, `padding-block`) for better RTL support
- **Test in Storybook** to verify changes work correctly
- **Validate with validate_css_vars.py** before committing

### ❌ Don't

- **Don't use px units** for spacing or sizing (use rem)
- **Don't use forbidden abbreviations** (px/py, w/h, cl, dsp, bdr)
- **Don't abbreviate randomly** - follow approved abbreviations only
- **Don't create one-off variables** - use the component pattern
- **Don't use `!important`** unless absolutely necessary
