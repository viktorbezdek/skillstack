# Depth vs Breadth

The fundamental tradeoff in interview design. Every brainstorm makes this choice — usually implicitly. This skill makes it explicit.

## The two extremes

### Pure breadth

12 personas, one round each, single message. Maximum perspective coverage, minimum depth per perspective.

**Trade:** comprehensive overview, but each persona contributes 400 words of necessarily-shallow take.

**When it works:** the user genuinely doesn't know what they don't know. Phase 1 of Arc 1 is pure breadth.

**When it fails:** the user wanted answers, not perspectives. Or specific tensions need pursuit but the breadth-only arc doesn't pursue them.

### Pure depth

2 personas, 4-5 rounds back and forth on a specific question. Maximum depth on one issue, minimum perspective coverage.

**Trade:** thorough resolution of one tension, but blind to perspectives outside those 2 personas.

**When it works:** the question is narrow and the right 2 personas are obvious. Phase 2 of Arc 2 is pure depth.

**When it fails:** the question turns out to depend on a perspective from a persona who wasn't in the room.

## The sweet-spot pattern

For most decisions, the sweet spot is:

```
Phase 1 — moderate breadth (5-7 personas, 1 round)
Phase 2 — focused depth (2-3 personas, 1 round on specific tension)
Phase 3 — narrow breadth (3-4 personas, 1 round on specific decision)
```

This is Arc 3 (full arc). It balances breadth (Phase 1's diverse opening) with depth (Phase 2's pursuit of specific tension) with convergence (Phase 3's pressure-test on a tentative direction).

## How to choose

### Choose breadth when:

- The decision is early-stage and you don't yet know which tensions matter
- The team has shared assumptions worth surfacing from many angles
- The user wants to "get unstuck" — generative work
- You're doing greenfield exploration

### Choose depth when:

- A specific disagreement has emerged that won't resolve with more perspectives
- The question is technical and the depth comes from one or two domains
- The user has narrowed and wants to pursue one path thoroughly
- You're pressure-testing a tentative direction

### Choose breadth-then-depth when:

- The decision is non-trivial AND has the time/budget for a multi-round arc
- The user values defensibility ("I want to be able to say I considered every angle")
- You suspect Phase 1 will surface a specific tension worth deepening

## Topic shape predicts depth-vs-breadth

| Topic shape | Default |
|---|---|
| Open exploration ("what should we do about X") | Breadth — Arc 1 or full Arc 3 |
| Specific decision ("should we ship X default-on or opt-in") | Depth — Arc 4 (pressure-test) |
| Technical evaluation ("Postgres vs MySQL for this workload") | Depth on tech — 2-3 technical personas, deep |
| Strategic question ("should we enter market X") | Breadth then depth — Arc 3 |
| Specific dispute ("PM and Eng disagree on scope, help us think") | Pure depth — Arc 2 |

## Don't decide once — iterate

You don't have to commit to depth or breadth at the start. Standard pattern:

1. Start with moderate breadth (Phase 1, 6 personas).
2. Synthesize, present.
3. Let the user's reaction tell you whether to go broader (more personas, second round of Phase 1) or deeper (Phase 2 on specific tension).

The user usually surfaces the right next move themselves.

## Per-decision-size guidance

| Decision size | Breadth | Depth |
|---|---|---|
| Trivial (button label) | 3-4 personas, one round | None — don't deepen |
| Small (single feature scope) | 4-5 personas, one round | Optional Phase 2 on one tension |
| Medium (architecture choice) | 5-7 personas, full arc | Phase 2 on specific tech tension |
| Large (product strategy) | 6-8 personas, full arc + decomposition | Multiple Phase 2s on sub-tensions |
| Very large (org redesign) | DECOMPOSE FIRST, then per-sub-decision | Per-sub-decision arcs |

## The depth trap

A common failure mode: pursuing depth on one tension forever, never returning to breadth.

Symptoms:
- You're 3 rounds deep on the same disagreement
- The same 2 personas keep saying the same thing in different words
- The user is getting impatient

What's happening: you've reached the limit of what the swarm can resolve. The question now needs evidence (data, user research, prototype) — not more perspective.

What to do: stop, summarize, name what evidence would resolve it, hand back to the user.

## The breadth trap

The opposite failure: spawning more and more personas to "be thorough."

Symptoms:
- You spawned all 12 canonical + 4 custom personas
- Synthesis has 16 contributions and is itself overwhelming
- The user still doesn't know what to decide

What's happening: breadth without depth doesn't produce decisions. More perspectives → more dimensions → harder synthesis.

What to do: stop spawning. Synthesize what you have. Then go deep on the top 1-2 tensions, not broader.

## The synthesis-load constraint

A practical limit: how much can the synthesis skill produce that a human can absorb?

| # of contributions | Synthesis quality |
|---|---|
| 4-5 | Excellent — clean consensus/dissent identification |
| 6-7 | Good — readable synthesis, clear groupings |
| 8-10 | Marginal — synthesis becomes summary, dissent loses crispness |
| 11+ | Poor — synthesis becomes either too long or too compressed; user can't act on it |

If you're spawning 11+ personas, decompose the topic first. Run multiple separate swarms on sub-topics.

## The 80/20 of arcs

For 80% of brainstorms, the right arc is:
- **Arc 1** (divergent only) for quick exploration
- **Arc 4** (pressure-test) for tentative-decision review

The remaining 20%:
- **Arc 2** when Phase 1 surfaces a specific worth-pursuing tension
- **Arc 3** when the decision is high-stakes and worth the full pass

Don't default to Arc 3. Most decisions don't need the full 30-50k tokens.
