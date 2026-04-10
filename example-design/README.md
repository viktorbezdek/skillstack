# Example Design

> **v1.0.10** | Documentation | 11 iterations

Design effective code examples, tutorials, and runnable samples with progressive complexity.

## What Problem Does This Solve

Code examples in documentation often dump an intimidating wall of production code at the reader, use meaningless `foo`/`bar` variable names, omit imports, and never show expected output — so developers cannot tell whether the code actually works or what it should produce. This skill provides a structured approach to building examples that start minimal and layer in complexity progressively, with a quality checklist that catches the most common pitfalls before they frustrate users.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "Write a code example for this API method" | Example anatomy template: context comment, setup imports, highlighted core line, and expected output |
| "Create a quickstart tutorial for this library" | Tutorial structure with time estimate, prerequisites, numbered steps with expected results, and next-steps links |
| "The examples in our docs are too complex for beginners" | Progressive complexity ladder from Level 1 (happy path only) to Level 5 (production-ready with error handling) |
| "What type of example should I use here — snippet or full app?" | Example types table mapping purpose and appropriate length to snippet, complete example, tutorial, and reference app |
| "Review these code samples for quality" | Quality checklist: runnable, complete imports, minimal scope, realistic names, commented key lines, verified output |
| "Our examples use foo and bar everywhere — how do we fix that?" | Anti-patterns list covering unrealistic names, missing imports, outdated syntax, no expected output, and untested code |

## When NOT to Use This Skill

- generating full

## Installation

```bash
claude install-plugin github:viktorbezdek/skillstack/example-design
```

## How to Use

**Direct invocation:**

```
Use the example-design skill to ...
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `examples`
- `tutorials`
- `samples`

## What's Inside

- **Example Types** -- Four-row reference table mapping snippet, complete example, tutorial, and reference app to their purpose and appropriate line-count range.
- **Progressive Complexity** -- Five-level ladder from minimal happy path through configuration, error handling, edge cases, and production-ready code.
- **Example Anatomy** -- Four-part structure for any code example: context comment, setup imports, highlighted core concept, and expected output.
- **Quality Checklist** -- Six-item checklist verifying that an example is runnable, complete, minimal, commented, realistic, and tested.
- **Tutorial Structure** -- Markdown template with time estimate, prerequisites, numbered steps (explanation + code + expected result), and next-steps navigation.
- **Anti-Patterns** -- Six common mistakes to avoid: foo/bar names, missing imports, outdated syntax, no expected output, untested code, and unexplained walls of code.

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

- **[Documentation Generator](../documentation-generator/)** -- Generate comprehensive documentation for repositories of any size - from small libraries to large monorepos. Creates bot...

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 49 production-grade plugins for Claude Code.
