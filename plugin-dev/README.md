# Plugin Dev

> **v1.0.0** | Development | End-to-end Claude Code plugin authoring toolkit

Eight skills covering the full plugin lifecycle — **ideate → research → architect → build (hooks / composition) → validate → evaluate → document** — plus four runnable scripts for scaffolding, validation, evaluation, and hook testing. Built to fill the gap Anthropic's "Complete Guide to Building Skills for Claude" doesn't cover: **hooks, multi-component plugin composition, plugin-level evaluation, and plugin documentation generation**.

## When to use this plugin

| Situation | Use |
|---|---|
| You have an idea for a plugin but don't know if it's worth building | `plugin-ideation` → 7-criteria problem-worthy checklist |
| You need to check if your plugin idea already exists | `plugin-research` → marketplace survey + authoritative docs |
| You're deciding skill vs hook vs MCP vs subagent vs command | `plugin-architecture` → decision matrix + manifest reference |
| You're writing hook scripts and want to avoid the exit-code-1 trap | `plugin-hooks` → 24+ hook events, handler types, anti-patterns |
| You're building a multi-component plugin (skills + hooks together) | `plugin-composition` → directory layout, path substitution |
| You want to know if your plugin structure is valid before shipping | `plugin-validation` → `validate_plugin.py` + frontmatter rules |
| You want to measure if your skill actually activates on real queries | `plugin-evaluation` → `run_eval.py` trigger + output evals |
| You found a plugin and want to generate comprehensive documentation for it | `plugin-documenter` → fetch, analyze, write full README with scenarios |

## When NOT to use this plugin

- **Writing a single SKILL.md in depth** → use Anthropic's bundled `skill-creator` (this plugin references it, doesn't replace it)
- **Building an MCP server** → use the `mcp-server` plugin in this marketplace
- **Designing one end-to-end workflow skill** → use `skillstack-workflows/write-your-own-skill`
- **Quick one-off prompts** → plugins are for repeatable work; use a CLAUDE.md entry instead

## Installation

Add the SkillStack marketplace and install this plugin from inside a Claude Code session:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install plugin-dev@skillstack
```

After installation, the 8 skills activate automatically based on trigger phrases in user prompts. The 4 runnable scripts live at `plugin-dev/scripts/` and are invoked via their CLI.

## What's inside

### 8 skills

| Skill | Trigger phrases | What it does |
|---|---|---|
| `plugin-ideation` | "want to build a plugin", "plugin idea", "should I build this" | Problem-first framing, pain-point mining, 7-criteria problem-worthy checklist, 7 ideation anti-patterns |
| `plugin-research` | "research existing plugins", "is there a plugin for X", "build or fork", "marketplace survey" | Marketplace survey methodology, authoritative source list (≥18 URLs), build-vs-fork-vs-contribute-vs-skip decision tree |
| `plugin-architecture` | "design a plugin", "skill vs hook vs mcp", "plugin structure", "plugin.json" | Five extension types, decision matrix, manifest schema reference, 10 real-plugin examples |
| `plugin-hooks` | "hook", "PreToolUse", "PostToolUse", "hooks.json", "SessionStart", "exit code 2" | 10 core hook events inline + 14+ more in reference, 4 handler types, matcher syntax, **14 anti-patterns including the exit-code-1 trap**, testing patterns |
| `plugin-composition` | "multi-component plugin", "CLAUDE_PLUGIN_ROOT", "plugin directory structure" | Canonical directory layout, path substitution variables (ROOT/DATA/PROJECT_DIR/ENV_FILE), namespacing, hook merge semantics, MCP auto-start lifecycle |
| `plugin-validation` | "validate plugin", "check SKILL.md frontmatter", "plugin structure issues" | Structural validator + frontmatter rules + per-layer checklist |
| `plugin-evaluation` | "evaluate plugin", "skill activation testing", "eval harness", "trigger rate", "output quality" | Two eval formats (trigger-evals.json + evals.json), grader/analyzer/comparator pattern, quality criteria, iteration methodology |
| `plugin-documenter` | "document a plugin", "write plugin README", "explain how a plugin works", "plugin tutorial" | Fetches all plugin files (GitHub URL or local path), analyzes architecture, generates comprehensive documentation with problem statement, scenarios, installation, and component breakdown |

### 4 runnable scripts

All at `plugin-dev/scripts/`. Every script has its own pytest suite at `plugin-dev/scripts/tests/`.

| Script | CLI | What it does |
|---|---|---|
| `validate_plugin.py` | `--plugin-dir PATH [--strict] [--json]` | Structural validation: plugin.json schema, SKILL.md frontmatter, dead reference citations, multi-skill plugin walk. Exit codes: 0=clean, 1=errors, 2=crash, 3=strict-mode warnings. Decoupled from the repo-wide validator with a drift contract test. |
| `scaffold_plugin.py` | `--name --skills --hooks --mcp --author --author-url --output-dir [--force]` | Deterministic plugin skeleton generator (no datetime.now, no uuid). Creates plugin.json, SKILL.md per skill, optional hooks.json, optional .mcp.json, README.md. Runs the validator on output. |
| `run_eval.py` | `--plugin-dir --skill [--mode trigger\|output] [--offline]` | Eval harness with **offline smoke mode** — forces structural checks when SDK/API_KEY missing, prints `OFFLINE MODE — STRUCTURAL SMOKE TEST ONLY` banner, never produces synthetic activation rates. Live mode requires `ANTHROPIC_API_KEY` + `pip install anthropic`. |
| `test_hook.sh` | `SCRIPT_PATH EVENT_JSON --expect-exit N --expect-output JQ --expect-stderr TEXT [--timeout N]` | Mock-stdin hook tester — invokes a hook script with a canned JSON event and asserts on exit code, stdout (via jq), stderr, and timeout. Fails loudly if `timeout`/`gtimeout` is unavailable (never silently skips). |

## Typical flows

### Flow 1: new plugin from scratch

```
1. plugin-ideation      → score the idea, pass the 7-criteria check
2. plugin-research      → survey marketplace, read authoritative docs
3. plugin-architecture  → decide component decomposition (skill / hook / MCP / …)
4. plugin-composition   → lay out the directory, wire path substitution
5. plugin-hooks         → author hook scripts (if hooks are in scope)
6. plugin-validation    → run validate_plugin.py → clean
7. plugin-evaluation    → author trigger-evals.json + evals.json → run_eval.py
```

### Flow 2: hook-only authoring

You have an existing plugin and want to add a hook:

```
1. plugin-hooks         → pick the right event, understand matcher/exit-code contract
2. plugin-composition   → wire into hooks/hooks.json with ${CLAUDE_PLUGIN_ROOT}
3. scripts/test_hook.sh → offline-test the hook script with synthetic input
4. plugin-validation    → confirm nothing else broke
```

### Flow 3: validating an existing plugin

You cloned someone else's plugin and want to check it ships clean:

```
1. scripts/validate_plugin.py --plugin-dir <path>   → structural checks
2. plugin-validation                                 → interpret any errors
3. plugin-evaluation                                 → write missing evals if absent
```

### Flow 4: evaluating a shipped plugin

Your skill is live but sometimes "forgets" to activate:

```
1. plugin-evaluation    → run trigger-evals (live or --offline smoke)
2. iteration-methodology reference → categorize failures, edit ONE thing
3. plugin-hooks / plugin-architecture → if the failure is architectural, not description-level
```

## Related plugins

- **[skill-creator](../skill-creator/)** (Anthropic bundled) — deep single-skill authoring with progressive disclosure
- **[mcp-server](../mcp-server/)** — MCP server authoring with FastMCP, TypeScript SDK, evaluation patterns
- **[skillstack-workflows](../skillstack-workflows/)** — 9 composed workflows including `write-your-own-skill`, `debug-a-failing-skill`, `review-a-plugin`

## Running evals

Every skill in the SkillStack has eval files (`evals/trigger-evals.json` + `evals/evals.json`). Use `run_eval.py` to test them.

### Offline smoke test (no API key needed)

Validates eval file structure only — does NOT measure real activation:

```bash
python3 plugin-dev/scripts/run_eval.py \
  --plugin-dir debugging \
  --skill debugging \
  --offline
```

### Live trigger evals (requires `ANTHROPIC_API_KEY` + `pip install anthropic`)

Measures whether the model actually picks the skill for each query:

```bash
python3 plugin-dev/scripts/run_eval.py \
  --plugin-dir debugging \
  --skill debugging \
  --mode trigger
```

### Live output evals

Measures whether the skill produces correct results (graded by LLM):

```bash
python3 plugin-dev/scripts/run_eval.py \
  --plugin-dir debugging \
  --skill debugging \
  --mode output
```

### Exit codes

| Code | Meaning |
|------|---------|
| 0 | Clean — all checks pass |
| 1 | Eval issues found |
| 2 | Skill not found |
| 3 | Mode requires API but `--offline` was passed |

## CI and tests

Plugin-dev ships with 48 pytest cases covering the four scripts plus a validator-drift contract test. The CI job `pytest / plugin-dev` runs on every push to main.

```bash
cd plugin-dev/scripts
pip install pytest pyyaml
pytest tests/ -v
```

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) — production-grade plugins for Claude Code. Licensed MIT.
