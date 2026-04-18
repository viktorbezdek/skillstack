> **v1.1.27** | Development | 29 iterations

# Debugging

> Find and fix bugs through systematic root cause analysis -- stack trace interpretation, browser DevTools automation, E2E testing with visual analysis, CI/CD pipeline debugging, performance profiling, and AI-powered error analysis.
> Single skill + 38 reference documents + 9 scripts + 15 templates + 8 examples | 13 trigger evals, 3 output evals

## The Problem

Developers spend 35-50% of their time debugging. The average debugging session takes 2-3 hours -- not because bugs are inherently complex, but because the approach is wrong. The typical pattern: see an error, guess a fix, try it, it does not work, try another guess, get deeper into the weeds, finally find the root cause 2 hours later. Under time pressure, this degenerates further: "quick fix for now, investigate later" creates more bugs than it resolves.

The problem compounds across the development lifecycle. Test failures are diagnosed by reading the assertion message and guessing, when the failing test often contains the exact root cause in the stack trace. Browser bugs are investigated by manually clicking through the UI, when DevTools automation can capture screenshots, console errors, and network traffic in seconds. CI/CD failures are debugged by re-running the pipeline and hoping it passes, when systematic analysis of the failure log reveals the pattern. Performance issues are addressed by adding caching everywhere, when profiling shows one specific query is responsible.

Each debugging domain (unit tests, browser, CI/CD, performance) has its own tools and patterns. Teams that lack a systematic framework for any of these domains default to guessing -- and guessing is expensive. Studies show systematic debugging achieves a 95% first-time fix rate versus 40% for random fixes, in 15-30 minutes versus 2-3 hours.

## The Solution

This plugin provides a comprehensive debugging toolkit combining methodology, automation scripts, and analysis tools across the entire development lifecycle. The core is the Iron Law of Debugging: no fixes without root cause investigation first. The skill enforces a four-phase process (Root Cause Investigation, Pattern Analysis, Hypothesis Testing, Implementation) and provides domain-specific tools for each debugging context.

For browser debugging, the plugin ships 9 Chrome DevTools automation scripts (navigation, screenshots, element interaction, console monitoring, network tracking, performance measurement). For E2E testing, it provides an 8-phase visual debugging workflow with Playwright, including LLM-powered screenshot analysis and regression detection. For CI/CD, it includes pipeline analysis scripts and a troubleshooting guide covering GitHub Actions, GitLab CI, and common failure patterns. For performance, it provides Core Web Vitals measurement and profiling guides. For test pollution, it ships a find-polluter script that isolates which test is contaminating others.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| See error, guess fix, try it, repeat for 2-3 hours | Four-phase systematic process: investigate root cause, analyze patterns, test hypothesis, implement fix in 15-30 min |
| Under time pressure, skip investigation and apply "quick fix" | Iron Law enforced: no fixes without Phase 1 completion; red flags trigger process reset |
| Browser bugs investigated by manual clicking | 9 DevTools automation scripts capture screenshots, console errors, network traffic, performance metrics |
| CI/CD failures debugged by re-running and hoping | Pipeline analyzer and troubleshooting reference systematically diagnose failure patterns |
| "Works on my machine" with no way to reproduce browser issues | E2E testing workflow with visual debugging, screenshot comparison, and regression detection |
| 40% first-time fix rate with frequent regression introduction | 95% first-time fix rate with defense-in-depth validation at every layer |

## Context to Provide

The single biggest predictor of fast debugging is error specificity. "My code is broken" produces a methodology lecture. A full stack trace, the exact conditions that reproduce the bug, and what you have already tried produce a targeted root cause analysis. The skill enforces root cause investigation before suggesting fixes -- give it the raw evidence, not your hypothesis about the cause.

**What to include in your prompt:**
- **The exact error message and full stack trace** -- do not paraphrase; paste the literal text including file paths and line numbers
- **Reproduction conditions** -- does it fail always or intermittently? Locally or only in CI? With specific inputs?
- **What changed recently** -- the git commits, dependency updates, or configuration changes immediately before the failure appeared
- **What you have already tried** -- each attempted fix and why it did not work; this prevents the skill from suggesting approaches you have already ruled out
- **The environment** (OS, runtime version, test runner, CI platform) -- especially for "works on my machine" failures

**What makes results better:**
- Pasting the actual stack trace rather than paraphrasing it -- the skill identifies patterns in specific file paths and line numbers
- Describing the test that fails by name and which assertion fails, not just "the test fails"
- For CI failures: including the relevant workflow log section, not just "CI is failing"
- For browser bugs: naming the browser, version, and whether DevTools console shows errors
- Mentioning if you have already tried multiple fixes -- this is a signal the root cause has not been identified yet

**What makes results worse:**
- Proposing your own fix first -- "I think the fix is X, should I try it?" skips root cause investigation; the skill enforces investigation before fixes
- Providing only the symptom without the error -- "my tests are slow" is not enough without profiling data
- Omitting the stack trace -- the exact error message and file/line references are the most information-dense input the skill has

**Template prompt:**
```
[Test/Component/Endpoint] fails with:

[paste exact error message and stack trace]

Conditions: [always / intermittently / only in CI / only in specific browser / only with specific input]. Recent changes: [what changed before this started]. I have already tried: [list of attempted fixes and why each failed]. Environment: [OS, runtime version, test runner, CI platform if relevant].
```

## Installation

Add the SkillStack marketplace and install:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install debugging@skillstack
```

### Prerequisites

For browser debugging: Node.js and npm (for Puppeteer scripts). For CI/CD analysis: Python 3. For E2E testing: Playwright (`npm install @playwright/test`). All are optional -- the systematic debugging methodology works without any scripts.

### Verify installation

After installing, test with:

```
I have a test failing with "TypeError: Cannot read properties of undefined" but only in CI, not locally. How do I debug this?
```

## Quick Start

1. Install the plugin using the commands above
2. Encounter a bug. Ask: `"My integration tests pass locally but fail in CI with timeout errors. Help me debug this systematically."`
3. The skill enforces Phase 1: read the error carefully, reproduce consistently, check recent changes, trace data flow
4. Follow up with: `"I found the error is in the database connection. What's the root cause tracing approach?"`
5. The skill walks you through backward tracing from symptom to source, then defense-in-depth validation

---

## System Overview

```
debugging (plugin)
└── debugging (skill)
    ├── Core methodology (Iron Law + 4 phases)
    ├── Browser debugging
    │   ├── scripts/chrome-devtools/ (9 automation scripts)
    │   ├── references/cdp-domains.md (47 CDP protocol domains)
    │   └── references/puppeteer-reference.md (complete API)
    ├── E2E testing workflow
    │   ├── references/e2e-workflow/ (8 phases: discovery → export)
    │   ├── templates/e2e-testing/ (Playwright templates)
    │   └── examples/e2e-testing/ (React Vite examples, reports)
    ├── CI/CD debugging
    │   ├── scripts/cicd/ (pipeline analyzer, health check)
    │   ├── references/cicd-*.md (5 CI/CD references)
    │   └── templates/cicd/ (GitHub Actions + GitLab CI)
    ├── Performance profiling
    │   └── references/performance-guide.md (Core Web Vitals)
    ├── Defense-in-depth validation
    ├── AI-powered error analysis
    │   └── references/workflow-modules/ (6 advanced modules)
    └── scripts/find-polluter.sh (test pollution finder)
```

## What's Inside

| Component | Type | Description |
|---|---|---|
| `debugging` | Skill | Core four-phase methodology, domain-specific debugging guides |
| `systematic-debugging/` | Reference set | Core debugging methodology with pressure tests |
| `root-cause-tracing.md` | Reference | Backward tracing technique from symptom to source |
| `defense-in-depth.md` | Reference | Multi-layer validation after fixing bugs |
| `verification-before-completion.md` | Reference | Verification checklist before claiming completion |
| `cdp-domains.md` | Reference | 47 Chrome DevTools Protocol domains |
| `puppeteer-reference.md` | Reference | Complete Puppeteer API patterns |
| `performance-guide.md` | Reference | Core Web Vitals optimization and profiling |
| `playwright-best-practices.md` | Reference | Playwright patterns for E2E testing |
| `e2e-workflow/` | Reference set | 8-phase E2E testing workflow (discovery through export) |
| `e2e-data/` | Reference set | Accessibility checks, common UI bugs, Playwright practices |
| `cicd-*.md` | Reference set | CI/CD troubleshooting, best practices, optimization, security, DevSecOps |
| `workflow-modules/` | Reference set | AI debugging, automated code review, performance optimization, TDD, refactoring |
| `troubleshooting.md` | Reference | Common issues and framework-specific fixes |
| Chrome DevTools scripts | Scripts | 9 scripts: navigate, screenshot, click, fill, evaluate, snapshot, console, network, performance |
| CI/CD scripts | Scripts | Pipeline analyzer, CI health check |
| `find-polluter.sh` | Script | Isolates which test is polluting shared state |
| E2E templates | Templates | Playwright config, test spec, page object, screenshot helper, global setup/teardown |
| CI/CD templates | Templates | GitHub Actions and GitLab CI templates for Node, Python, Go, Docker, security |
| E2E examples | Examples | React Vite test examples, visual analysis report examples |

### Component Spotlights

#### debugging (skill)

**What it does:** Activates on any technical debugging scenario -- test failures, browser bugs, CI/CD issues, performance problems. Enforces the Iron Law (no fixes without root cause investigation) and guides through four phases: Root Cause Investigation (read errors, reproduce, check changes, trace data flow), Pattern Analysis (find working examples, compare against references), Hypothesis Testing (form single hypothesis, test minimally), and Implementation (failing test, single fix, verify).

**Input -> Output:** Error description, stack trace, or failing behavior -> Systematic diagnosis identifying the root cause, a targeted fix addressing the source (not the symptom), defense-in-depth validation, and verification evidence.

**When to use:**
- Any test failure (unit, integration, E2E)
- Bugs in production or development
- Performance problems
- CI/CD pipeline failures
- Browser or UI issues
- Especially when under time pressure or after multiple failed fix attempts

**When NOT to use:**
- Writing new tests or setting up frameworks (use `testing-framework`)
- TDD methodology or writing tests before code (use `test-driven-development`)
- Code review or PR review (use `code-review`)

**Try these prompts:**

```
AuthService.test.ts fails with "connection refused" but only in GitHub Actions, not locally. Error:

Error: connect ECONNREFUSED 127.0.0.1:5432
    at TCPConnectWrap.afterConnect [as oncomplete] (node:net:1494:16)

The test starts a PostgreSQL container in beforeAll(). Recent change: we added a caching step to the workflow 3 days ago. Walk me through systematic debugging for this environment-specific failure.
```

```
I've tried 3 different fixes for what I think is a race condition in our queue processor. The test still fails intermittently. I'm starting to doubt my root cause hypothesis. Here's the test, the production code, and the three things I tried.

[paste code and attempted fixes]
```

```
My React checkout component renders correctly in Chrome 120 but the shipping address section collapses to zero height in Safari 17. The DevTools console shows no errors. How do I use the inspector to diagnose this CSS layout issue?
```

```
Our GitHub Actions test suite passes 70% of the time. When it fails, the error is always in user.integration.test.ts but different assertions fail each time. This started last Tuesday after we added the Redis session store. How do I isolate which test is causing the pollution?
```

**Key references (selected):**

| Reference | Topic |
|---|---|
| `systematic-debugging/` | Core four-phase debugging methodology with pressure test scenarios |
| `root-cause-tracing.md` | Backward tracing from symptom to source |
| `defense-in-depth.md` | Multi-layer validation at entry point, business logic, environment, instrumentation |
| `cdp-domains.md` | 47 Chrome DevTools Protocol domains for browser automation |
| `e2e-workflow/` | 8-phase visual debugging workflow: discovery through export |
| `cicd-troubleshooting.md` | Comprehensive CI/CD debugging for GitHub Actions, GitLab CI |
| `performance-guide.md` | Core Web Vitals measurement and optimization |
| `workflow-modules/ai-debugging.md` | AI-powered error classification, pattern matching, solution generation |

#### Chrome DevTools Scripts (scripts)

**What they do:** 9 Puppeteer-based automation scripts for browser debugging. Navigate to URLs, capture screenshots, click elements, fill forms, execute JavaScript in page context, extract interactive element metadata, monitor console messages, track network requests, and measure Core Web Vitals with trace recording.

**CLI:** `node scripts/chrome-devtools/<script>.js --url <url> [--options]`

**Typical workflow:** Screenshot a broken page, monitor console errors while reproducing the issue, capture network requests to identify failed API calls, measure performance to find bottlenecks.

#### find-polluter.sh (script)

**What it does:** Runs tests one-by-one to isolate which test is contaminating shared state and causing intermittent failures in other tests.

**CLI:** `./scripts/find-polluter.sh '.git' 'src/**/*.test.ts'`

**Typical workflow:** You have intermittent test failures that depend on test execution order. Run find-polluter to identify the contaminating test, then fix the shared state leakage.

#### CI/CD Analysis (scripts)

**What they do:** `ci_health.py` runs a quick health check on CI pipelines. `pipeline_analyzer.py` analyzes workflow YAML files for optimization opportunities.

**CLI:** `python3 scripts/cicd/ci_health.py --platform github --repo owner/repo`

---

## Prompt Patterns

### Good Prompts vs Bad Prompts

| Bad (vague, won't activate) | Good (specific, activates reliably) |
|---|---|
| "My code is broken" | "I'm getting 'TypeError: Cannot read properties of undefined' at line 42 of auth.service.ts. Here's the stack trace: ..." |
| "Fix this test" | "This test passes alone but fails when run with the full suite. I think another test is polluting global state." |
| "CI is failing" | "Our GitHub Actions workflow fails with 'Module not found: express' after adding a caching step. The log shows npm install succeeded." |
| "It's slow" | "This API endpoint takes 3 seconds to respond. It was 200ms last week. What changed and how do I profile it?" |

### Structured Prompt Templates

**For test failures:**
```
Test [name] fails with [error message] at [file:line]. Stack trace: [trace]. It [always/sometimes] fails [locally/in CI/both]. Recent changes: [what changed]. Help me find the root cause.
```

**For browser bugs:**
```
[Component] renders [incorrectly/not at all] in [browser]. Expected behavior: [what should happen]. Actual behavior: [what happens]. Console errors: [if any]. How do I debug this?
```

**For CI/CD failures:**
```
Our [GitHub Actions/GitLab CI] pipeline fails at the [step name] step with [error]. This started [when]. The relevant workflow config is [config]. What's causing this?
```

### Prompt Anti-Patterns

- **Proposing fixes before investigation:** "I think the fix is X, should I try it?" The skill enforces root cause investigation first. Proposed fixes before Phase 1 is complete are red flags.
- **Providing error messages without context:** "I get a 500 error" is not enough. Share the stack trace, the endpoint, recent changes, and whether it is reproducible.
- **Asking to skip debugging:** "Just tell me the fix" undermines the entire methodology. The Iron Law exists because guessing costs 4-6x more time than systematic investigation.

## Real-World Walkthrough

**Starting situation:** Your team deployed a release on Friday afternoon. Monday morning, customer support reports that 10% of users cannot log in. The login page loads but submitting credentials returns a blank page. No error message is displayed. Your monitoring shows the /api/auth/login endpoint returning 200 OK. The backend team says "our API works fine."

**Step 1: Root Cause Investigation -- Read the error.** You ask: "Users can't log in -- blank page after credential submission. API returns 200 OK. No visible error. Help me debug this systematically."

The skill starts with Phase 1. First question: if the API returns 200, the backend is probably not the issue. The blank page after submission suggests a frontend error that is swallowed. Check the browser console.

**Step 2: Browser automation.** You use the Chrome DevTools console script to monitor errors: `node scripts/chrome-devtools/console.js --url https://app.example.com/login --types error,warn --duration 10000`. The output captures: `TypeError: Cannot read properties of undefined (reading 'accessToken')` at `auth.js:142`. The 200 response body changed shape -- it now returns `{data: {accessToken: ...}}` instead of `{accessToken: ...}` -- but the frontend still reads `response.accessToken`.

**Step 3: Check recent changes.** Git log shows a backend PR merged Friday at 4pm that "standardized API response format." The PR wrapped all responses in a `{data: ...}` envelope. The backend returns 200 OK (technically correct) but the frontend reads the old response shape and gets `undefined`.

**Step 4: Root cause tracing.** The root cause is not the backend change -- it is the lack of a contract between frontend and backend. The backend changed the contract unilaterally. Fixing just the frontend access pattern would work today but leave the same vulnerability for next time.

**Step 5: Defense-in-depth.** The skill recommends fixes at four layers: (1) Entry point: add response shape validation in the API client -- if the expected field is missing, throw a descriptive error instead of silently returning undefined. (2) Business logic: update the auth flow to handle both old and new response formats during the migration period. (3) Environment guard: add a contract test that verifies the response shape matches the frontend's expectations. (4) Debug instrumentation: log response shapes for auth calls to detect future contract breaks immediately.

**Step 6: Implementation.** Write a failing test that reproduces the issue (test expects `response.data.accessToken`). Fix the frontend API client. Verify the test passes. Run the full suite. Deploy the contract test to CI. Total time: 45 minutes from report to fix deployed.

**Gotchas discovered:** The "API returns 200" was the misleading signal. A 200 status code does not mean the response is correct for the consumer. The skill's insistence on checking the browser console (rather than trusting the backend team's assertion) cut through the finger-pointing in 2 minutes.

## Usage Scenarios

### Scenario 1: Flaky tests in CI

**Context:** Your test suite passes 80% of the time. Some tests fail intermittently, but nobody can reproduce the failures locally.

**You say:** "We have flaky tests. They pass locally but fail randomly in CI. How do I find which test is causing the pollution?"

**The skill provides:**
- `find-polluter.sh` script to isolate the contaminating test
- Pattern analysis for common flakiness sources (shared state, timing dependencies, resource contention)
- Condition-based waiting patterns to replace arbitrary `sleep` calls
- CI-specific debugging configuration (ACTIONS_RUNNER_DEBUG for GitHub Actions)

**You end up with:** The specific polluting test identified, shared state leakage fixed, and CI reliability restored.

### Scenario 2: Performance regression after deployment

**Context:** Your main page load time jumped from 1.2s to 4.5s after the latest deployment.

**You say:** "Page load time tripled after our last deploy. How do I profile this and find the bottleneck?"

**The skill provides:**
- Performance measurement script for Core Web Vitals
- Trace recording for detailed analysis
- Systematic comparison: git diff between last good and current deploy
- Reference to performance guide for LCP, FID, CLS optimization

**You end up with:** The specific change causing the regression identified, a targeted fix, and performance monitoring to prevent recurrence.

### Scenario 3: E2E visual regression

**Context:** After a CSS refactor, your E2E tests pass but the UI looks wrong. Tests check functionality, not appearance.

**You say:** "Our E2E tests pass but the UI is visually broken after a CSS change. How do I add visual regression testing?"

**The skill provides:**
- 8-phase E2E workflow from discovery through export
- Screenshot capture and baseline comparison
- LLM-powered visual analysis for detecting layout, color, and spacing issues
- Playwright templates and page object patterns

**You end up with:** A visual regression test suite that catches appearance issues alongside functional tests.

---

## Decision Logic

**Which debugging tool should I use?**

| Issue Type | Primary Tool | When to Escalate |
|---|---|---|
| Test failures (unit/integration) | Systematic Debugging (4 phases) | If 3+ fixes fail, question architecture |
| Browser/UI bugs | Chrome DevTools scripts + E2E workflow | If not reproducible, use visual regression |
| CI/CD failures | Pipeline analyzer + troubleshooting reference | If intermittent, use find-polluter |
| Performance issues | Performance profiler + Core Web Vitals | If systemic, use profiling traces |
| Build errors | Root cause tracing | If dependency-related, check lock files |
| Flaky tests | find-polluter.sh | If not state pollution, check timing |

**What happens when Phase 1 is incomplete?**

The skill enforces sequencing. If you try to propose a fix before completing root cause investigation, the skill redirects: "You haven't identified the root cause yet. What was the exact error message? Can you reproduce it consistently? What changed recently?" This prevents the most expensive debugging anti-pattern: guessing at fixes without understanding the problem.

## Failure Modes & Edge Cases

| Failure | Symptom | Recovery |
|---|---|---|
| Heisenbug: bug disappears when you try to observe it | Adding logging or breakpoints changes timing enough to mask the issue | Use non-invasive observation (network monitoring, console capture); check for race conditions that are timing-sensitive |
| Root cause is in a dependency, not your code | Stack trace leads into node_modules or a library you do not control | Verify dependency version, check issue trackers, consider workaround at the integration boundary |
| Multiple bugs masquerading as one symptom | Fixing the first bug reveals a second bug with similar symptoms; appears like the fix did not work | After each fix, re-verify the exact original symptom; if the symptom changes, it is a second bug, not a failed fix |
| "Works on my machine" -- environment-specific failure | Bug occurs only in CI, only in production, or only on specific hardware | Audit environment differences: OS, runtime version, environment variables, available services, network configuration |

## Ideal For

- **Developers of any experience level** who want to cut debugging time from hours to minutes through systematic investigation instead of guessing
- **Frontend engineers** who need browser debugging automation for visual issues, console monitoring, and network analysis
- **DevOps engineers** debugging CI/CD pipeline failures across GitHub Actions, GitLab CI, and containerized environments
- **Tech leads** who want to establish debugging discipline on their teams and reduce the "random fix" culture that introduces regressions

## Not For

- **Writing new tests or setting up test frameworks** -- use `testing-framework` for test infrastructure and configuration
- **TDD methodology (red-green-refactor)** -- use `test-driven-development` for the test-first workflow
- **Code review or PR quality assessment** -- use `code-review` for reviewing code quality

## Related Plugins

- **testing-framework** -- Set up the test infrastructure that debugging depends on
- **test-driven-development** -- Write tests first to prevent bugs; debugging handles the bugs that get through
- **code-review** -- Catch bugs before they reach debugging through systematic code review
- **cicd-pipelines** -- Design CI/CD pipelines; debugging handles when they break
- **docker-containerization** -- Container environments where many CI/CD bugs originate

---

*SkillStack plugin by [Viktor Bezdek](https://github.com/viktorbezdek) -- licensed under MIT.*
