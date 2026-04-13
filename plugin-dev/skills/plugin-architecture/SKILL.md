---
name: plugin-architecture
description: Decides which Claude Code extension type to use for a given capability — skill, hook, MCP server, subagent, or slash command — and designs the plugin.json manifest around that decision. Use when designing a plugin, planning plugin structure, choosing between skill vs hook vs mcp, setting up plugin composition, laying out plugin components, or refactoring an existing plugin whose decomposition feels wrong. Covers the five extension types, the decision matrix (when each fits), plugin.json schema reference, directory layout, namespacing conventions, and worked examples from real plugins. NOT for the content of a single component — use skill-foundry, plugin-hooks, mcp-server, or plugin-composition for deep dives.
---

# Plugin Architecture

> **The decomposition matters more than any single component.** A plugin that puts the wrong capability in the wrong component fails silently — the skill never triggers, the hook blocks everything, the MCP tool is unreachable. This skill is the first decision you make, before writing any content.

---

## When to use this skill

- You have a plugin idea and don't know how to split it across components
- You're about to write a SKILL.md but wonder if it should be a hook instead
- An existing plugin has a skill that never triggers, and you suspect the capability belongs in a different component type
- You need to author `plugin.json` from scratch and want the full schema
- You're reviewing a plugin structure before shipping it

## When NOT to use this skill

- **Writing a single skill's content** → `skill-foundry` (advanced framework) or Anthropic's bundled `skill-creator`
- **Writing hook scripts** → `plugin-hooks`
- **Building an MCP server** → `mcp-server`
- **Integrating multiple components inside one plugin** → `plugin-composition`
- **Evaluating whether the plugin works** → `plugin-evaluation`
- **Validating structural correctness** → `plugin-validation`

---

## The five extension types

| Type | What it is | Fires when | Best for |
|---|---|---|---|
| **Skill** | A `SKILL.md` with frontmatter + optional references/scripts | Model chooses based on description + query match | Procedures, methodologies, domain expertise |
| **Hook** | An event handler in `hooks/hooks.json` | A specific event fires (tool call, session start, file change) | Guardrails, automation, context injection, reactive behavior |
| **MCP server** | A process exposing tools via Model Context Protocol | Claude calls a tool from the server | Access to external systems, APIs, databases, custom tooling |
| **Subagent** | An agent definition in `agents/<name>.md` | `Task(subagent_type="<name>")` is called | Long-running specialized tasks with dedicated context |
| **Slash command** | A markdown file in `commands/<name>.md` | User types `/<name>` | User-triggered workflows and one-shots |

A plugin may contain any combination of these — or all five. The question is: **which capability goes where?**

---

## The decision matrix (cheat sheet)

Full version: `references/component-decision-matrix.md`. Quick version:

```
Is the capability triggered by the model's judgment of a user query?
  YES → Skill (lives in skills/<name>/SKILL.md, triggered by description match)
  NO  → keep going ↓

Is it triggered by an event (tool call, session start, file change)?
  YES → Hook (lives in hooks/hooks.json)
  NO  → keep going ↓

Does it need to communicate with an external system (API, DB, service)?
  YES → MCP server (lives in .mcp.json + server process)
  NO  → keep going ↓

Is it a long-running, specialized task with its own context window?
  YES → Subagent (lives in agents/<name>.md)
  NO  → keep going ↓

Is it explicitly triggered by the user typing a command?
  YES → Slash command (lives in commands/<name>.md)
  NO  → you don't need a plugin component; use CLAUDE.md or docs
```

**Common mistakes this matrix catches**:

- "I'll write a skill that auto-formats on save" → ❌ that's a hook, not a skill (triggered by event, not by query)
- "I'll write a hook that teaches the model how to debug" → ❌ that's a skill (model-judgment, not event-driven)
- "I'll write a skill that calls our internal API" → ❌ the API call is MCP territory; the methodology around it might be a skill

---

## `plugin.json` manifest

Every plugin has a `.claude-plugin/plugin.json`. Minimum viable:

```json
{
  "name": "my-plugin",
  "version": "1.0.0",
  "description": "One-sentence description of the plugin's purpose",
  "author": {
    "name": "Your Name",
    "url": "https://github.com/you"
  }
}
```

Full schema with every documented field, including `keywords`, `license`, `repository`, `homepage`, `engines`, and optional component overrides, is in `references/manifest-reference.md`.

### Naming rules

- `name` is kebab-case, matches the directory name, matches the skill `name` for single-skill plugins
- No special characters except hyphens
- Namespace collision is real — if two plugins share a name, the later install overrides the earlier one

### Multi-skill plugins

For plugins with more than one skill:

```
my-plugin/
├── .claude-plugin/plugin.json
├── README.md
└── skills/
    ├── skill-one/SKILL.md
    ├── skill-two/SKILL.md
    └── skill-three/SKILL.md
```

The `plugin.json` stays at the plugin root. Each skill has its own `SKILL.md` with its own frontmatter. The validator walks `skills/*/` and reports errors scoped as `plugin/skill`.

---

## Directory layout

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json              # Required
├── README.md                    # Required
├── skills/                      # Optional — if plugin has skills
│   └── <skill-name>/
│       ├── SKILL.md             # Required per skill
│       ├── references/          # Optional — progressive disclosure
│       ├── scripts/             # Optional — deterministic tools
│       ├── evals/               # Recommended — plugin-evaluation format
│       └── fixtures/            # Optional — for scripts/tests
├── hooks/                       # Optional — if plugin has hooks
│   ├── hooks.json               # Hook configuration
│   └── scripts/                 # Hook scripts referenced by hooks.json
├── agents/                      # Optional — if plugin has subagents
│   └── <agent-name>.md
├── commands/                    # Optional — if plugin has slash commands
│   └── <command-name>.md
└── .mcp.json                    # Optional — if plugin ships an MCP server
```

**Rule of thumb**: if you have one component type, keep the structure flat. If you have two or more, follow the directory layout above strictly — mixing conventions is a source of hard-to-debug activation failures.

---

## Real plugin examples

See `references/real-plugin-examples.md` for ≥8 real plugins with their component breakdown and the reasoning behind each decision. Short list:

- **Anthropic `skill-creator`** — single skill, no hooks, no MCP
- **`plugin-dev` (this plugin)** — 7 skills + shared scripts, no hooks, no MCP
- **`skillstack-workflows`** — 9 composed-workflow skills
- **`superpowers`** — skills + subagents for development workflows
- **Community `ralph-wiggum`** — hooks + skills for persistence loops

Each example shows **what they chose, why, and what they could have chosen instead**.

---

## Cross-references

| Goal | Skill to use |
|---|---|
| Write a single good SKILL.md | `skill-foundry` (SkillStack's advanced framework) |
| Author a hooks.json with safe patterns | `plugin-hooks` (this plugin) |
| Build an MCP server | `mcp-server` (skillstack plugin) |
| Compose multiple components safely | `plugin-composition` (this plugin) |
| Evaluate triggering + output | `plugin-evaluation` (this plugin) |
| Validate structure before shipping | `plugin-validation` (this plugin) |

---

## References

| File | Contents |
|---|---|
| `references/component-decision-matrix.md` | Detailed decision matrix with columns ("Is the capability...") and rows per extension type, with worked examples |
| `references/manifest-reference.md` | Full `plugin.json` schema, every field, optional vs required, conventions |
| `references/real-plugin-examples.md` | ≥8 real plugins with their component breakdown and design rationale |

---

> *Plugin-Dev Authoring Toolkit by [Viktor Bezdek](https://github.com/viktorbezdek) — licensed under MIT.*
