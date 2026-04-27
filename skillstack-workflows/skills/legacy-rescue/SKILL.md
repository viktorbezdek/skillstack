---
name: legacy-rescue
description: Loop workflow for making real progress on a legacy codebase without breaking production. Starts by generating a codemap so you actually understand what exists (documentation-generator), identifies feedback-center modules (systems-thinking), gets a second perspective on areas you'll touch (code-review), builds a test safety net before any changes (test-driven-development), plans changes with rollback options (risk-management), makes small atomic commits (git-workflow), and loops through debugging as issues surface. Use when inheriting a codebase that's hard to change safely, when a production system needs modernization, or when you've been told "just don't break anything" but also need to ship features. NOT for greenfield work or isolated script changes.
---

# Legacy Codebase Rescue

> The dominant failure mode in legacy work isn't breaking things — it's refusing to touch anything because you might break things, then shipping nothing. This workflow makes legacy work safe enough to actually do.

Legacy code is code where the cost of change is higher than the cost of understanding. The rescue isn't a rewrite (almost always the wrong answer) — it's establishing enough safety that change becomes affordable again.

---

## When to use this workflow

- Inheriting a codebase with no tests, no docs, and the original author unreachable
- Modernizing a production system that currently works but is fragile
- Adding a feature to code that hasn't been touched in years
- Ghost-fixing a bug in a module everyone is afraid of
- Being told "just don't break anything" while also needing to ship

## When NOT to use this workflow

- **Greenfield work** — start with the `zero-to-launch` approach instead (workflow 1, not built yet)
- **Isolated script changes** — no test harness needed for a 50-line utility
- **A full rewrite has been green-lit** — different discipline; this workflow preserves, it doesn't replace
- **You can throw the system away** — if deletion is an option, consider it seriously before starting this

---

## Prerequisites

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install documentation-generator@skillstack
/plugin install systems-thinking@skillstack
/plugin install code-review@skillstack
/plugin install test-driven-development@skillstack
/plugin install risk-management@skillstack
/plugin install git-workflow@skillstack
/plugin install debugging@skillstack
```

---

## Core principle

**Make small, reversible changes frequently, not large, irreversible changes rarely.** The mathematical fact of legacy work: a large refactor has higher risk than N small refactors that accomplish the same thing, because blast radius is roughly linear in change size. The discipline is to resist the urge to fix everything at once.

Secondary principle: **build the safety net before you need it.** Writing tests after you've broken something is not testing — it's salvage. Tests written before any change become permanent infrastructure.

---

## The phases

### Phase 1 — codemap (documentation-generator)

Load the `documentation-generator` skill with codemap intent.

Before touching anything, produce a map of what exists. This is not documentation for the future — it's orientation for you right now. The goal is to know:

- **Module inventory** — what modules exist, what each owns
- **Entry points** — which modules are the entry points (HTTP handlers, message consumers, scheduled jobs)
- **Dependency graph** — which modules call which. This is critical. Circular dependencies are red flags.
- **Boundaries** — which modules are "pure" logic vs. "glue" (network, database, file system)
- **External contracts** — what APIs does this system expose to callers? What does it call?
- **Data flow** — for the major use cases, trace the data from input to output
- **Configuration** — what knobs exist, which matter

Output: a written codemap document (not code). For a small system, a single markdown file. For a large system, one per module. The `documentation-generator` skill has patterns for both scales.

The codemap is for YOU, in the next phase. It's an investment in legibility before action.

### Phase 2 — identify feedback centers (systems-thinking)

Load the `systems-thinking` skill.

Not all modules are equal. Some modules are structural hubs — many things depend on them, they live at the intersection of multiple concerns, and changes to them ripple widely. Others are leaf modules — nothing depends on them, and changes stay local.

Use the dependency graph from Phase 1 to find:

- **High in-degree modules** — many things import them. These are the structural hubs. Changes here have wide blast radius.
- **High out-degree modules** — they import many things. These are the orchestrators. Changes here often require understanding of the imported modules.
- **Cyclic dependencies** — circular imports. These are sources of confusion and are often where bugs live. Flag them but don't fix them yet.
- **Lonely modules** — nothing imports them, and they import little. These are safer to change and often safer to delete.

The strategic move: **make your changes in lonely modules first, or in well-defined leaves of the dependency graph.** Save the structural hubs for when you have the most test coverage and the clearest rollback plan.

Output: a prioritized list of modules ordered from "change first, lowest risk" to "change last, highest risk".

### Phase 3 — second opinion on the target areas (code-review)

Load the `code-review` skill.

Before you change anything, get a second perspective on the specific areas you'll touch. Even if "second perspective" means you reviewing your own work 24 hours later, the fresh eyes matter.

Apply:

- **Security review** — is there an exploit you're about to expose by changing this? Legacy code often has implicit assumptions that security depends on.
- **Performance review** — is this module on a hot path? Does your change have throughput implications?
- **Architectural review** — does the module's boundary match its current responsibility? Often in legacy code, the boundary has drifted.
- **Style vs. substance** — separate what you're tempted to clean up (style) from what you need to change (substance). The style cleanup can come later, in its own commit.

Output: a "areas of risk" document listing what to watch for in the changes you're planning.

### Phase 4 — build the safety net (test-driven-development)

Load the `test-driven-development` skill.

Now, BEFORE any changes, build tests around the code you're about to change. The tests should cover:

- **Current behavior** — whatever the system does today, lock it in with a characterization test. "Characterization test" = a test that captures actual behavior (including quirks) so you can detect when it changes. This is not about correctness; it's about detection.
- **Edge cases you noticed** — weird inputs, boundary conditions, null handling, empty collections
- **Critical paths** — the code paths that handle the most volume, the most revenue, or the most risk
- **Your planned changes** — tests for the NEW behavior you're about to introduce, which will fail until you make the change

The characterization tests are the key innovation. They lock in behavior you might not even understand. When you later change code and a characterization test fails, you know you changed something that someone depended on.

The legacy code's original author may have been defending against concrete bugs you haven't encountered yet. If a characterization test starts failing in an unexpected way, you just discovered one of those defenses. Don't just "fix" the test — investigate why it was there.

Output: a test suite that runs in CI and covers the surface area of your planned changes.

### Phase 5 — plan the change with a rollback (risk-management)

Load the `risk-management` skill.

For each change, write the answer to:

- **What could this break that's currently working?** Be specific.
- **How will I detect regression?** The characterization tests from Phase 4 are one answer. Production monitoring is another. Both are better.
- **What's my rollback path?** Git revert is the minimum. For stateful changes (migrations, data fixes), you need a more specific rollback — usually "restore from backup dated X, replay events from Y".
- **What's the blast radius if this goes wrong in production?** If the answer involves "every user" or "all data", you need a more cautious approach: feature flag, gradual rollout, shadow deployment.

For legacy work specifically:
- **Prefer feature flags over branches.** A feature flag lets you ship the change in an "off" state, turn it on for 1% of traffic, and verify before committing.
- **Prefer dual-write over cutover.** If you're changing how data is stored, write to both the old and new stores for a period, compare, then remove the old.
- **Prefer parallel old/new over replacement.** Keep the old code path working until you've verified the new one. Delete the old path only when confidence is high.

Output: a change plan for each area with explicit rollback steps.

### Phase 6 — make small atomic commits (git-workflow)

Load the `git-workflow` skill.

Make each change as small as possible. "Atomic" means: one logical change per commit, passing tests, independently reviewable, independently revertable.

- **One concern per commit.** A commit that "fixes bug X, also renames Y, and adds test Z" is three commits.
- **Each commit ships green.** Even if you're not pushing yet, each commit should have tests passing. If it doesn't, you lose the ability to bisect.
- **Commit messages explain the WHY.** In legacy work, the why is often the reason this change is safe. "Renamed X to Y because the old name implied a behavior that hasn't been true since 2019, and I verified via characterization tests that no consumer depends on the name."

Commit cadence: in legacy work, small and frequent beats large and rare. Ten 5-line commits are easier to review, revert, and debug than one 50-line commit.

Output: a commit history that a future person (possibly you) can bisect and understand.

### Phase 7 — the debugging loop

As you make changes, issues will surface. Load the `debugging` skill.

For any issue that appears:

1. **Does a characterization test detect it?** If yes, you've discovered a behavior dependency that wasn't obvious. Investigate before "fixing" the test.
2. **Does production monitoring show it?** If yes, rollback is the first move; understanding is the second.
3. **Can you reproduce it locally?** If yes, loop into the `debug-complex-issue` workflow.
4. **If the cause is in an area outside your change?** You may have uncovered a latent bug that the old behavior was accidentally compensating for. Fix it as a separate change with its own test.

---

## Gates and failure modes

**Gate 1: the map gate.** Phase 2 cannot start until Phase 1's codemap exists. Working on a module you don't have a dependency picture for is how you accidentally break things two modules away.

**Gate 2: the test gate.** Phase 6 (commits) cannot start until Phase 4 (test safety net) has produced tests covering the areas you'll change. Changes without tests are legacy work done the old way — and that's why you're rescuing legacy code in the first place.

**Gate 3: the rollback gate.** Each commit must have a rollback plan before it's written. "Git revert" is fine for stateless changes; stateful changes need more.

**Failure mode: the grand refactor.** You see many things you want to fix and decide to do them all in one sprint. Blast radius compounds. Something breaks. Root cause is unclear. You revert the whole thing and lose three days of work. Mitigation: Phase 6's atomic commit discipline. No exceptions.

**Failure mode: fear-based stasis.** You're so afraid of breaking things that you ship nothing. Mitigation: Phase 4's safety net makes small changes safe. Start with the smallest possible change to the least-connected module to build confidence.

**Failure mode: skipping characterization tests.** You think you understand the code well enough. You rewrite without tests. Something breaks in a case you didn't know was a case. Mitigation: characterization tests capture what you don't know, not what you do.

**Failure mode: the cleanup spiral.** While in Phase 6, you see code you want to clean up. You clean it. Now you're three levels deep in a refactor that wasn't in Phase 5's plan. Mitigation: separate cleanup commits. Open a second PR for style cleanup after the functional change has landed.

**Failure mode: removing "dead" code that isn't.** Phase 1 found a module nothing imports. You delete it. Three weeks later production breaks because it was called dynamically via reflection / a scheduled job / a feature flag / an eval. Mitigation: before deleting, check logs for runtime invocation, not just static imports.

---

## Output artifacts

A completed rescue phase produces:

1. **A codemap** — reusable orientation for the next person (or future-you)
2. **A dependency graph** — structural understanding of what depends on what
3. **A test safety net** — permanent infrastructure that makes future changes safer
4. **An audit trail of commits** — small, atomic, each with rollback context
5. **Rollback plans** — for stateful changes that can't be git-reverted
6. **A list of discoveries** — bugs found that were latent, assumptions that weren't documented, defenses that weren't obvious

The codemap and test net are the real output. The changes are downstream of them.

---

## Related workflows and skills

- For understanding why a bug is hard before attempting the rescue, use the `debug-complex-issue` workflow
- For deciding whether a rescue is even worth it vs. a rewrite or deletion, use the `strategic-decision` workflow
- For presenting the need for this work to stakeholders, use the `pitch-sprint` workflow
- For the first passes at the codemap, use `documentation-generator` directly

---

> *Workflow part of [skillstack-workflows](../../../README.md) by [Viktor Bezdek](https://github.com/viktorbezdek) — licensed under MIT.*
