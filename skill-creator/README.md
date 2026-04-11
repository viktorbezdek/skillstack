# Skill Creator

> **v1.1.19** | Development | 21 iterations

Comprehensive skill creation framework combining philosophy-first design, evidence-based prompting, progressive disclosure, anti-pattern prevention, and enterprise-grade workflows.

## What Problem Does This Solve

Most Claude Code skills are written as checklists or template dumps that activate too broadly, trigger on the wrong keywords, or give Claude procedures without the mental framework to apply them intelligently. Skills built without explicit philosophy, anti-patterns, and precise activation descriptions produce inconsistent results and false activations. This skill provides the methodology to create skills that encode expert knowledge, activate precisely when needed, and guide Claude's thinking rather than just constraining its output.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "Create a new skill from scratch for this domain" | 8-phase Skill Forge methodology from schema definition through adversarial testing, plus init_skill.py scaffold script |
| "Turn this API documentation into a skill" | Documentation-to-skill workflow: extract patterns, warnings, and best practices, then structure with progressive disclosure |
| "My skill activates when it shouldn't" | Description field engineering formula ([What] [Keywords] NOT for [Exclusions]) with a progression from bad to good examples |
| "Review this skill for quality issues" | Skill Review Checklist with CRITICAL (description, line limit, file refs, activation tests) and HIGH PRIORITY items |
| "How should I structure a skill that has a lot of content?" | Progressive disclosure architecture: core in SKILL.md (<500 lines), details in /references/, code in /scripts/ |
| "Score this skill's quality" | analyze_skill.py script producing a 0-100 quality score, plus the heuristics it checks against |

## When NOT to Use This Skill

- prompt engineering -- use [prompt-engineering](../prompt-engineering/) instead

## Installation

```bash
claude install-plugin github:viktorbezdek/skillstack/skill-creator
```

## How to Use

**Direct invocation:**

```
Use the skill-creator skill to ...
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `skill`
- `plugin`
- `creation`
- `framework`

## What's Inside

- **Philosophy: Skills as Mental Frameworks** -- Core principle distinguishing Constraining (templates, rigid rules) from Unlocking (frameworks, mental models) approaches, establishing the four pillars: Philosophy Before Procedure, Anti-Patterns as Guidance, Progressive Disclosure, and Shibboleths.
- **Quick Start: Creating a Skill** -- Two-track workflow: Minimal (5-step for simple skills) and Full 8-phase methodology for production skills, with time estimates per phase.
- **Skill Structure** -- Mandatory and optional file layout with the rule to only add files that SKILL.md explicitly references.
- **SKILL.md Template** -- Complete template with frontmatter, When to Use / When NOT to Use, Philosophy section, Core Instructions, Anti-Patterns, and Variation Guidance sections.
- **Description Field Engineering** -- Step-by-step formula for writing activation descriptions that hit 90%+ precision, with a Bad/Better/Good progression example.
- **Core Principles** -- Three technical principles: Progressive Disclosure (three loading phases), Anti-Pattern Detection (with format), and Shibboleth Encoding (novice vs. expert knowledge distinctions).
- **Common Anti-Patterns in Skill Creation** -- Five named anti-patterns: Reference Illusion, Description Soup, Template Theater, The Everything Skill, and Orphaned Sections.
- **Scripts Reference** -- Command-line tools for initializing, validating, packaging, analyzing, and upgrading skills, plus documentation extraction scripts.
- **Quality Heuristics** -- Ten-item checklist and target score of 70+/100 on analyze_skill.py for an effective skill.

## Version History

- `1.1.19` fix(meta): optimize descriptions for prompt-engineering and skill-creator (a9056e6)
- `1.1.18` fix(skill-creator): repair broken cross-references to non-existent skills (d1b0a7e)
- `1.1.17` fix: change author field from string to object in all plugin.json files (bcfe7a9)
- `1.1.16` fix: rename all claude-skills references to skillstack (19ec8c4)
- `1.1.15` refactor: remove old file locations after plugin restructure (a26a802)
- `1.1.14` docs: update README and install commands to marketplace format (af9e39c)
- `1.1.13` refactor: restructure all 34 skills into proper Claude Code plugin format (7922579)
- `1.1.12` refactor: make each skill an independent plugin with own plugin.json (6de4313)
- `1.1.11` fix: resolve broken links, flatten faber scripts, add validate-patterns.py (4647f46)
- `1.1.10` fix: make all shell scripts executable and fix Python syntax errors (61ac964)

## Related Skills

- **[Api Design](../api-design/)** -- Comprehensive API design skill for REST, GraphQL, gRPC, and Python library architectures. Design endpoints, schemas, aut...
- **[Debugging](../debugging/)** -- Comprehensive debugging skill combining systematic debugging methodology, browser DevTools automation, E2E testing with ...
- **[Frontend Design](../frontend-design/)** -- Comprehensive Frontend Design (UI/UX) skill combining UI design systems, component libraries, CSS/Tailwind styling, acce...
- **[Gws Cli](../gws-cli/)** -- Google Workspace CLI (gws) skill for managing Drive, Gmail, Sheets, Calendar, Docs, Chat, Tasks, and 11 more Workspace A...
- **[Mcp Server](../mcp-server/)** -- Comprehensive MCP (Model Context Protocol) server development skill. Build, configure, and manage MCP servers using Pyth...

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 50 production-grade plugins for Claude Code.
