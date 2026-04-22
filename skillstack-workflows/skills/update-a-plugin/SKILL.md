---
name: update-a-plugin
description: Workflow for modifying an existing Claude Code plugin — adding a new skill, fixing activation issues, improving content quality, adding hooks, or restructuring components. Composes five phases: audit current state (plugin-validation + plugin-evaluation), classify the change type, implement using the appropriate plugin-dev skills (skill-foundry / plugin-hooks / plugin-composition / plugin-architecture), regression-check via re-validation and re-evaluation, then version bump and README update. Use when extending or fixing an existing plugin with any component changes. NOT for building a new plugin from scratch — use the build-a-plugin workflow for that. NOT for a single-SKILL.md edit with no structural changes — edit the file directly.
---

# Update a Plugin

> The risk in modifying an existing plugin is regression. Build plugins are blank slates. Update workflows have existing users, existing evals, and existing activation patterns that must survive every change intact.

Updating a plugin feels simpler than building one. It rarely is. Adding one skill can invalidate activation boundaries across other skills. Changing frontmatter can break trigger evals that were passing. Restructuring a manifest can silently drop components. This workflow forces a complete audit before the first edit and a full regression check after the last one.

---

## When to use this workflow

- Adding a new skill to an existing plugin
- Fixing a skill that activates too broadly or too narrowly
- Improving the content quality of an existing skill
- Adding hook-based automation to a plugin that currently has only skills
- Adding an MCP server or subagent to an existing plugin
- Restructuring plugin components without changing their purpose
- Bumping a plugin version after accumulated changes

## When NOT to use this workflow

- **New plugin from scratch** — use the `build-a-plugin` workflow
- **Single-line SKILL.md edits** — edit directly, no workflow needed
- **Renaming or moving a plugin** — that is a repo operation, not a plugin operation
- **Eval-only updates** — extend the eval files directly, then re-run

---

## Prerequisites

```
/plugin install plugin-validation@skillstack
/plugin install plugin-evaluation@skillstack
/plugin install plugin-architecture@skillstack
/plugin install skill-foundry@skillstack
/plugin install plugin-hooks@skillstack
/plugin install plugin-composition@skillstack
```

Load only what your change type requires. Phase 3 tells you which ones.

---

## Core principle

**Audit before touching, regression-check after touching.** The complete state of the plugin — structure, activation, output quality — must be known before the first edit. After the last edit, the same checks run again. Any regression discovered in Phase 4 rolls back the change, not the check.

Secondary principle: **change type determines toolkit.** Adding a skill, fixing frontmatter, adding a hook, and restructuring the manifest are four different operations with four different risk profiles. Identifying the change type in Phase 2 determines which plugin-dev skills you actually need — not all of them, just the right ones.

---

## The phases

### Phase 1 — audit current state (plugin-validation + plugin-evaluation)

Load `plugin-validation` and `plugin-evaluation` before making any edit.

**Structural audit (plugin-validation):**
- Does `plugin.json` have all required fields? Are paths resolving?
- Does every skill have valid frontmatter (`name`, `description`)?
- Do all referenced files exist on disk?
- Are hook scripts executable with valid event patterns?

Record every existing error. These are pre-existing issues — you did not introduce them. But you must not leave the plugin in worse structural shape than you found it.

**Activation audit (plugin-evaluation trigger evals):**
- Run the existing trigger evals. Record which pass and which fail.
- If trigger evals don't exist yet, write them now before proceeding. You cannot measure regression without a baseline.
- Map which queries activate which skills. This is the activation surface you must protect.

**Output audit (plugin-evaluation output evals):**
- Run the existing output evals. Record which pass and which fail.
- Note which evals are weakest — these are likely the ones your change will affect.

Output: a written snapshot of current state — structural errors (if any), trigger eval pass rate, output eval pass rate. This is your regression baseline.

### Phase 2 — classify the change

Identify which category your modification falls into. Each has a different risk profile and toolkit:

| Change type | Risk | Skills to load |
|-------------|------|----------------|
| **Add a new skill** | Medium — new skill may overlap existing activation surfaces | `skill-foundry`, `plugin-composition` |
| **Fix activation** | Low-Medium — frontmatter changes, description rewrites | `skill-foundry` (frontmatter section) |
| **Improve content** | Low — content changes rarely affect structure | `skill-foundry` (content section) |
| **Add a hook** | Medium — hooks run unconditionally on matched events | `plugin-hooks`, `plugin-composition` |
| **Add MCP/subagent** | High — new components require manifest changes and wiring | `plugin-architecture`, `plugin-composition` |
| **Restructure** | High — component splits/merges affect everything | `plugin-architecture`, `plugin-composition`, `skill-foundry` |

If your change spans multiple categories, split it into discrete steps and handle each step's risk profile separately.

Output: a one-line change statement. "I am adding a new skill that does X to the plugin that does Y."

### Phase 3 — implement (skill-foundry / plugin-hooks / plugin-composition / plugin-architecture)

Load only the skills your change type requires (from Phase 2's table). Implement one change at a time.

**Adding a new skill (skill-foundry + plugin-composition):**

Load `skill-foundry`. Follow its conventions:
- Frontmatter: `name` and `description` are the activation surface. Write them last, after you know what the skill does.
- Progressive disclosure: lead with the most-used knowledge, defer edge cases to reference files.
- Scope: a skill that does everything activates on nothing. Scope the description tightly.

After the skill file exists, load `plugin-composition` and wire it into the manifest. Verify the path resolves.

**Fixing activation (skill-foundry frontmatter):**

The frontmatter `description` field determines when the skill activates. Rewrite it with specific triggers and explicit anti-triggers (NOT clauses). Run trigger evals immediately after each rewrite to measure the change before proceeding.

Pattern that works: "Use when [specific scenario]. NOT for [adjacent scenario that should NOT trigger this]."

**Adding a hook (plugin-hooks + plugin-composition):**

Load `plugin-hooks`. Identify the event (PreToolUse, PostToolUse, Stop, UserPromptSubmit). Write the hook script. Set the matcher to the narrowest pattern that covers your use case — broad matchers run on every tool call.

Wire the hook into `plugin.json` via `plugin-composition`. Hooks do not auto-discover; they must be declared in the manifest.

**Adding MCP/subagent or restructuring (plugin-architecture first):**

Load `plugin-architecture` before writing code. Map the new component, its type, and how it interacts with existing components. Component additions that aren't mapped first produce manifest drift — the code exists but the manifest doesn't know about it.

After the architecture document exists, implement and wire via `plugin-composition`.

### Phase 4 — regression check (plugin-validation + plugin-evaluation)

Run the same checks from Phase 1 against the modified plugin.

**Structural regression:**
- Run `plugin-validation` again. Zero new errors permitted.
- If a pre-existing error was fixed as a side effect, note it — that is a bonus, not a risk.

**Activation regression:**
- Run all existing trigger evals. Every test that was passing in Phase 1 must still pass.
- If a previously-passing trigger now fails, the change broke something. Roll back the specific edit that caused the regression — not the entire change.

**New coverage:**
- Write new trigger evals for the new skill or changed behavior. Minimum: 5 positive triggers and 3 negative triggers.
- Write new output evals for any new skill. Minimum: 2 scenario-based evals.
- Run them. Iterate until they pass.

**Gate:** Phase 5 cannot start until all existing evals still pass AND new evals pass.

### Phase 5 — version bump and documentation update

Bump the version in `plugin.json`. Use semantic versioning:
- **Patch** (x.y.Z) — content fixes, activation improvements, no new components
- **Minor** (x.Y.0) — new skill, new hook, new MCP tool added
- **Major** (X.0.0) — restructure, removed component, breaking interface change

Update the `description` field in `plugin.json` if the plugin's capability surface changed.

Update `README.md` to reflect any new skills, changed activation triggers, or new prerequisites.

If the plugin is published in a marketplace, update the marketplace entry's version and description to match.

---

## Gates and failure modes

**Gate 1: the audit gate.** Phase 3 cannot start until Phase 1 has produced a complete baseline (structural state + eval pass rates). Changing code without knowing the current state produces undetectable regressions.

**Gate 2: the regression gate.** Phase 5 cannot start until Phase 4 confirms zero regression in existing evals. Shipping a plugin where old evals broke is strictly worse than shipping no update.

**Failure mode: frontmatter drift.** A new skill's description uses language that overlaps with an existing skill. Both activate on the same queries. Users get both skills loaded simultaneously. Mitigation: Phase 4's trigger evals catch this if they cover the overlapping queries.

**Failure mode: manifest orphan.** A new skill file is created but not declared in `plugin.json`. The skill never loads. Mitigation: `plugin-composition` and `plugin-validation` both catch undeclared components.

**Failure mode: hook scope creep.** A hook added for one purpose runs on every tool call because the matcher is too broad. Mitigation: `plugin-hooks` has matcher-narrowing patterns; review them before committing any hook.

**Failure mode: version not bumped.** The plugin ships with the same version as before. Users with the old version cached never receive the update. Mitigation: Phase 5 makes the version bump mandatory before declaring done.

---

## Output artifacts

1. **Modified plugin files** — only the files that needed to change, nothing else
2. **Updated `plugin.json`** — bumped version, updated description if applicable
3. **Updated `README.md`** — reflects the new capability or fix
4. **New/updated eval files** — `trigger-evals.json` and `evals.json` for changed or new skills
5. **A change log entry** — one sentence per change, what it was and why

---

## Related workflows and skills

- For building a plugin from scratch, use the `build-a-plugin` workflow
- For writing a single new SKILL.md outside a plugin, use the `write-your-own-skill` workflow
- For debugging a plugin that's structurally valid but behaving wrong at runtime, use `debug-complex-issue`
- For evaluating whether a struggling plugin should be rebuilt vs. incrementally fixed, run Phase 1 first — if structural errors plus failing evals exceed 30% of components, consider `build-a-plugin` instead

---

> *SkillStack Workflows by [Viktor Bezdek](https://github.com/viktorbezdek) — licensed under MIT.*
