---
name: interview-facilitation
description: >-
  Structure the interview arc when a brainstorm-swarm interviews the user.
  Covers the divergent-then-convergent arc (open with breadth, close with
  depth), question design (open vs probing, leading vs neutral, what-vs-why-
  vs-how), depth-vs-breadth tradeoffs, and when to send a second round of
  follow-up questions to specific personas. Use when running a brainstorm
  swarm and the swarm-protocol skill has spawned the persona subagents — this
  skill teaches how those personas interact with the user during the
  interview phase. NOT for the persona swarm orchestration itself (use
  swarm-protocol). NOT for synthesizing the swarm output (use swarm-synthesis).
  NOT for designing custom personas (use custom-personas). NOT for one-on-one
  Socratic interviews (use deep-interview from skillstack).
---

# Interview Facilitation

> A swarm interview is choreography, not free-for-all. Without structure, six personas talking at once is six monologues. With structure, it's a roundtable.

This skill covers the *interview arc* — how the swarm's questions are sequenced, how depth and breadth trade off, and how the user is given enough air to think between rounds.

## Core principle

**Diverge first, converge last.** The first round of questions should open the topic from many angles (each persona surfacing different concerns). The closing round should narrow to specific decisions. In between, the orchestrator decides whether one or two areas need deeper probing.

## The three-phase arc

A well-facilitated swarm interview has three phases:

### Phase 1 — Divergent opening (one swarm round)

All personas spawn in parallel. Each surfaces their core questions, concerns, and observations. The user receives a synthesis covering breadth across all spawned personas.

This is the only round many brainstorms need. For a focused decision, opening + synthesis is sometimes enough.

### Phase 2 — Targeted probing (optional second round)

If synthesis surfaced 1-2 areas of significant disagreement or critical open questions, spawn a focused second round with just the personas in tension on those specific issues.

Examples:
- "Round 1 PM said 'ship default-on'; Skeptic said 'opt-in is safer'. Round 2: spawn just PM and Skeptic to argue this specific point."
- "Round 1 Pre-Mortem named a critical failure mode; Operator confirmed. Round 2: spawn Engineer + Operator to work through mitigation."

### Phase 3 — Convergent closing (one swarm round, narrow scope)

If the brainstorm produced a tentative direction, spawn a tight closing round to pressure-test the proposed decision. Usually 3-4 personas: Skeptic + relevant domain experts.

Closing prompt format: "Given that we're leaning toward [decision], each of you: name the strongest case AGAINST this and the strongest case FOR. One paragraph each."

## Question design

The orchestrator constructs the prompts each persona receives. Question design matters even though the persona subagents have their own voice.

### Open vs probing

| Type | When to use | Example |
|---|---|---|
| **Open** | Phase 1 — divergent opening | "What's your perspective on adding offline mode?" |
| **Probing** | Phase 2 — targeted probing | "Skeptic, you said 'we're inventing demand.' Specifically — name 3 user requests in your imagined evidence base that would convince you the demand is real." |
| **Closing** | Phase 3 — convergent closing | "Given the direction is opt-in offline mode for paid users only, name the strongest argument against." |

### Leading vs neutral

⛔ **Avoid leading questions in Phase 1.** They constrain the persona's contribution.

| Leading (avoid in Phase 1) | Neutral (preferred) |
|---|---|
| "Why is offline mode important?" | "What's your perspective on offline mode?" |
| "How should we ship this default-on?" | "How should we approach the rollout?" |
| "What are the risks of NOT doing this?" | "What are the relevant risks?" |

In Phase 2 and 3, leading questions become useful — they probe specific areas.

### What / Why / How balance

A good prompt covers:

- **What** — what is the proposal, what's the scope
- **Why** — why this, why now
- **How** — how does it ship, how does it operate

A prompt that asks only "How should we do X?" misses the "should we" question. A prompt that asks only "Why X?" misses the implementation reality.

The persona's structured output formats handle the balance — but the orchestrator's framing should leave space for all three.

## Depth vs breadth

The fundamental tradeoff in interview design:

| Approach | Pros | Cons |
|---|---|---|
| **Breadth** (many personas, one round) | Surfaces diverse perspectives quickly | Each contribution is shallow |
| **Depth** (few personas, multiple rounds) | Pursues specific tensions | Misses perspectives not in the few |

The standard arc balances them: Phase 1 is breadth (6 personas, one round), Phase 2 is depth (2-3 personas, focused probing), Phase 3 is breadth-on-narrow-decision.

### When to favor breadth

- The decision is early-stage; many perspectives haven't been considered
- The team has shared assumptions worth challenging from multiple angles
- The user explicitly wants "fresh angles I haven't thought of"

### When to favor depth

- A specific disagreement has emerged that's worth pursuing
- The user has a tentative direction and wants pressure-testing
- The decision is technical and the depth comes from one or two domains

See `references/interview-arcs.md` for the full library of arc patterns.

## Air for the user between rounds

Don't auto-spawn the next round. Between Phase 1 and Phase 2, present the synthesis to the user and ask:

- "These are the perspectives. Anything you want to dig into?"
- "I noticed dissent on [specific topic]. Want me to spawn a deeper round on just that?"
- "Or do you have enough to make a decision?"

The user might be ready to decide after Phase 1. Don't keep spawning if they're done.

## Question patterns by phase

### Phase 1 prompts (open, neutral)

Standard topic + context template. Personas know what to do.

```
Topic: [one-sentence framing]

Context:
- [Background]
- [Constraints]
- [Specific question being decided]

Your job: Contribute your perspective in your characteristic voice.
```

### Phase 2 prompts (probing, often persona-specific)

Tighter, calls out the specific tension.

```
Specific tension from Round 1:
- [Persona A] said [position]
- [Persona B] said [opposing position]

Your job (you are [Persona A or B]):
- Defend your position with specifics
- Name the conditions under which the other side would be right
- Identify the evidence that would settle this disagreement
```

### Phase 3 prompts (convergent, narrow)

Fixed format around the proposed decision.

```
We're leaning toward [decision].

Your job:
- Strongest argument FOR (one paragraph)
- Strongest argument AGAINST (one paragraph)
- The decisive consideration in your view (one sentence)
```

See `references/question-design.md` for detailed prompt patterns and worked examples.

## ✅ Use for

- Structuring the arc of a swarm brainstorm (divergent → probing → convergent)
- Designing the prompts each persona receives in each phase
- Deciding when to do a second round vs stop after Phase 1
- Balancing depth and breadth for the topic
- Giving the user air between rounds

## ❌ NOT for

- The persona swarm orchestration itself — use `swarm-protocol`
- Synthesizing the swarm's output — use `swarm-synthesis`
- Designing custom personas — use `custom-personas`
- One-on-one Socratic interview — use `deep-interview` (skillstack)
- Psychological elicitation techniques — use `elicitation` (skillstack)

## Anti-patterns

### The endless swarm

**What it looks like:** spawning round after round, going from 6 personas to 12 to 18 in pursuit of "completeness."

**Why it's wrong:** synthesis becomes harder; the user can't act on infinite input.

**What to do instead:** most decisions are well-served by 1-2 rounds. Push for a decision after the second round. If the user genuinely needs more, you have a decomposable topic — split it.

### Auto-spawn without checking in

**What it looks like:** Phase 1 ends, orchestrator immediately spawns Phase 2.

**Why it's wrong:** the user might have wanted to think, or might be ready to decide. Burning compute on rounds the user doesn't need.

**What to do instead:** present synthesis after each phase, ask whether to continue.

### Leading questions in Phase 1

**What it looks like:** asking "Skeptic, what could go wrong with this great proposal?"

**Why it's wrong:** baked-in framing ("great proposal") biases the persona; defeats the point of the skeptic.

**What to do instead:** "Skeptic, your perspective on this proposal." Let the persona apply their voice without orchestrator framing.

### Forced consensus in Phase 3

**What it looks like:** Phase 3 prompt that pressures personas to converge ("everyone, agree on the right answer").

**Why it's wrong:** the swarm's value is preserved dissent. Forcing consensus loses the disagreement.

**What to do instead:** Phase 3 prompts ask each persona to identify the "decisive consideration in their view," not to align with others.

### Prompt bloat

**What it looks like:** every persona's prompt includes 1500 words of context, prior synthesis, history.

**Why it's wrong:** personas are fresh subagents; bloat dilutes the prompt; they can't synthesize from a wall of text.

**What to do instead:** keep persona prompts to 100-300 words of context. The persona's own contribution-shape handles the rest.

## Workflow

The standard arc:

1. **Frame topic** (orchestrator + user). One sentence.
2. **Pick persona subset** (orchestrator, user signs off).
3. **Phase 1 — divergent opening** (single message, all Task() calls).
4. **Collect Phase 1 returns.**
5. **Hand off to swarm-synthesis** for Phase 1 synthesis.
6. **Present synthesis to user.** Ask: continue, deepen, or stop?
7. **If deepening — Phase 2 targeted probing.** 2-3 personas on the specific tension.
8. **Collect Phase 2 returns. Synthesize.**
9. **If user has tentative direction — Phase 3 convergent closing.** 3-4 personas pressure-test.
10. **Final synthesis. Decision support output.**

## References

| File | Contents |
|---|---|
| `references/interview-arcs.md` | The 4 standard arcs (divergent-only, probing, full-arc, decision-pressure-test); when each works |
| `references/question-design.md` | Prompt patterns for each phase; worked examples; leading-vs-neutral library |
| `references/depth-vs-breadth.md` | When to favor each; how the topic shapes the choice |

## Related skills

- **swarm-protocol** — the orchestration mechanics; this skill is the structural complement
- **swarm-synthesis** — what to do with the collected outputs after each phase
- **custom-personas** — when the canonical 12 don't cover a niche perspective
- **deep-interview** (skillstack) — single-agent Socratic alternative
- **elicitation** (skillstack) — psychological elicitation for deep one-on-one work
