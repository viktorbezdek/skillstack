# Test-Driven Development - Extended Patterns & Examples

Detailed code examples, language-specific guidance, and testing patterns extracted from the core skill.

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
pytest                                      # All tests
pytest --cov=src --cov-report=html          # With coverage
pytest tests/unit/test_feature.py -k "test_specific"  # Specific
pytest -v --tb=short                        # Verbose
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
    await page.getByTestId('start-button').click();
    await page.getByTestId('email-input').fill('test@example.com');
    await page.waitForURL('/dashboard');
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
  (let ((input "test"))
    (let ((result (my-function input)))
      (should (equal result "expected")))))

(ert-deftest test-buffer-manipulation ()
  "Test inserting into buffer."
  (with-temp-buffer
    (my-insert-function "test")
    (should (string= (buffer-string) "expected output"))))

(ert-deftest test-with-mocked-input ()
  "Test function that reads user input."
  (cl-letf (((symbol-function 'read-string)
             (lambda (prompt) "mocked-input")))
    (should (string= (my-function-that-reads) "expected"))))
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

### Phase 4: Refactor (IMPROVE)
- Clean up code while tests pass
- Extract methods, rename variables
- Remove duplication
- Run tests after each change

### Phase 5: Expand Coverage
- Add edge cases and error handling tests
- Add integration tests
- Repeat cycle for each new behavior

### Phase 6: Validate & Document
- Ensure coverage targets met (80-90%)
- Update documentation
- Commit with meaningful message

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
