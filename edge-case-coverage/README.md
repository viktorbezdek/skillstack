# Edge Case Coverage

> Systematically identify and document boundary conditions, error scenarios, corner cases, and validation requirements for robust software.

## Overview

Most software bugs live at the boundaries -- the empty string, the null value, the timeout, the off-by-one error. Developers naturally focus on the "happy path" during implementation, leaving edge cases as the primary source of production incidents. This skill provides a systematic framework for identifying, categorizing, and handling every boundary condition before it becomes a customer-facing bug.

The Edge Case Coverage skill is designed for developers writing new features, QA engineers designing test plans, technical writers documenting API behavior, and anyone reviewing code for robustness. It provides structured checklists, coverage matrices, and scenario templates that ensure no category of edge case is overlooked.

As part of the SkillStack collection, this skill is frequently loaded by other skills including documentation-generator (for troubleshooting and API docs), debugging (for systematic issue investigation), and frontend-design (for form validation and error states). It serves as a foundational quality layer across the entire toolkit.

## What's Included

This skill is a focused methodology skill contained in a single `SKILL.md` file. It does not include separate references, scripts, templates, or examples directories -- all content is self-contained in the skill definition, providing concise, immediately actionable frameworks.

## Key Features

- Six-category edge case taxonomy (Boundary, Input, State, Resource, Network, Permission)
- Numeric boundary analysis framework (below min, at min, just above min, normal, just below max, at max, above max)
- String boundary analysis (empty, single char, max length, over max, special chars, Unicode)
- Structured error scenario template (trigger, symptoms, root cause, prevention, recovery)
- Input validation checklist covering required fields, types, formats, ranges, lengths, and allowed characters
- State validation checklist covering initialization, resource availability, permissions, dependencies, and conflicts
- Coverage matrix pattern for tracking validation completeness across all inputs and edge case types
- Anti-pattern identification to catch common shortcuts (happy path only, ignoring nulls, silent failures)

## Usage Examples

**Design edge cases for a new API endpoint:**
```
I'm building a user registration endpoint. What edge cases should I handle?
```
Walks through each of the six categories (Boundary, Input, State, Resource, Network, Permission) applied to registration, generating a comprehensive coverage matrix for fields like email, password, and username.

**Review code for missing edge cases:**
```
Review this function for edge cases I might have missed.
```
Applies the boundary analysis framework to each parameter, checks for null/undefined handling, verifies timeout and error handling, and identifies any silent failure patterns.

**Create a validation test plan:**
```
Generate a test plan covering all edge cases for our payment processing module.
```
Produces a coverage matrix with every input field tested against valid, empty, null, overflow, and malformed scenarios, plus state and resource edge cases specific to payment processing.

**Document error scenarios:**
```
Document the error scenarios for our file upload feature.
```
Uses the error scenario template to create structured documentation for each failure mode: what triggers it, what the user sees, why it happens, how to prevent it, and how to recover.

**Audit existing validation:**
```
Audit the validation in our form components and identify gaps.
```
Applies the input validation checklist and anti-pattern detection to identify missing checks, inconsistent validation, and silent failure modes across form components.

## Quick Start

1. **Identify your inputs** -- list every parameter, field, or external dependency your code handles.

2. **Apply the boundary analysis** for each input:
   - For numbers: test below min, at min, just above min, normal, just below max, at max, above max
   - For strings: test empty, single char, max length, over max, special chars, Unicode

3. **Walk through the six categories** for each input:
   - Boundary: min/max/empty values
   - Input: null, undefined, wrong type
   - State: uninitialized, concurrent, stale
   - Resource: timeout, no memory, disk full
   - Network: offline, slow, partial failure
   - Permission: unauthorized, expired, revoked

4. **Build a coverage matrix** tracking which edge cases are tested for each input.

5. **Check for anti-patterns**: happy path only testing, ignoring nulls, assuming valid input, missing timeout handling, and silent failures.

## Related Skills

- **debugging** -- Use edge case knowledge to quickly identify root causes of boundary-related bugs
- **documentation-generator** -- Document edge cases in API references and troubleshooting guides
- **example-design** -- Include edge case handling in progressive code examples
- **frontend-design** -- Apply boundary validation to form inputs and UI state management

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) — `claude plugin add github:viktorbezdek/skillstack/edge-case-coverage` -- 34 production-grade skills for Claude Code.
