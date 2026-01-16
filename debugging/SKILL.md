---
name: debugging
description: Comprehensive debugging skill combining systematic debugging methodology, browser DevTools automation, E2E testing with visual analysis, CI/CD pipeline debugging, performance profiling, and AI-powered error analysis. Use for diagnosing bugs, test failures, performance issues, build failures, and any unexpected behavior.
license: Apache-2.0
---

# Comprehensive Debugging Skill

## Overview

This skill provides a complete debugging toolkit combining methodology, automation, and analysis tools for diagnosing and resolving software issues across the entire development lifecycle.

**Core Principle:** ALWAYS find root cause before attempting fixes. Symptom fixes are failure.

## The Iron Law of Debugging

```
NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST
```

If you haven't completed Phase 1 (Root Cause Investigation), you cannot propose fixes.

---

## Quick Reference

### When to Use This Skill

Use for ANY technical issue:
- Test failures (unit, integration, E2E)
- Bugs in production or development
- Unexpected behavior
- Performance problems
- Build failures
- CI/CD pipeline issues
- Browser/UI issues
- Integration issues

**ESPECIALLY use when:**
- Under time pressure (emergencies make guessing tempting)
- "Just one quick fix" seems obvious
- You've already tried multiple fixes
- Previous fix didn't work
- You don't fully understand the issue

### Quick Decision Matrix

| Issue Type | Primary Tool | Reference |
|------------|--------------|-----------|
| Test failures | Systematic Debugging | `references/systematic-debugging/` |
| Browser/UI bugs | Chrome DevTools + E2E Testing | `references/cdp-domains.md`, `references/e2e-workflow/` |
| CI/CD failures | Pipeline Analyzer | `scripts/cicd/`, `references/cicd-troubleshooting.md` |
| Performance issues | Performance Profiler | `references/performance-guide.md` |
| Build errors | Root Cause Tracing | `references/root-cause-tracing.md` |
| Flaky tests | Find Polluter Script | `scripts/find-polluter.sh` |

---

## Systematic Debugging Framework

### The Four Phases

You MUST complete each phase before proceeding to the next.

#### Phase 1: Root Cause Investigation

**BEFORE attempting ANY fix:**

1. **Read Error Messages Carefully**
   - Don't skip past errors or warnings
   - They often contain the exact solution
   - Read stack traces completely
   - Note line numbers, file paths, error codes

2. **Reproduce Consistently**
   - Can you trigger it reliably?
   - What are the exact steps?
   - Does it happen every time?
   - If not reproducible, gather more data, don't guess

3. **Check Recent Changes**
   - What changed that could cause this?
   - Git diff, recent commits
   - New dependencies, config changes
   - Environmental differences

4. **Gather Evidence in Multi-Component Systems**

   For EACH component boundary:
   - Log what data enters component
   - Log what data exits component
   - Verify environment/config propagation
   - Check state at each layer

5. **Trace Data Flow**
   - Where does bad value originate?
   - What called this with bad value?
   - Keep tracing up until you find the source
   - Fix at source, not at symptom

   See `references/root-cause-tracing.md` for detailed backward tracing technique.

#### Phase 2: Pattern Analysis

1. **Find Working Examples** - Locate similar working code in same codebase
2. **Compare Against References** - Read reference implementation COMPLETELY
3. **Identify Differences** - List every difference, however small
4. **Understand Dependencies** - What settings, config, environment?

#### Phase 3: Hypothesis and Testing

1. **Form Single Hypothesis** - "I think X is the root cause because Y"
2. **Test Minimally** - SMALLEST possible change to test hypothesis
3. **Verify Before Continuing** - Did it work? Yes = Phase 4, No = new hypothesis
4. **When You Don't Know** - Say "I don't understand X", don't pretend

#### Phase 4: Implementation

1. **Create Failing Test Case** - Simplest possible reproduction
2. **Implement Single Fix** - Address the root cause, ONE change at a time
3. **Verify Fix** - Test passes? No other tests broken?
4. **If 3+ Fixes Failed** - STOP and question the architecture

See `references/systematic-debugging/SKILL.md` for complete methodology.

---

## Browser Debugging Tools

### Chrome DevTools Scripts

Browser automation via executable Puppeteer scripts. All scripts output JSON for easy parsing.

**Installation:**
```bash
cd scripts/chrome-devtools
./install-deps.sh  # Linux/WSL only
npm install
```

**Available Scripts:**
- `navigate.js` - Navigate to URLs
- `screenshot.js` - Capture screenshots (auto-compresses >5MB)
- `click.js` - Click elements
- `fill.js` - Fill form fields
- `evaluate.js` - Execute JavaScript in page context
- `snapshot.js` - Extract interactive elements with metadata
- `console.js` - Monitor console messages/errors
- `network.js` - Track HTTP requests/responses
- `performance.js` - Measure Core Web Vitals + record traces

**Usage Pattern:**
```bash
cd scripts/chrome-devtools
node screenshot.js --url https://example.com --output ./page.png
node console.js --url https://example.com --types error,warn --duration 5000
```

**References:**
- `references/cdp-domains.md` - 47 Chrome DevTools Protocol domains
- `references/puppeteer-reference.md` - Complete Puppeteer API patterns
- `references/performance-guide.md` - Core Web Vitals optimization

---

## E2E Testing with Visual Debugging

### Overview

Automated Playwright e2e testing with LLM-powered visual debugging, screenshot capture, and fix recommendations.

**Key Capabilities:**
- Zero-setup automation with multi-framework support
- Visual debugging with screenshot capture and LLM analysis
- Regression testing with baseline comparison
- Actionable fix recommendations with file:line references

### Workflow Phases

1. **Phase 1: Discovery** - Detect app type, framework versions (`references/e2e-workflow/phase-1-discovery.md`)
2. **Phase 2: Setup** - Install Playwright, generate config (`references/e2e-workflow/phase-2-setup.md`)
3. **Phase 2.5: Preflight** - Validate app loads correctly (`references/e2e-workflow/phase-2.5-preflight.md`)
4. **Phase 3: Generation** - Create screenshot-enabled tests (`references/e2e-workflow/phase-3-generation.md`)
5. **Phase 4: Capture** - Run tests and capture visual data (`references/e2e-workflow/phase-4-capture.md`)
6. **Phase 5: Analysis** - LLM-powered visual analysis (`references/e2e-workflow/phase-5-analysis.md`)
7. **Phase 6: Regression** - Compare screenshots against baselines (`references/e2e-workflow/phase-6-regression.md`)
8. **Phase 7: Fixes** - Map issues to source code (`references/e2e-workflow/phase-7-fixes.md`)
9. **Phase 8: Export** - Package production-ready test suite (`references/e2e-workflow/phase-8-export.md`)

**Templates:**
- `templates/e2e-testing/playwright.config.template.ts`
- `templates/e2e-testing/test-spec.template.ts`
- `templates/e2e-testing/page-object.template.ts`
- `templates/e2e-testing/screenshot-helper.template.ts`

**Examples:**
- `examples/e2e-testing/react-vite/` - React Vite example
- `examples/e2e-testing/reports/` - Report examples

---

## CI/CD Pipeline Debugging

### Pipeline Analysis

**Quick Health Check:**
```bash
python3 scripts/cicd/ci_health.py --platform github --repo owner/repo
```

**Pipeline Optimization Analysis:**
```bash
python3 scripts/cicd/pipeline_analyzer.py --platform github --workflow .github/workflows/ci.yml
```

### Common Pipeline Issues

| Error Pattern | Common Cause | Quick Fix |
|---------------|--------------|-----------|
| "Module not found" | Missing dependency or cache issue | Clear cache, run `npm ci` |
| "Timeout" | Job taking too long | Add caching, increase timeout |
| "Permission denied" | Missing permissions | Add to `permissions:` block |
| "Cannot connect to Docker" | Docker not available | Use correct runner or DinD |
| Intermittent failures | Flaky tests or race conditions | Add retries, fix timing issues |

### Enable Debug Logging

**GitHub Actions:**
```yaml
# Add repository secrets:
# ACTIONS_RUNNER_DEBUG = true
# ACTIONS_STEP_DEBUG = true
```

**GitLab CI:**
```yaml
variables:
  CI_DEBUG_TRACE: "true"
```

**References:**
- `references/cicd-troubleshooting.md` - Comprehensive CI/CD debugging
- `references/cicd-best_practices.md` - Pipeline design patterns
- `references/cicd-optimization.md` - Performance tuning
- `references/cicd-security.md` - Security patterns
- `references/cicd-devsecops.md` - Security scanning (SAST, DAST, SCA)

**Templates:**
- `templates/cicd/github-actions/` - GitHub Actions templates
- `templates/cicd/gitlab-ci/` - GitLab CI templates

---

## Finding Test Polluters

When something appears during tests but you don't know which test causes it:

```bash
./scripts/find-polluter.sh '.git' 'src/**/*.test.ts'
```

Runs tests one-by-one, stops at first polluter.

---

## Defense-in-Depth Validation

After finding and fixing a bug, add validation at EVERY layer data passes through:

1. **Layer 1: Entry Point Validation** - Reject obviously invalid input at API boundary
2. **Layer 2: Business Logic Validation** - Ensure data makes sense for this operation
3. **Layer 3: Environment Guards** - Prevent dangerous operations in specific contexts
4. **Layer 4: Debug Instrumentation** - Capture context for forensics

See `references/defense-in-depth.md` for complete pattern.

---

## Verification Before Completion

**The Iron Law:**
```
NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE
```

Before claiming any status:
1. IDENTIFY: What command proves this claim?
2. RUN: Execute the FULL command (fresh, complete)
3. READ: Full output, check exit code, count failures
4. VERIFY: Does output confirm the claim?
5. ONLY THEN: Make the claim

See `references/verification-before-completion.md` for complete checklist.

---

## AI-Powered Debugging

For complex error analysis, use the AI-powered debugging module:

**Features:**
- Error type classification
- Pattern matching against known issues
- Solution generation with code examples
- Prevention strategy recommendations
- Fix time estimation

See `references/workflow-modules/ai-debugging.md` for implementation details.

---

## Red Flags - STOP and Follow Process

If you catch yourself thinking:
- "Quick fix for now, investigate later"
- "Just try changing X and see if it works"
- "Add multiple changes, run tests"
- "Skip the test, I'll manually verify"
- "It's probably X, let me fix that"
- "I don't fully understand but this might work"
- "One more fix attempt" (when already tried 2+)

**ALL of these mean: STOP. Return to Phase 1.**

---

## Resource Directory

### References
- `references/systematic-debugging/` - Core debugging methodology
- `references/root-cause-tracing.md` - Backward tracing technique
- `references/defense-in-depth.md` - Multi-layer validation
- `references/verification-before-completion.md` - Verification checklist
- `references/cdp-domains.md` - Chrome DevTools Protocol reference
- `references/puppeteer-reference.md` - Puppeteer API patterns
- `references/performance-guide.md` - Performance debugging
- `references/playwright-best-practices.md` - Playwright patterns
- `references/troubleshooting.md` - Common issues and fixes
- `references/ci-cd-integration.md` - CI/CD integration guide
- `references/cicd-*.md` - CI/CD specific references
- `references/e2e-workflow/` - E2E testing workflow phases
- `references/e2e-data/` - E2E testing data and patterns
- `references/workflow-modules/` - AI-powered debugging modules

### Scripts
- `scripts/chrome-devtools/` - Browser automation scripts
- `scripts/cicd/` - CI/CD analysis tools
- `scripts/find-polluter.sh` - Test pollution finder
- `scripts/workflow/` - Workflow automation

### Templates
- `templates/e2e-testing/` - Playwright test templates
- `templates/cicd/github-actions/` - GitHub Actions templates
- `templates/cicd/gitlab-ci/` - GitLab CI templates

### Examples
- `examples/e2e-testing/` - E2E testing examples
- `examples/workflow/` - Workflow examples

---

## Real-World Impact

From debugging sessions:
- Systematic approach: 15-30 minutes to fix
- Random fixes approach: 2-3 hours of thrashing
- First-time fix rate: 95% vs 40%
- New bugs introduced: Near zero vs common

---

## External Resources

- [Puppeteer Documentation](https://pptr.dev/)
- [Chrome DevTools Protocol](https://chromedevtools.github.io/devtools-protocol/)
- [Playwright Documentation](https://playwright.dev/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitLab CI Documentation](https://docs.gitlab.com/ee/ci/)












