# Testing Framework

> **v1.1.24** | Quality & Testing | 26 iterations

> Multi-language test infrastructure setup, framework selection, and test suite authoring -- covering unit testing (Rust, TypeScript, PHP, Shell), E2E testing (Playwright), component testing (React Testing Library), accessibility testing (axe-core), mutation testing, fuzz testing, and CI/CD integration.
> Single skill + 30 references + 11 scripts + 20+ templates + examples + assets

## Context to Provide

The skill routes you to the right testing module based on your language, platform, and specific testing need. The more precisely you describe your stack and constraints, the less back-and-forth is needed before configuration begins.

**What information to include in your prompt:**

- **Language and framework** -- "Rust CLI," "Next.js 15 with TypeScript," "TYPO3 extension in PHP 8.2," "Bash deployment scripts." This is the primary routing signal.
- **Test types needed** -- unit, integration, E2E, component, accessibility, mutation, or fuzz. Listing multiple types helps the skill configure them in the right order.
- **Current state** -- "no tests at all," "we have unit tests but no E2E," "migrating from Jest to Vitest." Starting point determines what gets set up vs what gets extended.
- **CI/CD platform** -- GitHub Actions, GitLab CI, or none. Templates exist for both; without this the CI step is skipped.
- **Specific constraints** -- "tests must run under 2 minutes," "must support PHP 8.1 and 8.2," "we use monorepo with Turbo." These determine configuration choices.
- **For specialized testing**: describe what triggered the need -- "88% coverage but a real bug shipped" (mutation testing), "our app has a UI" (accessibility testing), "we process untrusted user input" (fuzz testing).

**What makes results better vs worse:**

- Better: specify the exact framework version (Next.js 15, Vitest 2.x, PHP 8.2) -- configuration differs between versions
- Better: describe what you want to test, not just that you want tests ("repository layer with database," "React components with async state")
- Better: include your current test run time if you are asking for CI optimization
- Worse: asking to "add tests" without specifying the language -- the routing cannot work without this
- Worse: mentioning coverage percentages without specifying what should actually be tested
- Worse: asking for both TDD methodology and test infrastructure setup in one prompt -- use test-driven-development for the cycle, this plugin for the framework setup

**Template prompt:**

```
Set up testing for my [language/framework] project. Stack details:
- Language/framework: [e.g., Next.js 15 with TypeScript, Rust, PHP 8.2/TYPO3, Bash]
- Test types needed: [unit / integration / E2E / component / accessibility / mutation / fuzz]
- Current state: [no tests / some unit tests / migrating from X]
- CI platform: [GitHub Actions / GitLab CI / none]
- Constraints: [run time target, version compatibility, monorepo structure, etc.]
```

## The Problem

Setting up testing infrastructure is one of those tasks that takes half a day and nobody documents. You need to pick the right framework (Vitest vs. Jest for TypeScript? ShellSpec vs. BATS for shell scripts?), configure it for your project structure, set up CI/CD integration, add coverage reporting, and make sure the whole thing runs fast enough that developers actually use it. Get any of these decisions wrong and you either have slow tests nobody runs, flaky tests nobody trusts, or no tests at all.

The problem multiplies in polyglot projects. A team with a Rust backend, a Next.js frontend, and shell scripts for deployment needs three different testing setups, each with its own configuration, naming conventions, and CI integration patterns. The Rust developer writes excellent unit tests but has no idea how to set up Playwright for the frontend. The frontend developer uses React Testing Library but has never configured PHPUnit. The DevOps engineer writes shell scripts with no tests at all because "who tests bash scripts?"

Beyond setup, teams struggle with testing concerns that cross language boundaries: accessibility testing (how to integrate axe-core with component tests and E2E tests), mutation testing (how to verify your tests actually catch bugs, not just cover lines), fuzz testing (how to find edge cases you did not think of), and CI/CD integration (how to make tests run fast in parallel with proper artifact collection). Each of these is a specialized skill that requires different tools and patterns, and most teams learn them through painful trial and error.

## The Solution

This plugin provides a complete testing infrastructure toolkit covering six testing modules: Rust unit testing with cargo test and tokio, E2E testing with Playwright including visual analysis and screenshot capture, Next.js testing with Vitest, React Testing Library, and Playwright, TYPO3/PHP testing with PHPUnit, shell script testing with ShellSpec and BATS, and skill validation testing. It includes specialized coverage for accessibility testing (axe-core), mutation testing, fuzz testing, and CI/CD integration.

The skill operates as a decision matrix: describe what you need to test and in what language, and it routes you to the right framework, configuration, and patterns. Thirty reference files provide deep guidance on every testing topic from the AAA pattern and naming conventions through async testing and CI/CD integration. Eleven utility scripts handle infrastructure setup, test generation, quality analysis, and validation. Templates for Rust, E2E/Playwright, TYPO3/PHP, and Next.js provide ready-to-use configurations and test file starters.

The core philosophy is "deployment confidence, not coverage theater." Tests should catch real bugs, not boost metrics. Every recommendation is grounded in that principle -- from which assertions to use (specific over generic) to how to organize tests (by feature, not by type) to what to mock (external dependencies) and what not to mock (pure functions).

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Half a day setting up test infrastructure by trial and error | Decision matrix routes to the right framework, provides config templates, and generates test starters in minutes |
| Shell scripts with zero tests -- "who tests bash?" | ShellSpec (BDD-style) and BATS (TAP-compliant) with setup scripts, templates, and CI integration |
| Accessibility testing is a manual audit done once before launch | axe-core integrated into component tests and E2E tests, running automatically on every PR |
| 90% line coverage but tests do not catch real bugs | Mutation testing verifies test quality by checking whether tests fail when code is deliberately broken |
| Flaky E2E tests that fail randomly in CI | Playwright best practices: proper waits, retry strategies, artifact collection, and screenshot comparison |
| CI/CD test integration configured differently across projects | Reusable GitHub Actions and GitLab CI templates with parallel execution, coverage reporting, and artifact management |

## Installation

Add the SkillStack marketplace, then install this plugin:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install testing-framework@skillstack
```

### Verify installation

After installing, test with:

```
Set up a complete testing stack for my Next.js project -- I need unit tests, component tests, and E2E tests
```

The skill should activate and provide a configured Vitest + React Testing Library + Playwright setup with example tests and CI/CD integration.

## Quick Start

1. **Install** the plugin using the commands above
2. **Describe your testing need**: `I need to set up Playwright E2E tests for my React application`
3. The skill **configures the framework**: Playwright config, page object templates, global setup/teardown, and a first test spec
4. **Write your first test** with guidance: the skill shows the Playwright pattern for your specific page and walks through assertions
5. **Add CI integration**: the skill provides a GitHub Actions workflow that runs Playwright tests in parallel with screenshot artifact collection

---

## System Overview

```
User needs testing infrastructure / framework / test authoring
    │
    ▼
┌───────────────────────────────────────────────────────────┐
│              testing-framework (skill)                       │
│                                                             │
│  Decision Matrix:                                           │
│  ├── Rust? ──────── cargo test + tokio                     │
│  ├── Next.js/React? ─ Vitest + RTL + Playwright            │
│  ├── PHP/TYPO3? ──── PHPUnit + Playwright                  │
│  ├── Shell/Bash? ──── ShellSpec or BATS                    │
│  ├── E2E? ──────── Playwright (any frontend)               │
│  └── Skill testing? ─ JSON test suites                     │
│                                                             │
│  Cross-cutting concerns:                                    │
│  ├── Accessibility ── axe-core integration                  │
│  ├── Mutation ────── test quality verification              │
│  ├── Fuzz ────────── security edge case discovery           │
│  └── CI/CD ──────── GitHub Actions + GitLab CI              │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐    │
│  │           30 Reference Files (on-demand)              │    │
│  │                                                       │    │
│  │  Core: AAA pattern, naming, builders, anti-patterns   │    │
│  │  Frameworks: unit, functional, async, E2E, JS         │    │
│  │  Specialized: a11y, mutation, fuzz                    │    │
│  │  CI/CD: GitHub Actions, GitLab, SonarCloud            │    │
│  │  Shell: BATS gotchas, assertions, advanced            │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────┐  │
│  │  11 Scripts   │  │  Templates   │  │  Examples/Assets │  │
│  │  setup, gen-  │  │  Rust, E2E,  │  │  React Vite E2E, │  │
│  │  erate, anal- │  │  TYPO3/PHP,  │  │  Next.js tests,  │  │
│  │  yze, valid-  │  │  Next.js,    │  │  reports, configs │  │
│  │  ate, diag-   │  │  configs,    │  │  checklists,     │  │
│  │  nose, init   │  │  workflows   │  │  E2E phases      │  │
│  └──────────────┘  └──────────────┘  └──────────────────┘  │
└───────────────────────────────────────────────────────────┘
```

## What's Inside

| Component | Type | Purpose |
|---|---|---|
| `testing-framework` | skill | Decision matrix routing to six testing modules, universal best practices, troubleshooting |
| 6 core pattern references | reference | AAA pattern, naming conventions, test builders, anti-patterns, writing tests, test patterns |
| 6 framework references | reference | Unit testing (PHP), functional testing, async testing, E2E, JavaScript, functional patterns |
| 4 specialized testing refs | reference | Accessibility (2 files), fuzz testing, mutation testing |
| 6 CI/CD references | reference | GitHub Actions, GitLab CI, integration patterns, test runners, quality tools, SonarCloud |
| 5+ shell testing references | reference | BATS gotchas, assertions, advanced patterns, troubleshooting, real-world examples |
| 11 utility scripts | script | Infrastructure setup, test generation, quality analysis, validation, diagnostics |
| Rust templates | template | Unit test, async test, test builder patterns |
| E2E/Playwright templates | template | Config, test spec, page object, setup/teardown, screenshot helper, CSS configs |
| TYPO3/PHP templates | template | PHPUnit configs, bootstrap, CI workflow, Playwright setup, example tests |
| Next.js assets | asset | Vitest config, Playwright config, test setup |
| E2E workflow phases | asset | 8-phase E2E workflow documentation |
| Examples | example | React Vite E2E, Next.js unit/component/E2E, analysis reports |

**Eval coverage:** 13 trigger evaluation cases, 3 output evaluation cases.

### Component Spotlights

#### testing-framework (skill)

**What it does:** Activates when you need to set up testing infrastructure, choose a test framework, write tests, configure test automation, or integrate tests into CI/CD. Routes you to the right framework and patterns based on your language, platform, and testing needs. Covers unit, integration, E2E, component, accessibility, mutation, and fuzz testing across Rust, TypeScript, PHP, and Shell.

**Input -> Output:** A testing need (language, platform, testing type) -> Framework configuration, test templates, example tests, and CI/CD integration matching your specific stack.

**When to use:** Setting up test infrastructure from scratch. Choosing between frameworks (Vitest vs Jest, ShellSpec vs BATS). Writing tests for a specific platform. Adding accessibility, mutation, or fuzz testing. Configuring CI/CD test pipelines. Optimizing slow test suites.

**When NOT to use:** TDD methodology and red-green-refactor workflow (use test-driven-development). Diagnosing and fixing bugs (use debugging). Reviewing existing code or PRs (use code-review).

**Try these prompts:**

```
Set up a complete testing stack for my Next.js 15 project with TypeScript. I need:
- Vitest for unit tests (we use path aliases like @/components)
- React Testing Library for component tests with a custom render utility
- Playwright for E2E tests (desktop and mobile viewports)
- axe-core integrated into both component and E2E tests
- GitHub Actions CI with parallel shards
```

```
I need to test my Bash deployment scripts. They: parse YAML config files, validate environment variables,
call AWS CLI to deploy ECS services, and send Slack notifications. We have 500 lines across 3 scripts with
no tests. One quoting bug caused a failed deploy last month. Should I use ShellSpec or BATS?
```

```
Add accessibility testing to my React components using axe-core. Current setup: Vitest + React Testing
Library. I want axe violations to fail tests automatically on every PR. Start with our most complex
component (a multi-step form wizard).
```

```
Our GitHub Actions test suite takes 22 minutes -- unit tests (3min), integration tests (8min), and
Playwright E2E (11min). Developers skip running E2E locally. Configure parallel execution across 4 shards
with screenshot artifacts on failure and JUnit XML for the CI dashboard.
```

```
My TYPO3 extension tests have 88% line coverage but a bug shipped last week that none of them caught.
The tests assert mock call arguments instead of actual return values. How do I set up mutation testing
to verify the tests would actually catch real bugs?
```

```
Write Rust unit tests for this async HTTP client function using tokio. The function makes a request
and returns a Result<Response, ClientError>. I need tests for: successful response, 404 not found,
network timeout, and invalid JSON in response body. Use the AAA pattern with descriptive names.
[paste function signature]
```

**Key scripts:**

| Script | Purpose |
|---|---|
| `analyze-test-quality.py` | Analyze test file quality and patterns |
| `setup-testing.sh` | Set up TYPO3 testing infrastructure |
| `generate-test.sh` | Generate test class templates (unit, functional, E2E) |
| `validate-setup.sh` | Validate testing infrastructure configuration |
| `run_tests.py` | Run skill test suites |
| `generate_test_template.py` | Generate test templates from definitions |
| `init_bats_project.sh` | Initialize BATS project structure |
| `generate_test_deps.py` | Generate Next.js test dependencies |

---

## Prompt Patterns

### Good Prompts vs Bad Prompts

| Bad (vague, gets generic advice) | Good (specific, gets configured infrastructure) |
|---|---|
| "Help me with testing" | "Set up Vitest + React Testing Library + Playwright for my Next.js 15 project with TypeScript path aliases" |
| "Write some tests" | "Write Rust unit tests for this async HTTP client using tokio, following the AAA pattern with proper error case coverage" |
| "My tests are broken" | "My Playwright E2E tests pass locally but fail in GitHub Actions -- the page loads but elements are not found" |
| "Add test coverage" | "My TYPO3 extension has unit tests but no functional tests for the database layer -- set up PHPUnit functional tests with fixtures" |
| "Test my scripts" | "I need to test these Bash deployment scripts that parse YAML config and call AWS CLI -- recommend ShellSpec or BATS and set it up" |

### Structured Prompt Templates

**For setting up testing from scratch:**
```
Set up testing for my [language/framework] project. I need:
- [test types: unit / integration / E2E / component / accessibility]
- Framework: [specific or "recommend one"]
- CI: [GitHub Actions / GitLab CI / none yet]
- Current state: [no tests / some tests / migrating from X]
```

**For adding specialized testing:**
```
I want to add [accessibility / mutation / fuzz] testing to my [project type].
Current test setup: [describe what exists]. Framework: [what you use].
Goal: [catch accessibility violations on every PR / verify test quality / find edge cases].
```

**For CI/CD test integration:**
```
Configure [CI platform] to run my [test types] in parallel.
Current run time: [N minutes]. Target: [M minutes].
I need: [artifact collection / coverage reporting / quality gates / screenshot on failure].
```

**For framework selection:**
```
I need to test [what: shell scripts / React components / Rust async code / PHP services].
My constraints: [CI integration needed / must be fast / team knows X but not Y].
Recommend a framework and set it up.
```

### Prompt Anti-Patterns

- **Asking for tests without specifying the language and framework:** "Write tests for this function" could mean pytest, Vitest, PHPUnit, cargo test, or ERT. The skill needs to know which ecosystem to use for proper configuration and conventions.
- **Requesting "full coverage" without specifying what to test:** Coverage numbers without strategy produce coverage theater. Instead, specify which behaviors, edge cases, or failure modes you want tested. The skill will help you achieve meaningful coverage, not just high percentages.
- **Asking to set up testing without describing the project:** "Set up testing" for a Next.js app is completely different from a TYPO3 extension or a Rust CLI. Describe your stack, project structure, and what you want to test so the skill routes to the right module.
- **Ignoring the accessibility testing capability:** If your project has a UI, ask about axe-core integration. Most teams add accessibility testing as an afterthought; integrating it from the start with component and E2E tests is far cheaper.

## Real-World Walkthrough

You are building a TYPO3 extension for a large enterprise client. The extension manages product catalogs with CRUD operations, search, and a REST API. It needs unit tests for business logic, functional tests for database operations, E2E tests for the backend module UI, and the entire test suite must run in GitHub Actions. You have never set up testing for a TYPO3 extension before.

You open Claude Code and say:

```
I need to set up a complete testing infrastructure for a TYPO3 extension -- unit tests, functional tests with database, and E2E tests for the backend module. It needs to run in GitHub Actions.
```

The skill routes you to the **TYPO3/PHP testing module** and starts with infrastructure setup:

```bash
scripts/setup-testing.sh --with-e2e
```

This generates: `phpunit.xml` configurations for unit and functional tests, the bootstrap file, Playwright configuration for E2E, and the GitHub Actions workflow. The skill explains each component -- unit tests for pure PHP logic (milliseconds), functional tests with fresh database state per test (seconds), E2E tests automating the TYPO3 backend browser (minutes).

You generate a unit test for the product validator following the AAA pattern with descriptive naming (`validateRejectsEmptyProductName`). The skill generates four test methods: empty name, negative price, valid product, and boundary values. Then functional tests for the repository with database fixtures -- CRUD operations with proper container reset patterns.

For E2E, the skill generates Playwright tests using the page object pattern, including an accessibility test with axe-core. The GitHub Actions workflow runs unit tests across PHP 8.2 and 8.3, functional tests with MySQL, and Playwright E2E with screenshot artifacts on failure.

After setup, `scripts/validate-setup.sh` verifies everything is configured correctly. You have 8 unit tests, 6 functional tests, 4 E2E tests (including accessibility), and a CI pipeline -- set up in about an hour instead of half a day.

## Usage Scenarios

### Scenario 1: Setting up testing for a new Next.js project

**Context:** Starting a Next.js project, want testing from day one.

**You say:** `Set up the complete Next.js testing stack -- Vitest, React Testing Library, Playwright, and accessibility testing with axe-core`

**The skill provides:**
- Vitest config with path aliases and test setup
- React Testing Library with custom render utility
- Playwright config with desktop and mobile viewports
- axe-core integration for component and E2E tests
- Example tests for each type

**You end up with:** A fully configured testing stack with accessibility checking built in.

### Scenario 2: Adding tests to shell scripts

**Context:** 500 lines of untested Bash deployment scripts. A quoting bug caused a deployment failure.

**You say:** `I need to test my deployment shell scripts. They parse config files, validate environments, and call APIs.`

**The skill provides:**
- Framework recommendation (ShellSpec for BDD, BATS for TAP/CI)
- Project initialization with `init_bats_project.sh`
- Test templates for config parsing, environment validation, API mocking
- Common gotchas from `gotchas.md`

**You end up with:** A BATS test suite covering critical deployment paths, running in CI.

### Scenario 3: Verifying test quality with mutation testing

**Context:** 88% coverage but a real bug shipped. Tests may be testing implementation, not behavior.

**You say:** `My tests have high coverage but they didn't catch a real bug. How do I verify the tests actually work?`

**The skill provides:**
- Mutation testing setup -- deliberately break code and check if tests fail
- Analysis of behavior vs. implementation testing
- Anti-pattern identification (testing mock calls instead of results)

**You end up with:** A mutation testing report and revised tests that verify behavior.

### Scenario 4: Optimizing slow CI test pipelines

**Context:** Test suite takes 20 minutes in CI. Developers avoid running it.

**You say:** `Our CI tests take 20 minutes. Help me parallelize them and set up proper artifact collection.`

**The skill provides:**
- GitHub Actions matrix strategy for parallel shards
- Test splitting by execution time
- Artifact config for screenshots, coverage, JUnit XML
- SonarCloud quality gate integration

**You end up with:** A 5-minute CI pipeline with 4 parallel shards and failure artifacts.

---

## Decision Logic

**How does the skill choose which testing module to use?**

Based on language and platform:
- Rust project -> Rust unit testing module (cargo test, tokio for async)
- Next.js / React -> Next.js module (Vitest + RTL + Playwright)
- PHP / TYPO3 -> TYPO3/PHP module (PHPUnit + Playwright)
- Bash / Shell scripts -> Shell testing module (ShellSpec or BATS)
- Browser-based user workflows -> E2E module (Playwright) regardless of backend language
- Claude Code skill testing -> Skill testing module (JSON test suites)

**How does the skill choose between ShellSpec and BATS?**

- **ShellSpec**: BDD-style syntax, better for complex scripts with many scenarios, built-in mocking, parallel execution. Choose when readability matters and scripts are complex.
- **BATS**: TAP-compliant output, simpler syntax, wider CI integration, more community plugins. Choose when CI integration is the priority and scripts are straightforward.

**When does the skill recommend mutation testing?**

When the user reports high coverage but low confidence ("my tests pass but bugs still ship"), or when they explicitly ask about test quality verification. Mutation testing is not recommended for every project -- it is most valuable when coverage numbers are high but bug rates remain concerning.

**How are testing tiers assigned?**

- **Unit tests**: isolated logic with mocked dependencies. Run on every commit.
- **Functional/Integration tests**: component interactions, database operations. Run on PRs.
- **E2E tests**: complete user workflows through the browser. Run before deployment.
- **Accessibility tests**: integrated into both component tests (fast, per-commit) and E2E tests (comprehensive, pre-deployment).

## Failure Modes & Edge Cases

| Failure | Symptom | Recovery |
|---|---|---|
| Framework mismatch for the project | Vitest configured but the project uses CommonJS modules, or Jest configured for a Vite project | Describe your bundler and module system when asking for setup. Vitest for Vite-based projects, Jest for webpack/CRA. The skill checks for configuration conflicts. |
| E2E tests flaky in CI but pass locally | Elements not found, timeouts, screenshot mismatches that only appear in headless mode | Check viewport size (CI headless may differ), add explicit waits for dynamic content, use Playwright's `--trace on` to capture failure context. The skill references `playwright-best-practices.md`. |
| Mutation testing produces too many survivors | High mutation survival rate makes the report overwhelming and actionable items unclear | Focus on critical business logic modules first, not utility code. Set a mutation threshold for important modules only. The skill recommends incremental adoption. |
| Shell test mocking fails for complex scripts | Scripts that source other files or use complex subshell patterns break ShellSpec's mocking | Use BATS `bats-mock` plugin for simpler mocking, or restructure scripts into testable functions. The skill references `advanced-patterns.md` and `gotchas.md`. |
| CI pipeline slower after adding tests | Test suite grows and CI time regresses from the optimized state | Revisit parallelization: shard by test file, split slow E2E tests from fast unit tests, cache dependencies. The skill provides CI optimization patterns from `ci-cd.md`. |

## Ideal For

- **Teams setting up testing infrastructure from scratch** -- the decision matrix and configuration templates eliminate trial-and-error framework selection
- **Polyglot projects needing consistent testing across languages** -- unified methodology (AAA pattern, naming conventions, CI integration) across Rust, TypeScript, PHP, and Shell
- **Teams adding specialized testing** -- accessibility (axe-core), mutation, and fuzz testing setup with integration into existing test suites
- **DevOps engineers who need to test shell scripts** -- ShellSpec and BATS setup with templates, gotchas, and CI integration

## Not For

- **TDD methodology and red-green-refactor workflow** -- use [test-driven-development](../test-driven-development/) for the test-first methodology; this plugin provides the frameworks that TDD uses
- **Diagnosing and fixing bugs** -- use [debugging](../debugging/) for root cause analysis; this plugin helps write tests that prevent bugs
- **Reviewing existing code or PRs** -- use [code-review](../code-review/) for structured reviews; this plugin focuses on test authoring and infrastructure

## Related Plugins

- **[Test-Driven Development](../test-driven-development/)** -- The Red-Green-Refactor methodology that uses these frameworks (complementary)
- **[Python Development](../python-development/)** -- Python-specific testing with pytest, fixtures, and parametrization
- **[React Development](../react-development/)** -- React component testing patterns with hooks and architecture
- **[CI/CD Pipelines](../cicd-pipelines/)** -- Pipeline configuration beyond testing -- deployment, infrastructure, and release automation
- **[Code Review](../code-review/)** -- Review test quality and coverage as part of PR reviews

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
