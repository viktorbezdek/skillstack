# CSS Variables Guide

## Introduction

The @fpkit/acss component library uses **CSS custom properties** (CSS variables) to provide flexible theming and customization. This guide explains how to discover, understand, and customize component styles without modifying the library's source code.

### Why CSS Variables?

CSS variables give you powerful customization capabilities:

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

/* Component-specific overrides */
.custom-button {
  --btn-padding-inline: 2rem;
  --btn-radius: 0.25rem;
}
```

### Quick Start

1. **Discover variables**: Use browser DevTools or IDE autocomplete - type `--btn-` to see all button variables
2. **Override in your CSS**: Define custom values in `:root`, theme classes, or component selectors
3. **Test**: Changes reflect immediately without rebuilding

---

## Understanding the Naming Convention

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

### Common Patterns

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

// State with modifier
--btn-focus-outline-offset

// Element with variant
--alert-icon-error-color
```

---

## Abbreviation Reference

@fpkit/acss uses selective abbreviations to balance brevity with clarity:

### ✅ Abbreviated Properties

| Abbreviation | Full Name | Example |
|--------------|-----------|---------|
| `bg` | background / background-color | `--btn-bg` |
| `fs` | font-size | `--btn-fs` |
| `fw` | font-weight | `--btn-fw` |
| `radius` | border-radius | `--btn-radius` |
| `gap` | gap | `--btn-gap` |

### ✅ Full Word Properties

| Property | Variable Pattern | Example |
|----------|------------------|---------|
| padding | `--{component}-padding-{direction}` | `--btn-padding-inline` |
| margin | `--{component}-margin-{direction}` | `--card-margin-block` |
| color (text) | `--{component}-color` | `--btn-color` |
| border | `--{component}-border` | `--card-border` |
| display | `--{component}-display` | `--btn-display` |
| width | `--{component}-width` | `--input-width` |
| height | `--{component}-height` | `--input-height` |

**Logical Properties:**
```scss
/* Inline = horizontal (left/right) */
--btn-padding-inline: 1.5rem;
--btn-margin-inline: 0.5rem;

/* Block = vertical (top/bottom) */
--btn-padding-block: 0.5rem;
--btn-margin-block: 1rem;
```

---

## rem Units

**All spacing and sizing uses rem units** for accessibility and responsive design.

**Conversion formula:** `px / 16 = rem`

**Common conversions:**
- 8px = 0.5rem
- 12px = 0.75rem
- 16px = 1rem (base)
- 20px = 1.25rem
- 24px = 1.5rem
- 32px = 2rem

**Why rem units?**
- Respects user font size preferences (accessibility)
- Consistent scaling across breakpoints
- Better for responsive design

---

## Discovering Variables

### Method 1: Browser DevTools (Recommended)

1. Inspect a component in your browser
2. Open the **Computed** tab
3. Scroll to **CSS Variables** section
4. See all available variables and their current values

### Method 2: IDE Autocomplete

If using TypeScript/JSX with CSS Modules or styled-components:

```css
/* Type the component prefix */
--btn-   /* IDE shows: --btn-bg, --btn-padding-inline, --btn-radius, etc. */
--alert- /* IDE shows: --alert-error-bg, --alert-success-bg, etc. */
--card-  /* IDE shows: --card-padding, --card-header-bg, etc. */
```

### Method 3: Source Code

Browse the compiled CSS in `node_modules/@fpkit/acss/libs/index.css` to see all available variables.

---

## Customization Strategies

### Global Overrides

Override variables globally in `:root`:

```css
/* global.css */
:root {
  /* Customize all buttons */
  --btn-radius: 0.25rem;
  --btn-padding-inline: 2rem;

  /* Customize primary buttons */
  --btn-primary-bg: #0066cc;
  --btn-primary-color: white;

  /* Customize all cards */
  --card-padding: 1.5rem;
  --card-radius: 0.75rem;
}
```

### Theme Overrides

Create theme classes with custom variables:

```css
/* themes.css */
.light-theme {
  --btn-bg: white;
  --btn-color: #333;
  --card-bg: #f9f9f9;
}

.dark-theme {
  --btn-bg: #2d2d2d;
  --btn-color: #f0f0f0;
  --card-bg: #1a1a1a;
  --card-border: 1px solid #444;
}
```

```jsx
// Apply theme
<div className="dark-theme">
  <Button>Styled by theme</Button>
  <Card>Also themed</Card>
</div>
```

### Component-Specific Overrides

Override variables for specific instances:

```css
/* custom-components.css */
.hero-button {
  --btn-padding-inline: 3rem;
  --btn-padding-block: 1rem;
  --btn-fs: 1.25rem;
  --btn-radius: 0.5rem;
}

.compact-card {
  --card-padding: 0.75rem;
  --card-header-padding: 0.75rem 1rem;
  --card-footer-padding: 0.75rem 1rem;
}
```

```jsx
<Button className="hero-button">Large CTA</Button>
<Card className="compact-card">Compact content</Card>
```

### Inline Overrides

Use inline styles for dynamic or one-off customization:

```jsx
<Button
  style={{
    '--btn-bg': '#e63946',
    '--btn-color': 'white',
  }}
>
  Danger Action
</Button>
```

---

## Component Variable Reference

### Button Variables

```scss
// Base properties
--btn-display: inline-flex
--btn-padding-inline: 1.5rem
--btn-padding-block: 0.5rem
--btn-fs: 1rem
--btn-fw: 600
--btn-radius: 0.375rem
--btn-gap: 0.5rem

// Variants
--btn-primary-bg: #0066cc
--btn-primary-color: white
--btn-secondary-bg: transparent
--btn-secondary-color: currentColor

// States
--btn-hover-bg: brightness(1.1)
--btn-focus-outline: 2px solid currentColor
--btn-focus-outline-offset: 2px
--btn-disabled-opacity: 0.6
```

### Alert Variables

```scss
// Base properties
--alert-padding: 1rem
--alert-radius: 0.375rem
--alert-border-width: 1px

// Semantic variants
--alert-error-bg: #f8d7da
--alert-error-border: #f5c6cb
--alert-error-color: #721c24

--alert-success-bg: #d4edda
--alert-success-border: #c3e6cb
--alert-success-color: #155724

--alert-warning-bg: #fff3cd
--alert-warning-border: #ffeaa7
--alert-warning-color: #856404

--alert-info-bg: #d1ecf1
--alert-info-border: #bee5eb
--alert-info-color: #0c5460
```

### Card Variables

```scss
// Base properties
--card-padding: 1rem
--card-bg: white
--card-radius: 0.5rem
--card-border: 1px solid #e0e0e0

// Header
--card-header-padding: 1rem 1.5rem
--card-header-bg: #f9f9f9
--card-header-border-bottom: 1px solid #e0e0e0
--card-header-fs: 1.25rem
--card-header-fw: 600

// Footer
--card-footer-padding: 1rem 1.5rem
--card-footer-bg: #f9f9f9
--card-footer-border-top: 1px solid #e0e0e0
```

---

## Variant Organization

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

// Secondary button (medium emphasis)
--btn-secondary-bg: transparent;
--btn-secondary-color: #0066cc;
```

---

## State Variables

States represent interactive or conditional component appearances.

### Common States

| State | Description | Example Use |
|-------|-------------|-------------|
| `hover` | Mouse hover | `--btn-hover-bg` |
| `focus` | Keyboard focus | `--btn-focus-outline` |
| `active` | Active/pressed | `--btn-active-transform` |
| `disabled` | Disabled state | `--btn-disabled-opacity` |
| `visited` | Visited link | `--link-visited-color` |
| `checked` | Checked input | `--checkbox-checked-bg` |

### State Examples

```scss
// Hover state
--btn-hover-bg: #0052a3;
--btn-hover-transform: translateY(-1px);

// Focus state
--btn-focus-outline: 2px solid currentColor;
--btn-focus-outline-offset: 2px;

// Disabled state
--btn-disabled-opacity: 0.6;
--btn-disabled-cursor: not-allowed;
```

**Note on Disabled State**: fpkit Button uses `aria-disabled` pattern and automatically applies `.is-disabled` className. Style disabled buttons using this class or the disabled-specific CSS variables:

```css
/* Using CSS variables */
.my-button {
  --btn-disabled-opacity: 0.5;
  --btn-disabled-cursor: not-allowed;
}

/* Or target the .is-disabled class */
.my-button.is-disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
```

---

## Best Practices

### ✅ Do

- **Use the naming pattern** when creating custom variables for your components
- **Use rem units** for spacing and sizing
- **Use logical properties** (`padding-inline`, `padding-block`) for better RTL support
- **Test across themes** to ensure customizations work in all contexts
- **Use semantic naming** for custom variants (e.g., `--btn-danger-bg` not `--btn-red-bg`)

### ❌ Don't

- **Don't use px units** for spacing or sizing (use rem)
- **Don't use forbidden abbreviations** (px/py, w/h, cl, dsp, bdr)
- **Don't use `!important`** unless absolutely necessary
- **Don't create one-off variables** - follow the component pattern

---

## Framework Integration

### React

```jsx
// Global overrides
import './theme.css';

// Component-specific
function CustomButton() {
  return (
    <Button
      style={{
        '--btn-padding-inline': '2rem',
        '--btn-radius': '0.5rem',
      }}
    >
      Custom
    </Button>
  );
}
```

### CSS Modules

```css
/* Button.module.css */
.customButton {
  --btn-primary-bg: #e63946;
  --btn-primary-color: white;
  --btn-padding-inline: 2rem;
}
```

```jsx
import styles from './Button.module.css';

<Button className={styles.customButton}>Custom</Button>
```

### Styled Components

```jsx
import styled from 'styled-components';
import { Button } from '@fpkit/acss';

const CustomButton = styled(Button)`
  --btn-padding-inline: 2rem;
  --btn-radius: 0.5rem;
  --btn-primary-bg: #e63946;
`;
```

---

## Troubleshooting

### Variables Not Applying

1. **Check specificity**: Ensure your selector has equal or higher specificity
2. **Check cascade order**: Import fpkit CSS before your overrides
3. **Check typos**: Variable names are case-sensitive

```css
/* ❌ Won't work - imported after */
@import '@fpkit/acss/libs/index.css';

:root {
  --btn-bg: red; /* Applied first, then overwritten */
}

/* ✅ Works - correct order */
:root {
  --btn-bg: red; /* Overrides fpkit defaults */
}

@import '@fpkit/acss/libs/index.css';
```

### Finding Variable Names

Use browser DevTools Computed tab to see:
- All available variables for an element
- Current values (resolved)
- Where they're defined (inheritance chain)

---

## Additional Resources

- **Component Documentation**: See Storybook for complete component APIs
- **Composition Guide**: `docs/guides/composition.md` for building custom components
- **Accessibility Guide**: `docs/guides/accessibility.md` for WCAG compliance
- **Architecture Guide**: `docs/guides/architecture.md` for component patterns

---

For questions or issues, please visit our [GitHub repository](https://github.com/shawn-sandy/acss).
