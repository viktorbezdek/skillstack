# Phase 4: Reinforcement Mechanisms

**Date:** 2026-06-05  **Status:** PENDING APPROVAL  **Source:** plugin manifest inspection, hooks.json, commands/, scripts/, skillstack-workflows

## Scope

Maps every mechanism that currently reinforces (or fails to reinforce) taxonomy navigation. "Mechanism" = anything that routes a user to the right plugin or makes domain relationships explicit.

---

## Mechanism Inventory

### M1: Skill trigger descriptions (ACTIVE — primary routing)

**How it works:** Each SKILL.md frontmatter `description` field is the activation signal. Claude Code's skill-routing reads this description to decide whether to invoke a skill. This is the **sole primary routing mechanism** — all other mechanisms are secondary.

**Coverage:** 102 skills across 59 plugins. All 102 have the `NOT for` clause (verified Phase 1). Quality varies: some descriptions are vague generic phrases ("can you help me with outcome orientation?"); the best ones are domain-specific trigger phrase catalogs.

**Taxonomy reinforcement:** Weak. Descriptions don't reference domains (E/I/P/M). A user asking "help me think about my product" could trigger `product-thinking`, `creative-problem-solving`, `brainstorm-swarm`, or `prioritization` — no mechanism prioritizes or organizes these.

**Gap:** No domain signal in the trigger descriptions. Cross-domain disambiguation is left entirely to the natural language match.

---

### M2: `category` field in plugin.json (INACTIVE — source empty)

**How it works:** `build-registry.py` reads each `plugin.json`'s `category` field, groups plugins into named collections, and writes them to `registry.json`. Marketplace clients use collections for browsing.

**Coverage:** `category` is **empty on all 59 plugins**. The `collections` array in `registry.json` currently contains 9 collections generated from an empty category field — effectively inoperative.

**Taxonomy reinforcement:** Zero — the field exists but carries no data.

**Gap:** This is the primary structural gap Phase 5 fixes. Setting `category` to one of `{Engineering, Meta-Infra, Managerial-Product, Marketing-Comms}` on all 59 plugins activates the collection grouping.

---

### M3: skillstack-workflows (ACTIVE — cross-domain compositors)

**How it works:** 20 skills in `skillstack-workflows` each compose 3–8 skills from other plugins into an end-to-end workflow. They are the de-facto multi-plugin navigation layer.

**Coverage by domain:**

| Domain | Workflows that serve it |
|--------|------------------------|
| E | `api-to-production`, `legacy-rescue`, `debug-complex-issue`, `security-hardening-audit`, `onboard-to-codebase` |
| I | `context-engineering-pipeline`, `build-a-plugin`, `evaluate-plugin-or-skill`, `evaluate-and-improve-agent`, `llm-cost-optimization`, `write-your-own-skill`, `update-a-plugin`, `build-ai-agent` |
| P | `product-story-to-ship`, `strategic-decision`, `user-research-to-insight`, `pitch-sprint`, `storytelling-for-stakeholders`, `design-review-sprint` |
| M | **None** |

**Taxonomy reinforcement:** Strong for E/I/P, zero for M. The 5 M-domain plugins (communication, deslop, technical-copywriting, ux-writing, storytelling) have no workflow that composes them.

**Gap:** M domain lacks a workflow entry point. A "content-production" or "editorial-pipeline" workflow composing deslop → technical-copywriting → communication would close this.

---

### M4: Hooks — hindsight SessionStart/UserPromptSubmit/Stop (ACTIVE — memory persistence)

**How it works:** `hindsight` registers 3 hooks:
- `SessionStart` → `session_start.py` — recalls prior session context
- `UserPromptSubmit` → `recall.py` — injects relevant memories before each prompt
- `Stop` → `retain.py` (async) — stores session observations after each turn

**Taxonomy reinforcement:** Indirect. Hindsight can recall which domains a user has worked in, which plugins were activated, which skills were useful — but this is passive and unstructured. No hook explicitly fires on domain-boundary events or taxonomy navigation.

**Gap:** No hook for "user request spans multiple domains" or "requested skill is in wrong domain." Taxonomy awareness is not hook-enforced.

**Only plugin with hooks.** No other plugin in the marketplace registers hooks.

---

### M5: Commands (ACTIVE — 3 plugins, 8 commands)

**Inventory:**

| Command | Plugin | Domain | Function |
|---------|--------|--------|----------|
| `/brainstorm-swarm:start` | brainstorm-swarm | P | Orchestrates the full swarm brainstorm workflow |
| `/hindsight` | hindsight | I | Drives recall/reflect/retain/stats against Hindsight CLI |
| `/python-development:create-feature-task` | python-development | E | Creates structured feature task |
| `/python-development:use-command-template` | python-development | E | Applies command template |
| `/python-development:analyze-test-failures` | python-development | E | Analyzes test failure patterns |
| `/python-development:comprehensive-test-review` | python-development | E | Full test suite review |
| `/python-development:test-failure-mindset` | python-development | E | Reframes test failures |
| `/python-development:templates/*` | python-development | E | Template management |

**Taxonomy reinforcement:** Minimal. Commands are plugin-local — they deepen one plugin's functionality but don't navigate between plugins or domains.

**Gap:** No cross-domain command (e.g., `/skillstack:find <topic>` for domain-aware plugin lookup). No M-domain commands. No I-domain command beyond `/hindsight`.

---

### M6: Agents / subagent types (ACTIVE — brainstorm-swarm only)

**How it works:** `brainstorm-swarm` registers 12 named subagent types (pm, engineer, designer, skeptic, optimist, veteran, junior, etc.). These are invocable via `Task(subagent_type="brainstorm-swarm:<name>")`.

**Coverage:** 1 plugin. All 12 agents serve the P-domain brainstorm use case.

**Taxonomy reinforcement:** None at the taxonomy level — agents are internal to brainstorm-swarm's workflow, not cross-domain routers.

**Gap:** No agent for "route user to correct domain based on intent." No domain-navigator agent.

---

### M7: Per-skill scripts (ACTIVE — 21 plugins, skill-level helpers)

**How it works:** Scripts live at `<plugin>/skills/<skill>/scripts/`. Referenced from SKILL.md as runnable helpers. Examples: `api-design` has `schema_analyzer.py`, `validate-api-spec.sh`; `cicd-pipelines` has `pipeline_analyzer.py`, `verify-badge-criteria.sh`; `code-review` has `multi_agent_review.py`, `security_scan.sh`.

**Coverage:** 21 plugins have skill-level scripts. All in E or I domain — no M or P plugin has scripts.

**Taxonomy reinforcement:** None at taxonomy level. Scripts deepen individual skill execution.

**Gap:** M and P plugins have no scripted helpers. M skills (writing, editing) are text-only — scripts less natural here. P skills (frameworks, matrices) could benefit from scoring scripts.

---

### M8: References and templates (ACTIVE — passive depth layer)

**How it works:** `<plugin>/skills/<skill>/references/` holds deep-dive markdown. `templates/` holds reusable scaffolds. Both are available to SKILL.md via `Read`.

**Coverage:** Most E plugins have extensive references (cicd-pipelines has ~30 reference files, api-design has ~15). I plugins have moderate references. P and M plugins are lighter.

**Taxonomy reinforcement:** None. References are intra-skill — no cross-domain reference linking.

---

### M9: Validator and build scripts (ACTIVE — structural integrity)

**How it works:**
- `.github/scripts/validate_plugins.py` — pre-commit: verifies version trio, path_in_repo, SKILL.md cross-refs
- `scripts/build-marketplace.py` — generates `marketplace.json` from plugin.json
- `scripts/build-registry.py` — generates `registry.json` + collections from marketplace.json

**Taxonomy reinforcement:** `build-registry.py` is the taxonomy enforcement point — it groups plugins into collections based on `category`. Currently inert (empty category). Phase 5 activates this.

**Gap:** Validator doesn't check that `category` is set to a valid domain value. Phase 5 should add this check.

---

## Mechanism Map: Domain vs Coverage

| Mechanism | E | I | P | M | Cross |
|-----------|---|---|---|---|-------|
| Trigger descriptions | Y | Y | Y | Y | N |
| category collections | — | — | — | — | — (Phase 5 fix) |
| skillstack-workflows | Y | Y | Y | **N** | Y |
| Hooks | N | Y | N | N | N |
| Commands | Y | Y | Y | N | N |
| Agents | N | N | Y | N | N |
| Scripts | Y | Y | N | N | N |
| References | Y | Y | P | P | N |
| Validator | Y | Y | Y | Y | N |

Legend: Y=covered, N=absent, P=partial, —=not yet activated

**M-domain has the weakest reinforcement:** no workflows, no commands, no scripts, no hooks. Relies entirely on trigger descriptions.

---

## Findings

### F1: Category field is the single highest-leverage Phase 5 action

Setting `category` on all 59 plugins activates the `build-registry.py` collection mechanism and makes the domain taxonomy visible in the marketplace. Zero risk — the field is optional today, and the build script already handles it.

**Recommended Phase 5 action:** Set `category` to `{Engineering | Meta-Infra | Managerial-Product | Marketing-Comms}` on all 59 `plugin.json` files. Update marketplace and registry. Bump versions per trio rule.

---

### F2: M-domain needs a workflow

No `skillstack-workflows` skill serves the M domain. Five M plugins exist with no cross-plugin composition path.

**Recommended new workflow:** `editorial-pipeline` — compose `deslop → technical-copywriting → ux-writing → communication` into a content production workflow. Fits the existing `skillstack-workflows` multi-skill pattern.

**Scope:** Post-Phase-5. Not in the current migration.

---

### F3: Validator should gate on category value

`validate_plugins.py` does not check whether `category` is a valid domain value. After Phase 5 sets categories, a malformed or empty category would silently produce bad collections.

**Recommended addition to validator:**

```python
VALID_CATEGORIES = {"Engineering", "Meta-Infra", "Managerial-Product", "Marketing-Comms", ""}
# "" allowed pre-migration; could make non-empty mandatory post-Phase-5
if plugin_data.get("category", "") not in VALID_CATEGORIES:
    errors.append(f"{plugin}: invalid category '{plugin_data['category']}'")
```

**Scope:** Phase 5 — add before or alongside the category migration.

---

### F4: Cross-domain trigger disambiguation is missing

When a user request activates multiple skills from different domains simultaneously (e.g., "write secure API docs" → api-design E + security E + documentation-generator E + technical-copywriting M), no mechanism disambiguates or sequences them.

**Current state:** Claude Code routes to the best single match or activates multiple skills without ordering guidance.

**Potential mechanism:** A `routing-guide` skill or an updated `skillstack-workflows` preamble that identifies domain blend and sequences appropriately. Not a blocker for Phase 5 — document as a post-migration enhancement.

---

### F5: No collection-level discoverability today

Without `category` set, users browsing the marketplace see no collections — only the flat 59-plugin list. Post-Phase-5, the 4-domain collections appear automatically via `build-registry.py`. No additional code changes needed beyond category field population.

---

## Phase 5 Mechanics

Phase 5 requires these specific file changes per plugin:

```
<plugin>/.claude-plugin/plugin.json      → set "category": "<domain>"
.claude-plugin/marketplace.json          → update category field for plugin entry  
.claude-plugin/registry.json             → update category field + regenerate collections
<plugin>/CHANGELOG.md                    → new version entry
```

Version bump required per trio rule (plugin.json ↔ marketplace.json ↔ registry.json must all match). One commit per plugin. 59 commits minimum, or grouped by domain batch if the validator permits multi-plugin staging (it does — validator runs across the whole working tree, so staging all E-domain plugins before committing works as long as all their version trios are consistent).

**Recommended batching:** 4 commits — one per domain — rather than 59 individual commits. Verify: does `validate_plugins.py` require each plugin to be independently consistent, or does it allow mixed-version staging? Answer: it checks every plugin in the working tree, so all staged plugins must be consistent. Batch commits by domain are safe.

**Version bump strategy:** Category change is a non-breaking metadata change. Bump patch version (e.g., `1.0.5` → `1.0.6`). No SKILL.md content changes — no behavior change to signal.

---

## Post-Phase-5 Roadmap (mechanisms)

| Priority | Mechanism | Domain impact |
|----------|-----------|--------------|
| P0 | Add `editorial-pipeline` workflow to skillstack-workflows | M |
| P1 | Add category validation to validate_plugins.py | All |
| P1 | Add M-domain commands (at least one `/communication:*` or `/editorial:*`) | M |
| P2 | Cross-domain routing guidance in skillstack-workflows README | All |
| P2 | P-domain scoring scripts (RICE, ICE calculators) | P |
| P3 | Domain-navigator agent or skill | All |

---

*Decisions D-012 through D-014 logged in `hindsight/DECISIONS.md`*

---
*Pending Phase 5 approval*
