---
name: outcome-oriented-thinking
description: >-
  Apply outcome-over-output product thinking — separating what gets built from
  what actually changes for the user, running the "so what" test to climb from
  output to outcome to impact, choosing leading vs lagging metrics, and
  identifying a North Star metric. Use when the user asks whether something is
  an outcome or an output in a product context, wants to run the "so what"
  test on a deliverable, wants a North Star metric, needs to choose leading
  indicators for a product bet, or is debating whether shipping a feature
  equals success. NOT for generic OKR authoring (use outcome-orientation). NOT
  for feedback-loop analysis (use systems-thinking). NOT for metric scoring or
  ranking (use prioritization).
---

# Outcome-Oriented Thinking

Shipping a feature is not an outcome. Outputs are what your team produces. Outcomes are what changes for the user as a result. A product org can have a 95% delivery rate on its roadmap and a 0% outcome rate on its strategy.

This skill is the product-strategy lens on outcomes — specifically: North Star selection, outcome hypotheses, and the output/outcome/impact chain applied to product bets. For generic OKR authoring (team-level objectives and key results), use `outcome-orientation`.

## The output-outcome-impact chain

| Layer | Question it answers | Example |
|---|---|---|
| Activity | What are we doing? | Designing the new signup flow |
| Output | What did we produce? | Signup flow shipped to 100% of users |
| Outcome | What changed for the user? | Activation rate rose from 32% to 48% |
| Impact | What changed for the business? | Monthly recurring revenue rose 9% |

Teams are measured and rewarded on outputs. Customers experience outcomes. Executives read impact. Skipping any layer breaks the chain — you ship things that do not activate users, or activate users on metrics that do not move revenue.

## The "so what" test

For every proposed deliverable, ask "so what?" three times. The answer must reach an outcome and then an impact.

> We will ship the new signup flow. **So what?** Activation will rise. **So what?** More users will reach value in week one. **So what?** Retention will improve and CAC payback will shorten.

If any "so what" returns a synonym or a restatement of the output, the chain is broken. The team is building without a theory of how the work changes anything.

## North Star metric

The North Star is a single metric that captures the value customers get from the product. It is not revenue (that's impact) and it is not a feature count (that's output). It lives at the outcome layer.

### Criteria for a North Star

1. **Aligned to customer value** — when the metric rises, customers got more value.
2. **Actionable** — the team can move it through their work.
3. **Predictive of long-term business health** — it leads revenue, it doesn't lag it.
4. **Measurable with low effort** — the team can read it weekly without heroics.
5. **Understandable** — a new engineer can explain it on day one.

### Examples

| Company type | Possible North Star |
|---|---|
| Messaging app | Messages sent per weekly active user |
| Marketplace | Successful transactions per month |
| Devtool | Weekly active repos with ≥3 commits |
| Content platform | Minutes of content consumed per active user |

### Anti-North-Stars

- **Vanity metrics** — signups, page views. They rise without value being delivered.
- **Revenue as North Star** — lagging, not predictive of what caused it.
- **Composite scores** — "Engagement Score = 0.3 * A + 0.2 * B + ..." is unreadable and un-falsifiable.

See `references/north-star-selection.md` for selection methodology.

## Leading vs lagging indicators

| Kind | Signal speed | Example |
|---|---|---|
| Lagging | Slow — the outcome after it happens | Quarterly retention, NPS |
| Leading | Fast — predicts the lagging indicator | Weekly active repos, first-session completion |

The rule: **every product bet needs one leading indicator**. Without one, you wait until the lagging indicator moves to find out whether the bet worked — by then, the quarter is over.

Leading-indicator design:

1. State the outcome you expect (lagging).
2. Hypothesize the user behavior that causes it.
3. Measure the behavior directly and early.

Example: expected outcome is "quarterly retention rises 5%". Hypothesis is "first-session completion predicts retention". Leading indicator is "% of new users completing first session in week 1" — readable after 7 days, not 90.

Deep dive: `references/leading-indicators-design.md`.

## Outcome hypotheses — the unit of a product bet

A product bet is a falsifiable hypothesis, not a roadmap item.

```
HYPOTHESIS

We believe that [building X]
will cause [user behavior change]
for [segment]
which will produce [outcome — leading indicator]
and ultimately [impact — lagging indicator].

We will know we are right when [leading indicator threshold] within [timeframe].
We will kill this bet if [falsification condition].
```

Example:

> We believe that **adding a one-click sandbox** will cause **new users to try the product in their first 10 minutes** for **developer leads evaluating tools**, which will produce **first-session completion ≥ 40%** and ultimately **quarterly activation ≥ 25%**. We will know we are right when **first-session completion reaches 40% within 4 weeks of launch**. We will kill this bet if **it stays below 20% after 4 weeks**.

The `kill` clause is the most-skipped line and the most valuable. Without it, a failing bet survives because no one defined failure.

## Workflow

1. **Write the chain.** Activity → Output → Outcome → Impact for the proposed work.
2. **Run "so what" three times.** Stop if any link breaks.
3. **Name the North Star.** The outcome that matters most across bets.
4. **Set leading and lagging indicators.** At least one of each per bet.
5. **Write the hypothesis.** Include the kill clause.
6. **Schedule the review.** When and how will you read the leading indicator?

## Anti-patterns

- **Roadmap-as-strategy** — a list of outputs with no outcome hypothesis. Tells you what is being built but not why.
- **Output-masquerading-as-outcome** — "we shipped the feature to 100% of users" counted as an outcome. Shipping is not change.
- **Lagging-only metrics** — retention and revenue are the only measures tracked. You find out the bet failed three months after you could have acted.
- **No kill clause** — bets never die. Teams keep shipping against a failing hypothesis because nobody defined failure.
- **Moving the North Star** — the metric changes every quarter to flatter the roadmap. A North Star that shifts is not a North Star.
- **One metric, one team** — every team picks its own North Star and optimizes against it, pulling the product in five directions.

## References

| File | Contents |
|---|---|
| `references/north-star-selection.md` | Criteria, worked examples, common mistakes, when to revisit |
| `references/leading-indicators-design.md` | Behavior-to-indicator translation, cadence, pitfalls |
| `references/outcome-hypothesis-templates.md` | Hypothesis templates with kill clauses for B2B, consumer, platform |

## Related skills

- **outcome-orientation** — team-level OKR authoring with KR structure.
- **problem-definition** — frame the problem before writing the hypothesis.
- **user-needs-identification** — identify the user behavior the hypothesis targets.
- **value-proposition-design** — the gains on the VPC are candidate outcomes.
- **trade-off-analysis** — decide which outcome to pursue when you cannot pursue all.
- **systems-thinking** — understand feedback loops connecting outputs to outcomes.
