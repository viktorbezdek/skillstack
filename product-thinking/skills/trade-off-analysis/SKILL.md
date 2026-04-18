---
name: trade-off-analysis
description: >-
  Analyze trade-offs between competing product options using cost-benefit,
  opportunity cost, reversibility (one-way vs two-way doors), and second-order
  effects. Use when the user faces a product choice with non-trivial trade-offs,
  asks "what are we giving up", weighs short-term vs long-term impact, or needs
  to frame a decision before committing. NOT for scored prioritization of a
  backlog (use prioritization). NOT for quantified risk assessment (use
  risk-management). NOT for strategic go/no-go (use strategic-decision).
---

# Trade-Off Analysis

Every product decision kills alternatives. The cost of a choice is not its price — it is the value of the best option you did not take. Teams that do not surface trade-offs build by default and are surprised when the default was wrong.

## When to Use

- Facing a product choice with non-trivial trade-offs
- Asking "what are we giving up" by choosing X over Y
- Weighing short-term vs long-term impact
- Framing a decision before committing resources
- Determining whether a decision is reversible (two-way) or irreversible (one-way)
- Surfacing second-order effects of a decision

## When NOT to Use

- Scored prioritization of a backlog (use prioritization)
- Quantified risk assessment (use risk-management)
- Strategic go/no-go decisions (use strategic-decision)
- Problem framing (use problem-definition — do that first)

## Decision Tree

```
What trade-off problem do you have?
│
├─ "Should we do X?" — only one option framed
│  └─ One option is rationalization, not decision-making → Add alternatives + "do nothing"
│
├─ Multiple options, need to compare
│  ├─ 2-4 options? → Fill the trade-off matrix
│  └─ More than 4? → Prune to the top 3-4; adding more dilutes analysis
│
├─ How reversible is this?
│  ├─ Easy to undo, wrong choice costs days? → Two-way door; decide fast, test
│  ├─ Hard/impossible to undo, wrong choice costs months? → One-way door; decide slow, gather evidence
│  └─ Not sure? → Treat as one-way until proven otherwise
│
├─ Short-term vs long-term tension
│  ├─ Short-term win + long-term win? → Obvious choice; do it
│  ├─ Short-term cost + long-term win? → Strategic bet; do if reversible or high confidence
│  ├─ Short-term win + long-term cost? → Debt; only if win is large and you have a paydown plan
│  └─ Short-term cost + long-term cost? → Avoid
│
└─ Not sure what you're giving up
   └─ You haven't named the opportunity cost → Name the next-best alternative explicitly
```

## The four dimensions of a trade-off

Every non-trivial decision has trade-offs on these four axes. Analyzing only one is the most common failure mode.

### 1. Cost vs benefit

What does it cost (money, time, attention, complexity)? What benefit does it produce (outcome magnitude, confidence, timing)? The trap is treating cost as engineering time only and ignoring ongoing maintenance, cognitive load, and attention cost.

### 2. Opportunity cost

If we do A, we cannot do B. What is the value of B? A decision looks cheap when viewed alone and expensive when the foregone alternative is named.

Rule: **never evaluate an option in isolation — always name the next-best alternative and compare.**

### 3. Reversibility (one-way vs two-way doors)

Borrowed from Bezos. Decisions are not equal in reversibility.

| Type | Characteristics | How to decide |
|---|---|---|
| **Two-way door** | Easy to reverse. Wrong choice costs days, not months. | Decide fast, test, learn. |
| **One-way door** | Hard or impossible to reverse. Wrong choice costs months or quarters. | Decide slow, gather evidence, build consensus. |

Two-way door examples: UI copy, a feature flag rollout, a pricing experiment on 5% of users. One-way door examples: changing the pricing model globally, deprecating an API with external consumers, renaming a product.

The anti-pattern: treating one-way doors with the same speed as two-way doors. This is how teams ship decisions they cannot walk back.

Deep dive: `references/reversibility-framework.md`.

### 4. Second-order effects

First-order: what the decision does directly. Second-order: what the first-order effect causes downstream.

| First-order | Second-order |
|---|---|
| Add a rate limit to free tier. | Power users churn to a competitor who does not rate-limit. |
| Delete a rarely-used feature. | The small cohort who used it were your highest-NPS customers. |
| Launch a simpler onboarding. | Onboarding completes faster but usage patterns worsen because depth-of-use decreased. |

Teams optimize first-order effects and are surprised by second-order ones. For important bets, name at least two second-order effects for each option before deciding.

See `references/second-order-thinking.md` for elicitation techniques.

## The trade-off matrix

For any decision with 2-4 options, build the matrix.

```
             | Option A | Option B | Option C | Do nothing
-------------+----------+----------+----------+-----------
Direct cost  |          |          |          |
Opp. cost    |          |          |          |
Benefit      |          |          |          |
Timeline     |          |          |          |
Reversibility|  2-way   |  1-way   |  2-way   |  2-way
Confidence   |          |          |          |
2nd-order    |          |          |          |
Kills        |          |          |          |
```

Rules for the matrix:

1. **"Do nothing" is always an option.** Adding it forces the team to justify action, not default to it.
2. **Confidence is explicit.** "Low / medium / high" for the benefit estimate. Low confidence on a one-way door is a stop sign.
3. **"Kills" names what else is blocked by choosing this option.** Makes opportunity cost concrete.
4. **Fill with specifics, not adjectives.** "$80k / 3 months / 70% chance" is useful; "medium / short / likely" is not.

## Short-term vs long-term

Two trade-off dimensions travel together. Plot the option on both axes.

|   | Short-term win | Short-term cost |
|---|---|---|
| **Long-term win** | Obvious choice. Do it. | Strategic bet. Do it if reversible or confidence is high. |
| **Long-term cost** | Debt. Do it only if short-term win is large and explicitly pay down later. | Avoid. |

The dangerous quadrant is top-left-spelled-as-bottom-left — decisions that look like a short-term win but are actually debt because the long-term cost is invisible in the moment.

## Decision workflow

1. **State the decision as a question.** "Should we do X?" is incomplete — decisions are choices between options.
2. **List options including "do nothing" and "do a smaller version".** Minimum three options.
3. **Classify reversibility.** One-way or two-way per option.
4. **Fill the matrix.** Specific numbers, explicit confidence, named kills, named second-order effects.
5. **Sanity-check short-term vs long-term.**
6. **Name the decision.** Choose, document who chose, document the kill condition (what would make us reverse).
7. **Schedule the review.** Especially for one-way doors — what evidence would change our mind, and when do we look?

## Heuristics

- **If reversibility is high, bias toward speed.** Testing is cheaper than debating.
- **If reversibility is low, bias toward evidence.** Build consensus and lower confidence intervals before committing.
- **If the best alternative is close to the chosen option, be suspicious.** When two options are equally good, the decision often does not matter as much as you think — or you have not surfaced a real differentiator.
- **If no one can articulate the opportunity cost, stop.** The team is deciding without knowing what they are giving up.
- **If second-order effects are all positive, you are not thinking hard enough.** Every non-trivial decision produces at least one negative downstream effect.

## Anti-patterns

| Anti-Pattern | Problem | Solution |
|---|---|---|
| One option, no alternatives | "Should we do X?" with no comparison set = rationalization, not decision-making | Always include "do nothing" and "do a smaller version" as options |
| Sunk-cost anchoring | "We already started X so we should continue" is a cognitive trap, not a trade-off | Evaluate from a blank slate: "If we hadn't started, would we begin now?" |
| First-order-only | Optimizing direct metric and ignoring downstream effects on retention, support, morale | Name at least two second-order effects per option before deciding |
| Reversibility ignored | One-way doors decided fast; two-way doors debated endlessly | Classify reversibility first; invert the speed bias |
| Confidence theater | "High confidence" without stating what the confidence is based on | State the evidence behind confidence; low evidence + one-way door = stop |
| Opportunity cost left implicit | Debating option cost without naming the foregone alternative | Always name the next-best alternative explicitly |
| No kill clause | No condition would reverse the decision; it cannot be wrong and cannot be learned from | Document what evidence would change your mind; schedule a review |

## References

| File | Contents |
|---|---|
| `references/reversibility-framework.md` | One-way vs two-way doors with worked examples, edge cases |
| `references/second-order-thinking.md` | Techniques to surface downstream effects — pre-mortem, behavior mapping, stakeholder pulse |
| `references/trade-off-matrix-examples.md` | Filled matrices for B2B SaaS, consumer, platform, internal tools |

## Related skills

- **problem-definition** — the trade-off is between solutions to a defined problem; without a problem, trade-off analysis has no objective.
- **outcome-oriented-thinking** — the benefits in the matrix are outcomes, not outputs.
- **prioritization** — once options are analyzed, rank them with RICE/MoSCoW/ICE.
- **risk-management** — quantify the probabilities behind second-order effects.
- **strategic-decision** — for high-stakes strategic bets, run the full strategic-decision workflow.
- **systems-thinking** — surfacing second-order effects benefits from systems-thinking tools (CLD, feedback loops).
