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

The document follows a **4-layer competence model**. Most docs fail because they skip layers 2 and 4. Every layer is mandatory.

```
Layer 1: Awareness     → Title Card + Problem + Solution
Layer 2: Mental Model  → System Map + Component Spotlights
Layer 3: Execution     → Walkthrough + Prompt Patterns
Layer 4: Mastery       → Decision Logic + Edge Cases + Integration Patterns
```

Follow this structure. Sections marked (lean) can be shortened for simple single-skill plugins. Sections marked (power) can be omitted for plugins with fewer than 3 components.

---

#### LAYER 1 — AWARENESS (filter audience, create tension, show the fix)

```markdown
# [Plugin Name]

> [One-sentence value proposition — what problem, for whom]
> [Visual hint: N skills, N hooks, N scripts — or just "single skill + N references"]

## The Problem

[2-3 paragraphs. Describe the pain BEFORE this plugin exists. Be specific:
what goes wrong, how much time is wasted, what mistakes are made. This is
not "X is hard" — it's "without this, teams spend 3 hours doing Y manually
and still get Z wrong 40% of the time." Make this slightly longer than
typical — this is where you earn the reader's attention.]

## The Solution

[2-3 paragraphs. What changes WITH this plugin. Concrete outcomes, not
aspirational claims. Include a system-level overview: "The plugin provides
N skills that handle [phases], N hooks that automate [events], and N scripts
that [do what]." This is the first time the reader sees the shape of the
system.]

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| [Specific pain point 1] | [How the plugin solves it] |
| [Specific pain point 2] | [How the plugin solves it] |
| [Specific pain point 3] | [How the plugin solves it] |
| [Specific pain point 4] | [How the plugin solves it] |
| [Specific pain point 5] | [How the plugin solves it] |

## Installation

[Copy-pasteable commands from Step 5]

## Quick Start

[The fastest path to seeing value. 3-5 numbered steps:
1. Install
2. Type this exact prompt: `[prompt]`
3. The skill does X
4. You see Y
5. Next, try Z]
```

---

#### LAYER 2 — MENTAL MODEL (system map + component spotlights)

```markdown
## System Overview

[Diagram-style breakdown showing how components relate. Use a text diagram
or table showing: skills, hooks, commands, MCP servers, scripts — and the
data flow between them. This builds the mental model BEFORE details.]

## What's Inside

[Component inventory table]

### Component Spotlights

[Repeat this block for EACH component type present in the plugin:]

#### [Skill Name] (skill)

**What it does:** [plain language — when it activates, what methodology]

**Input → Output:** [What the user provides → what the skill produces]

**When to use:** [specific triggers]
**When NOT to use:** [specific anti-triggers + what to use instead]

**Try these prompts:**

\```
[Prompt 1 — starting fresh]
\```

\```
[Prompt 2 — reviewing existing work]
\```

\```
[Prompt 3 — specific sub-topic]
\```

\```
[Prompt 4 — advanced or edge-case]
\```

**Key references:** [summary table of reference files]

#### [Hook Name] (hook) — if plugin has hooks

**Trigger:** [event + matcher]
**Lifecycle timing:** [pre/post, sync/async]
**What it does:** [concrete behavior]
**Side effects:** [what changes in the environment]

#### [Script Name] (script) — if plugin has scripts

**CLI:** `command --flags`
**What it produces:** [output format, where it writes]
**Typical workflow:** [when you'd run this in a real project]

#### [MCP Server] (mcp) — if plugin has MCP

**Tools exposed:** [list of MCP tools with one-line descriptions]
**External system:** [what it connects to]
**Constraints:** [latency, rate limits, failure modes]
```

---

#### LAYER 3 — EXECUTION (prompt patterns + end-to-end walkthrough)

```markdown
## Prompt Patterns

### Good Prompts vs Bad Prompts

| Bad (vague, won't activate) | Good (specific, activates reliably) |
|---|---|
| "[vague query]" | "[specific query with context]" |
| "[too broad]" | "[scoped to a real scenario]" |
| "[names the skill]" | "[describes the need naturally]" |

### Structured Prompt Templates

**For [use case 1]:**
\```
[Template with placeholders users fill in]
\```

**For [use case 2]:**
\```
[Template]
\```

### Prompt Anti-Patterns

- [Anti-pattern 1: what people type that doesn't work, and why]
- [Anti-pattern 2]
- [Anti-pattern 3]

## Real-World Walkthrough

[ONE detailed end-to-end example. 500-1000 words. This is the centerpiece.
Show the full system in action — not just one skill, but how components
chain together on a real project.

Structure it as a story with intermediate steps:
1. **Starting situation** — what the user has, what they need
2. **Step 1** — user intent → exact prompt → Claude reasoning → skill invocation → output
3. **Step 2** — next phase, building on Step 1's output
4. **Step 3** — (continue for 4-6 steps total)
5. **Final outcome** — concrete deliverable with metrics if applicable
6. **Gotchas discovered** — tips the walkthrough revealed]

## Usage Scenarios

### Scenario 1: [Descriptive title]

**Context:** [The user's situation — role, project, problem]
**You say:** "[Exact prompt]"
**The skill provides:** [Bullet list of specific outputs]
**You end up with:** [Concrete deliverable]

### Scenario 2-5: [Same structure, aim for 3-5 total]
```

---

#### LAYER 4 — MASTERY (decision logic, edge cases, integration, advanced)

```markdown
## Decision Logic

[Reveal how the system decides what to use. This prevents blind usage
and builds operator-level understanding.]

**When does [Skill A] activate vs [Skill B]?**
[Branching logic, heuristics, rules]

**What happens when [component] fails?**
[Error handling, fallback behavior, recovery]

## Failure Modes & Edge Cases

| Failure | Symptom | Recovery |
|---|---|---|
| [Common error 1] | [What the user sees] | [How to fix] |
| [Common error 2] | [What the user sees] | [How to fix] |
| [Misuse scenario] | [What goes wrong] | [Correct approach] |

## Performance & Constraints (lean)

[Token cost implications, latency for MCP calls, rate limits, scaling.
Set realistic expectations to avoid disillusionment post-adoption.]

## Integration Patterns (power)

[How this plugin combines with others. Show specific compositions:]
- [Plugin A + this plugin → what you get]
- [This plugin in a CI pipeline → how]
- [This plugin + hooks from another plugin → workflow]

## Advanced Use Cases (power)

[Non-obvious applications, composability tricks, emergent behavior.
Differentiate beginners from power users.]

## Anti-Patterns

- [Overusing the skill when a simpler approach works]
- [Misplacing logic (prompt vs code vs MCP)]
- [Poor orchestration between components]

## Ideal For

- [User type 1 + specific rationale]
- [User type 2 + specific rationale]
- [User type 3 + specific rationale]
- [User type 4 + specific rationale]

## Not For

- [Anti-use-case 1 + what to use instead]
- [Anti-use-case 2 + what to use instead]
- [Anti-use-case 3 + what to use instead]

## FAQ (optional, for complex plugins)

**Q: [Common question or skepticism]**
A: [Direct answer with rationale]

## Related Plugins

[Cross-references to SkillStack plugins that complement this one]

## Version History

[From CHANGELOG.md if present]
```

---

#### Minimal Viable Set (for lean plugins)

If the plugin is a single skill with few references, use this reduced set:
- Title Card + Problem + Solution (Layer 1)
- 1 Component Spotlight with prompt templates (Layer 2)
- Real-World Walkthrough + Prompt Patterns (Layer 3)
- Ideal For / Not For (Layer 4 minimal)

Everything else is expansion for complex multi-component plugins.

### Step 7 — Quality check

Before delivering, verify:

**Layer 1 (Awareness):**
- [ ] "The Problem" describes real pain with specific consequences
- [ ] "Before vs After" table has >=5 rows with specific contrasts
- [ ] "Quick Start" gets the user to value in <=5 steps
- [ ] Installation instructions are copy-pasteable and correct

**Layer 2 (Mental Model):**
- [ ] System overview shows component relationships (not just a list)
- [ ] Every component has a spotlight with input → output
- [ ] Every skill has >=4 prompt templates using natural language
- [ ] Prompt templates vary in intent (start fresh, review, troubleshoot, advanced)
- [ ] Hook/script/MCP spotlights present for each component type in the plugin

**Layer 3 (Execution):**
- [ ] Good vs Bad prompt comparison table present
- [ ] Prompt anti-patterns documented (>=3)
- [ ] Real-World Walkthrough is 500+ words with intermediate steps shown
- [ ] >=3 usage scenarios with Context/You say/Provides/End up with

**Layer 4 (Mastery):**
- [ ] Decision logic explains when component A vs B activates
- [ ] Failure modes table has >=3 entries with recovery steps
- [ ] "Ideal For" has >=4 entries with specific user types and rationale
- [ ] "Not For" has >=3 entries with alternatives
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
