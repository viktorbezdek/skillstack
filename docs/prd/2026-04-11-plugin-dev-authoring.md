# `plugin-dev` — End-to-End Claude Plugin Authoring Toolkit

Created: 2026-04-11
Category: Infrastructure
Status: Draft
Research: Deep

---

## Problem Statement

People building Claude Code plugins today face three documentation gaps that Anthropic's own authoritative guide (*The Complete Guide to Building Skills for Claude*, Jan 2026) explicitly does not cover:

1. **Plugin composition** — when a capability belongs in a skill vs. a hook vs. an MCP tool vs. a subagent vs. a slash command. The official guide covers single-skill authoring exhaustively but is silent on multi-component plugins.
2. **Hooks** — the Claude Code docs document 28 hook event types and 4 handler types, but the Anthropic skill-building guide does not mention hooks at all. There is no tutorial-style resource that teaches hook authoring end-to-end.
3. **End-to-end lifecycle** — existing resources (`skill-creator`, `mcp-server`) cover isolated authoring steps. Nothing covers the upstream phases (ideation, research) or the downstream phases (plugin-level validation and evaluation) in a way that ties the whole project together.

The consequence: people ship plugins where the manifest is wrong, the skills silently fail to activate, the hooks have silent exit-code traps, and no one has measured whether the plugin actually works. Real-world surveys of 10 community plugins show only ~3 have any tests at all.

This PRD specifies a new skillstack plugin, **`plugin-dev`**, that fills those three gaps as a single multi-skill plugin with runnable tooling. It is designed to serve someone going from "I want a plugin that does X" to a deployed, validated, evaluated plugin without having to stitch together content from five different sources.

---

## Core User Flows

### Flow 1: End-to-end new plugin build

1. User asks Claude: *"I want to build a Claude Code plugin that helps me manage my personal finance spreadsheets."*
2. `plugin-ideation` skill activates. It guides the user through pain-point mining, existing-plugin gap analysis ("is there already something in the marketplace?"), and the "problem worthy of a plugin" checklist. Output: a written one-paragraph problem statement.
3. User accepts the framing. `plugin-research` skill activates next (or Claude loads it manually). It guides a marketplace survey (what exists, what doesn't), capability audit (what the user's actual workflow needs), and the build-vs-fork-vs-skip decision. Output: a go/no-go decision and a rough feature list.
4. `plugin-architecture` skill activates. It walks the user through component decomposition: which features belong in skills, which in hooks, which (if any) need an MCP server, which belong in agents, which belong in slash commands. The decision matrix is explicit. Output: a draft plugin structure — directory layout, manifest fields, component list.
5. User runs `python scripts/scaffold_plugin.py --name my-finance-plugin --skills spreadsheet-parse,budget-analysis --hooks PostToolUse` (or asks Claude to run it). The scaffolder creates a skeleton plugin directory with `plugin.json`, `skills/{name}/SKILL.md` stubs, `hooks/hooks.json`, and a `README.md` scaffold.
6. `plugin-hooks` and `plugin-composition` skills activate as the user fills in the scaffold. They provide specific guidance on frontmatter fields, `${CLAUDE_PLUGIN_ROOT}` usage, hook handler patterns, and cross-component integration.
7. User runs `python scripts/validate_plugin.py --plugin-dir ./my-finance-plugin`. `plugin-validation` skill activates to explain any errors. User fixes them.
8. User writes `evals/evals.json` (output-quality test cases) and `evals/trigger-evals.json` (activation test cases) following the `plugin-evaluation` skill's guidance.
9. User runs `python scripts/run_eval.py --plugin-dir ./my-finance-plugin`. Gets trigger rate (should-trigger queries passing, should-not-trigger queries correctly rejecting) and output-quality scores.
10. User iterates until pass rates are acceptable, then publishes.

### Flow 2: Authoring hooks specifically

1. User asks Claude: *"I want a hook that auto-formats TypeScript files with prettier after every Edit."*
2. `plugin-hooks` skill activates. It explains that this is a `PostToolUse` hook with a `matcher: "Edit|Write"` and a `command` handler type.
3. Claude draws on the skill's reference file `hook-event-reference.md` to fill in the exact JSON schema for the hook configuration, the proper matcher syntax (exact vs `|`-separated vs JavaScript regex), and the exit-code contract.
4. The skill's `hook-anti-patterns.md` reference flags potential traps (exit code 1 is non-blocking, shell profile contaminating JSON output, infinite `Stop` loop risk, `updatedInput` replaces the whole object).
5. User writes the hook. Runs `bash scripts/test_hook.sh ./scripts/format-ts.sh '{"tool_name":"Edit","tool_input":{"file_path":"foo.ts"}}'` to smoke-test with mock stdin and assert exit code 0.
6. User drops the hook into an existing plugin's `hooks/hooks.json` and validates with `validate_plugin.py`.

### Flow 3: Validating an existing plugin

1. User has an existing plugin directory from a third party or an old project.
2. User runs `python scripts/validate_plugin.py --plugin-dir /path/to/plugin`.
3. The validator checks: `plugin.json` syntax and required fields, `SKILL.md` frontmatter for every skill inside, frontmatter `name` matches directory, cross-references (referenced files exist on disk), hook handler paths are valid, `${CLAUDE_PLUGIN_ROOT}` usage is present where expected.
4. Output is a structured error list with file paths and line numbers. `plugin-validation` skill activates if the user asks Claude to explain or fix errors.

### Flow 4: Evaluating an existing plugin

1. User has a plugin that "seems to work" but there is no measurement.
2. User writes `evals/evals.json` with 3+ output test cases (each with `query`, `files`, `expected_behavior`) and `evals/trigger-evals.json` with 8+ should-trigger queries and 5+ should-not-trigger queries.
3. User runs `python scripts/run_eval.py --plugin-dir ./my-plugin --skill spreadsheet-parse`.
4. The harness:
   - Splits trigger evals 60/40 train/test
   - Runs each query 3 times against the current description for reliable trigger rate
   - Spawns `with_skill` and `without_skill` subagents for each output eval
   - Grades output via a grader subagent returning `{text, passed, evidence}` per expected behavior
   - Produces a benchmark report with pass rate, precision/recall on triggers, and comparison against baseline
5. User sees where the skill underperforms and iterates (using the `plugin-evaluation` skill's methodology).

---

## Scope

### In Scope

**Plugin structure:**
- One new multi-skill plugin `plugin-dev` at `plugin-dev/` in the skillstack repo
- `plugin.json` manifest with standard skillstack fields (name, version `1.0.0`, description, author Viktor Bezdek, license MIT, keywords, repository)
- `README.md` following skillstack conventions (problem statement, scenario table, when-not-to-use, installation via `/plugin install plugin-dev@skillstack`, what's inside, cross-references to `skill-creator`, `mcp-server`, `skillstack-workflows`)
- Catalog registration in `.claude-plugin/registry.json` and `.claude-plugin/marketplace.json` (alphabetically between `persona-mapping` and `prioritization`; category `development`)
- Root `README.md` updates: plugin count 51 → 52, new entry in Development catalog section and in the "Find a skill by goal" / "I want to document and create skills" table

**7 skills under `plugin-dev/skills/`:**

1. **`plugin-ideation`** (target: ~180 lines SKILL.md + 2-3 references)
   - Core principle: problem-first framing. Do not build a plugin for a one-off task.
   - Frontmatter description triggers: "want to build a Claude plugin", "have an idea for a plugin", "should I build this as a plugin", "plugin idea", "plugin for X"
   - Sections: pain-point mining (what repetitive workflow do you have?), workflow audit (where do you redo work that Claude could remember?), existing-plugin gap analysis (marketplace search methodology), "problem worthy of a plugin" checklist (7 criteria), ideation anti-patterns (building for yourself only, building a tool you want vs. a problem you have, scope creep at ideation time)
   - Reference: `references/problem-worthy-checklist.md`, `references/ideation-anti-patterns.md`

2. **`plugin-research`** (~180 lines SKILL.md + 2 references)
   - Core principle: validate an idea before building. Most plugin ideas die at research time, and that is a success not a failure.
   - Frontmatter triggers: "research existing plugins", "is there a plugin for X", "should I build or fork", "marketplace survey", "plugin research"
   - Sections: marketplace survey methodology (how to search the official marketplace, Anthropic's skills repo, community plugins on GitHub), Anthropic doc fetching (canonical sources: the PDF, plugins reference, skills reference), community pattern discovery (reading 3-5 real plugins before building), the build-vs-fork-vs-skip decision gate
   - Reference: `references/authoritative-sources.md` (list of canonical URLs), `references/build-vs-fork-decision.md`

3. **`plugin-architecture`** (~220 lines SKILL.md + 3 references)
   - Core principle: the decomposition matters more than any single component. A plugin that puts the wrong capability in the wrong component fails silently.
   - Frontmatter triggers: "design a plugin", "plugin structure", "skill vs hook vs mcp", "plugin composition", "plugin components", "plugin architecture"
   - Sections: the five extension types (skill, hook, MCP server, subagent, slash command) with their roles, the decision matrix ("is this knowledge Claude should load? → skill. Is this a runtime trigger on an event? → hook. Is this an external tool? → MCP. Is this a multi-step workflow with a specialized prompt? → subagent. Is this a user-invoked command? → slash command"), `plugin.json` manifest design, directory layout, namespacing (`plugin-name:component-name`), real examples from Anthropic's official plugins (`plugin-dev`, `hookify`, `ralph-wiggum`, `security-guidance`)
   - References: `references/component-decision-matrix.md`, `references/manifest-reference.md`, `references/real-plugin-examples.md`

4. **`plugin-hooks`** (~220 lines SKILL.md + 4 references)
   - Core principle: hooks are the most powerful and most trap-laden extension type. Exit code 1 does not block. Matcher syntax has three modes. `updatedInput` replaces, not merges.
   - Frontmatter triggers: "hook", "PreToolUse", "PostToolUse", "SessionStart", "Stop hook", "hook event", "auto-format on edit", "block dangerous bash", "session hook"
   - Sections: the 10 hook events users actually write (PreToolUse, PostToolUse, PermissionRequest, UserPromptSubmit, SessionStart, SessionEnd, Stop, Notification, FileChanged, WorktreeCreate), the 4 handler types (command, http, prompt, agent) with when-to-use, matcher syntax (exact vs `|`-separated vs regex), exit code contract (0 = success, 2 = block, 1 = non-blocking error — the trap), JSON output schema for structured decisions, `${CLAUDE_PLUGIN_ROOT}` usage, testing with mock stdin
   - References: `references/hook-event-reference.md` (all 28 events with schemas), `references/hook-handler-types.md` (command/http/prompt/agent deep-dive), `references/hook-anti-patterns.md` (exit code 1 trap, infinite Stop loops, shell profile contaminating JSON, mixing exit and JSON, partial updatedInput, over-broad matchers, async hooks expected to block), `references/hook-testing-patterns.md` (mock stdin, debug log, `/hooks` menu, transcript view)

5. **`plugin-composition`** (~200 lines SKILL.md + 2 references)
   - Core principle: a plugin is more than the sum of its components. Shared conventions (path substitution, namespacing, settings) make the difference between a working plugin and a fragile one.
   - Frontmatter triggers: "multi-component plugin", "combine skills and hooks", "plugin directory structure", "CLAUDE_PLUGIN_ROOT", "plugin layout", "inside a plugin"
   - Sections: canonical directory layout (the table from Claude Code docs), the `.claude-plugin/` directory rule ("only plugin.json inside"), `${CLAUDE_PLUGIN_ROOT}` vs `${CLAUDE_PLUGIN_DATA}` (path substitution, persistence), the `bin/` directory pattern for plugin executables, skill namespacing, hook merging behavior when plugin is enabled, MCP server auto-start lifecycle, how to integrate components (pre-flight hook that runs before a skill, skill that references a script in `bin/`)
   - References: `references/directory-layout-reference.md`, `references/path-substitution-patterns.md`

6. **`plugin-validation`** (~180 lines SKILL.md + 2 references)
   - Core principle: plugins that pass `claude plugin validate` fail in production all the time. Structural validation is necessary but not sufficient; it just eliminates the stupid failures.
   - Frontmatter triggers: "validate a plugin", "plugin structure errors", "plugin.json errors", "frontmatter errors", "is my plugin correctly set up"
   - Sections: what `claude plugin validate` checks, what it misses (frontmatter name mismatch with directory, reference cross-reference validation, orphan catalog entries — the things skillstack's own validator catches), running `scripts/validate_plugin.py`, interpreting errors, CI integration (link to skillstack's `.github/workflows/ci.yml` as a reference)
   - References: `references/frontmatter-rules.md` (exact rules: kebab-case, max 64 chars, no XML tags, description ≤1024 chars, no first person, must front-load key use case in first 250 chars), `references/validation-checklist.md` (pre-ship checklist)

7. **`plugin-evaluation`** (~220 lines SKILL.md + 3 references)
   - Core principle: if you haven't measured the activation rate and the output pass rate, you have not evaluated your plugin. Manual testing is unreliable at scale.
   - Frontmatter triggers: "evaluate a plugin", "skill activation testing", "eval harness", "measure plugin quality", "plugin tests", "trigger rate", "output quality"
   - Sections: the three test types (triggering, functional, performance comparison), the two eval file formats (`evals/evals.json` for output quality with `query`/`files`/`expected_behavior`, `evals/trigger-evals.json` for activation with `query`/`should_trigger`), quality criteria for eval queries (realistic, varied, near-miss negatives, 8+ should-trigger and 5+ should-not-trigger minimum), running `scripts/run_eval.py`, interpreting results (precision, recall, pass rate, delta vs baseline), iteration methodology (60/40 train-test split, 3 runs per query, fail CI on regressions), the grader/analyzer/comparator pattern from Anthropic's skill-creator
   - References: `references/eval-file-formats.md` (full JSON schemas + examples), `references/eval-quality-criteria.md` (what makes a good eval query, with counter-examples), `references/iteration-methodology.md` (how to iterate on a skill description based on eval results)

**`scripts/` directory with 4 runnable tools** (at `plugin-dev/scripts/`):

1. **`scaffold_plugin.py`** — interactive plugin skeleton generator
   - CLI: `python scaffold_plugin.py --name NAME [--skills A,B,C] [--hooks EVENT1,EVENT2] [--mcp] [--author "Name"] [--output-dir PATH]`
   - Produces: `NAME/.claude-plugin/plugin.json`, `NAME/skills/{skill}/SKILL.md` stubs for each named skill, `NAME/hooks/hooks.json` with handlers stubbed out for each named event, `NAME/README.md` with sections pre-filled from the manifest, optional `.mcp.json` if `--mcp` flag, empty `NAME/scripts/` and `NAME/assets/` directories
   - Validates the generated output by running `validate_plugin.py` on it before returning

2. **`validate_plugin.py`** — structural validator adapted from `.github/scripts/validate_plugins.py`
   - CLI: `python validate_plugin.py --plugin-dir PATH [--strict] [--json]`
   - Accepts any plugin directory (not just skillstack-hosted plugins) and validates the full contract: manifest, frontmatter, name consistency, cross-references, required/optional fields, hook config if present
   - Exits non-zero on errors; `--strict` also fails on warnings; `--json` outputs structured results for CI consumption
   - Unlike the skillstack-internal validator, does NOT require catalog entries in `registry.json`/`marketplace.json` (those are skillstack-specific)

3. **`run_eval.py`** — activation and output eval harness adapted from Anthropic's `skill-creator` scripts
   - CLI: `python run_eval.py --plugin-dir PATH --skill SKILL_NAME [--mode trigger|output|both] [--workspace DIR] [--model MODEL] [--max-iterations N] [--verbose]`
   - Reads `evals/trigger-evals.json` and `evals/evals.json` from the plugin/skill directory
   - For trigger mode: 60/40 train-test split, 3 runs per query, computes precision and recall on should-trigger and should-not-trigger queries
   - For output mode: spawns `with_skill` and `without_skill` subagents per eval case, saves outputs to `workspace/iteration-N/eval-X-name/{with_skill,without_skill}/`, invokes a grader subagent with the strict `{text, passed, evidence}` output shape, aggregates into `benchmark.json` and `benchmark.md`
   - Reports pass rate, delta vs baseline, and highlights non-discriminating test cases (passed both with and without skill — not useful)

4. **`test_hook.sh`** — mock-stdin hook tester
   - CLI: `bash test_hook.sh SCRIPT_PATH '{"tool_name":"...","tool_input":{...}}' [--expect-exit N] [--expect-output JSON_PATH] [--expect-stderr TEXT]`
   - Pipes the mock event JSON to the hook script on stdin, captures stdout/stderr/exit code, asserts expectations
   - Fails loudly on: wrong exit code, invalid JSON on stdout, missing expected stderr substring, timeout (5-second default)
   - Useful in CI for regression-testing hook scripts

**Tests for the scripts** (at `plugin-dev/scripts/tests/`):
- `test_scaffold_plugin.py` — pytest suite that runs the scaffolder with several CLI arg combinations in tmp directories and asserts the output structure, then validates the output with `validate_plugin.py`
- `test_validate_plugin.py` — pytest suite using synthetic fake plugin directories (mirroring `.github/scripts/tests/test_validate_plugins.py`'s fixture pattern), covering all failure modes
- `test_run_eval.py` — pytest suite with mocked subagent responses, asserting the eval harness correctly computes precision/recall and produces the expected benchmark report shape
- `test_test_hook.sh` — bash test suite that creates trivial hook scripts and pipes mock stdin, asserting the expected assertions fire

**Skillstack repo updates:**
- `.claude-plugin/registry.json`: new entry for `plugin-dev`
- `.claude-plugin/marketplace.json`: new entry for `plugin-dev`
- Root `README.md`: plugin count 51 → 52, new catalog entry in "Development" section, new row in "I want to document and create skills" goal-routing table
- `.github/scripts/validate_plugins.py`: no changes needed (already supports multi-skill plugins as of commit `9c762cd`)

### Explicitly Out of Scope

- **Slash commands** (`/plugin-dev:ideate`, `/plugin-dev:scaffold`, etc.) — rejected in favor of plain scripts invoked via Claude or by the user directly. Avoids command/skill drift and matches the "approach A" choice from clarifying questions. Can be added in a future iteration if demand warrants.
- **GitHub Actions CI template** — the "Full: CI integration" option was rejected in favor of the "Ship harness + activation-testing guidance" option. Users can integrate `run_eval.py` into their own CI without us shipping a template.
- **MCP server authoring deep-dive** — `plugin-architecture` skill points users at the existing `mcp-server` skillstack plugin for MCP-specific depth. Duplicating that content here would create drift.
- **Single-skill authoring deep-dive** — `plugin-architecture` skill points users at the existing `skill-creator` plugin. Same rationale.
- **Broad ideation / creative problem solving** — scoped narrowly to *plugin* ideation. General creative thinking is covered by the existing `creative-problem-solving` skill.
- **Tool-first ideation framing** — rejected in the clarifying questions in favor of problem-first only. A plugin that wraps an MCP the user already has is still reached via problem-first framing ("I have this MCP, what problem is it solving for me?").
- **Multi-agent system design** — covered by `multi-agent-patterns` skill.
- **Hook event coverage for all 28 events inline in SKILL.md** — the main SKILL.md covers the core 10 events; the other 18 events are in `references/hook-event-reference.md` and loaded only when needed (progressive disclosure).
- **A published JSON Schema file at a stable URL** — we don't own a stable URL. We can reference hesreallyhim's community JSON Schema from the validation skill but not host our own.
- **Cross-harness support** (Cursor, Codex, OpenCode) — skillstack is Claude Code-only. Future iteration.
- **Versioning/publishing workflows** (semantic version bumps, changelog generation, publish CLI) — `git-workflow` skill covers general versioning. Not plugin-specific enough to duplicate.

---

## Technical Context

- **Repository**: `/Users/vbezdek/Work/skillstack` (github.com/viktorbezdek/skillstack)
- **Existing validator**: `.github/scripts/validate_plugins.py` (366 lines, supports single-skill and multi-skill plugins since commit `9c762cd`). `validate_plugin.py` in this new plugin is an adaptation of it for general use.
- **Existing validator tests**: `.github/scripts/tests/test_validate_plugins.py` (16 tests, including 3 for multi-skill plugins). Serves as a template for this plugin's own script tests.
- **Multi-skill plugin precedent**: `skillstack-workflows/` plugin (committed in `9c762cd`) has 9 skills in one plugin with their own subdirectories. This plugin follows the same pattern.
- **CI**: `.github/workflows/ci.yml` runs `plugin-validation` job that invokes the repo-level validator. The new plugin's scripts get their own `pytest` job in CI (same pattern as the existing `skill-creator/scripts/tests` pytest job).
- **Related existing plugins to cross-reference from the new plugin's README and skills**:
  - `skill-creator` — for single-skill authoring depth
  - `mcp-server` — for MCP server authoring
  - `skillstack-workflows` — specifically the `write-your-own-skill` workflow inside it (meta-workflow for one skill, complementary to this plugin's full lifecycle coverage)
  - `prompt-engineering` — referenced from `plugin-architecture` when discussing skill descriptions
  - `agent-evaluation` — referenced from `plugin-evaluation` for the LLM-as-judge methodology

- **Constraints from research findings**:
  - Every SKILL.md body should be under 500 lines per Anthropic best practices; use references for anything beyond that.
  - Description fields must be front-loaded in the first 250 characters (context budget truncation).
  - Descriptions must be third-person; no "I" or "my".
  - Hook `command` handlers must use `${CLAUDE_PLUGIN_ROOT}` for path references, not relative paths.
  - `name` field in plugin.json must match directory name (catch this in validator tests).
  - Multi-skill plugins register at the plugin root in registry.json (`path_in_repo: "plugin-dev"`), not at skill root.

- **Naming collision note**: Anthropic ships their own `plugin-dev` plugin in the official marketplace. Our plugin lives under the `skillstack` marketplace namespace, so it installs as `plugin-dev@skillstack` — no collision with the official `plugin-dev@claude-plugins-official`. The content complements Anthropic's (which is more tutorial-focused) with an opinionated lifecycle and shipped tooling.

- **Runnable scripts must be self-contained**: `scaffold_plugin.py`, `validate_plugin.py`, and `run_eval.py` should work without users installing anything beyond Python 3.12 stdlib + `pyyaml` (already a dependency of the existing skill-creator tests). `run_eval.py` additionally needs an LLM provider — use the Anthropic SDK (`anthropic` package) with graceful degradation if the API key is not set.

- **Research artifacts**: the four research reports produced during this PRD (plugin architecture, hooks, evaluation/validation, real-world plugins) should be saved as `plugin-dev/skills/plugin-dev-research-notes.md` or similar and used as the source material when writing the reference files. Content should be cited but not copy-pasted wholesale.

---

## Key Decisions

| Decision | Choice | Why |
|---|---|---|
| Scope of skill set | Full 6-phase lifecycle (+ an architecture skill, 7 total) | Research showed the gap is the whole lifecycle, not just one phase. Tight-focus alternative rejected because users have to stitch content from multiple sources otherwise. |
| Package structure | Multi-skill plugin with shipped runnable tooling | Precedent exists (`skillstack-workflows`). Anthropic's own `plugin-dev` ships a similar shape (1 command + 3 agents + 7 skills). Ships scripts as approach A (no slash commands) to minimize surface area while retaining runnable value. |
| Eval depth | Ship Anthropic-adapted harness + activation-testing guidance | Anthropic's skill-creator ships `run_loop.py`/`run_eval.py` that nobody else has productized. Porting them is high-leverage. Full CI integration rejected as over-ambitious for v1. |
| Hooks coverage | Core 10 events in SKILL.md body, comprehensive 28-event reference file | Progressive disclosure. Full inline coverage would violate Anthropic's 500-line guideline. Split-per-category would fragment the skill. |
| Ideation framing | Problem-first only | Simpler, more opinionated. Tool-first framing is covered by the research skill ("I have this tool, what problem does it solve for me?") rather than as a parallel track. |
| Approach (PDK shape) | Approach A: skills + scripts, no slash commands | Matches the user's clarifying-question answers. Avoids command/skill drift. Scripts can be invoked via Claude-in-the-loop or by users directly. |
| Naming | `plugin-dev` | Matches Anthropic's naming. Namespace scoping (`plugin-dev@skillstack` vs `plugin-dev@claude-plugins-official`) prevents collision. Clear, discoverable, aligns with community expectations. |
| Skill count | 7 skills | Enough to cover each lifecycle phase distinctly without fragmenting. Precedent: Anthropic's plugin-dev has 7, skillstack-workflows has 9, cloud-finops has 26. 7 is in range. |
| Cross-references | Explicit links to `skill-creator`, `mcp-server`, `skillstack-workflows/write-your-own-skill` | Avoids duplication. The new plugin fills gaps, not overlaps. |
| Out: slash commands | Rejected | Approach A chosen over C. Can add in v2 if usage demand warrants. |
| Out: GitHub Actions CI template | Rejected | Approach "Ship harness + activation-testing guidance" chosen over "Full: CI integration". v2. |
| Out: tool-first ideation | Rejected | Problem-first chosen in clarifying questions. Simpler, more opinionated. |
| Hook reference strategy | All 28 events documented in `references/hook-event-reference.md`; core 10 inline | Progressive disclosure. Users loading the skill for PreToolUse work don't pay context cost for FileChanged details. |
| Eval file format | Mirror Anthropic's skill-creator exactly (`evals/evals.json`, `evals/trigger-evals.json`) | Interoperability with Anthropic's own harness. No reason to invent a new format. |

## Research Findings

Deep research was conducted across four parallel streams before writing this PRD. Key findings that shaped the scope:

**1. The authoritative source (Anthropic's PDF)** — *The Complete Guide to Building Skills for Claude* (Jan 2026) defines skills as folders with `SKILL.md` + optional `scripts/`, `references/`, `assets/`. Three-level progressive disclosure: frontmatter always loaded, SKILL.md body on match, references on demand. Three use-case categories: Document/Asset Creation, Workflow Automation, MCP Enhancement. Testing has three areas: triggering, functional, performance comparison. **Does not mention hooks at all.** Does not cover multi-component plugin composition. `skill-creator` is Anthropic's recommended authoring tool and ships an undocumented-but-real eval harness.

**2. Plugin architecture research** — Claude Code plugins have 7 component types: skills, commands, agents, hooks, MCP servers, output styles, LSP servers. `plugin.json` is *optional*; `name` is the only required field. Directory layout is explicit: everything except `plugin.json` goes at plugin root (never inside `.claude-plugin/`). `${CLAUDE_PLUGIN_ROOT}` is substituted at runtime; `${CLAUDE_PLUGIN_DATA}` provides persistence across updates. Real-world examples: `anthropics/claude-code/plugins/plugin-dev` (1 cmd + 3 agents + 7 skills), `hookify` (4 cmds + 1 agent + 1 skill + 4 hooks), `ralph-wiggum` (2 cmds + 1 hook), `feature-dev` (1 cmd + 3 agents). The densest official plugin is `plugin-dev`. The only verified "full-stack" community plugin shipping its own MCP servers is `levnikolaevich/claude-code-skills`.

**3. Hooks research** — Claude Code supports **28 hook events**, not the ~8 commonly cited. Events span session (SessionStart/End, Stop/Failure), tool-loop (PreToolUse, PostToolUse, PermissionRequest/Denied), subagent (SubagentStart/Stop), agent-team (TaskCreated/Completed, TeammateIdle), instructions (InstructionsLoaded, PreCompact/PostCompact), workspace (ConfigChange, CwdChanged, FileChanged, WorktreeCreate/Remove), MCP elicitation (Elicitation/Result). Four handler types: `command` (shell), `http` (POST), `prompt` (LLM), `agent` (tool-equipped subagent, up to 50 turns). Matcher syntax has three modes depending on characters: `*`/`""` matches all, letters/digits/`_`/`|` is exact string or `|`-separated list, any other character is JavaScript regex. **Exit code trap**: Exit 2 blocks for most events; exit 1 is non-blocking (unlike Unix convention). Precedence across hooks: deny > defer > ask > allow. Hooks in plugins live at `hooks/hooks.json` and merge automatically when the plugin is enabled. Plugin-shipped agents cannot include `hooks`, `mcpServers`, or `permissionMode` for security.

**4. Evaluation/validation research** — Structural: `claude plugin validate` is Anthropic's first-party validator (checks `plugin.json`, frontmatter, component location). Community: `hesreallyhim/claude-code-json-schema` provides unofficial JSON schemas. skillstack's own `validate_plugins.py` catches additional cases (frontmatter name mismatch, cross-references, orphan catalog entries). Effectiveness: Anthropic's `skill-creator` ships `run_loop.py`/`run_eval.py`/`aggregate_benchmark` — a real working harness using `evals/evals.json` + `evals/trigger-evals.json`, 60/40 train-test split, 3 runs per query, grader/analyzer/comparator subagent pattern. Community: `TribeAI/claude-evals` ships a production-grade framework with regression severity classification (CRITICAL >20%, HIGH >10%). Real empirical finding from Scott Spence's research: activation is **keyword-biased**, not semantic — descriptions should read like SEO, not prose. Best-practices doc explicit rule: descriptions must be third-person, include both WHAT and WHEN, use specific trigger phrases.

**5. Real-world complex plugins** — Surveyed 10 plugins. Only 3 have real tests (superpowers, OMC, ECC, claude-toolbox). Only 1 (`levnikolaevich`) ships first-party MCP servers. The common "complex plugin" shape is `skills + commands + agents + hooks` — MCP is an advanced mode. Cross-cutting patterns: one skill per extension type (plugin-dev), progressive disclosure inside skills, parallel agent invocation for expensive analysis, validation scripts as runnable executables, kill switches for disabling features without uninstalling, hooks to inject `<system-reminder>` steering, persistent state in scoped directories (`.omc/`).

All four research reports are saved under `/Users/vbezdek/Work/skillstack/.omc/research/` (specifically `anthropic-skills-guide-extracted.txt` for the Anthropic PDF extraction). The source material will be used when writing the reference files inside the plugin.

---

*PRD complete. Ready to hand off to `/spec` for implementation planning.*
