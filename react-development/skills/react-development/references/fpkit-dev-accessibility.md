# Accessibility Guide

## Overview

@fpkit/acss components follow **WCAG 2.1 Level AA** standards. This guide explains accessibility patterns, ARIA attributes, keyboard navigation, and focus management to help you maintain accessibility when using and composing fpkit components.

---

## Core Principles

### 1. Semantic HTML First

fpkit components use the most appropriate HTML elements by default:

```tsx
// fpkit Button renders as <button>
import { Button } from '@fpkit/acss'
<Button>Click me</Button>
// Renders: <button type="button">Click me</button>

// fpkit Card renders as <article>
import { Card } from '@fpkit/acss'
<Card>Content</Card>
// Renders: <article>Content</article>
```

**Polymorphic Components**: Many fpkit components support the `as` prop for semantic flexibility:

```tsx
// Button as link
<Button as="a" href="/page">Navigate</Button>

// Card as section
<Card as="section">...</Card>
```

### 2. Keyboard Navigation

All fpkit interactive components are keyboard accessible:

- **Tab**: Navigate between focusable elements
- **Enter/Space**: Activate buttons and links
- **Arrow keys**: Navigate within menus, tabs, and lists
- **Escape**: Close modals and dialogs

**Testing**: Try navigating your app using only the keyboard:
```bash
# Tab through interactive elements
# Enter/Space to activate
# Escape to close
```

### 3. Focus Management

fpkit components include built-in focus management:

- **Visible focus indicators**: `:focus-visible` for keyboard users only
- **Focus trapping**: Modals keep focus within the dialog
- **Focus restoration**: Focus returns to trigger element when closing overlays

**Customizing focus styles**:
```css
/* Override focus indicator globally */
:root {
  --btn-focus-outline: 2px solid #0066cc;
  --btn-focus-outline-offset: 2px;
}
```

### 4. Screen Reader Support

fpkit components include appropriate ARIA attributes:

- **Descriptive labels**: Every interactive element has a label
- **Alternative text**: Icons have `aria-label` or `aria-hidden`
- **ARIA attributes**: States and properties for complex widgets
- **Live regions**: Alerts and notifications use proper ARIA roles

---

## ARIA Attributes

### Labels and Descriptions

fpkit components handle basic labeling, but you may need to add context:

```tsx
// Icon-only button needs aria-label
<Button aria-label="Close dialog">
  <Icon name="close" />
</Button>

// Button with visible text - no aria-label needed
<Button>
  <Icon name="save" aria-hidden="true" />
  Save
</Button>

// Grouping with aria-labelledby
<div role="group" aria-labelledby="filter-heading">
  <h3 id="filter-heading">Filter Options</h3>
  <Button>Apply</Button>
</div>

// Additional description
<Input
  type="email"
  aria-describedby="email-hint"
/>
<div id="email-hint">We'll never share your email</div>
```

### States and Properties

```tsx
// Expanded state (dropdowns, accordions)
<Button aria-expanded={isOpen} aria-controls="menu-list">
  Menu
</Button>
<div id="menu-list" hidden={!isOpen}>
  {/* Menu items */}
</div>

// Toggle state (toolbar buttons)
<Button aria-pressed={isBold} onClick={toggleBold}>
  <Icon name="bold" aria-hidden="true" />
  Bold
</Button>

// Current page in navigation
<nav aria-label="Pagination">
  <Button aria-current="page">1</Button>
  <Button>2</Button>
  <Button>3</Button>
</nav>

// Hide decorative elements
<Badge>
  New
  <span aria-hidden="true">✨</span>
</Badge>
```

### Live Regions

Announce dynamic content changes:

```tsx
// Polite announcement (non-urgent)
<div aria-live="polite" aria-atomic="true">
  {statusMessage}
</div>

// Alert role (urgent messages)
<Alert variant="error" role="alert">
  Form submission failed. Please check your input.
</Alert>

// Status role (progress updates)
<div role="status" aria-live="polite">
  Saving... {progress}% complete
</div>
```

---

## Button Patterns

### Why fpkit Uses aria-disabled

fpkit buttons use the **`aria-disabled` pattern** instead of the native `disabled` attribute for superior accessibility and user experience:

```tsx
// fpkit Button with aria-disabled
<Button disabled>Submit</Button>
// Renders: <button aria-disabled="true">Submit</button>

// NOT: <button disabled>Submit</button> ❌
```

**WCAG 2.1 Compliance Benefits:**
- **✅ Keyboard accessible (WCAG 2.1.1)**: Disabled buttons remain in tab order for discovery
- **✅ Screen reader context (WCAG 4.1.2)**: Users can discover and understand disabled state
- **✅ Tooltip compatible**: Can show explanation tooltips on hover/focus
- **✅ Consistent styling**: Better visual control for WCAG AA contrast compliance
- **✅ Focus management**: Stays focusable for accessibility tools

**Performance & Implementation:**
- Uses optimized `useDisabledState` hook with stable references
- Automatic className merging eliminates boilerplate
- ~90% reduction in unnecessary re-renders
- Prevents all interactions when disabled (click, pointer, keyboard)

**Adding tooltips to disabled buttons**:
```tsx
// Excellent UX - explains why button is disabled
<Tooltip content="Complete all required fields first">
  <Button disabled>Submit</Button>
</Tooltip>

// Users can still focus and read the tooltip!
```

**Supports both modern and legacy props**:
```tsx
// Modern API (recommended)
<Button disabled={true}>Submit</Button>

// Legacy API (still supported)
<Button isDisabled={true}>Submit</Button>

// Both render with aria-disabled pattern
```

### Button Types

Always specify button type when inside forms:

```tsx
// Inside forms
<form>
  <Button type="submit">Save</Button>
  <Button type="reset">Clear</Button>
  <Button type="button">Cancel</Button>
</form>

// Outside forms - defaults to type="button"
<Button onClick={handleAction}>Action</Button>
```

---

## Interactive Elements

### Making Non-Button Elements Clickable

When you need to make a non-button element interactive (e.g., clickable card):

```tsx
import { Card } from '@fpkit/acss'

<Card
  as="article"
  role="button"
  tabIndex={0}
  onClick={handleClick}
  onKeyDown={(e) => {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault()
      handleClick(e)
    }
  }}
  aria-label="View article details"
>
  {/* Card content */}
</Card>
```

**Requirements:**
- `role="button"`: Announces as interactive
- `tabIndex={0}`: Makes keyboard focusable
- `onClick`: Mouse/touch interaction
- `onKeyDown`: Keyboard activation (Enter/Space)
- `aria-label` or `aria-labelledby`: Descriptive label

**Better alternative**: Wrap in an actual button or link when possible:
```tsx
// Better - uses semantic <a> element
<Card as="a" href="/article/123">
  {/* Card content */}
</Card>
```

---

## Focus Visible Pattern

fpkit components use `:focus-visible` to show focus only for keyboard users:

```scss
// Already built into fpkit components
button {
  outline: none; // Removes default for mouse users

  &:focus-visible {
    outline: 2px solid var(--btn-focus-outline);
    outline-offset: var(--btn-focus-outline-offset, 2px);
  }
}
```

**Customizing focus indicators**:
```css
/* Global override */
:root {
  --btn-focus-outline: 3px solid #ff6b6b;
  --btn-focus-outline-offset: 4px;
}

/* Component-specific */
.primary-button {
  --btn-focus-outline: 3px solid #0066cc;
}
```

**WCAG 2.4.7: Focus Visible** - Any keyboard operable interface has a mode where the focus indicator is visible.

---

## Link Patterns

### External Links with Automatic Security

fpkit Link components **automatically add security attributes** for external links:

```tsx
import { Link } from '@fpkit/acss'

// External link - security attributes added automatically! 🔒
<Link
  href="https://example.com"
  target="_blank"
>
  External Site
  <span className="sr-only">(opens in new tab)</span>
</Link>
// Renders: <a href="..." target="_blank" rel="noopener noreferrer">

// fpkit automatically merges: noopener noreferrer
```

**Security Features:**
- **`noopener`**: Prevents `window.opener` exploitation (security)
- **`noreferrer`**: Prevents referrer header leakage (privacy)
- **Smart merging**: Combines with user-provided `rel` values
- **Prefetch support**: Adds `prefetch` hint when enabled

**Advanced usage with prefetch**:
```tsx
// Enable prefetch for performance
<Link
  href="https://example.com"
  target="_blank"
  prefetch={true}
>
  External Site
</Link>
// Renders: rel="noopener noreferrer prefetch"
```

**Custom rel values are preserved**:
```tsx
<Link
  href="https://example.com"
  target="_blank"
  rel="nofollow"
>
  Sponsored Link
</Link>
// Renders: rel="noopener noreferrer nofollow"
```

### Focus Management with Ref Forwarding

fpkit Links support ref forwarding for focus management:

```tsx
import { useRef, useEffect } from 'react'
import { Link } from '@fpkit/acss'

// Skip link with focus management
const SkipLink = () => {
  const mainRef = useRef<HTMLAnchorElement>(null)

  useEffect(() => {
    // Programmatic focus for skip links
    mainRef.current?.focus()
  }, [])

  return (
    <Link ref={mainRef} href="#main-content">
      Skip to main content
    </Link>
  )
}
```

### Event Handling Best Practices

**Use `onClick` for accessibility** - captures ALL activation methods:

```tsx
// ✅ GOOD: onClick captures keyboard, mouse, touch, assistive tech
<Link
  href="/products"
  onClick={(e) => {
    trackEvent('link_click', { href: '/products' })
    // This fires for Enter key, mouse clicks, touch, screen readers!
  }}
>
  Products
</Link>

// ⚠️ LIMITED: onPointerDown only for pointer-specific needs
<Link
  href="/products"
  onPointerDown={(e) => {
    // Only fires for mouse/touch/pen - NOT keyboard!
    console.log('Pointer type:', e.pointerType)
  }}
>
  Products
</Link>

// ✅ BEST: Use both when needed
<Link
  href="/products"
  onClick={(e) => trackAllActivations(e)}      // Keyboard + all
  onPointerDown={(e) => provideFeedback(e)}    // Pointer-specific
>
  Products
</Link>
```

### Visited Link State

Maintain visited link styling:

```css
/* Customize visited state */
:root {
  --link-color: #0066cc;
  --link-visited-color: #551a8b;
  --link-hover-color: #004499;
}
```

---

## Form Patterns

### Field Labels

Always associate labels with inputs:

```tsx
// ✅ Explicit association (recommended)
<label htmlFor="email">Email Address</label>
<Input id="email" type="email" name="email" />

// ✅ Implicit association
<label>
  Email Address
  <Input type="email" name="email" />
</label>

// ❌ No association - inaccessible
<label>Email Address</label>
<Input type="email" name="email" />
```

### Error Messages

Link error messages to inputs:

```tsx
<label htmlFor="password">Password</label>
<Input
  id="password"
  type="password"
  aria-describedby={hasError ? 'password-error' : undefined}
  aria-invalid={hasError}
/>
{hasError && (
  <div id="password-error" role="alert">
    Password must be at least 8 characters
  </div>
)}
```

### Required Fields

```tsx
<label htmlFor="name">
  Name <span aria-label="required">*</span>
</label>
<Input
  id="name"
  type="text"
  required
  aria-required="true"
/>
```

### Field Hints

```tsx
<label htmlFor="username">Username</label>
<Input
  id="username"
  type="text"
  aria-describedby="username-hint"
/>
<div id="username-hint">
  3-20 characters, letters and numbers only
</div>
```

---

## Modal/Dialog Patterns

fpkit Dialog components handle focus management automatically:

```tsx
import { Dialog, Button } from '@fpkit/acss'

<Dialog
  isOpen={isOpen}
  onClose={handleClose}
  aria-labelledby="dialog-title"
>
  <h2 id="dialog-title">Confirm Action</h2>
  <p>Are you sure you want to proceed?</p>
  <Button onClick={handleClose}>Cancel</Button>
  <Button onClick={handleConfirm}>Confirm</Button>
</Dialog>
```

**Built-in features:**
- ✅ Focus trap (keyboard stays within dialog)
- ✅ Escape key closes dialog
- ✅ Focus restoration (returns to trigger element)
- ✅ Backdrop click closes (with `closeOnBackdrop` prop)
- ✅ `aria-modal="true"` attribute

**Custom focus management**:
```tsx
import { useEffect, useRef } from 'react'

const CustomDialog = ({ isOpen, onClose }) => {
  const firstFocusRef = useRef(null)

  useEffect(() => {
    if (isOpen) {
      // Focus specific element when opening
      firstFocusRef.current?.focus()
    }
  }, [isOpen])

  return (
    <Dialog isOpen={isOpen} onClose={onClose}>
      <Button ref={firstFocusRef}>Primary Action</Button>
    </Dialog>
  )
}
```

---

## Screen Reader Only Content

### Visually Hidden Text

Use the `sr-only` utility class for screen reader only content:

```css
/* Add to your global CSS */
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

```tsx
// Icon-only button
<Button>
  <Icon name="close" aria-hidden="true" />
  <span className="sr-only">Close dialog</span>
</Button>

// Loading indicator
<div>
  <Spinner aria-hidden="true" />
  <span className="sr-only">Loading content...</span>
</div>
```

---

## Color Contrast

### WCAG AA Requirements

- **Normal text** (< 18pt): 4.5:1 contrast ratio minimum
- **Large text** (≥ 18pt or ≥ 14pt bold): 3:1 contrast ratio minimum
- **UI components**: 3:1 for interactive elements

fpkit components meet these requirements by default:

```scss
// Example built-in contrasts
--btn-primary-bg: #0066cc;      // Blue
--btn-primary-color: #ffffff;    // White (7.5:1 - exceeds AA)

--alert-error-bg: #f8d7da;
--alert-error-color: #721c24;    // Dark red (9.2:1 - exceeds AA)
```

**Testing color contrast**:
1. Browser DevTools → Elements → Accessibility
2. [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
3. Lighthouse accessibility audit

**Custom colors**:
```css
/* Ensure sufficient contrast when overriding */
:root {
  --btn-custom-bg: #your-color;
  --btn-custom-color: #text-color; /* Test contrast! */
}
```

---

## Landmarks and Regions

### Semantic HTML5 Elements

```tsx
<header>
  <nav aria-label="Main navigation">
    {/* Navigation links */}
  </nav>
</header>

<main>
  <article>
    <header>
      <h1>Article Title</h1>
    </header>
    <section>
      {/* Article content */}
    </section>
  </article>

  <aside aria-label="Related articles">
    {/* Sidebar content */}
  </aside>
</main>

<footer>
  <nav aria-label="Footer navigation">
    {/* Footer links */}
  </nav>
</footer>
```

### Multiple Landmarks of Same Type

Use `aria-label` to differentiate:

```tsx
<nav aria-label="Main navigation">...</nav>
<nav aria-label="Footer navigation">...</nav>

<aside aria-label="Related articles">...</aside>
<aside aria-label="Advertisements">...</aside>
```

---

## Testing Accessibility

### Manual Testing

#### 1. Keyboard Navigation
- Tab through all interactive elements
- Activate with Enter/Space
- Navigate menus with arrow keys
- Close modals with Escape
- Ensure focus order is logical

#### 2. Screen Reader Testing

**macOS - VoiceOver**:
```bash
# Enable VoiceOver
Cmd + F5

# Navigate
VO + Right Arrow (next)
VO + Left Arrow (previous)
```

**Windows - NVDA** (free):
- Download from [nvaccess.org](https://www.nvaccess.org/)
- Navigate with arrow keys
- Read with Insert + Down Arrow

#### 3. Browser DevTools

**Chrome/Edge**:
1. DevTools → Lighthouse → Accessibility audit
2. DevTools → Elements → Accessibility pane
3. Inspect accessibility tree

**Firefox**:
- DevTools → Accessibility inspector

### Automated Testing

```tsx
import { render } from '@testing-library/react'
import { axe, toHaveNoViolations } from 'jest-axe'

expect.extend(toHaveNoViolations)

describe('Button accessibility', () => {
  it('should not have accessibility violations', async () => {
    const { container } = render(<Button>Click me</Button>)
    const results = await axe(container)
    expect(results).toHaveNoViolations()
  })
})
```

### Accessibility Testing Tools

| Tool | Type | Use Case |
|------|------|----------|
| [axe DevTools](https://www.deque.com/axe/devtools/) | Browser Extension | Real-time violation detection |
| [WAVE](https://wave.webaim.org/extension/) | Browser Extension | Visual feedback on issues |
| [Lighthouse](https://developers.google.com/web/tools/lighthouse) | Built-in Chrome | Comprehensive audit |
| [jest-axe](https://github.com/nickcolley/jest-axe) | Testing Library | Automated unit testing |
| [pa11y](https://pa11y.org/) | CLI | CI/CD integration |

---

## WCAG 2.1 Level AA Checklist

### Perceivable

- [ ] Text alternatives for non-text content (images, icons)
- [ ] Captions/transcripts for audio/video
- [ ] Content can be presented in different ways without losing information
- [ ] Sufficient color contrast (4.5:1 for normal, 3:1 for large text)
- [ ] Text can be resized up to 200% without loss of functionality

### Operable

- [ ] All functionality available via keyboard
- [ ] No keyboard traps (can navigate away from all elements)
- [ ] Users have enough time to read and interact with content
- [ ] No content flashes more than 3 times per second
- [ ] Clear page titles and headings
- [ ] Visible focus indicator for keyboard navigation
- [ ] Multiple ways to navigate (search, sitemap, nav)

### Understandable

- [ ] Language of page is programmatically determined
- [ ] Labels and instructions provided for user input
- [ ] Error messages are clear and helpful
- [ ] Consistent navigation and identification
- [ ] Components behave predictably

### Robust

- [ ] Valid HTML (no duplicate IDs, proper nesting)
- [ ] ARIA attributes used correctly
- [ ] Compatible with current and future assistive technologies
- [ ] Status messages announced to screen readers

---

## Common Mistakes to Avoid

### ❌ Don't

- Use `div` or `span` as buttons without proper ARIA
- Remove focus outlines without providing alternatives
- Use `placeholder` as a label replacement
- Use color alone to convey information
- Create keyboard traps unintentionally
- Use positive `tabindex` values (> 0) - disrupts natural tab order
- Announce every state change - overwhelming for screen readers
- Nest interactive elements (`<button>` inside `<a>`)
- Use `alt=""` on informative images
- Auto-play audio/video without controls

### ✅ Do

- Use semantic HTML elements (button, nav, main, etc.)
- Provide visible focus indicators with `:focus-visible`
- Include proper labels for all form controls
- Use multiple cues (color + icon, color + text)
- Ensure modals trap focus intentionally
- Use `tabindex="0"` for custom interactive elements, `tabindex="-1"` to remove from tab order
- Use `aria-live="polite"` for non-critical updates, `"assertive"` for urgent ones
- Use `<button>` or `<a>` appropriately (buttons for actions, links for navigation)
- Provide meaningful `alt` text for images
- Provide controls and don't auto-play media

---

## Composing Accessible Components

When composing fpkit components, maintain accessibility:

```tsx
import { Button, Badge } from '@fpkit/acss'

// ✅ Good - maintains accessibility
export const NotificationButton = ({ count, onClick }) => {
  return (
    <Button onClick={onClick} aria-label={`Notifications (${count} unread)`}>
      <Icon name="bell" aria-hidden="true" />
      {count > 0 && (
        <Badge aria-hidden="true">{count}</Badge>
      )}
    </Button>
  )
}
```

**Why this works:**
- Button is keyboard accessible (inherits from fpkit Button)
- `aria-label` provides context for screen readers
- Visual elements (icon, badge) are hidden from screen readers with `aria-hidden`
- Count is announced via `aria-label`

---

## Resources

### WCAG Guidelines

- [WCAG 2.1 Quick Reference](https://www.w3.org/WAI/WCAG21/quickref/)
- [WCAG 2.1 Understanding Docs](https://www.w3.org/WAI/WCAG21/Understanding/)
- [WebAIM Articles](https://webaim.org/articles/)

### ARIA

- [WAI-ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/)
- [ARIA in HTML](https://www.w3.org/TR/html-aria/)
- [ARIA Roles](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles)

### Testing Tools

- [axe DevTools](https://www.deque.com/axe/devtools/)
- [WAVE Browser Extension](https://wave.webaim.org/extension/)
- [Lighthouse](https://developers.google.com/web/tools/lighthouse)
- [jest-axe](https://github.com/nickcolley/jest-axe)
- [Pa11y](https://pa11y.org/)

### Learning Resources

- [Web Accessibility by Google](https://www.udacity.com/course/web-accessibility--ud891)
- [A11ycasts with Rob Dodson](https://www.youtube.com/playlist?list=PLNYkxOF6rcICWx0C9LVWWVqvHlYJyqw7g)
- [The A11Y Project](https://www.a11yproject.com/)

---

## Additional Guides

- **[CSS Variables Guide](./css-variables.md)** - Customize components accessibly
- **[Composition Guide](./composition.md)** - Build accessible compositions
- **[Testing Guide](./testing.md)** - Test accessibility in your components

---

**Remember**: Accessibility is not optional. It ensures your application is usable by everyone, including people with disabilities. fpkit provides accessible components by default - your job is to maintain that accessibility when composing and customizing them.
