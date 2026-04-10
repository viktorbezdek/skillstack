# Consistency Standards

> **v1.0.10** | Quality & Testing | 11 iterations

Establish and maintain naming conventions, taxonomy standards, style guides, and reuse patterns across documentation and code.

## What Problem Does This Solve

Projects that grow without consistent naming and terminology develop synonym sprawl — the same concept called "user," "account," and "customer" in different parts of the codebase, documentation, and UI, confusing both developers and end users. Without DRY patterns for shared content, the same definitions get copy-pasted and drift out of sync. This skill provides concrete naming conventions, glossary templates, voice and tone guidelines, and content reuse patterns to eliminate inconsistency before it becomes technical debt.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "What naming convention should we use for TypeScript variables, CSS classes, and database columns?" | Case style reference table mapping camelCase, PascalCase, snake_case, kebab-case, and SCREAMING_SNAKE to their appropriate contexts |
| "Our docs use 'click', 'press', 'tap', and 'select' interchangeably — how do we standardize?" | Glossary template with Term / Definition / Do Not Use columns for establishing authoritative terminology |
| "The tone in our error messages is inconsistent — sometimes angry, sometimes apologetic" | Voice and tone guide with examples per context (instructions, errors, success states) |
| "We're duplicating the same authentication section across five different pages" | Single-source content reuse patterns including snippets, variables, conditionals, and include directives |
| "I need to audit our codebase and docs for consistency violations" | Style checklist covering capitalization, date formats, UI element names, voice, glossary compliance, and code style |
| "What anti-patterns should I look for when reviewing our style guide adherence?" | Anti-pattern catalog covering synonym sprawl, capitalization drift, mixed voice, and orphaned content |

## Installation

```bash
claude install-plugin github:viktorbezdek/skillstack/consistency-standards
```

## How to Use

**Direct invocation:**

```
Use the consistency-standards skill to ...
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `naming`
- `conventions`
- `style-guide`

## What's Inside

- **Naming Conventions** -- Case style table mapping five conventions to their appropriate contexts, plus file naming pattern with type-name-variant structure
- **Terminology Standards** -- Glossary template with preferred term, definition, and prohibited synonyms; voice and tone guide with context-specific examples
- **Content Reuse Patterns** -- Single-source component types (snippet, variable, conditional, template) and DRY documentation syntax for includes and variables
- **Style Checklist** -- Six-point audit checklist covering capitalization, date formats, UI element names, voice consistency, glossary compliance, and code style alignment
- **Anti-Patterns** -- Four consistency failure modes (synonym sprawl, inconsistent capitalization, mixed voice, orphaned content) with identification criteria

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
- **[Edge Case Coverage](../edge-case-coverage/)** -- Identify and document boundary conditions, error scenarios, corner cases, and validation requirements.
- **[Test Driven Development](../test-driven-development/)** -- Comprehensive Test-Driven Development skill implementing Red-Green-Refactor cycle across Python, TypeScript, JavaScript,...
- **[Testing Framework](../testing-framework/)** -- Comprehensive testing framework for multiple languages and platforms. Covers unit testing (Rust, TypeScript, PHP, Shell)...

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 49 production-grade plugins for Claude Code.
