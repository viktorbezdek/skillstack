import { test, expect } from '@playwright/test'
import AxeBuilder from '@axe-core/playwright'

/**
 * Example E2E test demonstrating Playwright best practices
 * with accessibility testing via axe-core
 */

test.describe('Entity Management', () => {
  test.beforeEach(async ({ page }) => {
    // Navigate to entities page
    await page.goto('/entities')
  })

  test('displays entity list', async ({ page }) => {
    // Wait for content to load
    await page.waitForSelector('[role="list"]')

    // Verify entities are displayed
    const entities = page.getByRole('listitem')
    await expect(entities).not.toHaveCount(0)

    // Verify entity cards have proper structure
    const firstEntity = entities.first()
    await expect(firstEntity.getByRole('heading')).toBeVisible()
  })

  test('creates new entity', async ({ page }) => {
    // Click create button
    await page.getByRole('button', { name: /create entity/i }).click()

    // Verify form is displayed
    await expect(page.getByRole('heading', { name: /new entity/i })).toBeVisible()

    // Fill in form
    await page.getByLabel(/name/i).fill('Mysterious Stranger')
    await page.getByLabel(/type/i).selectOption('character')
    await page.getByLabel(/description/i).fill('A traveler from distant lands')

    // Submit form
    await page.getByRole('button', { name: /save|create/i }).click()

    // Verify success message or redirect
    await expect(
      page.getByText(/entity created|success/i)
    ).toBeVisible({ timeout: 5000 })

    // Verify new entity appears in list
    await page.goto('/entities')
    await expect(page.getByText('Mysterious Stranger')).toBeVisible()
  })

  test('edits existing entity', async ({ page }) => {
    // Find and click edit button for first entity
    const firstEntity = page.getByRole('listitem').first()
    const entityName = await firstEntity.getByRole('heading').textContent()

    await firstEntity.getByRole('button', { name: /edit/i }).click()

    // Update name
    const nameInput = page.getByLabel(/name/i)
    await nameInput.clear()
    await nameInput.fill(`${entityName} (Updated)`)

    // Save changes
    await page.getByRole('button', { name: /save|update/i }).click()

    // Verify update
    await expect(page.getByText(/updated|success/i)).toBeVisible()
    await page.goto('/entities')
    await expect(page.getByText(`${entityName} (Updated)`)).toBeVisible()
  })

  test('deletes entity with confirmation', async ({ page }) => {
    // Click delete button
    const firstEntity = page.getByRole('listitem').first()
    const entityName = await firstEntity.getByRole('heading').textContent()

    await firstEntity.getByRole('button', { name: /delete/i }).click()

    // Confirm deletion in dialog
    const dialog = page.getByRole('dialog')
    await expect(dialog.getByText(/confirm|sure/i)).toBeVisible()
    await dialog.getByRole('button', { name: /delete|confirm/i }).click()

    // Verify entity is removed
    await expect(page.getByText(entityName!)).not.toBeVisible()
  })

  test('searches entities', async ({ page }) => {
    // Enter search query
    const searchInput = page.getByRole('searchbox', { name: /search/i })
    await searchInput.fill('character')

    // Wait for filtered results
    await page.waitForTimeout(500) // Debounce

    // Verify filtered results
    const results = page.getByRole('listitem')
    const count = await results.count()

    // All visible results should match search
    for (let i = 0; i < count; i++) {
      const item = results.nth(i)
      await expect(item.getByText(/character/i)).toBeVisible()
    }
  })

  test('filters entities by type', async ({ page }) => {
    // Select filter
    await page.getByLabel(/filter by type/i).selectOption('location')

    // Wait for filtered results
    await page.waitForSelector('[role="listitem"]')

    // Verify all results are locations
    const badges = page.locator('.badge')
    const count = await badges.count()

    for (let i = 0; i < count; i++) {
      await expect(badges.nth(i)).toHaveText('location')
    }
  })

  test('keyboard navigation works', async ({ page }) => {
    // Focus first interactive element
    await page.keyboard.press('Tab')

    // Navigate through entities with arrow keys
    await page.keyboard.press('ArrowDown')
    await page.keyboard.press('ArrowDown')

    // Activate focused element with Enter
    await page.keyboard.press('Enter')

    // Verify navigation worked
    await expect(page.getByRole('heading', { name: /entity/i })).toBeVisible()
  })

  test('meets accessibility standards', async ({ page }) => {
    // Run axe accessibility scan
    const accessibilityScanResults = await new AxeBuilder({ page }).analyze()

    // Expect no violations
    expect(accessibilityScanResults.violations).toEqual([])
  })

  test('is responsive on mobile', async ({ page }) => {
    // Set mobile viewport
    await page.setViewportSize({ width: 375, height: 667 })

    // Verify mobile layout
    await expect(page.getByRole('button', { name: /menu/i })).toBeVisible()

    // Test mobile navigation
    await page.getByRole('button', { name: /menu/i }).click()
    await expect(page.getByRole('navigation')).toBeVisible()
  })
})

test.describe('Entity Relationships', () => {
  test('creates relationship between entities', async ({ page }) => {
    // Navigate to first entity detail page
    await page.goto('/entities')
    await page.getByRole('listitem').first().click()

    // Open relationship creation
    await page.getByRole('button', { name: /add relationship/i }).click()

    // Select related entity
    await page.getByLabel(/related entity/i).fill('Location')
    await page.keyboard.press('ArrowDown')
    await page.keyboard.press('Enter')

    // Select relationship type
    await page.getByLabel(/relationship type/i).selectOption('lives_in')

    // Save relationship
    await page.getByRole('button', { name: /create|save/i }).click()

    // Verify relationship appears
    await expect(page.getByText(/lives_in/i)).toBeVisible()
  })

  test('relationship section is accessible', async ({ page }) => {
    await page.goto('/entities')
    await page.getByRole('listitem').first().click()

    // Scan relationships section
    const accessibilityScanResults = await new AxeBuilder({ page })
      .include('#relationships')
      .analyze()

    expect(accessibilityScanResults.violations).toEqual([])
  })
})
