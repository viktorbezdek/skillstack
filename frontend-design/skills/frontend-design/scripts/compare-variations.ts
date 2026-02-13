#!/usr/bin/env node

/**
 * UI Variations Comparison Script
 *
 * Compares two or more UI variations side-by-side using screenshots,
 * accessibility scores, and performance metrics.
 *
 * Usage:
 *   npx tsx compare-variations.ts <url-a> <url-b> [url-c...] [options]
 *
 * Options:
 *   --output-dir     Directory for comparison results (default: ./ui-comparison)
 *   --viewport       Viewport size (default: 1920x1080)
 *   --mobile         Use mobile viewport (default: false)
 *   --labels         Comma-separated labels for variants (default: A,B,C...)
 */

import { chromium, Browser, Page } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';
import * as fs from 'fs';
import * as path from 'path';

interface ComparisonOptions {
  outputDir: string;
  viewport: { width: number; height: number };
  mobile: boolean;
  labels: string[];
}

interface VariantResult {
  label: string;
  url: string;
  screenshot: string;
  accessibility: {
    violations: number;
    passes: number;
  };
  performance: {
    ttfb: number;
    fcp: number;
    lcp: number;
    cls: number;
  };
  score: number;
}

interface ComparisonReport {
  timestamp: string;
  viewport: { width: number; height: number };
  variants: VariantResult[];
  winner: string;
}

async function parseArgs(): Promise<{ urls: string[]; options: ComparisonOptions }> {
  const args = process.argv.slice(2);

  if (args.length < 2) {
    console.error('Error: At least 2 URLs are required for comparison');
    console.log('Usage: npx tsx compare-variations.ts <url-a> <url-b> [url-c...] [options]');
    process.exit(1);
  }

  const urls: string[] = [];
  const options: ComparisonOptions = {
    outputDir: './ui-comparison',
    viewport: { width: 1920, height: 1080 },
    mobile: false,
    labels: [],
  };

  let i = 0;
  while (i < args.length && !args[i].startsWith('--')) {
    urls.push(args[i]);
    i++;
  }

  // Process flags
  while (i < args.length) {
    const flag = args[i];
    const value = args[i + 1];

    switch (flag) {
      case '--output-dir':
        options.outputDir = value;
        i += 2;
        break;
      case '--viewport':
        const [width, height] = value.split('x').map(Number);
        options.viewport = { width, height };
        i += 2;
        break;
      case '--mobile':
        options.mobile = value === 'true';
        i += 2;
        break;
      case '--labels':
        options.labels = value.split(',');
        i += 2;
        break;
      default:
        i++;
    }
  }

  if (options.mobile) {
    options.viewport = { width: 375, height: 667 };
  }

  // Generate default labels if not provided
  if (options.labels.length === 0) {
    options.labels = urls.map((_, index) => String.fromCharCode(65 + index)); // A, B, C, ...
  }

  if (options.labels.length !== urls.length) {
    console.error('Error: Number of labels must match number of URLs');
    process.exit(1);
  }

  return { urls, options };
}

async function evaluateVariant(
  url: string,
  label: string,
  page: Page,
  outputDir: string
): Promise<VariantResult> {
  console.log(`\\n🔍 Evaluating variant ${label}: ${url}`);

  await page.goto(url, { waitUntil: 'networkidle' });

  // Capture screenshot
  const screenshotPath = path.join(outputDir, `variant-${label}.png`);
  await page.screenshot({
    path: screenshotPath,
    fullPage: true,
    animations: 'disabled',
  });
  console.log(`  ✓ Screenshot captured`);

  // Run accessibility audit
  const a11yResults = await new AxeBuilder({ page })
    .withTags(['wcag2a', 'wcag2aa'])
    .analyze();
  console.log(`  ✓ Accessibility: ${a11yResults.violations.length} violations`);

  // Measure performance
  const perfMetrics = await page.evaluate(() => {
    const perf = performance.getEntriesByType('navigation')[0] as PerformanceNavigationTiming;
    const paint = performance.getEntriesByType('paint');
    return {
      ttfb: perf.responseStart - perf.requestStart,
      fcp: paint.find((p) => p.name === 'first-contentful-paint')?.startTime || 0,
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

  console.log(`  ✓ Performance: TTFB ${perfMetrics.ttfb.toFixed(0)}ms, FCP ${perfMetrics.fcp.toFixed(0)}ms`);

  // Calculate score
  let score = 100;
  score -= a11yResults.violations.length * 5;
  if (perfMetrics.ttfb > 500) score -= 5;
  if (perfMetrics.fcp > 1800) score -= 10;
  if (lcp > 2500) score -= 15;
  if (cls > 0.1) score -= 10;
  score = Math.max(0, score);

  return {
    label,
    url,
    screenshot: screenshotPath,
    accessibility: {
      violations: a11yResults.violations.length,
      passes: a11yResults.passes.length,
    },
    performance: {
      ttfb: perfMetrics.ttfb,
      fcp: perfMetrics.fcp,
      lcp,
      cls,
    },
    score,
  };
}

async function generateComparisonHTML(report: ComparisonReport, outputDir: string): Promise<void> {
  const html = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>UI Variations Comparison</title>
  <style>
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      max-width: 1400px;
      margin: 0 auto;
      padding: 2rem;
      background: #f9fafb;
    }
    h1 { color: #111827; }
    h2 { color: #374151; margin-top: 2rem; }
    .variants {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
      gap: 2rem;
      margin: 2rem 0;
    }
    .variant {
      background: white;
      border-radius: 0.5rem;
      padding: 1.5rem;
      box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    .variant.winner {
      border: 3px solid #10B981;
      box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.1);
    }
    .variant-label {
      font-size: 1.5rem;
      font-weight: bold;
      margin-bottom: 0.5rem;
    }
    .score {
      font-size: 3rem;
      font-weight: bold;
      text-align: center;
      margin: 1rem 0;
    }
    .score.high { color: #10B981; }
    .score.medium { color: #F59E0B; }
    .score.low { color: #EF4444; }
    .screenshot {
      width: 100%;
      border-radius: 0.5rem;
      box-shadow: 0 4px 6px rgba(0,0,0,0.1);
      margin: 1rem 0;
    }
    .metrics {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 0.5rem;
      margin-top: 1rem;
    }
    .metric {
      background: #f9fafb;
      padding: 0.75rem;
      border-radius: 0.25rem;
    }
    .metric-label {
      font-size: 0.75rem;
      color: #6B7280;
      text-transform: uppercase;
    }
    .metric-value {
      font-size: 1.25rem;
      font-weight: 600;
      color: #111827;
    }
    .comparison-table {
      width: 100%;
      border-collapse: collapse;
      background: white;
      border-radius: 0.5rem;
      overflow: hidden;
      margin: 2rem 0;
    }
    .comparison-table th {
      background: #f3f4f6;
      padding: 1rem;
      text-align: left;
      font-weight: 600;
    }
    .comparison-table td {
      padding: 1rem;
      border-top: 1px solid #e5e7eb;
    }
    .comparison-table .best {
      background: #D1FAE5;
      font-weight: 600;
    }
    .winner-badge {
      background: #10B981;
      color: white;
      padding: 0.25rem 0.75rem;
      border-radius: 9999px;
      font-size: 0.875rem;
      font-weight: 600;
      display: inline-block;
      margin-left: 0.5rem;
    }
  </style>
</head>
<body>
  <h1>UI Variations Comparison</h1>
  <p><strong>Timestamp:</strong> ${report.timestamp}</p>
  <p><strong>Viewport:</strong> ${report.viewport.width}x${report.viewport.height}</p>
  <p><strong>Winner:</strong> Variant ${report.winner} <span class="winner-badge">BEST</span></p>

  <h2>Side-by-Side Comparison</h2>
  <div class="variants">
    ${report.variants.map(v => `
      <div class="variant ${v.label === report.winner ? 'winner' : ''}">
        <div class="variant-label">
          Variant ${v.label}
          ${v.label === report.winner ? '<span class="winner-badge">WINNER</span>' : ''}
        </div>
        <p><small>${v.url}</small></p>

        <div class="score ${v.score >= 85 ? 'high' : v.score >= 70 ? 'medium' : 'low'}">
          ${v.score}/100
        </div>

        <img src="variant-${v.label}.png" alt="Variant ${v.label}" class="screenshot">

        <div class="metrics">
          <div class="metric">
            <div class="metric-label">A11y Violations</div>
            <div class="metric-value">${v.accessibility.violations}</div>
          </div>
          <div class="metric">
            <div class="metric-label">A11y Passes</div>
            <div class="metric-value">${v.accessibility.passes}</div>
          </div>
          <div class="metric">
            <div class="metric-label">TTFB</div>
            <div class="metric-value">${v.performance.ttfb.toFixed(0)}ms</div>
          </div>
          <div class="metric">
            <div class="metric-label">FCP</div>
            <div class="metric-value">${v.performance.fcp.toFixed(0)}ms</div>
          </div>
          <div class="metric">
            <div class="metric-label">LCP</div>
            <div class="metric-value">${v.performance.lcp.toFixed(0)}ms</div>
          </div>
          <div class="metric">
            <div class="metric-label">CLS</div>
            <div class="metric-value">${v.performance.cls.toFixed(3)}</div>
          </div>
        </div>
      </div>
    `).join('')}
  </div>

  <h2>Detailed Metrics Comparison</h2>
  <table class="comparison-table">
    <thead>
      <tr>
        <th>Metric</th>
        ${report.variants.map(v => `<th>Variant ${v.label}</th>`).join('')}
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Overall Score</td>
        ${report.variants.map(v => {
          const isBest = v.score === Math.max(...report.variants.map(vv => vv.score));
          return `<td class="${isBest ? 'best' : ''}">${v.score}/100</td>`;
        }).join('')}
      </tr>
      <tr>
        <td>A11y Violations</td>
        ${report.variants.map(v => {
          const isBest = v.accessibility.violations === Math.min(...report.variants.map(vv => vv.accessibility.violations));
          return `<td class="${isBest ? 'best' : ''}">${v.accessibility.violations}</td>`;
        }).join('')}
      </tr>
      <tr>
        <td>TTFB</td>
        ${report.variants.map(v => {
          const isBest = v.performance.ttfb === Math.min(...report.variants.map(vv => vv.performance.ttfb));
          return `<td class="${isBest ? 'best' : ''}">${v.performance.ttfb.toFixed(2)}ms</td>`;
        }).join('')}
      </tr>
      <tr>
        <td>FCP</td>
        ${report.variants.map(v => {
          const isBest = v.performance.fcp === Math.min(...report.variants.map(vv => vv.performance.fcp));
          return `<td class="${isBest ? 'best' : ''}">${v.performance.fcp.toFixed(2)}ms</td>`;
        }).join('')}
      </tr>
      <tr>
        <td>LCP</td>
        ${report.variants.map(v => {
          const isBest = v.performance.lcp === Math.min(...report.variants.map(vv => vv.performance.lcp));
          return `<td class="${isBest ? 'best' : ''}">${v.performance.lcp.toFixed(2)}ms</td>`;
        }).join('')}
      </tr>
      <tr>
        <td>CLS</td>
        ${report.variants.map(v => {
          const isBest = v.performance.cls === Math.min(...report.variants.map(vv => vv.performance.cls));
          return `<td class="${isBest ? 'best' : ''}">${v.performance.cls.toFixed(3)}</td>`;
        }).join('')}
      </tr>
    </tbody>
  </table>

  <h2>Recommendations</h2>
  <div style="background: #DBEAFE; border-left: 4px solid #3B82F6; padding: 1rem; margin: 1rem 0;">
    <strong>Winner:</strong> Variant ${report.winner} scored highest (${report.variants.find(v => v.label === report.winner)?.score}/100)
  </div>
  ${report.variants.filter(v => v.label !== report.winner).map(v => `
    <div style="background: #FEF3C7; border-left: 4px solid #F59E0B; padding: 1rem; margin: 1rem 0;">
      <strong>Variant ${v.label}:</strong> Consider adopting best practices from Variant ${report.winner}
      ${v.accessibility.violations > 0 ? `<br>- Fix ${v.accessibility.violations} accessibility violations` : ''}
      ${v.performance.lcp > 2500 ? '<br>- Optimize Largest Contentful Paint' : ''}
      ${v.performance.cls > 0.1 ? '<br>- Reduce Cumulative Layout Shift' : ''}
    </div>
  `).join('')}
</body>
</html>`;

  const reportPath = path.join(outputDir, 'comparison.html');
  fs.writeFileSync(reportPath, html);
  console.log(`\\n📄 Comparison report generated: ${reportPath}`);
}

async function compareVariations(urls: string[], options: ComparisonOptions): Promise<ComparisonReport> {
  const browser: Browser = await chromium.launch();
  const context = await browser.newContext({
    viewport: options.viewport,
  });

  console.log(`\\n🔬 Comparing ${urls.length} variations`);
  console.log(`📐 Viewport: ${options.viewport.width}x${options.viewport.height}`);

  // Create output directory
  if (!fs.existsSync(options.outputDir)) {
    fs.mkdirSync(options.outputDir, { recursive: true });
  }

  const variants: VariantResult[] = [];

  // Evaluate each variant
  for (let i = 0; i < urls.length; i++) {
    const page = await context.newPage();
    const result = await evaluateVariant(urls[i], options.labels[i], page, options.outputDir);
    variants.push(result);
    await page.close();
  }

  await browser.close();

  // Determine winner (highest score)
  const winner = variants.reduce((max, v) => (v.score > max.score ? v : max)).label;

  const report: ComparisonReport = {
    timestamp: new Date().toISOString(),
    viewport: options.viewport,
    variants,
    winner,
  };

  return report;
}

async function main() {
  const { urls, options } = await parseArgs();

  try {
    const report = await compareVariations(urls, options);

    // Save JSON report
    const jsonPath = path.join(options.outputDir, 'comparison.json');
    fs.writeFileSync(jsonPath, JSON.stringify(report, null, 2));
    console.log(`\\n💾 JSON report saved: ${jsonPath}`);

    // Generate HTML report
    await generateComparisonHTML(report, options.outputDir);

    // Print summary
    console.log(`\\n📊 Comparison Results:`);
    report.variants.forEach(v => {
      console.log(`  ${v.label === report.winner ? '🏆' : '  '} Variant ${v.label}: ${v.score}/100`);
    });
    console.log(`\\n✅ Winner: Variant ${report.winner}`);

  } catch (error) {
    console.error('\\n❌ Error during comparison:', error);
    process.exit(1);
  }
}

main();
