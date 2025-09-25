# Playwright E2E Testing Patterns

**Source**: Context7 `/microsoft/playwright` (topic: "user flows accessibility keyboard navigation")

**When to consult**: Creating E2E tests, user flow testing, accessibility testing

---

## Core E2E Structure

```typescript
import { test, expect } from '@playwright/test'

test.describe('Feature - User Flows', () => {
  test.beforeEach(async ({ page }) => {
    // Login and navigate
    await page.goto('/login')
    await page.fill('[data-testid="email"]', 'test@example.com')
    await page.fill('[data-testid="password"]', 'password')
    await page.click('[data-testid="submit"]')
    await page.waitForURL('/dashboard')
  })

  test('user can create entity', async ({ page }) => {
    // Test goes here
  })
})
```

---

## Selector Strategy

**ALWAYS use data-testid (not CSS classes or IDs)**:

```typescript
// ✅ CORRECT - Stable selector
await page.click('[data-testid="create-button"]')

// ❌ WRONG - Fragile selector
await page.click('.btn-primary')
```

**Why**: CSS classes change for styling, data-testid is for testing only.

---

## User-Centric Actions

```typescript
// Navigation
await page.goto('/path')
await page.waitForURL('/expected-path')

// Interaction
await page.fill('[data-testid="input"]', 'value')
await page.click('[data-testid="button"]')
await page.press('Enter')

// Waiting
await page.waitForSelector('[data-testid="element"]')
await page.waitForLoadState('networkidle')
```

---

## Assertions

```typescript
// Visibility
await expect(page.locator('[data-testid="element"]')).toBeVisible()
await expect(page.locator('[data-testid="element"]')).not.toBeVisible()

// Content
await expect(page.locator('[data-testid="element"]')).toContainText('text')
await expect(page.locator('[data-testid="element"]')).toHaveText('exact text')

// State
await expect(page.locator('[data-testid="button"]')).toBeDisabled()
await expect(page.locator('[data-testid="button"]')).toBeFocused()

// Attributes
await expect(page.locator('[data-testid="input"]')).toHaveAttribute('aria-label')
```

---

## Accessibility Testing (WCAG 2.1 AA)

### Keyboard Navigation

```typescript
test('supports keyboard navigation', async ({ page }) => {
  // Focus element
  await page.locator('[data-testid="button"]').focus()

  // Navigate with keyboard
  await page.keyboard.press('Enter')  // Activate
  await page.keyboard.press('Tab')    // Next element
  await page.keyboard.press('Escape') // Close modal

  // Verify focus
  await expect(page.locator('[data-testid="next-element"]')).toBeFocused()
})
```

### ARIA Labels

```typescript
test('has proper ARIA labels', async ({ page }) => {
  const form = page.locator('form')
  await expect(form).toHaveAttribute('aria-label', /create/i)

  const input = page.locator('[data-testid="email-input"]')
  await expect(input).toHaveAttribute('aria-label', /email/i)
  await expect(input).toHaveAttribute('aria-required', 'true')
})
```

### Focus Indicators

```typescript
test('shows focus indicators', async ({ page }) => {
  const button = page.locator('[data-testid="button"]')
  await button.focus()

  await expect(button).toBeFocused()
  // CSS focus ring should be visible (visual check in screenshot)
})
```

---

## Complete CRUD Flow Pattern

```typescript
test.describe('CRUD Flows', () => {
  test('create entity', async ({ page }) => {
    // Open form
    await page.click('[data-testid="create-button"]')
    await expect(page.locator('[data-testid="create-modal"]')).toBeVisible()

    // Fill form
    await page.fill('[data-testid="name-input"]', 'Test Entity')
    await page.click('[data-testid="submit-button"]')

    // Verify success
    await expect(page.locator('[data-testid="success-message"]')).toBeVisible()
    await expect(page.locator('[data-testid="entity-list"]')).toContainText('Test Entity')
  })

  test('read entity', async ({ page }) => {
    await page.click('[data-testid="entity-item"]:first-child')
    await expect(page.locator('[data-testid="entity-details"]')).toBeVisible()
  })

  test('update entity', async ({ page }) => {
    await page.click('[data-testid="entity-item"]:first-child')
    await page.click('[data-testid="edit-button"]')
    await page.fill('[data-testid="name-input"]', 'Updated Name')
    await page.click('[data-testid="submit-button"]')
    await expect(page.locator('[data-testid="success-message"]')).toBeVisible()
  })

  test('delete entity', async ({ page }) => {
    await page.click('[data-testid="entity-item"]:first-child')
    await page.click('[data-testid="delete-button"]')
    await page.click('[data-testid="confirm-delete"]')
    await expect(page.locator('[data-testid="success-message"]')).toBeVisible()
  })
})
```

---

## Loading and Error States

```typescript
test('shows loading state', async ({ page }) => {
  const button = page.locator('[data-testid="submit-button"]')
  await button.click()

  // Loading state
  await expect(button).toBeDisabled()
  await expect(page.locator('[data-testid="loading-spinner"]')).toBeVisible()

  // Eventually completes
  await expect(button).not.toBeDisabled({ timeout: 5000 })
})

test('shows error message on failure', async ({ page }) => {
  // Simulate network error
  await page.route('**/api/*', route => route.abort())

  await page.click('[data-testid="submit-button"]')

  await expect(page.locator('[data-testid="error-message"]')).toBeVisible()
  await expect(page.locator('[data-testid="error-message"]')).toContainText(/error/i)
})
```

---

## Best Practices

1. **Use data-testid for all selectors** - Stable, semantic
2. **Test complete user workflows** - Not individual components
3. **Include accessibility checks** - Keyboard navigation, ARIA
4. **Verify loading states** - Spinners, disabled buttons
5. **Test error scenarios** - Network failures, validation errors
6. **Keep tests isolated** - No dependencies between tests
7. **Use auto-wait** - Playwright waits automatically for elements

---

**Latest patterns**: Query Context7 `/microsoft/playwright` for updates
