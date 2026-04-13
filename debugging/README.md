> **v1.1.26** | Development | 28 iterations

# Debugging

> Find and fix bugs through systematic root cause analysis -- from stack traces and test failures to browser debugging, CI/CD pipelines, and performance profiling.

## The Problem

When something breaks, developers guess. They change something that looks related, run the tests, and if it does not work, they change something else. After three failed attempts in 90 minutes, they are further from the solution than when they started because each speculative fix introduced new variables. The original bug is now buried under layers of failed patches. The codebase has uncommitted changes across six files. And the developer has lost track of what they actually changed versus what was already broken.

This happens because debugging is treated as an art rather than a process. There is no standard methodology that says "do this before that" and "stop if you have tried three fixes without understanding the root cause." Teams lack tooling for the full debugging spectrum: they know how to read a stack trace but not how to automate browser inspection, trace data flow across multi-component systems, diagnose flaky tests by finding the polluting test, or debug CI/CD pipelines that fail in ways local environments cannot reproduce.

The cost is enormous. Studies consistently show that debugging consumes 50% or more of development time. The difference between systematic debugging (15-30 minutes, 95% first-time fix rate) and random-fix debugging (2-3 hours, 40% fix rate, frequent introduction of new bugs) is not talent -- it is process.

## The Solution

This plugin enforces a systematic four-phase debugging methodology (root cause investigation, pattern analysis, hypothesis testing, implementation) backed by concrete tooling for every debugging domain: Chrome DevTools automation scripts for browser debugging, an eight-phase E2E testing workflow with visual analysis, CI/CD pipeline analyzers for GitHub Actions and GitLab CI, performance profiling with Core Web Vitals, a test pollution finder for flaky tests, and an AI-powered error classification module.

The iron law -- "no fixes without root cause investigation" -- is enforced through the phase structure. Phase 1 requires reading errors completely, reproducing consistently, checking recent changes, gathering evidence at component boundaries, and tracing data flow to the source. Only after completing Phase 1 can you form a hypothesis (Phase 3), and only after testing it minimally can you implement a fix (Phase 4). If three fixes fail, the process forces you to stop and question the architecture rather than trying a fourth speculative fix.

The plugin ships with executable scripts, Playwright templates, CI/CD workflow templates, and examples that make the methodology immediately actionable -- not just theory but tools you can run against real bugs today.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Guess at fixes, change random things, spend 2-3 hours thrashing | Systematic four-phase process: investigate, analyze, hypothesize, implement -- 15-30 minutes average |
| Try to fix symptoms without understanding the root cause | Iron law enforcement: no fixes until root cause is identified through evidence |
| No process for browser-side debugging beyond manual DevTools clicks | Chrome DevTools automation scripts: screenshots, console monitoring, network tracking, performance traces |
| CI/CD failures are opaque -- "works on my machine" | Pipeline analyzers and CI-specific debugging references for GitHub Actions and GitLab CI |
| Flaky tests get retried or ignored with no diagnosis | Test pollution finder (`find-polluter.sh`) isolates the exact test causing intermittent failures |
| After fixing a bug, similar bugs appear in other code paths | Defense-in-depth validation adds checks at every layer data passes through |

## Installation

Add the SkillStack marketplace, then install this plugin:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install debugging@skillstack
```

### Verify installation

After installing, test with:

```
I have a failing test that passes when I run it alone but fails in the full suite -- help me debug this
```

## Quick Start

1. Install the plugin using the commands above
2. Describe your bug: `My API returns 500 on the /users endpoint but only in production -- staging works fine`
3. The skill enforces Phase 1: read the error logs completely, reproduce the failure, check what changed between staging and production, and trace the data flow
4. After root cause identification, the skill guides you through a minimal hypothesis test and single-fix implementation with verification
5. Post-fix, it walks you through defense-in-depth: adding validation at the entry point, business logic, and environment layers so the bug category cannot recur

## What's Inside

| Component | Description |
|---|---|
| `debugging` skill | Core skill with the four-phase systematic methodology, iron law enforcement, decision matrix, browser debugging, E2E workflow, CI/CD debugging, and verification requirements |
| 18 reference items | Systematic debugging methodology, root cause tracing, defense-in-depth, verification checklist, CDP domains, Puppeteer API, Playwright patterns, performance guide, CI/CD troubleshooting/optimization/security/DevSecOps, E2E workflow phases, and AI debugging modules |
| Scripts | Chrome DevTools automation (9 scripts), CI/CD analysis tools, test pollution finder, workflow automation |
| Templates | Playwright test templates (config, test spec, page object, screenshot helper), GitHub Actions and GitLab CI workflow templates |
| Examples | React Vite E2E testing examples, report examples, workflow examples |
| 13 trigger eval cases | Validates correct skill activation and near-miss rejection |
| 3 output eval cases | Tests debugging guidance, root cause analysis, and fix quality |

### debugging

**What it does:** Activates when you need to debug any technical issue -- test failures, production bugs, browser issues, CI/CD pipeline failures, performance problems, build errors, or flaky tests. Enforces the iron law of root cause investigation before any fix attempt and provides domain-specific tooling for each debugging context.

**Try these prompts:**

```
My test passes in isolation but fails when run with the full suite -- help me find which test is polluting the state
```

```
I'm getting a 401 error on my API endpoint but the JWT token looks valid -- walk me through systematic root cause investigation
```

```
Our CI pipeline has been failing intermittently for a week -- sometimes the E2E tests time out, sometimes they pass. Debug this.
```

```
My React app renders correctly on initial load but breaks after navigation -- I need to debug this with browser DevTools
```

```
We shipped a performance regression -- page load went from 1.2s to 4.8s after last week's deploy. Help me profile and identify the cause.
```

**Key references:**

| Reference | Topic |
|---|---|
| `systematic-debugging/` | Complete four-phase debugging methodology with detailed procedures for each phase |
| `root-cause-tracing.md` | Backward tracing technique for finding the true source of a bug across component boundaries |
| `defense-in-depth.md` | Multi-layer validation pattern: entry point, business logic, environment guards, and debug instrumentation |
| `verification-before-completion.md` | Verification checklist requiring fresh evidence before any completion claim |
| `cdp-domains.md` | 47 Chrome DevTools Protocol domains for programmatic browser debugging |
| `puppeteer-reference.md` | Complete Puppeteer API patterns for browser automation |
| `performance-guide.md` | Core Web Vitals optimization and performance profiling techniques |
| `playwright-best-practices.md` | Playwright testing patterns for reliable E2E tests |
| `cicd-troubleshooting.md` | CI/CD pipeline debugging for GitHub Actions and GitLab CI |
| `cicd-optimization.md` | Pipeline performance tuning and caching strategies |
| `e2e-workflow/` | Eight-phase E2E testing workflow from discovery through export |

## Real-World Walkthrough

You are maintaining a Node.js API for an e-commerce platform. A customer reports that their checkout fails intermittently -- about 30% of the time, they get a 500 error on the payment endpoint. Your team has been unable to reproduce it locally.

You open Claude Code:

```
Our checkout endpoint returns 500 about 30% of the time in production. We can't reproduce it locally. The error logs show "Connection refused" from our payment processor, but their status page shows no issues.
```

The debugging skill activates and immediately enforces Phase 1: Root Cause Investigation.

**Step 1: Read errors carefully.** The skill asks you to share the full error logs, not just the summary. You pull the production logs and share the complete stack trace. The skill notices something you glossed over: the error is not "Connection refused" generically -- it is "Connection refused" from a specific IP address that is your payment processor's API gateway in the us-east-2 region, while your other calls succeed against us-west-2. This is not a payment processor outage. It is a regional routing issue.

**Step 2: Reproduce consistently.** You cannot reproduce locally because your development environment always hits us-west-2. The skill guides you to add a DNS override or force the us-east-2 endpoint: `PAYMENT_API_HOST=api-east.processor.com npm test`. You run the checkout endpoint 10 times against the east endpoint. It fails 4 times. Now you have a reproducible failure.

**Step 3: Check recent changes.** You pull the git log from the past week. The skill spots a commit from 4 days ago that changed the payment client's connection pooling configuration: `maxSockets` was changed from 10 to 2 as part of a "resource optimization" effort. The timing matches when customer complaints started.

**Step 4: Trace data flow.** The skill walks you through instrumenting the payment client. You add logging at the connection pool layer and discover: when `maxSockets` is 2 and your checkout handler makes 3 concurrent requests to the payment processor (charge, fraud check, and receipt generation), the third request waits for a socket. The us-east-2 endpoint has higher latency than us-west-2 (180ms vs 40ms), so under load, the socket wait queue builds up and eventually times out, producing "Connection refused" when the pool cannot allocate a connection within the timeout.

**Root cause identified:** The combination of reduced connection pool size and higher latency on the east region endpoint causes socket exhaustion under normal checkout load. Neither the pool size reduction nor the east region latency would cause the issue alone -- it is the interaction.

**Phase 3: Hypothesis testing.** The skill guides you to test minimally: revert `maxSockets` to 10 and run the east endpoint test again. 10 attempts, 0 failures. Hypothesis confirmed.

**Phase 4: Implementation.** You revert the `maxSockets` change and add two layers of defense-in-depth:

1. **Entry point validation:** The payment client constructor now validates that `maxSockets` is at least 5 (the minimum needed for a checkout flow), logging a warning if configured lower.
2. **Business logic validation:** The checkout handler checks socket pool availability before starting the three parallel requests, queuing them sequentially if the pool is near capacity.

You write a test that simulates the exact failure condition: 2 max sockets, 3 concurrent requests, 200ms latency. The test fails before the fix (confirming it catches the bug) and passes after. You run the full test suite -- all green.

The skill reminds you to verify in production, not just locally. You deploy to a canary, monitor for 1 hour, and confirm zero payment failures. The fix goes to full production. Customer complaints stop immediately.

Total debugging time: 45 minutes. If you had followed the initial instinct of "payment processor must be flaky, add retry logic," you would have masked the real issue, introduced retry-related billing problems, and spent days chasing the wrong problem.

## Usage Scenarios

### Scenario 1: Flaky test investigation

**Context:** Your test suite has 3 tests that fail intermittently in CI but always pass when run individually. The team has been adding `@retry(3)` annotations to suppress them.

**You say:** `Three tests fail randomly in CI but pass alone -- help me find the polluter instead of just retrying them`

**The skill provides:**
- Test pollution finder script (`find-polluter.sh`) that runs tests one-by-one to isolate the exact polluting test
- Systematic approach: identify shared state (global variables, database records, file system, environment variables)
- Root cause patterns for common polluters: test order dependencies, uncleared database state, singleton mutations
- Fix verification: run the full suite 5 times consecutively to confirm the flakiness is resolved

**You end up with:** The specific test causing pollution identified, the shared state mechanism understood, and a fix that eliminates the flakiness permanently.

### Scenario 2: Production-only bug

**Context:** Your API works perfectly in development and staging but returns errors in production. The code is identical -- something in the environment is different.

**You say:** `This endpoint works in staging but returns 500 in production -- same code, same database migration. What's different?`

**The skill provides:**
- Systematic environment diff checklist: environment variables, service versions, network configuration, DNS resolution, certificate chains, connection pool sizes
- Multi-component evidence gathering at each boundary
- Data flow tracing through the production stack
- Hypothesis testing with minimal production changes

**You end up with:** The specific environmental difference causing the failure, identified through systematic elimination rather than guessing.

### Scenario 3: CI/CD pipeline debugging

**Context:** Your GitHub Actions pipeline started failing after a Node.js version update. The error message is unhelpful and the build succeeds locally.

**You say:** `Our CI pipeline broke after upgrading to Node 22 -- the build fails with a cryptic error but it works locally. Help me debug the pipeline.`

**The skill provides:**
- CI/CD specific debugging: enable debug logging, compare local vs CI environment
- Pipeline analysis with the CI health checker script
- Common patterns: dependency cache invalidation after version changes, native module recompilation, changed default settings
- Pipeline optimization to prevent similar issues

**You end up with:** The root cause identified (often a cached `node_modules` from the old version or a native dependency that needs recompilation) and a CI configuration that handles version upgrades gracefully.

### Scenario 4: Performance regression investigation

**Context:** Your web application's Largest Contentful Paint went from 1.2s to 4.8s after last week's deployment. Users are complaining.

**You say:** `Our LCP went from 1.2s to 4.8s after last week's deploy -- help me profile and find what caused the regression`

**The skill provides:**
- Chrome DevTools performance scripts for automated profiling
- Core Web Vitals measurement and baseline comparison
- Systematic bisection: which commit in last week's deploy introduced the regression?
- Performance trace analysis: long tasks, render blocking resources, layout thrashing

**You end up with:** The specific change causing the regression identified, a performance test to prevent recurrence, and the LCP restored to acceptable levels.

## Ideal For

- **Developers who spend too long on bugs** -- the four-phase methodology cuts average debugging time from hours to minutes
- **Teams with flaky test suites** -- the pollution finder and systematic approach eliminate intermittent failures permanently
- **Frontend developers debugging browser issues** -- Chrome DevTools automation scripts provide programmatic access to console, network, and performance data
- **DevOps engineers troubleshooting CI/CD** -- pipeline analyzers and CI-specific references diagnose build failures that do not reproduce locally
- **Anyone who has tried 3+ fixes without success** -- the process forces you to stop guessing and find root cause

## Not For

- **Writing new tests or setting up test frameworks** -- use [testing-framework](../testing-framework/) instead
- **TDD methodology** (writing tests before code) -- use [test-driven-development](../test-driven-development/) instead
- **Code review or PR quality assessment** -- use [code-review](../code-review/) instead

## How It Works Under the Hood

The plugin is a single-skill architecture with extensive reference materials, executable scripts, templates, and examples.

The **core skill** (`SKILL.md`) defines the four-phase systematic debugging methodology with iron law enforcement, a quick decision matrix routing issues to the right tool, browser debugging with Chrome DevTools automation, an eight-phase E2E testing workflow, CI/CD pipeline debugging for major platforms, test pollution detection, defense-in-depth validation, and verification requirements.

The **reference library** provides depth across six domains:
- **Systematic debugging** -- complete methodology with detailed phase procedures and red flag detection
- **Browser debugging** -- 47 Chrome DevTools Protocol domains, Puppeteer API patterns, Playwright best practices, and performance profiling with Core Web Vitals
- **E2E testing** -- eight workflow phases from discovery through export, with visual debugging and LLM-powered analysis
- **CI/CD debugging** -- troubleshooting, optimization, security, and DevSecOps references for GitHub Actions and GitLab CI
- **Root cause tracing** -- backward tracing technique for multi-component systems, defense-in-depth validation pattern
- **AI debugging** -- error classification, pattern matching against known issues, and fix time estimation

The **scripts directory** ships executable tools: 9 Chrome DevTools automation scripts (navigate, screenshot, click, fill, evaluate, snapshot, console, network, performance), CI/CD analysis tools (health checker, pipeline analyzer), and a test pollution finder. The **templates directory** provides Playwright test templates and CI/CD workflow templates for immediate use.

## Related Plugins

- **[Testing Framework](../testing-framework/)** -- Test infrastructure setup, framework selection, and test suite authoring across languages
- **[Test-Driven Development](../test-driven-development/)** -- TDD methodology: red-green-refactor cycle, writing tests before implementation
- **[Code Review](../code-review/)** -- Multi-agent code review covering security, performance, style, and test coverage
- **[CI/CD Pipelines](../cicd-pipelines/)** -- Pipeline design and DevOps automation for GitHub Actions, GitLab CI, and Terraform

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
