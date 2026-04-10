# Skill Creator

> **v1.1.19** | Development | 21 iterations

Comprehensive skill creation framework combining philosophy-first design, evidence-based prompting, progressive disclosure, anti-pattern prevention, and enterprise-grade workflows.

## What Problem Does This Solve

A comprehensive framework for creating high-quality Claude Code skills that encode domain expertise, follow evidence-based prompting principles, and leverage progressive disclosure architecture.

## When to Use This Skill

Create high-quality Claude Code skills using philosophy-first design, evidence-based prompting, progressive disclosure, and anti-pattern prevention. Use when creating skills, building skills, designing skills, reviewing skill quality, building skills from documentation, or applying skill best practices.

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

- **Philosophy: Skills as Mental Frameworks**
- **When to Use This Skill**
- **Quick Start: Creating a Skill**
- **Skill Structure**
- **SKILL.md Template**
- **When to Use**
- **Philosophy: [Core Mental Framework]**
- **Core Instructions**

## Key Capabilities

- **Phase 1 (~100 tokens)**
- **Phase 2 (<5k tokens)**
- **Phase 3 (as needed)**
- **Skill**
- **Subagent**
- **MCP**

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

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 49 production-grade plugins for Claude Code.
