# Test-Driven Development

> Comprehensive TDD skill implementing Red-Green-Refactor across Python, TypeScript, JavaScript, and Emacs Lisp with pytest, Vitest, Playwright, ERT, and Zod.

## Overview

Test-Driven Development (TDD) is the practice of writing tests before implementation code, following the Red-Green-Refactor cycle. This skill provides a unified, multi-language approach to TDD that covers unit tests, integration tests, and end-to-end tests across modern frameworks.

Whether you are building Python backends with pytest, TypeScript frontends with Vitest, browser automation with Playwright, or Emacs packages with ERT, this skill gives you the patterns, templates, and scripts to maintain a disciplined TDD workflow. It enforces the Arrange-Act-Assert structure, meaningful test naming, and coverage validation at every tier.

This skill is part of the SkillStack collection and works alongside the testing-framework skill (which focuses on multi-language test infrastructure) and the workflow-automation skill (which integrates TDD into CI/CD pipelines).

## What's Included

### References

- `references/extended-patterns.md` - Detailed code examples and language-specific guidance for Python/pytest, TypeScript/Vitest, Playwright E2E, and Emacs Lisp/ERT
- `references/general-tdd.md` - Core TDD principles and methodology
- `references/python-tdd.md` - Python-specific TDD practices with pytest
- `references/elisp-tdd.md` - Emacs Lisp TDD with the ERT framework
- `references/vitest-patterns.md` - Vitest testing patterns for TypeScript/JavaScript
- `references/playwright-e2e-patterns.md` - Playwright end-to-end testing patterns
- `references/playwright-best-practices.md` - E2E testing guidelines and best practices
- `references/zod-testing-patterns.md` - Schema validation testing with Zod
- `references/test-design-patterns.md` - Common test design patterns (builder, factory, fixture)
- `references/test-structure-guide.md` - Test organization and file structure conventions
- `references/refactoring-with-tests.md` - Safe refactoring practices backed by tests
- `references/coverage-validation.md` - Coverage analysis and validation guide

### Templates

- `templates/python_test_template.py.template` - Boilerplate pytest test file with fixtures and AAA structure
- `templates/elisp_test_template.el` - ERT test template for Emacs Lisp packages
- `templates/test_checklist.md` - Coverage checklist template for verifying test completeness
- `templates/tdd_session_log.md` - Session logging template for tracking Red-Green-Refactor cycles

### Scripts

- `scripts/run_tests.py` - Multi-framework test runner utility
- `scripts/coverage_analyzer.py` - Coverage analysis tool with reporting
- `scripts/coverage_check.py` - Coverage threshold checker for CI gates
- `scripts/test_template_generator.py` - Generate test boilerplate from function signatures
- `scripts/skill_validator.py` - Validate test implementations against skill requirements
- `scripts/with_server.py` - Helper to run tests with a live server process

## Key Features

- **Red-Green-Refactor cycle** enforced through structured workflow phases and session logging
- **Multi-language support** for Python (pytest), TypeScript/JavaScript (Vitest), Emacs Lisp (ERT), and Playwright E2E
- **Three-tier testing model** covering unit, integration, and end-to-end tests with clear guidance on when to use each
- **Arrange-Act-Assert pattern** consistently applied across all languages and frameworks
- **Coverage validation** with configurable thresholds (80-90% unit, critical paths integration, main workflows E2E)
- **Test naming conventions** that describe expected behavior rather than implementation details
- **Refactoring safety net** with patterns for safely improving code while tests remain green
- **Schema validation testing** with Zod patterns for runtime type safety

## Usage Examples

### Start a TDD session for a new Python feature

```
Write a user authentication function using TDD. Start with the failing test for valid credentials, then implement, then refactor.
```

Produces a pytest test file with Arrange-Act-Assert structure, followed by minimal implementation code, then a refactored version with proper error handling.

### Generate test templates for an existing module

```
Generate pytest test templates for all public functions in src/services/payment.py
```

Creates a test file with test stubs covering happy path, edge cases, and error conditions for each function.

### Add E2E tests with Playwright

```
Write Playwright E2E tests for the checkout flow: add to cart, enter shipping, enter payment, confirm order.
```

Produces a Playwright test spec with page object model, proper selectors, and assertions for each step of the user workflow.

### Check coverage and find gaps

```
Analyze test coverage for the src/auth/ module and identify untested edge cases.
```

Runs coverage analysis and produces a report highlighting uncovered branches, missing error condition tests, and suggested test cases.

### TDD for Zod schema validation

```
Use TDD to build a Zod schema for a user registration form with email, password strength, and age validation.
```

Produces failing tests for each validation rule first, then builds the Zod schema incrementally to make each test pass.

## Quick Start

1. **Define behavior** - Identify the feature or function you want to implement and its expected behavior.
2. **Write a failing test** (RED) - Use the appropriate template from `templates/` to create a test that describes the expected behavior. Run it to confirm it fails.
3. **Write minimal code** (GREEN) - Implement just enough production code to make the test pass. No more.
4. **Refactor** - Clean up both production code and test code while keeping all tests green. Use patterns from `references/refactoring-with-tests.md`.
5. **Repeat** - Pick the next behavior and start a new Red-Green-Refactor cycle.
6. **Validate coverage** - Run `scripts/coverage_check.py` to verify you meet coverage thresholds before committing.

## Related Skills

- [testing-framework](../testing-framework/) - Multi-language test infrastructure including Rust, PHP, shell scripts, accessibility, and mutation testing
- [typescript-development](../typescript-development/) - TypeScript type system patterns and Zod runtime validation
- [python-development](../python-development/) - Python development patterns and best practices
- [workflow-automation](../workflow-automation/) - CI/CD pipelines and TDD workflow integration
- [code-review](../code-review/) - Automated code review with test quality validation

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) — `claude plugin add github:viktorbezdek/skillstack/test-driven-development` — 34 production-grade skills for Claude Code.
