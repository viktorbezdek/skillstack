# Trade-off Matrix — Worked Examples

Each example shows the matrix applied to a real-shape decision: named options including "do nothing," specific costs, named second-order effects, and an explicit kill clause on the chosen option.

## Example 1 — Rate limit on free tier (B2B SaaS)

**Decision context**: The team proposes adding a hard rate limit to the free tier (1000 API calls/day) to drive conversions. Growth is stalling and revenue forecasts require an action.

**Options**:
- A: Hard rate limit at 1000 calls/day with upgrade prompt.
- B: Soft rate limit with gradual slowdown above 1000 calls/day.
- C: Usage-tracking only with dashboard visibility, no limits.
- D: Do nothing — leave free tier unchanged.

### Matrix

|   | A: Hard limit | B: Soft limit | C: Visibility only | D: Do nothing |
|---|---|---|---|---|
| Direct cost | 1 eng-week | 2 eng-weeks | 1 eng-week | 0 |
| Opp. cost | blocks growth bet | blocks growth bet | blocks growth bet | misses conversion lift opportunity |
| Benefit | High conversion lift estimate (15%) | Medium conversion lift (8%) | Low direct lift (2%) | 0 immediate |
| Timeline | 2 weeks | 3 weeks | 1 week | 0 |
| Reversibility | 2-way (flag-able) | 2-way | 2-way | — |
| Confidence | Medium (survey-based) | Low | Low | High |
| 2nd-order | Power user churn 5-15%; support volume +30% | Less churn but weaker signal | Dashboard noise; no behavior change | Competitor catches up; free-tier costs grow |
| Kills | Alternative growth bets this quarter | Same | — | Several other options |

### Decision
**Choose B** (soft limit) with a 30-day evaluation window. Reasoning: the goal (drive conversions) is achievable without the hard-limit cliff that second-order analysis predicts will churn power users. Soft limit preserves the signal while avoiding the worst downstream effect.

### Kill condition
Kill if either: (a) conversion lift is below 4% after 30 days, OR (b) power-user churn rises above 3% baseline. In either case, revert to visibility-only (option C).

---

## Example 2 — Rename the product (consumer)

**Decision context**: The founders want to rename the product from "TaskFlow" to "Flowly" to reflect a new positioning. Growth team favors it; engineering worries about the migration.

**Options**:
- A: Rebrand and rename across all surfaces.
- B: Keep the product name, refresh visual identity only.
- C: Introduce new name as a subtitle/tagline; keep legal name.
- D: Do nothing.

### Matrix

|   | A: Full rename | B: Visual refresh | C: Subtitle addition | D: Do nothing |
|---|---|---|---|---|
| Direct cost | 8-12 eng-weeks | 2 eng-weeks | 1 eng-week | 0 |
| Opp. cost | 2 months of roadmap | Minimal | Minimal | — |
| Benefit | New positioning lands; press cycle | Visual refresh only; no positioning shift | Soft positioning shift | — |
| Timeline | 3 months | 1 month | 2 weeks | — |
| Reversibility | **1-way** (SEO, docs, customer memory, integrations) | 2-way | 2-way | — |
| Confidence | Medium (repositioning value); Low (execution risk) | High | High | High |
| 2nd-order | Customer confusion period 3-6 months; SEO rank loss; integrator notices; press cycle | Minimal | Subtle positioning shift; some customer confusion | Positioning grows stale |
| Kills | Every growth initiative this half | None | None | — |

### Decision
**Choose C** (subtitle addition) as the minimum reversible test of new positioning. Reasoning: A is a one-way door with high reversal cost, and the confidence on positioning value is medium at best. C allows testing the positioning with 2-way-door reversibility. If the new positioning resonates, revisit full rename with more evidence.

### Kill condition
Kill (remove subtitle) if within 90 days: (a) brand survey shows no lift in new-positioning recall, OR (b) organic search traffic drops >5%.

---

## Example 3 — Cut a rarely-used feature (dev tool)

**Decision context**: Feature X is used by 3% of active users. Maintenance cost is significant. Team proposes deprecating.

**Options**:
- A: Deprecate feature with 90-day notice.
- B: Freeze (stop new investment) but keep running.
- C: Scope reduce — keep core, cut advanced subset.
- D: Do nothing.

### Matrix

|   | A: Deprecate | B: Freeze | C: Scope reduce | D: Do nothing |
|---|---|---|---|---|
| Direct cost | 3 eng-weeks + support load | 0 | 4 eng-weeks | 0 |
| Opp. cost | Frees ~2 eng-weeks/quarter | — | Frees ~1 eng-week/quarter | Ongoing maintenance |
| Benefit | Large maintenance savings | Some savings (no new bugs) | Moderate savings; preserves most use | — |
| Timeline | 4 months | 0 | 2 months | — |
| Reversibility | **Close to 1-way** (users rebuild workarounds) | 2-way | Partial 1-way | — |
| Confidence | High (usage metrics) | High | Medium | High |
| 2nd-order | **The 3% includes high-NPS customers; churn-risk ≈ 20% of segment**; referral loss; "dev tool that deprecates features" reputation | Feature decays; complaints grow | Partial churn; some user anger | Maintenance burden grows |
| Kills | Keeping feature for advocates | — | Full deprecation later | Every cleanup option |

### Decision
**Choose B** (freeze). Reasoning: the second-order analysis flagged that the 3% likely includes high-NPS users whose advocacy matters disproportionately. Full deprecation is close to 1-way for those users' relationships. Freeze preserves the option while capturing maintenance savings on net-new investment.

### Kill condition
Revisit freeze decision if: (a) support load from feature exceeds 1 FTE-equivalent for 2 consecutive quarters, OR (b) usage drops below 1% (indicates natural attrition — safer to deprecate).

---

## Example 4 — Pricing model change (SaaS)

**Decision context**: Current seat-based pricing is causing friction for teams with many low-usage users. Considering a shift to usage-based.

**Options**:
- A: Full shift to usage-based for all new customers, grandfather existing.
- B: Hybrid — seat-based base + usage-based overage.
- C: Pricing experiment on 10% of new signups with feature flag.
- D: Do nothing.

### Matrix

|   | A: Full shift | B: Hybrid | C: 10% experiment | D: Do nothing |
|---|---|---|---|---|
| Direct cost | 6 eng-weeks + legal/finance | 4 eng-weeks | 1 eng-week | 0 |
| Opp. cost | Blocks other finance projects | Same | Minimal | — |
| Benefit | Best-case revenue lift if hypothesis right | Moderate lift, lower risk | Learning, no commitment | — |
| Timeline | 4 months | 3 months | 3 weeks | — |
| Reversibility | **1-way** (existing customers form expectations; reversal breaks trust) | **1-way** (hybrid is a promise) | **2-way** (flag-able, segment-isolated) | — |
| Confidence | Medium (good hypothesis, no evidence) | Medium | High (experimental) | High |
| 2nd-order | Predictability of revenue improves or worsens; sales motion changes; CS load shifts | Complexity for sales; invoicing changes | Cohort differences; small sample; no commitment | Continue current friction |
| Kills | Pricing stability for 2 years | Same | Several experiments later | Pricing innovation |

### Decision
**Choose C** (10% experiment). Reasoning: A and B are one-way doors with medium-confidence benefits. C converts the decision into a two-way door and produces evidence to lower the confidence interval before committing. If the experiment produces clear signal, revisit A or B with evidence.

### Kill condition
End experiment at 8 weeks regardless of signal (time-boxed). If revenue per experimental cohort > 15% above baseline at 8 weeks, escalate to planning a committed rollout. If <5%, discontinue the experiment and stay on seat-based.

---

## Patterns across examples

1. **"Do nothing" is always on the matrix.** Forces the team to justify action.
2. **Reversibility classification drives decision speed.** One-way doors require evidence; two-way doors reward speed.
3. **Second-order effects are where the real trade-off lives.** First-order is usually the easy comparison; second-order changes the answer.
4. **The kill clause is specific and time-bounded.** Not "if it doesn't work out" — a named threshold with a deadline.
5. **"Smaller version" options often win.** Converting a one-way door to a two-way door (via phased rollout, feature flag, or pilot) is frequently the best move.
6. **Confidence is made explicit.** Low confidence on a high-cost one-way door is a stop sign every time.
