# Plugin Dev

> **v1.1.0** | Build Claude Code plugins that actually work -- from validating the idea to measuring activation rate in production.
> 8 skills + 4 scripts + 18 references | 109 trigger evals + 24 output evals (133 total)

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

---

## System Overview

```
Plugin Development Lifecycle
============================

  1. Ideation          2. Research          3. Architecture
  plugin-ideation      plugin-research      plugin-architecture
  7-criteria check     marketplace survey   5 extension types
  7 anti-patterns      18+ Anthropic URLs   decision matrix
       |                    |                    |
       v                    v                    v
  Worth building? -----> Already exists? ----> Component types decided
       |                                         |
       v                                         v
  4. Scaffolding       5. Composition       6. Hooks
  scaffold_plugin.py   plugin-composition   plugin-hooks
  generates skeleton   directory layout     24+ events
                       path substitution    exit code semantics
                       hook merge rules     14 anti-patterns
       |                    |                    |
       v                    v                    v
  7. Validation        8. Evaluation        9. Documentation
  validate_plugin.py   plugin-evaluation    plugin-documenter
  plugin-validation    run_eval.py          README generation
  structural checks    trigger + output     from source files
       |                    |                    |
       v                    v                    v
  Structure correct    Activation measured   README published
```

The eight skills activate independently based on what phase you are in. You do not need to follow the lifecycle sequentially -- jump to `plugin-hooks` if you just need to write a hook, or `plugin-evaluation` if you need to measure activation rate for an existing skill.

## What's Inside

### 8 Skills

| Skill | Trigger evals | Output evals | References | What it does |
|---|---|---|---|---|
| `plugin-ideation` | 13 | 3 | 2 | Problem-first framing with 7-criteria checklist and 7 ideation anti-patterns |
| `plugin-research` | 13 | 3 | 2 | Marketplace survey, 18+ authoritative URLs, build-vs-fork decision tree |
| `plugin-architecture` | 13 | 3 | 3 | Decision matrix for 5 extension types, plugin.json schema, 10 real examples |
| `plugin-hooks` | 16 | 3 | 4 | 24+ hook events, 4 handler types, exit code semantics, 14 anti-patterns |
| `plugin-composition` | 13 | 3 | 2 | Directory layout, path substitution variables, hook merge, MCP lifecycle |
| `plugin-validation` | 13 | 3 | 2 | Plugin.json schema, SKILL.md frontmatter, dead reference detection |
| `plugin-evaluation` | 14 | 3 | 3 | Trigger + output eval formats, grader pattern, iteration methodology |
| `plugin-documenter` | 14 | 3 | 0 | Fetches all plugin files, analyzes architecture, generates comprehensive README |

### 4 Runnable Scripts

All at `plugin-dev/scripts/`. 48 pytest cases cover all four scripts.

| Script | CLI | What it does |
|---|---|---|
| `scaffold_plugin.py` | `--name --skills --hooks --mcp --author` | Generates a plugin skeleton with plugin.json, SKILL.md per skill, optional hooks.json, optional .mcp.json. Runs validator on output. |
| `validate_plugin.py` | `--plugin-dir PATH [--strict] [--json]` | Structural validation: plugin.json schema, SKILL.md frontmatter, dead references, multi-skill walk. Exit codes: 0=clean, 1=errors, 2=crash, 3=strict warnings. |
| `run_eval.py` | `--plugin-dir --skill [--mode trigger\|output] [--offline]` | Eval harness with offline smoke mode (structural checks without API key) and live mode for measuring activation rate. |
| `test_hook.sh` | `SCRIPT_PATH EVENT_JSON --expect-exit N` | Mock-stdin hook tester. Tests hook scripts with canned JSON, asserts exit code, stdout, stderr, and timeout. |

### Component Spotlights

#### plugin-ideation (skill)

**What it does:** Evaluates whether a plugin idea is worth building before you write any code. Applies a 7-criteria problem-worthy checklist (repeatable pain, within plugin scope, not already solved, real friction, clear user, measurable outcome, sustainable maintenance) and catches 7 ideation anti-patterns.

**Input -> Output:** You describe a plugin idea -> You get a scored evaluation with a build/redirect/kill recommendation plus reasoning.

**When to use:** You have an idea for a Claude Code plugin and want to know if it is worth pursuing.
**When NOT to use:** You already have a validated idea and need to start building -> use `plugin-architecture`.

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

#### plugin-hooks (skill)

**What it does:** The authoritative guide to Claude Code hooks. Covers all 24+ hook events, 4 handler types (command, http, prompt, agent), matcher syntax, exit code semantics, and 14 documented anti-patterns.

**Input -> Output:** You describe what you want a hook to do -> You get the correct event, matcher, handler type, exit code contract, and working script with test instructions.

**When to use:** Writing, debugging, or understanding any hook in a Claude Code plugin.
**When NOT to use:** Building a complete plugin that also needs skills and MCP -> start with `plugin-architecture`, then come here for the hook-specific parts.

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

#### plugin-evaluation (skill)

**What it does:** Measures whether a plugin actually works by running trigger evals (does the model select the skill?) and output evals (does it produce correct results?). Teaches eval file formats, grader/analyzer/comparator patterns, quality criteria, and iteration methodology.

**Input -> Output:** You describe activation problems or need eval authoring guidance -> You get eval file structure, diverse test queries, and a methodology for iterating on your SKILL.md description to improve activation rate.

**When to use:** After shipping a skill, when activation is unreliable, or when building a new skill and wanting to test before publishing.
**When NOT to use:** Testing hook behavior (exit codes, JSON output) -> use `test_hook.sh`.

**Try these prompts:**

```
My skill is live but Claude doesn't always pick it up -- how do I test and fix activation rate?
```

```
Write trigger evals for my API design skill -- I need positive and negative test cases
```

```
Walk me through the eval iteration process: my skill fails for 30% of queries
```

```
What makes a good eval query? My tests pass but users report the skill doesn't activate.
```

#### plugin-documenter (skill)

**What it does:** Generates comprehensive documentation for any Claude Code plugin. Takes a GitHub URL or local path, inventories all plugin files, analyzes architecture, and produces a complete README following a 4-layer documentation model (Awareness, Mental Model, Execution, Mastery).

**Input -> Output:** You provide a plugin URL or path -> You get a comprehensive README with problem statement, installation, component breakdown, usage scenarios, and cross-references.

**When to use:** Documenting any Claude Code plugin -- yours or someone else's.
**When NOT to use:** Building a plugin (use `plugin-architecture` + `plugin-composition`), validating structure (use `plugin-validation`).

**Try these prompts:**

```
Document the plugin at https://github.com/user/repo/tree/main/my-plugin
```

```
Write a comprehensive README for the cloud-finops plugin in this repository
```

```
Generate documentation for the plugin at ./workflow-automation
```

```
Explain how the plugin-dev plugin works -- generate a tutorial-style walkthrough
```

#### plugin-architecture (skill)

**What it does:** Decides which Claude Code extension types to use for each capability. Provides the decision matrix for 5 types (skill, hook, MCP server, subagent, slash command), plugin.json schema reference, and 10 worked examples from real plugins.

**Input -> Output:** You describe capabilities your plugin needs -> You get a component decomposition mapping each capability to the appropriate extension type.

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
Show me examples of real plugins and how they decomposed their capabilities
```

#### plugin-composition (skill)

**What it does:** Teaches how to integrate multiple components inside a single plugin. Covers canonical directory layout, path substitution variables, namespacing rules, hook merge semantics, and MCP auto-start lifecycle.

**Input -> Output:** You describe a multi-component plugin -> You get the directory structure, path variable usage, and wiring instructions.

**Try these prompts:**

```
How do I structure a plugin that has three skills, two hooks, and an MCP server?
```

```
My hook script can't find a file that's in the plugin directory -- I think my path reference is wrong
```

```
What's the difference between CLAUDE_PLUGIN_ROOT and CLAUDE_PLUGIN_DATA?
```

```
Two plugins install hooks for the same event -- which one wins?
```

#### plugin-research (skill)

**What it does:** Validates a plugin idea against the ecosystem before you write code. Surveys the marketplace, checks 18+ authoritative Anthropic URLs, and applies the build-vs-fork-vs-contribute-vs-skip decision tree.

**Try these prompts:**

```
Is there already a Claude Code plugin for automated code review?
```

```
Research what's available for TypeScript development plugins
```

```
I found a plugin that does 70% of what I need -- should I fork it or build my own?
```

```
Where are the authoritative Anthropic docs on plugin hooks and SKILL.md format?
```

#### plugin-validation (skill)

**What it does:** Validates structural correctness before shipping. Checks plugin.json schema, SKILL.md frontmatter, reference cross-references, and multi-skill directory conventions.

**Try these prompts:**

```
Validate my plugin before I publish -- run all structural checks
```

```
My plugin won't load after installation -- help me debug the structure
```

```
What are the SKILL.md frontmatter rules? I keep getting activation failures.
```

```
Set up CI to validate our plugin structure on every PR
```

#### scaffold_plugin.py (script)

**CLI:** `python scripts/scaffold_plugin.py --name my-plugin --skills skill-a skill-b --hooks --author "Name"`
**What it produces:** A complete plugin directory with `plugin.json`, `SKILL.md` per skill, `hooks/hooks.json` (if `--hooks`), `.mcp.json` (if `--mcp`), and eval templates.
**Typical workflow:** Run once at the start of a new plugin project, then customize the generated files.

#### validate_plugin.py (script)

**CLI:** `python scripts/validate_plugin.py --plugin-dir ./my-plugin [--strict] [--json]`
**What it produces:** Validation report with errors, warnings, and pass/fail status. Exit codes: 0=clean, 1=errors, 2=crash, 3=strict warnings.
**Typical workflow:** Run after any structural change and in CI on every PR.

#### run_eval.py (script)

**CLI:** `python scripts/run_eval.py --plugin-dir ./my-plugin --skill my-skill [--mode trigger] [--offline]`
**What it produces:** Activation rate report (e.g., "8/10 positive triggers activated, 0/5 negative triggers activated"). Offline mode validates eval file structure without API calls.
**Typical workflow:** Run after writing or editing evals, and after modifying SKILL.md descriptions.

#### test_hook.sh (script)

**CLI:** `bash scripts/test_hook.sh hooks/scripts/my-hook.sh event.json --expect-exit 2`
**What it produces:** Pass/fail assertion on exit code, stdout content, and stderr content. Tests hooks offline with synthetic JSON input.
**Typical workflow:** Run after writing or modifying any hook script.

---

## Prompt Patterns

### Good Prompts vs Bad Prompts

| Bad (vague, may not activate) | Good (specific, activates reliably) |
|---|---|
| "Help me build a plugin" | "I want to build a plugin that enforces Python coding standards -- is this worth building?" |
| "Fix my hook" | "My PreToolUse hook returns exit code 1 but the command still executes -- what's wrong?" |
| "Plugin doesn't work" | "My skill activates for me but not for my teammates -- how do I measure and fix activation rate?" |
| "How do plugins work?" | "What hook events are available? I need to run something after every file edit." |
| "Make docs for my plugin" | "Generate documentation for the plugin at ./my-plugin -- I need installation, scenarios, and architecture" |

### Structured Prompt Templates

**For ideation:**
```
I want to build a Claude Code plugin that [what it does]. My team of [N] developers hits this problem [frequency]. Is this worth building as a plugin, or should it be a [CLAUDE.md entry / hook / MCP server]?
```

**For architecture:**
```
Design the plugin structure for [what it does]. It needs to [capability 1, e.g., provide guidance], [capability 2, e.g., block dangerous commands], and [capability 3, e.g., connect to an external API]. Which component types should I use?
```

**For hook debugging:**
```
My [event type] hook is supposed to [expected behavior] but instead [actual behavior]. Here's the script: [paste script or describe]. What's wrong?
```

**For eval authoring:**
```
Write trigger evals for my [skill name] skill. It should activate for [types of queries] and NOT activate for [near-miss queries]. I need [N] positive and [N] negative test cases.
```

**For documentation generation:**
```
Generate documentation for the plugin at [path or GitHub URL]. I need [full README / just the architecture section / usage scenarios].
```

### Prompt Anti-Patterns

- **Skipping ideation and jumping to implementation:** Asking "scaffold a plugin for X" without first evaluating whether X is worth building as a plugin. The 7-criteria checklist prevents wasted effort.
- **Asking about MCP server implementation:** This skill handles plugin architecture (which extension type to use) and plugin composition (how to wire components together). For MCP server implementation (FastMCP, TypeScript SDK, protocol details), use the mcp-server plugin.
- **Testing hooks manually in live sessions instead of offline:** Use `test_hook.sh` with synthetic input first. Testing hooks in a live Claude Code session is slow and gives poor error diagnostics.
- **Writing evals that only match your own phrasing:** Trigger evals need diversity -- different phrasings, different contexts, different levels of specificity. If all your eval queries sound like you wrote them, they will not catch activation gaps for other users.

## Real-World Walkthrough

You are a platform engineer at a company with 40 developers using Claude Code. Your team has a recurring problem: developers write API endpoints without consistent error handling, and every code review catches the same issues. You decide to build a Claude Code plugin.

**Step 1 -- Ideation.** You ask:

```
I want to build a plugin that provides API design guidance and catches inconsistent error handling. Is this worth building?
```

The `plugin-ideation` skill runs the 7-criteria checklist. Your idea scores well: repeatable pain (every API endpoint), clear user (40 developers), measurable outcome (consistent error handling). One concern: "Is this a CLAUDE.md entry or a plugin?" Static rules can go in CLAUDE.md. Dynamic analysis (inspect endpoint structure, provide context-specific recommendations) warrants a plugin. Your case involves structural analysis -- plugin confirmed.

**Step 2 -- Research.** You ask:

```
Is there already a Claude Code plugin for API design guidance?
```

`plugin-research` finds the existing `api-design` plugin. It covers general REST, GraphQL, and gRPC patterns but not your company-specific conventions. The build-vs-fork tree recommends: install `api-design` for general patterns, build a separate plugin for your company-specific rules.

**Step 3 -- Architecture.** You ask:

```
Design the plugin structure -- I need guidance through conversation AND blocking of endpoints without error handling
```

`plugin-architecture` maps requirements to types: guidance = skill (activates from natural language). Blocking = hook (PreToolUse on file writes, exit code 2 to block). Two-component plugin.

**Step 4 -- Scaffolding and Composition.** You run `scaffold_plugin.py --name api-standards --skills api-guidance --hooks`. The `plugin-composition` skill explains the directory layout and how to reference the hook script using `${CLAUDE_PLUGIN_ROOT}`.

**Step 5 -- Hook authoring.** You ask:

```
Write a PreToolUse hook that blocks Write and Edit calls to src/api/ files that don't include error handling
```

`plugin-hooks` provides the hook script with the correct exit code contract. It explicitly warns: exit 1 does NOT block -- only exit 2 blocks. You test with `test_hook.sh` using synthetic JSON before deploying.

**Step 6 -- Validation.** You run `validate_plugin.py --plugin-dir ./api-standards --strict`. The validator flags a missing NOT-for clause in SKILL.md and a dead reference path. You fix both.

**Step 7 -- Evaluation.** You ask:

```
Write trigger evals for my api-guidance skill
```

`plugin-evaluation` helps you write 10 positive and 5 negative queries. You run `run_eval.py` -- the skill activates for 8/10. The iteration methodology shows how to edit the SKILL.md description to catch the 2 misses.

**Step 8 -- Documentation.** You ask:

```
Generate documentation for the plugin at ./api-standards
```

`plugin-documenter` reads all files and generates a comprehensive README. Total time from idea to documented, evaluated plugin: one day.

**Gotchas discovered:** The exit code 1 vs 2 distinction is the single most common hook authoring mistake. Testing with `test_hook.sh` before deploying catches it every time.

## Usage Scenarios

### Scenario 1: Starting a new plugin from scratch

**Context:** You have an idea for a plugin and want to go from zero to shipped with confidence.

**You say:** `I want to build a plugin that helps developers write better commit messages. Walk me through the whole process.`

**The skill provides:**
- Ideation evaluation, marketplace research, architecture decomposition, scaffolding, composition guidance, validation, eval authoring, and documentation generation -- the full lifecycle

**You end up with:** A validated, evaluated plugin with a comprehensive README.

### Scenario 2: Debugging a hook that does not block

**Context:** Your PreToolUse hook runs but does not prevent the command from executing.

**You say:** `My PreToolUse hook is supposed to block git push --force but the push goes through`

**The skill provides:**
- Immediate diagnosis: exit code 1 vs 2
- Complete exit code reference and JSON output schema
- `test_hook.sh` for offline testing

**You end up with:** A working blocking hook with test coverage.

### Scenario 3: Improving activation rate

**Context:** Your plugin works when you test it but teammates report Claude "ignores" it.

**You say:** `My skill works for me but my team says Claude doesn't activate it`

**The skill provides:**
- Trigger eval authoring with diverse phrasings
- `run_eval.py` for quantitative measurement
- Iteration methodology for improving SKILL.md description

**You end up with:** A SKILL.md description that activates reliably for diverse user phrasings.

---

## Decision Logic

**Which skill handles which phase?**

| Phase | Skill | Decision |
|---|---|---|
| "Should I build this?" | `plugin-ideation` | 7-criteria checklist -> build/redirect/kill |
| "Does this exist already?" | `plugin-research` | Marketplace survey -> build/fork/contribute/skip |
| "What component types?" | `plugin-architecture` | Decision matrix -> skill/hook/MCP/subagent/command |
| "How do I wire components?" | `plugin-composition` | Directory layout + path variables |
| "How do hooks work?" | `plugin-hooks` | Event reference + exit codes + anti-patterns |
| "Is my structure correct?" | `plugin-validation` | Automated checks + frontmatter rules |
| "Does it activate?" | `plugin-evaluation` | Trigger evals + iteration methodology |
| "How do I document it?" | `plugin-documenter` | Source analysis -> comprehensive README |

**When to use a script vs a skill?**

Scripts automate mechanical checks. Skills provide decision guidance. Use `validate_plugin.py` to check structure automatically, then use `plugin-validation` the skill to understand and fix the errors. Use `run_eval.py` to measure activation rate, then use `plugin-evaluation` the skill to iterate on the SKILL.md description based on failures.

**Typical lifecycle flows:**

New plugin from scratch: ideation -> research -> architecture -> scaffold -> composition -> hooks -> validate -> evaluate -> document

Hook-only authoring: hooks -> composition -> test_hook.sh -> validate

Existing plugin improvement: evaluation (measure) -> iterate SKILL.md -> evaluate (re-measure) -> document

## Failure Modes & Edge Cases

| Failure | Symptom | Recovery |
|---|---|---|
| Hook uses exit code 1 expecting it to block | Hook script runs, log shows execution, but the tool call proceeds anyway | Change to exit code 2. Exit 1 = log error but allow. Exit 2 = block with message. Test with `test_hook.sh --expect-exit 2`. |
| Skill activates for author but not for users | Author tests pass, but team reports "Claude ignores the plugin" | Write diverse trigger evals with different phrasings, not just how you would ask. Run `run_eval.py` to measure. Iterate on the SKILL.md description to broaden trigger coverage. |
| Plugin structure passes local validation but fails on install | `validate_plugin.py` reports clean but plugin does not load in Claude Code | Run with `--strict` flag. Check that skill directory names match the `name` field in SKILL.md frontmatter. Verify `plugin.json` version field is a valid semver string. |
| Path substitution variable does not resolve at runtime | Hook or MCP config references a file path that works in development but 404s after installation | Use `${CLAUDE_PLUGIN_ROOT}` for files shipped with the plugin, `${CLAUDE_PLUGIN_DATA}` for persistent state created at runtime. Never hardcode absolute paths. |
| Plugin idea passes ideation but nobody uses it | Plugin is structurally correct, activates in evals, but real usage is zero | Re-run ideation with the "clear user" criterion. Is the pain repeatable enough? Is the plugin discoverable? Consider that CLAUDE.md entries are simpler and project-scoped -- a plugin only wins if the guidance needs to be dynamic or shared across projects. |

## Running Tests

```bash
cd plugin-dev/scripts
pip install pytest pyyaml
pytest tests/ -v
```

48 pytest cases covering all four scripts plus a validator-drift contract test.

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

## Ideal For

- **Teams building their first Claude Code plugin** -- the lifecycle flow prevents the guesswork and reverse-engineering that wastes the first week
- **Hook authors** -- the most complete documentation of hook events, exit code semantics, and anti-patterns available, with offline testing tooling
- **Plugin maintainers measuring quality** -- trigger evals quantify activation rate instead of relying on "it works when I test it"
- **Anyone evaluating third-party plugins** -- `plugin-documenter` generates comprehensive documentation from source files in minutes
- **CI/CD pipelines for plugin repos** -- `validate_plugin.py` provides automated structural checks with clear exit codes

## Not For

- **Writing a single SKILL.md in depth** -- use Anthropic's bundled `skill-creator` or SkillStack's more advanced skill engineering for deep single-skill authoring
- **Building an MCP server** -- use [mcp-server](../mcp-server/) for FastMCP, TypeScript SDK, and MCP evaluation patterns
- **Designing a complete end-to-end workflow skill** -- use [skillstack-workflows](../skillstack-workflows/) `write-your-own-skill` for workflow composition
- **Quick one-off automation** -- plugins are for repeatable work; use a CLAUDE.md entry for project-specific rules

## Related Plugins

- **[MCP Server](../mcp-server/)** -- MCP server authoring with FastMCP, TypeScript SDK, and evaluation patterns
- **[SkillStack Workflows](../skillstack-workflows/)** -- 18 composed workflows including `build-a-plugin` and `write-your-own-skill`
- **[Tool Design](../tool-design/)** -- Design the tools that MCP servers expose, complementing the plugin structure this skill teaches
- **[Agent Evaluation](../agent-evaluation/)** -- Broader agent evaluation frameworks that build on the trigger eval methodology here

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
