---
name: debug-complex-issue
description: Loop workflow for debugging a complex issue you've been stuck on for more than 30 minutes. Runs systematic hypothesis formation (debugging skill), feedback-loop mapping when the bug looks like a dynamic problem (systems-thinking), context-pathology check when it's an LLM/agent bug (context-degradation), blast-radius assessment before any fix attempt (risk-management), and uses test-driven-development as the debugging oracle — write a failing test that reproduces the bug, then iterate fix → test until green. Use when a bug has defeated a first-pass attempt, when symptoms seem to shift under investigation, when an LLM-based system is misbehaving in ways simple prompt fixes don't resolve, or when you need to fix safely under production constraints. NOT for obvious bugs where the fix is visible — just fix those directly.
---

# Debug Complex Issue

> Most complex bugs aren't complicated — they're just resistant to the first hypothesis you form. This workflow replaces hunting with a deliberate loop that forces evidence before every attempted fix.

Stuck debugging usually means the bug has a property the debugger hasn't noticed yet: it's timing-dependent, state-dependent, environment-dependent, or the result of a feedback loop that's invisible from any single stack trace. This workflow surfaces that property.

---

## When to use this workflow

- A bug has defeated your first one or two fix attempts
- Symptoms shift under investigation (the repro stops reproducing, or moves)
- An LLM or agent is behaving wrong in ways prompt tweaks don't fix
- The fix must be safe under production constraints (no trial-and-error allowed)
- You're handing the bug off and want to hand over structure, not just a stack trace
- You've been stuck for more than 30 minutes

## When NOT to use this workflow

- **The bug is obvious** — just fix it
- **Tight feedback loop in dev** — you can iterate in seconds, no workflow overhead needed
- **You need triage, not debugging** — is this even worth fixing right now? use prioritization instead
- **Post-incident learning** — use a postmortem template, not a debugging workflow

---

## Prerequisites

Install these plugins:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install debugging@skillstack
/plugin install systems-thinking@skillstack
/plugin install context-degradation@skillstack
/plugin install risk-management@skillstack
/plugin install test-driven-development@skillstack
```

---

## Core principle

**Write the failing test before you write the fix.** This is the single most important debugging rule and it's also the one developers skip most often under pressure. A failing test turns "I think I fixed it" into a deterministic check. Without it, you'll introduce the bug again in three months and not know until production.

The secondary principle: **evidence before hypothesis before attempt**. A fix attempted without an explicit hypothesis is a lottery ticket. A hypothesis formed without evidence is a guess. The workflow enforces the order.

---

## The loop

### Phase 1 — observe (before forming any hypothesis)

Load the `debugging` skill. Before hypothesizing anything:

- Write down what you actually observed, not what you think it means. ("The process exited with code 137" — not "OOM killer triggered".) Separate observation from interpretation; they'll blur together if you don't.
- Identify what's consistent vs. what varies. Consistent details constrain the hypothesis space. Varying details often contain the diagnostic signal (timing, order, environment).
- Find the minimum reproducer. If you can't reproduce the bug on demand, that's the bug you're working on until you can — the "flaky test" or "intermittent error" IS the bug.

If you can't reproduce it after 30 minutes of trying, escalate: it's likely timing- or state-dependent and you need different tooling (logging, tracing, memory dumps).

### Phase 2 — classify (what kind of bug is this?)

Complex bugs cluster into a few families. Match the family first; it tells you which tools to reach for.

| Family | Signal | Tool to add |
|---|---|---|
| **Race / timing bug** | Symptoms change with system load, CPU count, or added logging | Add `systems-thinking` — this is a feedback loop or a delay |
| **State-machine bug** | Failure depends on the order of prior events, not on any single step | `systems-thinking` again — map the state graph explicitly |
| **Environment bug** | Works locally, breaks in CI/prod (or vice versa) | Compare environments; delta is the diagnosis |
| **Resource exhaustion** | Bug only appears after N operations or time T | Leak or unbounded growth; add instrumentation |
| **Flaky test** | Same test passes and fails with no code change | Race condition or hidden state dependency; see `debugging` skill's test-pollution section |
| **LLM/agent misbehavior** | Agent gives wrong answer, loops, or drifts over a session | Add `context-degradation` — it's likely lost-in-middle, poisoning, clash, or confusion |
| **Upstream dependency** | Bug tracks to a library/service you don't own | Pin versions; isolate; decide whether to upstream the fix |

### Phase 3 — hypothesize (one at a time)

For each hypothesis, write it down in one sentence, then ask:

- What would I expect to see if this hypothesis is true?
- What would I expect to see if it's false?
- Can I observe either without changing production state?

Abandon any hypothesis you can't test. Hypotheses you can't test are fiction.

**Multi-hypothesis discipline.** If you have several plausible causes, don't pick a favorite and chase it. Instead, run cheap tests that differentiate. Example: a bug could be caused by cache invalidation OR by a bad config. A one-line config check is faster than investigating the cache.

### Phase 4 — assess blast radius (before touching anything)

Load the `risk-management` skill. For each potential fix, ask:

- What could this change break that's currently working?
- How would I detect regression?
- Can I roll back?
- If I ship this fix at 5pm on a Friday, what's the worst case?

For production bugs, write the rollback plan before the fix. "Git revert" is acceptable if your release process supports it. For stateful changes (migrations, data fixes), the rollback plan needs specifics — "restore from backup dated X, replay events from Y".

If the fix would affect more systems than the one with the bug, stop and loop back to Phase 3 — you probably have the wrong hypothesis.

### Phase 5 — the TDD loop (the core of the workflow)

Load the `test-driven-development` skill.

**Step 1: write a failing test that reproduces the bug.**

This is the single highest-leverage debugging activity and the one most debugging effort skips. The test is the contract that says "this specific behavior must work". It gives you:
- A deterministic repro (no more "I think it's fixed")
- A permanent regression guard
- A way to iterate quickly without running the full system
- Evidence of completion when the fix is real

If the bug is hard to reproduce in a unit test, reproduce it in whatever scope you can — integration, end-to-end, a scripted scenario. The test doesn't have to be pretty; it has to fail for the right reason.

**Step 2: run the failing test.** Confirm it fails. If it passes, your test doesn't actually capture the bug — loop back.

**Step 3: attempt the minimal fix.**

Not the best fix. Not the architecturally beautiful fix. The minimum change that makes the test pass. Bigger rewrites during debugging hide what's actually fixing the bug.

**Step 4: run the test.**

If it's green, you have a concrete "this change fixed this bug" claim. If it's still red, your hypothesis is probably wrong — loop back to Phase 3. Don't keep hacking at a wrong hypothesis.

**Step 5: run the surrounding test suite.** The fix may have broken something else. Broken tests outside the scope of your change are evidence that your fix has wider blast radius than you thought — loop back to Phase 4.

**Step 6: if green, write a second test.** A regression test covering a slightly different variation of the same bug. This catches the "fixed the specific case, not the underlying cause" trap.

### Phase 6 — document the bug, not just the fix

When you commit, the commit message should explain:

1. What the symptom was (observable behavior)
2. What the cause was (the underlying mechanism)
3. Why the fix works (which property of the system it relies on)
4. What test guards against regression
5. Any related areas you investigated and ruled out

Future-you or another debugger will hit a similar-looking bug in six months. The commit message is how they'll find and learn from this one.

---

## Specific loop variants

### Variant: LLM/agent bug

Substitute Phase 2's classification with a `context-degradation` audit:

- Is this **lost-in-middle**? (Important info mid-context ignored.) Test by moving the info to the end.
- Is this **context poisoning**? (Earlier wrong info persisting into later turns.) Test by stripping the poisoned content.
- Is this **context clash**? (Two valid pieces of context contradicting each other.) Test by presenting only one side.
- Is this **context confusion**? (Too much unrelated info making the agent unfocused.) Test by pruning.
- Is this a **model capability limit**? (The task is beyond the model's reasoning threshold.) Test with a larger model — if it works, the fix is model routing, not prompt engineering.

Then Phase 5's test can be a pinned prompt + expected output, iterated under the hypothesis.

### Variant: state-machine / concurrency bug

In Phase 3, draw the state graph explicitly. Most concurrency bugs live in transitions the graph doesn't account for. Add logging at every transition, not at every statement — transition logs show the sequence, statement logs drown you.

For race conditions specifically: stress-test with unnatural timing (thread sleeps, forced context switches). A race condition that reproduces under artificial delay is a race condition that can exist under natural load.

### Variant: environment-specific bug

In Phase 3, the goal is to find the environment delta. Systematic approach:
- Diff installed versions (dependencies, runtime, OS)
- Diff environment variables
- Diff file-system state (permissions, presence of expected files)
- Diff network state (outbound connectivity, DNS, TLS)

The first observable difference is usually the cause. Stop and verify before chasing further.

---

## Gates and failure modes

**Gate 1: the reproducer gate.** Phase 5 cannot start until you have a reliable repro. If you attempt a fix without a repro, you're guessing.

**Gate 2: the rollback gate.** For production bugs, Phase 5 cannot start until Phase 4 has produced a specific rollback plan. "Git revert" counts; vague confidence doesn't.

**Gate 3: the second-test gate.** Phase 5 step 6 is non-negotiable. A fix with only the exact repro test is brittle — it fixes the case you found, not necessarily the cause.

**Failure mode: hypothesis anchoring.** You formed a hypothesis in the first 5 minutes and now every observation is interpreted as evidence for it. Mitigation: Phase 2's family-matching. If none of the families fit your hypothesis, the hypothesis is probably wrong.

**Failure mode: "I know this code".** Intimate knowledge of the codebase is the #1 cause of missed bugs in familiar code. You stop observing and start assuming. Mitigation: Phase 1 discipline. Separate observations from interpretations.

**Failure mode: fix creep.** "While I'm in here, let me also clean up..." turns a 50-line debugging change into a 500-line refactor and now nobody can tell which change fixed the bug. Mitigation: Phase 5 step 3's "minimal fix" rule. Open a second PR for the refactor after the bug is closed.

**Failure mode: relief bias.** After spending three hours on a bug, the first fix attempt that "seems to work" feels like a win and you ship it. Mitigation: Phase 5 step 6 (second test) and Phase 6 (document cause, not just fix). Both force you to understand the bug instead of just making the symptom go away.

---

## Output artifacts

A completed debug run produces:

1. **The fix itself** — a minimal diff, not a rewrite
2. **At least two tests** — one reproducing the bug, one covering a related variation
3. **A commit message** explaining symptom, cause, fix rationale, and ruled-out hypotheses
4. **A notebook entry** (for team learning) if the bug revealed a class of issue rather than a one-off

---

## Related workflows and skills

- For understanding why an LLM agent is stuck or drifting, pair with the `context-optimization` skill
- For widespread debugging across a legacy codebase, use the `legacy-rescue` workflow
- For deciding whether this bug deserves priority at all, use the `strategic-decision` workflow
- For post-hoc team learning, write a structured postmortem (see `documentation-generator` skill)

---

> *Workflow part of [skillstack-workflows](../../../README.md) by [Viktor Bezdek](https://github.com/viktorbezdek) — licensed under MIT.*
