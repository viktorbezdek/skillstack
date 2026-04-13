# Edge Case Coverage

> **v1.0.10** | Quality & Testing | 11 iterations

Systematically identify and document boundary conditions, error scenarios, corner cases, and validation requirements before they become production incidents.

## What Problem Does This Solve

Code that works on the happy path silently breaks on empty inputs, maximum values, null fields, expired tokens, or network timeouts -- the cases nobody thought to specify. These gaps are rarely caught during code review because reviewers follow the same mental path the author did. This skill provides a systematic catalogue of edge case categories (boundary, input, state, resource, network, permission), boundary analysis templates, error scenario documentation formats, validation checklists, and coverage matrices that make it practical to enumerate the full input space before shipping.

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install edge-case-coverage@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention the triggers below, or you can invoke it explicitly.

## What's Inside

Single-skill plugin with one SKILL.md covering six areas:

| Component | What It Provides |
|---|---|
| **Edge Case Categories** | Taxonomy of six category types -- boundary, input, state, resource, network, and permission -- each with concrete examples |
| **Boundary Analysis** | Structured templates for numeric and string boundaries showing the seven values to test around any limit (below min, at min, just above, normal, just below max, at max, above max) |
| **Error Scenario Template** | Five-field markdown template (trigger, symptoms, root cause, prevention, recovery) for documenting each failure mode |
| **Validation Checklist** | Two-section checklist covering input validation (type, format, range, length, characters) and state validation (initialization, resources, permissions, dependencies) |
| **Coverage Matrix** | Tabular format mapping every input field against the five key test conditions: valid, empty, null, overflow, and malformed |
| **Anti-Patterns** | Common defensive-programming mistakes: happy-path-only testing, ignoring nulls, assuming valid input, missing timeout handling, and silent failures |

## How to Use

**Direct invocation:**

```
Use the edge-case-coverage skill to analyze this registration form for boundary conditions
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

`edge-cases` · `boundary-conditions` · `validation`

## Usage Scenarios

**1. Auditing an API endpoint before release.** You have a user registration endpoint accepting name, email, and age. Ask the skill to build a coverage matrix and it maps each field against valid, empty, null, overflow, and malformed inputs -- producing a concrete checklist of 15+ cases to verify before the endpoint ships.

**2. Documenting known failure modes for on-call engineers.** A payment processing function has three known failure scenarios (timeout, insufficient funds, duplicate charge). Use the error scenario template to document trigger, symptoms, root cause, prevention, and recovery for each -- producing runbook-quality entries the on-call team can act on.

**3. Reviewing validation logic for gaps.** Your form has client-side validation for email format but you suspect server-side gaps. Run through the validation checklist (required, type, format, range, length, characters) against each field to identify exactly where server-side validation is missing.

**4. Hardening a function that handles user-uploaded files.** Apply the boundary analysis template to file size (0 bytes, 1 byte, at limit, over limit), file name (empty, special characters, path traversal attempts), and file type (valid MIME, spoofed extension, no extension) to enumerate the full input space.

**5. Pre-review self-check on a pull request.** Before requesting review, use the anti-patterns list as a self-audit: are you testing only the happy path? Ignoring null returns from external calls? Assuming the database connection will always be available? Catch these before the reviewer does.

## When to Use / When NOT to Use

**Use when:** You need to identify what could go wrong with an input, a state transition, or a resource dependency -- before it does. Works for form fields, API parameters, file uploads, concurrent access scenarios, permission models, or any code that touches external boundaries.

**Do NOT use for:** Writing the actual tests. Once you have identified the edge cases with this skill, hand the list to [test-driven-development](../test-driven-development/) or [testing-framework](../testing-framework/) to implement the test code.

## Related Plugins in SkillStack

- **[Code Review](../code-review/)** -- Multi-agent swarm code review covering security, performance, style, and test coverage
- **[Consistency Standards](../consistency-standards/)** -- Naming conventions, taxonomy standards, and style guides across documentation
- **[Test Driven Development](../test-driven-development/)** -- Red-Green-Refactor cycle across Python, TypeScript, JavaScript, and more
- **[Testing Framework](../testing-framework/)** -- Test infrastructure setup and suite authoring across multiple languages

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
