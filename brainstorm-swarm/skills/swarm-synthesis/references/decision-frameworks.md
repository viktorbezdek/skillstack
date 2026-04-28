# Decision Frameworks

How to recommend a next move based on what the brainstorm produced. The synthesizer's only editorial contribution.

## The recommended-next-move patterns

The synthesis ends with a recommendation. The recommendation depends on the brainstorm's shape.

### Pattern 1: clear consensus → ship

When the swarm strongly converged on a direction:

```markdown
### Recommended next move
Direction is clear from the swarm: [X].

Next move: [smallest valuable version of X], shipped to [audience], measured by [metric].

Alternative if rejected: [the runner-up direction the swarm considered].
```

**When to use:** 4+ personas explicitly endorsed the same direction; dissent is minor.

### Pattern 2: dissent on empirical question → research first

When personas disagreed and the disagreement hinges on missing data:

```markdown
### Recommended next move
The swarm's core disagreement is empirical: [the substantive question].

Next move: gather [specific evidence] before deciding.
- [Data source 1] — gives us [insight A]
- [Data source 2] — gives us [insight B]

Re-run the brainstorm once evidence is in. Estimated effort: [X hours/days].
```

**When to use:** dissent traces to a "we don't know yet" question that's answerable with research.

### Pattern 3: many open questions → pause, scope down

When the brainstorm exposed that the team isn't ready:

```markdown
### Recommended next move
We're not ready to decide. The swarm exposed [N] open questions, the most
load-bearing being [the critical question].

Next move: tighten the scope of what we're trying to decide. The full topic
([original topic]) is too broad. Suggest decomposing into:
- Sub-decision A: [specific narrow question]
- Sub-decision B: [specific narrow question]

Run a brainstorm-swarm on Sub-decision A first. Once resolved, re-frame B with new context.
```

**When to use:** 3+ open questions emerged; the original topic was too broad.

### Pattern 4: consensus on constraint, dissent on path → prototype

When personas agreed on what the constraint is but disagreed on which path satisfies it:

```markdown
### Recommended next move
Consensus: [the constraint] is the binding limit.

Dissent: paths [A] and [B] both satisfy it; the swarm split on which is right.

Next move: prototype both A and B for [time-box, e.g. 1 week]. Decide based
on what the prototypes teach us, not based on more brainstorming.

Specifically:
- Prototype A: [smallest test of A's main claim]
- Prototype B: [smallest test of B's main claim]
- Decision criterion: [the metric or observation that picks the winner]
```

**When to use:** the disagreement is path-related and prototyping is feasible.

### Pattern 5: skeptic + pre-mortem heavy → mitigate or kill

When the brainstorm surfaced critical risk:

```markdown
### Recommended next move
Pre-Mortem and Skeptic surfaced critical risk: [the risk].

Recommendation: do NOT proceed without first [mitigation].

If mitigation is feasible, re-run a tighter brainstorm focused on the mitigated
proposal. If mitigation is infeasible, kill the proposal — the risk dominates
the value.

Specifically:
- Proposed mitigation: [action]
- If mitigation works → [next step]
- If mitigation doesn't work → [alternative proposal or kill]
```

**When to use:** a load-bearing risk emerged that the proposal-as-stated doesn't address.

### Pattern 6: optimist outsized → consider the bigger ambition

When the brainstorm exposed under-imagining:

```markdown
### Recommended next move
The Optimist surfaced a 10x version of this proposal: [the bigger ambition].

The swarm-as-a-whole is split on whether this is in scope. Recommend one of:

(a) Stay with original scope ([proposal]). Ship as planned. Re-evaluate the
    bigger ambition after launch with real usage data.

(b) Re-frame to the 10x version ([bigger ambition]). Brainstorm again with the
    bigger frame. Likely 2-3x the engineering cost; potentially the next major
    product moment.

The decision hinges on: [the strategic question — appetite for ambitious bets,
team capacity, opportunity cost].
```

**When to use:** the brainstorm exposed that the proposal might be too small.

### Pattern 7: constraint-setter heavy → cut scope

When multiple personas (especially Constraint-Setter) flagged scope creep:

```markdown
### Recommended next move
Scope is the dominant concern: 4 personas (Constraint-Setter, Skeptic,
Pre-Mortem, Engineer) raised scope risk.

Recommended cuts:
- [Specific cut from Constraint-Setter] — saves [estimated time]
- [Specific cut] — saves [estimated time]

Recommended NEW scope: [proposal-with-cuts-applied].

Validate the new scope by running a tight Phase 3 pressure-test on the cut version.
```

**When to use:** scope discipline is the headline; cuts are clear.

## Decision-fitness checks

Before finalizing the recommended next move, sanity-check it against the brainstorm:

- [ ] Does the recommendation address the dissent (not paper over it)?
- [ ] Does the recommendation address the open questions (not ignore them)?
- [ ] Is the recommended action specific enough to execute (not "more research" — what specific research)?
- [ ] Is the alternative named (so the user can override without starting over)?
- [ ] Is the recommendation honest about confidence (don't claim consensus where there was dissent)?

## When NOT to recommend

Sometimes the right answer is "the user should decide; the swarm gave you the inputs":

```markdown
### What the swarm gave you
The swarm produced clear inputs but the decision is yours:
- The case FOR: [synthesized from optimist, PM, user advocate]
- The case AGAINST: [synthesized from skeptic, pre-mortem, engineer]
- The deciding factor: [the strategic question only you can answer]

I won't recommend a direction here — the decision depends on [factor only the
user knows].
```

**When to use:** the decision genuinely depends on values, appetite, or context only the user has. Better to be honest than to fake-recommend.

## The "what would change my recommendation" question

Add a one-line falsifying condition to the recommendation:

```markdown
### Recommended next move
Direction: [X].

This recommendation would change if: [specific evidence — "if user research
shows the cellular cohort is < 5% of revenue, drop the proposal entirely"].
```

Names the decision-shifting evidence. Useful for the user when more data later arrives.

## Recommendation length

The recommended-next-move section is 100-300 words. Not more — too long means it's not actionable. Not less — too short means it's not specific.

## Anti-patterns

### "More research is needed" without specifics

Vague. Doesn't help. Always name the specific research, the data source, the estimated effort.

### "Personas disagreed; the user should decide"

Punts. Even when you can't recommend a direction, you can frame the decision sharply (Pattern: When NOT to recommend).

### "It depends on..."

If you find yourself starting with "it depends," finish the sentence: WHAT does it depend on, and what would resolve that dependency?

### Hidden recommendation

Burying the recommendation 8 paragraphs deep. The recommendation should be in the synthesis's last 200 words, clearly labeled.

### Pretending consensus

Recommending a direction as if the swarm was unanimous when it was split. Acknowledge the dissent in the recommendation: "Despite Skeptic's concerns about X, the swarm's consensus on Y suggests..."
