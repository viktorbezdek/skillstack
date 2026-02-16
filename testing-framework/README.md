# Testing Framework

> Comprehensive multi-language testing framework covering unit, E2E, component, accessibility, mutation, and fuzz testing across Rust, TypeScript, PHP, Shell, and React.

## Overview

Setting up robust testing infrastructure across different languages and platforms is time-consuming and error-prone. This skill provides a complete testing toolkit that spans unit testing in Rust, TypeScript, PHP, and Shell, end-to-end testing with Playwright, component testing with React Testing Library, and specialized techniques like accessibility auditing, mutation testing, and fuzz testing.

The skill is designed for teams working with polyglot codebases or anyone who needs to establish testing best practices quickly. It includes ready-to-use configuration templates, test generators, quality analysis scripts, and CI/CD integration patterns so you can go from zero tests to a fully automated test suite.

As part of the SkillStack collection, this skill complements the test-driven-development skill (which focuses on the TDD methodology) and integrates with the workflow-automation skill for CI/CD pipeline setup.

## What's Included

### References

**Core Testing Patterns**
- `references/aaa-pattern.md` - Arrange-Act-Assert pattern details and examples
- `references/naming-conventions.md` - Test naming best practices across languages
- `references/test-builders.md` - Test builder patterns for complex object construction
- `references/anti-patterns.md` - Common testing anti-patterns to avoid
- `references/writing_tests.md` - Best practices for writing effective tests
- `references/test_patterns.md` - Test pattern examples for different skill types

**Framework-Specific**
- `references/unit-testing.md` - PHP/TYPO3 unit testing guide
- `references/functional-testing.md` - Functional testing with database interactions
- `references/functional-test-patterns.md` - Container reset patterns, PHPUnit migration
- `references/async-testing.md` - Async test patterns for concurrent code
- `references/e2e-testing.md` - End-to-end testing guide
- `references/javascript-testing.md` - JavaScript/TypeScript testing patterns

**Specialized Testing**
- `references/fuzz-testing.md` - Security fuzz testing for input validation
- `references/mutation-testing.md` - Test quality verification through code mutation
- `references/accessibility-testing.md` - axe-core WCAG compliance testing
- `references/a11y-testing.md` - Accessibility testing guidelines and integration

**CI/CD and Tools**
- `references/ci-cd.md` - GitHub Actions and GitLab CI test workflows
- `references/ci-integration.md` - CI/CD integration patterns
- `references/ci-cd-integration.md` - E2E CI/CD examples
- `references/test-runners.md` - Test orchestration and runner patterns
- `references/quality-tools.md` - PHPStan, Rector, php-cs-fixer integration
- `references/sonarcloud.md` - SonarCloud quality gate integration

**Shell Testing**
- `references/gotchas.md` - BATS common pitfalls and workarounds
- `references/assertions.md` - BATS assertion reference
- `references/advanced-patterns.md` - ShellSpec advanced testing patterns
- `references/troubleshooting.md` - Debugging test failures
- `references/collected-experience.md` - Lessons learned from real testing projects
- `references/real-world-examples.md` - Production shell testing patterns
- `references/projects.md` - Real-world project examples
- `references/experience-feedback.md` - Community testing experience and feedback

### Templates

**Rust**
- `templates/rust/unit-test.md` - Basic Rust unit test template with AAA pattern
- `templates/rust/async-test.md` - Async test template with tokio runtime
- `templates/rust/test-builder.md` - Test builder pattern for complex test data

**E2E / Playwright**
- `templates/e2e/playwright.config.template.ts` - Playwright configuration template
- `templates/e2e/test-spec.template.ts` - Test spec template with best practices
- `templates/e2e/page-object.template.ts` - Page Object Model template
- `templates/e2e/global-setup.template.ts` - Global setup for authentication/state
- `templates/e2e/global-teardown.template.ts` - Global teardown for cleanup
- `templates/e2e/screenshot-helper.template.ts` - Screenshot capture utilities
- `templates/e2e/configs/postcss-tailwind-v3.js` - PostCSS config for Tailwind v3
- `templates/e2e/configs/postcss-tailwind-v4.js` - PostCSS config for Tailwind v4
- `templates/e2e/css/tailwind-v3.css` - Tailwind v3 CSS template
- `templates/e2e/css/tailwind-v4.css` - Tailwind v4 CSS template
- `templates/e2e/css/vanilla.css` - Vanilla CSS template

**TYPO3 / PHP**
- `templates/typo3/UnitTests.xml` - PHPUnit unit test configuration
- `templates/typo3/FunctionalTests.xml` - PHPUnit functional test configuration
- `templates/typo3/FunctionalTestsBootstrap.php` - Functional test bootstrap file
- `templates/typo3/github-actions-tests.yml` - GitHub Actions CI workflow
- `templates/typo3/Build/playwright/` - Complete Playwright E2E setup for TYPO3
- `templates/typo3/docker/` - Docker Compose setup for testing environments
- `templates/typo3/example-tests/` - Example unit, functional, and acceptance tests

### Scripts

- `scripts/analyze-test-quality.py` - Analyze Rust test file quality and coverage
- `scripts/setup-testing.sh` - Set up TYPO3 testing infrastructure from scratch
- `scripts/generate-test.sh` - Generate test class templates by type (unit/functional/e2e)
- `scripts/validate-setup.sh` - Validate that testing setup is correctly configured
- `scripts/run_tests.py` - Run skill test suites with JSON input/output validation
- `scripts/generate_test_template.py` - Generate test templates from skill definitions
- `scripts/validate_test_results.py` - Validate actual vs expected test outputs
- `scripts/diagnose_test.sh` - Diagnose ShellSpec test failures
- `scripts/init_bats_project.sh` - Initialize a new BATS testing project
- `scripts/strip_colors.sh` - Strip ANSI color codes from test output
- `scripts/generate_test_deps.py` - Generate Next.js test dependency configuration

### Examples

**E2E**
- `examples/e2e/react-vite/example-test.spec.ts` - Playwright test for a React Vite app
- `examples/e2e/react-vite/example-page-object.ts` - Page Object Model example
- `examples/e2e/reports/visual-analysis-report.example.md` - Visual regression analysis report
- `examples/e2e/reports/fix-recommendations.example.md` - Fix recommendation report

**Next.js**
- `examples/nextjs/unit-test.ts` - Vitest unit test example
- `examples/nextjs/component-test.tsx` - React Testing Library component test
- `examples/nextjs/e2e-test.ts` - Playwright E2E test for Next.js

### Assets

**Next.js Configuration**
- `assets/nextjs/vitest.config.ts` - Vitest configuration for Next.js
- `assets/nextjs/playwright.config.ts` - Playwright configuration for Next.js
- `assets/nextjs/test-setup.ts` - Test environment setup file

**E2E Workflow Phases**
- `assets/e2e-workflow/phase-1-discovery.md` - Application discovery phase
- `assets/e2e-workflow/phase-2-setup.md` - Playwright setup phase
- `assets/e2e-workflow/phase-2.5-preflight.md` - Pre-flight health check
- `assets/e2e-workflow/phase-3-generation.md` - Test generation phase
- `assets/e2e-workflow/phase-4-capture.md` - Screenshot capture phase
- `assets/e2e-workflow/phase-5-analysis.md` - Visual analysis phase
- `assets/e2e-workflow/phase-6-regression.md` - Regression detection phase
- `assets/e2e-workflow/phase-7-fixes.md` - Fix generation phase
- `assets/e2e-workflow/phase-8-export.md` - Test suite export phase

**E2E Data**
- `assets/e2e-data/playwright-best-practices.md` - Curated Playwright best practices
- `assets/e2e-data/accessibility-checks.md` - Accessibility check definitions
- `assets/e2e-data/common-ui-bugs.md` - Common UI bug patterns for visual testing

**Shell Testing**
- `assets/shellspec/spec_template.sh` - ShellSpec BDD test template

**Skill Testing**
- `assets/skill-testing/test_template.json` - JSON test suite template for skill validation

**Rust Checklists**
- `assets/rust-checklists/pre-commit.md` - Pre-commit testing checklist
- `assets/rust-checklists/review.md` - Code review testing checklist

## Key Features

- **Multi-language unit testing** for Rust (cargo test, tokio), TypeScript (Vitest), PHP (PHPUnit), and Shell (ShellSpec, BATS)
- **End-to-end testing** with Playwright including visual analysis, screenshot capture, and LLM-powered debugging
- **Component testing** with React Testing Library and Vitest for Next.js applications
- **Accessibility testing** with axe-core for WCAG compliance auditing
- **Mutation testing** to verify test suite quality by introducing controlled code mutations
- **Fuzz testing** for security-critical input validation
- **CI/CD integration** with ready-to-use GitHub Actions and GitLab CI workflow templates
- **Test quality analysis** with automated scoring and improvement recommendations

## Usage Examples

### Set up testing for a new Rust project

```
Set up a comprehensive test suite for my Rust API project with unit tests, async tests, and CI integration.
```

Generates test files using the AAA pattern, configures tokio for async tests, and provides a GitHub Actions workflow with quality gates.

### Create Playwright E2E tests for a React app

```
Create E2E tests for my React Vite app covering the login flow, dashboard navigation, and data export features.
```

Produces Playwright test specs with Page Object Models, proper accessibility selectors, screenshot capture, and a CI-ready configuration.

### Add accessibility testing to a Next.js project

```
Add accessibility testing to my Next.js app. I want both component-level axe-core checks and E2E accessibility audits.
```

Sets up axe-core integration with React Testing Library for component tests and Playwright for full-page accessibility scans, targeting WCAG 2.1 AA.

### Analyze test quality in a PHP/TYPO3 project

```
Analyze the test quality of my TYPO3 extension and suggest improvements. The tests are in Tests/Unit/ and Tests/Functional/.
```

Runs quality analysis covering naming conventions, assertion quality, test isolation, and coverage gaps, then recommends specific improvements.

### Set up shell script testing with BATS

```
Set up BATS testing for my deployment scripts in scripts/. Include tests for the main deploy.sh and rollback.sh scripts.
```

Initializes a BATS project structure, creates test files with common assertions, and configures CI integration.

## Quick Start

1. **Identify your stack** - Use the Quick Decision Matrix in SKILL.md to find the right testing approach for your language and framework.
2. **Copy the template** - Grab the relevant template from `templates/` (Rust, E2E, or TYPO3) as your starting point.
3. **Configure the framework** - Use asset files from `assets/` for framework-specific configuration (Vitest, Playwright, etc.).
4. **Generate tests** - Run the appropriate script (`scripts/generate-test.sh` for PHP, `scripts/generate_test_template.py` for skills) to scaffold your test files.
5. **Write your first test** - Follow the AAA pattern from `references/aaa-pattern.md` and naming conventions from `references/naming-conventions.md`.
6. **Run and validate** - Execute tests and use `scripts/analyze-test-quality.py` to get a quality score and improvement suggestions.
7. **Integrate with CI** - Add the appropriate CI workflow from `templates/` to your repository.

## Related Skills

- [test-driven-development](../test-driven-development/) - TDD methodology with Red-Green-Refactor workflow
- [typescript-development](../typescript-development/) - TypeScript patterns for type-safe test utilities
- [react-development](../react-development/) - React component patterns that complement component testing
- [workflow-automation](../workflow-automation/) - CI/CD pipeline setup and test automation integration
- [frontend-design](../frontend-design/) - Frontend design patterns with testability in mind

---

Part of [SkillStack](https://github.com/viktorbezdek/claude-skills) — `/plugin install testing-framework@claude-skills` — 34 production-grade skills for Claude Code.
