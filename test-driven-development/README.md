# Test Driven Development

> **v1.1.17** | Quality & Testing | 19 iterations

> The Red-Green-Refactor methodology for writing failing tests before implementation code -- across Python (pytest), TypeScript (Vitest), Playwright E2E, Emacs Lisp (ERT), and Zod schema validation.
> Single skill + 12 references + 5 scripts + 4 templates

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

---

## System Overview

```
User wants to build a feature using TDD
    │
    ▼
┌─────────────────────────────────────────────────────────┐
│          test-driven-development (skill)                  │
│                                                           │
│  Red-Green-Refactor Cycle:                                │
│                                                           │
│  ┌───────────────────────────────────────────────┐        │
│  │  RED: Write failing test                       │        │
│  │  (define expected behavior)                    │        │
│  │       │                                        │        │
│  │       ▼                                        │        │
│  │  GREEN: Write minimal code                     │        │
│  │  (just enough to pass)                         │        │
│  │       │                                        │        │
│  │       ▼                                        │        │
│  │  REFACTOR: Improve code quality                │        │
│  │  (tests stay green)                            │        │
│  │       │                                        │        │
│  │       └──── REPEAT ──── ↑                      │        │
│  └───────────────────────────────────────────────┘        │
│                                                           │
│  Three Testing Tiers:                                     │
│  ├── Unit (fast, isolated, 80-90% coverage)               │
│  ├── Integration (component interactions, critical paths) │
│  └── E2E (user workflows, pre-deployment)                 │
│                                                           │
│  Language Support:                                         │
│  ├── Python ──── pytest     ── python-tdd.md              │
│  ├── TypeScript ── Vitest   ── vitest-patterns.md         │
│  ├── E2E ──────── Playwright ── playwright-*.md           │
│  ├── Emacs Lisp ── ERT     ── elisp-tdd.md               │
│  └── Schema ───── Zod      ── zod-testing-patterns.md    │
│                                                           │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐    │
│  │  12 References│  │  5 Scripts   │  │  4 Templates │    │
│  │  patterns,    │  │  run, cover- │  │  pytest, ERT │    │
│  │  refactoring, │  │  age, check, │  │  checklist,  │    │
│  │  coverage     │  │  generate,   │  │  session log │    │
│  │              │  │  validate    │  │              │    │
│  └──────────────┘  └──────────────┘  └──────────────┘    │
└─────────────────────────────────────────────────────────┘
```

## What's Inside

| Component | Type | Purpose |
|---|---|---|
| `test-driven-development` | skill | Core TDD methodology: Red-Green-Refactor, Arrange-Act-Assert, three testing tiers, coverage targets, naming conventions |
| `general-tdd.md` | reference | TDD principles and philosophy |
| `python-tdd.md` | reference | Python-specific TDD with pytest: fixtures, parametrization, markers |
| `vitest-patterns.md` | reference | Vitest testing patterns for TypeScript/JavaScript |
| `playwright-e2e-patterns.md` | reference | Playwright E2E test patterns with TDD mindset |
| `playwright-best-practices.md` | reference | E2E testing guidelines and common pitfalls |
| `zod-testing-patterns.md` | reference | Schema validation testing with Zod |
| `elisp-tdd.md` | reference | Emacs Lisp TDD with ERT framework |
| `test-design-patterns.md` | reference | Common test patterns: builder, mother, fixture |
| `test-structure-guide.md` | reference | Test file organization and naming conventions |
| `refactoring-with-tests.md` | reference | Safe refactoring techniques with green tests as safety net |
| `coverage-validation.md` | reference | Coverage analysis, threshold enforcement, gap identification |
| `extended-patterns.md` | reference | Detailed language-specific examples and the 6-phase TDD workflow |
| `run_tests.py` | script | Test runner utility with formatting and filtering |
| `coverage_analyzer.py` | script | Analyze coverage data and identify gaps |
| `coverage_check.py` | script | Enforce minimum coverage thresholds |
| `test_template_generator.py` | script | Generate test boilerplate for new modules |
| `skill_validator.py` | script | Validate test implementations against TDD practices |
| 4 template files | template | pytest, ERT, coverage checklist, and TDD session log |

**Eval coverage:** 13 trigger evaluation cases, 3 output evaluation cases.

### Component Spotlights

#### test-driven-development (skill)

**What it does:** Activates when you want to practice TDD, follow the Red-Green-Refactor cycle, or write tests before implementation. Walks you through each phase: write a failing test (RED), implement minimal code to pass (GREEN), refactor while tests stay green (REFACTOR). Supports Python/pytest, TypeScript/Vitest, Playwright E2E, Emacs Lisp/ERT, and Zod schema testing.

**Input -> Output:** A feature or behavior to implement -> A test-first development session with failing test, minimal implementation, refactoring, and iterative expansion through successive TDD cycles.

**When to use:** Implementing new features with test-first methodology. Adding tests to increase coverage. Refactoring with a test safety net. Writing E2E tests that define expected UX. Practicing TDD in a new language or framework.

**When NOT to use:** Choosing or setting up test frameworks (use testing-framework). Finding and fixing bugs (use debugging). Reviewing existing code or PRs (use code-review).

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

**Key references:**

| Reference | Topic |
|---|---|
| `general-tdd.md` | TDD principles and methodology |
| `python-tdd.md` | pytest fixtures, parametrization, markers |
| `vitest-patterns.md` | Vitest testing patterns for TypeScript |
| `playwright-e2e-patterns.md` | Playwright E2E with TDD mindset |
| `test-design-patterns.md` | Builder, mother, fixture patterns |
| `refactoring-with-tests.md` | Safe refactoring techniques |
| `coverage-validation.md` | Coverage analysis and gap identification |

#### coverage_analyzer.py (script)

**CLI:** `python scripts/coverage_analyzer.py --path src/ --threshold 80`
**What it produces:** A coverage analysis report identifying uncovered lines, branches, and functions, ranked by impact. Highlights the highest-value gaps to close first.
**Typical workflow:** After a TDD session, run to verify coverage targets are met and identify remaining gaps.

#### test_template_generator.py (script)

**CLI:** `python scripts/test_template_generator.py --module src/auth.py --output tests/test_auth.py`
**What it produces:** A test file skeleton with Arrange-Act-Assert structure, proper fixtures, and descriptive test names for each public function in the module.
**Typical workflow:** When starting TDD on an existing module that has no tests, generate the skeleton first then fill in assertions.

---

## Prompt Patterns

### Good Prompts vs Bad Prompts

| Bad (skips the TDD mindset) | Good (embraces test-first thinking) |
|---|---|
| "Write a discount calculator" | "I need a discount calculator with percentage, fixed, and stacking rules -- let's TDD it starting with the simplest case" |
| "Write tests for this function" | "I want to practice TDD for this feature -- start with the failing test before any implementation exists" |
| "Add tests to get coverage up" | "My coverage is 65% and I need 80%. Analyze the gaps and prioritize: untested business logic first, edge cases second" |
| "Test this component" | "Walk me through red-green-refactor for this React component -- I want E2E tests with Playwright that define the UX first" |
| "Refactor this code" | "This 400-line function works (tests green). Walk me through extracting smaller functions with the test safety net." |

### Structured Prompt Templates

**For starting a new feature with TDD:**
```
I need to implement [feature description] in [language: Python / TypeScript / Emacs Lisp].
The key behaviors are [list 2-3 core behaviors]. Let's do TDD with [framework: pytest / Vitest / ERT].
Start with the failing test for the simplest behavior.
```

**For increasing coverage:**
```
My [project / module] has [N]% test coverage and I need [target]%.
Analyze the gaps and write tests for the highest-impact uncovered code.
Focus on [priority: business logic / error handling / edge cases] first.
```

**For safe refactoring:**
```
This [function / class / module] is [N] lines and needs refactoring.
All tests pass. Walk me through safe refactoring: one extraction at a time,
run tests after each change, no behavior changes.
```

**For E2E with TDD mindset:**
```
Write Playwright E2E tests for [user workflow] using TDD. Define the expected
user experience as tests BEFORE I build the UI. The key steps are:
[list user actions and expected outcomes].
```

### Prompt Anti-Patterns

- **Asking to "write tests for existing code" without the TDD mindset:** This is test-after, not test-driven. The skill works best when you describe the behavior you want to implement and let it write the failing test first. If the code already exists, ask for coverage gap analysis instead.
- **Requesting the entire implementation at once:** TDD works in small cycles. Asking to "implement the full authentication system with TDD" skips the incremental nature of the methodology. Instead, ask to start with one behavior ("valid email returns true") and build up.
- **Skipping the RED verification:** The failing test must fail for the right reason (missing functionality, not syntax errors). If you do not verify the failure, you might write a test that accidentally passes, defeating the purpose.
- **Asking to "just make it pass" without mentioning refactoring:** The REFACTOR phase is not optional. After GREEN, explicitly ask about refactoring opportunities. The skill will prompt you, but acknowledging the phase keeps the cycle disciplined.

## Real-World Walkthrough

You are building a notification service that sends alerts through email, Slack, and SMS based on user preferences. The service needs to handle preference lookup, channel routing, rate limiting, and delivery confirmation. You want to build it test-first to ensure every behavior is explicitly defined before implementation.

You open Claude Code and say:

```
I'm building a notification service in Python. It sends alerts via email, Slack, and SMS based on user preferences. Let's do TDD with pytest.
```

The skill starts with the **RED** phase. Before writing any implementation code, it identifies the simplest behavior to test first: "Given a user with email preferences, sending a notification should route to the email channel."

```python
def test_send_notification_routes_to_email_when_user_prefers_email():
    user = User(id="u1", preferences=NotificationPreferences(channels=["email"]))
    notification = Notification(user_id="u1", message="Server is down", severity="critical")
    result = send_notification(notification, user)
    assert result.channel == "email"
    assert result.status == "sent"
```

You run the test: it fails with `ImportError: cannot import name 'send_notification'`. This is the correct kind of failure -- the function does not exist yet. RED is complete.

The skill moves to **GREEN**: write the minimal code to pass this one test. Not the entire notification service -- just enough:

```python
def send_notification(notification, user):
    channel = user.preferences.channels[0]
    return NotificationResult(channel=channel, status="sent")
```

Deliberately naive. Test passes. GREEN is complete. REFACTOR: nothing to refactor yet -- too simple.

**Second cycle -- multiple channels:** Write a test expecting a list of results for multiple preferred channels. RED: fails because the function returns a single result. GREEN: modify to iterate over channels. REFACTOR: extract channel routing into a separate function.

**Third cycle -- rate limiting:** Write a test that sends 4 notifications when the rate limit is 3, asserting the 4th returns "rate_limited." RED: fails. GREEN: add a counter. REFACTOR: extract into a `RateLimiter` class.

After six TDD cycles, you have channel routing, multi-channel delivery, rate limiting, severity-based overrides, delivery confirmation, and retry logic -- every behavior defined by a test before implementation. The test suite has 14 tests. Coverage check:

```bash
uv run pytest --cov=src/notifications --cov-report=term-missing
# 94% coverage -- 2 lines uncovered in retry backoff
```

One more test for the backoff edge case brings coverage to 97%. The skill then walks you through a final refactoring pass: the `send_notification` function has grown to 45 lines across six cycles. Using the test safety net, you extract it into three functions (`route`, `deliver`, `confirm`), running the full suite after each extraction.

## Usage Scenarios

### Scenario 1: TDD for complex business logic

**Context:** You are adding a discount calculation feature with percentage, fixed amount, minimum purchase, and stacking rules.

**You say:** `I need to implement discount calculation with percentage, fixed, and stacking rules. Let's TDD it.`

**The skill provides:**
- Starting test for the simplest case (single percentage discount)
- Progressive test additions for each rule
- Refactoring guidance after each GREEN
- Edge case tests: zero discount, negative total, expired discounts

**You end up with:** A discount calculator with 20+ tests where each business rule was defined as a test before implementation.

### Scenario 2: E2E testing with Playwright using TDD

**Context:** Building a checkout flow and want E2E tests to define the expected UX before the UI exists.

**You say:** `Write Playwright E2E tests for our checkout flow using TDD -- define the UX before I build it`

**The skill provides:**
- E2E tests defining the happy path: cart, shipping, payment, confirmation
- Page object structure and locator patterns
- Assertion patterns for each step
- Guidance on E2E vs unit test boundaries

**You end up with:** A Playwright suite that serves as a living specification -- the implementation passes when the UX matches.

### Scenario 3: Closing a coverage gap

**Context:** 65% coverage, CI requires 80%. Need to fill the gaps efficiently.

**You say:** `My coverage is at 65% and I need 80%. Find the gaps and write the missing tests.`

**The skill provides:**
- Coverage analysis identifying uncovered lines and branches
- Priority ranking: business logic first, error handling second, edge cases third
- Test generation for highest-impact gaps
- Threshold enforcement with `coverage_check.py`

**You end up with:** Targeted tests closing the 15% gap, focused on code that matters.

### Scenario 4: Safe refactoring with test safety net

**Context:** A 400-line function works correctly but is impossible to maintain. Tests are green.

**You say:** `This 400-line function needs refactoring. Tests are green. Walk me through safe refactoring.`

**The skill provides:**
- Extract method strategy, one function at a time
- Test execution after each extraction
- New tests for previously implicit behaviors
- Verification that refactoring preserved behavior

**You end up with:** The same behavior in 5 well-named functions under 80 lines each, with original tests passing plus new tests for implicit behaviors.

---

## Decision Logic

**How does the skill choose which testing tier to apply?**

- **Unit tests** (default): when testing isolated functions, business logic, or data transformations with no external dependencies. Mock everything external. Run in milliseconds.
- **Integration tests**: when testing interactions between components, database queries, or external API contracts. Use test databases or fixtures. Run in seconds.
- **E2E tests**: when defining or verifying complete user workflows through the UI. Use Playwright with real or staging environments. Run in minutes.

The skill defaults to unit tests unless the task involves component interactions (integration) or user workflows (E2E).

**How does the skill choose which language reference to load?**

Based on file extensions and explicit mentions:
- `.py` files or "pytest" mentions -> `python-tdd.md`
- `.ts`/`.tsx` files or "Vitest" mentions -> `vitest-patterns.md`
- "Playwright" or "E2E" or "browser" -> `playwright-e2e-patterns.md`
- `.el` files or "ERT" or "Emacs Lisp" -> `elisp-tdd.md`
- "Zod" or "schema" -> `zod-testing-patterns.md`

**When does REFACTOR happen?**

After every GREEN phase. The skill checks: Is the implementation code clean? Are there duplicated patterns? Has the function grown too long? Are there extract method opportunities? If yes, refactor now with tests as the safety net. If the code is still simple (early cycles), the skill notes this and moves to the next RED.

## Failure Modes & Edge Cases

| Failure | Symptom | Recovery |
|---|---|---|
| Test passes when it should fail (GREEN before RED) | The test accidentally passes because the function already exists or the assertion is wrong | Verify the RED phase: the test must fail because the behavior is not implemented, not because of a syntax error. If the test passes immediately, the assertion is not testing the right thing. |
| Tests coupled to implementation, not behavior | Refactoring breaks tests even though behavior has not changed -- tests assert mock call arguments instead of outputs | Rewrite tests to assert observable behavior (return values, side effects, state changes) not implementation details (which functions were called, in what order). |
| Refactoring step consistently skipped | Code works but grows messily across TDD cycles -- functions become long, names become vague | The skill explicitly prompts for refactoring after every GREEN. If you skip it, technical debt accumulates during the TDD session itself. Treat REFACTOR as mandatory, not optional. |
| Coverage numbers are high but tests are shallow | 90% line coverage but tests only check happy paths -- no edge cases, no error handling, no boundary conditions | Line coverage is necessary but not sufficient. The skill uses `coverage_analyzer.py` to identify covered-but-shallow code and suggests edge case, error, and boundary tests. |
| E2E tests are too slow for TDD rhythm | Playwright tests take 30+ seconds per run, breaking the fast feedback cycle | Use unit/integration tests for the rapid RED-GREEN-REFACTOR cycle. Write E2E tests to define the workflow specification, but do not run them on every micro-cycle. Run E2E after each feature is unit-tested. |

## Ideal For

- **Developers adopting TDD for the first time** -- the skill walks through each phase (RED, GREEN, REFACTOR) explicitly, preventing the common mistake of skipping refactoring
- **Teams building complex business logic** -- test-first ensures every business rule is defined as a test before implementation, making rules auditable and preventing regression
- **Polyglot teams working across Python, TypeScript, and Emacs Lisp** -- consistent TDD methodology across languages with framework-specific patterns
- **Engineers refactoring legacy code** -- the test safety net approach ensures refactoring does not change behavior

## Not For

- **Choosing or setting up test frameworks** -- use [testing-framework](../testing-framework/) for framework selection, infrastructure setup, and configuration across languages
- **Finding and fixing bugs** -- use [debugging](../debugging/) for root cause analysis and stack trace interpretation; TDD prevents bugs, it does not diagnose them
- **Reviewing existing code or PRs** -- use [code-review](../code-review/) for structured code review; TDD is a development methodology, not a review tool

## Related Plugins

- **[Testing Framework](../testing-framework/)** -- Test infrastructure setup and framework selection (complementary: TDD is the methodology, testing-framework is the tooling)
- **[Python Development](../python-development/)** -- Python-specific patterns including pytest fixtures and parametrization
- **[React Development](../react-development/)** -- React component testing with hooks and component architecture patterns
- **[Debugging](../debugging/)** -- When TDD catches a bug, debugging helps trace the root cause
- **[Code Review](../code-review/)** -- Review test quality and coverage as part of PR reviews

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
