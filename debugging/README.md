# Debugging

> **v1.1.26** | Development | 28 iterations

Comprehensive debugging skill combining systematic debugging methodology, browser DevTools automation, E2E testing with visual analysis, CI/CD pipeline debugging, performance profiling, and AI-powered error analysis.

## What Problem Does This Solve

Debugging failures almost always stem from the same root cause: jumping to fixes before establishing root cause. Engineers under time pressure guess, try multiple changes at once, and introduce new bugs while chasing symptoms. This skill enforces a four-phase iron-law framework (root cause investigation before any fix), and combines it with concrete automation tools for browser DevTools scripting, Playwright E2E visual debugging, CI/CD pipeline analysis, and AI-powered error classification.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "There's a bug — I've tried a few things and nothing is working" | Four-phase systematic debugging framework: root cause investigation, pattern analysis, hypothesis testing, and implementation — each phase must complete before the next |
| "I have a failing test but I can't reproduce it consistently" | Find-polluter script and test isolation methodology for identifying which test contaminates the environment |
| "The app looks broken in the browser — something visual is wrong" | Chrome DevTools automation scripts: navigate, screenshot, click, fill, evaluate, snapshot, console monitoring, network tracking, and Core Web Vitals performance measurement |
| "My E2E tests are failing but I don't know which component is at fault" | Eight-phase Playwright E2E workflow with LLM-powered visual analysis, screenshot capture, regression baseline comparison, and file:line fix recommendations |
| "My CI/CD pipeline is failing intermittently" | CI health check and pipeline analyzer scripts for GitHub Actions and GitLab CI, with a common error pattern table and debug logging configuration |
| "I fixed the bug but how do I prevent it from coming back?" | Defense-in-depth validation pattern: four-layer validation (entry point, business logic, environment guards, debug instrumentation) added after root cause resolution |

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install debugging@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention the triggers below, or you can invoke it explicitly.

## How to Use

**Direct invocation:**

```
Use the debugging skill to ...
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `debugging`
- `devtools`
- `profiling`
- `root-cause-analysis`

## What's Inside

- **Overview** -- Core principle and the iron law: no fixes are permitted before completing root cause investigation.
- **The Iron Law of Debugging** -- Explicit enforcement gate ensuring Phase 1 completion before any fix is proposed.
- **Quick Reference** -- Issue-type decision matrix mapping test failures, browser bugs, CI failures, performance issues, build errors, and flaky tests to their primary tools and reference files.
- **Systematic Debugging Framework** -- Four-phase methodology: root cause investigation (read errors, reproduce, check recent changes, trace data flow), pattern analysis, hypothesis and minimal testing, and single-change implementation.
- **Browser Debugging Tools** -- Nine executable Puppeteer scripts for browser automation with installation instructions and JSON output format.
- **E2E Testing with Visual Debugging** -- Eight-phase Playwright workflow from app discovery through test export, with Playwright config templates and React Vite examples.
- **CI/CD Pipeline Debugging** -- Pipeline health check and analyzer scripts, common error pattern table, debug logging configuration for GitHub Actions and GitLab CI.
- **Finding Test Polluters** -- Shell script that runs tests one-by-one and stops at the first test that contaminates shared state.

## Version History

- `1.1.26` fix(testing+debugging): optimize descriptions with NOT clauses for disambiguation (b00fc60)
- `1.1.25` fix: update plugin count and normalize footer in 31 original plugin READMEs (3ea7c00)
- `1.1.24` fix: change author field from string to object in all plugin.json files (bcfe7a9)
- `1.1.23` fix: rename all claude-skills references to skillstack (19ec8c4)
- `1.1.22` refactor: remove old file locations after plugin restructure (a26a802)
- `1.1.21` docs: update README and install commands to marketplace format (af9e39c)
- `1.1.20` refactor: restructure all 34 skills into proper Claude Code plugin format (7922579)
- `1.1.19` refactor: make each skill an independent plugin with own plugin.json (6de4313)
- `1.1.18` fix: make all shell scripts executable and fix Python syntax errors (61ac964)
- `1.1.17` fix(deps): update all dependencies to latest versions (e72fc10)

## Related Skills

- **[Api Design](../api-design/)** -- Comprehensive API design skill for REST, GraphQL, gRPC, and Python library architectures. Design endpoints, schemas, aut...
- **[Frontend Design](../frontend-design/)** -- Comprehensive Frontend Design (UI/UX) skill combining UI design systems, component libraries, CSS/Tailwind styling, acce...
- **[Gws Cli](../gws-cli/)** -- Google Workspace CLI (gws) skill for managing Drive, Gmail, Sheets, Calendar, Docs, Chat, Tasks, and 11 more Workspace A...
- **[Mcp Server](../mcp-server/)** -- Comprehensive MCP (Model Context Protocol) server development skill. Build, configure, and manage MCP servers using Pyth...
- **[Nextjs Development](../nextjs-development/)** -- Comprehensive Next.js development skill covering App Router (13+/15/16), Server Components, Server Actions, Cache Compon...

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 50 production-grade plugins for Claude Code.
