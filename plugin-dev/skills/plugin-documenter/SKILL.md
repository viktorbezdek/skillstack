---
name: plugin-documenter
description: Generates comprehensive documentation for any Claude Code plugin by fetching and analyzing all source files. Use when you need to document a Claude plugin, write a plugin README, explain how a plugin works, generate plugin usage guides, create plugin tutorials, analyze a plugin architecture for documentation, or produce installation and setup instructions. Takes a GitHub URL or local path, fetches all plugin files, maps the component architecture, identifies real use-case scenarios from skill descriptions and reference content, and produces a complete documentation package with problem statement, architecture overview, component-by-component guide, realistic usage scenarios, installation instructions, and cross-reference map. NOT for building plugins (use plugin-architecture), NOT for validating plugin structure (use plugin-validation), NOT for evaluating plugin activation (use plugin-evaluation).
---

# Plugin Documenter

> **The best plugin documentation answers three questions in this order: what problem does this solve, how do I install it, and what can I do with it.** Everything else is reference material that users look up after they've decided to install. This skill enforces that order.

---

## When to use this skill

- You found a Claude Code plugin on GitHub and want to understand what it does
- You built a plugin and need to write or rewrite its README
- You're evaluating whether to install a plugin and want a thorough breakdown first
- You want to generate a tutorial for a plugin you or someone else authored
- You need to document a plugin for a team that will be using it

## When NOT to use this skill

- **Building a new plugin** → use `plugin-architecture` + `plugin-composition`
- **Validating plugin structure** → use `plugin-validation`
- **Evaluating activation quality** → use `plugin-evaluation`
- **Writing a single SKILL.md** → use `skill-creator`

---

## How to invoke

```
/plugin-dev:plugin-documenter https://github.com/user/repo/tree/main/plugin-name
```

Or for a local plugin:

```
/plugin-dev:plugin-documenter ./path/to/plugin
```

Or natural language:

```
Document the plugin at https://github.com/user/repo
Write detailed docs for the cloud-finops plugin
```

---

## The documentation process

### Step 1 — Fetch and inventory

Fetch every file that belongs to the plugin. For GitHub URLs, use web-fetch or git clone. For local paths, read directly.

**Files to collect:**

| File | Required | Purpose |
|---|---|---|
| `.claude-plugin/plugin.json` | Yes | Manifest — name, version, description, author |
| `README.md` | Yes | Existing documentation (may be sparse or outdated) |
| `skills/*/SKILL.md` | Yes | Each skill's frontmatter + body |
| `skills/*/references/*.md` | If present | Deep reference content per skill |
| `skills/*/evals/*.json` | If present | What the skill is tested against |
| `hooks/hooks.json` | If present | Hook configuration |
| `hooks/scripts/*.sh` | If present | Hook implementations |
| `.mcp.json` | If present | MCP server configuration |
| `agents/*.md` | If present | Subagent definitions |
| `commands/*.md` | If present | Slash command definitions |
| `scripts/*.py` or `scripts/*.sh` | If present | Runnable tooling |
| `CHANGELOG.md` | If present | Version history |

**Output:** a file inventory table with path, type, and size for each file.

### Step 2 — Analyze architecture

From the inventory, determine:

1. **Plugin shape** — single-skill, multi-skill, hooks-only, composed (skills + hooks + MCP)?
2. **Component count** — how many skills, hooks, MCP tools, subagents, commands?
3. **Component relationships** — which skills reference each other? Do hooks complement specific skills? Does a skill instruct the model to call MCP tools?
4. **Progressive disclosure structure** — how deep is the reference tree? What's the SKILL.md body vs reference split?
5. **Scripts and tooling** — what runnable tools does the plugin ship? What are their CLIs?

**Output:** an architecture summary with a component diagram (text-based).

### Step 3 — Extract the problem statement

Read ALL skill descriptions (frontmatter) and the plugin.json description. From these, synthesize:

- **What problem does this plugin solve?** — in plain language, for someone who has never heard of it
- **Who is it for?** — what kind of user benefits
- **What does the world look like WITHOUT this plugin?** — the pain it eliminates
- **What does the world look like WITH it?** — the outcome it enables

Do NOT copy the frontmatter description verbatim. The frontmatter is written for Claude's activation engine. The problem statement is written for humans deciding whether to install.

### Step 4 — Map real use-case scenarios

For each skill in the plugin, read:
- The frontmatter trigger phrases (the "use when" clauses)
- The SKILL.md body (the methodology, phases, checklists)
- The references (deep domain content)
- The evals (if present — eval queries are excellent proxies for real user scenarios)

From these, construct **3-5 realistic scenarios per skill**:

```
Scenario: "You just inherited a legacy codebase and need to add a feature safely"
1. User says: "I inherited this codebase and I'm afraid to touch it"
2. The skill activates and provides: [specific methodology from the skill body]
3. User follows the phases: [step-by-step from the skill]
4. Output: [what the user has at the end]
```

Scenarios must be **specific and realistic** — not "user asks about X and gets an answer." Show the journey, not just the trigger.

### Step 5 — Write installation instructions

From the plugin.json and the plugin's location:

```markdown
## Installation

Add the marketplace and install:

```
/plugin marketplace add OWNER/REPO
/plugin install PLUGIN-NAME@MARKETPLACE-ID
```

### Prerequisites

[List any dependencies — other plugins that should be installed alongside, runtime requirements]

### Verify installation

After installing, test with:
```
[A realistic query that should trigger the plugin's primary skill]
```
```

If the plugin is part of a marketplace (like skillstack), use the marketplace install flow. If it's standalone, use the direct GitHub install.

### Step 6 — Generate the documentation package

Assemble everything into a structured document:

```markdown
# [Plugin Name]

> [One-sentence value proposition — what problem, for whom]

## What Problem Does This Solve

[Problem statement from Step 3 — 2-3 paragraphs, plain language]

## Installation

[From Step 5]

## What's Inside

[Architecture overview from Step 2 — component table, relationships]

### [Component 1 Name]
[What it does, when it activates, what methodology it provides]

### [Component 2 Name]
[...]

## Usage Scenarios

### Scenario 1: [Title]
[Full scenario from Step 4]

### Scenario 2: [Title]
[...]

## Reference Guide

[For each skill: trigger phrases, key concepts, reference file summaries]

## How It Works Under the Hood

[Architecture from Step 2 — how components relate, data flow, progressive disclosure]

## Version History

[From CHANGELOG.md if present]
```

### Step 7 — Quality check

Before delivering, verify:

- [ ] Problem statement doesn't use jargon the target audience wouldn't know
- [ ] Installation instructions are copy-pasteable and correct
- [ ] Every skill in the plugin has at least one scenario
- [ ] Scenarios are specific (not "user asks about X")
- [ ] No frontmatter description was copy-pasted as documentation prose
- [ ] Component relationships are documented (not just listed)
- [ ] The document answers "what, why, how to install, how to use" in that order

---

## Output format

By default, the documentation is written as a replacement for the plugin's `README.md`. If the user requests a different format (tutorial, wiki page, blog post), adapt the structure but keep the same content order: problem → install → what's inside → scenarios → reference.

---

## Tips for documenting specific component types

### Skills

Focus on **when it activates** and **what methodology it provides**. The trigger phrases from frontmatter tell you the "when". The SKILL.md body tells you the "what". Don't document the frontmatter — document the behavior.

### Hooks

Focus on **what events they handle** and **what they prevent or automate**. Read `hooks.json` for the event/matcher pairs and the hook scripts for the logic. Common patterns: guardrails (PreToolUse blocks), automation (PostToolUse formats), context injection (SessionStart adds info).

### MCP servers

Focus on **what tools they expose** and **what external systems they connect to**. Read `.mcp.json` for the server config and any tool definitions.

### Scripts

Focus on **CLI usage** and **what they produce**. Show the command, the flags, and example output.

---

## References

This skill uses the analysis framework from `plugin-architecture` (component decision matrix) and the structural knowledge from `plugin-validation` (what a valid plugin looks like) to inform its documentation. It does not duplicate those skills — it applies their frameworks to produce human-readable documentation.

---

> *Plugin-Dev Authoring Toolkit by [Viktor Bezdek](https://github.com/viktorbezdek) — licensed under MIT.*
