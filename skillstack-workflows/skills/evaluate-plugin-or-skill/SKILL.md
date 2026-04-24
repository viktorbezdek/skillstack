---
name: evaluate-plugin-or-skill
description: Use when evaluating a Claude Code plugin or single SKILL.md and a verdict is needed — ship-ready, needs improvement, or rework. Multi-pass audit workflow that composes plugin-dev's structural validation, plugin-evaluation's activation and output measurement, and skill-foundry's anti-pattern audit to grade quality across five dimensions: structure, activation reliability, content discipline, output behavior, and documentation completeness. Trigger phrases include "evaluate this plugin", "review this skill", "audit this SKILL.md", "is this ready to publish", "check the quality of this plugin", "should this skill be shared", "give feedback on this plugin", "score this plugin before shipping". Use also when reviewing a third-party plugin before installation or recommendation. NOT for building a new plugin from scratch (use build-a-plugin). NOT for fixing a known bug or extending an existing plugin (use update-a-plugin). NOT for measuring runtime agent quality in production (use evaluate-and-improve-agent).
---

# Evaluate Plugin or Skill

> **A plugin is ready to share when its structure is correct, its activation is reliable, its content is disciplined, its documentation answers the three install-time questions, and its anti-patterns are absent.** This workflow checks all five dimensions against the same standards skill-foundry and plugin-dev enforce — and returns a single verdict instead of a wall of unsorted feedback.

## When to use this workflow

- You finished a plugin or skill and want to know if it is shippable
- You are reviewing a third-party plugin before installing or recommending it
- You drafted a SKILL.md and want to know whether the description will actually trigger
- You want a structured second opinion before publishing to a marketplace
- You need feedback that is ranked by priority — not a flat list of nitpicks

## When NOT to use this workflow

- **Building a new plugin from scratch** → use `build-a-plugin`
- **Extending or fixing an existing plugin** → use `update-a-plugin`
- **Authoring a single new SKILL.md** → use `write-your-own-skill`
- **Measuring runtime agent quality (eval suites for production agents)** → use `evaluate-and-improve-agent`
- **Fixing a single broken validation check** → run `plugin-validation` directly

## Prerequisites

Install the underlying plugins so the audit has real depth:

```
/plugin install plugin-validation@skillstack
/plugin install plugin-evaluation@skillstack
/plugin install skill-foundry@skillstack
/plugin install plugin-documenter@skillstack
```

Without these installed, the workflow still runs as a checklist — but the depth and the live eval harness disappear.

## Core principle

**A verdict beats a list.** Ten unranked findings overwhelm; one verdict with three ranked actions ships. The audit sorts every finding by severity (blocker, gap, polish) and folds them into one of three outcomes: SHIP, IMPROVE, or REWORK. Authors get a clear next step instead of a homework pile.

Secondary principle: **measure activation, do not assume it.** Most plugins fail in the wild because their description does not trigger reliably — not because their content is bad. Trigger evals are non-negotiable; if none exist, this workflow generates seed evals and runs them before issuing a verdict.

Third principle: **eat the dog food.** This skill audits other skills against skill-foundry's anti-patterns. It must itself avoid those anti-patterns — lean SKILL.md, references on demand, decision tables over prose.

## The phases

### Phase 1 — Intake and classification

Detect what the user provided. Inputs come in three forms: a GitHub URL, a local plugin directory, or a single SKILL.md path.

Classify the artifact:

- **Plugin** — has `.claude-plugin/plugin.json` and a `skills/` (or `hooks/`, `mcp-servers/`, `agents/`, `commands/`) directory
- **Single skill** — has a single `SKILL.md` with frontmatter, no plugin manifest
- **Ambiguous** — neither — ask the user before proceeding

Inventory components without deep-reading: count skills, hooks, MCP servers, subagents, commands. Note size of each SKILL.md in lines. This inventory drives which phases are relevant.

Output: a one-paragraph summary of what is being evaluated and which phases will run.

### Phase 2 — Structural validation (plugin-validation)

Load the `plugin-validation` skill.

Check, for plugins:

- `plugin.json` has `name`, `version`, `description`, `author`, `license`
- Each `skills/<name>/SKILL.md` exists and has YAML frontmatter
- `name` in frontmatter equals the directory name
- All referenced files (`references/*.md`, `scripts/*.py`, etc.) exist on disk
- Plugin name and version follow conventions of the target marketplace
- No SKILL.md exceeds 500 lines (skill-foundry hard limit)

For single skills, run a subset: frontmatter validity, name field present, referenced files exist.

If `plugin-dev/scripts/validate_plugins.py` is available, run it for objective output. Otherwise, run the checklist by hand.

Severity classification:

- **Blocker** — manifest missing, name mismatch, frontmatter invalid, broken reference
- **Gap** — missing optional but expected fields (keywords, repository URL)
- **Polish** — convention drift (kebab-case violations, unusual naming)

Output: structural score (blocker count, gap count, polish count).

### Phase 3 — Skill content audit (skill-foundry)

Load the `skill-foundry` skill.

For each SKILL.md, audit against the five canonical anti-patterns:

| Anti-pattern | Symptom | Fix |
|---|---|---|
| Reference Illusion | SKILL.md cites references that do not exist or are never loaded | Inline the content or remove the citation |
| Description Soup | Frontmatter description is generic prose without trigger keywords or NOT clauses | Rewrite with concrete trigger phrases + explicit NOT clause |
| Template Theater | Sections present because the template said so, not because the skill needs them | Delete unused sections |
| Everything Skill | Tries to handle multiple unrelated capabilities | Split into multiple skills, one per capability |
| Orphaned Sections | Sections never referenced from anywhere — readers cannot find them | Either link to them or delete them |

Also check the structural quality bar:

- Description has trigger phrases AND a NOT clause (target: ≥3 trigger keywords, ≥2 NOT cases)
- SKILL.md ≤500 lines (≤200 preferred for activation skills)
- Decision tables, not paragraphs, for routing logic
- Progressive disclosure: heavy content lives in `references/`, not inline

Severity classification:

- **Blocker** — Everything Skill, Reference Illusion, description with no trigger keywords
- **Gap** — Description Soup, no NOT clause, missing decision tables
- **Polish** — Template Theater, mild Orphaned Sections

Output: per-skill anti-pattern findings with severity.

### Phase 4 — Activation evaluation (plugin-evaluation)

Load the `plugin-evaluation` skill.

If `skills/<skill>/evals/trigger-evals.json` exists, run the harness:

```bash
python3 plugin-dev/scripts/run_eval.py \
  --plugin-dir <path> --skill <name> --mode trigger
```

If no trigger evals exist, this is itself a finding — but do not stop. Generate seed evals: 5 positive cases (varied phrasings of when the skill should activate) and 5 near-miss negatives (queries that look related but should NOT trigger). Run those.

Targets:

- Positive trigger rate ≥ 90%
- Negative no-trigger rate ≥ 95%

Severity classification:

- **Blocker** — positive trigger rate < 60%, or negative no-trigger rate < 80% (skill collides with other skills)
- **Gap** — positive 60–89%, or negative 80–94%
- **Polish** — positive 90–94%, or negative 95–98%
- **No finding** — positive ≥ 95% AND negative ≥ 99%

Output: trigger-rate table per skill.

### Phase 5 — Output evaluation (plugin-evaluation, optional)

If `skills/<skill>/evals/evals.json` exists, run output evals to check whether the skill produces correct results when activated. Otherwise, mark as a gap and proceed — output evals are nice-to-have for shipping, mandatory for production-critical plugins.

Severity classification:

- **Blocker** — output pass rate < 70% on existing evals
- **Gap** — no output evals exist for a plugin marketed as production-ready
- **Polish** — output pass rate 70–89%

Output: output-eval pass rate (or absence note).

### Phase 6 — Documentation and shareability

The best plugin documentation answers three questions in install order: **what problem does this solve, how do I install it, what can I do with it.** Check whether the README answers these in that order.

Checklist:

- README opens with a problem statement, not "this plugin provides…"
- Installation block exists and works as written
- At least three concrete example prompts, scenarios, or invocations
- License and attribution footer present
- CHANGELOG.md exists with at least one version entry
- Plugin manifest keywords are searchable (matches actual use cases, not generic words like "tools" or "ai")

Severity classification:

- **Blocker** — no README, broken install instructions, no license
- **Gap** — README leads with capabilities instead of the problem; no example prompts; no CHANGELOG
- **Polish** — keyword stuffing, missing screenshots for visual plugins

Output: documentation gap list.

### Phase 7 — Verdict synthesis

Score each dimension 0–3:

| Score | Meaning |
|---|---|
| 3 | Zero blockers, zero gaps |
| 2 | Zero blockers, ≤2 gaps |
| 1 | Zero blockers, 3+ gaps OR 1 blocker |
| 0 | 2+ blockers OR critical activation failure |

Aggregate the five scores (structure, content, activation, output, documentation) into one verdict:

- **SHIP** — every dimension ≥ 2 AND total ≥ 12. Worth sharing as-is or with cosmetic polish.
- **IMPROVE** — one or two dimensions at 1, none at 0. Concrete, addressable fixes. List the top three ranked actions; the author can ship after addressing them.
- **REWORK** — any dimension at 0, OR three+ dimensions at 1, OR positive trigger rate < 60%. The plugin needs a structural revisit; suggest restarting from `build-a-plugin` (for plugins) or `write-your-own-skill` (for single skills).

Output: a one-screen verdict report with:

1. Verdict (SHIP / IMPROVE / REWORK) — single word, top of the report
2. Dimension scores table (5 rows, score + one-sentence reason each)
3. Top three ranked actions (only the ones that move the verdict — skip polish-only items unless the verdict is already SHIP)
4. If REWORK: which workflow to restart from and why

## Gates and failure modes

| Gate | Failure mode | Recovery |
|---|---|---|
| Phase 1 classification ambiguous | Cannot tell what is being audited | Ask the user before running phases 2–7 |
| Phase 2 blocker found | Plugin will not load | Stop — return a REWORK verdict with structural fixes only |
| Phase 4 trigger evals missing AND skill description is the only signal | Cannot measure activation | Generate seed evals before issuing verdict; do not skip Phase 4 |
| Phase 7 produces SHIP without trigger eval data | Verdict is unfounded | Downgrade to IMPROVE pending eval evidence |
| Author asks "just tell me if it is good" | Tempting to skip phases | Run all phases — verdict is only credible if every dimension was checked |

The most common failure mode is **issuing SHIP without measuring activation.** If you cannot point to a trigger pass rate, you have not evaluated the plugin — you have read it.

## Output artifacts

- A verdict report (SHIP / IMPROVE / REWORK) with dimension scores and ranked actions
- Optional: generated `trigger-evals.json` seed file if none existed
- Optional: a one-page diff between the plugin's current state and shippable state, suitable for handing back to the author

## Related workflows and skills

- `build-a-plugin` — when REWORK is the verdict for a plugin, restart here
- `write-your-own-skill` — when REWORK is the verdict for a single skill
- `update-a-plugin` — when IMPROVE is the verdict and the author wants a guided fix loop
- `plugin-validation`, `plugin-evaluation`, `skill-foundry`, `plugin-documenter` — the underlying skills this workflow composes

---

> *Workflow part of [skillstack-workflows](../../README.md) by [Viktor Bezdek](https://github.com/viktorbezdek) — licensed under MIT.*
