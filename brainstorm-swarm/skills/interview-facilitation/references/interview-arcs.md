# Interview Arcs

Four standard arcs for a brainstorm-swarm interview. Pick the one that fits the decision and the user's readiness.

## Arc 1 — Divergent only (one round, breadth-first)

The simplest arc. Spawn 5-7 personas in parallel for one round, synthesize, present, done.

```
Frame topic → Pick subset → Phase 1 spawn → Collect → Synthesize → Present → DONE
```

**Best for:** early-stage thinking; "I want fresh angles I haven't considered"; users who want to do the deciding themselves once they have the perspectives.

**Skip:** Phases 2 and 3.

**Total cost:** ~12-18k tokens, ~3-5 min wall.

**Output:** synthesis with consensus / dissent / open questions / per-persona contributions.

## Arc 2 — Probing (two rounds, depth on tension)

Standard arc when Phase 1 surfaces a specific disagreement worth deepening.

```
Phase 1 (divergent) → Synthesize → Identify tension →
Phase 2 (probe — 2-3 personas on the specific disagreement) →
Re-synthesize → Present → DONE
```

**Best for:** a specific disagreement emerged in Phase 1 and resolving it would advance the decision.

**When NOT to use:** Phase 1 surfaced consensus or the tensions are already understood.

**Total cost:** ~20-30k tokens, ~5-10 min wall.

**Output:** Phase 1 synthesis + Phase 2 deep-dive + integrated final.

## Arc 3 — Full arc (three rounds, divergent + probing + convergent)

The complete arc. Use when the user wants a defensible decision with full pressure-testing.

```
Phase 1 (divergent — 6 personas) → Synthesize → Present →
Phase 2 (probe — 2-3 personas on tension) → Synthesize →
User forms tentative direction →
Phase 3 (convergent — 3-4 personas pressure-test the direction) →
Final synthesis → DONE
```

**Best for:** high-stakes decisions; decisions that will be defended to stakeholders later; decisions where the user wants to feel they've considered every angle.

**When NOT to use:** small decisions; the user just wants a quick brainstorm; the user's already decided and wants validation.

**Total cost:** ~35-50k tokens, ~10-20 min wall.

**Output:** full decision document with multi-round synthesis.

## Arc 4 — Decision pressure-test (one round, convergent only)

When the user has a tentative decision and just wants pressure-testing.

```
Frame proposed decision → Pick relevant personas (Skeptic + 2-3 domain) →
Phase 3 spawn (each: strongest FOR, strongest AGAINST, decisive consideration) →
Synthesize the cases → Present → DONE
```

**Best for:** "I'm leaning toward X. Tell me what I'm missing."; final-pass review; decision-defense rehearsal.

**When NOT to use:** the user hasn't formed a tentative direction yet (use Arc 1 or 3).

**Total cost:** ~10-15k tokens, ~3-5 min wall.

**Output:** focused FOR/AGAINST analysis with each persona's decisive consideration.

## Arc selection — quick decision tree

```
What's the user's state?

  Just exploring, no direction yet         → Arc 1 (Divergent only)
  Has tension to resolve                   → Arc 2 (Probing)
  High-stakes decision, wants defensible   → Arc 3 (Full arc)
  Has tentative direction, wants check     → Arc 4 (Pressure-test)
```

## Arc transitions

You don't have to commit to an arc upfront. Common pattern:

1. Start with Arc 1 (divergent).
2. After synthesis, the user reacts. If they say "interesting, but PM and Skeptic disagreed strongly, can we go deeper?" — you've just moved to Arc 2.
3. After Phase 2, the user says "OK I'm leaning toward [X], pressure-test that." — you've now extended to Arc 3.

The arcs are nested: Arc 3 contains Arc 2 contains Arc 1.

## Anti-arcs (don't)

### Arc -1: Skip Phase 1, jump straight to Phase 3

**What it looks like:** user proposes a decision, orchestrator spawns Phase 3 pressure-test without first running Phase 1 divergent.

**Why it's wrong:** the proposed decision might not be the right framing in the first place. Phase 1 surfaces alternatives; skipping it means pressure-testing a possibly-wrong question.

**Exception:** if the user explicitly says "I'm not exploring; I've decided; just pressure-test this," respect it. They may have already done their own exploration.

### Arc 0: Endless rounds

**What it looks like:** Phase 1 → Phase 2 → Phase 2 again → Phase 3 → Phase 3 again.

**Why it's wrong:** you're not converging; you're collecting indefinitely. Eventually the user has to decide. The swarm's job is to inform decision, not replace it.

**Fix:** after Phase 2, push for a decision. After Phase 3, the brainstorm is over — the user owns the next move.

## Pacing across rounds

Each round should feel substantive. If a round produces the same synthesis as the previous, you've stopped learning.

Signals that a round was wasted (and you should stop, not spawn more):

- Synthesis names the same consensus / dissent / open-questions as the previous round
- Personas restate their previous contributions without new specifics
- The user's reaction is "yeah, I already thought of those"

Signals that another round is worth running:

- Synthesis surfaced a question nobody on the previous round answered
- The user's reaction is "wait, can we dig into [specific thing]?"
- A specific persona's contribution suggests they have more to say if asked deeper

## Time-boxing

For decisions you'd want to make in real-time (during a meeting, during a planning session), aim for:

- Arc 1: 5-10 minutes wall time
- Arc 2: 10-20 minutes wall time
- Arc 3: 20-40 minutes wall time
- Arc 4: 5-10 minutes wall time

If you're heading toward 60+ minutes for a single brainstorm, the topic is too big — decompose first, then spawn per sub-topic.
