# Test Driven Development

> **v1.1.17** | Quality & Testing | 19 iterations

Comprehensive Test-Driven Development skill implementing Red-Green-Refactor cycle across Python, TypeScript, JavaScript, and Emacs Lisp. Covers pytest, Vitest, Playwright, ERT, and Zod.

## What Problem Does This Solve

Developers who write tests after the fact end up retrofitting tests around code that was never designed to be testable, leading to brittle test suites that break on refactors and fail to catch regressions. TDD inverts the workflow: writing a failing test first forces you to define the expected behavior before you write a single line of implementation, producing code that is inherently modular and verifiable. This skill provides the structured Red-Green-Refactor cycle, language-specific tooling (pytest, Vitest, ERT, Playwright), and coverage analysis to sustain that discipline across a full project.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "I need to implement user authentication using TDD" | Step-by-step Red-Green-Refactor cycle with test-first examples in Python or TypeScript |
| "How do I write pytest tests before writing the function?" | Arrange-Act-Assert structure, fixture setup, and test naming conventions for pytest |
| "Walk me through TDD for a Vitest component test" | Vitest-specific patterns including watch mode, mocking, and test isolation |
| "My unit tests are slow and interdependent" | Test independence principles, fixture strategies, and guidance on eliminating shared mutable state |
| "I need E2E tests for a user signup flow with Playwright" | Playwright workflow patterns and the testing tier model (unit/integration/E2E) |
| "What coverage should I aim for and how do I measure it" | Coverage targets by tier (80-90% unit, critical paths integration), checklist of cases to cover, and scripts to analyze and enforce thresholds |

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install test-driven-development@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention the triggers below, or you can invoke it explicitly.

## How to Use

**Direct invocation:**

```
Use the test-driven-development skill to ...
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `tdd`
- `red-green-refactor`
- `pytest`
- `vitest`

## What's Inside

- **Overview** -- High-level map of what the skill covers: workflow, languages, tiers, frameworks, and quality assurance.
- **Core TDD Principles** -- The Red-Green-Refactor cycle explained with the five key practices (test first, small steps, minimal implementation, frequent refactoring, fast feedback).
- **Test Structure Pattern: Arrange-Act-Assert** -- The canonical three-section test template with annotated Python example.
- **Testing Tiers** -- Unit, integration, and E2E definitions including execution speed targets, isolation requirements, and when each tier runs.
- **Test Coverage Guidelines** -- Coverage targets by tier, checklist of case categories (happy path, edge cases, error conditions, state transitions), and threshold enforcement.
- **Best Practices** -- Test naming conventions, test independence requirements, fast feedback loops, and meaningful assertion patterns.
- **Available Resources** -- Language-specific reference documents (Python, TypeScript, Emacs Lisp, Playwright, Zod), scripts for running and analyzing tests, and boilerplate templates.

## Key Capabilities

- **Unit Tests**
- **Integration Tests**
- **E2E Tests**

## Version History

- `1.1.17` fix(testing+debugging): optimize descriptions with NOT clauses for disambiguation (b00fc60)
- `1.1.16` fix: update plugin count and normalize footer in 31 original plugin READMEs (3ea7c00)
- `1.1.15` fix: change author field from string to object in all plugin.json files (bcfe7a9)
- `1.1.14` fix: rename all claude-skills references to skillstack (19ec8c4)
- `1.1.13` refactor: remove old file locations after plugin restructure (a26a802)
- `1.1.12` docs: update README and install commands to marketplace format (af9e39c)
- `1.1.11` refactor: restructure all 34 skills into proper Claude Code plugin format (7922579)
- `1.1.10` refactor: make each skill an independent plugin with own plugin.json (6de4313)
- `1.1.9` docs: add detailed README documentation for all 34 skills (7ba1274)
- `1.1.8` refactor: standardize frontmatter and split oversized SKILL.md files (4a21a62)

## Related Skills

- **[Code Review](../code-review/)** -- Perform thorough code reviews with multi-agent swarm analysis covering security, performance, style, tests, and document...
- **[Consistency Standards](../consistency-standards/)** -- Establish and maintain naming conventions, taxonomy standards, style guides, and reuse patterns across documentation and...
- **[Edge Case Coverage](../edge-case-coverage/)** -- Identify and document boundary conditions, error scenarios, corner cases, and validation requirements.
- **[Testing Framework](../testing-framework/)** -- Comprehensive testing framework for multiple languages and platforms. Covers unit testing (Rust, TypeScript, PHP, Shell)...

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 50 production-grade plugins for Claude Code.
