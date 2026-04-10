# Code Review

> **v1.1.24** | Quality & Testing | 26 iterations

Perform thorough code reviews with multi-agent swarm analysis covering security, performance, style, tests, and documentation. Analyze PRs, extract and prioritize comments, and generate actionable fix plans.

## What Problem Does This Solve

This skill is a curated merge of four complementary code review skills:

## When to Use This Skill

|.

## Installation

```bash
claude install-plugin github:viktorbezdek/skillstack/code-review
```

## How to Use

**Direct invocation:**

```
Use the code-review skill to ...
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `code-review`
- `security`
- `performance`
- `style`

## What's Inside

- **When to Use**
- **Core Capabilities**
- **Severity Levels**
- **Validation Rules**
- **Success Criteria**
- **Resources Reference**

## Key Capabilities

- **Security Reviewer**
- **Performance Analyst**
- **Style Reviewer**
- **Test Specialist**
- **Documentation Reviewer**
- **Truthfulness**

## Version History

- `1.1.24` fix(testing+debugging): optimize descriptions with NOT clauses for disambiguation (b00fc60)
- `1.1.23` fix: update plugin count and normalize footer in 31 original plugin READMEs (3ea7c00)
- `1.1.22` fix: change author field from string to object in all plugin.json files (bcfe7a9)
- `1.1.21` fix: rename all claude-skills references to skillstack (19ec8c4)
- `1.1.20` refactor: remove old file locations after plugin restructure (a26a802)
- `1.1.19` docs: update README and install commands to marketplace format (af9e39c)
- `1.1.18` refactor: restructure all 34 skills into proper Claude Code plugin format (7922579)
- `1.1.17` refactor: make each skill an independent plugin with own plugin.json (6de4313)
- `1.1.16` fix: resolve broken links, flatten faber scripts, add validate-patterns.py (4647f46)
- `1.1.15` fix: make all shell scripts executable and fix Python syntax errors (61ac964)

## Related Skills

- **[Consistency Standards](../consistency-standards/)** -- Establish and maintain naming conventions, taxonomy standards, style guides, and reuse patterns across documentation and...
- **[Edge Case Coverage](../edge-case-coverage/)** -- Identify and document boundary conditions, error scenarios, corner cases, and validation requirements.
- **[Test Driven Development](../test-driven-development/)** -- Comprehensive Test-Driven Development skill implementing Red-Green-Refactor cycle across Python, TypeScript, JavaScript,...
- **[Testing Framework](../testing-framework/)** -- Comprehensive testing framework for multiple languages and platforms. Covers unit testing (Rust, TypeScript, PHP, Shell)...

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 49 production-grade plugins for Claude Code.
