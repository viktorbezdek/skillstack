# Edge Case Coverage

> **v1.0.10** | Quality & Testing | 11 iterations

Identify and document boundary conditions, error scenarios, corner cases, and validation requirements.

## What Problem Does This Solve

Code that works on the happy path often silently breaks on empty inputs, maximum values, null fields, expired tokens, or network timeouts — the cases no one thought to specify. This skill provides a systematic catalogue of edge case categories, boundary analysis templates, and validation checklists that make it practical to enumerate and document the full input space before shipping, rather than discovering failures in production.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "What edge cases should I handle for this input field?" | Boundary analysis template with below-min, at-min, normal, at-max, above-max, and special-character cases |
| "Document the error scenarios for this API endpoint" | Error scenario template covering trigger, symptoms, root cause, prevention, and recovery |
| "Review this validation logic for gaps" | Input validation checklist: required, type, format, range, length, allowed characters |
| "Check if we're handling null and undefined correctly" | Edge case categories for null/undefined, wrong type, uninitialized state |
| "We keep getting timeouts — what should we document?" | Resource edge cases: timeout, memory exhaustion, disk full, partial failure |
| "Build a coverage matrix for the user registration form" | Coverage matrix template mapping each input against valid, empty, null, overflow, and malformed scenarios |

## When NOT to Use This Skill

- writing tests

## Installation

```bash
claude install-plugin github:viktorbezdek/skillstack/edge-case-coverage
```

## How to Use

**Direct invocation:**

```
Use the edge-case-coverage skill to ...
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `edge-cases`
- `boundary-conditions`
- `validation`

## What's Inside

- **Edge Case Categories** -- Taxonomy of six category types: boundary, input, state, resource, network, and permission, each with concrete examples.
- **Boundary Analysis** -- Structured templates for numeric and string boundaries showing the seven values to test around any limit (below min, at min, just above, normal, just below max, at max, above max).
- **Error Scenario Template** -- Five-field markdown template (trigger, symptoms, root cause, prevention, recovery) for documenting each failure mode.
- **Validation Checklist** -- Two-section checklist covering input validation (type, format, range, length, characters) and state validation (initialization, resources, permissions, dependencies).
- **Coverage Matrix** -- Tabular format mapping every input field against the five key test conditions: valid, empty, null, overflow, and malformed.
- **Anti-Patterns** -- Common defensive-programming mistakes: happy-path-only testing, ignoring nulls, assuming valid input, missing timeout handling, and silent failures.

## Version History

- `1.0.10` fix(docs+quality): optimize descriptions for api-design, docs, edge-cases, examples, navigation, standards (6e315cf)
- `1.0.9` fix: update plugin count and normalize footer in 31 original plugin READMEs (3ea7c00)
- `1.0.8` fix: change author field from string to object in all plugin.json files (bcfe7a9)
- `1.0.7` fix: rename all claude-skills references to skillstack (19ec8c4)
- `1.0.6` docs: update README and install commands to marketplace format (af9e39c)
- `1.0.5` refactor: restructure all 34 skills into proper Claude Code plugin format (7922579)
- `1.0.4` refactor: make each skill an independent plugin with own plugin.json (6de4313)
- `1.0.3` docs: add detailed README documentation for all 34 skills (7ba1274)
- `1.0.2` refactor: standardize frontmatter and split oversized SKILL.md files (4a21a62)
- `1.0.1` docs: improve helper skill descriptions and add trigger words (9c0d140)

## Related Skills

- **[Code Review](../code-review/)** -- Perform thorough code reviews with multi-agent swarm analysis covering security, performance, style, tests, and document...
- **[Consistency Standards](../consistency-standards/)** -- Establish and maintain naming conventions, taxonomy standards, style guides, and reuse patterns across documentation and...
- **[Test Driven Development](../test-driven-development/)** -- Comprehensive Test-Driven Development skill implementing Red-Green-Refactor cycle across Python, TypeScript, JavaScript,...
- **[Testing Framework](../testing-framework/)** -- Comprehensive testing framework for multiple languages and platforms. Covers unit testing (Rust, TypeScript, PHP, Shell)...

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 49 production-grade plugins for Claude Code.
