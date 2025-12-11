---
name: testing-framework
description: Comprehensive testing framework for multiple languages and platforms. Covers unit testing (Rust, TypeScript, PHP, Shell), E2E testing (Playwright), component testing (React Testing Library), accessibility testing (axe-core), mutation testing, fuzz testing, and CI/CD integration. Use when setting up test infrastructure, writing tests, debugging test failures, implementing TDD/BDD, or configuring test automation.
---

# Testing Framework

A comprehensive, multi-language testing skill combining best practices for unit testing, E2E testing, component testing, accessibility testing, and test automation across multiple platforms and frameworks.

## Overview

This skill provides testing guidance and tooling for:

- **Unit Testing**: Rust, TypeScript/JavaScript, PHP, Bash/Shell
- **E2E Testing**: Playwright with visual analysis and screenshot capture
- **Component Testing**: React Testing Library, Vitest
- **Accessibility Testing**: axe-core integration
- **Shell Script Testing**: ShellSpec, BATS frameworks
- **Specialized Testing**: Mutation testing, fuzz testing, skill validation
- **CI/CD Integration**: GitHub Actions, GitLab CI

## When to Use This Skill

**Trigger Phrases**:
- "set up testing for my project"
- "write unit tests for..."
- "help me debug test failures"
- "create E2E tests with Playwright"
- "add accessibility testing"
- "test my shell scripts"
- "set up CI/CD test automation"

**Use Cases**:
- Setting up test infrastructure from scratch
- Writing new tests (unit, integration, E2E)
- Debugging failing tests
- Improving test quality and coverage
- Implementing TDD/BDD workflows
- Adding accessibility testing requirements
- Configuring CI/CD pipelines with test automation

## Quick Decision Matrix

| Need | Technology | Reference |
|------|------------|-----------|
| Rust unit tests | cargo test, tokio | `references/unit-testing.md`, `templates/rust/` |
| Next.js/React testing | Vitest, RTL, Playwright | `assets/nextjs/`, `references/a11y-testing.md` |
| PHP/TYPO3 testing | PHPUnit, Playwright | `templates/typo3/`, `references/functional-testing.md` |
| Bash/Shell testing | ShellSpec, BATS | `assets/shellspec/`, `references/gotchas.md` |
| E2E with screenshots | Playwright | `assets/e2e-workflow/`, `templates/e2e/` |
| Accessibility testing | axe-core | `references/accessibility-testing.md` |
| Test quality analysis | Python scripts | `scripts/analyze-test-quality.py` |
| Skill validation | JSON test suites | `scripts/run_tests.py` |

## Testing Modules

### 1. Rust Unit Testing

High-quality Rust unit tests following AAA pattern with deployment confidence.

**Key Principles**:
- Test naming: `test_<function>_<scenario>_<expected_behavior>`
- AAA Pattern: Arrange-Act-Assert with clear sections
- Mock external dependencies, not pure functions
- Speed target: milliseconds per test

**Quick Start**:
```rust
#[tokio::test]
async fn test_withdraw_valid_amount_decreases_balance() {
    // Arrange
    let mut account = Account::new(100);

    // Act
    let result = account.withdraw(30).await;

    // Assert
    assert!(result.is_ok());
    assert_eq!(account.balance(), 70);
}
```

**Resources**:
- Templates: `templates/rust/unit-test.md`, `templates/rust/async-test.md`
- References: `references/aaa-pattern.md`, `references/naming-conventions.md`
- Quality analysis: `scripts/analyze-test-quality.py`

### 2. E2E Testing with Playwright

Automated E2E testing with LLM-powered visual debugging.

**Workflow Phases**:
1. Application Discovery
2. Playwright Setup
3. Pre-flight Health Check
4. Test Generation
5. Screenshot Capture
6. Visual Analysis
7. Regression Detection
8. Fix Generation
9. Test Suite Export

**Quick Start**:
```typescript
import { test, expect } from '@playwright/test';

test('user creates new entity', async ({ page }) => {
  await page.goto('/entities');
  await page.getByRole('button', { name: /create/i }).click();
  await page.getByLabel(/name/i).fill('New Item');
  await page.getByRole('button', { name: /save/i }).click();
  await expect(page.getByText('New Item')).toBeVisible();
});
```

**Resources**:
- Workflow: `assets/e2e-workflow/phase-*.md`
- Templates: `templates/e2e/playwright.config.template.ts`
- Data: `assets/e2e-data/playwright-best-practices.md`

### 3. Next.js Testing Stack

Complete testing setup for Next.js with Vitest, RTL, and Playwright.

**Setup**:
```bash
python scripts/generate_test_deps.py --nextjs-version <version> --typescript
```

**Test Patterns**:
```typescript
// Component test with accessibility
import { render, screen } from '@/test/utils/render'
import { axe } from '@axe-core/playwright'

it('has no accessibility violations', async () => {
  const { container } = render(<EntityCard entity={mockEntity} />)
  const results = await axe(container)
  expect(results.violations).toHaveLength(0)
})
```

**Resources**:
- Config templates: `assets/nextjs/vitest.config.ts`, `assets/nextjs/playwright.config.ts`
- Examples: `examples/nextjs/`
- References: `references/a11y-testing.md`

### 4. TYPO3/PHP Testing

PHPUnit-based testing for TYPO3 extensions with E2E support.

**Test Types**:
- Unit tests (no database, fast)
- Functional tests (with database)
- E2E tests (Playwright browser automation)
- Fuzz tests (security, input mutation)
- Mutation tests (test quality verification)

**Quick Start**:
```bash
# Setup
scripts/setup-testing.sh --with-e2e

# Generate test
scripts/generate-test.sh unit UserValidator
scripts/generate-test.sh functional ProductRepository
scripts/generate-test.sh e2e backend-module
```

**Resources**:
- Templates: `templates/typo3/`
- References: `references/functional-testing.md`, `references/mutation-testing.md`
- Scripts: `scripts/setup-testing.sh`, `scripts/generate-test.sh`

### 5. Shell Script Testing

Testing frameworks for Bash and POSIX shell scripts.

#### ShellSpec (BDD-style)
```bash
Describe 'Calculator'
  Include lib/calculator.sh

  It 'performs addition'
    When call add 2 3
    The output should eq 5
  End
End
```

#### BATS (TAP-compliant)
```bash
@test "describe expected behavior" {
    run my_command arg1 arg2
    assert_success
    assert_output --partial "expected substring"
}
```

**Resources**:
- ShellSpec template: `assets/shellspec/spec_template.sh`
- BATS scripts: `scripts/init_bats_project.sh`
- References: `references/gotchas.md`, `references/advanced-patterns.md`

### 6. Skill Testing Framework

Validation tools for testing skills with input/output pair validation.

**Test Types**:
- Unit tests for individual components
- Integration tests for complete workflows
- Regression tests against baselines

**Quick Start**:
```bash
# Generate test template
scripts/generate_test_template.py /path/to/skill --output tests.json

# Run tests
scripts/run_tests.py tests.json --skill-path /path/to/skill

# Validate results
scripts/validate_test_results.py actual.txt expected.txt
```

**Resources**:
- Template: `assets/skill-testing/test_template.json`
- Scripts: `scripts/run_tests.py`, `scripts/generate_test_template.py`
- References: `references/test_patterns.md`, `references/writing_tests.md`

## Available Scripts

| Script | Purpose |
|--------|---------|
| `scripts/analyze-test-quality.py` | Analyze Rust test file quality |
| `scripts/setup-testing.sh` | Set up TYPO3 testing infrastructure |
| `scripts/generate-test.sh` | Generate test class templates |
| `scripts/validate-setup.sh` | Validate testing setup |
| `scripts/run_tests.py` | Run skill test suites |
| `scripts/generate_test_template.py` | Generate test templates |
| `scripts/validate_test_results.py` | Validate test outputs |
| `scripts/diagnose_test.sh` | Diagnose ShellSpec test failures |
| `scripts/init_bats_project.sh` | Initialize BATS project |
| `scripts/strip_colors.sh` | Strip ANSI colors from output |
| `scripts/generate_test_deps.py` | Generate Next.js test dependencies |

## Reference Documentation

### Core Testing Patterns
- `references/aaa-pattern.md` - Arrange-Act-Assert pattern details
- `references/naming-conventions.md` - Test naming best practices
- `references/test-builders.md` - Test builder patterns
- `references/anti-patterns.md` - Common testing anti-patterns to avoid
- `references/writing_tests.md` - Best practices for effective testing
- `references/test_patterns.md` - Examples for different skill types

### Framework-Specific
- `references/unit-testing.md` - PHP/TYPO3 unit testing
- `references/functional-testing.md` - Functional testing with database
- `references/functional-test-patterns.md` - Container reset, PHPUnit migration
- `references/async-testing.md` - Async test patterns
- `references/e2e-testing.md` - End-to-end testing guide
- `references/javascript-testing.md` - JavaScript/TypeScript testing

### Specialized Testing
- `references/fuzz-testing.md` - Security fuzz testing
- `references/mutation-testing.md` - Test quality verification
- `references/accessibility-testing.md` - axe-core WCAG compliance
- `references/a11y-testing.md` - Accessibility testing guidelines

### CI/CD & Tools
- `references/ci-cd.md` - GitHub Actions, GitLab CI workflows
- `references/ci-integration.md` - CI/CD integration patterns
- `references/ci-cd-integration.md` - E2E CI/CD examples
- `references/test-runners.md` - Test orchestration patterns
- `references/quality-tools.md` - PHPStan, Rector, php-cs-fixer
- `references/sonarcloud.md` - SonarCloud integration

### Shell Testing
- `references/gotchas.md` - BATS common pitfalls
- `references/assertions.md` - BATS assertion reference
- `references/advanced-patterns.md` - ShellSpec advanced patterns
- `references/troubleshooting.md` - Debugging test failures
- `references/collected-experience.md` - Lessons learned
- `references/real-world-examples.md` - Production patterns
- `references/projects.md` - Real-world project examples

## Templates

### Rust
- `templates/rust/unit-test.md` - Basic unit test template
- `templates/rust/async-test.md` - Async test template
- `templates/rust/test-builder.md` - Test builder pattern

### E2E/Playwright
- `templates/e2e/playwright.config.template.ts` - Playwright config
- `templates/e2e/test-spec.template.ts` - Test spec template
- `templates/e2e/page-object.template.ts` - Page Object Model
- `templates/e2e/global-setup.template.ts` - Global setup
- `templates/e2e/global-teardown.template.ts` - Global teardown
- `templates/e2e/screenshot-helper.template.ts` - Screenshot utilities

### TYPO3/PHP
- `templates/typo3/UnitTests.xml` - PHPUnit unit config
- `templates/typo3/FunctionalTests.xml` - PHPUnit functional config
- `templates/typo3/FunctionalTestsBootstrap.php` - Bootstrap file
- `templates/typo3/github-actions-tests.yml` - CI workflow
- `templates/typo3/Build/playwright/` - Playwright E2E setup
- `templates/typo3/example-tests/` - Example test classes

## Examples

### E2E
- `examples/e2e/react-vite/` - React Vite example tests
- `examples/e2e/reports/` - Example analysis reports

### Next.js
- `examples/nextjs/unit-test.ts` - Unit test example
- `examples/nextjs/component-test.tsx` - Component test example
- `examples/nextjs/e2e-test.ts` - E2E test example

## Assets

### Configuration
- `assets/nextjs/vitest.config.ts` - Vitest configuration
- `assets/nextjs/playwright.config.ts` - Playwright configuration
- `assets/nextjs/test-setup.ts` - Test setup file

### ShellSpec
- `assets/shellspec/spec_template.sh` - ShellSpec test template

### Skill Testing
- `assets/skill-testing/test_template.json` - Test suite template

### E2E Workflow
- `assets/e2e-workflow/phase-*.md` - Detailed workflow phases

### E2E Data
- `assets/e2e-data/playwright-best-practices.md`
- `assets/e2e-data/accessibility-checks.md`
- `assets/e2e-data/common-ui-bugs.md`

### Checklists
- `assets/rust-checklists/pre-commit.md` - Pre-commit checklist
- `assets/rust-checklists/review.md` - Code review checklist

## Best Practices

### Universal Testing Principles

1. **Quality over coverage** - Tests should catch real bugs, not boost metrics
2. **Test naming matters** - Names should describe expected behavior
3. **AAA pattern** - Arrange, Act, Assert for clear structure
4. **Single responsibility** - Each test verifies ONE behavior
5. **Fast tests** - Unit tests should run in milliseconds
6. **Mock external dependencies** - APIs, databases, file systems, time
7. **Don't mock** - Value types, pure functions, code under test

### Test Organization

1. Group tests by feature or domain, not by test type
2. Keep fixtures minimal, reusable, and documented
3. Ensure each test runs independently
4. Apply setUp() and tearDown() consistently
5. Document test strategy in AGENTS.md or README

### CI/CD Integration

1. Generate JUnit reports for CI integration
2. Run tests in parallel when possible
3. Set up code coverage thresholds
4. Configure test artifacts (screenshots, reports)
5. Use test tags for selective execution

## Troubleshooting

### Common Issues

**Tests not found:**
- Check file naming conventions
- Verify configuration file paths
- Ensure test class extends correct base class

**Tests are slow:**
- Enable parallel execution
- Mock external dependencies
- Use setup_file() for expensive operations

**Flaky tests:**
- Check for global state leakage
- Ensure proper cleanup in tearDown
- Mock time/random dependencies

**Database errors:**
- Verify database driver configuration
- Check fixture format
- Ensure bootstrap file is configured

**E2E failures:**
- Verify Node.js version
- Install browsers with playwright install
- Check baseURL configuration

## External Resources

| Resource | Use For |
|----------|---------|
| [Playwright Docs](https://playwright.dev/docs/intro) | E2E testing, Page Objects |
| [Vitest Docs](https://vitest.dev/) | Unit testing, configuration |
| [Testing Library](https://testing-library.com/) | React component testing |
| [axe-core](https://www.deque.com/axe/) | Accessibility testing |
| [ShellSpec](https://shellspec.info/) | Shell script BDD testing |
| [BATS](https://bats-core.readthedocs.io/) | Shell script TAP testing |
| [PHPUnit](https://phpunit.de/documentation.html) | PHP unit testing |

---

**Remember**: The goal is deployment confidence, not coverage theater. Focus testing effort where failures hurt most.







