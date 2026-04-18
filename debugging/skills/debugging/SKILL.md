---
name: debugging
description: |
  Finds and fixes bugs through systematic root cause analysis, stack trace interpretation, browser DevTools automation, CI/CD pipeline debugging, performance profiling, test pollution detection, and AI-powered error analysis. Use when the user asks to debug, fix a bug, investigate an error, analyze a stack trace, find root cause of a failure, profile performance, diagnose test failures (unit/integration/E2E), troubleshoot CI/CD pipelines, debug flaky tests, use Chrome DevTools, or trace data flow to source. NOT for writing new tests or setting up test frameworks (use testing-framework), NOT for TDD methodology or writing tests before code (use test-driven-development), NOT for reviewing code quality or PRs (use code-review), NOT for designing CI/CD pipelines (use cicd-pipelines), NOT for feature development or refactoring (use language-specific plugins).
license: Apache-2.0
---

# Comprehensive Debugging Skill

**Core Principle:** ALWAYS find root cause before attempting fixes. Symptom fixes are failure.

## The Iron Law of Debugging

```
NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST
```

## When to Use / Not Use

**Use when:**
- Test failures (unit, integration, E2E)
- Bugs in production or development
- Unexpected behavior or performance problems
- Build failures or CI/CD pipeline issues
- Browser/UI issues
- ESPECIALLY when under time pressure, "just one quick fix" seems obvious, or you've already tried multiple fixes

**Do NOT use when:**
- Writing new tests or setting up test frameworks -> use `testing-framework`
- TDD methodology or writing tests before code -> use `test-driven-development`
- Reviewing code quality or PRs -> use `code-review`
- Designing CI/CD pipelines -> use `cicd-pipelines`

## Decision Tree

```
What type of issue are you debugging?
├── Test failure
│   ├── Always fails (deterministic) -> Phase 1-4 systematic debugging
│   ├── Intermittently fails (flaky) -> find-polluter.sh + timing analysis
│   └── Only fails in CI, not locally -> Environment audit (OS, runtime, services)
├── Browser/UI bug
│   ├── Visual/layout issue -> Chrome DevTools scripts + screenshot
│   ├── Console errors -> console.js monitoring
│   ├── Network/API issue -> network.js tracking
│   └── Performance issue -> performance.js + Core Web Vitals
├── CI/CD pipeline failure
│   ├── Build error (module not found, etc.) -> Root cause tracing + cache check
│   ├── Timeout -> Pipeline analyzer + caching optimization
│   ├── Permission error -> Permissions block audit
│   └── Docker connection issue -> Runner/DinD configuration
├── Performance regression
│   ├── Known when it started -> Git diff between good and current deploy
│   └── Unknown source -> Performance profiler + trace recording
├── 3+ fix attempts have failed
│   └── STOP. Question the architecture. Return to Phase 1.
└── Not a debugging problem? -> See related skills
```

## Quick Decision Matrix

| Issue Type | Primary Tool | Reference |
|------------|--------------|-----------|
| Test failures | Systematic Debugging | `references/systematic-debugging/` |
| Browser/UI bugs | Chrome DevTools + E2E Testing | `references/cdp-domains.md`, `references/e2e-workflow/` |
| CI/CD failures | Pipeline Analyzer | `scripts/cicd/`, `references/cicd-troubleshooting.md` |
| Performance issues | Performance Profiler | `references/performance-guide.md` |
| Build errors | Root Cause Tracing | `references/root-cause-tracing.md` |
| Flaky tests | Find Polluter Script | `scripts/find-polluter.sh` |

## The Four Phases

You MUST complete each phase before proceeding to the next.

### Phase 1: Root Cause Investigation

**BEFORE attempting ANY fix:**

1. **Read Error Messages Carefully** — Don't skip past errors; they often contain the exact solution. Read stack traces completely. Note line numbers, file paths, error codes.
2. **Reproduce Consistently** — Can you trigger it reliably? If not reproducible, gather more data, don't guess.
3. **Check Recent Changes** — Git diff, recent commits, new dependencies, config changes, environmental differences.
4. **Gather Evidence in Multi-Component Systems** — For each component boundary: log data in, log data out, verify config propagation, check state at each layer.
5. **Trace Data Flow** — Where does the bad value originate? Keep tracing up until you find the source. Fix at source, not at symptom.

See `references/root-cause-tracing.md` for detailed backward tracing technique.

### Phase 2: Pattern Analysis

1. Find working examples in same codebase
2. Compare against reference implementation COMPLETELY
3. List every difference, however small
4. Understand dependencies: settings, config, environment

### Phase 3: Hypothesis and Testing

1. Form single hypothesis: "I think X is the root cause because Y"
2. Test minimally — smallest possible change to test hypothesis
3. Verify before continuing — Did it work? Yes = Phase 4, No = new hypothesis
4. When you don't know — Say "I don't understand X", don't pretend

### Phase 4: Implementation

1. Create failing test case — simplest possible reproduction
2. Implement single fix — address the root cause, ONE change at a time
3. Verify fix — Test passes? No other tests broken?
4. If 3+ fixes failed — STOP and question the architecture

## Browser Debugging Tools

**Installation:**
```bash
cd scripts/chrome-devtools && npm install
```

**Available Scripts:**
| Script | Purpose |
|--------|---------|
| `navigate.js` | Navigate to URLs |
| `screenshot.js` | Capture screenshots (auto-compresses >5MB) |
| `click.js` | Click elements |
| `fill.js` | Fill form fields |
| `evaluate.js` | Execute JavaScript in page context |
| `snapshot.js` | Extract interactive elements with metadata |
| `console.js` | Monitor console messages/errors |
| `network.js` | Track HTTP requests/responses |
| `performance.js` | Measure Core Web Vitals + record traces |

**Usage:**
```bash
cd scripts/chrome-devtools
node screenshot.js --url https://example.com --output ./page.png
node console.js --url https://example.com --types error,warn --duration 5000
```

## E2E Testing Workflow

8-phase visual debugging with Playwright:
1. **Discovery** — Detect app type, framework (`references/e2e-workflow/phase-1-discovery.md`)
2. **Setup** — Install Playwright, generate config
3. **Preflight** — Validate app loads correctly
4. **Generation** — Create screenshot-enabled tests
5. **Capture** — Run tests and capture visual data
6. **Analysis** — LLM-powered visual analysis
7. **Regression** — Compare screenshots against baselines
8. **Export** — Package production-ready test suite

Templates: `templates/e2e-testing/` | Examples: `examples/e2e-testing/`

## CI/CD Pipeline Debugging

```bash
python3 scripts/cicd/ci_health.py --platform github --repo owner/repo
python3 scripts/cicd/pipeline_analyzer.py --platform github --workflow .github/workflows/ci.yml
```

| Error Pattern | Common Cause | Quick Fix |
|---------------|-------------|-----------|
| "Module not found" | Missing dependency or cache issue | Clear cache, run `npm ci` |
| "Timeout" | Job taking too long | Add caching, increase timeout |
| "Permission denied" | Missing permissions | Add to `permissions:` block |
| "Cannot connect to Docker" | Docker not available | Use correct runner or DinD |
| Intermittent failures | Flaky tests or race conditions | Add retries, fix timing issues |

**Debug logging:** GitHub Actions: `ACTIONS_RUNNER_DEBUG=true` | GitLab CI: `CI_DEBUG_TRACE: "true"`

## Test Pollution Detection

```bash
./scripts/find-polluter.sh '.git' 'src/**/*.test.ts'
```
Runs tests one-by-one, stops at first polluter.

## Defense-in-Depth Validation

After fixing a bug, add validation at EVERY layer:
1. **Entry Point** — Reject obviously invalid input at API boundary
2. **Business Logic** — Ensure data makes sense for this operation
3. **Environment Guards** — Prevent dangerous operations in specific contexts
4. **Debug Instrumentation** — Capture context for forensics

See `references/defense-in-depth.md` for complete pattern.

## Verification Before Completion

```
NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE
```

1. IDENTIFY: What command proves this claim?
2. RUN: Execute the FULL command (fresh, complete)
3. READ: Full output, check exit code, count failures
4. VERIFY: Does output confirm the claim?
5. ONLY THEN: Make the claim

## Anti-Patterns

| Anti-Pattern | Problem | Solution |
|---|---|---|
| "Quick fix for now, investigate later" | Creates more bugs than it resolves; root cause remains | Iron Law: no fixes without Phase 1. Always complete root cause investigation first |
| Guessing at fixes without understanding | 40% first-time fix rate vs 95% systematic; 2-3 hours vs 15-30 min | Follow all 4 phases; form single hypothesis and test minimally |
| "Just try changing X and see if it works" | Random changes compound problems; introduce new bugs | Test ONE hypothesis at a time with smallest possible change |
| Adding multiple changes at once | Cannot identify which change fixed (or broke) what | One change at a time; verify after each |
| Skipping the test / manual verification only | No regression protection; bug will recur | Always create failing test case first (Phase 4, Step 1) |
| 3+ failed fix attempts without stopping | Indicates wrong root cause hypothesis | STOP after 3 failures; question the architecture; return to Phase 1 |
| Trusting "API returns 200" as success | 200 status doesn't mean response shape is correct for consumer | Check actual response data, not just status; validate contracts |
| Proposing fixes before investigation | "I think the fix is X" skips root cause analysis | Let Phase 1 complete before suggesting any fix |
| Omitting the stack trace | Most information-dense debugging input discarded | Always paste exact error message, stack trace, file paths, line numbers |
|| Fixing at symptom, not source | Bad value originates elsewhere; symptom fix masks real problem | Trace data flow upstream to source; fix at origin (Phase 1, Step 5) |
|| Assuming "it works" after one test passes | Fix may not cover edge cases; other components may break | Run full test suite after fix; verify at each defense layer |
|| Debugging without a failing test | No reproducibility; can't verify fix works or stays fixed | Create failing test first (Phase 4, Step 1); it's proof the fix is correct |
|| Ignoring environment differences | Bug appears only in CI/production but not locally | Audit OS, runtime version, env vars, services, network before assuming code is the cause |

## Red Flags — STOP and Follow Process

If you catch yourself thinking:
- "Quick fix for now, investigate later"
- "Just try changing X and see if it works"
- "Add multiple changes, run tests"
- "Skip the test, I'll manually verify"
- "It's probably X, let me fix that"
- "I don't fully understand but this might work"
- "One more fix attempt" (when already tried 2+)

**ALL of these mean: STOP. Return to Phase 1.**

## Resource Directory

### References
- `references/systematic-debugging/` — Core debugging methodology
- `references/root-cause-tracing.md` — Backward tracing technique
- `references/defense-in-depth.md` — Multi-layer validation
- `references/verification-before-completion.md` — Verification checklist
- `references/cdp-domains.md` — Chrome DevTools Protocol (47 domains)
- `references/puppeteer-reference.md` — Puppeteer API patterns
- `references/performance-guide.md` — Performance debugging
- `references/cicd-*.md` — CI/CD specific references
- `references/e2e-workflow/` — E2E testing workflow phases
- `references/workflow-modules/` — AI-powered debugging modules

### Scripts
- `scripts/chrome-devtools/` — Browser automation scripts
- `scripts/cicd/` — CI/CD analysis tools
- `scripts/find-polluter.sh` — Test pollution finder

### Templates
- `templates/e2e-testing/` — Playwright test templates
- `templates/cicd/` — GitHub Actions + GitLab CI templates

## Integration

- testing-framework — Set up test infrastructure debugging depends on
- test-driven-development — Write tests first; debugging handles what gets through
- code-review — Catch bugs before they reach debugging
- cicd-pipelines — Design CI/CD pipelines; debugging handles when they break
- docker-containerization — Container environments where many CI/CD bugs originate
