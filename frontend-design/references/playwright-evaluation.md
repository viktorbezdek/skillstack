# Playwright UI Evaluation

Guide to using Playwright for evaluating UI quality through visual regression testing, accessibility auditing, and performance analysis.

## Overview

Playwright enables objective UI evaluation by automating browser interactions, capturing visual snapshots, running accessibility audits, and measuring performance metrics. This transforms subjective design critique into measurable, repeatable assessments.

**What Playwright evaluation provides:**
- Visual regression detection (spot unintended changes)
- Accessibility compliance verification (WCAG 2.2)
- Performance metrics (load time, responsiveness)
- Cross-browser consistency checks
- Responsive design validation
- User interaction simulation

## Setup

### Installation

```bash
npm install -D @playwright/test
npx playwright install
```

### Additional dependencies for evaluation:

```bash
# Accessibility testing
npm install -D @axe-core/playwright

# Visual comparison
npm install -D pixelmatch
npm install -D pngjs

# Performance monitoring
npm install -D playwright-performance
```

### Configuration

**playwright.config.ts:**
```typescript
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './tests',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 1 : undefined,
  reporter: 'html',
  use: {
    baseURL: 'http://localhost:3000',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
  },
  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
    {
      name: 'firefox',
      use: { ...devices['Desktop Firefox'] },
    },
    {
      name: 'webkit',
      use: { ...devices['Desktop Safari'] },
    },
    // Mobile viewports
    {
      name: 'Mobile Chrome',
      use: { ...devices['Pixel 5'] },
    },
    {
      name: 'Mobile Safari',
      use: { ...devices['iPhone 13'] },
    },
  ],
});
```

## Visual Regression Testing

### Basic Screenshot Comparison

Playwright captures and compares screenshots to detect visual changes.

**Simple screenshot test:**
```typescript
import { test, expect } from '@playwright/test';

test('homepage visual regression', async ({ page }) => {
  await page.goto('/');

  // Wait for content to load
  await page.waitForLoadState('networkidle');

  // Full page screenshot with comparison
  await expect(page).toHaveScreenshot('homepage.png', {
    fullPage: true,
    animations: 'disabled',
  });
});
```

**Component screenshot:**
```typescript
test('button component variations', async ({ page }) => {
  await page.goto('/components/button');

  // Screenshot specific element
  const primaryButton = page.getByRole('button', { name: 'Primary' });
  await expect(primaryButton).toHaveScreenshot('button-primary.png');

  // Hover state
  await primaryButton.hover();
  await expect(primaryButton).toHaveScreenshot('button-primary-hover.png');

  // Disabled state
  const disabledButton = page.getByRole('button', { name: 'Disabled' });
  await expect(disabledButton).toHaveScreenshot('button-disabled.png');
});
```

### Screenshot Options

**Configuration for better comparisons:**
```typescript
await expect(page).toHaveScreenshot('page.png', {
  // Capture entire page including scrollable areas
  fullPage: true,

  // Disable animations for stable screenshots
  animations: 'disabled',

  // Clip to specific area
  clip: { x: 0, y: 0, width: 1280, height: 720 },

  // Mask dynamic content
  mask: [page.locator('.timestamp'), page.locator('.live-data')],

  // Maximum pixel difference threshold (0-1)
  maxDiffPixels: 100,

  // Percentage difference threshold (0-1)
  maxDiffPixelRatio: 0.01,

  // Omit background for transparent elements
  omitBackground: true,

  // Wait before screenshot
  timeout: 5000,
});
```

### Handling Dynamic Content

Dynamic content (timestamps, random IDs) requires masking.

```typescript
test('dashboard with dynamic content', async ({ page }) => {
  await page.goto('/dashboard');

  // Mask elements with changing content
  await expect(page).toHaveScreenshot('dashboard.png', {
    fullPage: true,
    mask: [
      page.locator('[data-testid="timestamp"]'),
      page.locator('.live-chart'),
      page.locator('.user-avatar'), // May change between runs
    ],
    animations: 'disabled',
  });
});
```

### Cross-Browser Visual Testing

Detect browser-specific rendering differences.

```typescript
import { test, expect, devices } from '@playwright/test';

const browsers = ['chromium', 'firefox', 'webkit'];

browsers.forEach((browserName) => {
  test(`homepage renders consistently on ${browserName}`, async ({ page }) => {
    await page.goto('/');
    await expect(page).toHaveScreenshot(`homepage-${browserName}.png`, {
      fullPage: true,
    });
  });
});
```

### Responsive Design Testing

Validate layouts across viewport sizes.

```typescript
const viewports = [
  { name: 'mobile', width: 375, height: 667 },
  { name: 'tablet', width: 768, height: 1024 },
  { name: 'desktop', width: 1920, height: 1080 },
];

viewports.forEach(({ name, width, height }) => {
  test(`homepage responsive - ${name}`, async ({ page }) => {
    await page.setViewportSize({ width, height });
    await page.goto('/');

    await expect(page).toHaveScreenshot(`homepage-${name}.png`, {
      fullPage: true,
    });
  });
});
```

## Accessibility Evaluation

### Automated Accessibility Testing

Use axe-core for comprehensive WCAG audits.

**Basic accessibility test:**
```typescript
import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

test('homepage accessibility', async ({ page }) => {
  await page.goto('/');

  const accessibilityScanResults = await new AxeBuilder({ page })
    .withTags(['wcag2a', 'wcag2aa', 'wcag21aa', 'wcag22aa'])
    .analyze();

  expect(accessibilityScanResults.violations).toEqual([]);
});
```

**Testing specific components:**
```typescript
test('navigation menu accessibility', async ({ page }) => {
  await page.goto('/');

  const results = await new AxeBuilder({ page })
    .include('nav') // Only test navigation element
    .analyze();

  expect(results.violations).toEqual([]);
});
```

**Excluding known issues:**
```typescript
test('form accessibility (excluding known color-contrast issue)', async ({ page }) => {
  await page.goto('/contact');

  const results = await new AxeBuilder({ page })
    .exclude('.legacy-widget') // Exclude third-party widget
    .disableRules(['color-contrast']) // Temporarily disable specific rules
    .analyze();

  expect(results.violations).toEqual([]);
});
```

### Detailed Violation Reporting

Generate human-readable accessibility reports.

```typescript
test('comprehensive accessibility report', async ({ page }) => {
  await page.goto('/');

  const results = await new AxeBuilder({ page })
    .withTags(['wcag2a', 'wcag2aa'])
    .analyze();

  if (results.violations.length > 0) {
    console.log('Accessibility Violations:');
    results.violations.forEach((violation) => {
      console.log(`\\n${violation.id}: ${violation.description}`);
      console.log(`Impact: ${violation.impact}`);
      console.log(`Help: ${violation.helpUrl}`);
      console.log('Affected elements:');
      violation.nodes.forEach((node) => {
        console.log(`  - ${node.html}`);
      });
    });
  }

  expect(results.violations).toEqual([]);
});
```

### Keyboard Navigation Testing

Verify keyboard accessibility.

```typescript
test('keyboard navigation', async ({ page }) => {
  await page.goto('/');

  // Tab through all focusable elements
  const focusableElements = [];

  for (let i = 0; i < 20; i++) {
    await page.keyboard.press('Tab');
    const activeElement = await page.evaluate(() => {
      const el = document.activeElement;
      return {
        tag: el?.tagName,
        text: el?.textContent?.trim().substring(0, 50),
        ariaLabel: el?.getAttribute('aria-label'),
      };
    });
    focusableElements.push(activeElement);
  }

  // Verify logical tab order
  console.log('Tab order:', focusableElements);

  // Check that focus is visible
  await page.keyboard.press('Tab');
  const focusOutlineVisible = await page.evaluate(() => {
    const focused = document.activeElement;
    const styles = window.getComputedStyle(focused);
    return styles.outline !== 'none' && styles.outlineWidth !== '0px';
  });

  expect(focusOutlineVisible).toBe(true);
});
```

### Screen Reader Testing

Test ARIA labels and descriptions.

```typescript
test('screen reader accessibility', async ({ page }) => {
  await page.goto('/');

  // Check all images have alt text
  const imagesWithoutAlt = await page.locator('img:not([alt])').count();
  expect(imagesWithoutAlt).toBe(0);

  // Check all interactive elements have accessible names
  const buttons = await page.locator('button, [role="button"]').all();
  for (const button of buttons) {
    const accessibleName = await button.evaluate((el) => {
      return (
        el.getAttribute('aria-label') ||
        el.textContent?.trim() ||
        el.getAttribute('aria-labelledby')
      );
    });
    expect(accessibleName).toBeTruthy();
  }

  // Check form inputs have labels
  const inputs = await page.locator('input, textarea, select').all();
  for (const input of inputs) {
    const hasLabel = await input.evaluate((el) => {
      const id = el.id;
      return (
        !!el.getAttribute('aria-label') ||
        !!el.getAttribute('aria-labelledby') ||
        !!document.querySelector(`label[for="${id}"]`)
      );
    });
    expect(hasLabel).toBe(true);
  }
});
```

## Performance Evaluation

### Measuring Load Performance

Capture key performance metrics.

```typescript
import { test, expect } from '@playwright/test';

test('homepage performance', async ({ page }) => {
  await page.goto('/');

  // Measure performance metrics
  const metrics = await page.evaluate(() => {
    const perf = performance.getEntriesByType('navigation')[0] as PerformanceNavigationTiming;
    const paint = performance.getEntriesByType('paint');

    return {
      // Time to first byte
      ttfb: perf.responseStart - perf.requestStart,

      // DOM content loaded
      domContentLoaded: perf.domContentLoadedEventEnd - perf.domContentLoadedEventStart,

      // Full page load
      loadComplete: perf.loadEventEnd - perf.loadEventStart,

      // First paint
      firstPaint: paint.find((p) => p.name === 'first-paint')?.startTime || 0,

      // First contentful paint
      fcp: paint.find((p) => p.name === 'first-contentful-paint')?.startTime || 0,

      // Total page size
      transferSize: perf.transferSize,
    };
  });

  console.log('Performance metrics:', metrics);

  // Assert performance budgets
  expect(metrics.ttfb).toBeLessThan(500); // TTFB < 500ms
  expect(metrics.fcp).toBeLessThan(1800); // FCP < 1.8s
  expect(metrics.loadComplete).toBeLessThan(3000); // Load < 3s
});
```

### Largest Contentful Paint (LCP)

Measure when main content is visible.

```typescript
test('LCP performance', async ({ page }) => {
  await page.goto('/');

  const lcp = await page.evaluate(() => {
    return new Promise((resolve) => {
      new PerformanceObserver((list) => {
        const entries = list.getEntries();
        const lastEntry = entries[entries.length - 1];
        resolve(lastEntry.startTime);
      }).observe({ entryTypes: ['largest-contentful-paint'] });

      // Timeout after 10 seconds
      setTimeout(() => resolve(null), 10000);
    });
  });

  console.log('LCP:', lcp);
  expect(lcp).toBeLessThan(2500); // LCP < 2.5s (good)
});
```

### Cumulative Layout Shift (CLS)

Measure visual stability.

```typescript
test('CLS performance', async ({ page }) => {
  await page.goto('/');

  await page.waitForLoadState('networkidle');

  const cls = await page.evaluate(() => {
    return new Promise((resolve) => {
      let clsValue = 0;

      new PerformanceObserver((list) => {
        for (const entry of list.getEntries()) {
          if (!(entry as any).hadRecentInput) {
            clsValue += (entry as any).value;
          }
        }
      }).observe({ entryTypes: ['layout-shift'] });

      setTimeout(() => resolve(clsValue), 5000);
    });
  });

  console.log('CLS:', cls);
  expect(cls).toBeLessThan(0.1); // CLS < 0.1 (good)
});
```

### Network Performance

Monitor resource loading.

```typescript
test('network performance', async ({ page }) => {
  const resourceSizes: Record<string, number> = {
    script: 0,
    stylesheet: 0,
    image: 0,
    font: 0,
    document: 0,
  };

  page.on('response', async (response) => {
    const request = response.request();
    const resourceType = request.resourceType();
    const bodySize = (await response.body()).length;

    if (resourceType in resourceSizes) {
      resourceSizes[resourceType] += bodySize;
    }
  });

  await page.goto('/');
  await page.waitForLoadState('networkidle');

  console.log('Resource sizes (bytes):', resourceSizes);

  // Assert budgets
  expect(resourceSizes.script).toBeLessThan(500_000); // JS < 500KB
  expect(resourceSizes.stylesheet).toBeLessThan(100_000); // CSS < 100KB
  expect(resourceSizes.image).toBeLessThan(1_000_000); // Images < 1MB
});
```

## UI Quality Scoring

### Automated Quality Checklist

Create a comprehensive quality score.

```typescript
interface UIQualityReport {
  score: number;
  accessibility: {
    violations: number;
    passes: number;
  };
  performance: {
    lcp: number;
    cls: number;
    ttfb: number;
  };
  visual: {
    hasDifferences: boolean;
    diffPercentage: number;
  };
  responsive: {
    mobile: boolean;
    tablet: boolean;
    desktop: boolean;
  };
}

async function evaluateUIQuality(page: Page): Promise<UIQualityReport> {
  // Accessibility score
  const a11yResults = await new AxeBuilder({ page })
    .withTags(['wcag2a', 'wcag2aa'])
    .analyze();

  // Performance score
  const perfMetrics = await page.evaluate(() => {
    const perf = performance.getEntriesByType('navigation')[0] as PerformanceNavigationTiming;
    const paint = performance.getEntriesByType('paint');
    return {
      ttfb: perf.responseStart - perf.requestStart,
      fcp: paint.find((p) => p.name === 'first-contentful-paint')?.startTime || 0,
    };
  });

  // Calculate overall score
  let score = 100;

  // Deduct for accessibility violations
  score -= a11yResults.violations.length * 5;

  // Deduct for performance issues
  if (perfMetrics.ttfb > 500) score -= 10;
  if (perfMetrics.fcp > 1800) score -= 15;

  return {
    score: Math.max(0, score),
    accessibility: {
      violations: a11yResults.violations.length,
      passes: a11yResults.passes.length,
    },
    performance: {
      lcp: 0, // Measured separately
      cls: 0, // Measured separately
      ttfb: perfMetrics.ttfb,
    },
    visual: {
      hasDifferences: false,
      diffPercentage: 0,
    },
    responsive: {
      mobile: true,
      tablet: true,
      desktop: true,
    },
  };
}

test('UI quality evaluation', async ({ page }) => {
  await page.goto('/');
  const report = await evaluateUIQuality(page);

  console.log('UI Quality Report:', JSON.stringify(report, null, 2));

  expect(report.score).toBeGreaterThan(85); // Target score > 85
});
```

## A/B Testing Comparison

### Side-by-Side Visual Comparison

Compare two UI variations.

```typescript
test('compare button variations', async ({ page }) => {
  // Version A
  await page.goto('/components/button?variant=a');
  await expect(page.locator('[data-testid="button"]')).toHaveScreenshot('button-variant-a.png');

  // Version B
  await page.goto('/components/button?variant=b');
  await expect(page.locator('[data-testid="button"]')).toHaveScreenshot('button-variant-b.png');

  // Manual comparison or use image diff library
  console.log('Compare screenshots in test-results/ directory');
});
```

### Interaction Comparison

Test user flows with different designs.

```typescript
test('compare checkout flows', async ({ page }) => {
  // Test variant A
  await page.goto('/checkout?variant=a');
  const startTimeA = Date.now();

  await page.getByLabel('Email').fill('user@example.com');
  await page.getByLabel('Card number').fill('4242424242424242');
  await page.getByRole('button', { name: 'Complete purchase' }).click();

  const durationA = Date.now() - startTimeA;

  // Test variant B
  await page.goto('/checkout?variant=b');
  const startTimeB = Date.now();

  await page.getByLabel('Email').fill('user@example.com');
  await page.getByLabel('Card number').fill('4242424242424242');
  await page.getByRole('button', { name: 'Complete purchase' }).click();

  const durationB = Date.now() - startTimeB;

  console.log(`Variant A: ${durationA}ms, Variant B: ${durationB}ms`);
});
```

## Best Practices

1. **Baseline management**: Update screenshots when intentional changes are made
2. **Mask dynamic content**: Timestamps, user data, random IDs
3. **Disable animations**: Use `animations: 'disabled'` for stable screenshots
4. **Wait for stability**: Use `waitForLoadState('networkidle')` before screenshots
5. **Test across browsers**: Catch browser-specific issues
6. **Responsive testing**: Test multiple viewport sizes
7. **Combine approaches**: Visual + accessibility + performance
8. **Automate in CI**: Run on every pull request
9. **Set thresholds**: Define acceptable diff percentages
10. **Review failures**: Always investigate screenshot diff failures

## Updating Baselines

When UI changes are intentional, update baselines:

```bash
# Update all screenshots
npx playwright test --update-snapshots

# Update specific test
npx playwright test homepage.spec.ts --update-snapshots

# Update for specific browser
npx playwright test --project=chromium --update-snapshots
```

## Resources

- Playwright documentation
- axe-core rules reference
- Web Vitals documentation (LCP, CLS, FID)
- WCAG 2.2 guidelines
