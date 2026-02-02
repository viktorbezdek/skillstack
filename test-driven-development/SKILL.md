---
name: test-driven-development
description: Comprehensive Test-Driven Development skill implementing Red-Green-Refactor cycle across Python, TypeScript, JavaScript, and Emacs Lisp. Covers pytest, Vitest, Playwright, ERT, and Zod. Use when writing tests before implementation, setting up TDD workflows, implementing test strategies at unit/integration/E2E levels, or ensuring coverage and quality assurance. Triggers include TDD, test-driven, red-green-refactor, pytest, vitest, playwright, test coverage, and testing methodology.
---

# Test-Driven Development (TDD) Comprehensive Skill

A unified, comprehensive skill for implementing Test-Driven Development across multiple languages, frameworks, and testing levels. This skill combines best practices from TDD methodology, testing strategies, and modern testing frameworks.

## Overview

Test-Driven Development is a software development methodology where tests are written before the implementation code. This skill provides comprehensive guidance for:

1. **Core TDD Workflow** - Red-Green-Refactor cycle
2. **Multi-Language Support** - Python, TypeScript, Emacs Lisp
3. **Testing Tiers** - Unit, Integration, E2E testing
4. **Modern Frameworks** - pytest, Vitest, Playwright
5. **Quality Assurance** - Coverage analysis, validation strategies

---

## Core TDD Principles

### The Red-Green-Refactor Cycle

```
┌─────────────────────────────────────────────────────────────┐
│                    TDD CYCLE                                │
│                                                             │
│     ┌─────────┐                                             │
│     │  RED    │  Write a failing test first                 │
│     │ (Fail)  │  - Define expected behavior                 │
│     └────┬────┘  - Test should fail initially               │
│          │                                                  │
│          ▼                                                  │
│     ┌─────────┐                                             │
│     │  GREEN  │  Write minimal code to pass                 │
│     │ (Pass)  │  - Just enough to make test pass            │
│     └────┬────┘  - Don't over-engineer                      │
│          │                                                  │
│          ▼                                                  │
│     ┌─────────┐                                             │
│     │REFACTOR │  Improve code quality                       │
│     │(Improve)│  - Clean up while tests pass                │
│     └────┬────┘  - Maintain test coverage                   │
│          │                                                  │
│          └──────────► Repeat                                │
└─────────────────────────────────────────────────────────────┘
```

### Key TDD Practices

1. **Test First**: Always write the test before implementation
2. **Small Steps**: One test at a time, one behavior at a time
3. **Minimal Implementation**: Write only enough code to pass
4. **Frequent Refactoring**: Clean code while tests are green
5. **Fast Feedback**: Run tests frequently (every few minutes)

---

## Test Structure Pattern: Arrange-Act-Assert

All tests should follow the AAA pattern for clarity and consistency:

```python
def test_descriptive_name():
    """Clear description of what is being tested."""
    # Arrange - Set up test data and conditions
    input_data = prepare_test_data()
    expected_result = "expected_value"

    # Act - Execute the code under test
    actual_result = function_under_test(input_data)

    # Assert - Verify the results
    assert actual_result == expected_result
```

---

## Testing Tiers

### Tier 1: Unit Tests
Fast, isolated tests for individual functions/methods.

**Characteristics:**
- No external dependencies (mocked)
- Execute in milliseconds
- High coverage of business logic
- Run on every save/commit

**Example (Python/pytest):**
```python
def test_calculate_total_with_discount():
    """Unit test for discount calculation."""
    # Arrange
    cart = Cart(items=[Item(price=100), Item(price=50)])
    discount = Discount(percentage=10)

    # Act
    total = cart.calculate_total(discount)

    # Assert
    assert total == 135.0  # 150 - 10%
```

### Tier 2: Integration Tests
Tests for component interactions and external services.

**Characteristics:**
- Test multiple components together
- May use test databases/services
- Execute in seconds
- Run on pull requests

**Example (TypeScript/Vitest):**
```typescript
describe('UserService Integration', () => {
  it('should create user and send welcome email', async () => {
    // Arrange
    const userService = new UserService(testDb, emailService);
    const userData = { email: 'test@example.com', name: 'Test' };

    // Act
    const user = await userService.createUser(userData);

    // Assert
    expect(user.id).toBeDefined();
    expect(emailService.send).toHaveBeenCalledWith(
      expect.objectContaining({ to: userData.email })
    );
  });
});
```

### Tier 3: End-to-End Tests
Full system tests through the user interface.

**Characteristics:**
- Test complete user workflows
- Use real or staging environment
- Execute in minutes
- Run before deployment

**Example (Playwright):**
```typescript
test('user can complete checkout flow', async ({ page }) => {
  // Navigate and add item
  await page.goto('/products');
  await page.getByTestId('product-card').first().click();
  await page.getByTestId('add-to-cart').click();

  // Checkout
  await page.getByTestId('checkout-button').click();
  await page.getByTestId('confirm-order').click();

  // Verify
  await expect(page.getByTestId('order-confirmation')).toBeVisible();
});
```

---

## Language-Specific Guidance

### Python Testing with pytest

**Installation:**
```bash
pip install pytest pytest-cov pytest-mock
```

**Test Organization:**
```
project/
├── src/
│   └── module/
│       └── feature.py
└── tests/
    ├── unit/
    │   └── test_feature.py
    ├── integration/
    │   └── test_feature_integration.py
    └── conftest.py
```

**Key pytest Features:**
```python
import pytest

# Fixtures for setup/teardown
@pytest.fixture
def sample_data():
    return {"key": "value"}

# Parametrized tests
@pytest.mark.parametrize("input,expected", [
    ("a", 1),
    ("b", 2),
    ("c", 3),
])
def test_multiple_cases(input, expected):
    assert function(input) == expected

# Testing exceptions
def test_raises_error():
    with pytest.raises(ValueError, match="invalid input"):
        function("invalid")

# Mocking with pytest-mock
def test_with_mock(mocker):
    mock_api = mocker.patch('module.external_api')
    mock_api.return_value = {'status': 'ok'}
    result = function_that_calls_api()
    assert result == expected
```

**Running Tests:**
```bash
# All tests
pytest

# With coverage
pytest --cov=src --cov-report=html

# Specific file or pattern
pytest tests/unit/test_feature.py -k "test_specific"

# Verbose output
pytest -v --tb=short
```

### TypeScript Testing with Vitest

**Installation:**
```bash
npm install -D vitest @vitest/coverage-v8
```

**Key Vitest Patterns:**
```typescript
import { describe, it, expect, vi, beforeEach } from 'vitest';

describe('FeatureService', () => {
  let service: FeatureService;

  beforeEach(() => {
    vi.clearAllMocks();
    service = new FeatureService();
  });

  it('should process data correctly', () => {
    const result = service.process({ input: 'test' });
    expect(result).toEqual({ output: 'processed' });
  });

  it('should call dependency with correct params', () => {
    const mockDep = vi.fn().mockReturnValue('mocked');
    service.setDependency(mockDep);

    service.execute('param');

    expect(mockDep).toHaveBeenCalledWith('param');
  });
});
```

**Mocking Patterns:**
```typescript
// Mock entire module
vi.mock('./dependency', () => ({
  fetchData: vi.fn().mockResolvedValue({ data: 'mocked' })
}));

// Spy on method
const spy = vi.spyOn(object, 'method');

// Mock implementation
vi.fn().mockImplementation((arg) => arg * 2);
```

### Playwright E2E Testing

**Key Patterns:**
```typescript
import { test, expect } from '@playwright/test';

test.describe('Feature Flow', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/');
  });

  test('completes user journey', async ({ page }) => {
    // Use data-testid for reliable selectors
    await page.getByTestId('start-button').click();

    // Fill forms
    await page.getByTestId('email-input').fill('test@example.com');

    // Wait for navigation
    await page.waitForURL('/dashboard');

    // Assertions
    await expect(page.getByTestId('welcome-message')).toContainText('Welcome');
  });
});
```

**Best Practices:**
- Always use `data-testid` attributes for selectors
- Avoid arbitrary timeouts; use `waitFor` methods
- Test user-visible behavior, not implementation
- Keep tests independent and idempotent

### Emacs Lisp Testing with ERT

**Test Structure:**
```elisp
(require 'ert)
(require 'my-module)

(ert-deftest test-basic-functionality ()
  "Test basic functionality with valid input."
  ;; Arrange
  (let ((input "test"))
    ;; Act
    (let ((result (my-function input)))
      ;; Assert
      (should (equal result "expected")))))

(ert-deftest test-buffer-manipulation ()
  "Test inserting into buffer."
  (with-temp-buffer
    ;; Act
    (my-insert-function "test")
    ;; Assert
    (should (string= (buffer-string) "expected output"))))

(ert-deftest test-with-mocked-input ()
  "Test function that reads user input."
  (cl-letf (((symbol-function 'read-string)
             (lambda (prompt) "mocked-input")))
    (should (string= (my-function-that-reads) "expected"))))
```

**Running ERT Tests:**
```elisp
;; Interactive
M-x ert RET t RET                 ; All tests
M-x ert RET "test-prefix-*" RET   ; Matching pattern

;; Batch mode
emacs -batch -l ert -l module.el -l test-module.el \
      -f ert-run-tests-batch-and-exit
```

---

## TDD Workflow: 6-Phase Process

### Phase 1: Understand Requirements
- Review specifications and acceptance criteria
- Identify test scenarios and edge cases
- Document expected behaviors

### Phase 2: Write Failing Test (RED)
```python
def test_new_feature():
    """Test the feature we're about to implement."""
    result = new_feature("input")
    assert result == "expected_output"
```
- Run test to confirm it fails
- Failure should be for the right reason (not syntax error)

### Phase 3: Implement Minimal Code (GREEN)
```python
def new_feature(input):
    """Minimal implementation to pass test."""
    return "expected_output"
```
- Write just enough code to pass
- Don't add extra functionality

### Phase 4: Refactor (IMPROVE)
- Clean up code while tests pass
- Extract methods, rename variables
- Remove duplication
- Run tests after each change

### Phase 5: Expand Coverage
- Add edge cases
- Add error handling tests
- Add integration tests
- Repeat cycle for each new behavior

### Phase 6: Validate & Document
- Ensure coverage targets met (80-90%)
- Update documentation
- Commit with meaningful message

---

## Test Coverage Guidelines

### Coverage Targets
- **Unit Tests**: 80-90% line coverage
- **Integration Tests**: Critical paths covered
- **E2E Tests**: Main user workflows covered

### Running Coverage Analysis

**Python:**
```bash
pytest --cov=src --cov-report=html --cov-fail-under=80
```

**TypeScript:**
```bash
vitest run --coverage
```

### Coverage Checklist
- [ ] Happy path tests
- [ ] Edge cases (empty, null, boundary values)
- [ ] Error conditions
- [ ] Integration points
- [ ] State transitions

---

## Best Practices

### Test Naming
Use descriptive names that explain the scenario:
```python
# Good
def test_calculate_discount_returns_zero_for_empty_cart():
    ...

# Bad
def test_discount():
    ...
```

### Test Independence
- Each test should run in isolation
- No shared mutable state between tests
- Use fixtures for setup/teardown

### Fast Feedback
- Unit tests should run in milliseconds
- Run tests frequently during development
- Use watch mode for continuous testing

### Meaningful Assertions
```python
# Good - specific assertion with message
assert result.status == "success", f"Expected success but got {result.status}"

# Bad - generic assertion
assert result
```

---

## Available Resources

### Reference Documents
- `references/general-tdd.md` - TDD principles and methodology
- `references/python-tdd.md` - Python-specific TDD practices
- `references/elisp-tdd.md` - Emacs Lisp TDD with ERT
- `references/vitest-patterns.md` - Vitest testing patterns
- `references/playwright-e2e-patterns.md` - Playwright best practices
- `references/playwright-best-practices.md` - E2E testing guidelines
- `references/zod-testing-patterns.md` - Schema validation testing
- `references/test-design-patterns.md` - Common test patterns
- `references/test-structure-guide.md` - Test organization
- `references/refactoring-with-tests.md` - Safe refactoring practices
- `references/coverage-validation.md` - Coverage analysis guide

### Scripts
- `scripts/run_tests.py` - Test runner utility
- `scripts/coverage_analyzer.py` - Coverage analysis tool
- `scripts/coverage_check.py` - Coverage threshold checker
- `scripts/test_template_generator.py` - Generate test boilerplate
- `scripts/skill_validator.py` - Validate test implementations
- `scripts/with_server.py` - Test server management

### Templates
- `templates/python_test_template.py.template` - pytest test template
- `templates/elisp_test_template.el` - ERT test template
- `templates/test_checklist.md` - Coverage checklist template
- `templates/tdd_session_log.md` - TDD session logging template

---

## Quick Reference Commands

### Python/pytest
```bash
pytest                           # Run all tests
pytest -v                        # Verbose output
pytest -k "pattern"              # Run matching tests
pytest --cov=src                 # With coverage
pytest -x                        # Stop on first failure
pytest --lf                      # Run last failed
```

### TypeScript/Vitest
```bash
vitest                           # Watch mode
vitest run                       # Run once
vitest run --coverage            # With coverage
vitest run -t "pattern"          # Run matching tests
```

### Playwright
```bash
npx playwright test              # Run all tests
npx playwright test --ui         # Interactive UI mode
npx playwright test --debug      # Debug mode
npx playwright show-report       # View HTML report
```

### Emacs/ERT
```elisp
M-x ert RET t RET               ; All tests
M-x ert RET "pattern" RET       ; Matching tests
```

---

## Troubleshooting

### Test Flakiness
- Use explicit waits instead of sleep
- Ensure test isolation
- Check for race conditions
- Reset state between tests

### Coverage Gaps
- Review uncovered branches
- Add edge case tests
- Check error handling paths
- Verify mock configurations

### Slow Tests
- Profile test execution
- Move slow tests to integration tier
- Optimize fixtures
- Use parallel execution

---

## Contributing

When adding new tests or modifying existing ones:

1. Follow the Arrange-Act-Assert pattern
2. Use descriptive test names
3. Include docstrings explaining the test purpose
4. Ensure tests are independent
5. Maintain coverage thresholds
6. Update documentation as needed

---

*This skill consolidates best practices from test-driven-development-tdd-skill, testing-guide-skill, test-agent-technical-skill, and development-workflow-specialist.*







