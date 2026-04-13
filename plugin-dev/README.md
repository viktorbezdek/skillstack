# Plugin Dev

> **v1.1.0** | Development | End-to-end Claude Code plugin authoring toolkit

> Build Claude Code plugins that actually work -- from validating the idea to measuring activation rate in production.

## The Problem

Anthropic's "Complete Guide to Building Skills for Claude" covers SKILL.md authoring, but the harder parts of plugin development are undocumented or scattered across source code. How hooks work is a minefield: exit code 1 does NOT block tool execution -- only exit code 2 does. Teams discover this after deploying a "blocking" hook that silently does nothing. How to compose multiple components (skills, hooks, MCP servers, subagents) inside a single plugin requires understanding path substitution variables (`${CLAUDE_PLUGIN_ROOT}`, `${CLAUDE_PLUGIN_DATA}`) that appear nowhere in public docs. How to validate structure before shipping -- is the frontmatter correct? Do reference paths resolve? Does plugin.json have the right fields? -- is manual inspection that misses errors.

The biggest gap is measuring whether a plugin actually works after shipping. A skill can have a perfect SKILL.md and still fail to activate because the description does not match how users phrase their requests. Without trigger evals, teams have no way to know that their skill activates for "design an API" but not for "help me with my REST endpoints" -- and they never discover the gap because they only test with their own phrasing.

Teams building Claude Code plugins end up reverse-engineering hook mechanics from source, guessing at frontmatter rules, shipping skills they have never tested for activation rate, and writing documentation manually that is incomplete within a week. The plugin development lifecycle has no tooling -- just a blank directory and a SKILL.md template.

## The Solution

This plugin provides eight specialized skills covering every phase of the plugin lifecycle, plus four CLI scripts that automate the mechanical parts. The lifecycle flows from ideation (is this worth building?) through research (does it already exist?), architecture (which component types?), composition (how to wire them together), hooks (event-driven automation), validation (is the structure correct?), evaluation (does it activate?), and documentation (does the README explain it?).

The skills are not theoretical guides -- they are decision frameworks. `plugin-ideation` has a 7-criteria checklist that kills bad ideas before you write code. `plugin-architecture` has a decision matrix for choosing between skills, hooks, MCP servers, subagents, and slash commands. `plugin-hooks` documents all 24+ hook events, the exit code semantics that trip up every new author, and 14 anti-patterns. `plugin-evaluation` teaches the trigger eval methodology that measures real-world activation rate.

The four scripts automate what should not be manual: `scaffold_plugin.py` generates a plugin skeleton, `validate_plugin.py` checks structural correctness, `run_eval.py` runs trigger and output evals, and `test_hook.sh` tests hook scripts offline with synthetic input. All four have pytest suites (48 test cases total).

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Hook deployed with exit code 1 thinking it blocks tool execution -- it does not | `plugin-hooks` documents exit code semantics: only exit code 2 blocks. 14 anti-patterns prevent common traps. |
| Skill shipped without testing -- activates for author's phrasing but not users' | `plugin-evaluation` + `run_eval.py` measure activation rate against diverse trigger queries |
| Plugin structure validated by manually reading plugin.json and SKILL.md | `validate_plugin.py` checks schema, frontmatter, dead references, and name consistency automatically |
| Multi-component plugin breaks because path references do not resolve at runtime | `plugin-composition` documents `${CLAUDE_PLUGIN_ROOT}`, `${CLAUDE_PLUGIN_DATA}`, and 2 other substitution variables |
| Plugin idea seems good, build takes two weeks, nobody uses it | `plugin-ideation` 7-criteria checklist kills bad ideas before code is written |
| Documentation written manually, outdated within a week | `plugin-documenter` generates comprehensive README from source files in minutes |

## Installation

Add the SkillStack marketplace, then install this plugin:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install plugin-dev@skillstack
```

### Prerequisites

For the skills: no additional dependencies.

For the scripts:
- Python 3.8+ for `scaffold_plugin.py`, `validate_plugin.py`, `run_eval.py`
- `pip install pytest pyyaml` for running script tests
- `ANTHROPIC_API_KEY` for live eval mode (offline mode works without)
- Bash for `test_hook.sh`

### Verify installation

After installing, test with:

```
I want to build a Claude Code plugin that enforces our team's coding standards -- is this a good idea?
```

## Quick Start

1. Install the plugin with the commands above
2. Start with your idea: `I want to build a plugin that automatically adds error handling to Python functions -- is this worth building?`
3. The `plugin-ideation` skill evaluates your idea against the 7-criteria checklist and either greenlights it or redirects you
4. If greenlit, ask: `Design the plugin structure -- should this be a skill, a hook, or both?`
5. `plugin-architecture` provides the component decomposition, then follow the lifecycle through composition, validation, and evaluation

## What's Inside

This is a **multi-skill plugin** with 8 independently-activating skills, 4 runnable scripts, 18 reference documents, and 133 eval cases.

### 8 Skills

| Skill | What it does |
|---|---|
| `plugin-ideation` | Problem-first framing with 7-criteria checklist and 7 ideation anti-patterns. Kills bad ideas before you write code. |
| `plugin-research` | Marketplace survey methodology with 18+ authoritative Anthropic URLs and a build-vs-fork-vs-contribute-vs-skip decision tree. |
| `plugin-architecture` | Decision matrix for choosing between 5 extension types (skill, hook, MCP server, subagent, slash command). Plugin.json schema reference and 10 real-plugin examples. |
| `plugin-hooks` | Authoritative guide to all 24+ hook events, 4 handler types (command, http, prompt, agent), matcher syntax, exit code semantics, and 14 documented anti-patterns. |
| `plugin-composition` | Canonical directory layout, path substitution variables, namespacing rules, hook merge semantics, and MCP auto-start lifecycle for multi-component plugins. |
| `plugin-validation` | Structural validator covering plugin.json schema, SKILL.md frontmatter rules, dead reference detection, and multi-skill plugin walk. |
| `plugin-evaluation` | Two eval formats (trigger-evals.json + evals.json), grader/analyzer/comparator pattern, quality criteria for eval queries, and iteration methodology. |
| `plugin-documenter` | Fetches all plugin files (GitHub URL or local path), analyzes architecture, generates comprehensive README with problem statement, scenarios, and component breakdown. |

### 4 Runnable Scripts

All at `plugin-dev/scripts/`. 48 pytest cases cover all four scripts.

| Script | CLI | What it does |
|---|---|---|
| `scaffold_plugin.py` | `--name --skills --hooks --mcp --author` | Generates a plugin skeleton with plugin.json, SKILL.md per skill, optional hooks.json, optional .mcp.json. Runs validator on output. |
| `validate_plugin.py` | `--plugin-dir PATH [--strict] [--json]` | Structural validation: plugin.json schema, SKILL.md frontmatter, dead references, multi-skill walk. Exit codes: 0=clean, 1=errors, 2=crash, 3=strict warnings. |
| `run_eval.py` | `--plugin-dir --skill [--mode trigger\|output] [--offline]` | Eval harness with offline smoke mode (structural checks without API key) and live mode for measuring activation rate. |
| `test_hook.sh` | `SCRIPT_PATH EVENT_JSON --expect-exit N` | Mock-stdin hook tester. Tests hook scripts with canned JSON, asserts exit code, stdout, stderr, and timeout. |

### Reference Documents

| Skill | References | Topic |
|---|---|---|
| `plugin-architecture` | 3 | Component decision matrix, manifest schema reference, 10 real-plugin examples |
| `plugin-composition` | 2 | Directory layout reference, path substitution patterns |
| `plugin-hooks` | 4 | Hook event reference (24+ events), handler types, anti-patterns, testing patterns |
| `plugin-evaluation` | 3 | Eval file formats, quality criteria, iteration methodology |
| `plugin-ideation` | 2 | Problem-worthy checklist, ideation anti-patterns |
| `plugin-research` | 2 | Authoritative sources list, build-vs-fork decision tree |
| `plugin-validation` | 2 | Frontmatter rules, validation checklist |

### plugin-ideation

**What it does:** Evaluates whether a plugin idea is worth building. Applies the 7-criteria problem-worthy checklist (repeatable pain, within plugin scope, not already solved, real friction, clear user, measurable outcome, sustainable maintenance) and catches 7 ideation anti-patterns (scope creep, engineering exercise, one-off task, already solved, too broad, too narrow, no user).

**Try these prompts:**

```
I want to build a Claude Code plugin that enforces our team's Python coding standards -- is this worth building?
```

```
I have three plugin ideas and don't know which one to pursue -- help me evaluate them
```

```
We keep doing the same API design review manually -- should this be a plugin or just a CLAUDE.md entry?
```

```
What kinds of repeatable workflow pain points make good plugin ideas?
```

### plugin-research

**What it does:** Validates a plugin idea against the existing ecosystem before you write code. Surveys the Claude Code plugin marketplace, checks authoritative Anthropic documentation (18+ canonical URLs), discovers community patterns, and applies the build-vs-fork-vs-contribute-vs-skip decision tree.

**Try these prompts:**

```
Is there already a Claude Code plugin for automated code review? I don't want to build something that exists
```

```
Research what's available for TypeScript development plugins -- I want to know what's already built vs what's missing
```

```
I found a plugin that does 70% of what I need -- should I fork it, contribute to it, or build my own?
```

```
Where are the authoritative Anthropic docs on plugin hooks and SKILL.md format?
```

### plugin-architecture

**What it does:** Decides which Claude Code extension types to use for each capability in your plugin and designs the plugin.json manifest around that decision. Provides the five extension types (skill, hook, MCP server, subagent, slash command), the decision matrix for choosing between them, plugin.json schema reference, and 10 worked examples from real plugins.

**Try these prompts:**

```
Design the plugin structure for a code quality enforcer -- it needs to block dangerous commands and provide review guidance
```

```
Should this capability be a skill, a hook, or an MCP server? It needs to intercept file writes and add license headers.
```

```
I'm building a multi-component plugin with skills, hooks, and an MCP server -- help me design the architecture
```

```
Show me examples of real plugins and how they decomposed their capabilities into skills vs hooks vs MCP
```

### plugin-hooks

**What it does:** The authoritative guide to Claude Code hooks. Covers all 24+ hook events (PreToolUse, PostToolUse, SessionStart, Stop, Notification, FileChanged, and more), 4 handler types (command, http, prompt, agent), matcher syntax (exact, OR-list, regex), exit code semantics (exit 1 does NOT block -- only exit 2 blocks), JSON output schema, and 14 documented anti-patterns.

**Try these prompts:**

```
Write a PreToolUse hook that blocks git push --force on the main branch
```

```
My hook returns exit code 1 but it's not blocking the tool call -- what's wrong?
```

```
What hook events are available in Claude Code? I need to run something after every file edit.
```

```
Show me the anti-patterns for hook development -- I want to avoid common mistakes
```

### plugin-composition

**What it does:** Teaches how to integrate multiple components inside a single plugin. Covers the canonical directory layout, path substitution variables (`${CLAUDE_PLUGIN_ROOT}` for install dir, `${CLAUDE_PLUGIN_DATA}` for persistent state, `${CLAUDE_PROJECT_DIR}` for user's project, `${CLAUDE_ENV_FILE}` for secrets), the bin/ shared-scripts pattern, namespacing rules, hook merge semantics, and MCP auto-start lifecycle.

**Try these prompts:**

```
How do I structure a plugin that has three skills, two hooks, and an MCP server?
```

```
My hook script can't find a file that's in the plugin directory -- I think my path reference is wrong
```

```
What's the difference between CLAUDE_PLUGIN_ROOT and CLAUDE_PLUGIN_DATA? When do I use each?
```

```
Two plugins install hooks for the same event -- which one wins? How does merge work?
```

### plugin-validation

**What it does:** Validates the structural correctness of a plugin before shipping. Checks plugin.json schema (required fields, valid values), SKILL.md YAML frontmatter (format, name consistency), reference cross-references (do referenced files exist?), and multi-skill directory conventions. Use `validate_plugin.py` for automated checks or the skill for interpreting errors and fixing issues.

**Try these prompts:**

```
Validate my plugin before I publish -- run all structural checks
```

```
My plugin won't load after installation -- help me debug the structure
```

```
What are the SKILL.md frontmatter rules? I keep getting activation failures and I think my description is malformed.
```

```
Set up CI to validate our plugin structure on every PR
```

### plugin-evaluation

**What it does:** Measures whether a plugin actually works by running trigger evals (does the model select the skill for a given query?) and output evals (does it produce the correct result?). Teaches two eval file formats (trigger-evals.json and evals.json), the grader/analyzer/comparator pattern, quality criteria for eval queries, and the iteration methodology for improving activation rate.

**Try these prompts:**

```
My skill is live but Claude doesn't always pick it up -- how do I test and fix activation rate?
```

```
Write trigger evals for my API design skill -- I need positive and negative test cases
```

```
Walk me through the eval iteration process: my skill fails for 30% of queries and I don't know what to change
```

```
What makes a good eval query? My tests all pass but users report the skill doesn't activate for their prompts.
```

### plugin-documenter

**What it does:** Generates comprehensive documentation for any Claude Code plugin. Takes a GitHub URL or local path, fetches all plugin files (SKILL.md, plugin.json, hooks, references, scripts, examples, evals), analyzes the architecture, and produces a complete README with problem statement, installation instructions, component breakdown, realistic usage scenarios, and cross-references.

**Try these prompts:**

```
Document the plugin at https://github.com/user/repo/tree/main/my-plugin
```

```
Write a comprehensive README for the cloud-finops plugin in this repository
```

```
Generate documentation for the plugin at ./workflow-automation -- I need installation, usage scenarios, and architecture overview
```

```
Explain how the plugin-dev plugin works -- generate a tutorial-style walkthrough
```

## Real-World Walkthrough

You are a platform engineer at a company with 40 developers using Claude Code. Your team has a recurring problem: developers write API endpoints without consistent error handling, and every code review catches the same issues. You decide to build a Claude Code plugin that provides API design guidance and catches common mistakes.

**Phase 1: Ideation**

You start by testing the idea:

```
I want to build a plugin that provides API design guidance and catches inconsistent error handling across our endpoints. Is this worth building as a plugin?
```

The `plugin-ideation` skill runs the 7-criteria checklist. Your idea scores well on most criteria: repeatable pain (every API endpoint), clear user (your 40 developers), measurable outcome (consistent error handling across endpoints). But it flags one concern: "Is this a CLAUDE.md entry or a plugin?" Your pain is company-specific, so a project-level CLAUDE.md rule might be sufficient. The skill distinguishes: if the guidance is static (always apply the same rules), a CLAUDE.md entry works. If the guidance is dynamic (analyze the endpoint structure and provide context-specific recommendations), a plugin is warranted. Your case involves structural analysis, so the plugin path is confirmed.

**Phase 2: Research**

```
Is there already a Claude Code plugin for API design guidance?
```

The `plugin-research` skill surveys the marketplace and finds the existing `api-design` plugin in SkillStack. It covers REST, GraphQL, and gRPC patterns. You review it and find it provides general API design guidance but not your company's specific error handling conventions. The build-vs-fork decision tree recommends: install `api-design` for general patterns, build a separate plugin for your company-specific rules, and have them complement each other rather than compete.

**Phase 3: Architecture**

```
Design the plugin structure -- I need it to provide guidance through conversation AND block endpoints that don't have error handling
```

The `plugin-architecture` skill maps your requirements to component types. The guidance part is a skill (activates from natural language, provides methodology and patterns). The blocking part is a hook (PreToolUse on file writes, checks for error handling patterns, exit code 2 to block writes that miss error handling). The skill recommends a two-component plugin: one skill for API design guidance, one hook for enforcement.

**Phase 4: Composition and Hooks**

```
How do I structure a plugin with one skill and one hook? And how do I write the hook to block file writes?
```

The `plugin-composition` skill provides the directory layout. The `plugin-hooks` skill walks you through writing the PreToolUse hook: match on `Write` and `Edit` tool calls, check if the file is in the `src/api/` directory, inspect the content for error handling patterns, and return exit code 2 with a description if error handling is missing. The skill explicitly warns about the exit code 1 trap: using exit 1 for "failure" is wrong -- it logs the event but does not block. Only exit 2 blocks.

**Phase 5: Scaffolding and Validation**

You run `scaffold_plugin.py --name api-standards --skills api-guidance --hooks pre-write-check` to generate the skeleton. You write the SKILL.md and hook script. Then you run `validate_plugin.py --plugin-dir ./api-standards --strict` to catch structural issues. The validator flags that your SKILL.md description is missing NOT-for clauses, and that one reference path does not resolve. You fix both.

**Phase 6: Evaluation**

```
Write trigger evals for my api-guidance skill -- I need to test whether Claude activates it for the right queries
```

The `plugin-evaluation` skill helps you write 10 positive queries (variations of "help me design this API endpoint", "review my error handling", "what's the right status code for...") and 5 negative queries (near-misses that should NOT trigger the skill, like "help me set up the database" or "write unit tests for my API"). You run `run_eval.py --offline` to validate the eval file structure, then `run_eval.py` with your API key to measure activation rate. The skill activates for 8/10 positive queries. The `plugin-evaluation` skill's iteration methodology shows you how to edit the SKILL.md description to catch the two misses without breaking the existing 8.

**Phase 7: Documentation**

```
Generate documentation for the plugin at ./api-standards
```

The `plugin-documenter` skill reads all files and generates a comprehensive README with problem statement, installation instructions, skill and hook documentation, usage scenarios, and cross-references to the complementary `api-design` plugin.

The total process from idea to documented, evaluated plugin takes one day. Without the toolkit, the same process would take a week of reverse-engineering hook mechanics, guessing at frontmatter format, and never testing activation rate.

## Usage Scenarios

### Scenario 1: Starting a new plugin from scratch

**Context:** You have an idea for a plugin and want to go from zero to shipped with confidence that the structure is correct and the skill activates reliably.

**You say:** `I want to build a plugin that helps developers write better commit messages. Walk me through the whole process.`

**The skill provides:**
- Ideation: 7-criteria evaluation of the idea
- Research: marketplace survey for existing commit message plugins
- Architecture: skill vs hook decision (likely both -- a skill for guidance and a hook for enforcement)
- Composition: directory layout and path wiring
- Validation: automated structural checks
- Evaluation: trigger eval authoring and activation rate measurement

**You end up with:** A validated, evaluated plugin with a comprehensive README, ready to publish.

### Scenario 2: Debugging a hook that does not block

**Context:** You wrote a PreToolUse hook to prevent `git push --force` but it is not blocking the command. The hook script runs and prints an error, but the push goes through.

**You say:** `My PreToolUse hook is supposed to block git push --force but it doesn't work -- the hook runs but the command still executes`

**The skill provides:**
- Immediate diagnosis: you are likely using exit code 1 (does NOT block) instead of exit code 2 (blocks)
- Complete exit code reference: 0 = allow, 1 = log error but allow, 2 = block with message
- The JSON output schema for returning a descriptive block message
- `test_hook.sh` for testing the fixed hook offline

**You end up with:** A working blocking hook with offline test coverage and understanding of the exit code contract.

### Scenario 3: Improving activation rate for a shipped skill

**Context:** Your plugin is installed and works great when you test it, but your teammates report that Claude "ignores" the skill for their queries. You suspect the SKILL.md description does not match how they phrase requests.

**You say:** `My skill works for me but my team says Claude doesn't activate it. How do I measure and fix activation rate?`

**The skill provides:**
- Trigger eval authoring: how to write diverse positive queries (different phrasings, different contexts) and negative near-miss queries
- `run_eval.py` for measuring activation rate quantitatively
- Iteration methodology: categorize failures, edit the SKILL.md description (usually the trigger phrases in the description frontmatter), re-run evals
- Quality criteria for eval queries: realistic (how real users phrase it), varied (different angles), near-miss negatives (similar but should NOT trigger)

**You end up with:** A SKILL.md description that activates reliably for diverse user phrasings, backed by eval data.

### Scenario 4: Documenting a plugin you found

**Context:** You found a Claude Code plugin on GitHub that looks useful but the README is sparse. You want to understand what it does before installing it.

**You say:** `Document the plugin at https://github.com/user/repo/tree/main/their-plugin -- I want to understand the architecture and use cases before installing`

**The skill provides:**
- Architecture analysis: component inventory, skill count, hook events, MCP tools, references
- Problem statement: what the plugin solves, synthesized from all skill descriptions
- Usage scenarios: realistic prompts derived from skill descriptions and eval queries
- Installation instructions with verification step

**You end up with:** A comprehensive README that tells you exactly what the plugin does, how to use it, and whether it fits your needs.

## Typical Flows

### New plugin from scratch
```
1. plugin-ideation      -> score the idea, pass the 7-criteria check
2. plugin-research      -> survey marketplace, read authoritative docs
3. plugin-architecture  -> decide component decomposition
4. scaffold_plugin.py   -> generate plugin skeleton
5. plugin-composition   -> wire path substitution and multi-component layout
6. plugin-hooks         -> author hook scripts (if needed)
7. validate_plugin.py   -> structural validation
8. plugin-evaluation    -> author evals, measure activation rate
9. plugin-documenter    -> generate README
```

### Hook-only authoring
```
1. plugin-hooks         -> pick the right event, understand exit-code contract
2. plugin-composition   -> wire into hooks/hooks.json
3. test_hook.sh         -> offline-test with synthetic input
4. validate_plugin.py   -> confirm nothing broke
```

## Running Tests

```bash
cd plugin-dev/scripts
pip install pytest pyyaml
pytest tests/ -v
```

48 pytest cases covering all four scripts plus a validator-drift contract test.

## Ideal For

- **Teams building their first Claude Code plugin** -- the lifecycle flow prevents the guesswork and reverse-engineering that wastes the first week
- **Hook authors** -- the most complete documentation of hook events, exit code semantics, and anti-patterns available, with offline testing tooling
- **Plugin maintainers measuring quality** -- trigger evals quantify activation rate instead of relying on "it works when I test it"
- **Anyone evaluating third-party plugins** -- `plugin-documenter` generates comprehensive documentation from source files in minutes
- **CI/CD pipelines for plugin repos** -- `validate_plugin.py` provides automated structural checks with clear exit codes

## Not For

- **Writing a single SKILL.md in depth** -- use Anthropic's bundled `skill-creator` for deep single-skill authoring with progressive disclosure
- **Building an MCP server** -- use [mcp-server](../mcp-server/) for FastMCP, TypeScript SDK, and MCP evaluation patterns
- **Designing a complete end-to-end workflow skill** -- use [skillstack-workflows](../skillstack-workflows/) `write-your-own-skill` for workflow composition
- **Quick one-off automation** -- plugins are for repeatable work; use a CLAUDE.md entry for project-specific rules

## Related Plugins

- **[Skill Creator](../skill-creator/)** -- Deep single-skill authoring with progressive disclosure (Anthropic bundled)
- **[MCP Server](../mcp-server/)** -- MCP server authoring with FastMCP, TypeScript SDK, and evaluation patterns
- **[SkillStack Workflows](../skillstack-workflows/)** -- 18 composed workflows including `build-a-plugin` and `write-your-own-skill`

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) — production-grade plugins for Claude Code.
