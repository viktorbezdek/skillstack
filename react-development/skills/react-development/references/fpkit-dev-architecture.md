# Architecture Guide

## Overview

@fpkit/acss follows consistent architectural patterns that ensure maintainability, type safety, accessibility, and reusability. This guide explains these patterns to help you use and compose fpkit components effectively.

---

## The UI Component Foundation

All fpkit components are built on a polymorphic `UI` base component that provides:

- **Polymorphic rendering** - Render as any HTML element via `as` prop
- **Type-safe prop spreading** - Full TypeScript support
- **Style merging** - Combine default and custom styles
- **Ref forwarding** - For focus management
- **Automatic ARIA** - Attribute forwarding

###  Understanding Polymorphism

The `as` prop lets you change the rendered HTML element while preserving component behavior:

```tsx
import { Button, Card } from '@fpkit/acss'

// Button as link
<Button as="a" href="/page">
  Navigate
</Button>
// Renders: <a href="/page">Navigate</a>

// Card as section instead of article
<Card as="section">
  Content
</Card>
// Renders: <section>Content</section>

// Badge as span instead of sup
<Badge as="span">
  Label
</Badge>
// Renders: <span>Label</span>
```

**Why this matters:**
- Semantic HTML flexibility
- Better accessibility (correct element for the job)
- SEO benefits (proper HTML structure)
- CSS targeting (style based on element type)

---

## Component Patterns

### Simple Components

Standalone components with no sub-components.

**Examples**: Badge, Button, Tag, Icon

```tsx
import { Badge } from '@fpkit/acss'

// Simple component with variant
<Badge variant="rounded">New</Badge>

// Polymorphic - render as different element
<Badge as="span">Label</Badge>

// Custom styles via CSS variables
<Badge style={{ '--badge-bg': '#ff0000' }}>
  Alert
</Badge>
```

**Characteristics:**
- Single export
- Props extend base HTML element props
- Variants via `data-*` attributes
- Customizable via CSS variables

---

### Compound Components

Complex components with multiple related sub-components.

**Examples**: Card, Dialog, Alert, Form

```tsx
import { Card } from '@fpkit/acss'

// Using sub-components
<Card>
  <Card.Header>
    <Card.Title>Title</Card.Title>
  </Card.Header>
  <Card.Content>
    Content goes here
  </Card.Content>
  <Card.Footer>
    <Button>Action</Button>
  </Card.Footer>
</Card>

// Or import individually
import { Card, CardHeader, CardTitle, CardContent, CardFooter } from '@fpkit/acss'

<Card>
  <CardHeader>
    <CardTitle>Title</CardTitle>
  </CardHeader>
  <CardContent>Content</CardContent>
  <CardFooter>
    <Button>Action</Button>
  </CardFooter>
</Card>
```

**Characteristics:**
- Main component + sub-components
- Available as `Component.SubComponent` or individual exports
- Each sub-component is independently customizable
- Flexible composition (use what you need)

---

## TypeScript Support

### Component Props

All fpkit components are fully typed:

```tsx
import type { ButtonProps, CardProps } from '@fpkit/acss'

// Extend fpkit component props
interface CustomButtonProps extends ButtonProps {
  loading?: boolean
  loadingText?: string
}

const CustomButton = ({
  loading,
  loadingText = 'Loading...',
  children,
  ...props
}: CustomButtonProps) => {
  return (
    <Button {...props}>
      {loading ? loadingText : children}
    </Button>
  )
}
```

### Polymorphic Types

Types adapt based on the `as` prop:

```tsx
// Button as button - button props available
<Button type="submit" onClick={handleClick}>
  Submit
</Button>

// Button as link - anchor props available
<Button as="a" href="/page" target="_blank">
  Link
</Button>

// Button as div - div props available
<Button as="div" onKeyDown={handleKeyDown}>
  Custom
</Button>
```

### Generic Props Pattern

```tsx
import type { ComponentProps } from 'react'
import { Button } from '@fpkit/acss'

// Get button props type
type BaseButtonProps = ComponentProps<typeof Button>

// Extend with custom props
interface MyButtonProps extends BaseButtonProps {
  icon?: string
  badge?: number
}
```

---

## Composition Patterns

### Pattern 1: Container + Content

Wrap fpkit components with additional structure:

```tsx
import { Button, Badge } from '@fpkit/acss'

export const StatusButton = ({ status, children, ...props }) => {
  return (
    <Button {...props}>
      {children}
      <Badge variant={status}>{status}</Badge>
    </Button>
  )
}

// Usage
<StatusButton status="active">Server Status</StatusButton>
```

### Pattern 2: Conditional Composition

Different combinations based on props:

```tsx
import { Alert, Dialog } from '@fpkit/acss'

export const Notification = ({ inline, variant, children, ...props }) => {
  if (inline) {
    return <Alert variant={variant}>{children}</Alert>
  }

  return (
    <Dialog {...props}>
      <Alert variant={variant}>{children}</Alert>
    </Dialog>
  )
}

// Usage
<Notification inline variant="success">Saved!</Notification>
<Notification isOpen={showModal} variant="error">Error!</Notification>
```

### Pattern 3: Enhanced Wrapper

Add behavior around fpkit components:

```tsx
import { Button } from '@fpkit/acss'
import { useState } from 'react'

export const LoadingButton = ({ loading, onClick, children, ...props }) => {
  const [isLoading, setIsLoading] = useState(loading)

  const handleClick = async (e) => {
    setIsLoading(true)
    try {
      await onClick?.(e)
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <Button
      {...props}
      disabled={isLoading || props.disabled}
      onClick={handleClick}
    >
      {isLoading ? 'Loading...' : children}
    </Button>
  )
}

// Usage
<LoadingButton onClick={async () => await saveData()}>
  Save
</LoadingButton>
```

See the [Composition Guide](./composition.md) for more patterns and examples.

---

## Styling Architecture

### Attribute-Based Variants

fpkit uses `data-*` attributes for variants:

```tsx
// Component
<Button variant="primary" size="large">Click me</Button>

// Renders as
<button data-btn="primary large">Click me</button>

// Styled with SCSS
button[data-btn~="primary"] {
  background: var(--btn-primary-bg);
}

button[data-btn~="large"] {
  font-size: var(--btn-size-lg);
}
```

**Benefits:**
- Multiple variants on same element
- Clean HTML output
- Type-safe variants in TypeScript
- Easy CSS targeting

### CSS Variable Integration

All styling uses CSS custom properties:

```tsx
// Global overrides
:root {
  --btn-primary-bg: #0066cc;
  --btn-padding-inline: 2rem;
}

// Component-specific overrides
<Button
  style={{
    '--btn-bg': '#e63946',
    '--btn-color': 'white',
  }}
>
  Custom
</Button>

// CSS class overrides
.hero-button {
  --btn-padding-inline: 3rem;
  --btn-fs: 1.25rem;
}
```

See the [CSS Variables Guide](./css-variables.md) for complete customization options.

---

## Props Patterns

### Common Props

All fpkit components accept these common props:

```tsx
// className - additional CSS classes
<Button className="custom-button">Click</Button>

// style - inline styles
<Button style={{ marginTop: '1rem' }}>Click</Button>

// data-* - custom data attributes
<Button data-testid="submit-btn">Click</Button>

// aria-* - accessibility attributes
<Button aria-label="Close dialog">×</Button>

// ref - React ref
const ref = useRef()
<Button ref={ref}>Click</Button>

// as - polymorphic element
<Button as="a" href="/page">Link</Button>
```

### Variant Props

Components use semantic variant names:

```tsx
// Button variants
<Button variant="primary">Primary</Button>
<Button variant="secondary">Secondary</Button>
<Button variant="danger">Danger</Button>

// Alert variants
<Alert variant="error">Error message</Alert>
<Alert variant="success">Success message</Alert>
<Alert variant="warning">Warning message</Alert>
<Alert variant="info">Info message</Alert>

// Badge variants
<Badge variant="rounded">Rounded</Badge>
<Badge variant="pill">Pill</Badge>
```

### Size Props

When components support sizing:

```tsx
<Button size="small">Small</Button>
<Button size="medium">Medium</Button>
<Button size="large">Large</Button>
```

### Boolean Props

State and behavior props:

```tsx
// Disabled state
<Button disabled>Disabled</Button>

// Interactive cards
<Card interactive onClick={handleClick}>Clickable</Card>

// Modal/dialog states
<Dialog isOpen={isOpen} onClose={handleClose}>Content</Dialog>

// Dismissable alerts
<Alert onClose={handleClose}>Dismissable</Alert>
```

---

## Accessibility Architecture

### Semantic HTML

fpkit components render as appropriate semantic elements:

| Component | Default Element | Purpose |
|-----------|----------------|---------|
| Button | `<button>` | Interactive action |
| Card | `<article>` | Self-contained content |
| Alert | `<div role="alert">` | Important message |
| Dialog | `<dialog>` | Modal content |
| Nav | `<nav>` | Navigation menu |

### ARIA Attributes

Components include built-in ARIA:

```tsx
// Button disabled state
<Button disabled>
// Renders: <button aria-disabled="true">

// Alert role
<Alert variant="error">
// Renders: <div role="alert">

// Dialog modal
<Dialog isOpen>
// Renders: <dialog aria-modal="true">

// Expandable elements
<Accordion expanded>
// Renders: <div aria-expanded="true">
```

### Keyboard Navigation

All interactive components support:
- **Tab**: Focus navigation
- **Enter/Space**: Activation
- **Escape**: Close modals/dialogs
- **Arrow keys**: Navigate lists/menus

See the [Accessibility Guide](./accessibility.md) for complete patterns.

---

## Component Lifecycle

### Initialization

```tsx
// Components accept default HTML element props
<Button onClick={handleClick}>Click</Button>

// Plus component-specific props
<Button variant="primary" disabled>Click</Button>

// Props spread to underlying element
<Button data-testid="btn" aria-label="Submit">
  Submit
</Button>
```

### Updates

```tsx
// Props update reactively
const [disabled, setDisabled] = useState(false)

<Button disabled={disabled}>
  {disabled ? 'Disabled' : 'Enabled'}
</Button>

// CSS variables update in real-time
const [color, setColor] = useState('#0066cc')

<Button style={{ '--btn-bg': color }}>
  Dynamic Color
</Button>
```

### Cleanup

```tsx
// Refs are properly forwarded
const buttonRef = useRef<HTMLButtonElement>(null)

useEffect(() => {
  // Access DOM element directly
  buttonRef.current?.focus()

  return () => {
    // Cleanup if needed
  }
}, [])

<Button ref={buttonRef}>Click</Button>
```

---

## Best Practices

### ✅ Do

- **Use semantic elements** - Leverage the `as` prop for correct HTML
- **Compose over create** - Combine fpkit components rather than building from scratch
- **Extend props properly** - Use TypeScript to extend component props
- **Customize with CSS variables** - Override styles without modifying components
- **Preserve accessibility** - Keep ARIA attributes and keyboard navigation
- **Forward refs** - When wrapping components, forward refs appropriately

```tsx
// ✅ Good - proper composition
import { forwardRef } from 'react'
import { Button, type ButtonProps } from '@fpkit/acss'

interface LoadingButtonProps extends ButtonProps {
  loading?: boolean
}

export const LoadingButton = forwardRef<HTMLButtonElement, LoadingButtonProps>(
  ({ loading, children, ...props }, ref) => {
    return (
      <Button ref={ref} {...props} disabled={loading || props.disabled}>
        {loading ? 'Loading...' : children}
      </Button>
    )
  }
)
```

### ❌ Don't

- **Don't duplicate components** - Reuse existing fpkit components
- **Don't break accessibility** - Maintain ARIA attributes and keyboard support
- **Don't hardcode styles** - Use CSS variables for customization
- **Don't ignore types** - Leverage TypeScript for type safety
- **Don't nest interactive elements** - Avoid `<button>` inside `<a>`

```tsx
// ❌ Bad - duplicating fpkit logic
export const MyBadge = ({ children }) => {
  return <span className="my-badge">{children}</span>
}

// ✅ Good - reuse fpkit component
import { Badge } from '@fpkit/acss'
export const MyBadge = Badge
```

---

## Component API Patterns

### Children Prop

```tsx
// String children
<Button>Click me</Button>

// Element children
<Button>
  <Icon name="save" />
  Save
</Button>

// Render prop pattern
<Card>
  {({ isHovered }) => (
    <div>Content {isHovered ? 'hovered' : ''}</div>
  )}
</Card>
```

### Event Handlers

```tsx
// Mouse events
<Button onClick={handleClick}>Click</Button>
<Button onMouseEnter={handleHover}>Hover</Button>

// Keyboard events
<Input onKeyDown={handleKeyPress} />

// Form events
<Input onChange={handleChange} />
<Form onSubmit={handleSubmit} />

// Custom events
<Dialog onClose={handleClose} />
<Alert onDismiss={handleDismiss} />
```

### Render Props

```tsx
// Custom rendering
<Select>
  {(option) => (
    <div>
      <Icon name={option.icon} />
      {option.label}
    </div>
  )}
</Select>
```

---

## Framework Integration

### React

fpkit is designed for React:

```tsx
import { Button, Card } from '@fpkit/acss'

export default function App() {
  return (
    <Card>
      <Card.Title>Welcome</Card.Title>
      <Card.Content>
        <p>Content here</p>
        <Button variant="primary">Action</Button>
      </Card.Content>
    </Card>
  )
}
```

### Next.js

Works seamlessly with Next.js:

```tsx
import { Button } from '@fpkit/acss'
import Link from 'next/link'

// Button as Next.js Link
<Button as={Link} href="/page">
  Navigate
</Button>
```

### TypeScript

Full type safety:

```tsx
import type { ButtonProps } from '@fpkit/acss'

// Type-safe custom component
const CustomButton = (props: ButtonProps) => {
  return <Button {...props} />
}
```

---

## Additional Resources

- **[Composition Guide](./composition.md)** - Component composition patterns and strategies
- **[CSS Variables Guide](./css-variables.md)** - Styling and customization
- **[Accessibility Guide](./accessibility.md)** - WCAG compliance and ARIA patterns
- **[Testing Guide](./testing.md)** - Testing strategies for fpkit components

---

## Summary

@fpkit/acss architecture provides:

1. **Polymorphic Components** - Flexible HTML element rendering via `as` prop
2. **Compound Components** - Complex UIs with sub-components
3. **Composition-First** - Build custom components by combining primitives
4. **Type Safety** - Full TypeScript support with proper prop types
5. **CSS Variables** - Customizable styling without component modification
6. **Accessibility** - Built-in WCAG 2.1 AA compliance

Understanding these patterns helps you use fpkit effectively and build maintainable, accessible applications.
