# Component Architecture Patterns

## Overview

fpkit components follow consistent architectural patterns that ensure maintainability, type safety, accessibility, and reusability. This guide documents the core patterns used throughout the library.

---

## The UI Component Foundation

All fpkit components are built on top of the polymorphic `UI` component, which provides:

- **Polymorphic rendering** via `as` prop (render as any HTML element)
- **Type-safe prop spreading** with TypeScript
- **Style merging** (defaultStyles + custom styles)
- **Ref forwarding** for focus management
- **Automatic ARIA attribute forwarding**

### Basic Usage Pattern

```typescript
import { UI } from '#components/ui'

export const MyComponent = ({ children, ...props }: MyComponentProps) => {
  return (
    <UI as="div" {...props}>
      {children}
    </UI>
  )
}
```

### Props Extension Pattern

```typescript
import type { React } from 'react'
import type { UI } from '#components/ui'

// Extend UI component props
export type MyComponentProps = Partial<React.ComponentProps<typeof UI>> & {
  variant?: 'primary' | 'secondary'
  size?: 'small' | 'medium' | 'large'
}
```

---

## Component File Structure

Every component follows a consistent 5-file structure:

```
components/
└── my-component/
    ├── my-component.tsx          # Component implementation
    ├── my-component.types.ts     # Type definitions (for complex components)
    ├── my-component.scss         # Styles with CSS variables
    ├── my-component.stories.tsx  # Storybook stories
    └── my-component.test.tsx     # Vitest tests
```

### When to Use Separate Types File

**Use `component.types.ts` when:**
- Component has complex type definitions (>50 lines)
- Multiple related interfaces/types need to be exported
- Compound component with sub-component types
- Types are reused across multiple files

**Use inline types when:**
- Simple components with few props (<20 lines of types)
- Types are only used within the component file
- No compound components or sub-components

**Examples:**
- Button: Inline types (simple props)
- Badge: Inline types (simple props)
- Card: Separate types file (compound component with multiple interfaces)

---

## Simple Component Pattern

Used for standalone components with no sub-components.

### Structure

```typescript
import * as React from 'react'
import { UI } from '#components/ui'

/**
 * Component description
 *
 * @example
 * ```tsx
 * <Badge>New</Badge>
 * ```
 */
export const Badge = ({ children, variant, ...props }: BadgeProps) => {
  return (
    <UI as="sup" data-badge={variant} {...props}>
      <span>{children}</span>
    </UI>
  )
}

Badge.displayName = 'Badge'

// Types defined inline
export type BadgeProps = {
  children?: React.ReactNode
  variant?: 'rounded'
} & React.ComponentProps<typeof UI>
```

### Key Characteristics

- Single component export
- Props extend `React.ComponentProps<typeof UI>`
- Uses `data-*` attributes for styling variants
- Always includes displayName for debugging
- JSDoc documentation with examples

---

## Compound Component Pattern

Used for complex components with multiple related sub-components.

### Structure

```typescript
import * as React from 'react'
import { UI } from '#components/ui'
import type { CardProps, CardTitleProps } from './card.types'

/**
 * Card component with sub-components
 */
export const Card = ({ children, interactive, ...props }: CardProps) => {
  // Component logic
  return (
    <UI as="article" {...props}>
      {children}
    </UI>
  )
}

Card.displayName = 'Card'

/**
 * Card title sub-component
 */
export const Title = ({ as = 'h2', children, ...props }: CardTitleProps) => {
  return (
    <UI as={as} {...props}>
      {children}
    </UI>
  )
}

Title.displayName = 'Card.Title'

// Export as compound component
Card.Title = Title
export { Card, Title as CardTitle }
```

### Key Characteristics

- Main component + sub-components
- Each sub-component has own displayName
- Sub-components attached as static properties
- Types in separate file
- Exports both compound (Card.Title) and individual (CardTitle) forms

---

## Component Reuse Strategies

fpkit prioritizes **composition over duplication**. Before creating a new component, always evaluate opportunities to reuse existing components.

### The Reuse Decision Matrix

| Scenario | Strategy | Implementation |
|----------|----------|----------------|
| Component already exists | **Extend** | Add variant or new prop to existing component |
| 2+ existing components combine | **Compose** | Import and combine existing components |
| >50% similar to existing | **Adapt** | Extend or compose with modifications |
| Novel UI primitive | **Create New** | Scaffold with UI base component |

### Strategy 1: Composition (Preferred)

**When to use**: Build new components by combining existing ones.

```typescript
// ✅ Good: Compose from existing components
import { Badge } from '../badge/badge'
import { Button } from '../buttons/button'

export const StatusButton = ({ status, children, ...props }) => {
  return (
    <Button {...props}>
      {children}
      <Badge variant={status}>{status}</Badge>
    </Button>
  )
}
```

**Benefits**:
- Maintains consistency across the library
- Leverages existing tests and accessibility features
- Reduces code duplication
- Easier to maintain (bug fixes propagate automatically)

### Strategy 2: Extension

**When to use**: Add functionality to an existing component without breaking changes.

```typescript
// ✅ Good: Extend existing component
import { Alert, type AlertProps } from '../alert/alert'

export type EnhancedAlertProps = AlertProps & {
  dismissable?: boolean
  onDismiss?: () => void
}

export const EnhancedAlert = ({
  dismissable,
  onDismiss,
  children,
  ...props
}: EnhancedAlertProps) => {
  return (
    <Alert {...props}>
      {children}
      {dismissable && (
        <button onClick={onDismiss} aria-label="Dismiss">
          ×
        </button>
      )}
    </Alert>
  )
}
```

**Considerations**:
- If extension is widely useful, consider contributing variant to base component
- Document what's new vs inherited
- Maintain backward compatibility with base component

### Strategy 3: Create New (Last Resort)

**When to use**: Only when composition or extension is not viable.

```typescript
// ✅ Good: New primitive component
import { UI } from '#components/ui'

export const Tooltip = ({ content, children, ...props }: TooltipProps) => {
  const [visible, setVisible] = React.useState(false)

  return (
    <UI as="span" data-tooltip {...props}>
      {children}
      {visible && <span role="tooltip">{content}</span>}
    </UI>
  )
}
```

**Requirements for new components**:
- Must be a truly novel UI pattern
- Cannot be reasonably composed from existing components
- Provides reusable value to the library
- Follows all fpkit patterns and conventions

### Automated Reuse Detection

The fpkit-component-builder skill includes automated tools to suggest reuse:

```bash
# Analyze and get recommendations
python3 scripts/recommend_approach.py ComponentName

# Scaffold with composition mode
python3 scripts/scaffold_component.py StatusButton \
  --mode compose \
  --uses Badge,Button
```

### Reuse Anti-Patterns

**❌ Avoid: Creating duplicate components**

```typescript
// ❌ Bad: Duplicating Badge logic
export const Label = ({ children, color }) => {
  return <span className={`label label-${color}`}>{children}</span>
}

// ✅ Good: Reuse Badge
import { Badge } from '../badge/badge'
export const Label = Badge  // or create alias
```

**❌ Avoid: Over-wrapping without value**

```typescript
// ❌ Bad: Wrapper adds no value
export const MyButton = (props) => <Button {...props} />

// ✅ Good: Only wrap if adding functionality
export const MyButton = ({ loading, ...props }) => (
  <Button disabled={loading} {...props}>
    {loading && <Spinner />}
    {props.children}
  </Button>
)
```

### Composition Best Practices

1. **Import smartly**: Use path aliases for clean imports
2. **Document composition**: JSDoc should list all composed components
3. **Minimal custom styles**: Reuse base component styles
4. **Test integration**: Test how components work together
5. **Export properly**: Include composed components in index.ts

**Example with best practices**:

```typescript
import * as React from 'react'
import { Badge } from '../badge/badge'
import { Button } from '../buttons/button'
import { Icon } from '../icons/icon'

/**
 * StatusButton - Button with status badge and optional icon
 *
 * Composed from:
 * - Button (primary component)
 * - Badge (status indicator)
 * - Icon (optional decoration)
 *
 * @example
 * ```tsx
 * <StatusButton status="active" icon="check">
 *   Active Server
 * </StatusButton>
 * ```
 */
export const StatusButton = ({
  status,
  icon,
  children,
  ...props
}: StatusButtonProps) => {
  return (
    <Button {...props}>
      {icon && <Icon name={icon} />}
      {children}
      <Badge variant={status}>{status}</Badge>
    </Button>
  )
}

StatusButton.displayName = 'StatusButton'

export type StatusButtonProps = React.ComponentProps<typeof Button> & {
  status: 'active' | 'inactive' | 'pending'
  icon?: string
}
```

### Reference Documentation

For more detailed patterns and examples, see:
- **[Composition Patterns Guide](./composition-patterns.md)** - Detailed composition strategies and examples
- **[CSS Variable Guide](./css-variable-guide.md)** - Styling patterns for composed components
- **[Accessibility Patterns](./accessibility-patterns.md)** - Ensuring composed components remain accessible

---

## Hook Integration Pattern

Components can use custom hooks for shared logic.

### Example: Disabled State Management

```typescript
import { useDisabledState } from '#hooks/use-disabled-state'

export const Button = ({
  disabled,
  isDisabled,
  type = 'button',
  ...props
}: ButtonProps) => {
  // Resolve disabled prop (supports both disabled and isDisabled)
  const resolvedDisabled = useDisabledState({ disabled, isDisabled })

  return (
    <UI
      as="button"
      type={type}
      aria-disabled={resolvedDisabled}
      {...props}
    >
      {props.children}
    </UI>
  )
}
```

### Benefits

- Centralized logic (DRY principle)
- Consistent behavior across components
- Easier to test and maintain
- Reusable across multiple components

---

## Styling Pattern

### Attribute-Based Variants

Use `data-*` attributes to style variants:

```typescript
// Component
<UI as="button" data-btn="primary large" {...props}>

// SCSS
button[data-btn~="primary"] {
  background: var(--btn-primary-bg);
}

button[data-btn~="large"] {
  font-size: var(--btn-size-lg);
}
```

### CSS Variable Integration

```scss
:root {
  // Base properties
  --component-property: value;

  // Variants
  --component-variant-property: value;

  // States
  --component-state-property: value;

  // Elements
  --component-element-property: value;
}

.component {
  property: var(--component-property);

  &:hover {
    property: var(--component-hover-property);
  }
}
```

---

## Conditional Rendering Pattern

Handle optional features or interactive modes:

```typescript
export const Card = ({
  children,
  interactive = false,
  onClick,
  ...props
}: CardProps) => {
  const interactiveProps = interactive
    ? {
        role: 'button',
        tabIndex: 0,
        onClick,
        onKeyDown: (e: React.KeyboardEvent) => {
          if (e.key === 'Enter' || e.key === ' ') {
            onClick?.(e)
          }
        },
      }
    : {}

  return (
    <UI as="article" {...interactiveProps} {...props}>
      {children}
    </UI>
  )
}
```

---

## Development Warnings Pattern

Provide helpful warnings during development:

```typescript
export const Card = ({ 'aria-label': ariaLabel, 'aria-labelledby': ariaLabelledby, ...props }: CardProps) => {
  React.useEffect(() => {
    if (process.env.NODE_ENV === 'development') {
      if (!ariaLabel && !ariaLabelledby && props.interactive) {
        console.warn(
          'Card: Interactive cards should have aria-label or aria-labelledby for accessibility'
        )
      }
    }
  }, [ariaLabel, ariaLabelledby, props.interactive])

  // Component implementation
}
```

---

## Export Patterns

### Index.ts Organization

Components are organized by category in `src/index.ts`:

```typescript
// Core UI components
export { Button, type ButtonProps } from "./components/buttons/button";
export { Badge, type BadgeProps } from "./components/badge/badge";

// Compound components
export {
  Card,
  Title as CardTitle,
  Content as CardContent,
  Footer as CardFooter,
  type CardProps,
} from "./components/cards/card";

// Wildcard exports for related components
export * from "./components/layout/landmarks";
export * from "./components/nav/nav";
```

### Export Checklist

When adding a new component to `index.ts`:

- [ ] Export component by name
- [ ] Export Props type
- [ ] Export sub-components (if compound)
- [ ] Add to appropriate section (Core UI, Layout, Navigation, etc.)
- [ ] Maintain alphabetical order within section
- [ ] Use wildcard exports only for cohesive groups

---

## Path Aliases

fpkit uses TypeScript path aliases for clean imports:

```typescript
// Import from components
import { UI } from '#components/ui'
import { Button } from '#components/buttons/button'

// Import from hooks
import { useDisabledState } from '#hooks/use-disabled-state'

// Import from decorators
import { withAccessibility } from '#decorators/accessibility'
```

### Configured in tsconfig.json

```json
{
  "compilerOptions": {
    "paths": {
      "#*": ["./src/*"],
      "#components/*": ["./src/components/*"],
      "#hooks/*": ["./src/hooks/*"],
      "#decorators/*": ["./src/decorators/*"]
    }
  }
}
```

---

## Best Practices

### ✅ Do

- Build on the UI component for polymorphism
- Use TypeScript strict mode with explicit types
- Include comprehensive JSDoc documentation
- Use displayName for all components
- Follow the 5-file structure
- Use data-attributes for styling variants
- Implement keyboard navigation for interactive components
- Add development warnings for common mistakes

### ❌ Don't

- Hardcode HTML elements (use UI component's `as` prop)
- Mix inline styles with CSS variables
- Skip accessibility attributes
- Forget to export types
- Create components without tests
- Use class-based components (use functional + hooks)
- Ignore TypeScript errors

---

## Component Development Checklist

When creating a new component:

- [ ] Component extends UI component
- [ ] Props interface extends `React.ComponentProps<typeof UI>`
- [ ] JSDoc documentation with examples
- [ ] displayName set for debugging
- [ ] Accessibility attributes (ARIA, role, tabIndex)
- [ ] Keyboard navigation (for interactive components)
- [ ] SCSS file with CSS variables (rem units only)
- [ ] Storybook stories with play functions
- [ ] Vitest tests (rendering, interaction, accessibility)
- [ ] Exported from src/index.ts
- [ ] Validation passes (lint, type-check, CSS vars)
