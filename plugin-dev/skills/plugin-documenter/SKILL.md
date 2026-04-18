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

Inventory all plugin files. For GitHub URLs, use web-fetch or git clone. For local paths, use glob/ls.

**Do NOT read every file yet.** Step 1 is inventory only — listing paths and sizes. Deep reads happen selectively in later steps to control token usage.

**Files to inventory:**

| File | Required | Read depth |
|---|---|---|
| `.claude-plugin/plugin.json` | Yes | Full (small) |
| `README.md` | Yes | Full |
| `CHANGELOG.md` | If present | Full (version history) |
| `skills/*/SKILL.md` | Yes | Full — frontmatter + body |
| `skills/*/references/*.md` | If present | **Title + first blockquote only** (see token strategy below) |
| `skills/*/evals/trigger-evals.json` | If present | Count cases only (`jq length`) |
| `skills/*/evals/evals.json` | If present | Count cases only |
| `skills/*/templates/` | If present | List filenames |
| `skills/*/examples/` | If present | List filenames |
| `skills/*/scripts/` | If present | List filenames |
| `skills/*/fixtures/` | If present | List filenames |
| `hooks/hooks.json` | If present | Full (small) |
| `hooks/scripts/*.sh` | If present | First 5 lines of each |
| `.mcp.json` | If present | Full (small) |
| `agents/*.md` | If present | Frontmatter only |
| `commands/*.md` | If present | First 10 lines |
| `scripts/*.py` or `scripts/*.sh` | If present | First 10 lines + `--help` if available |

**Output:** a file inventory table with path, type, line count, and read-depth note.

### Token efficiency strategy

**The rule: read structure first, content on demand.**

1. **Always read fully:** plugin.json, SKILL.md files, hooks.json, .mcp.json, CHANGELOG.md
2. **Read selectively:** reference files — read only the title and opening blockquote
3. **Read on demand:** deep-read specific references only when needed for scenarios
4. **Never read:** test fixtures, example skill bodies, large script implementations
5. **Count, don't read:** eval files — report counts without reading queries

**For a plugin with N reference files:**
- N=0-5: read all references fully (small plugin)
- N=6-15: read titles + blockquotes, deep-read 2-3 most important
- N=16+: read titles only, deep-read on demand for scenarios

### Step 2 — Analyze architecture

From the inventory, determine:

1. **Plugin shape** — single-skill, multi-skill, hooks-only, composed (skills + hooks + MCP)?
2. **Component count** — how many skills, hooks, MCP tools, subagents, commands?
3. **Component relationships** — which skills reference each other? Do hooks complement specific skills?
4. **Progressive disclosure structure** — how deep is the reference tree?
5. **Scripts and tooling** — what runnable tools does the plugin ship?

**Output:** an architecture summary with a component diagram (text-based).

### Step 3 — Extract the problem statement

Read ALL skill descriptions (frontmatter) and the plugin.json description. Synthesize:

- **What problem does this plugin solve?** — in plain language
- **Who is it for?** — what kind of user benefits
- **What does the world look like WITHOUT this plugin?** — the pain
- **What does the world look like WITH it?** — the outcome

Do NOT copy the frontmatter description verbatim. The frontmatter is written for Claude's activation engine. The problem statement is written for humans deciding whether to install.

### Step 4 — Write "How to Use" with prompt templates

For EACH skill in the plugin, produce a practical usage section with:

1. **What it does** — one paragraph in plain language
2. **Prompt templates** — 3-5 copy-pasteable prompts showing different angles:

```markdown
### How to Use: [skill-name]

**What it does:** [plain language explanation]

**Try these prompts:**

```
Help me design a REST API for a bookstore inventory with CRUD operations
```

```
Review my API — I'm not sure about the pagination approach
```

```
What's the best error response format for a public API?
```
```

**Rules for prompt templates:**
- Show the user's actual words, not the skill name
- Vary the intent: starting fresh, reviewing, specific sub-topic, troubleshooting
- Include context where it helps
- Never include skill invocation syntax — the skill activates from natural language

### Step 5 — Map realistic use-case scenarios

Read the frontmatter trigger phrases, SKILL.md body, references, and evals. Construct **3-5 realistic scenarios per skill**:

```markdown
#### Scenario: Migrating a monolith to microservices

**Context:** You're breaking a Rails monolith into services and need to design
the inter-service API contracts before coding anything.

**You say:** "Help me design the API contracts between our user service and
order service — we need to handle auth tokens and eventual consistency"

**The skill provides:**
- Resource decomposition following REST conventions
- Auth token propagation patterns

**You end up with:** A documented API contract with schemas, error codes, and sequence diagrams.
```

Scenarios must be **specific and grounded** — tied to a real situation a developer/PM/designer would recognize.

### Step 6 — Write installation instructions

From the plugin.json and the plugin's location:

```markdown
## Installation

Add the marketplace and install:

```
/plugin marketplace add OWNER/REPO
/plugin install PLUGIN-NAME@MARKETPLACE-ID
```

### Prerequisites

[List any dependencies]

### Verify installation

After installing, test with:

```
[A realistic query that should trigger the plugin's primary skill]
```
```

### Step 7 — Generate the documentation package

The document follows a **4-layer competence model**. Every layer is mandatory.

```
Layer 1: Awareness     → Title Card + Problem + Solution
Layer 2: Mental Model  → System Map + Component Spotlights
Layer 3: Execution     → Walkthrough + Prompt Patterns
Layer 4: Mastery       → Decision Logic + Edge Cases + Integration Patterns
```

Sections marked (lean) can be shortened for simple single-skill plugins. Sections marked (power) can be omitted for plugins with fewer than 3 components.

---

#### LAYER 1 — AWARENESS

```markdown
# [Plugin Name]

> [One-sentence value proposition — what problem, for whom]
> [Visual hint: N skills, N hooks, N scripts]

## The Problem

[2-3 paragraphs. Describe the pain BEFORE this plugin exists. Be specific:
what goes wrong, how much time is wasted, what mistakes are made. Not "X is hard"
but "without this, teams spend 3 hours doing Y manually and still get Z wrong 40% of the time."]

## The Solution

[2-3 paragraphs. What changes WITH this plugin. Concrete outcomes, not
aspirational claims.]

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| [Pain 1] | [Fix 1] |
| [Pain 2] | [Fix 2] |
| [Pain 3] | [Fix 3] |
| [Pain 4] | [Fix 4] |
| [Pain 5] | [Fix 5] |

## Installation

[Copy-pasteable commands from Step 6]

## Quick Start

[The fastest path to seeing value. 3-5 numbered steps]
```

---

#### LAYER 2 — MENTAL MODEL

```markdown
## System Overview

[Text diagram or table showing components and data flow between them]

## What's Inside

[Component inventory table]

### Component Spotlights

[Repeat for EACH component type:]

#### [Skill Name] (skill)

**What it does:** [plain language]
**Input → Output:** [What user provides → what skill produces]
**When to use:** [specific triggers]
**When NOT to use:** [anti-triggers + what to use instead]

**Try these prompts:**

```
[Prompt 1 — starting fresh]
```

```
[Prompt 2 — reviewing existing work]
```

```
[Prompt 3 — specific sub-topic]
```

**Key references:** [summary table]

#### [Hook Name] (hook)

**Trigger:** [event + matcher]
**What it does:** [concrete behavior]
**Side effects:** [what changes]

#### [Script Name] (script)

**CLI:** `command --flags`
**What it produces:** [output format]
**Typical workflow:** [when you'd run this]
```

---

#### LAYER 3 — EXECUTION

```markdown
## Prompt Patterns

### Good Prompts vs Bad Prompts

| Bad (vague) | Good (specific) |
|---|---|
| "[vague query]" | "[specific query with context]" |

### Prompt Anti-Patterns

- [Anti-pattern 1: what people type that doesn't work, and why]
- [Anti-pattern 2]
- [Anti-pattern 3]

## Real-World Walkthrough

[ONE detailed end-to-end example. 500-1000 words. Show the full system in action.
Structure: Starting situation → Steps 1-N → Final outcome → Gotchas discovered]

## Usage Scenarios

### Scenario 1: [Descriptive title]

**Context:** [The user's situation]
**You say:** "[Exact prompt]"
**The skill provides:** [Bullet list of outputs]
**You end up with:** [Concrete deliverable]
```

---

#### LAYER 4 — MASTERY

```markdown
## Decision Logic

[When does component A activate vs B?]

## Failure Modes & Edge Cases

| Failure | Symptom | Recovery |
|---|---|---|
| [Error 1] | [What user sees] | [How to fix] |

## Anti-Patterns

- [Overusing the skill when a simpler approach works]
- [Misplacing logic]
- [Poor orchestration between components]

## Ideal For

- [User type 1 + rationale]
- [User type 2 + rationale]

## Not For

- [Anti-use-case + what to use instead]

## Related Plugins

[Cross-references to complementary plugins]
```

---

#### Minimal Viable Set (for lean plugins)

Single skill with few references — use this reduced set:
- Title Card + Problem + Solution (Layer 1)
- 1 Component Spotlight with prompt templates (Layer 2)
- Real-World Walkthrough + Prompt Patterns (Layer 3)
- Ideal For / Not For (Layer 4 minimal)

---

### Step 8 — Quality check

Before delivering, verify:

**Layer 1:** Problem describes real pain, Before vs After >=5 rows, Quick Start <=5 steps, installation is copy-pasteable
**Layer 2:** System overview shows relationships, every component has a spotlight, every skill has >=4 prompt templates
**Layer 3:** Good vs Bad prompt table present, >=3 prompt anti-patterns, Walkthrough 500+ words, >=3 usage scenarios
**Layer 4:** Decision logic documented, failure modes >=3, Ideal For >=4, Not For >=3, no frontmatter copy-pasted as prose

---

## Anti-patterns

1. **Copy-pasting frontmatter as documentation prose** — frontmatter is for Claude's activation engine, not for human readers. Rewrite in plain language.
2. **Documenting every reference file's content in the README** — reference files exist for progressive disclosure; summarize them in a table, don't reproduce them.
3. **Writing scenarios that say "user asks about X and gets an answer"** — scenarios must describe a real situation with context, not a generic query-response.
4. **Skipping the problem statement** — jumping straight to features without establishing why the reader should care.
5. **Including skill invocation syntax in prompts** — users type natural language, not `/plugin:skill-name`. Document how people actually talk.
6. **Reading all files into context before analyzing** — this wastes tokens and degrades output. Follow the token efficiency strategy.

---

## Output format

By default, the documentation is written as a replacement for the plugin's `README.md`. If the user requests a different format (tutorial, wiki page, blog post), adapt the structure but keep the same content order: problem → install → what's inside → scenarios → reference.

---

## References

This skill uses the analysis framework from `plugin-architecture` (component decision matrix) and the structural knowledge from `plugin-validation` (what a valid plugin looks like) to inform its documentation. It does not duplicate those skills — it applies their frameworks to produce human-readable documentation.

---

> *Plugin-Dev Authoring Toolkit by [Viktor Bezdek](https://github.com/viktorbezdek) — licensed under MIT.*
