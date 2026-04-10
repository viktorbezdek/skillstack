# Testing Framework

> **v1.1.23** | Quality & Testing | 25 iterations

Comprehensive testing framework for multiple languages and platforms. Covers unit testing (Rust, TypeScript, PHP, Shell), E2E testing (Playwright), component testing (React Testing Library), accessibility testing (axe-core), mutation testing, fuzz testing, and CI/CD integration.

## What Problem Does This Solve

Starting a new project or language and not knowing which test framework to pick, how to configure it, or how to structure the first test suite costs days of setup time and often produces fragile configurations. This skill answers the "what framework and how do I set it up" question for Rust, TypeScript/React, PHP/TYPO3, and Bash/Shell, and extends into Playwright E2E, axe-core accessibility testing, mutation testing, and CI/CD integration. Rather than debugging infrastructure, teams can focus on writing tests that actually build deployment confidence.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "Set up testing for my Next.js project from scratch" | Vitest + React Testing Library + Playwright config files and a generated dependency list via scripts |
| "Write unit tests for my Rust async functions" | Rust AAA test templates with tokio, naming conventions, and a test quality analysis script |
| "Add accessibility testing to my React components" | axe-core integration patterns and the a11y-testing reference for WCAG compliance |
| "My TYPO3 extension needs PHPUnit functional tests" | PHPUnit templates for unit and functional tests, database fixture guidance, and GitHub Actions CI workflow |
| "Test my Bash deployment scripts" | ShellSpec BDD templates and BATS TAP-compliant patterns with troubleshooting for common shell test failures |
| "How do I verify my tests actually catch bugs, not just run?" | Mutation testing setup and guidance on what metrics indicate genuine test quality vs. coverage theater |

## Installation

```bash
claude install-plugin github:viktorbezdek/skillstack/testing-framework
```

## How to Use

**Direct invocation:**

```
Use the testing-framework skill to ...
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `testing`
- `playwright`
- `unit-tests`
- `e2e`
- `mutation-testing`

## What's Inside

- **Overview** -- Summary of all supported languages, testing types, and frameworks in one place.
- **When to Use This Skill** -- Trigger phrases and concrete use cases for when to activate this skill vs. related ones.
- **Quick Decision Matrix** -- At-a-glance table mapping technology needs (Rust, Next.js, PHP, Bash, E2E) to the right reference files and templates.
- **Testing Modules** -- Detailed guidance for each platform: Rust unit tests, Playwright E2E, Next.js stack, TYPO3/PHP, Shell script testing, and skill validation testing.
- **Available Scripts** -- Reference table of all automation scripts for test generation, setup, quality analysis, and validation.
- **Reference Documentation** -- Organized index of all reference files covering AAA patterns, naming conventions, anti-patterns, framework-specific guides, accessibility, mutation/fuzz testing, and CI/CD.
- **Templates** -- Ready-to-use configuration and test spec templates for Rust, Playwright, and TYPO3/PHP projects.
- **Examples** -- Complete working test examples for React Vite E2E, Next.js unit/component/E2E, and E2E analysis reports.

## Key Capabilities

- **Unit Testing**
- **E2E Testing**
- **Component Testing**
- **Accessibility Testing**
- **Shell Script Testing**
- **Specialized Testing**

## Version History

- `1.1.23` fix(testing+debugging): optimize descriptions with NOT clauses for disambiguation (b00fc60)
- `1.1.22` fix: update plugin count and normalize footer in 31 original plugin READMEs (3ea7c00)
- `1.1.21` fix: change author field from string to object in all plugin.json files (bcfe7a9)
- `1.1.20` fix: rename all claude-skills references to skillstack (19ec8c4)
- `1.1.19` refactor: remove old file locations after plugin restructure (a26a802)
- `1.1.18` docs: update README and install commands to marketplace format (af9e39c)
- `1.1.17` refactor: restructure all 34 skills into proper Claude Code plugin format (7922579)
- `1.1.16` refactor: make each skill an independent plugin with own plugin.json (6de4313)
- `1.1.15` fix: make all shell scripts executable and fix Python syntax errors (61ac964)
- `1.1.14` docs: add detailed README documentation for all 34 skills (7ba1274)

## Related Skills

- **[Code Review](../code-review/)** -- Perform thorough code reviews with multi-agent swarm analysis covering security, performance, style, tests, and document...
- **[Consistency Standards](../consistency-standards/)** -- Establish and maintain naming conventions, taxonomy standards, style guides, and reuse patterns across documentation and...
- **[Edge Case Coverage](../edge-case-coverage/)** -- Identify and document boundary conditions, error scenarios, corner cases, and validation requirements.
- **[Test Driven Development](../test-driven-development/)** -- Comprehensive Test-Driven Development skill implementing Red-Green-Refactor cycle across Python, TypeScript, JavaScript,...

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 49 production-grade plugins for Claude Code.
