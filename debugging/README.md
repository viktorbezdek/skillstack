# Debugging

> Comprehensive debugging toolkit combining systematic methodology, browser DevTools automation, E2E visual testing, CI/CD pipeline debugging, performance profiling, and AI-powered error analysis.

## Overview

Software debugging is one of the most time-consuming activities in development, yet most teams approach it with ad-hoc "try and see" methods that waste hours and often introduce new bugs. This skill replaces guesswork with a rigorous, four-phase methodology that consistently resolves issues in 15-30 minutes instead of 2-3 hours.

The Debugging skill is designed for any developer who encounters test failures, production bugs, performance problems, CI/CD pipeline issues, or browser/UI defects. It enforces a strict "no fixes without root cause investigation" discipline and provides executable scripts, reference materials, and templates for every common debugging scenario.

As part of the SkillStack collection, this skill integrates with the E2E testing workflow, CI/CD pipeline analysis, and performance profiling tools, creating a unified debugging experience from local development through production monitoring.

## What's Included

### References

- `references/systematic-debugging/SKILL.md` - Core four-phase debugging methodology
- `references/systematic-debugging/CREATION-LOG.md` - Methodology creation log
- `references/systematic-debugging/test-academic.md` - Academic test case for the methodology
- `references/systematic-debugging/test-pressure-1.md` - Pressure test scenario 1
- `references/systematic-debugging/test-pressure-2.md` - Pressure test scenario 2
- `references/systematic-debugging/test-pressure-3.md` - Pressure test scenario 3
- `references/root-cause-tracing.md` - Backward tracing technique for finding bug origins
- `references/defense-in-depth.md` - Multi-layer validation pattern after fixing bugs
- `references/verification-before-completion.md` - Checklist to verify fixes before claiming done
- `references/cdp-domains.md` - 47 Chrome DevTools Protocol domain reference
- `references/puppeteer-reference.md` - Complete Puppeteer API patterns and usage
- `references/performance-guide.md` - Core Web Vitals and performance debugging guide
- `references/playwright-best-practices.md` - Playwright testing patterns and best practices
- `references/troubleshooting.md` - Common issues and their fixes
- `references/ci-cd-integration.md` - CI/CD integration guide for debugging workflows
- `references/cicd-troubleshooting.md` - Comprehensive CI/CD debugging reference
- `references/cicd-best_practices.md` - Pipeline design patterns and conventions
- `references/cicd-optimization.md` - CI/CD performance tuning strategies
- `references/cicd-security.md` - Security patterns for CI/CD pipelines
- `references/cicd-devsecops.md` - Security scanning (SAST, DAST, SCA) integration
- `references/e2e-workflow/phase-1-discovery.md` - App type and framework detection
- `references/e2e-workflow/phase-2-setup.md` - Playwright installation and config generation
- `references/e2e-workflow/phase-2.5-preflight.md` - App load validation
- `references/e2e-workflow/phase-3-generation.md` - Screenshot-enabled test creation
- `references/e2e-workflow/phase-4-capture.md` - Test execution and visual data capture
- `references/e2e-workflow/phase-5-analysis.md` - LLM-powered visual analysis
- `references/e2e-workflow/phase-6-regression.md` - Screenshot baseline comparison
- `references/e2e-workflow/phase-7-fixes.md` - Issue-to-source-code mapping
- `references/e2e-workflow/phase-8-export.md` - Production-ready test suite packaging
- `references/e2e-data/accessibility-checks.md` - Accessibility validation checks
- `references/e2e-data/common-ui-bugs.md` - Common UI bug patterns
- `references/e2e-data/error-patterns.yaml` - Error pattern definitions
- `references/e2e-data/framework-detection-patterns.yaml` - Framework detection rules
- `references/e2e-data/framework-versions.yaml` - Framework version compatibility
- `references/e2e-data/playwright-best-practices.md` - Playwright best practices for E2E
- `references/workflow-modules/ai-debugging.md` - AI-powered error analysis module
- `references/workflow-modules/automated-code-review.md` - Automated code review module
- `references/workflow-modules/performance-optimization.md` - Performance optimization module
- `references/workflow-modules/smart-refactoring.md` - Intelligent refactoring module
- `references/workflow-modules/tdd-context7.md` - TDD with Context7 integration
- `references/workflow-modules/README.md` - Workflow modules overview

### Scripts

- `scripts/chrome-devtools/navigate.js` - Navigate browser to URLs via CDP
- `scripts/chrome-devtools/screenshot.js` - Capture screenshots (auto-compresses >5MB)
- `scripts/chrome-devtools/click.js` - Click elements in the browser
- `scripts/chrome-devtools/fill.js` - Fill form fields programmatically
- `scripts/chrome-devtools/evaluate.js` - Execute JavaScript in page context
- `scripts/chrome-devtools/snapshot.js` - Extract interactive elements with metadata
- `scripts/chrome-devtools/console.js` - Monitor console messages and errors
- `scripts/chrome-devtools/network.js` - Track HTTP requests and responses
- `scripts/chrome-devtools/performance.js` - Measure Core Web Vitals and record traces
- `scripts/chrome-devtools/install-deps.sh` - Install Linux/WSL dependencies
- `scripts/chrome-devtools/install.sh` - Install Node.js dependencies
- `scripts/chrome-devtools/lib/browser.js` - Browser connection helper library
- `scripts/chrome-devtools/lib/selector.js` - CSS selector utilities
- `scripts/cicd/ci_health.py` - CI/CD pipeline health check tool
- `scripts/cicd/pipeline_analyzer.py` - Pipeline optimization analyzer
- `scripts/find-polluter.sh` - Find which test pollutes shared state
- `scripts/workflow/with_server.py` - Run commands with a temporary server

### Templates

- `templates/e2e-testing/playwright.config.template.ts` - Playwright configuration template
- `templates/e2e-testing/test-spec.template.ts` - E2E test specification template
- `templates/e2e-testing/page-object.template.ts` - Page Object Model template
- `templates/e2e-testing/screenshot-helper.template.ts` - Screenshot capture helper template
- `templates/e2e-testing/global-setup.template.ts` - Global test setup template
- `templates/e2e-testing/global-teardown.template.ts` - Global test teardown template
- `templates/e2e-testing/configs/postcss-tailwind-v3.js` - PostCSS config for Tailwind v3
- `templates/e2e-testing/configs/postcss-tailwind-v4.js` - PostCSS config for Tailwind v4
- `templates/e2e-testing/css/tailwind-v3.css` - Base Tailwind v3 CSS
- `templates/e2e-testing/css/tailwind-v4.css` - Base Tailwind v4 CSS
- `templates/e2e-testing/css/vanilla.css` - Vanilla CSS fallback
- `templates/alfred-integration.md` - Alfred app integration template
- `templates/cicd/github-actions/node-ci.yml` - Node.js CI workflow for GitHub Actions
- `templates/cicd/github-actions/python-ci.yml` - Python CI workflow for GitHub Actions
- `templates/cicd/github-actions/go-ci.yml` - Go CI workflow for GitHub Actions
- `templates/cicd/github-actions/docker-build.yml` - Docker build workflow for GitHub Actions
- `templates/cicd/github-actions/security-scan.yml` - Security scanning workflow for GitHub Actions
- `templates/cicd/gitlab-ci/node-ci.yml` - Node.js CI workflow for GitLab CI
- `templates/cicd/gitlab-ci/python-ci.yml` - Python CI workflow for GitLab CI
- `templates/cicd/gitlab-ci/go-ci.yml` - Go CI workflow for GitLab CI
- `templates/cicd/gitlab-ci/docker-build.yml` - Docker build workflow for GitLab CI
- `templates/cicd/gitlab-ci/security-scan.yml` - Security scanning workflow for GitLab CI

### Examples

- `examples/e2e-testing/react-vite/example-test.spec.ts` - Example Playwright test for React Vite app
- `examples/e2e-testing/react-vite/example-page-object.ts` - Example Page Object for React Vite app
- `examples/e2e-testing/reports/visual-analysis-report.example.md` - Sample visual analysis report
- `examples/e2e-testing/reports/fix-recommendations.example.md` - Sample fix recommendation report
- `examples/workflow/ai-powered-testing.py` - AI-powered testing workflow example
- `examples/workflow/console_logging.py` - Console logging automation example
- `examples/workflow/element_discovery.py` - Element discovery automation example
- `examples/workflow/static_html_automation.py` - Static HTML automation example

## Key Features

- Four-phase systematic debugging methodology (Root Cause, Pattern Analysis, Hypothesis Testing, Implementation)
- "Iron Law" enforcement: no fixes without root cause investigation
- Chrome DevTools Protocol automation with 9 executable Puppeteer scripts
- E2E visual debugging with LLM-powered screenshot analysis across 8 workflow phases
- CI/CD pipeline health checking and optimization for GitHub Actions and GitLab CI
- Test polluter detection for flaky test suites
- Defense-in-depth validation patterns for multi-layer bug prevention
- AI-powered error classification, pattern matching, and solution generation
- Ready-to-use CI/CD templates for Node.js, Python, Go, Docker, and security scanning

## Usage Examples

**Diagnose a failing test:**
```
I have a test that's failing intermittently in CI but passes locally. Help me debug it.
```
Activates the systematic debugging framework starting with Phase 1 (Root Cause Investigation), checks for environment differences, and uses the find-polluter script if test pollution is suspected.

**Debug a browser UI issue:**
```
The login form submit button doesn't respond on mobile. Help me debug this.
```
Uses Chrome DevTools scripts to capture screenshots, inspect element state, monitor console errors, and analyze network requests to identify the root cause.

**Analyze a slow CI/CD pipeline:**
```
Our GitHub Actions CI takes 25 minutes. Help me optimize it.
```
Runs the pipeline analyzer to identify bottlenecks, suggests caching strategies, parallelization opportunities, and provides optimized workflow templates.

**Investigate a performance regression:**
```
Page load time jumped from 2s to 8s after the last deployment. Help me profile it.
```
Uses the performance script to measure Core Web Vitals, record traces, and identify the specific change causing the regression via root cause tracing.

**Set up E2E visual testing:**
```
Set up Playwright E2E tests with visual regression detection for our React app.
```
Follows the 8-phase E2E workflow from discovery through export, generating page objects, test specs, and screenshot baseline comparison infrastructure.

## Quick Start

1. **Identify your issue type** using the Quick Decision Matrix in SKILL.md to find the right tool.

2. **Follow Phase 1** -- read error messages carefully, reproduce consistently, check recent changes, and trace data flow. Do not skip to fixing.

3. **For browser issues**, install the Chrome DevTools scripts:
   ```bash
   cd scripts/chrome-devtools && npm install
   node screenshot.js --url http://localhost:3000 --output ./debug.png
   ```

4. **For CI/CD issues**, run the health check:
   ```bash
   python3 scripts/cicd/ci_health.py --platform github --repo owner/repo
   ```

5. **For flaky tests**, find the polluting test:
   ```bash
   ./scripts/find-polluter.sh '.git' 'src/**/*.test.ts'
   ```

6. **Verify your fix** using the verification checklist before claiming the issue is resolved.

## Related Skills

- **edge-case-coverage** -- Identify boundary conditions that cause bugs before they happen
- **docker-containerization** -- Debug containerized applications and CI/CD Docker builds
- **git-workflow** -- Track down regressions with git bisect and commit analysis
- **frontend-design** -- Debug UI/UX issues with accessibility and responsive design patterns
- **documentation-generator** -- Document debugging runbooks and troubleshooting guides

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 34 production-grade skills for Claude Code.
