---
name: test-driven-development
description: |
  Guides the Test-Driven Development methodology: the Red-Green-Refactor cycle of writing failing tests before implementation code, then making them pass with minimal code, then refactoring. Use when the user asks to do TDD, practice test-driven development, follow red-green-refactor, write tests first, apply test-first methodology, or implement a feature using TDD workflow with pytest, Vitest, ERT, or Zod. NOT for choosing or setting up test frameworks (use testing-framework), NOT for finding and fixing bugs or analyzing stack traces (use debugging), NOT for reviewing existing code or PRs (use code-review).
---

# Test-Driven Development (TDD) Comprehensive Skill

A unified, comprehensive skill for implementing Test-Driven Development across multiple languages, frameworks, and testing levels.

## Overview

1. **Core TDD Workflow** - Red-Green-Refactor cycle
2. **Multi-Language Support** - Python, TypeScript, Emacs Lisp
3. **Testing Tiers** - Unit, Integration, E2E testing
4. **Modern Frameworks** - pytest, Vitest, Playwright
5. **Quality Assurance** - Coverage analysis, validation strategies

---

## Core TDD Principles

### The Red-Green-Refactor Cycle

```
RED    -> Write a failing test first (define expected behavior)
GREEN  -> Write minimal code to pass (just enough, don't over-engineer)
REFACTOR -> Improve code quality (clean up while tests pass)
REPEAT
```

### Key TDD Practices

1. **Test First**: Always write the test before implementation
2. **Small Steps**: One test at a time, one behavior at a time
3. **Minimal Implementation**: Write only enough code to pass
4. **Frequent Refactoring**: Clean code while tests are green
5. **Fast Feedback**: Run tests frequently (every few minutes)

---

## Test Structure Pattern: Arrange-Act-Assert

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
- No external dependencies (mocked)
- Execute in milliseconds
- High coverage of business logic
- Run on every save/commit

### Tier 2: Integration Tests
Tests for component interactions and external services.
- Test multiple components together
- May use test databases/services
- Execute in seconds
- Run on pull requests

### Tier 3: End-to-End Tests
Full system tests through the user interface.
- Test complete user workflows
- Use real or staging environment
- Execute in minutes
- Run before deployment

---

## Test Coverage Guidelines

### Coverage Targets
- **Unit Tests**: 80-90% line coverage
- **Integration Tests**: Critical paths covered
- **E2E Tests**: Main user workflows covered

### Coverage Checklist
- [ ] Happy path tests
- [ ] Edge cases (empty, null, boundary values)
- [ ] Error conditions
- [ ] Integration points
- [ ] State transitions

---

## Best Practices

### Test Naming
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

See [Extended Patterns](references/extended-patterns.md) for detailed language-specific guidance (Python/pytest, TypeScript/Vitest, Playwright E2E, Emacs Lisp/ERT), the 6-phase TDD workflow, quick reference commands, and troubleshooting.

---

## Available Resources

### Reference Documents
- `references/extended-patterns.md` - Detailed code examples and language guidance
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

### Templates
- `templates/python_test_template.py.template` - pytest test template
- `templates/elisp_test_template.el` - ERT test template
- `templates/test_checklist.md` - Coverage checklist template
- `templates/tdd_session_log.md` - TDD session logging template

---

*This skill consolidates best practices from test-driven-development-tdd-skill, testing-guide-skill, test-agent-technical-skill, and development-workflow-specialist.*
