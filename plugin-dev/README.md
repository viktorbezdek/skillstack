# Plugin Dev

> **v1.1.0** | Development | End-to-end Claude Code plugin authoring toolkit

Eight skills covering the full plugin lifecycle -- ideate, research, architect, build (hooks + composition), validate, evaluate, document -- plus four runnable scripts for scaffolding, validation, evaluation, and hook testing.

## What Problem Does This Solve

Anthropic's "Complete Guide to Building Skills for Claude" covers SKILL.md authoring well, but the harder parts of plugin development are undocumented or scattered: how hooks work (and how exit code 1 does NOT block -- only exit code 2 does), how to compose multiple components inside a single plugin, how to validate structure before shipping, how to measure whether a skill actually activates in production, and how to generate documentation that explains what a plugin does to someone who has never seen it. Teams building Claude Code plugins end up reverse-engineering hook mechanics from source, guessing at frontmatter rules, and shipping skills they have never tested for activation rate.

This plugin fills those gaps with eight specialized skills that cover each phase of the plugin lifecycle, plus four CLI scripts that automate the mechanical parts: scaffolding a plugin skeleton, validating its structure, running trigger and output evals, and testing hook scripts with synthetic input.

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install plugin-dev@skillstack
```

After installation, the 8 skills activate automatically based on trigger phrases. The 4 runnable scripts live at `plugin-dev/scripts/` and are invoked via CLI.

## What's Inside

This is a **multi-skill plugin** with 8 independently-activating skills, 4 runnable scripts with pytest suites, and 20+ reference documents.

### 8 Skills

| Skill | Trigger phrases | What it does |
|---|---|---|
| `plugin-ideation` | "want to build a plugin", "plugin idea", "should I build this" | Problem-first framing, pain-point mining, 7-criteria problem-worthy checklist, 7 ideation anti-patterns |
| `plugin-research` | "research existing plugins", "is there a plugin for X", "build or fork" | Marketplace survey methodology, 18+ authoritative Anthropic URLs, build-vs-fork-vs-contribute-vs-skip decision tree |
| `plugin-architecture` | "design a plugin", "skill vs hook vs mcp", "plugin structure" | Five extension types (skill, hook, MCP, subagent, slash command), decision matrix, plugin.json schema reference, 10 real-plugin examples |
| `plugin-hooks` | "hook", "PreToolUse", "PostToolUse", "hooks.json", "exit code 2" | 24+ hook events, 4 handler types (command, http, prompt, agent), matcher syntax, exit code semantics, 14 anti-patterns including the exit-code-1 trap, testing patterns |
| `plugin-composition` | "multi-component plugin", "CLAUDE_PLUGIN_ROOT", "directory structure" | Canonical directory layout, path substitution variables (ROOT/DATA/PROJECT_DIR/ENV_FILE), namespacing rules, hook merge semantics, MCP auto-start lifecycle |
| `plugin-validation` | "validate plugin", "check SKILL.md frontmatter", "plugin structure issues" | Structural validator covering plugin.json schema, SKILL.md frontmatter rules, dead reference detection, multi-skill plugin walk |
| `plugin-evaluation` | "evaluate plugin", "skill activation testing", "trigger rate" | Two eval formats (trigger-evals.json + evals.json), grader/analyzer/comparator pattern, quality criteria for eval queries, iteration methodology |
| `plugin-documenter` | "document a plugin", "write plugin README", "explain how a plugin works" | Fetches all plugin files (GitHub URL or local path), analyzes architecture, generates comprehensive README with problem statement, scenarios, installation, and component breakdown |

### 4 Runnable Scripts

All at `plugin-dev/scripts/`. Every script has its own pytest suite at `plugin-dev/scripts/tests/` (48 test cases total).

| Script | CLI | What it does |
|---|---|---|
| `scaffold_plugin.py` | `--name --skills --hooks --mcp --author` | Deterministic plugin skeleton generator. Creates plugin.json, SKILL.md per skill, optional hooks.json, optional .mcp.json, README.md. Runs the validator on output. |
| `validate_plugin.py` | `--plugin-dir PATH [--strict] [--json]` | Structural validation: plugin.json schema, SKILL.md frontmatter, dead references, multi-skill walk. Exit codes: 0=clean, 1=errors, 2=crash, 3=strict-mode warnings. |
| `run_eval.py` | `--plugin-dir --skill [--mode trigger\|output] [--offline]` | Eval harness with offline smoke mode (structural checks without API key). Live mode requires `ANTHROPIC_API_KEY`. |
| `test_hook.sh` | `SCRIPT_PATH EVENT_JSON --expect-exit N` | Mock-stdin hook tester. Invokes a hook script with canned JSON and asserts on exit code, stdout, stderr, and timeout. |

### Reference Documents by Skill

| Skill | References |
|---|---|
| `plugin-architecture` | Component decision matrix, manifest schema reference, 10 real-plugin examples |
| `plugin-composition` | Directory layout reference, path substitution patterns |
| `plugin-hooks` | Hook event reference (24+ events), handler types, anti-patterns, testing patterns |
| `plugin-evaluation` | Eval file formats, quality criteria, iteration methodology |
| `plugin-ideation` | Ideation anti-patterns, problem-worthy checklist |
| `plugin-research` | Authoritative sources list, build-vs-fork decision tree |
| `plugin-validation` | Frontmatter rules, validation checklist |

## Usage Scenarios

**1. "I have an idea for a plugin but don't know if it's worth building"**
Start with `plugin-ideation`. The 7-criteria problem-worthy checklist evaluates whether the idea solves a repeatable pain point (not a one-off task), whether it's within scope for a plugin (vs. a CLAUDE.md entry or an MCP server), and whether the friction is real or imagined. The 7 ideation anti-patterns catch common traps: scope creep, engineering-exercise plugins, already-solved problems.

**2. "I need to write hook scripts and I keep getting blocked by exit code behavior"**
The `plugin-hooks` skill is the authoritative guide to Claude Code hooks. The single most important fact: exit code 1 does NOT block -- only exit code 2 blocks. The skill covers all 24+ hook events, the 4 handler types, matcher syntax (exact, OR-list, regex), and 14 documented anti-patterns. Use `test_hook.sh` to test hook scripts offline before deploying.

**3. "I'm building a plugin with both skills and hooks -- how do I structure it?"**
`plugin-composition` provides the canonical directory layout, explains path substitution variables (`${CLAUDE_PLUGIN_ROOT}` for your plugin's install dir, `${CLAUDE_PLUGIN_DATA}` for persistent state, `${CLAUDE_PROJECT_DIR}` for the user's project), and documents hook merge semantics when multiple plugins install hooks for the same event.

**4. "My skill is live but sometimes Claude forgets to use it"**
`plugin-evaluation` teaches you to write trigger-evals.json (does the model pick the skill for each query?) and run them with `run_eval.py`. The iteration methodology: categorize failures, edit ONE thing (usually the SKILL.md description), re-run evals, repeat. The offline mode validates eval file structure without burning API calls.

**5. "I found a plugin and want to generate documentation for it"**
`plugin-documenter` takes a GitHub URL or local path, fetches all plugin files (SKILL.md, plugin.json, hooks, references, scripts, examples), analyzes the architecture (single-skill vs multi-skill, which components exist), and generates a complete README with problem statement, installation, component breakdown, realistic usage scenarios, and cross-references.

## Typical Flows

### New plugin from scratch
```
1. plugin-ideation      -> score the idea, pass the 7-criteria check
2. plugin-research      -> survey marketplace, read authoritative docs
3. plugin-architecture  -> decide component decomposition
4. plugin-composition   -> lay out the directory, wire path substitution
5. plugin-hooks         -> author hook scripts (if needed)
6. plugin-validation    -> run validate_plugin.py
7. plugin-evaluation    -> author evals, run run_eval.py
```

### Hook-only authoring
```
1. plugin-hooks         -> pick the right event, understand exit-code contract
2. plugin-composition   -> wire into hooks/hooks.json
3. test_hook.sh         -> offline-test with synthetic input
4. plugin-validation    -> confirm nothing broke
```

### Validating an existing plugin
```
1. validate_plugin.py --plugin-dir <path>   -> structural checks
2. plugin-validation                        -> interpret errors
3. plugin-evaluation                        -> write missing evals
```

## When to Use / When NOT to Use

**Use when:**
- Building a new Claude Code plugin from scratch
- Adding hooks to an existing plugin
- Validating plugin structure before shipping
- Measuring whether a skill activates on real queries
- Generating documentation for any plugin

**Do NOT use when:**
- Writing a single SKILL.md in depth -- use Anthropic's bundled `skill-creator`
- Building an MCP server -- use [mcp-server](../mcp-server/) instead
- Designing a complete end-to-end workflow skill -- use [skillstack-workflows](../skillstack-workflows/) `write-your-own-skill`
- Quick one-off prompts -- plugins are for repeatable work; use a CLAUDE.md entry

## Running Tests

```bash
cd plugin-dev/scripts
pip install pytest pyyaml
pytest tests/ -v
```

48 pytest cases covering all four scripts plus a validator-drift contract test.

## Related Plugins in SkillStack

- **[Skill Creator](../skill-creator/)** -- Deep single-skill authoring with progressive disclosure (Anthropic bundled)
- **[MCP Server](../mcp-server/)** -- MCP server authoring with FastMCP, TypeScript SDK, and evaluation patterns
- **[SkillStack Workflows](../skillstack-workflows/)** -- 18 composed workflows including `build-a-plugin` and `write-your-own-skill`

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
