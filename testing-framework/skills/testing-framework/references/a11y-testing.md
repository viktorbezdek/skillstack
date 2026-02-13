# Accessibility Testing Guide

Comprehensive guide for implementing accessibility testing in Next.js applications.

## Overview

Accessibility testing ensures applications are usable by people with disabilities and comply with WCAG standards.

## Tools

### axe-core

Industry-standard accessibility testing engine that detects WCAG violations.

**Installation:**
```bash
npm install -D @axe-core/playwright jest-axe
```

### @axe-core/playwright

Playwright integration for axe-core enabling E2E accessibility testing.

### jest-axe

Jest/Vitest matcher for accessibility assertions in component tests.

## Component-Level Testing

### Setup

```typescript
import { axe, toHaveNoViolations } from 'jest-axe'

expect.extend(toHaveNoViolations)
```

### Basic Usage

```typescript
it('has no accessibility violations', async () => {
  const { container } = render(<MyComponent />)
  const results = await axe(container)
  expect(results).toHaveNoViolations()
})
```

### Testing Specific Elements

```typescript
it('form has no violations', async () => {
  const { container } = render(<SignupForm />)
  const form = container.querySelector('form')
  const results = await axe(form)
  expect(results).toHaveNoViolations()
})
```

### Custom Rules

```typescript
const results = await axe(container, {
  rules: {
    'color-contrast': { enabled: true },
    'valid-aria-role': { enabled: true }
  }
})
```

## E2E Accessibility Testing

### Setup

```typescript
import AxeBuilder from '@axe-core/playwright'
```

### Page-Level Scanning

```typescript
test('homepage meets a11y standards', async ({ page }) => {
  await page.goto('/')

  const accessibilityScanResults = await new AxeBuilder({ page }).analyze()

  expect(accessibilityScanResults.violations).toEqual([])
})
```

### Scanning Specific Regions

```typescript
test('navigation is accessible', async ({ page }) => {
  await page.goto('/')

  const results = await new AxeBuilder({ page })
    .include('#navigation')
    .analyze()

  expect(results.violations).toEqual([])
})
```

### Excluding Elements

```typescript
const results = await new AxeBuilder({ page })
  .exclude('#third-party-widget')
  .analyze()
```

### Custom Tags

Test specific WCAG levels:

```typescript
// WCAG 2.1 Level AA
const results = await new AxeBuilder({ page })
  .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'])
  .analyze()
```

## Common Violations and Fixes

### Missing Alt Text

**Violation:** Images without alt attributes

**Fix:**
```tsx
// Bad
<img src="/avatar.jpg" />

// Good
<img src="/avatar.jpg" alt="User avatar" />

// Decorative images
<img src="/divider.png" alt="" />
```

### Form Labels

**Violation:** Form inputs without labels

**Fix:**
```tsx
// Bad
<input type="text" placeholder="Name" />

// Good
<label htmlFor="name">Name</label>
<input id="name" type="text" />

// Or use aria-label
<input type="text" aria-label="Name" />
```

### Color Contrast

**Violation:** Insufficient contrast ratio

**Fix:**
- Use contrast ratio of at least 4.5:1 for normal text
- Use contrast ratio of at least 3:1 for large text
- Test with tools like WebAIM Contrast Checker

### Heading Hierarchy

**Violation:** Skipped heading levels

**Fix:**
```tsx
// Bad
<h1>Page Title</h1>
<h3>Section</h3>

// Good
<h1>Page Title</h1>
<h2>Section</h2>
```

### Keyboard Navigation

**Violation:** Interactive elements not keyboard accessible

**Fix:**
```tsx
// Bad
<div onClick={handleClick}>Click me</div>

// Good
<button onClick={handleClick}>Click me</button>

// Or add keyboard handlers
<div
  role="button"
  tabIndex={0}
  onClick={handleClick}
  onKeyDown={(e) => {
    if (e.key === 'Enter' || e.key === ' ') {
      handleClick()
    }
  }}
>
  Click me
</div>
```

### Focus Indicators

**Violation:** Invisible focus indicators

**Fix:**
```css
/* Ensure visible focus */
:focus-visible {
  outline: 2px solid blue;
  outline-offset: 2px;
}
```

## ARIA Best Practices

### Landmarks

```tsx
<header role="banner">
<nav role="navigation">
<main role="main">
<aside role="complementary">
<footer role="contentinfo">
```

### Live Regions

```tsx
<div role="status" aria-live="polite">
  Form submitted successfully
</div>

<div role="alert" aria-live="assertive">
  Error: Please correct the following fields
</div>
```

### Dynamic Content

```tsx
<button
  aria-expanded={isOpen}
  aria-controls="dropdown-menu"
>
  Menu
</button>

<div id="dropdown-menu" aria-hidden={!isOpen}>
  {/* Menu items */}
</div>
```

## Testing Checklist

- [ ] All images have alt text
- [ ] Form inputs have labels
- [ ] Heading hierarchy is logical
- [ ] Color contrast meets WCAG AA
- [ ] Keyboard navigation works
- [ ] Focus indicators are visible
- [ ] ARIA attributes are correct
- [ ] Dynamic content announces properly
- [ ] No violations in axe scans
- [ ] Screen reader tested (optional but recommended)

## CI Integration

### GitHub Actions

```yaml
- name: Run accessibility tests
  run: npm run test:e2e -- --grep @a11y

- name: Upload a11y results
  uses: actions/upload-artifact@v3
  with:
    name: accessibility-results
    path: test-results/
```

### Failed Test Reporting

```typescript
test('check accessibility', async ({ page }) => {
  await page.goto('/')

  const results = await new AxeBuilder({ page }).analyze()

  if (results.violations.length > 0) {
    console.log('Accessibility violations:')
    results.violations.forEach(violation => {
      console.log(`- ${violation.id}: ${violation.description}`)
      console.log(`  Impact: ${violation.impact}`)
      console.log(`  Elements: ${violation.nodes.length}`)
    })
  }

  expect(results.violations).toEqual([])
})
```

## Resources

- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [axe-core Documentation](https://github.com/dequelabs/axe-core)
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/)
