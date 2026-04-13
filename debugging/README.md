> **v1.1.26** | Development | 28 iterations

# Debugging

Systematic debugging methodology combined with browser DevTools automation, Playwright E2E visual debugging, CI/CD pipeline analysis, and AI-powered error classification -- all enforced by an iron law: no fixes without root cause investigation first.

## What Problem Does This Solve

Debugging failures almost always stem from the same root cause: jumping to fixes before establishing root cause. Engineers under time pressure guess, try multiple changes at once, and introduce new bugs while chasing symptoms. After three failed fix attempts, the problem is usually architectural -- not a matter of trying one more thing. This skill enforces a four-phase framework (root cause investigation, pattern analysis, hypothesis testing, single-change implementation) and combines it with concrete automation tools: Puppeteer scripts for Chrome DevTools automation, an eight-phase Playwright E2E workflow with LLM-powered visual analysis, CI/CD pipeline health checks, and a test polluter finder for flaky test suites.

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install debugging@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention the triggers below, or you can invoke it explicitly.

## What's Inside

This is a large single-skill plugin with extensive references, scripts, templates, and examples:

| Component | Description |
|---|---|
| `skills/debugging/SKILL.md` | Core skill: the iron law of debugging, four-phase systematic framework, quick decision matrix by issue type, browser debugging tools overview, E2E testing workflow, CI/CD pipeline debugging, test polluter detection, defense-in-depth validation, and verification protocol |
| **References** | |
| `references/systematic-debugging/` | Complete systematic debugging methodology |
| `references/root-cause-tracing.md` | Backward tracing technique for finding the source of bad values |
| `references/defense-in-depth.md` | Four-layer validation pattern (entry point, business logic, environment guards, debug instrumentation) |
| `references/cdp-domains.md` | 47 Chrome DevTools Protocol domains reference |
| `references/puppeteer-reference.md` | Complete Puppeteer API patterns |
| `references/performance-guide.md` | Core Web Vitals optimization and performance profiling |
| `references/playwright-best-practices.md` | Playwright patterns and best practices |
| `references/e2e-workflow/` | Eight-phase E2E testing workflow (discovery through export) |
| `references/cicd-*.md` | Five CI/CD references: troubleshooting, best practices, optimization, security, DevSecOps |
| **Scripts** | |
| `scripts/chrome-devtools/` | Nine Puppeteer scripts: navigate, screenshot, click, fill, evaluate, snapshot, console, network, performance |
| `scripts/cicd/` | CI health check and pipeline analyzer (GitHub Actions, GitLab CI) |
| `scripts/find-polluter.sh` | Runs tests one-by-one to find which test contaminates shared state |
| **Templates** | |
| `templates/e2e-testing/` | Playwright config, test spec, page object, and screenshot helper templates |
| `templates/cicd/` | GitHub Actions and GitLab CI pipeline templates |
| **Examples** | |
| `examples/e2e-testing/` | React Vite example with page objects and report samples |
| `examples/workflow/` | AI-powered testing, console logging, element discovery, static HTML automation |

## Usage Scenarios

**1. Bug that resists multiple fix attempts**

You have tried three fixes and none worked. The skill enforces: stop and return to Phase 1. Read the error messages completely (they often contain the exact solution). Reproduce the bug consistently with exact steps. Check recent changes via `git diff`. Trace the data flow backward from the symptom to the source. Fix at the source, not where the error appears. If 3+ fixes have failed, question the approach -- the pattern is wrong, not the fix.

**2. Visual UI regression with no obvious code change**

The app looks broken in the browser but tests pass. Use the Chrome DevTools scripts: `screenshot.js` captures the page, `console.js` monitors for JavaScript errors, `network.js` tracks failed requests, `performance.js` measures Core Web Vitals. For systematic visual regression, the eight-phase Playwright E2E workflow captures screenshots, compares against baselines, performs LLM-powered visual analysis, and maps issues to specific file:line locations with fix recommendations.

**3. CI/CD pipeline fails intermittently**

Your pipeline works sometimes and fails other times. Run `ci_health.py` for a quick health check, then `pipeline_analyzer.py` on your workflow file. The common error pattern table maps symptoms to causes: "Module not found" (dependency cache issue), "Timeout" (add caching or increase timeout), "Permission denied" (missing permissions block), intermittent failures (flaky tests or race conditions). Enable debug logging with `ACTIONS_RUNNER_DEBUG` and `ACTIONS_STEP_DEBUG` for GitHub Actions.

**4. Flaky test that passes in isolation but fails in the suite**

One test fails when run with the full suite but passes alone -- a test polluter is contaminating shared state. Run `./scripts/find-polluter.sh '.git' 'src/**/*.test.ts'` to execute tests one-by-one and stop at the first test that leaves dirty state. The script identifies which test creates the contamination so you can fix the cleanup.

**5. Bug fixed but you need to prevent it from recurring**

After finding and fixing the root cause, apply defense-in-depth validation at every layer the data passes through: (1) Entry point validation -- reject invalid input at the API boundary, (2) Business logic validation -- ensure data makes sense for the operation, (3) Environment guards -- prevent dangerous operations in specific contexts, (4) Debug instrumentation -- capture context for forensics. Single validation fixes the bug; all four layers make the bug impossible.

## How to Use

**Direct invocation:**

```
Use the debugging skill to investigate why this test fails intermittently
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `debugging`
- `devtools`
- `profiling`
- `root-cause-analysis`

## When to Use / When NOT to Use

**Use when:**
- Any test failure (unit, integration, E2E)
- Bugs in production or development
- Browser/UI issues requiring DevTools inspection
- CI/CD pipeline failures or intermittent issues
- Performance problems requiring profiling
- You have already tried multiple fixes (especially then)

**Do NOT use when:**
- Writing new tests or setting up test frameworks -- use [testing-framework](../testing-framework/) instead
- TDD methodology or writing tests before code -- use [test-driven-development](../test-driven-development/) instead
- Reviewing code quality or PRs -- use [code-review](../code-review/) instead

## Related Plugins

- **[Testing Framework](../testing-framework/)** -- Test infrastructure setup, framework selection, and test suite authoring across multiple languages
- **[CI/CD Pipelines](../cicd-pipelines/)** -- Pipeline design, DevOps automation, infrastructure as code, and container orchestration
- **[Frontend Design](../frontend-design/)** -- UI design systems, component libraries, CSS/Tailwind styling, and accessibility
- **[MCP Server](../mcp-server/)** -- MCP server development with Python and TypeScript SDKs
- **[Next.js Development](../nextjs-development/)** -- Next.js App Router, Server Components, Server Actions, and caching strategies

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
