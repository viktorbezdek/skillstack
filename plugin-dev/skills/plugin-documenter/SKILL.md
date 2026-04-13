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
| `skills/*/templates/` | If present | List filenames — document as shipped templates |
| `skills/*/examples/` | If present | List filenames — document as bundled examples |
| `skills/*/scripts/` | If present | List filenames — skill-private tooling |
| `skills/*/fixtures/` | If present | List filenames — test fixtures |
| `hooks/hooks.json` | If present | Full (small) |
| `hooks/scripts/*.sh` | If present | First 5 lines of each (shebang + purpose comment) |
| `.mcp.json` | If present | Full (small) |
| `agents/*.md` | If present | Frontmatter only |
| `commands/*.md` | If present | First 10 lines |
| `scripts/*.py` or `scripts/*.sh` | If present | First 10 lines (docstring/usage) + `--help` if available |

**Output:** a file inventory table with path, type, line count, and read-depth note.

### Token efficiency strategy

Plugins vary wildly in size — from 3 files (single-skill) to 30+ files (cloud-finops has 27 reference files alone). Reading everything into context wastes tokens and degrades output quality.

**The rule: read structure first, content on demand.**

1. **Always read fully:** plugin.json, SKILL.md files, hooks.json, .mcp.json, CHANGELOG.md — these are small and essential.
2. **Read selectively:** reference files — read only the title (first `#` heading) and the opening blockquote (the scope statement). This gives you enough to summarize what each reference covers without burning 200+ lines of context per file.
3. **Read on demand:** if a specific reference is needed for a scenario (e.g. you need the AWS-specific content from `finops-aws.md` to write an AWS cost scenario), read just that one file.
4. **Never read:** test fixtures, example skill bodies (list filenames only), large script implementations (read docstring/usage only).
5. **Count, don't read:** eval files — report "8 positive + 5 negative trigger cases, 3 output cases" without reading the actual queries.

**For a plugin with N reference files, total reads should be:**
- N=0-5: read all references fully (small plugin)
- N=6-15: read titles + blockquotes, deep-read 2-3 most important
- N=16+: read titles only, deep-read on demand for scenarios

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

### Step 4 — Write "How to Use" with prompt templates

For EACH skill in the plugin, produce a practical usage section with:

1. **What it does** — one paragraph explaining the capability in plain language
2. **Prompt templates** — 3-5 copy-pasteable prompts that trigger the skill. These are NOT the eval queries — they are realistic prompts a user would type in a Claude Code session. Each prompt should show a different angle of the skill:

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

**Rules for good prompt templates:**
- Show the user's actual words, not the skill name ("Help me design a REST API", not "Use api-design to design an API")
- Vary the intent: one for starting fresh, one for reviewing existing work, one for a specific sub-topic, one for troubleshooting
- Include context where it helps ("I'm using Express.js" or "This is a public-facing API")
- Never include the skill invocation syntax (`/plugin-dev:plugin-hooks`) — the skill activates automatically from natural language

### Step 5 — Map realistic use-case scenarios

For each skill in the plugin, read:
- The frontmatter trigger phrases (the "use when" clauses)
- The SKILL.md body (the methodology, phases, checklists)
- The references (deep domain content)
- The evals (if present — eval queries are excellent proxies for real user scenarios)

From these, construct **3-5 realistic scenarios per skill**. Each scenario describes WHERE the user is (their situation), WHAT they ask, WHAT the skill provides, and WHAT they end up with:

```markdown
#### Scenario: Migrating a monolith to microservices

**Context:** You're breaking a Rails monolith into services and need to design
the inter-service API contracts before coding anything.

**You say:** "Help me design the API contracts between our user service and
order service — we need to handle auth tokens and eventual consistency"

**The skill provides:**
- Resource decomposition following REST conventions
- Auth token propagation patterns (header forwarding vs service-to-service JWT)
- Eventual consistency strategies (saga pattern, outbox pattern)
- Error contract for cross-service failures (4xx vs 5xx semantics)

**You end up with:** A documented API contract both teams can implement
against, with schemas, error codes, and sequence diagrams.
```

Scenarios must be **specific and grounded** — tied to a real situation a developer/PM/designer would recognize. Not "user asks about X and gets an answer."

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

### [Skill 1 Name]

**What it does:** [plain language — when it activates, what methodology it provides]

**Try these prompts:**

\```
[Prompt template 1 — starting fresh]
\```

\```
[Prompt template 2 — reviewing existing work]
\```

\```
[Prompt template 3 — specific sub-topic or troubleshooting]
\```

**Key references:** [summary table of reference files, if any]

### [Skill 2 Name]
[Same structure...]

## Usage Scenarios

### Scenario 1: [Descriptive title grounded in a real situation]

**Context:** [Where the user is — their project, their problem, their role]

**You say:** "[Exact prompt they would type]"

**The skill provides:** [Bullet list of specific outputs from the skill's methodology]

**You end up with:** [Concrete deliverable]

### Scenario 2: [Title]
[Same structure...]

## How It Works Under the Hood

[Architecture from Step 2 — how components relate, data flow, progressive disclosure]

## Version History

[From CHANGELOG.md if present]
```

### Step 7 — Quality check

Before delivering, verify:

- [ ] Problem statement doesn't use jargon the target audience wouldn't know
- [ ] Installation instructions are copy-pasteable and correct
- [ ] Every skill has a "How to Use" section with ≥3 prompt templates
- [ ] Prompt templates use natural language (not skill invocation syntax)
- [ ] Prompt templates vary in intent (start fresh, review, troubleshoot, specific sub-topic)
- [ ] Every skill has at least one realistic scenario with Context/You say/Provides/End up with
- [ ] Scenarios are grounded in real situations (not "user asks about X")
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

### References (progressive disclosure)

References are the depth behind the SKILL.md body. Document them as a **summary table** — one row per file, with the topic and what a user would learn from it. Do NOT reproduce reference content in the README. The point is to tell users "this depth exists" so they know the skill is not surface-level.

Example for a plugin with 20 references:
```markdown
| Reference | Topic |
|---|---|
| `finops-aws.md` | AWS-specific cost optimization strategies |
| `finops-kubernetes.md` | Kubernetes cluster right-sizing |
| ... | ... |
```

### Hooks

Focus on **what events they handle** and **what they prevent or automate**. Read `hooks.json` for the event/matcher pairs and the hook scripts for the logic. Common patterns: guardrails (PreToolUse blocks), automation (PostToolUse formats), context injection (SessionStart adds info).

### MCP servers

Focus on **what tools they expose** and **what external systems they connect to**. Read `.mcp.json` for the server config and any tool definitions.

### Scripts

Focus on **CLI usage** and **what they produce**. Show the command, the flags, and example output. Read only the docstring or `--help` output, not the full implementation.

### Templates and examples

List them with a one-line description each. Templates are starting points for users; examples are demonstrations. Both are important to mention but don't need deep documentation — the files themselves are the docs.

### Fixtures and test data

Mention their existence ("includes N test fixtures for the eval harness") but do not document individual fixture files. They are implementation details, not user-facing.

---

## References

This skill uses the analysis framework from `plugin-architecture` (component decision matrix) and the structural knowledge from `plugin-validation` (what a valid plugin looks like) to inform its documentation. It does not duplicate those skills — it applies their frameworks to produce human-readable documentation.

---

> *Plugin-Dev Authoring Toolkit by [Viktor Bezdek](https://github.com/viktorbezdek) — licensed under MIT.*
