# Edge Case Coverage

> **v1.0.10** | Quality & Testing | 11 iterations

> Systematically identify every boundary condition, error scenario, and validation gap before they become production incidents.

## The Problem

Every production outage post-mortem tells the same story: the code worked fine on the happy path, but nobody checked what happens when the input is empty, the token is expired, the file is zero bytes, or the database connection drops mid-transaction. These failures are not exotic -- they are the most common class of bugs in production systems. Yet they are consistently missed because developers and reviewers follow the same mental path through the code, focusing on what the feature *should* do rather than what happens when assumptions break.

The root cause is not laziness -- it is a lack of systematic enumeration. When a developer is asked "have you handled edge cases?" they scan for what comes to mind: maybe null, maybe an empty string. But the input space is combinatorial. A registration form with three fields (name, email, age) has at least 15 distinct edge conditions per field -- boundary values, type mismatches, format violations, encoding issues, and overflow scenarios. Without a framework, most developers cover 3-4 of these and call it done.

The cost compounds silently. Each missed edge case is a latent defect that passes code review, passes QA (which tests the same happy path), and ships to production where it surfaces as a 3am alert, a corrupted record, or a security vulnerability. By the time it is caught, the fix costs 10-50x what it would have cost to enumerate the case up front.

## The Solution

This plugin gives Claude a structured methodology for systematically enumerating edge cases across six categories: boundary values, input validation, state transitions, resource limits, network conditions, and permission models. Instead of relying on intuition, Claude walks through each category with concrete templates -- the seven values to test around any numeric limit, the six dimensions of input validation, and a coverage matrix that maps every field against every failure condition.

When you describe a function, an API endpoint, or a form, the skill produces a complete enumeration of what could go wrong -- not as abstract advice, but as a concrete checklist you can turn directly into test cases or validation rules. The error scenario template captures trigger, symptoms, root cause, prevention, and recovery for each failure mode, producing documentation that doubles as a runbook for on-call engineers.

The output is actionable: a coverage matrix you can paste into a ticket, a validation checklist you can walk through during review, and an anti-pattern audit that catches the five most common defensive-programming mistakes (happy-path-only testing, ignoring nulls, assuming valid input, missing timeout handling, and silent failures).

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Edge case analysis depends on the developer's memory and experience -- gaps are invisible until production | Systematic six-category enumeration surfaces conditions the developer never thought to check |
| Code reviews catch only the edge cases the reviewer personally thinks of, duplicating the author's blind spots | Coverage matrix provides a visual artifact showing exactly which conditions are tested and which are not |
| Error scenarios are undocumented -- on-call engineers reverse-engineer failure modes from stack traces | Error scenario template produces runbook-quality entries with trigger, symptoms, root cause, and recovery |
| Boundary values are checked informally ("did you handle zero?") instead of exhaustively | Boundary analysis template provides the seven canonical values to test around any numeric or string limit |
| Validation logic is split between client and server with no single view of what is actually checked | Validation checklist covers six dimensions (required, type, format, range, length, characters) per field |
| Post-mortems repeatedly cite "we didn't think of that case" as root cause | Anti-pattern audit catches the five most common gaps before review |

## Installation

Add the SkillStack marketplace, then install this plugin:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install edge-case-coverage@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when your prompts mention edge cases, boundary conditions, validation, corner cases, or error scenarios.

## Quick Start

1. Install the plugin using the commands above
2. Open a Claude Code session in your project
3. Type: `What edge cases should I handle in this user registration endpoint?`
4. The skill produces a coverage matrix mapping every input field against valid, empty, null, overflow, and malformed conditions -- plus boundary analysis for numeric fields and a validation checklist
5. Hand the resulting list to your testing workflow: `Now write tests for all of these edge cases` (which activates test-driven-development or testing-framework)

## What's Inside

Single-skill plugin shipping one SKILL.md with six structured components, 13 trigger eval cases, and 3 output eval cases.

| Component | What It Provides |
|---|---|
| **Edge Case Categories** | Taxonomy of six types -- boundary, input, state, resource, network, permission -- each with concrete examples |
| **Boundary Analysis** | Templates for numeric and string limits showing the seven canonical values to test around any boundary |
| **Error Scenario Template** | Five-field documentation format (trigger, symptoms, root cause, prevention, recovery) for each failure mode |
| **Validation Checklist** | Two-section checklist covering input validation (type, format, range, length, characters) and state validation (initialization, resources, permissions, dependencies) |
| **Coverage Matrix** | Tabular format mapping every input field against five key test conditions: valid, empty, null, overflow, malformed |
| **Anti-Patterns** | The five most common defensive-programming mistakes with explanations |

### edge-case-coverage

**What it does:** Activates when you ask about edge cases, boundary conditions, validation gaps, corner cases, or error scenarios. Walks through a six-category taxonomy (boundary, input, state, resource, network, permission) and applies structured templates to your specific code, producing coverage matrices, boundary analysis trees, validation checklists, and error scenario documentation.

**Try these prompts:**

```
What edge cases should I handle for this file upload endpoint that accepts PDFs up to 10MB?
```

```
Review this payment processing function for boundary conditions and error scenarios I might have missed
```

```
Build a coverage matrix for our search API -- it takes a query string, page number, page size, and optional date range filter
```

```
Document the failure modes for our third-party payment gateway integration using the error scenario template
```

```
Audit this form validation logic -- I want to know every gap between what the client checks and what the server checks
```

## Real-World Walkthrough

You are building a REST API for an e-commerce platform and your current sprint includes a `POST /orders` endpoint. The endpoint accepts a JSON body with `customerId` (UUID), `items` (array of objects with `productId`, `quantity`, and `unitPrice`), `shippingAddress` (nested object), and `couponCode` (optional string). You have the happy path working: valid customer, valid products, valid address, no coupon. Time to harden it before code review.

You start by asking Claude: **"Analyze the edge cases for this order creation endpoint"** and paste the request schema.

Claude activates the edge-case-coverage skill and begins with the **coverage matrix**. It maps every top-level and nested field against the five conditions:

| Input | Valid | Empty | Null | Overflow | Malformed |
|---|---|---|---|---|---|
| customerId | existing UUID | `""` | `null` | 256-char string | `"not-a-uuid"` |
| items | 1 valid item | `[]` | `null` | 10,000 items | `[{"garbage": true}]` |
| items[].quantity | 1 | 0 | `null` | `999999999` | `"three"` |
| items[].unitPrice | 9.99 | 0.00 | `null` | `99999999.99` | `-5.00` |
| shippingAddress | complete | `{}` | `null` | all fields max-length | missing required fields |
| couponCode | `"SAVE10"` | `""` | `null` (valid - optional) | 256-char string | SQL injection attempt |

This immediately surfaces cases you had not considered: an empty `items` array (is a zero-item order valid?), a quantity of zero (should it be rejected or silently ignored?), negative unit prices (refund exploit?), and the difference between `null` and `""` for the optional coupon code.

Next, Claude applies the **boundary analysis template** to the numeric fields. For `quantity`:

```
Value: items[].quantity
├── Below min: -1 (negative quantity -- refund attack?)
├── At min: 0 (zero quantity -- valid or rejected?)
├── Just above min: 1 (minimum valid order)
├── Normal: 5
├── Just below max: 99 (assuming stock limit)
├── At max: 100 (business rule limit)
└── Above max: 101 (over stock limit)
```

And for `unitPrice`, the same seven-value analysis reveals that you need to decide: does the server trust the client-supplied price, or validate it against the catalog? If the client sends `unitPrice: 0.01` for a $500 item, is that a bug or a fraud attempt?

Claude then produces the **error scenario documentation** for three failure modes it identified:

**Scenario: Stale coupon code applied to completed order.** Trigger: customer applies a coupon, then takes 30 minutes to submit; coupon expires between apply and submit. Symptoms: order fails with a cryptic 500 error because the coupon validation throws an unhandled exception. Prevention: validate the coupon at order submission time, not just at apply time; return a clear 422 with a message that the coupon has expired. Recovery: customer retries without the coupon or applies a new one.

**Scenario: Concurrent stock depletion.** Trigger: two customers submit orders for the last 3 units of a product simultaneously. Symptoms: both orders succeed, but only 3 units exist; one order cannot be fulfilled. Prevention: use database-level stock reservation with row locking during order creation. Recovery: notify the second customer and offer a backorder or cancellation.

**Scenario: Partial address validation failure.** Trigger: customer submits a shipping address with a valid ZIP code but non-existent city-ZIP combination. Symptoms: order is created but shipment bounces, generating a support ticket days later. Prevention: validate city-ZIP-state consistency at submission time using USPS API. Recovery: flag order for address confirmation before shipping.

Finally, Claude runs through the **anti-pattern audit** on your existing code. It flags that your error handling catches `OrderCreationException` but not `DatabaseTimeoutException` (silent failure), that you validate `items` is not null but not that it is non-empty (happy-path-only testing), and that you pass the coupon code directly to a database query without sanitization (assuming valid input).

You now have a concrete list of 20+ edge cases, three documented failure scenarios with prevention strategies, and three specific code gaps to fix -- all before requesting code review. You hand the coverage matrix to your testing workflow and the error scenarios to your team's runbook.

## Usage Scenarios

### Scenario 1: Hardening an API endpoint before release

**Context:** You have a working `POST /users` endpoint and want to ensure every input is properly validated before shipping.

**You say:** "Build a coverage matrix for this user registration endpoint -- it accepts name, email, password, and date of birth"

**The skill provides:**
- Coverage matrix with 5 conditions (valid, empty, null, overflow, malformed) for each of the 4 fields
- Boundary analysis for date of birth (future dates, dates before 1900, today, age < 13)
- Validation checklist highlighting the six dimensions to verify per field
- Anti-pattern check against your existing validation code

**You end up with:** A 20+ item checklist of specific test cases to write, with exact test values for each.

### Scenario 2: Documenting failure modes for on-call engineers

**Context:** Your payment processing service has had three incidents in the past month, each requiring a different engineer to reverse-engineer the failure from logs.

**You say:** "Document the error scenarios for our Stripe integration -- timeout, card declined, duplicate charge, webhook delivery failure"

**The skill provides:**
- Error scenario template for each failure mode with trigger, symptoms, root cause, prevention, and recovery
- State validation checklist for the payment state machine (pending, authorized, captured, refunded)
- Network edge cases specific to webhook-based architectures (delayed delivery, out-of-order events, replay attacks)

**You end up with:** Runbook-quality documentation that any on-call engineer can use to diagnose and resolve each failure mode without reading source code.

### Scenario 3: Pre-review self-audit on a pull request

**Context:** You have a PR open for a file upload feature and want to catch issues before your reviewer does.

**You say:** "What edge cases am I missing in this file upload handler?" and paste the code.

**The skill provides:**
- Boundary analysis for file size (0 bytes, 1 byte, at limit, over limit, exactly at limit)
- Input validation gaps (missing MIME type check, no file extension validation, no path traversal sanitization)
- Resource edge cases (disk full during write, upload interrupted mid-stream, concurrent uploads to same path)
- Anti-pattern audit (silent failure on write error, happy-path-only test coverage)

**You end up with:** A list of specific gaps to fix before requesting review, preventing the back-and-forth of "did you handle X?" comments.

### Scenario 4: Analyzing a state machine for transition edge cases

**Context:** Your order management system has 6 states (created, paid, processing, shipped, delivered, cancelled) and you suspect there are invalid transitions that are not guarded.

**You say:** "Analyze the edge cases in this order state machine -- what transitions could happen that shouldn't?"

**The skill provides:**
- State validation checklist for each transition (e.g., can you cancel a delivered order? Can you ship an unpaid order?)
- Concurrent state change scenarios (two webhooks arrive simultaneously attempting conflicting transitions)
- Error scenarios for each invalid transition with proper error responses
- Coverage matrix of all state pairs showing which transitions are valid, guarded, and unguarded

**You end up with:** A complete state transition table with explicit handling for every cell, including the invalid ones.

## Ideal For

- **Backend developers shipping API endpoints** -- the coverage matrix catches input validation gaps that code reviews systematically miss
- **Teams with on-call rotations** -- the error scenario template produces documentation that reduces mean-time-to-resolution for production incidents
- **Developers doing pre-review self-audits** -- the anti-pattern checklist catches the five most common gaps before the reviewer sees the code
- **Security-conscious teams** -- boundary analysis surfaces injection, overflow, and privilege-escalation vectors at design time rather than in a pentest report
- **Junior developers learning defensive programming** -- the six-category taxonomy provides a mental model for thinking about failure that transfers across any codebase

## Not For

- **Writing the actual test code** -- this plugin identifies *what* to test, not *how* to test it. Hand the output to [test-driven-development](../test-driven-development/) or [testing-framework](../testing-framework/) for implementation
- **Performance testing and load analysis** -- resource boundaries (disk, memory, connections) are covered, but systematic load testing is a different discipline. Use dedicated load-testing tools
- **Business rule validation** -- this plugin identifies *technical* edge cases (null, overflow, timeout). Whether a business rule like "users must be 18+" is correct is a product question, not an edge case question

## How It Works Under the Hood

The plugin is a single-skill architecture with no references, hooks, or MCP dependencies. The SKILL.md contains six structured sections that Claude applies sequentially:

1. **Edge Case Categories** -- Claude classifies the input space into six categories (boundary, input, state, resource, network, permission) and identifies which categories apply to the user's specific code
2. **Boundary Analysis** -- For each numeric or string field, Claude applies the seven-value template (below min, at min, just above, normal, just below max, at max, above max)
3. **Coverage Matrix** -- Claude builds a table mapping every identified field against five test conditions (valid, empty, null, overflow, malformed)
4. **Validation Checklist** -- Claude walks through the six input dimensions and four state dimensions, checking each against the existing code
5. **Error Scenario Template** -- For each identified failure mode, Claude fills in the five-field template (trigger, symptoms, root cause, prevention, recovery)
6. **Anti-Pattern Audit** -- Claude checks the code against the five common defensive-programming mistakes

The skill is designed to pair with downstream plugins: its output (a list of edge cases) is the input to test-driven-development (which writes the tests) or code-review (which verifies the cases are covered).

## Related Plugins

- **[Test Driven Development](../test-driven-development/)** -- Takes the edge case list and implements tests using the Red-Green-Refactor cycle
- **[Testing Framework](../testing-framework/)** -- Test infrastructure setup and suite authoring across multiple languages
- **[Code Review](../code-review/)** -- Multi-agent swarm review covering security, performance, style, and test coverage
- **[Consistency Standards](../consistency-standards/)** -- Naming conventions and taxonomy standards for uniform documentation

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
