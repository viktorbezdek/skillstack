# Example Design

> **v1.0.10** | Documentation | 11 iterations

Design effective code examples, tutorials, and runnable samples with progressive complexity.

## What Problem Does This Solve

Code examples in documentation often dump an intimidating wall of production code at the reader, use meaningless `foo`/`bar` variable names, omit imports, and never show expected output -- so developers cannot tell whether the code actually works or what it should produce. This skill provides a structured approach to building examples that start minimal and layer in complexity progressively, with a quality checklist that catches the most common pitfalls before they frustrate users.

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install example-design@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention the triggers below, or you can invoke it explicitly.

## What's Inside

Single-skill plugin with one SKILL.md covering six areas:

| Component | What It Provides |
|---|---|
| **Example Types** | Four-row reference table mapping snippet (5-15 lines), complete example (20-50 lines), tutorial (multi-file), and reference app (full project) to their purpose and line-count range |
| **Progressive Complexity** | Five-level ladder from Level 1 (minimal happy path) through configuration, error handling, edge cases, to Level 5 (production-ready) |
| **Example Anatomy** | Four-part structure for any code example: context comment, setup imports, highlighted core concept, and expected output |
| **Quality Checklist** | Six-item checklist verifying that an example is runnable, complete, minimal, commented, realistic, and tested |
| **Tutorial Structure** | Markdown template with time estimate, prerequisites, numbered steps (explanation + code + expected result), and next-steps navigation |
| **Anti-Patterns** | Six common mistakes to avoid: foo/bar names, missing imports, outdated syntax, no expected output, untested code, and unexplained walls of code |

## How to Use

**Direct invocation:**

```
Use the example-design skill to write a code example for this API method
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

`examples` · `tutorials` · `samples`

## Usage Scenarios

**1. Writing a quickstart for an open-source library.** You just built a CLI tool and need a quickstart in the README. Use the tutorial structure template to produce a 10-minute walkthrough with prerequisites, numbered steps each showing code and expected output, and a next-steps section pointing to the full API reference.

**2. Reviewing existing docs for example quality.** Your SDK documentation has 30 code examples and you suspect many are broken. Run each through the quality checklist: does it include all imports? Can a developer copy-paste and run it? Does it show expected output? Flag the ones that fail and prioritize fixes.

**3. Building a progressive tutorial for a complex feature.** Your authentication library has a simple use case (API key) and a complex one (OAuth2 with refresh tokens). Use the progressive complexity ladder: Level 1 shows API key auth in 10 lines, Level 2 adds config options, Level 3 adds error handling, Level 4 covers token expiry edge cases, Level 5 shows the production-ready implementation.

**4. Deciding what type of example to write.** You have a feature that can be demonstrated in a snippet but the PM wants "a full tutorial." Use the example types table to match the purpose to the right format -- a snippet for a single concept, a complete example for a working demonstration, or a tutorial only when step-by-step guidance adds genuine value.

**5. Cleaning up examples that use foo and bar.** Your legacy docs use `foo`, `bar`, and `baz` throughout. Apply the anti-patterns reference to systematically replace them with realistic names (`createUser`, `orderTotal`, `invoiceId`) and add the missing context comments and expected output that make examples self-documenting.

## When to Use / When NOT to Use

**Use when:** You are creating code examples, quickstart guides, tutorials, sample code, or any runnable demonstration content for documentation.

**Do NOT use for:** Generating full reference documentation or API docs -- use [documentation-generator](../documentation-generator/) instead. This skill is specifically about the example code within documentation, not the documentation structure itself.

## Related Plugins in SkillStack

- **[Documentation Generator](../documentation-generator/)** -- Comprehensive documentation generation for repositories of any size

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
