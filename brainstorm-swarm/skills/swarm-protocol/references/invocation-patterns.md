# Invocation Patterns

How to choose the right persona subset for a given decision type. Default subsets, edge cases, and when to depart from defaults.

## The default-subset matrix

For each decision type, a default 5-7 persona subset that handles 80% of cases. Adjust based on the specific topic.

### Feature design (typical: 6 personas)

```
PM + Engineer + Designer + Skeptic + User Advocate + Pre-Mortem
```

Why these:
- **PM** — the value/scope/metric framing
- **Engineer** — feasibility and rollout cost
- **Designer** — user flow and friction
- **Skeptic** — pressure-test the assumption that this is worth building
- **User Advocate** — the customer voice
- **Pre-Mortem** — how does this fail in 6 months

Add **Operator** if production-critical. Add **Veteran** if the feature pattern-matches to common past failures (notifications, plugin systems, real-time sync, etc.).

### Architecture decision (typical: 6 personas)

```
Engineer + Operator + Skeptic + Veteran + First-Principles + Constraint-Setter
```

Why these:
- **Engineer** — implementation depth
- **Operator** — production reality
- **Skeptic** — assumption-testing on the architectural claim
- **Veteran** — pattern-matching against past architecture mistakes
- **First-Principles** — "are we solving the right problem?"
- **Constraint-Setter** — what's NOT in scope for this architecture

Add **PM** if the architecture decision has product implications. Drop **Designer** unless the architecture surfaces UX (which is rare).

### Product strategy (typical: 6 personas)

```
PM + User Advocate + Skeptic + Optimist + First-Principles + Pre-Mortem
```

Why these:
- **PM** — the strategic framing
- **User Advocate** — what customers actually want
- **Skeptic** — pressure-test the strategic claim
- **Optimist** — the 10x version (strategy benefits from upside imagination)
- **First-Principles** — strip back inherited strategic frames
- **Pre-Mortem** — how does this strategic bet fail

Drop **Engineer** unless the strategy depends on technical capability the team doesn't have.

### Technical migration (typical: 6 personas)

```
Engineer + Operator + Veteran + Pre-Mortem + Constraint-Setter + Skeptic
```

Why these:
- **Engineer** — implementation
- **Operator** — production safety
- **Veteran** — migrations are pattern-prone (always include)
- **Pre-Mortem** — migrations have known failure modes worth imagining
- **Constraint-Setter** — what's NOT in scope (migrations grow if not constrained)
- **Skeptic** — "do we need to migrate at all?"

Add **First-Principles** if the migration is questionable (might not be needed). Drop **PM** unless the migration has user-facing implications.

### Content / writing (typical: 5 personas)

```
First-Principles + Skeptic + User Advocate + Optimist + Junior
```

Why these:
- **First-Principles** — what's the actual claim being made
- **Skeptic** — what's the strongest counter-argument
- **User Advocate** — who reads this and why
- **Optimist** — what's the most ambitious version of the piece
- **Junior** — what's not yet defined; what assumes too much

Drop the production-side personas (Engineer, Operator, Designer) unless the content is documentation for a technical thing.

### Process / org change (typical: 5 personas)

```
Skeptic + Veteran + User Advocate (= the affected team) + Pre-Mortem + Constraint-Setter
```

Why these:
- **Skeptic** — org changes are change-resistant for reasons
- **Veteran** — process changes pattern-match (RFCs, design reviews, on-call rotations)
- **User Advocate** — the affected team is the "user" here
- **Pre-Mortem** — process changes fail predictably
- **Constraint-Setter** — what's NOT changing (lock the unchanged parts)

Add **First-Principles** if the process is being questioned, not just changed.

### Greenfield exploration (typical: 5 personas)

```
Optimist + First-Principles + User Advocate + Junior + Skeptic
```

Why these:
- **Optimist** — generative, ambitious framing
- **First-Principles** — start from fundamentals, not inherited solutions
- **User Advocate** — who is this even for
- **Junior** — what assumptions are baked into "we should do X"
- **Skeptic** — pressure-test before committing

Don't include **Engineer**/**Operator** until there's a specific implementation to discuss. Don't include **Veteran** — at greenfield, pattern-matching narrows too early.

## Edge cases

### Very small topic — 3-4 personas

For tightly-scoped decisions, don't spawn 6 personas. Pick 3-4. Example for "should this button say 'Save' or 'Submit'?":

```
Designer + User Advocate + Junior
```

That's it. Skeptic, PM, etc. don't add value at this granularity.

### Very large topic — pre-decompose first

If the topic is huge ("redesign onboarding"), don't spawn 12 personas to brainstorm everything. First decompose: "what are the 3-4 sub-decisions inside this?" Then spawn a swarm per sub-decision.

### Politically sensitive topic — add the affected stakeholder

If the topic affects a specific stakeholder group (e.g. "should we deprecate the legacy API used by enterprise customers"), include a persona representing that stakeholder. Use **User Advocate** with explicit framing ("you are the enterprise CTO whose team uses this API").

For HR or org changes, this might mean a custom persona — see the `custom-personas` skill.

### Already-pessimistic room — boost optimism

If the user has already decided this is a bad idea but wants pressure-testing, include **Optimist** alongside **Skeptic** — the room needs the upside view to balance.

If the user is already over-committed and needs help cutting scope, drop **Optimist**, double down on **Constraint-Setter** + **Skeptic**.

### Already-optimistic room — add pessimism

If the user is enthusiastic and wants to go ahead, the swarm's value is in the failure modes. Make sure **Pre-Mortem**, **Skeptic**, and **Operator** are all in.

## When to drop the canonical and use custom

Some domains have personas that aren't in the canonical 12:

- **CFO** — budget brainstorms, ROI analysis
- **Legal/Compliance** — regulatory decisions, contract changes
- **Security Engineer** — threat modeling beyond what Operator covers
- **Customer Success** — for B2B retention decisions
- **Sales** — for pricing/packaging decisions
- **Marketing** — for positioning/launch decisions

When you need these, use the `custom-personas` skill to design them inline. Don't try to force the canonical 12 to cover everything.

## How to present the subset to the user

Before spawning, show the user the proposed subset and let them adjust:

```
For brainstorming "should we add offline mode to the mobile app", I'll spawn:

  - Engineer (feasibility, complexity, sync logic)
  - Designer (UX implications of offline state)
  - User Advocate (do users actually want this?)
  - Pre-Mortem Specialist (failure modes of offline systems)
  - Operator (production complexity of bidirectional sync)
  - Skeptic (assumption-testing the demand)

Spawning 6 personas in parallel. Want to adjust the subset before I do?
```

This lets the user add (e.g. PM) or drop (e.g. Skeptic if they want generative-only).

## How many is too many?

| Subset size | Use for | Risk |
|---|---|---|
| 3 personas | Tight, scoped decisions | Might miss a perspective |
| 4-5 personas | Most narrow brainstorms | Sweet spot for focused decisions |
| 6-7 personas | Standard brainstorm | The canonical default |
| 8-10 personas | Big strategic decisions | Synthesis becomes harder |
| 11-12 personas | Almost never | Too much noise, redundant outputs |

If you're tempted to spawn all 12, reconsider — you probably need 6 in this round and another 6 in a deeper second-round on a sub-decision.

## Second-round patterns

After the first synthesis, sometimes a specific dissent is worth deepening. Spawn just the personas in tension with a more focused prompt:

```
First round: PM said 'ship it default-on'. Skeptic said 'opt-in for safety'.
Second round: spawn JUST PM and Skeptic with the prompt 'PM and Skeptic
disagree on default-on vs opt-in. PM, defend default-on with specifics.
Skeptic, give the strongest opt-in case.'
```

Second rounds are where the swarm gets sharp.
