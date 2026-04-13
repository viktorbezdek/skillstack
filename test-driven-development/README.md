# Test Driven Development

> **v1.1.17** | Quality & Testing | 19 iterations

> The Red-Green-Refactor methodology for writing failing tests before implementation code -- across Python (pytest), TypeScript (Vitest), Playwright E2E, Emacs Lisp (ERT), and Zod schema validation.

## The Problem

Most developers write code first and tests second -- if they write tests at all. The tests they write are shaped by the implementation they already built, so the tests verify the code does what it does, not what it should do. Edge cases that were not considered during implementation are not considered during testing either. The tests become a rubber stamp rather than a design tool, and the team ships bugs that a test-first approach would have caught.

When developers do practice TDD, they often do it wrong. They write tests that are too large (testing an entire workflow instead of one behavior), too coupled to implementation (asserting mock call arguments instead of observable behavior), or too isolated (100% unit test coverage but no integration tests, so the units work individually and fail together). The Red-Green-Refactor cycle degrades into "write test, write code, move on" -- the refactoring step is skipped because the tests are green and there is pressure to ship.

The problem compounds across languages. A team that practices TDD well in Python with pytest does not know how to apply the same discipline in TypeScript with Vitest. Playwright E2E tests are written without the TDD mindset because "E2E tests cannot be written first." Schema validation with Zod is not tested at all because "the schema IS the test." These gaps mean TDD coverage is inconsistent across the stack, and bugs hide in the untested layers.

## The Solution

This plugin implements the complete TDD methodology across four languages and five testing frameworks: Python with pytest, TypeScript with Vitest, browser E2E with Playwright, Emacs Lisp with ERT, and schema validation with Zod. It enforces the Red-Green-Refactor cycle at every level: write a failing test that defines the expected behavior (RED), write the minimal code to make it pass (GREEN), then improve the code while keeping tests green (REFACTOR).

The skill covers three testing tiers with clear boundaries: Unit tests (fast, isolated, mock external dependencies, run on every commit), Integration tests (test component interactions, may use test databases, run on pull requests), and E2E tests (complete user workflows, run before deployment). Coverage targets are explicit: 80-90% line coverage for unit tests, critical paths for integration, and main user workflows for E2E.

Twelve reference files provide language-specific patterns, test design patterns, refactoring techniques, and coverage validation. Five utility scripts handle test execution, coverage analysis, threshold checking, test template generation, and implementation validation. Four templates provide starting points for pytest, ERT, checklists, and session logging.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Code first, tests second -- tests verify what the code does, not what it should do | Tests first, code second -- tests define the expected behavior before implementation exists |
| Tests too large: testing entire workflows instead of individual behaviors | One test at a time, one behavior at a time -- small steps that build confidence incrementally |
| Green bar and move on -- refactoring step skipped under delivery pressure | Explicit REFACTOR phase after every GREEN: improve code quality while tests guarantee behavior |
| TDD practiced in one language but not others -- gaps across the stack | Consistent methodology across Python (pytest), TypeScript (Vitest), E2E (Playwright), Emacs Lisp (ERT), and Zod |
| Test names like `test_discount()` -- no indication of what behavior is being tested | Descriptive naming: `test_calculate_discount_returns_zero_for_empty_cart` -- behavior documented in the name |
| Shared mutable state between tests -- test order affects results | Test independence enforced: no shared state, fixtures for setup/teardown, each test runs in isolation |

## Installation

Add the SkillStack marketplace, then install this plugin:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install test-driven-development@skillstack
```

### Verify installation

After installing, test with:

```
I want to implement a shopping cart discount calculator using TDD -- walk me through the red-green-refactor cycle
```

The skill should activate and start with the RED phase: writing a failing test for the simplest case before any implementation code exists.

## Quick Start

1. **Install** the plugin using the commands above
2. **Start with the test**: `I need a function that validates email addresses -- let's do TDD`
3. The skill writes the **first failing test** (RED): `test_valid_email_returns_true` with a simple happy path case
4. You confirm the test **fails as expected** (not a syntax error -- it fails because the function does not exist yet)
5. The skill writes **minimal implementation** (GREEN): just enough code to pass that one test, then immediately asks for the next behavior to test

## What's Inside

This is a single-skill plugin with 12 reference files, 5 utility scripts, and 4 templates.

| Component | Purpose |
|---|---|
| `SKILL.md` | Core TDD methodology -- Red-Green-Refactor cycle, Arrange-Act-Assert pattern, three testing tiers, coverage targets, best practices |
| 12 reference files | Language-specific patterns, test design, refactoring, coverage validation |
| 5 utility scripts | Test runner, coverage analysis, threshold checking, template generation, validation |
| 4 templates | pytest, ERT, checklist, session logging |

**Eval coverage:** 13 trigger evaluation cases, 3 output evaluation cases.

**Key references:**

| Reference | Topic |
|---|---|
| `general-tdd.md` | TDD principles and methodology -- the philosophy behind the practice |
| `python-tdd.md` | Python-specific TDD with pytest -- fixtures, parametrization, markers |
| `vitest-patterns.md` | Vitest testing patterns for TypeScript/JavaScript |
| `playwright-e2e-patterns.md` | Playwright E2E test patterns with TDD mindset |
| `playwright-best-practices.md` | E2E testing guidelines and common pitfalls |
| `zod-testing-patterns.md` | Schema validation testing with Zod |
| `elisp-tdd.md` | Emacs Lisp TDD with ERT framework |
| `test-design-patterns.md` | Common test patterns: builder, mother, fixture, etc. |
| `test-structure-guide.md` | Test file organization and naming conventions |
| `refactoring-with-tests.md` | Safe refactoring techniques with green tests as a safety net |
| `coverage-validation.md` | Coverage analysis, threshold enforcement, gap identification |
| `extended-patterns.md` | Detailed language-specific examples and the 6-phase TDD workflow |

**Key scripts:**

| Script | Purpose |
|---|---|
| `run_tests.py` | Test runner utility with formatting and filtering |
| `coverage_analyzer.py` | Analyze coverage data and identify gaps |
| `coverage_check.py` | Enforce minimum coverage thresholds |
| `test_template_generator.py` | Generate test boilerplate for new modules |
| `skill_validator.py` | Validate test implementations against TDD practices |

### test-driven-development

**What it does:** Activates when you want to practice TDD, follow the Red-Green-Refactor cycle, or write tests before implementation code. The skill walks you through each phase of the cycle: write a failing test that defines expected behavior (RED), implement the minimal code to pass (GREEN), then refactor while keeping tests green (REFACTOR). Supports Python/pytest, TypeScript/Vitest, Playwright E2E, Emacs Lisp/ERT, and Zod schema testing.

**Try these prompts:**

```
I need to implement a user authentication module -- let's do TDD with pytest
```

```
Walk me through red-green-refactor for a React component that filters a product list by category
```

```
I want to write Playwright E2E tests using TDD for our checkout flow
```

```
My test coverage is at 65% -- help me identify the gaps and write tests to get to 80%
```

```
I'm refactoring this payment processor. The tests are green. Walk me through safe refactoring with the test safety net.
```

```
Write Vitest tests for this TypeScript utility module following TDD -- start with the failing test
```

## Real-World Walkthrough

You are building a notification service that sends alerts through email, Slack, and SMS based on user preferences. The service needs to handle preference lookup, channel routing, rate limiting, and delivery confirmation. You want to build it test-first to ensure every behavior is explicitly defined before implementation.

You open Claude Code and say:

```
I'm building a notification service in Python. It sends alerts via email, Slack, and SMS based on user preferences. Let's do TDD with pytest.
```

The skill starts with the **RED** phase. Before writing any implementation code, it identifies the simplest behavior to test first: "Given a user with email preferences, sending a notification should route to the email channel."

```python
def test_send_notification_routes_to_email_when_user_prefers_email():
    # Arrange
    user = User(id="u1", preferences=NotificationPreferences(channels=["email"]))
    notification = Notification(user_id="u1", message="Server is down", severity="critical")
    
    # Act
    result = send_notification(notification, user)
    
    # Assert
    assert result.channel == "email"
    assert result.status == "sent"
```

You run the test: it fails with `ImportError: cannot import name 'send_notification'`. This is the correct kind of failure -- the function does not exist yet, not a syntax error or logic error. The RED phase is complete.

The skill moves to **GREEN**: write the minimal code to pass this one test. Not the entire notification service -- just enough to make this specific test pass:

```python
def send_notification(notification, user):
    channel = user.preferences.channels[0]
    return NotificationResult(channel=channel, status="sent")
```

This implementation is deliberately naive. It takes the first channel, ignores severity, does not actually send anything, and does not handle rate limiting. That is fine -- the GREEN phase is about passing the test, not designing the architecture. You run the test: it passes. GREEN is complete.

Before adding more features, the skill enters the **REFACTOR** phase. The current code is so simple that there is nothing to refactor yet. The skill notes this and moves to the next behavior.

**Second cycle -- multiple channels:**

```python
def test_send_notification_routes_to_all_preferred_channels():
    user = User(id="u1", preferences=NotificationPreferences(channels=["email", "slack"]))
    notification = Notification(user_id="u1", message="Deploy complete", severity="info")
    
    results = send_notification(notification, user)
    
    assert len(results) == 2
    assert {r.channel for r in results} == {"email", "slack"}
```

RED: the test fails because `send_notification` returns a single result, not a list. GREEN: modify the function to iterate over all channels and return a list. Now both tests pass. REFACTOR: extract the channel routing into a separate function `route_to_channels(notification, preferences)` because the routing logic will grow.

**Third cycle -- rate limiting:**

```python
def test_send_notification_respects_rate_limit():
    user = User(id="u1", preferences=NotificationPreferences(channels=["sms"], rate_limit=3))
    
    for i in range(3):
        send_notification(Notification(user_id="u1", message=f"Alert {i}", severity="info"), user)
    
    result = send_notification(Notification(user_id="u1", message="Alert 4", severity="info"), user)
    
    assert result[0].status == "rate_limited"
```

RED: the test fails because there is no rate limiting logic. GREEN: add a simple counter per user per channel. REFACTOR: extract rate limiting into a `RateLimiter` class with a clear interface.

After six TDD cycles, you have a notification service with: channel routing (tested), multi-channel delivery (tested), rate limiting (tested), severity-based channel override (tested), delivery confirmation (tested), and retry logic for failed deliveries (tested). Every behavior was defined by a test before it was implemented. The test suite has 14 tests covering happy paths, edge cases, and error conditions.

The skill runs a coverage check:

```bash
uv run pytest --cov=src/notifications --cov-report=term-missing
# 94% coverage -- 2 lines uncovered in the retry backoff calculation
```

You add a test for the backoff edge case (maximum retry delay), bringing coverage to 97%. The skill then suggests the refactoring pass: the `send_notification` function has grown to 45 lines across the six cycles. Using the test safety net, you extract it into three functions (`route`, `deliver`, `confirm`) and run the full test suite after each extraction to verify nothing breaks.

The final service has clean separation of concerns, 97% test coverage, and every behavior documented in the test names. A new team member reading the test file understands exactly what the service does without reading the implementation.

## Usage Scenarios

### Scenario 1: TDD for a new feature in an existing codebase

**Context:** You are adding a discount calculation feature to an e-commerce application. The business rules are complex: percentage discounts, fixed amount discounts, minimum purchase requirements, and discount stacking rules.

**You say:** `I need to implement discount calculation with percentage, fixed, and stacking rules. Let's TDD it.`

**The skill provides:**
- Starting test for the simplest case (single percentage discount on one item)
- Progressive test additions: fixed discounts, minimum purchase, stacking order
- Refactoring guidance after each GREEN phase
- Edge case tests: zero discount, negative total, expired discounts

**You end up with:** A discount calculator with 20+ tests covering every business rule, where each rule was defined as a test before it was implemented.

### Scenario 2: E2E testing with Playwright using TDD mindset

**Context:** You are building a checkout flow and want to write E2E tests before the UI exists to define the expected user experience.

**You say:** `Write Playwright E2E tests for our checkout flow using TDD -- I want the tests to define the UX before I build it`

**The skill provides:**
- E2E test defining the happy path: add to cart, enter shipping, enter payment, confirm order
- Test structure using Playwright's page objects and locators
- Assertion patterns for each step (form validation, loading states, success confirmation)
- Guidance on what to test E2E vs. what to cover with unit tests

**You end up with:** A Playwright test suite that serves as a living specification for the checkout flow -- the implementation passes when the UX matches the defined behavior.

### Scenario 3: Increasing test coverage from 65% to 80%

**Context:** Your codebase has 65% test coverage and the CI pipeline now requires 80%. You need to identify and fill the gaps efficiently.

**You say:** `My coverage is at 65% and I need 80%. Help me find the gaps and write the missing tests.`

**The skill provides:**
- Coverage analysis identifying uncovered lines and branches using `coverage_analyzer.py`
- Priority ranking: untested business logic first, error handling second, edge cases third
- Test generation for the highest-impact gaps following TDD naming conventions
- Coverage threshold enforcement with `coverage_check.py`

**You end up with:** Targeted tests that close the 15% gap efficiently, focused on the code that matters most rather than chasing coverage in utility functions.

### Scenario 4: Safe refactoring with the test safety net

**Context:** You have a 400-line function that works correctly (tests are green) but is impossible to maintain. You want to refactor it into smaller, cleaner functions without breaking anything.

**You say:** `This 400-line function needs refactoring. Tests are green. Walk me through safe refactoring.`

**The skill provides:**
- Refactoring strategy: extract method, one function at a time, run tests after each extraction
- Guidance from `refactoring-with-tests.md` on safe transformation patterns
- New test additions for behaviors that the existing tests only covered implicitly
- Verification that refactoring did not change behavior (same inputs, same outputs)

**You end up with:** The same behavior split across 5 well-named functions, each under 80 lines, with the original tests still passing plus 3 new tests for previously implicit behaviors.

## Ideal For

- **Developers adopting TDD for the first time** -- the skill walks through each phase (RED, GREEN, REFACTOR) explicitly, preventing the common mistake of skipping the refactoring step
- **Teams building complex business logic** -- test-first ensures every business rule is defined as a test before implementation, making rules auditable and preventing regression
- **Polyglot teams working across Python, TypeScript, and Emacs Lisp** -- consistent TDD methodology across languages with framework-specific patterns for pytest, Vitest, Playwright, and ERT
- **Engineers refactoring legacy code** -- the test safety net approach ensures refactoring does not change behavior, with green tests as the guarantee

## Not For

- **Choosing or setting up test frameworks** -- use [testing-framework](../testing-framework/) for framework selection, infrastructure setup, and configuration across languages
- **Finding and fixing bugs** -- use [debugging](../debugging/) for root cause analysis and stack trace interpretation; TDD prevents bugs, it does not diagnose them
- **Reviewing existing code or PRs** -- use [code-review](../code-review/) for structured code review; TDD is a development methodology, not a review tool

## How It Works Under the Hood

The plugin is a single skill with progressive disclosure through 12 reference files. The SKILL.md body contains the core TDD methodology: the Red-Green-Refactor cycle, Arrange-Act-Assert pattern, three testing tiers with coverage targets, naming conventions, and best practices. This covers the methodology itself -- the "how to think" about TDD.

When language-specific guidance is needed, the skill loads the matching reference:

- **Language-specific:** `python-tdd.md`, `vitest-patterns.md`, `elisp-tdd.md`, `zod-testing-patterns.md`
- **E2E specific:** `playwright-e2e-patterns.md`, `playwright-best-practices.md`
- **Cross-cutting:** `test-design-patterns.md`, `test-structure-guide.md`, `refactoring-with-tests.md`, `coverage-validation.md`
- **Methodology deep-dive:** `general-tdd.md`, `extended-patterns.md`

Five utility scripts automate common TDD operations: `run_tests.py` for test execution, `coverage_analyzer.py` and `coverage_check.py` for coverage analysis and enforcement, `test_template_generator.py` for generating test boilerplate, and `skill_validator.py` for validating test implementations. Four templates provide starting points for pytest, ERT, coverage checklists, and session logging.

## Related Plugins

- **[Testing Framework](../testing-framework/)** -- Test infrastructure setup and framework selection (complementary: TDD is the methodology, testing-framework is the tooling)
- **[Python Development](../python-development/)** -- Python-specific patterns including pytest fixtures and parametrization
- **[React Development](../react-development/)** -- React component testing with hooks and component architecture patterns
- **[Debugging](../debugging/)** -- When TDD catches a bug, debugging helps trace the root cause
- **[Code Review](../code-review/)** -- Review test quality and coverage as part of PR reviews

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
