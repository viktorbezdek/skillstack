#!/usr/bin/env node

/**
 * UI Evaluation Script
 *
 * Evaluates UI quality using Playwright by capturing screenshots,
 * running accessibility audits, and measuring performance metrics.
 *
 * Usage:
 *   npx tsx evaluate-ui.ts <url> [options]
 *
 * Options:
 *   --output-dir     Directory for evaluation results (default: ./ui-evaluation)
 *   --viewport       Viewport size (default: 1920x1080)
 *   --mobile         Use mobile viewport (default: false)
 *   --threshold      Accessibility violation threshold (default: 0)
 *   --screenshot     Capture screenshots (default: true)
 *   --a11y           Run accessibility checks (default: true)
 *   --performance    Measure performance metrics (default: true)
 */

import { chromium, Browser, Page } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';
import * as fs from 'fs';
import * as path from 'path';

interface EvaluationOptions {
  outputDir: string;
  viewport: { width: number; height: number };
  mobile: boolean;
  threshold: number;
  screenshot: boolean;
  a11y: boolean;
  performance: boolean;
}

interface PerformanceMetrics {
  ttfb: number;
  fcp: number;
  lcp: number;
  cls: number;
  domContentLoaded: number;
  loadComplete: number;
  transferSize: number;
}

interface AccessibilityResult {
  violations: number;
  passes: number;
  violationDetails: Array<{
    id: string;
    impact: string;
    description: string;
    helpUrl: string;
    nodes: number;
  }>;
}

interface UIEvaluationReport {
  url: string;
  timestamp: string;
  viewport: { width: number; height: number };
  score: number;
  screenshots?: {
    fullPage: string;
    aboveFold: string;
  };
  accessibility?: AccessibilityResult;
  performance?: PerformanceMetrics;
  recommendations: string[];
}

async function parseArgs(): Promise<{ url: string; options: EvaluationOptions }> {
  const args = process.argv.slice(2);

  if (args.length === 0 || args[0].startsWith('--')) {
    console.error('Error: URL is required');
    console.log('Usage: npx tsx evaluate-ui.ts <url> [options]');
    process.exit(1);
  }

  const url = args[0];
  const options: EvaluationOptions = {
    outputDir: './ui-evaluation',
    viewport: { width: 1920, height: 1080 },
    mobile: false,
    threshold: 0,
    screenshot: true,
    a11y: true,
    performance: true,
  };

  for (let i = 1; i < args.length; i += 2) {
    const flag = args[i];
    const value = args[i + 1];

    switch (flag) {
      case '--output-dir':
        options.outputDir = value;
        break;
      case '--viewport':
        const [width, height] = value.split('x').map(Number);
        options.viewport = { width, height };
        break;
      case '--mobile':
        options.mobile = value === 'true';
        break;
      case '--threshold':
        options.threshold = parseInt(value, 10);
        break;
      case '--screenshot':
        options.screenshot = value === 'true';
        break;
      case '--a11y':
        options.a11y = value === 'true';
        break;
      case '--performance':
        options.performance = value === 'true';
        break;
    }
  }

  if (options.mobile) {
    options.viewport = { width: 375, height: 667 };
  }

  return { url, options };
}

async function captureScreenshots(page: Page, outputDir: string): Promise<{ fullPage: string; aboveFold: string }> {
  console.log('📸 Capturing screenshots...');

  const fullPagePath = path.join(outputDir, 'screenshot-full-page.png');
  const aboveFoldPath = path.join(outputDir, 'screenshot-above-fold.png');

  // Full page screenshot
  await page.screenshot({
    path: fullPagePath,
    fullPage: true,
    animations: 'disabled',
  });

  // Above the fold screenshot
  await page.screenshot({
    path: aboveFoldPath,
    fullPage: false,
    animations: 'disabled',
  });

  console.log(`  ✓ Full page: ${fullPagePath}`);
  console.log(`  ✓ Above fold: ${aboveFoldPath}`);

  return {
    fullPage: fullPagePath,
    aboveFold: aboveFoldPath,
  };
}

async function runAccessibilityAudit(page: Page): Promise<AccessibilityResult> {
  console.log('♿ Running accessibility audit...');

  const results = await new AxeBuilder({ page })
    .withTags(['wcag2a', 'wcag2aa', 'wcag21aa', 'wcag22aa'])
    .analyze();

  const violationDetails = results.violations.map((violation) => ({
    id: violation.id,
    impact: violation.impact || 'unknown',
    description: violation.description,
    helpUrl: violation.helpUrl,
    nodes: violation.nodes.length,
  }));

  console.log(`  ✓ Found ${results.violations.length} violations`);
  console.log(`  ✓ Passed ${results.passes.length} checks`);

  if (results.violations.length > 0) {
    console.log('\\n  Violations:');
    violationDetails.forEach((v) => {
      console.log(`    - ${v.id} (${v.impact}): ${v.description}`);
      console.log(`      Affects ${v.nodes} element(s)`);
      console.log(`      Help: ${v.helpUrl}`);
    });
  }

  return {
    violations: results.violations.length,
    passes: results.passes.length,
    violationDetails,
  };
}

async function measurePerformance(page: Page): Promise<PerformanceMetrics> {
  console.log('⚡ Measuring performance...');

  const metrics = await page.evaluate(() => {
    const perf = performance.getEntriesByType('navigation')[0] as PerformanceNavigationTiming;
    const paint = performance.getEntriesByType('paint');

    return {
      ttfb: perf.responseStart - perf.requestStart,
      fcp: paint.find((p) => p.name === 'first-contentful-paint')?.startTime || 0,
      domContentLoaded: perf.domContentLoadedEventEnd - perf.domContentLoadedEventStart,
      loadComplete: perf.loadEventEnd - perf.loadEventStart,
      transferSize: perf.transferSize || 0,
    };
  });

  // Measure LCP
  const lcp = await page.evaluate(() => {
    return new Promise<number>((resolve) => {
      new PerformanceObserver((list) => {
        const entries = list.getEntries();
        const lastEntry = entries[entries.length - 1];
        resolve(lastEntry.startTime);
      }).observe({ entryTypes: ['largest-contentful-paint'] });

      setTimeout(() => resolve(0), 5000);
    });
  });

  // Measure CLS
  const cls = await page.evaluate(() => {
    return new Promise<number>((resolve) => {
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

  const result = { ...metrics, lcp, cls };

  console.log(`  ✓ TTFB: ${result.ttfb.toFixed(2)}ms`);
  console.log(`  ✓ FCP: ${result.fcp.toFixed(2)}ms`);
  console.log(`  ✓ LCP: ${result.lcp.toFixed(2)}ms`);
  console.log(`  ✓ CLS: ${result.cls.toFixed(3)}`);
  console.log(`  ✓ Load time: ${result.loadComplete.toFixed(2)}ms`);

  return result;
}

function calculateScore(
  accessibility?: AccessibilityResult,
  performance?: PerformanceMetrics
): number {
  let score = 100;

  // Accessibility score (50 points max)
  if (accessibility) {
    // Deduct 5 points per violation
    score -= Math.min(accessibility.violations * 5, 50);
  }

  // Performance score (50 points max)
  if (performance) {
    // TTFB (10 points)
    if (performance.ttfb > 500) score -= 5;
    if (performance.ttfb > 1000) score -= 5;

    // FCP (10 points)
    if (performance.fcp > 1800) score -= 5;
    if (performance.fcp > 3000) score -= 5;

    // LCP (15 points)
    if (performance.lcp > 2500) score -= 8;
    if (performance.lcp > 4000) score -= 7;

    // CLS (15 points)
    if (performance.cls > 0.1) score -= 8;
    if (performance.cls > 0.25) score -= 7;
  }

  return Math.max(0, score);
}

function generateRecommendations(
  accessibility?: AccessibilityResult,
  performance?: PerformanceMetrics
): string[] {
  const recommendations: string[] = [];

  if (accessibility && accessibility.violations > 0) {
    recommendations.push(
      `Fix ${accessibility.violations} accessibility violation(s) to improve inclusivity`
    );

    const criticalViolations = accessibility.violationDetails.filter(
      (v) => v.impact === 'critical' || v.impact === 'serious'
    );
    if (criticalViolations.length > 0) {
      recommendations.push(
        `Address ${criticalViolations.length} critical/serious accessibility issues immediately`
      );
    }
  }

  if (performance) {
    if (performance.ttfb > 500) {
      recommendations.push('Improve server response time (TTFB > 500ms)');
    }
    if (performance.fcp > 1800) {
      recommendations.push('Optimize First Contentful Paint (FCP > 1.8s)');
    }
    if (performance.lcp > 2500) {
      recommendations.push('Optimize Largest Contentful Paint (LCP > 2.5s)');
    }
    if (performance.cls > 0.1) {
      recommendations.push('Reduce Cumulative Layout Shift (CLS > 0.1)');
    }
    if (performance.transferSize > 1_000_000) {
      recommendations.push(`Reduce page weight (${(performance.transferSize / 1_000_000).toFixed(2)}MB)`);
    }
  }

  if (recommendations.length === 0) {
    recommendations.push('Great job! No major issues detected.');
  }

  return recommendations;
}

async function generateHTMLReport(report: UIEvaluationReport, outputDir: string): Promise<void> {
  const html = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>UI Evaluation Report - ${report.url}</title>
  <style>
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      max-width: 1200px;
      margin: 0 auto;
      padding: 2rem;
      background: #f9fafb;
    }
    h1 { color: #111827; }
    h2 { color: #374151; margin-top: 2rem; }
    .score {
      font-size: 4rem;
      font-weight: bold;
      text-align: center;
      margin: 2rem 0;
      color: ${report.score >= 85 ? '#10B981' : report.score >= 70 ? '#F59E0B' : '#EF4444'};
    }
    .metric {
      background: white;
      padding: 1rem;
      margin: 1rem 0;
      border-radius: 0.5rem;
      box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    .metric-label { font-weight: 600; color: #6B7280; }
    .metric-value { font-size: 1.5rem; font-weight: bold; }
    .violation {
      background: #FEF2F2;
      border-left: 4px solid #EF4444;
      padding: 1rem;
      margin: 0.5rem 0;
    }
    .recommendation {
      background: #DBEAFE;
      border-left: 4px solid #3B82F6;
      padding: 1rem;
      margin: 0.5rem 0;
    }
    .screenshots {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1rem;
      margin: 2rem 0;
    }
    .screenshots img {
      width: 100%;
      border-radius: 0.5rem;
      box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
  </style>
</head>
<body>
  <h1>UI Evaluation Report</h1>
  <p><strong>URL:</strong> ${report.url}</p>
  <p><strong>Timestamp:</strong> ${report.timestamp}</p>
  <p><strong>Viewport:</strong> ${report.viewport.width}x${report.viewport.height}</p>

  <div class="score">${report.score}/100</div>

  ${report.screenshots ? `
    <h2>Screenshots</h2>
    <div class="screenshots">
      <div>
        <h3>Above the Fold</h3>
        <img src="screenshot-above-fold.png" alt="Above the fold screenshot">
      </div>
      <div>
        <h3>Full Page</h3>
        <img src="screenshot-full-page.png" alt="Full page screenshot">
      </div>
    </div>
  ` : ''}

  ${report.accessibility ? `
    <h2>Accessibility</h2>
    <div class="metric">
      <div class="metric-label">Violations</div>
      <div class="metric-value" style="color: ${report.accessibility.violations === 0 ? '#10B981' : '#EF4444'}">
        ${report.accessibility.violations}
      </div>
    </div>
    <div class="metric">
      <div class="metric-label">Passed Checks</div>
      <div class="metric-value" style="color: #10B981">${report.accessibility.passes}</div>
    </div>
    ${report.accessibility.violationDetails.length > 0 ? `
      <h3>Violation Details</h3>
      ${report.accessibility.violationDetails.map(v => `
        <div class="violation">
          <strong>${v.id}</strong> (${v.impact})<br>
          ${v.description}<br>
          <small>Affects ${v.nodes} element(s) - <a href="${v.helpUrl}" target="_blank">Learn more</a></small>
        </div>
      `).join('')}
    ` : ''}
  ` : ''}

  ${report.performance ? `
    <h2>Performance</h2>
    <div class="metric">
      <div class="metric-label">Time to First Byte (TTFB)</div>
      <div class="metric-value">${report.performance.ttfb.toFixed(2)}ms</div>
    </div>
    <div class="metric">
      <div class="metric-label">First Contentful Paint (FCP)</div>
      <div class="metric-value">${report.performance.fcp.toFixed(2)}ms</div>
    </div>
    <div class="metric">
      <div class="metric-label">Largest Contentful Paint (LCP)</div>
      <div class="metric-value">${report.performance.lcp.toFixed(2)}ms</div>
    </div>
    <div class="metric">
      <div class="metric-label">Cumulative Layout Shift (CLS)</div>
      <div class="metric-value">${report.performance.cls.toFixed(3)}</div>
    </div>
    <div class="metric">
      <div class="metric-label">Page Weight</div>
      <div class="metric-value">${(report.performance.transferSize / 1_000_000).toFixed(2)}MB</div>
    </div>
  ` : ''}

  <h2>Recommendations</h2>
  ${report.recommendations.map(r => `<div class="recommendation">${r}</div>`).join('')}
</body>
</html>`;

  const reportPath = path.join(outputDir, 'report.html');
  fs.writeFileSync(reportPath, html);
  console.log(`\\n📄 HTML report generated: ${reportPath}`);
}

async function evaluateUI(url: string, options: EvaluationOptions): Promise<UIEvaluationReport> {
  const browser: Browser = await chromium.launch();
  const context = await browser.newContext({
    viewport: options.viewport,
  });
  const page: Page = await context.newPage();

  console.log(`\\n🔍 Evaluating: ${url}`);
  console.log(`📐 Viewport: ${options.viewport.width}x${options.viewport.height}\\n`);

  await page.goto(url, { waitUntil: 'networkidle' });

  const report: UIEvaluationReport = {
    url,
    timestamp: new Date().toISOString(),
    viewport: options.viewport,
    score: 0,
    recommendations: [],
  };

  // Create output directory
  if (!fs.existsSync(options.outputDir)) {
    fs.mkdirSync(options.outputDir, { recursive: true });
  }

  // Capture screenshots
  if (options.screenshot) {
    report.screenshots = await captureScreenshots(page, options.outputDir);
  }

  // Run accessibility audit
  if (options.a11y) {
    report.accessibility = await runAccessibilityAudit(page);
  }

  // Measure performance
  if (options.performance) {
    report.performance = await measurePerformance(page);
  }

  // Calculate score
  report.score = calculateScore(report.accessibility, report.performance);

  // Generate recommendations
  report.recommendations = generateRecommendations(report.accessibility, report.performance);

  await browser.close();

  return report;
}

async function main() {
  const { url, options } = await parseArgs();

  try {
    const report = await evaluateUI(url, options);

    // Save JSON report
    const jsonPath = path.join(options.outputDir, 'report.json');
    fs.writeFileSync(jsonPath, JSON.stringify(report, null, 2));
    console.log(`\\n💾 JSON report saved: ${jsonPath}`);

    // Generate HTML report
    await generateHTMLReport(report, options.outputDir);

    // Print summary
    console.log(`\\n📊 Overall Score: ${report.score}/100`);
    console.log('\\n✨ Recommendations:');
    report.recommendations.forEach((r, i) => {
      console.log(`  ${i + 1}. ${r}`);
    });

    // Exit with error if score is below threshold
    if (report.score < options.threshold) {
      console.error(`\\n❌ Score ${report.score} is below threshold ${options.threshold}`);
      process.exit(1);
    }

    console.log(`\\n✅ Evaluation complete!`);
  } catch (error) {
    console.error('\\n❌ Error during evaluation:', error);
    process.exit(1);
  }
}

main();
