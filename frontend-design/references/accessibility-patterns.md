# Accessibility Patterns

## Overview

fpkit components follow WCAG 2.1 Level AA standards. This guide documents accessibility patterns, ARIA attributes, keyboard navigation, and focus management strategies used throughout the library.

---

## Core Principles

### 1. Semantic HTML First

Use the most appropriate HTML element for the job:

```typescript
// ✅ Good - semantic button
<button type="button">Click me</button>

// ❌ Bad - div masquerading as button
<div onClick={handleClick}>Click me</div>
```

The UI component's `as` prop enables semantic HTML:

```typescript
<UI as="button" type="button">Click me</UI>
<UI as="nav" aria-label="Main navigation">...</UI>
<UI as="article" role="article">...</UI>
```

### 2. Keyboard Navigation

All interactive elements must be keyboard accessible:

- **Tab**: Navigate between focusable elements
- **Enter/Space**: Activate buttons and links
- **Arrow keys**: Navigate within composite widgets (menus, tabs, lists)
- **Escape**: Close modals and dialogs

### 3. Focus Management

- **Visible focus indicators**: `:focus-visible` for keyboard users
- **Focus trapping**: Keep focus within modals
- **Focus restoration**: Return focus when closing overlays
- **Skip links**: Allow users to skip navigation

### 4. Screen Reader Support

- **Descriptive labels**: Every interactive element has a label
- **Alternative text**: Images have meaningful alt text
- **ARIA attributes**: Enhance semantics when HTML is insufficient
- **Live regions**: Announce dynamic content changes

---

## ARIA Attributes

### Common ARIA Patterns

#### Labels and Descriptions

```typescript
// aria-label: Provides a label when no visible label exists
<button aria-label="Close dialog">
  <Icon name="close" />
</button>

// aria-labelledby: References visible text as the label
<dialog aria-labelledby="dialog-title">
  <h2 id="dialog-title">Confirm Action</h2>
</dialog>

// aria-describedby: Additional description
<input
  type="email"
  aria-describedby="email-hint"
/>
<div id="email-hint">We'll never share your email</div>
```

#### States and Properties

```typescript
// aria-disabled: For elements that look disabled but remain focusable
<button aria-disabled="true" onClick={handleClick}>
  Submit
</button>

// aria-expanded: Disclosure widgets (dropdowns, accordions)
<button aria-expanded={isOpen} aria-controls="menu-list">
  Menu
</button>

// aria-pressed: Toggle buttons
<button aria-pressed={isPressed} onClick={togglePress}>
  Bold
</button>

// aria-hidden: Hide decorative elements from screen readers
<span aria-hidden="true">→</span>
```

#### Live Regions

```typescript
// aria-live: Announce dynamic content changes
<div aria-live="polite" aria-atomic="true">
  {statusMessage}
</div>

// Role alert: For important messages
<div role="alert">
  Form submission failed. Please check your input.
</div>
```

---

## Button Patterns

### Why aria-disabled Instead of disabled?

fpkit buttons use `aria-disabled` instead of the native `disabled` attribute:

```typescript
// ✅ fpkit pattern
<button aria-disabled="true" onClick={handleClick}>
  Submit
</button>

// ❌ Avoid native disabled
<button disabled>Submit</button>
```

**Benefits:**
- **Keyboard accessible**: Disabled buttons remain in tab order
- **Screen reader context**: Users understand why the button is disabled
- **Tooltip compatible**: Can show why button is disabled
- **Consistent styling**: Easier to style with CSS

**Implementation:**

```typescript
const Button = ({ disabled, onClick, ...props }: ButtonProps) => {
  const handleClick = (e: React.MouseEvent) => {
    if (disabled) {
      e.preventDefault()
      return
    }
    onClick?.(e)
  }

  return (
    <UI
      as="button"
      aria-disabled={disabled}
      onClick={handleClick}
      {...props}
    />
  )
}
```

### Button Types

Always specify button type:

```typescript
// ✅ Explicit type
<button type="button">Cancel</button>
<button type="submit">Save</button>
<button type="reset">Clear Form</button>

// ❌ Implicit type (defaults to submit in forms)
<button>Click me</button>
```

---

## Interactive Card Pattern

### Making Non-Interactive Elements Interactive

When a card needs to be clickable:

```typescript
const Card = ({ interactive, onClick, ...props }: CardProps) => {
  const interactiveProps = interactive
    ? {
        role: 'button',
        tabIndex: 0,
        onClick,
        onKeyDown: (e: React.KeyboardEvent) => {
          if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault()
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

**Requirements:**
- `role="button"`: Announces as interactive
- `tabIndex={0}`: Makes focusable
- `onClick`: Handle mouse clicks
- `onKeyDown`: Handle Enter and Space keys
- `aria-label` or `aria-labelledby`: Descriptive label

---

## Focus Visible Pattern

Use `:focus-visible` to show focus only for keyboard users:

```scss
button {
  // No default focus outline (removed for mouse users)
  outline: none;

  // Only show outline for keyboard navigation
  &:focus-visible {
    outline: 2px solid var(--btn-focus-outline);
    outline-offset: var(--btn-focus-outline-offset, 2px);
  }
}
```

**WCAG 2.4.7: Focus Visible** - Any keyboard operable interface has a visible focus indicator.

---

## Link Patterns

### Internal vs External Links

```typescript
// Internal navigation link
<Link href="/about">About Us</Link>

// External link (opens in new tab)
<Link
  href="https://example.com"
  target="_blank"
  rel="noopener noreferrer"
>
  External Site
  <span className="sr-only">(opens in new tab)</span>
</Link>
```

### Visited Link State

Maintain visited link styling for usability:

```scss
a {
  color: var(--link-color);

  &:visited {
    color: var(--link-visited-color);
  }

  &:hover,
  &:focus {
    color: var(--link-hover-color);
    text-decoration: underline;
  }
}
```

---

## Form Patterns

### Field Labels

Always associate labels with inputs:

```typescript
// ✅ Explicit association
<label htmlFor="email">Email Address</label>
<input id="email" type="email" name="email" />

// ✅ Implicit association
<label>
  Email Address
  <input type="email" name="email" />
</label>

// ❌ No association
<label>Email Address</label>
<input type="email" name="email" />
```

### Error Messages

Link error messages to inputs:

```typescript
<label htmlFor="password">Password</label>
<input
  id="password"
  type="password"
  aria-describedby="password-error"
  aria-invalid={hasError}
/>
{hasError && (
  <div id="password-error" role="alert">
    Password must be at least 8 characters
  </div>
)}
```

### Required Fields

```typescript
<label htmlFor="name">
  Name <span aria-label="required">*</span>
</label>
<input
  id="name"
  type="text"
  required
  aria-required="true"
/>
```

---

## Modal/Dialog Patterns

### Focus Trap

```typescript
const Dialog = ({ open, onClose, children }: DialogProps) => {
  const dialogRef = React.useRef<HTMLDialogElement>(null)

  React.useEffect(() => {
    if (open) {
      dialogRef.current?.showModal()
      // Trap focus within dialog
      const focusableElements = dialogRef.current?.querySelectorAll(
        'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
      )
      // Focus first element
      (focusableElements?.[0] as HTMLElement)?.focus()
    } else {
      dialogRef.current?.close()
    }
  }, [open])

  return (
    <dialog
      ref={dialogRef}
      aria-labelledby="dialog-title"
      aria-modal="true"
    >
      {children}
    </dialog>
  )
}
```

### Escape Key Handling

```typescript
React.useEffect(() => {
  const handleEscape = (e: KeyboardEvent) => {
    if (e.key === 'Escape' && open) {
      onClose()
    }
  }

  document.addEventListener('keydown', handleEscape)
  return () => document.removeEventListener('keydown', handleEscape)
}, [open, onClose])
```

---

## Screen Reader Only Content

### Visually Hidden Pattern

```scss
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border-width: 0;
}
```

### Usage

```typescript
<button>
  <Icon name="close" aria-hidden="true" />
  <span className="sr-only">Close dialog</span>
</button>
```

---

## Color Contrast

### WCAG AA Requirements

- **Normal text**: 4.5:1 contrast ratio minimum
- **Large text** (18pt+): 3:1 contrast ratio minimum
- **UI components**: 3:1 for interactive elements

### CSS Variable Design

```scss
:root {
  // Good contrast by default
  --btn-primary-bg: #0066cc;      // Blue
  --btn-primary-color: #ffffff;    // White (meets AA)

  // Error colors with sufficient contrast
  --alert-error-bg: #f8d7da;
  --alert-error-color: #721c24;    // Dark red (meets AA)
}
```

---

## Landmarks and Regions

### Semantic HTML5 Elements

```typescript
<header>
  <nav aria-label="Main navigation">...</nav>
</header>

<main>
  <article>
    <header>...</header>
    <section>...</section>
    <aside>...</aside>
  </article>
</main>

<footer>
  <nav aria-label="Footer navigation">...</nav>
</footer>
```

### Multiple Landmarks of Same Type

Use `aria-label` to differentiate:

```typescript
<nav aria-label="Main navigation">...</nav>
<nav aria-label="Footer navigation">...</nav>

<aside aria-label="Related articles">...</aside>
<aside aria-label="Advertisement">...</aside>
```

---

## Testing Accessibility

### Manual Testing

1. **Keyboard Navigation**
   - Tab through all interactive elements
   - Activate with Enter/Space
   - Close modals with Escape

2. **Screen Reader Testing**
   - VoiceOver (macOS/iOS)
   - NVDA (Windows)
   - JAWS (Windows)

3. **Browser DevTools**
   - Lighthouse accessibility audit
   - Accessibility tree inspection
   - Color contrast analyzer

### Automated Testing

```typescript
import { axe } from 'jest-axe'

it('should not have accessibility violations', async () => {
  const { container } = render(<Button>Click me</Button>)
  const results = await axe(container)
  expect(results).toHaveNoViolations()
})
```

---

## WCAG 2.1 Level AA Checklist

### Perceivable

- [ ] Text alternatives for non-text content
- [ ] Captions for audio/video
- [ ] Content can be presented in different ways
- [ ] Sufficient color contrast (4.5:1 for normal text, 3:1 for large)

### Operable

- [ ] All functionality available via keyboard
- [ ] Users have enough time to interact
- [ ] No content causes seizures (no flashing > 3 times per second)
- [ ] Users can navigate and find content
- [ ] Multiple ways to navigate (search, sitemap, links)

### Understandable

- [ ] Text is readable and understandable
- [ ] Content appears and operates in predictable ways
- [ ] Users are helped to avoid and correct mistakes

### Robust

- [ ] Content is compatible with assistive technologies
- [ ] Valid HTML (no duplicate IDs, proper nesting)
- [ ] ARIA used correctly

---

## Common Accessibility Mistakes

### ❌ Don't

- Use `div` or `span` as buttons
- Remove focus outlines without providing alternatives
- Use `placeholder` as a label replacement
- Use color alone to convey information
- Create keyboard traps (can't tab out)
- Use positive `tabindex` values (messes with tab order)
- Announce every state change (overwhelming for screen readers)

### ✅ Do

- Use semantic HTML elements
- Provide visible focus indicators
- Include proper labels for all form controls
- Use multiple cues (color + icon, color + text)
- Ensure modals trap focus intentionally
- Use `tabindex="0"` for custom interactive elements
- Use `aria-live="polite"` for non-critical updates

---

## Resources

### WCAG Guidelines

- [WCAG 2.1 Quick Reference](https://www.w3.org/WAI/WCAG21/quickref/)
- [WCAG 2.1 Understanding Docs](https://www.w3.org/WAI/WCAG21/Understanding/)

### ARIA

- [WAI-ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/)
- [ARIA in HTML](https://www.w3.org/TR/html-aria/)

### Testing Tools

- [axe DevTools](https://www.deque.com/axe/devtools/)
- [WAVE Browser Extension](https://wave.webaim.org/extension/)
- [Lighthouse](https://developers.google.com/web/tools/lighthouse)
- [jest-axe](https://github.com/nickcolley/jest-axe)
