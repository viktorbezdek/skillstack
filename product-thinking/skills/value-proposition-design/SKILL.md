---
name: value-proposition-design
description: >-
  Design a product value proposition using the Value Proposition Canvas (jobs,
  pains, gains, pain relievers, gain creators) and the Kano model. Use when the
  user asks to write a value proposition, map pains and gains to product
  features, apply VPC, distinguish basic/performance/delighter features (Kano),
  or articulate why a product matters to a specific customer. NOT for marketing
  copy or microcopy (use ux-writing). NOT for pitching the value prop to
  stakeholders (use storytelling-for-stakeholders). NOT for generic slogans.
---

# Value Proposition Design

A value proposition is not a slogan. It is a structured claim about which user jobs you do better, which pains you relieve, and which gains you create — specific enough that a failure to deliver any of the three invalidates the claim.

## The Value Proposition Canvas (VPC)

Two halves that must map onto each other.

### Customer profile (right side)

| Element | What it is | Example (remote team lead) |
|---|---|---|
| Jobs | What the customer is trying to get done | Run a productive weekly standup across 3 time zones |
| Pains | Obstacles, frustrations, risks | Some people are always tired; attendance is patchy |
| Gains | Wanted outcomes (expected and unexpected) | Everyone feels included; decisions happen in 20 min |

### Value map (left side)

| Element | What it is | Example |
|---|---|---|
| Products & services | What you offer | Async standup tool with threaded updates |
| Pain relievers | How you remove or reduce pains | Timezone-aware scheduling; no live call required |
| Gain creators | How you produce wanted gains | Summary digest with decisions highlighted |

The canvas works only when each pain reliever and gain creator traces to a specific pain or gain on the right side. Orphans — pain relievers that do not match any stated pain — are features built for nobody.

Full VPC walkthrough: `references/vpc-walkthrough.md`.

## Fit

The VPC has three fit levels. A product must clear each in order.

1. **Problem-solution fit** — the value map addresses stated jobs, pains, gains on the right side. Paper exercise. Cheap.
2. **Product-market fit** — real customers in the target segment confirm the value map through behavior (retention, referral, revenue). Expensive to reach.
3. **Business-model fit** — the offer is profitable and scalable. Ultimate validation.

A beautiful VPC without problem-solution evidence is fiction. A product with PMF but no business-model fit is a hobby with customers.

## Kano model — which pains and gains to prioritize

Not all pain relievers and gain creators land equally. The Kano model sorts features into three categories based on customer reaction.

| Category | Customer reaction when present | Customer reaction when absent | Example |
|---|---|---|---|
| **Basic (threshold)** | No pleasure — it's expected. | Churn / abandonment. | Login works. |
| **Performance (linear)** | Satisfaction scales with quality. | Dissatisfaction if weak. | Upload speed. |
| **Delighter (excitement)** | Joy, word of mouth. | No impact — customer didn't expect it. | Auto-summary of the meeting. |

Implications:

- **Underinvesting in basics** — one missing basic wipes out any number of delighters. Delighters must not be built at the cost of basics.
- **Overinvesting in performance** — improving a performance attribute past the "good enough" line produces diminishing returns.
- **Delighter decay** — today's delighter becomes tomorrow's expected performance attribute and next year's basic. The Kano category of a feature is not permanent.

Deep dive: `references/kano-model-deep-dive.md`.

## The value proposition statement

Once the canvas is filled and Kano categories are assigned, compress into a statement.

```
For [specific customer segment]
who [context / trigger / job],
our [product category]
provides [top 1-2 gain creators]
and relieves [top 1-2 pains]
unlike [named alternative],
because [the reason your value map is different].
```

Example:

> For **remote engineering leads** who **run weekly standups across three time zones**, our **async standup tool** provides **a 20-minute decision digest** and relieves **the fatigue of 7am-for-them meetings**, unlike **Zoom calls with rotating schedules**, because **we structure updates to be skim-read, not replayed.**

Rules:

- One segment. If you need two statements, write two.
- Name the alternative. "Unlike other tools" is a non-statement.
- The "because" must state the differentiator, not restate the gain.

## Workflow

1. **Segment first.** Write one VPC per segment. Averaging segments destroys the value map.
2. **Fill the right side from evidence.** Jobs, pains, gains come from interviews and observation — not team speculation.
3. **Fill the left side as hypotheses.** Pain relievers and gain creators are your bets. Mark each as hypothesis until validated.
4. **Trace every left item to a right item.** Orphans are deleted or the right side is updated.
5. **Apply Kano.** Tag each pain reliever / gain creator as basic, performance, or delighter.
6. **Compress into the statement.** One sentence per segment.
7. **Test the statement.** Show it to a member of the segment. Can they restate it in their own words? Do they agree it applies to them?

## Anti-patterns

- **Slogan instead of claim** — "we make work better" is marketing copy, not a value proposition. A value proposition is specific and falsifiable.
- **Segment of one or segment of everyone** — the canvas is either built for a single interviewee or for "small businesses" (too broad to act on).
- **Orphaned pain relievers** — the value map lists features that do not trace to any stated pain or gain.
- **Basics dressed as delighters** — login and search are basics. Calling them delighters hides gaps.
- **Ignoring Kano decay** — a feature that was a delighter two years ago is now a basic; keeping it as a differentiator leaves the product behind.
- **"Unlike X" is missing or vague** — without a named alternative, the claim is undifferentiated.

## References

| File | Contents |
|---|---|
| `references/vpc-walkthrough.md` | Step-by-step VPC for three segments with orphan detection and traceability |
| `references/kano-model-deep-dive.md` | Kano survey method, category reassignment cadence, worked examples |
| `references/value-prop-statement-examples.md` | Good vs bad statements across SaaS, consumer, platform |

## Related skills

- **problem-definition** — the problem must be sharp before the value map can be built.
- **user-needs-identification** — jobs, pains, gains on the right side come from the needs discovery.
- **outcome-oriented-thinking** — the gains are the outcomes the product produces.
- **trade-off-analysis** — decide which pain relievers to build when you cannot build them all.
- **storytelling-for-stakeholders** — translate the value proposition into a pitch.
