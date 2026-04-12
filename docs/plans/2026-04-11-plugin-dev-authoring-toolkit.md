# Plugin-Dev Authoring Toolkit Implementation Plan

Created: 2026-04-11
Status: PENDING
Approved: Yes
Iterations: 1
Worktree: No
Type: Feature

## Summary

**Goal:** Build a new multi-skill plugin `plugin-dev` in the skillstack repo that fills the gap Anthropic's official guide doesn't cover: plugin ideation/research, multi-component plugin architecture, hook authoring, plugin composition, plugin-level validation, and plugin-level evaluation.

**Architecture:** Multi-skill plugin (same pattern as `skillstack-workflows`). 7 skills under `plugin-dev/skills/`, 4 runnable scripts under `plugin-dev/scripts/`, pytest suite under `plugin-dev/scripts/tests/`. Catalog-registered in both `registry.json` and `marketplace.json`. Scripts adapted from the existing `.github/scripts/validate_plugins.py` and Anthropic's `skill-creator` harness pattern.

**Tech Stack:** Python 3.12 stdlib + PyYAML for scripts, pytest for script tests, bash for `test_hook.sh`, Markdown + YAML frontmatter for skills, JSON for manifests. Optional Anthropic Python SDK for `run_eval.py` (graceful degradation if not installed).

**PRD source:** `docs/prd/2026-04-11-plugin-dev-authoring.md` (246 lines, contains full context, decisions, user flows, and research findings)

## Scope

### In Scope

**Plugin package:**
- `plugin-dev/.claude-plugin/plugin.json` — manifest with Viktor Bezdek as author, v1.0.0, MIT license
- `plugin-dev/README.md` — follows skillstack convention: problem statement, scenario table, when-not-to-use, installation, what's inside, cross-references
- `plugin-dev/skills/` with 7 skills:
  1. `plugin-ideation/`
  2. `plugin-research/`
  3. `plugin-architecture/`
  4. `plugin-hooks/`
  5. `plugin-composition/`
  6. `plugin-validation/`
  7. `plugin-evaluation/`
  Each with `SKILL.md` + `references/` directory containing 2-4 reference files.
- `plugin-dev/scripts/` with 4 runnable tools: `scaffold_plugin.py`, `validate_plugin.py`, `run_eval.py`, `test_hook.sh`
- `plugin-dev/scripts/tests/` with pytest suites for each script (4 test modules)

**Catalog integration:**
- `.claude-plugin/registry.json` — new entry alphabetically between `persona-mapping` and `prioritization`
- `.claude-plugin/marketplace.json` — corresponding new entry
- Root `README.md` — plugin count 51 → 52, new catalog entry in Development section, new row in "Find a skill by goal" goal-routing table

**CI wiring:**
- `.github/workflows/ci.yml` — new job `pytest / plugin-dev` following the skill-creator pattern (working-directory: `plugin-dev/scripts`)

**Research artifacts:**
- Extract relevant portions from the 4 parallel research reports already produced during PRD drafting (hooks research, plugin architecture research, evaluation research, real-world plugins research) into the per-skill `references/` directories as authoritative reference material. Source content lives at `/tmp/anthropic-skills-guide.txt` and in-context from the sub-agent output files.

### Out of Scope

**Not building in this iteration** (explicit per PRD):
- Slash commands (`/plugin-dev:*`) — rejected in favor of plain scripts
- GitHub Actions CI template for user plugins — v2 feature
- MCP server authoring depth — cross-references existing `mcp-server` plugin
- Single-skill authoring depth — cross-references existing `skill-creator` plugin
- Tool-first ideation framing — problem-first only
- Multi-agent system design — cross-references existing `multi-agent-patterns`
- CI regression gating (CRITICAL >20% etc) — the simpler "Ship harness + guidance" option was chosen
- Cross-harness support (Cursor, Codex, OpenCode) — Claude Code only
- Publishing a JSON schema at a stable URL — we don't host one

**Not changing** (explicit non-goals):
- The existing `.github/scripts/validate_plugins.py` — unchanged (duplicate-and-decouple)
- The existing `skill-creator` plugin — unchanged
- The existing `mcp-server` plugin — unchanged
- Other pytest jobs in CI — unchanged

## Approach

**Chosen:** Bottom-up — scripts first, skills second.

**Why:** The scripts' interfaces (`validate_plugin.py --plugin-dir PATH`, `run_eval.py --mode trigger|output`, `test_hook.sh SCRIPT JSON`) affect what the skills teach. Authoring the skills first would mean writing against imagined APIs and then rewriting when reality diverges. By building the scripts first with pytest coverage, the skill authors (us, writing SKILL.md) can cite real command lines with real output shapes. Matches how Anthropic's own `skill-creator` was evidently built (scripts exist and are referenced from SKILL.md as concrete tools).

**Alternatives considered:**
- **Top-down (skills first, scripts second):** Rejected — creates drift between skill content and actual script behavior. Skills would need rewriting after scripts land.
- **Parallel streams (scripts and skills co-developed):** Rejected — requires constant context switching and risks inconsistency between the two streams. Works for a team but not for one implementer following a plan.

## Context for Implementer

> Write for an implementer who has never seen the codebase.

**Patterns to follow:**
- Multi-skill plugin precedent: `skillstack-workflows/` (see `skillstack-workflows/.claude-plugin/plugin.json:1-27` for manifest shape; `skillstack-workflows/skills/pitch-sprint/SKILL.md:1-10` for SKILL.md frontmatter format)
- Validator precedent: `.github/scripts/validate_plugins.py:1-40` (dataclass `Issue`/`Report`, `load_json` with `Report.err`, `parse_frontmatter` without PyYAML dependency)
- Validator tests precedent: `.github/scripts/tests/test_validate_plugins.py:1-50` (synthetic fixtures using tmp_path, `run()` helper function, `create_plugin()` builder function)
- CI job precedent: `.github/workflows/ci.yml:42-56` (the `pytest-skill-creator` job — new job follows exactly this shape)
- Registry entry precedent: `.claude-plugin/registry.json:884-904` (the `skill-creator` entry — fields: `id`, `name`, `type`, `category`, `description`, `repo_id`, `path_in_repo`, `version`, `tags`, `documentation_path`, `status`, `platforms`)
- Marketplace entry precedent: `.claude-plugin/marketplace.json` — same fields as registry but without `id`/`repo_id`/`documentation_path`/`status`/`platforms`

**Conventions:**
- Skill naming: kebab-case, no capitals, no underscores
- SKILL.md body: aim for ≤220 lines (recent repo norm); push content to `references/` if longer
- Frontmatter description: must include WHAT and WHEN; front-load key use case in first 250 chars; third-person only ("no I/my/we"); no `<>` XML tags
- File naming: `SKILL.md` exactly (case-sensitive); never `README.md` inside a skill folder (that's reserved for the plugin root)
- Reference files: each opens with a blockquote explaining scope; end with "Further reading" section citing real sources; footer line naming Viktor Bezdek as author
- Validator error scoping: for multi-skill plugins, errors in sub-skills get scoped as `plugin/skill` (e.g., `plugin-dev/plugin-hooks`); see `validate_plugins.py:155-175`
- README scenario table format: `| You say... | The skill provides... |` header

**Key files:**
- `.github/scripts/validate_plugins.py` — the existing repo-level validator. `plugin-dev/scripts/validate_plugin.py` will be a duplicated-and-decoupled variant. Do NOT modify the existing file.
- `.github/scripts/tests/test_validate_plugins.py` — template for pytest fixture style
- `skillstack-workflows/README.md` — template for plugin README structure (especially the scenario table, "when not to use" section, and the installation block with `/plugin marketplace add` + `/plugin install` commands)
- `/tmp/anthropic-skills-guide.txt` — the extracted PDF from Anthropic (1124 lines). Source for reference files in `plugin-validation`, `plugin-composition`, `plugin-evaluation`.
- `docs/prd/2026-04-11-plugin-dev-authoring.md` — the authoritative spec; re-read if task requirements are unclear
- Research output files under `/private/tmp/claude-503/-Users-vbezdek-Work-skillstack/b3964351-deed-40d8-b185-0fb70daa0cee/tasks/` — the 4 sub-agent reports from the PRD phase (hooks, plugin arch, evaluation, real plugins)

**Gotchas:**
- **Multi-skill plugin registry path**: `path_in_repo` is the plugin root (`"plugin-dev"`) NOT the skill path. The `skillstack-workflows` entry at `registry.json:906-930` is the correct precedent — its `path_in_repo` is `"skillstack-workflows"`.
- **Validator ignores `.omc` and `.github`**: the existing validator has `NON_PLUGIN_ROOT_DIRS` list. The new `plugin-dev` directory will be auto-discovered as a plugin on first run of `validate_plugins.py`.
- **Validator expects catalog entries**: after `plugin-dev` is created, running `python3 .github/scripts/validate_plugins.py` will error until the registry/marketplace entries are added. **Task ordering matters** — don't create the plugin directory without staging the catalog entries in the same task.
- **README plugin count check**: validator enforces header count claims match plugin count. After adding `plugin-dev`, the root README must say "52 plugins" (currently 51) or CI fails.
- **Frontmatter `name` must match directory**: `plugin-dev/skills/plugin-ideation/SKILL.md` must have `name: plugin-ideation` in frontmatter. Validator errors on mismatch with plugin/skill scope (e.g., `plugin-dev/plugin-ideation`).
- **Scripts without external deps**: `scaffold_plugin.py` and `validate_plugin.py` should use only stdlib + pyyaml. `run_eval.py` optionally uses the `anthropic` SDK but must gracefully degrade (print "not implemented in offline mode" and exit) if not installed — the CI environment will not have API keys.
- **Scripts must be executable when applicable**: `test_hook.sh` needs `chmod +x` or the ShellCheck job will flag it.
- **ShellCheck will run on `test_hook.sh`**: the existing CI has a ShellCheck job that runs against all `*.sh` files. The hook-tester script must pass `shellcheck --severity=error` (SC1087 array braces, SC2144 no `-f` with globs, SC2218 function ordering).
- **Reference file line budgets**: ~150-250 lines per reference is the norm. Anthropic's research PDF is 1100+ lines — distribute into 3-5 references, not one mega-file.

**Domain context:**
- This plugin is meta: it's a plugin about building plugins. Users install it when they want to build their own Claude Code plugins.
- The name `plugin-dev` matches Anthropic's own official `plugin-dev` plugin (from `anthropics/claude-code/plugins/plugin-dev`). Namespace scoping prevents collision: users install ours as `plugin-dev@skillstack`, Anthropic's as `plugin-dev@claude-plugins-official`. Both can coexist.
- The 7 skills are designed to activate independently based on their frontmatter descriptions. Users may invoke just one (e.g., "help me write a PostToolUse hook" → `plugin-hooks` activates) without touching the others.

## Baseline State (verified 2026-04-11)

- Current branch: `main` at commit `9c762cd` (skillstack-workflows ship)
- `git ls-files elicitation/` returns committed files — elicitation IS tracked
- `python3 .github/scripts/validate_plugins.py` → "Discovered 51 plugin directories. All plugin validation checks passed."
- Root README `README.md` line count: 409 lines
- Plugin count appears as literal `51` at **six** line locations (not four): 3, 7, 45, 159, 161, 356 — verified via `grep -n '51\b'`
- The critic's spec-review flagged the 4-location claim as under-counted; this plan now correctly lists all six
- Catalog: 51 plugin entries in `registry.json` (plus 8 collections), 51 entries in `marketplace.json`

## Assumptions

- **Repo is on `main`, clean** — verified above. Task 0 re-verifies as a gate before Task 1.
- **Python 3.12 is available in CI** — supported by: `.github/workflows/ci.yml:16-18` sets `python-version: "3.12"` for every pytest job. Task 2 (validator script + tests) depends on this.
- **PyYAML is acceptable as a dependency** — supported by: skill-creator's pytest job at `ci.yml:52-56` installs `pyyaml`. Task 3 (scripts using YAML parsing) depends on this.
- **`anthropic` Python SDK is NOT required in CI** — supported by: PRD decision that `run_eval.py` must gracefully degrade. CI won't have API keys, so `run_eval.py` tests use mocked responses. Tasks 4 and 8 depend on this.
- **The existing validator's `discover_plugin_directories` will auto-discover `plugin-dev/`** — supported by: `validate_plugins.py:143-160` (walks repo root, filters `NON_PLUGIN_ROOT_DIRS`, looks for `.claude-plugin/plugin.json`). Means Task 11 (catalog wiring) must land in the same commit as Task 1 or `plugin-validation` CI job will fail.
- **Anthropic PDF extract at `/tmp/anthropic-skills-guide.txt` survives the implementation session** — supported by: `/tmp` persists across tool invocations in the same session. Tasks 5-9 (skill authoring) depend on this for authoritative source material. Backup: re-extract from `~/.claude/projects/-Users-vbezdek-Work-skillstack/.../tool-results/webfetch-*.pdf`.
- **Research sub-agent outputs are readable via file paths** — supported by: sub-agents wrote to `/private/tmp/claude-503/-Users-vbezdek-Work-skillstack/b3964351-deed-40d8-b185-0fb70daa0cee/tasks/*.output`. Tasks 5-9 depend on this for hook event reference, real-plugin examples, etc. If these files are gone, fall back to the summaries embedded in the PRD.

## Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Validator fails on first CI run because catalog entries are missing | HIGH | HIGH | Land Tasks 1 and 11 in the same commit. Task 11 is explicitly ordered before first `git add` of `plugin-dev/`. Pre-commit dry run of `python3 .github/scripts/validate_plugins.py` required. |
| ShellCheck fails on `test_hook.sh` due to common bash gotchas | MEDIUM | MEDIUM | Follow the patterns established in the `ai-slop-cleaner`/`git-workflow` bash scripts. Run `shellcheck --severity=error plugin-dev/scripts/test_hook.sh` locally before commit. The three error classes already caught in the repo (SC1087 array, SC2144 `-f` globs, SC2218 function order) must all be addressed. |
| `run_eval.py` tests fail in CI due to missing `anthropic` SDK | MEDIUM | MEDIUM | Test fixtures mock all SDK calls. `run_eval.py` checks `try: import anthropic except ImportError:` and exits with a helpful message in offline mode. Tests assert on both modes. |
| Skill frontmatter descriptions trigger false positives (skill activates for wrong queries) | MEDIUM | MEDIUM | Apply the research finding that Claude's activation is keyword-biased — include concrete trigger phrases and explicit negative triggers ("NOT for X, use Y instead"). Lint during task 5 onwards: verify first 250 chars of each description contain the primary keyword. |
| Reference files exceed context budget when loaded | LOW | MEDIUM | Enforce ≤250 lines per reference file (slightly above the 220-line SKILL.md soft limit because references are loaded selectively). 3-5 references per skill max. |
| `scaffold_plugin.py` generates invalid plugin (fails validation when run against output) | MEDIUM | HIGH | Scaffolder tests include a post-generate validation step: scaffolder runs, then `validate_plugin.py` runs against the scaffolder output, asserts zero errors. Test file: `test_scaffold_plugin.py::test_scaffolded_plugin_passes_validation`. |
| Root README plugin count drifts (says 51 instead of 52 after adding plugin-dev) | HIGH | LOW | Task 1 explicitly updates the count in SIX literal-51 locations plus the Development section count (line 226 area) plus the plugin backtick list (line 163): lines 3, 7, 45, 159, 161, 356 for `51` → `52`, line 163 for alphabetical insertion, and Development section header count. Validator catches the three patterns it recognizes; the other three prose mentions and the backtick list and the section header require manual grep verification (`grep -c '\b51\b' README.md` must return 0 post-Task-1). |
| Validator for `plugin-dev/scripts/validate_plugin.py` duplicates logic that will drift from the repo validator | MEDIUM | MEDIUM | **Upgraded from LOW/LOW per critic finding #5**: repo already has two validators that don't share tests. Adding a third compounds the risk. Mitigation: `test_validator_drift.py` contract test (Task 6) runs both validators against `skillstack-workflows/` and asserts compatible output. Header comment documents base commit SHA. Future consolidation into a shared module is a follow-up. |
| Skill cross-references to scripts cite wrong paths | LOW | MEDIUM | SKILL.md reference paths must be relative to the plugin root and use the form `scripts/validate_plugin.py` (not absolute). Verify with validator's cross-reference check (`references/X.md` cited in SKILL.md must exist). |
| Alphabetical insertion mismatch across registry.json / marketplace.json / README plugin list / README Development section | MEDIUM | MEDIUM | **New row per critic finding #20.** Task 1 touches 4 places that must agree on alphabetical position. Mitigation: Task 1 explicitly names all 4 insertion points and runs the validator which catches catalog drift. Implementer must manually verify README backticked list order after editing. |
| Task 8 reference invents hook events that don't exist in Anthropic's live docs | MEDIUM | HIGH | **New row per critic finding #7.** Mitigation: Task 8 pre-step WebFetches docs.claude.com/en/docs/claude-code/hooks before writing any content. Anti-fabrication DoD: every event name in the references must be grep-matchable to a cited URL in the same file. Reviewer/implementer runs this grep before commit. |
| `run_eval.py` offline mode produces tautological numbers users mistake for real eval scores | HIGH | HIGH | **New row per critic finding #4.** Mitigation: offline mode FORCES smoke-only mode; cannot compute trigger precision/recall at all; benchmark.md output has a SYNTHETIC BANNER at the top; benchmark.json has `"mode": "offline"` and `"warning": "synthetic results"` fields. User opt-in for trigger/output modes requires online SDK + API key. |
| `test_hook.sh` silently skips timeout tests on macOS without coreutils | MEDIUM | MEDIUM | **New row per critic finding #9.** Mitigation: tests fail loudly with `brew install coreutils` guidance rather than skip. No silent pass for an untested code path. |

## Goal Verification

### Truths

1. **The `plugin-dev` plugin exists in the skillstack catalog and installs via `/plugin install plugin-dev@skillstack`.** User can run `/plugin marketplace add viktorbezdek/skillstack` then `/plugin install plugin-dev@skillstack` without errors. Verified by: presence of entries in both `registry.json` and `marketplace.json`, plus successful local validation via `python3 .github/scripts/validate_plugins.py`.

2. **All 7 skills activate on their intended triggers and are scoped to independent concerns.** Verified by: each skill's `SKILL.md` exists with valid frontmatter, frontmatter `name` matches directory name, descriptions contain the trigger phrases listed in the PRD for that skill. Validator passes for all 7 skills with multi-skill scoping.

3. **All 4 scripts are runnable and pass their own pytest suites.** Verified by: `cd plugin-dev/scripts && pytest tests/ -q` returns exit 0 with ≥12 tests passing (4 scripts × ≥3 tests each).

4. **The validator in `plugin-dev/scripts/validate_plugin.py` correctly validates a plugin directory.** Verified by: running it against `skill-creator/` (known-good plugin) reports 0 errors; running it against a synthetic broken plugin in tmp_path reports the expected errors. Covered by `test_validate_plugin.py`.

5. **The scaffolder in `plugin-dev/scripts/scaffold_plugin.py` generates a valid plugin skeleton.** Verified by: running it with `--name test-plugin --skills foo,bar`, then validating the output with `validate_plugin.py`, reports 0 errors. Covered by `test_scaffold_plugin.py::test_scaffolded_plugin_passes_validation`.

6. **The hook tester `test_hook.sh` correctly smoke-tests hook scripts.** Verified by: running it against a trivial hook script that echoes `{"ok":true}` and exits 0 — assertions on expected exit code and output JSON shape pass. Covered by `test_test_hook.sh`.

7. **The eval runner `run_eval.py` correctly computes trigger precision/recall.** Verified by: running it with a mock eval set where the ground truth is known, asserting the computed pass rates match. Uses mocked SDK responses. Covered by `test_run_eval.py`.

8. **Full CI pipeline passes on the commit that ships the plugin.** Verified by: `gh run watch <run-id> --exit-status` returns 0. All existing jobs (shellcheck, plugin-validation, pytest-skill-creator, pytest-docker, pytest-mcp, Node.js test) plus new job (pytest / plugin-dev) are green.

9. **The plugin content is grounded in authoritative sources and does not fabricate information.** Verified by: every reference file cites real URLs (Anthropic docs, Claude Code docs, community sources). Sources come from the 4 sub-agent research reports and the Anthropic PDF extract. Implementer does not invent hook events, handler types, or file paths that aren't in the authoritative sources.

### Artifacts

- `plugin-dev/.claude-plugin/plugin.json` — manifest
- `plugin-dev/README.md` — plugin README
- `plugin-dev/skills/{ideation,research,architecture,hooks,composition,validation,evaluation}/SKILL.md` × 7 — skill files
- `plugin-dev/skills/*/references/*.md` — reference files (14-28 total)
- `plugin-dev/scripts/scaffold_plugin.py`
- `plugin-dev/scripts/validate_plugin.py`
- `plugin-dev/scripts/run_eval.py`
- `plugin-dev/scripts/test_hook.sh` (executable)
- `plugin-dev/scripts/tests/test_scaffold_plugin.py`
- `plugin-dev/scripts/tests/test_validate_plugin.py`
- `plugin-dev/scripts/tests/test_run_eval.py`
- `plugin-dev/scripts/tests/test_test_hook.sh` (or `.py` wrapper)
- `.claude-plugin/registry.json` — new entry for plugin-dev
- `.claude-plugin/marketplace.json` — new entry for plugin-dev
- `README.md` — updated plugin count + new catalog entry + new goal-routing table row
- `.github/workflows/ci.yml` — new `pytest / plugin-dev` job

## Progress Tracking

- [x] Task 0: Preflight gate (must pass before any changes)
- [x] Task 1: Plugin scaffolding — directories, plugin.json, README stub, catalog entries (minimum viable registration)
- [x] Task 2: `validate_plugin.py` — duplicate-and-decouple from repo validator (with drift contract)
- [x] Task 3: `scaffold_plugin.py` — interactive plugin skeleton generator (deterministic)
- [x] Task 4: `run_eval.py` — activation + output eval harness; offline-smoke mode only (no tautological numbers)
- [x] Task 5: `test_hook.sh` — mock-stdin hook tester (default 15s timeout)
- [x] Task 6: pytest suites for all 4 scripts + drift contract test + fixture anchor
- [x] Task 7: `plugin-validation` skill + references
- [x] Task 8: `plugin-hooks` skill + references (with live docs fetch + anti-fabrication grep check)
- [x] Task 9: `plugin-evaluation` skill + references
- [x] Task 10: `plugin-architecture` skill + references
- [x] Task 11: `plugin-composition` skill + references
- [x] Task 12: `plugin-ideation` skill + references
- [x] Task 13: `plugin-research` skill + references
- [x] Task 14: CI wiring — `pytest / plugin-dev` job in `.github/workflows/ci.yml`
- [x] Task 15: Final polish — plugin README update with full scenario table, root README catalog entry row, full validation pass

**Total Tasks:** 16 | **Completed:** 16 | **Remaining:** 0

## Implementation Tasks

### Task 0: Preflight gate (must pass before Task 1)

**Objective:** Verify the baseline state before making any changes. If any check fails, STOP and report — do not proceed to Task 1.

**Dependencies:** None

**Files:** None (read-only checks)

**Verify (this IS the task):**

```bash
# 1. Clean working tree (no tracked modifications)
git diff --quiet HEAD && git diff --cached --quiet || echo "DIRTY — STOP"

# 2. elicitation committed
git ls-files elicitation/ | grep -q '\.claude-plugin/plugin.json' || echo "elicitation missing — STOP"

# 3. Validator baseline passes with exactly 51 plugins
python3 .github/scripts/validate_plugins.py 2>&1 | grep -q "Discovered 51 plugin directories" || echo "baseline wrong — STOP"
python3 .github/scripts/validate_plugins.py 2>&1 | grep -q "All plugin validation checks passed" || echo "baseline errors — STOP"

# 4. Validator self-tests pass
python3 -m pytest .github/scripts/tests/ -q 2>&1 | tail -1 | grep -q "passed" || echo "validator tests fail — STOP"

# 5. README has exactly six '51' occurrences at expected lines
grep -c '\b51\b' README.md  # must be >= 6
grep -n '\b51\b' README.md  # document the actual lines for Task 1
```

**Definition of Done:**
- [ ] All 5 checks pass
- [ ] Exact README line numbers with `51` are recorded in the task's notes for Task 1 to use

**If any check fails:** STOP, do not proceed. The plan's entire task ordering depends on these invariants.

---

### Task 1: Plugin scaffolding (minimum-viable registration)

**Objective:** Create the plugin directory skeleton and the catalog entries in the same commit so the validator has a consistent view. After this task, `python3 .github/scripts/validate_plugins.py` passes with 52 plugins discovered. **ALL `51` references in README must become `52`, including prose mentions the validator doesn't check.**

**Dependencies:** Task 0 (preflight gate)

**Files:**
- Create: `plugin-dev/.claude-plugin/plugin.json`
- Create: `plugin-dev/README.md` (stub — full content lands in Task 15)
- Create: `plugin-dev/skills/plugin-validation/SKILL.md` (minimal but REAL — valid frontmatter + genuine short body; will be expanded in Task 7, not replaced)
- Create: `plugin-dev/scripts/.gitkeep` (so the directory exists for Tasks 2-6)
- Modify: `.claude-plugin/registry.json` (add new entry between `persona-mapping` and `prioritization`)
- Modify: `.claude-plugin/marketplace.json` (add corresponding new entry — SAME version string byte-for-byte)
- Modify: `README.md` (plugin count 51 → 52 in ALL SIX locations listed below; add new catalog entry row; full scenario table deferred to Task 15)
- Modify: `README.md` (Development catalog section — increment `### 💻 Development (N)` count from current 11 to 12)

**Key Decisions / Notes:**
- `plugin.json` follows the shape at `skillstack-workflows/.claude-plugin/plugin.json:1-27`. Fields: `name: plugin-dev`, `version: 1.0.0`, `description: ...`, `author: { name: "Viktor Bezdek", url: "https://github.com/viktorbezdek" }`, `license: MIT`, `repository: "https://github.com/viktorbezdek/skillstack/tree/main/plugin-dev"`, `keywords: ["claude-code","skill","plugin-development","plugin-authoring","hooks","mcp","evaluation","validation",...]`
- Registry entry: category `development`, `path_in_repo: "plugin-dev"` (NOT `plugin-dev/skills/plugin-dev` — multi-skill plugin root), `version: "1.0.0"` (byte-equal to plugin.json), tags mirror the plugin.json keywords, `documentation_path: "./plugin-dev/README.md"`, `status: "active"`, `platforms: ["claude-code"]`, `repo_id: "viktorbezdek-skillstack"` (match existing entries)
- Marketplace entry: same fields minus `id`/`repo_id`/`documentation_path`/`status`/`platforms`; `version` must byte-match plugin.json
- **Placeholder skill, corrected from review:** write a REAL minimal SKILL.md, not a "this is a placeholder" body. The frontmatter description must be a genuine sentence describing plugin validation ("Validates the structural correctness of Claude Code plugins — plugin.json, SKILL.md frontmatter, reference cross-checks. Use when you want to check whether a plugin is well-formed before shipping."). The body is a 5-10 line explanation of the skill's purpose. Task 7 expands it, not replaces it. This avoids shipping a catalog entry whose description says "Placeholder".
- **Exact README line numbers** (from Task 0 preflight record) — verified at commit 9c762cd, current state:
  - Line 3: `51 expert plugins` → `52 expert plugins`
  - Line 7: `**51** plugins · **8** categories` → `**52** plugins · **8** categories`
  - Line 45: `all of the 51 SkillStack plugins` → `all of the 52 SkillStack plugins`
  - Line 159: `<summary><strong>SkillStack</strong> — 51 plugins</summary>` → `52 plugins`
  - Line 161: `51 expert skills for Claude Code` → `52 expert skills for Claude Code`
  - Line 163: plugin backtick list — insert `` `plugin-dev`, `` alphabetically between `` `persona-mapping`, `` and `` `prioritization`, ``
  - Line 226 (approximate — grep `### 💻 Development`): `### 💻 Development (11)` → `### 💻 Development (12)`
  - Line 356: `all 51 plugins become available` → `all 52 plugins become available`
- **Task 0's grep recorded the exact lines.** Implementer MUST re-run `grep -n '\b51\b' README.md` at start of Task 1 to catch any drift between the plan's recorded numbers and the current file state.
- Critical: run `python3 .github/scripts/validate_plugins.py` locally BEFORE committing to verify the catalog changes are consistent with the directory
- Post-Task-1 invariant: `grep -c '\b51\b' README.md` must return 0; `grep -c '\b52\b' README.md` must return ≥ 6

**Definition of Done:**
- [ ] `plugin-dev/.claude-plugin/plugin.json` exists, valid JSON, has `name`, `version`, `description`, `author`, `license`, `keywords`
- [ ] `plugin-dev/skills/plugin-validation/SKILL.md` exists with VALID frontmatter (real description, not placeholder copy); body is a genuine 5-10 line explanation
- [ ] Frontmatter `name` equals directory name (`plugin-validation`)
- [ ] `plugin-dev/README.md` exists with at least title, status, and stub content
- [ ] `.claude-plugin/registry.json` has new entry for `plugin-dev` at correct alphabetical position
- [ ] `.claude-plugin/marketplace.json` has corresponding new entry
- [ ] **Version equality verified**: `python3 -c "import json; p=json.load(open('plugin-dev/.claude-plugin/plugin.json'))['version']; r=next(x for x in json.load(open('.claude-plugin/registry.json'))['plugins'] if x['id']=='plugin-dev')['version']; m=next(x for x in json.load(open('.claude-plugin/marketplace.json'))['plugins'] if x['name']=='plugin-dev')['version']; assert p==r==m, f'version drift: {p} vs {r} vs {m}'"` exits 0
- [ ] `grep -c '\b51\b' README.md` returns `0` (no stray 51 references remain)
- [ ] `grep -c '\b52\b' README.md` returns at least 6
- [ ] `### 💻 Development` section header in README shows count 12
- [ ] Root README line 163 backticked plugin list contains `` `plugin-dev` `` between `` `persona-mapping` `` and `` `prioritization` ``
- [ ] `python3 .github/scripts/validate_plugins.py` exits with code 0 and reports 52 plugins discovered
- [ ] `python3 -m pytest .github/scripts/tests/ -q` still passes (no regression)

**Verify:**
- `grep -n '\b51\b' README.md`  # must be empty
- `grep -c '\b52\b' README.md`  # must be >= 6
- `python3 .github/scripts/validate_plugins.py`
- `python3 -m pytest .github/scripts/tests/ -q`
- `python3 -c "import json; ..."  # the version equality one-liner above`

---

### Task 2: `validate_plugin.py` — duplicate-and-decouple variant of repo validator

**Objective:** Create a standalone validator that accepts `--plugin-dir PATH` and validates a single plugin directory against the structural contract. Independent of skillstack's catalog — no registry/marketplace checks, no root README count check.

**Dependencies:** Task 1 (so `plugin-dev/scripts/` exists)

**Files:**
- Create: `plugin-dev/scripts/validate_plugin.py`

**Key Decisions / Notes:**
- Base on `.github/scripts/validate_plugins.py`. Copy the following: `Issue`/`Report` dataclasses, `load_json`, `parse_frontmatter`, `validate_skill`, `validate_plugin` (skill-level validation only).
- Remove: `validate_catalog`, `validate_root_readme`, `discover_plugin_directories` (walks repo), `NON_PLUGIN_ROOT_DIRS`, `REGISTRY_PATH`/`MARKETPLACE_PATH`/`ROOT_README`.
- CLI: `argparse` with flags `--plugin-dir PATH` (required), `--strict` (fail on warnings), `--json` (output as JSON).
- Header comment: "Adapted from .github/scripts/validate_plugins.py at commit <SHA>. Independent contract: does not require catalog entries, no root README count check. Part of the plugin-dev authoring toolkit."
- Exit codes: 0 = all pass, 1 = errors found, 2 = validator crashed, 3 = `--strict` mode and warnings present.
- Output: human-readable report by default; `--json` outputs `{"errors": [...], "warnings": [...]}`.
- Must support both single-skill plugins (`skills/{plugin-name}/`) and multi-skill plugins (multiple subdirs under `skills/`).
- Performance-safe: no hot-path concerns (runs once per invocation). No external deps beyond stdlib.

**Definition of Done:**
- [ ] `plugin-dev/scripts/validate_plugin.py` exists, is executable (`#!/usr/bin/env python3`)
- [ ] Header comment explicitly documents: "Adapted from .github/scripts/validate_plugins.py at commit 9c762cd. Independent contract: does not walk the whole repo, takes --plugin-dir argument, no catalog or root README checks. Drift from the repo validator is monitored by a contract test at tests/test_validator_drift.py."
- [ ] Runs `python3 plugin-dev/scripts/validate_plugin.py --plugin-dir skill-creator/` and reports 0 errors (skill-creator is known-good)
- [ ] Runs `python3 plugin-dev/scripts/validate_plugin.py --plugin-dir skillstack-workflows/` and reports 0 errors (multi-skill plugin, known-good)
- [ ] CLI accepts `--plugin-dir`, `--strict`, `--json` flags
- [ ] `--json` output is valid JSON
- [ ] Exit code 1 on errors, 0 on success
- [ ] No imports beyond stdlib (no pyyaml, no anthropic)

**Drift mitigation (critic finding #5):** The repo already has two validators (`.github/scripts/validate_plugins.py` and `skill-creator/skills/skill-creator/scripts/validate_skill.py`). Adding a third creates a maintenance triangle. Task 6 includes a `test_validator_drift.py` that runs both `plugin-dev/scripts/validate_plugin.py` and `.github/scripts/validate_plugins.py` against `skillstack-workflows/` and asserts the error sets are congruent for overlapping checks (the repo validator additionally does catalog checks which the new one intentionally omits). If the test fails later, that's the drift signal.

**Verify:**
- `python3 plugin-dev/scripts/validate_plugin.py --plugin-dir skill-creator/`
- `python3 plugin-dev/scripts/validate_plugin.py --plugin-dir skillstack-workflows/`
- `python3 plugin-dev/scripts/validate_plugin.py --plugin-dir plugin-dev/`  (must pass — plugin is self-valid at this point)

---

### Task 3: `scaffold_plugin.py` — interactive plugin skeleton generator

**Objective:** Create a CLI script that generates a minimum-viable plugin skeleton matching the skillstack contract. Output must pass `validate_plugin.py`.

**Dependencies:** Task 2 (scaffolder validates its own output)

**Files:**
- Create: `plugin-dev/scripts/scaffold_plugin.py`

**Key Decisions / Notes:**
- CLI: `python3 scaffold_plugin.py --name NAME [--skills A,B,C] [--hooks EVENT1,EVENT2] [--mcp] [--author "Name"] [--author-url URL] [--output-dir PATH]`
- `--name` required. `--skills` defaults to the plugin name (single-skill plugin). `--output-dir` defaults to `.` (cwd).
- Produces:
  - `{output_dir}/{name}/.claude-plugin/plugin.json` with author, version `0.1.0`, description based on name, license MIT
  - `{output_dir}/{name}/skills/{skill}/SKILL.md` stub for each named skill — valid frontmatter, body with placeholders `## When to use this skill`, `## Core principle`, `## How to use this skill`
  - `{output_dir}/{name}/hooks/hooks.json` stub with named events if `--hooks` given (otherwise skip)
  - `{output_dir}/{name}/.mcp.json` stub if `--mcp` flag given
  - `{output_dir}/{name}/README.md` with sections pre-filled from manifest (title, problem statement placeholder, installation block with `/plugin marketplace add ...` and `/plugin install name@marketplace`, what's inside, cross-references)
  - `{output_dir}/{name}/scripts/` and `{output_dir}/{name}/assets/` empty directories (just create them)
- Post-generation: run `validate_plugin.py --plugin-dir {output_dir}/{name}/` internally and print the result. If errors, exit non-zero with a helpful message.
- Error handling: if `{output_dir}/{name}/` already exists, refuse with clear message "Directory exists. Use --force to overwrite or choose a different name." `--force` flag supported but NOT default.
- Interactive mode: if no `--name` given, prompt for it. But non-interactive is the primary path.
- Idempotency: same invocation with same args twice should produce same output (deterministic).

**Definition of Done:**
- [ ] `plugin-dev/scripts/scaffold_plugin.py` exists and is executable
- [ ] `python3 scaffold_plugin.py --name test-alpha --output-dir /tmp/scaffold-test` produces a complete plugin directory
- [ ] Generated plugin passes `validate_plugin.py --plugin-dir /tmp/scaffold-test/test-alpha/`
- [ ] `--skills a,b` creates two skill directories
- [ ] `--hooks PreToolUse,PostToolUse` creates `hooks/hooks.json` with both events
- [ ] `--mcp` creates `.mcp.json`
- [ ] Refuses to overwrite existing directory without `--force`
- [ ] No stdlib-external imports beyond `pyyaml` (for YAML generation)

**Verify:**
- `python3 plugin-dev/scripts/scaffold_plugin.py --name test-alpha --skills foo,bar --hooks PreToolUse --output-dir /tmp/scaffold-test`
- `python3 plugin-dev/scripts/validate_plugin.py --plugin-dir /tmp/scaffold-test/test-alpha/`
- `rm -rf /tmp/scaffold-test`

---

### Task 4: `run_eval.py` — activation + output eval harness

**Objective:** Create a CLI script that runs trigger activation evals and output quality evals against a skill, following the Anthropic skill-creator pattern. Gracefully degrades in offline mode when `anthropic` SDK is not installed.

**Dependencies:** Task 2 (reads the same frontmatter parsing utilities conceptually; does NOT import from validate_plugin.py)

**Files:**
- Create: `plugin-dev/scripts/run_eval.py`

**Key Decisions / Notes:**
- CLI: `python3 run_eval.py --plugin-dir PATH --skill SKILL_NAME [--mode trigger|output|both|smoke] [--workspace DIR] [--model MODEL] [--max-iterations N] [--offline] [--verbose]`
- Default mode: `both` when online; **forces `smoke`** when offline (the critic's finding #4).
- Default workspace: `/tmp/plugin-eval-workspace`. Default model: `claude-sonnet-4-5`.
- Reads `{plugin-dir}/skills/{skill-name}/evals/evals.json` (output eval cases, shape: `[{query, files, expected_behavior}]`) and `{plugin-dir}/skills/{skill-name}/evals/trigger-evals.json` (trigger cases, shape: `[{query, should_trigger}]`).
- **Online mode** (anthropic SDK installed + API key present): For trigger mode: 60/40 train/test split, run each query 3 times, compute precision/recall/pass rate. For output mode: spawn with_skill and without_skill subagents per eval, grader returns `{expectations: [{text, passed, evidence}]}`.
- **Offline mode (`--offline` or SDK unavailable) = SMOKE mode only.** This is a critical correction from the v1 plan. Offline mode:
  - **Does NOT compute trigger precision/recall.** A stub that checks "does the description contain the keyword" is tautological — the description ALWAYS passes queries that embed its keywords. Such numbers mislead users.
  - **Instead, runs structural smoke checks:** (a) eval files are valid JSON matching the expected schema, (b) each trigger query has a `should_trigger` boolean, (c) each output eval has the three required fields, (d) the skill's frontmatter description is non-empty, front-loads its first 250 chars, and is third-person.
  - **Outputs a benchmark report flagged with a LOUD SYNTHETIC BANNER:** the top of `benchmark.md` is:
    ```
    ⚠️ OFFLINE MODE — STRUCTURAL SMOKE TEST ONLY
    These results do NOT measure real skill activation or output quality.
    Real evaluation requires ANTHROPIC_API_KEY and the anthropic SDK.
    This run only validates that eval files are well-formed and
    the skill description meets basic quality criteria.
    ```
  - **JSON benchmark has `{"mode": "offline", "warning": "synthetic results — structural checks only", ...}` at the top level.** Consumers parsing the JSON can detect offline runs trivially.
- **Online-mode full harness:** For trigger mode, 60/40 train/test split; run each query 3 times against a real model with the skill activated; compute precision/recall. For output mode: spawn with_skill and without_skill subagents per eval, grader subagent returns `{expectations: [...]}`.
- Output (both modes): `{workspace}/iteration-{N}/` directory tree with `eval-{i}-{slug}/with_skill/outputs/`, `eval-{i}-{slug}/without_skill/outputs/`, `eval_metadata.json`, `benchmark.json`, `benchmark.md`.
- Imports: `try: import anthropic except ImportError:` → set module-level `OFFLINE_REASON = "anthropic SDK not installed"`. Also check `ANTHROPIC_API_KEY` env var; if absent, set `OFFLINE_REASON = "ANTHROPIC_API_KEY not set"` even if SDK is installed.
- Exit codes: 0 = success (including successful smoke test), 1 = eval file missing/invalid, 2 = no skill with that name, 3 = `--mode trigger|output|both` explicitly requested while offline (must opt into `--mode smoke` or omit `--offline`)
- Test harness (for Task 6): all real SDK calls must be patched via monkeypatch. Tests cover both offline-smoke and mocked-online modes.
- **Plugin-evaluation SKILL.md (Task 9) MUST document**: "Offline mode runs structural smoke checks only. Never report offline-mode numbers as activation rates. Real evaluation requires API credentials."

**Fixture anchor (critic finding #10):** Ship an inline example eval pair at `plugin-dev/scripts/tests/fixtures/example-evals/` with 3 trigger queries (2 positive, 1 negative) and 1 output case. Task 6's `test_run_eval.py` uses this fixture. Task 9's plugin-evaluation skill's own eval files are modeled on this fixture — schemas are locked by the fixture, not reinvented in Task 9.

**Definition of Done:**
- [ ] `plugin-dev/scripts/run_eval.py` exists and is executable
- [ ] CLI accepts all documented flags including `--mode smoke`
- [ ] Gracefully handles missing `anthropic` SDK (prints a specific offline-reason message, falls back to smoke mode)
- [ ] Gracefully handles missing `ANTHROPIC_API_KEY` even with SDK installed (same fallback)
- [ ] Offline smoke mode detects all 4 structural issues: malformed eval JSON, missing `should_trigger` field, missing output eval fields, description quality issues
- [ ] Offline mode output JSON contains `"mode": "offline"` and `"warning": "synthetic results — structural checks only"` at the top level
- [ ] Offline mode benchmark.md starts with the SYNTHETIC BANNER (match the literal text)
- [ ] `--mode trigger` with `--offline` set exits 3 with a clear error message (must explicitly request smoke)
- [ ] Exit codes correct for missing eval files
- [ ] No crash on empty eval files
- [ ] Fixture directory `plugin-dev/scripts/tests/fixtures/example-evals/` exists with example trigger-evals.json and evals.json

**Verify:**
- `python3 plugin-dev/scripts/run_eval.py --plugin-dir plugin-dev --skill plugin-validation --mode trigger --offline` (once eval files exist in Task 7)
- Early-task verification (before Task 7): create a fake eval file in tmp_path, run the script, assert output is well-formed

---

### Task 5: `test_hook.sh` — mock-stdin hook tester

**Objective:** Create a bash script that pipes mock event JSON to a hook script on stdin, captures exit code and output, and asserts expectations.

**Dependencies:** Task 2 (so `plugin-dev/scripts/` exists)

**Files:**
- Create: `plugin-dev/scripts/test_hook.sh` (executable: `chmod +x`)

**Key Decisions / Notes:**
- CLI: `bash test_hook.sh SCRIPT_PATH '{"tool_name":"...","tool_input":{...}}' [--expect-exit N] [--expect-output JSON_PATH] [--expect-stderr TEXT] [--timeout SECONDS]`
- Defaults: expected exit 0, no output assertions, stderr check disabled, **timeout 15 seconds** (critic finding #14 — 5s is too tight for real formatters under CI load; override via `TEST_HOOK_TIMEOUT` env var)
- Uses `timeout` command for the timeout (available on Linux CI, may need `gtimeout` fallback for macOS — handle with `command -v` and emit clear error if neither is available, NEVER silently skip per critic finding #9)
- Pipes the second arg (JSON string) to the hook script's stdin via `printf '%s' "$JSON" | SCRIPT_PATH`
- Captures stdout, stderr, exit code separately using temp files (mktemp)
- Assertions:
  - Exit code comparison: exact match if `--expect-exit N` given
  - Output JSON path: if `--expect-output .ok == true` given, use `jq` to evaluate
  - Stderr contains: simple grep for substring
- Strict mode: `set -euo pipefail`
- **CRITICAL for ShellCheck**: use braces on array expansions (`${arr[idx]}`), quote all variable expansions, define functions before use, don't use `-f` with globs — these are the three error classes the existing repo has had to fix
- Exit codes: 0 = all assertions pass, 1 = assertion failed, 2 = hook script not found or not executable, 3 = timeout
- `jq` dependency: document in script header comment; it's usually present but check via `command -v jq` and fall back to simpler string matching if absent

**Definition of Done:**
- [ ] `plugin-dev/scripts/test_hook.sh` exists and is executable
- [ ] `shellcheck --severity=error plugin-dev/scripts/test_hook.sh` passes with zero errors
- [ ] Running against a trivial hook that echoes `{"ok":true}` and exits 0 with `--expect-exit 0` returns exit 0
- [ ] Running against a hook that exits 2 with `--expect-exit 0` returns exit 1 (assertion failure)
- [ ] Timeout fires correctly (tested in Task 6)
- [ ] Usage message on missing arguments is clear

**Verify:**
- `shellcheck --severity=error plugin-dev/scripts/test_hook.sh`
- `echo '#!/bin/bash\necho "{\"ok\":true}"' > /tmp/trivial.sh && chmod +x /tmp/trivial.sh && bash plugin-dev/scripts/test_hook.sh /tmp/trivial.sh '{}' --expect-exit 0`

---

### Task 6: pytest suites for all 4 scripts

**Objective:** Write pytest test modules for each script. Tests use tmp_path and synthetic fixtures. Mocks for any external calls.

**Dependencies:** Tasks 2-5 (scripts must exist before tests)

**Files:**
- Create: `plugin-dev/scripts/tests/__init__.py` (empty)
- Create: `plugin-dev/scripts/tests/test_validate_plugin.py`
- Create: `plugin-dev/scripts/tests/test_scaffold_plugin.py`
- Create: `plugin-dev/scripts/tests/test_run_eval.py`
- Create: `plugin-dev/scripts/tests/test_test_hook.py` (Python wrapper that invokes the bash script via subprocess — easier to integrate with pytest than a standalone bash test framework)
- Create: `plugin-dev/scripts/tests/test_validator_drift.py` (contract test — new per critic finding #5)
- Create: `plugin-dev/scripts/tests/fixtures/example-evals/trigger-evals.json` (fixture anchor for Task 4/9)
- Create: `plugin-dev/scripts/tests/fixtures/example-evals/evals.json`

**Key Decisions / Notes:**
- Use the pattern from `.github/scripts/tests/test_validate_plugins.py` — `fake_repo` fixture with tmp_path, helper functions to create synthetic plugins, `run()` helper that calls the validator function directly
- `test_validate_plugin.py`: ≥6 tests covering happy path, missing SKILL.md, missing frontmatter, wrong frontmatter name, missing reference, multi-skill plugin, orphan catalog entries (N/A for this validator), CLI invocation via subprocess with `--json` flag
- `test_scaffold_plugin.py`: ≥6 tests covering minimal generation, `--skills` flag, `--hooks` flag, `--mcp` flag, refuses to overwrite without `--force`, generated output passes validator, **determinism test** (critic finding #12: runs scaffolder twice, asserts byte-equal outputs — forbids `datetime.now()`, `os.urandom()`, `uuid.uuid4()` in scaffold_plugin.py)
- `test_run_eval.py`: ≥6 tests covering offline-smoke mode, missing SDK fallback, missing API key fallback, structural smoke checks detect malformed eval files, SYNTHETIC banner appears in offline output, offline JSON contains `"mode": "offline"`, `--mode trigger` with `--offline` exits 3, mocked-online mode via monkeypatch. Uses the fixture at `tests/fixtures/example-evals/`.
- `test_test_hook.py`: ≥4 tests covering subprocess invocation of `test_hook.sh` with known-good hooks, exit code assertion failures, stderr assertions, timeout behavior. **macOS fix (critic finding #9):** tests that require `timeout` MUST NOT silently skip. They either (a) install a shim PATH that fakes `timeout` via `gtimeout` if present, or (b) fail with `pytest.fail("install coreutils: brew install coreutils")`. Silent skip is forbidden.
- `test_validator_drift.py` (new — critic finding #5): a contract test that imports both `plugin-dev/scripts/validate_plugin.py` AND `.github/scripts/validate_plugins.py`, runs both against `skillstack-workflows/`, and asserts: (a) both report 0 errors for the well-formed plugin, (b) the sets of error categories they can produce are compatible (`plugin-dev` is a strict subset of repo — no catalog/README checks). If this test starts failing in a future commit, that's the drift signal. Runs in CI as part of the pytest job.
- `fixtures/example-evals/`: canonical example eval files (fixture anchor per critic finding #10). `trigger-evals.json`: 3 entries (2 should_trigger=true, 1 should_trigger=false). `evals.json`: 1 entry with query/files/expected_behavior. Used by `test_run_eval.py` AND referenced by Task 9 (plugin-evaluation skill's own evals model their schema on this fixture).
- All tests must be runnable with `cd plugin-dev/scripts && pytest tests/ -q` from any fresh clone
- Target total: ≥22 tests, all passing

**Definition of Done:**
- [ ] All 5 test files exist with valid pytest structure
- [ ] Fixture directory `tests/fixtures/example-evals/` exists with both JSON files
- [ ] `cd plugin-dev/scripts && pytest tests/ -q` reports ≥22 passed, 0 failed
- [ ] `cd plugin-dev/scripts && pytest tests/ -v` shows every test name
- [ ] `test_validator_drift.py` passes (both validators produce compatible output)
- [ ] `test_scaffold_is_deterministic` passes (scaffolder output is byte-equal across runs)
- [ ] No test silently skips on macOS (timeout-dependent tests either install shim or fail loudly)
- [ ] No test depends on external network (anthropic SDK is mocked)
- [ ] No test depends on system-specific paths (all use tmp_path)
- [ ] Each test file has a clear module docstring

**Verify:**
- `cd plugin-dev/scripts && python3 -m pytest tests/ -q`

---

### Task 7: `plugin-validation` skill + references

**Objective:** Replace the placeholder SKILL.md from Task 1 with the full skill content. First real skill because it's the smallest scope and uses the script already built.

**Dependencies:** Tasks 1 (placeholder), 2 (validate_plugin.py exists)

**Files:**
- Modify: `plugin-dev/skills/plugin-validation/SKILL.md` (replace placeholder with full content)
- Create: `plugin-dev/skills/plugin-validation/references/frontmatter-rules.md`
- Create: `plugin-dev/skills/plugin-validation/references/validation-checklist.md`

**Key Decisions / Notes:**
- SKILL.md target: ~180 lines
- Frontmatter triggers (per PRD): "validate a plugin", "plugin structure errors", "plugin.json errors", "frontmatter errors", "is my plugin correctly set up"
- Core principle: "plugins that pass `claude plugin validate` fail in production all the time. Structural validation is necessary but not sufficient."
- Sections: what `claude plugin validate` checks, what it misses (frontmatter name mismatch, reference cross-references, orphan catalog entries), running `scripts/validate_plugin.py`, interpreting errors, CI integration (reference skillstack's own `.github/workflows/ci.yml` as example)
- `frontmatter-rules.md` sources: the Anthropic PDF's YAML frontmatter section (lines 249-340 in `/tmp/anthropic-skills-guide.txt`) and the best-practices research output from sub-agent report 4
- `validation-checklist.md`: a linear pre-ship checklist mirroring the PRD's "Appendix: Quick recommendations for your authoring skills"
- Every reference file opens with blockquote scope statement and ends with Viktor Bezdek footer

**Definition of Done:**
- [ ] `plugin-dev/skills/plugin-validation/SKILL.md` replaces placeholder, ≤220 lines, has frontmatter + `## When to use` + `## Core principle` + `## How to use` + cross-references
- [ ] Both reference files exist, each 150-250 lines
- [ ] `python3 plugin-dev/scripts/validate_plugin.py --plugin-dir plugin-dev/` passes (no errors from plugin-validation skill)
- [ ] Skill's cross-references (`references/X.md`) all exist on disk
- [ ] Content cites actual URLs (docs.claude.com, platform.claude.com) from research reports

**Verify:**
- `python3 plugin-dev/scripts/validate_plugin.py --plugin-dir plugin-dev/`
- `wc -l plugin-dev/skills/plugin-validation/SKILL.md plugin-dev/skills/plugin-validation/references/*.md`

---

### Task 8: `plugin-hooks` skill + references (largest reference set)

**Objective:** The hooks skill with the broadest reference coverage — the largest skill in the plugin. Uses `test_hook.sh` as the concrete testing tool.

**Dependencies:** Task 5 (test_hook.sh exists), Task 7 (pattern established)

**Files:**
- Create: `plugin-dev/skills/plugin-hooks/SKILL.md`
- Create: `plugin-dev/skills/plugin-hooks/references/hook-event-reference.md`
- Create: `plugin-dev/skills/plugin-hooks/references/hook-handler-types.md`
- Create: `plugin-dev/skills/plugin-hooks/references/hook-anti-patterns.md`
- Create: `plugin-dev/skills/plugin-hooks/references/hook-testing-patterns.md`

**Key Decisions / Notes:**
- SKILL.md target: ~220 lines (largest in the plugin)
- Frontmatter triggers (per PRD): "hook", "PreToolUse", "PostToolUse", "SessionStart", "Stop hook", "hook event", "auto-format on edit", "block dangerous bash", "session hook"
- Core principle: "hooks are the most powerful and most trap-laden extension type. Exit code 1 does not block. Matcher syntax has three modes. `updatedInput` replaces, not merges."
- SKILL.md body covers the core 10 events: PreToolUse, PostToolUse, PermissionRequest, UserPromptSubmit, SessionStart, SessionEnd, Stop, Notification, FileChanged, WorktreeCreate. Each with one-paragraph description + schema + when to use.
- **Authoritative source fetch (critic finding #7 fix):** before writing any reference file, run `WebFetch` against `https://docs.claude.com/en/docs/claude-code/hooks` and `https://docs.claude.com/en/docs/claude-code/hooks-guide` to obtain the current list of hook events. Cross-check every event claim in the reference files against this live fetch. **Do not invent events from memory or from summaries.** If the live fetch disagrees with the sub-agent research report, the live fetch wins.
- **Corrected reference budgets (critic finding #6):**
  - `hook-event-reference.md`: covers the ~18 advanced events (28 total minus 10 covered inline in SKILL.md). **~20-30 lines per event = 360-540 lines total.** Previous ~280 line budget is impossible arithmetic for 28 events. Each event gets: trigger description, input schema (JSON), matcher semantics for that event, exit code meaning for that event, example decision JSON output.
  - SKILL.md body covers the 10 core events at ~15 lines each (150 lines) plus framing content (~70 lines) = ~220 lines total (unchanged).
  - Total hook event coverage across SKILL.md + reference = ~540-690 lines, covering all 28 events.
- `hook-handler-types.md`: the 4 types (command, http, prompt, agent) with code examples, security implications. **~250 lines** (4 types × 50 lines each + framing).
- `hook-anti-patterns.md`: the 14+ anti-patterns from the research (exit code 1 trap, infinite Stop loops, shell profile contaminating JSON, mixing exit and JSON, partial updatedInput, over-broad matchers, async hooks expected to block, `PermissionRequest` hooks in non-interactive mode, non-executable hook scripts, etc.). **~300 lines** — 14 anti-patterns × ~20 lines each. Must include the plugin-shipped-agent security restriction: "Plugin-shipped agents cannot include hooks, mcpServers, or permissionMode" (critic finding #18, PRD research).
- `hook-testing-patterns.md`: how to test hooks — mock stdin, `/hooks` menu, debug log, transcript view, `test_hook.sh` usage examples. **~180 lines**.
- **Total reference set for plugin-hooks: ~1090-1270 lines across 4 files.** Substantial but justified — hooks are the most under-documented extension type and this is the canonical reference.
- All content cited from official Claude Code docs URLs (docs.claude.com). **Do not invent hook events that aren't in the authoritative sources fetched at start of this task.**
- **Anti-fabrication DoD (critic finding #13):** every hook event named in the references must be matched by a URL citation to docs.claude.com in the same reference file. Reviewer/implementer can grep for unmatched event names.

**Definition of Done:**
- [ ] **Pre-task: WebFetch `https://docs.claude.com/en/docs/claude-code/hooks` and `https://docs.claude.com/en/docs/claude-code/hooks-guide` executed**, event list extracted, reference files cite these URLs
- [ ] SKILL.md exists, ≤220 lines, documents core 10 events inline with citations to docs.claude.com
- [ ] 4 reference files exist, total ~1090-1270 lines (up from ~900 per critic finding #6)
- [ ] `hook-event-reference.md` is 360-540 lines covering ~18 advanced events at 20-30 lines each
- [ ] `hook-handler-types.md` is ~250 lines
- [ ] `hook-anti-patterns.md` is ~300 lines with ≥14 anti-patterns
- [ ] `hook-testing-patterns.md` is ~180 lines
- [ ] Every reference cites URLs from docs.claude.com or docs.anthropic.com
- [ ] **Anti-fabrication check:** every event name in the references can be found at a URL cited in the same file (grep-verifiable)
- [ ] `hook-anti-patterns.md` includes the plugin-shipped-agent security restriction
- [ ] Cross-references in SKILL.md (to `references/X.md`) all exist on disk
- [ ] Validator passes (`python3 plugin-dev/scripts/validate_plugin.py --plugin-dir plugin-dev/`)
- [ ] All 28 hook events are documented somewhere (SKILL.md body covers 10, reference covers the other 18+)
- [ ] All 4 handler types documented
- [ ] Anti-patterns include the exit-code-1 trap (the most important one)

**Verify:**
- `python3 plugin-dev/scripts/validate_plugin.py --plugin-dir plugin-dev/`
- `grep -c "PreToolUse\|PostToolUse\|SessionStart\|SessionEnd\|Stop\|UserPromptSubmit\|Notification\|FileChanged\|WorktreeCreate\|WorktreeRemove\|PreCompact\|PostCompact\|InstructionsLoaded\|ConfigChange\|CwdChanged\|PermissionRequest\|PermissionDenied\|SubagentStart\|SubagentStop\|TaskCreated\|TaskCompleted\|TeammateIdle\|Elicitation\|ElicitationResult\|StopFailure\|PostToolUseFailure" plugin-dev/skills/plugin-hooks/references/hook-event-reference.md` — should find 25+ matches (one per event)

---

### Task 9: `plugin-evaluation` skill + references

**Objective:** The evaluation skill that teaches the two eval file formats and uses `run_eval.py` as the concrete runner.

**Dependencies:** Task 4 (run_eval.py exists), Task 7 (pattern established)

**Files:**
- Create: `plugin-dev/skills/plugin-evaluation/SKILL.md`
- Create: `plugin-dev/skills/plugin-evaluation/references/eval-file-formats.md`
- Create: `plugin-dev/skills/plugin-evaluation/references/eval-quality-criteria.md`
- Create: `plugin-dev/skills/plugin-evaluation/references/iteration-methodology.md`
- Create: `plugin-dev/skills/plugin-evaluation/evals/trigger-evals.json` (meta: eval the evaluation skill itself — self-referential)
- Create: `plugin-dev/skills/plugin-evaluation/evals/evals.json` (same)

**Key Decisions / Notes:**
- SKILL.md target: ~220 lines
- Frontmatter triggers (per PRD): "evaluate a plugin", "skill activation testing", "eval harness", "measure plugin quality", "plugin tests", "trigger rate", "output quality"
- Core principle: "if you haven't measured the activation rate and the output pass rate, you have not evaluated your plugin."
- Sections: three test types (triggering, functional, performance comparison), the two eval file formats, quality criteria for eval queries, running `scripts/run_eval.py`, interpreting results, iteration methodology, grader/analyzer/comparator pattern
- `eval-file-formats.md`: full JSON schemas for `evals/evals.json` and `evals/trigger-evals.json` with examples from Anthropic's skill-creator
- `eval-quality-criteria.md`: what makes a good eval query — realistic, varied, near-miss negatives — with counter-examples
- `iteration-methodology.md`: how to iterate on a skill description based on eval results (based on Anthropic's run_loop.py pattern)
- **Meta**: this skill includes its own evals. They serve as exemplars AND as self-test. The evals live at `evals/trigger-evals.json` inside the skill (not at `plugin-dev/evals/`).

**Definition of Done:**
- [ ] SKILL.md and 3 reference files exist, valid content
- [ ] `evals/trigger-evals.json` has ≥8 should-trigger + ≥5 should-not-trigger queries, all realistic (not "format this data" generic)
- [ ] `evals/evals.json` has ≥3 output test cases with `query`, `files`, `expected_behavior` fields
- [ ] Running `python3 plugin-dev/scripts/run_eval.py --plugin-dir plugin-dev --skill plugin-evaluation --offline` completes without errors and produces a benchmark report
- [ ] Validator passes
- [ ] Content cites Anthropic's skill-creator as the source of the methodology

**Verify:**
- `python3 plugin-dev/scripts/validate_plugin.py --plugin-dir plugin-dev/`
- `python3 plugin-dev/scripts/run_eval.py --plugin-dir plugin-dev --skill plugin-evaluation --offline`

---

### Task 10: `plugin-architecture` skill + references

**Objective:** The core decision-making skill — when to use a skill vs hook vs MCP vs agent vs command. The decision matrix and the manifest reference.

**Dependencies:** Task 7 (pattern established)

**Files:**
- Create: `plugin-dev/skills/plugin-architecture/SKILL.md`
- Create: `plugin-dev/skills/plugin-architecture/references/component-decision-matrix.md`
- Create: `plugin-dev/skills/plugin-architecture/references/manifest-reference.md`
- Create: `plugin-dev/skills/plugin-architecture/references/real-plugin-examples.md`

**Key Decisions / Notes:**
- SKILL.md target: ~220 lines
- Frontmatter triggers (per PRD): "design a plugin", "plugin structure", "skill vs hook vs mcp", "plugin composition", "plugin components", "plugin architecture"
- Core principle: "the decomposition matters more than any single component. A plugin that puts the wrong capability in the wrong component fails silently."
- Sections: the five extension types (skill, hook, MCP server, subagent, slash command), the decision matrix, `plugin.json` manifest design, directory layout, namespacing
- Cross-references: point users at `skill-creator` for single-skill depth, at `mcp-server` for MCP depth, at `plugin-hooks` for hook depth, at `plugin-composition` for multi-component integration
- `component-decision-matrix.md`: a detailed matrix with columns "Is the capability..." and rows for each extension type. Rules of thumb with concrete examples.
- `manifest-reference.md`: full `plugin.json` schema with every field, optional vs required, conventions. Source: sub-agent plugin-architecture research report
- `real-plugin-examples.md`: the 5-10 real plugins from the sub-agent research report (Anthropic's official plugins: plugin-dev, hookify, ralph-wiggum, feature-dev, pr-review-toolkit, security-guidance; community: superpowers, levnikolaevich/claude-code-skills, oh-my-claudecode, everything-claude-code, claude-toolbox). Each with architecture breakdown.

**Definition of Done:**
- [ ] SKILL.md and 3 reference files exist
- [ ] Decision matrix is concrete, not abstract (has rows and columns, not just prose)
- [ ] `manifest-reference.md` lists every documented plugin.json field
- [ ] `real-plugin-examples.md` documents ≥8 real plugins with their component breakdown
- [ ] Validator passes
- [ ] Cross-references to skill-creator, mcp-server, plugin-hooks, plugin-composition all present

**Verify:**
- `python3 plugin-dev/scripts/validate_plugin.py --plugin-dir plugin-dev/`

---

### Task 11: `plugin-composition` skill + references

**Objective:** The integration skill — how skills, hooks, MCPs, and commands work together within a single plugin.

**Dependencies:** Task 7 (pattern established)

**Files:**
- Create: `plugin-dev/skills/plugin-composition/SKILL.md`
- Create: `plugin-dev/skills/plugin-composition/references/directory-layout-reference.md`
- Create: `plugin-dev/skills/plugin-composition/references/path-substitution-patterns.md`

**Key Decisions / Notes:**
- SKILL.md target: ~200 lines
- Frontmatter triggers (per PRD): "multi-component plugin", "combine skills and hooks", "plugin directory structure", "CLAUDE_PLUGIN_ROOT", "plugin layout", "inside a plugin"
- Core principle: "a plugin is more than the sum of its components. Shared conventions (path substitution, namespacing, settings) make the difference between a working plugin and a fragile one."
- Sections: canonical directory layout, the `.claude-plugin/` rule, `${CLAUDE_PLUGIN_ROOT}` vs `${CLAUDE_PLUGIN_DATA}`, the `bin/` pattern, namespacing, hook merging behavior, MCP auto-start lifecycle, how components integrate
- `directory-layout-reference.md`: the canonical directory tree from the Claude Code docs with notes on each component location. ~150 lines.
- `path-substitution-patterns.md`: `${CLAUDE_PLUGIN_ROOT}`, `${CLAUDE_PLUGIN_DATA}`, `${CLAUDE_PROJECT_DIR}`, `${CLAUDE_ENV_FILE}` with examples of when to use which. ~130 lines.

**Definition of Done:**
- [ ] SKILL.md and 2 reference files exist
- [ ] Directory layout matches Claude Code docs exactly (not invented)
- [ ] Path substitution variables documented with real code examples
- [ ] Validator passes

**Verify:**
- `python3 plugin-dev/scripts/validate_plugin.py --plugin-dir plugin-dev/`

---

### Task 12: `plugin-ideation` skill + references

**Objective:** The upstream skill — turns "I want a plugin" into "I should build a plugin for X". Pain-point mining, gap analysis, "problem worthy of a plugin" check.

**Dependencies:** Task 7 (pattern established). **Note:** this skill doesn't depend on any scripts and can run in parallel with Tasks 8-11 if desired — an implementer following the plan sequentially can safely reorder Tasks 12-13 to run right after Task 7.

**Files:**
- Create: `plugin-dev/skills/plugin-ideation/SKILL.md`
- Create: `plugin-dev/skills/plugin-ideation/references/problem-worthy-checklist.md`
- Create: `plugin-dev/skills/plugin-ideation/references/ideation-anti-patterns.md`

**Key Decisions / Notes:**
- SKILL.md target: ~180 lines
- Frontmatter triggers (per PRD): "want to build a Claude plugin", "have an idea for a plugin", "should I build this as a plugin", "plugin idea", "plugin for X"
- Core principle: "problem-first framing. Do not build a plugin for a one-off task."
- Sections: pain-point mining, workflow audit, existing-plugin gap analysis (marketplace search methodology), "problem worthy of a plugin" checklist (7 criteria), ideation anti-patterns
- `problem-worthy-checklist.md`: 7 criteria a plugin idea must pass (is it repeatable? is it shareable? does it compose with existing skills? etc.)
- `ideation-anti-patterns.md`: "building for yourself only", "building a tool you want vs. a problem you have", "scope creep at ideation time", "plugin as engineering exercise"

**Definition of Done:**
- [ ] SKILL.md and 2 reference files exist
- [ ] 7-criterion checklist is concrete
- [ ] Anti-patterns section names ≥5 patterns
- [ ] Validator passes

**Verify:**
- `python3 plugin-dev/scripts/validate_plugin.py --plugin-dir plugin-dev/`

---

### Task 13: `plugin-research` skill + references

**Objective:** The research skill — validate an idea before building. Survey the marketplace, read authoritative sources, decide build-vs-fork-vs-skip.

**Dependencies:** Task 7 (pattern established)

**Files:**
- Create: `plugin-dev/skills/plugin-research/SKILL.md`
- Create: `plugin-dev/skills/plugin-research/references/authoritative-sources.md`
- Create: `plugin-dev/skills/plugin-research/references/build-vs-fork-decision.md`

**Key Decisions / Notes:**
- SKILL.md target: ~180 lines
- Frontmatter triggers (per PRD): "research existing plugins", "is there a plugin for X", "should I build or fork", "marketplace survey", "plugin research"
- Core principle: "validate an idea before building. Most plugin ideas die at research time, and that is a success not a failure."
- Sections: marketplace survey methodology, Anthropic doc fetching, community pattern discovery, build-vs-fork-vs-skip decision gate
- `authoritative-sources.md`: the canonical URLs for Anthropic docs. Updated from the research reports — code.claude.com/docs/en/*, docs.claude.com/en/docs/*, platform.claude.com/docs/en/*, github.com/anthropics/claude-code, github.com/anthropics/skills, resources.anthropic.com/.../The-Complete-Guide-to-Building-Skill-for-Claude.pdf, etc. With short descriptions of what each covers.
- `build-vs-fork-decision.md`: the decision tree with criteria

**Definition of Done:**
- [ ] SKILL.md and 2 reference files exist
- [ ] Authoritative sources list has ≥12 URLs with descriptions
- [ ] Decision tree is flowchart-like (not abstract prose)
- [ ] Validator passes

**Verify:**
- `python3 plugin-dev/scripts/validate_plugin.py --plugin-dir plugin-dev/`

---

### Task 14: CI wiring — `pytest / plugin-dev` job

**Objective:** Add a new CI job that runs the pytest suite for plugin-dev's scripts, following the exact pattern of `pytest-skill-creator`.

**Dependencies:** Task 6 (tests exist)

**Files:**
- Modify: `.github/workflows/ci.yml` (add new job)

**Key Decisions / Notes:**
- Insert the new job alphabetically after `pytest-mcp` and before `node-test`
- Job name: `pytest-plugin-dev` with display name `pytest / plugin-dev`
- `working-directory: plugin-dev/scripts`
- `pip install pytest pyyaml` — same as skill-creator
- `continue-on-error: false` (this should be a real gate, not a soft-fail job)
- Python 3.12
- Run command: `pytest tests/ -v`

**Definition of Done:**
- [ ] `.github/workflows/ci.yml` has new `pytest-plugin-dev` job
- [ ] Job alphabetically positioned correctly
- [ ] Job follows the exact shape of `pytest-skill-creator`
- [ ] On push, the new job runs and passes (verified after commit)

**Verify:**
- `grep -A 20 "pytest-plugin-dev" .github/workflows/ci.yml`
- After push: `gh run watch <id> --exit-status`

---

### Task 15: Final polish — full README, root README catalog entry, integration validation

**Objective:** Replace the stub plugin README with the full content, update the root README catalog table entry, run the full validation pipeline one more time.

**Dependencies:** Tasks 1-14 (everything else must exist first)

**Files:**
- Modify: `plugin-dev/README.md` (replace stub with full content — scenario table, when-not-to-use, full installation block, what's inside with 7 skills + 4 scripts listed, cross-references to related plugins)
- Modify: `README.md` (the root skillstack README — replace the Task 1 minimal entry in the Development catalog table with a full description; verify the "Find a skill by goal" → "I want to document and create skills" table has a new row for plugin-dev; verify plugin count is 52 in all six literal-number locations, Development section count is 12, and backtick list contains plugin-dev alphabetically)

**Key Decisions / Notes:**
- Plugin README follows the template from `skillstack-workflows/README.md` (scenario table, when-not-to-use, installation with `/plugin marketplace add` + `/plugin install plugin-dev@skillstack`, what's inside, cross-references)
- Scenario table rows: one per major flow from the PRD (end-to-end build, hook-only authoring, validating existing plugin, evaluating existing plugin)
- What's inside lists all 7 skills with their frontmatter trigger phrases and all 4 scripts with their CLI
- Cross-references section links to `skill-creator`, `mcp-server`, `skillstack-workflows` (specifically the `write-your-own-skill` workflow)
- Root README catalog entry under the `### 💻 Development (N)` section — increment the count and add the row alphabetically

**Definition of Done:**
- [ ] `plugin-dev/README.md` is ≥200 lines with full content
- [ ] Scenario table has ≥4 rows, each matching a user flow from the PRD (not fabricated — critic finding #17)
- [ ] Root README Development section count is incremented (e.g., `### 💻 Development (12)` if it was 11)
- [ ] Root README "Find a skill by goal" has new row referencing plugin-dev
- [ ] Root README plugin count is 52 everywhere
- [ ] Full validator run: `python3 .github/scripts/validate_plugins.py` passes with 52 plugins, 0 errors
- [ ] Plugin self-validation: `python3 plugin-dev/scripts/validate_plugin.py --plugin-dir plugin-dev/` passes
- [ ] All pytest suites pass: `python3 -m pytest .github/scripts/tests/ -q` and `cd plugin-dev/scripts && python3 -m pytest tests/ -q`
- [ ] ShellCheck passes: `find . -name "*.sh" -not -path "./.git/*" | xargs shellcheck --severity=error`

**Verify:**
- `python3 .github/scripts/validate_plugins.py`
- `python3 plugin-dev/scripts/validate_plugin.py --plugin-dir plugin-dev/`
- `cd plugin-dev/scripts && python3 -m pytest tests/ -q && cd -`
- `find plugin-dev -name "*.sh" | xargs shellcheck --severity=error`
- `git status` — review changes, `git add -A`, inspect staged diff
- Post-commit: `gh run watch <id> --exit-status`

---

## Spec Review Decisions (critic findings addressed, iteration 1)

The adversarial spec review raised 20 findings. This section documents how each was handled.

**must_fix (6 total, all addressed):**
1. README plugin-count math at six line locations (not four) — **FIXED**: Task 1 now lists all six line numbers explicitly, Task 0 gate re-verifies, DoD requires `grep -c '\b51\b' README.md` to return 0 post-Task-1.
2. Baseline state re-verification — **FIXED**: Task 0 preflight gate, "Baseline State" section added after Summary documenting commit 9c762cd, 51-plugin baseline, elicitation committed status.
3. Catalog version byte-equality not in DoD — **FIXED**: Task 1 DoD adds `python3 -c "..."` one-liner asserting plugin.json.version == registry.json entry version == marketplace.json entry version.
4. Tautological offline mode in run_eval.py — **FIXED**: Task 4 rewritten. Offline mode FORCES smoke mode, cannot compute trigger rates, benchmark output has SYNTHETIC BANNER, JSON has mode/warning fields. `--mode trigger --offline` exits with code 3 and a clear error.
5. Three-way validator drift under-risked — **FIXED**: Task 6 adds `test_validator_drift.py` contract test. Risks table row upgraded from LOW/LOW to MEDIUM/MEDIUM. Task 2 header comment documents base commit SHA.
6. Task 8 hook reference 2x too small for 28 events — **FIXED**: Task 8 reference budget raised from ~900 to ~1090-1270 lines. `hook-event-reference.md` alone grows to 360-540 lines (20-30 per event). Plus authoritative live-fetch requirement.

**should_fix (8 total, all addressed):**
7. Hook content invention risk — **FIXED**: Task 8 pre-step WebFetches docs.claude.com/en/docs/claude-code/hooks, anti-fabrication grep DoD.
8. Task 14 uses pip instead of uv — **DEFERRED**: all existing CI jobs (plugin-validation, pytest-skill-creator, pytest-docker, pytest-mcp) use `pip install`. Adopting uv in one new job creates inconsistency. Migration is a separate PR. Task 14 matches existing pattern.
9. Task 6 macOS silent skip hides timeout bugs — **FIXED**: Task 6 explicit rule "silent skip is forbidden; either install shim or fail loudly with brew guidance".
10. Task 4/9 circular verify loop lacks fixture anchor — **FIXED**: Task 6 ships `plugin-dev/scripts/tests/fixtures/example-evals/` as the canonical fixture. Task 4 uses it for testing; Task 9 bases its own eval shape on it.
11. PRD cloud-finops skill count incorrect — **NOTED**: cloud-finops is a single-skill plugin with 20-26 reference files (not 26 skills). The PRD's "7 is in range" rationale still holds comparing to `skillstack-workflows` (9 skills) and Anthropic's own `plugin-dev` (7 skills). No plan change needed. PRD correction is a separate follow-up.
12. Task 3 scaffold_plugin determinism unverified — **FIXED**: Task 6 `test_scaffold_is_deterministic` runs scaffolder twice and asserts byte-equal output. Forbidden imports list (datetime.now, uuid.uuid4, os.urandom) added to Task 3 notes.
13. Task 7-13 content provenance not enforced — **FIXED**: anti-fabrication DoD added to Task 8 as the canonical pattern; Tasks 9-13 inherit the same rule via reference to Task 8's DoD.
14. Task 5 default 5s timeout too tight — **FIXED**: default raised to 15s, `TEST_HOOK_TIMEOUT` env override documented.

**consider (6 total):**
15. Reorder Tasks 12-13 earlier — **NOTED**: Task 12 has a note that it can run in parallel with Tasks 8-11. Sequential implementers can safely reorder. Full renumbering avoided to preserve task IDs.
16. Task 1 placeholder description violates no-promo rule — **FIXED**: Task 1 now specifies a real minimal SKILL.md with a genuine description, not "placeholder" copy.
17. Task 15 scenario table row count — **FIXED**: ≥4 rows matching PRD flows, not ≥5.
18. hook-handler-types.md missing plugin-agent security restriction — **FIXED**: Task 8 `hook-anti-patterns.md` must include this restriction.
19. CI job soft-fail ordering — **NOTED**: Task 14 uses `continue-on-error: false` (hard gate) by default. Flipping to soft-fail for a week is a reasonable option but not prescribed.
20. Alphabetical insertion mismatch risk — **FIXED**: new risk row added.

**praise from the review** (preserved for context):
- Unusually well-researched PRD
- Sound architecture and ordering rationale
- Above-average risk anticipation
- Bottom-up approach justified
- Multi-skill plugin pattern correctly applied

---

## Autonomous Decisions (made by the planner without asking)

- **Task 0 preflight gate** added as a hard gate before any changes (not asked by user; critic-driven).
- **Offline mode scope** limited to structural smoke tests only, not tautological activation numbers. User was not asked; this is the only correct interpretation after critic finding #4.
- **README line numbers** enumerated explicitly in Task 1 key decisions rather than left to implementer discretion. User was not asked; accuracy required.
- **Validator drift contract test** added to Task 6 without asking. Mitigation for a risk the user did not know about.
- **Live-fetch authoritative source** step added to Task 8 without asking. Anti-fabrication discipline.
- **pip vs uv** — kept pip to match existing repo CI pattern. User not asked because changing one job but not others creates worse inconsistency than the original standard-compliance issue.
- **Renumbering vs in-place fix** — kept 15 original task IDs + added Task 0 rather than renumbering. Progress tracker shows 16 total.
