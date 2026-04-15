# Outcome Hypothesis — Templates

A product bet is a falsifiable hypothesis, not a roadmap item. The hypothesis has six parts: the build, the behavior change, the segment, the leading indicator, the lagging indicator, and the kill clause. Missing any part turns the bet into a commitment without feedback.

## Core template

```
OUTCOME HYPOTHESIS

We believe that [building X]
will cause [user behavior change]
for [segment]
which will produce [outcome — leading indicator]
and ultimately [impact — lagging indicator].

We will know we are right when [leading indicator threshold] within [timeframe].
We will kill this bet if [falsification condition].
```

Rules:
- Every variable must be filled with specifics.
- The kill clause is mandatory.
- The timeframe must be shorter than the quarter (or whatever horizon you report on).

## Template variations

### Acquisition bet

```
We believe that [building a free-tier signup path without credit card]
will cause [developer evaluators to try the product before talking to sales]
for [individual developers at companies of 100-500 engineers].

It will produce [free-tier activation rate ≥ 40% in first month]
and ultimately [qualified pipeline per quarter up 25% from baseline 100 to 125].

We will know we are right when [free-tier activation ≥ 30% within 6 weeks].
We will kill this bet if [free-tier activation < 15% after 6 weeks OR free-to-paid
conversion < 3% by end of Q+1].
```

### Activation bet

```
We believe that [one-click sandbox provisioning]
will cause [new engineering leads to run a successful first deploy in their first session]
for [engineering leads doing tool evaluations, first 14 days after signup].

It will produce [first-session success rate ≥ 60% (up from 25%)]
and ultimately [14-day activation rate ≥ 50% (up from 32%)].

We will know we are right when [first-session success reaches 50% within 4 weeks].
We will kill this bet if [first-session success stays below 35% after 4 weeks].
```

### Retention bet

```
We believe that [weekly personalized digest of team-relevant activity]
will cause [product managers to return to the product Mondays for weekly planning]
for [PMs at teams of 20+ who haven't returned in the past 7 days].

It will produce [reactivation rate ≥ 25% (up from current 8%)]
and ultimately [30-day churn among dormant users down from 60% to 40%].

We will know we are right when [reactivation reaches 18% within 3 weeks].
We will kill this bet if [reactivation stays below 10% after 3 weeks].
```

### Monetization bet

```
We believe that [usage-based add-on pricing for high-volume API users]
will cause [users approaching seat-tier limits to add usage capacity rather than churn]
for [accounts in top decile by API usage].

It will produce [add-on attach rate ≥ 30% at limit-approaching accounts]
and ultimately [expansion revenue up 15% quarter-over-quarter].

We will know we are right when [add-on attach rate reaches 20% within 6 weeks].
We will kill this bet if [add-on attach rate stays below 10% after 6 weeks
OR churn at the top decile rises above baseline 8%].
```

### Referral bet

```
We believe that [post-purchase invite-a-colleague prompt with pre-filled value story]
will cause [new paying users to refer one colleague within 7 days of first value]
for [new paying users who completed the first-value milestone].

It will produce [invite-send rate ≥ 20% within 7 days of first value]
and ultimately [referral-attributable signups up 40% from baseline].

We will know we are right when [invite-send rate reaches 15% within 4 weeks].
We will kill this bet if [invite-send rate stays below 8% after 4 weeks].
```

## The kill clause — why it matters

The kill clause is the most frequently skipped line and the highest-leverage one. Without it:

- Bets never die — they survive by inertia.
- Teams keep shipping variations of a failing bet instead of reading the signal.
- Learning from failure is impossible because failure was never defined.

The kill clause answers: **what evidence would convince us to reverse this bet?** If nothing would, the bet is a commitment — which is fine, but call it that, not a bet.

### Kill clause structure

Good kill clauses have three properties:

1. **Specific threshold**: a number on a named metric.
2. **Specific timeframe**: by when the threshold must be met.
3. **Pre-committed action**: what happens if the threshold is missed. "Kill the bet" / "scale down" / "escalate for reassessment."

Bad kill clause: "If it doesn't seem to be working, we'll reconsider."
Good kill clause: "If first-session completion stays below 35% after 4 weeks, we roll back the sandbox and ship the original onboarding."

## Writing process

1. **Start with the lagging outcome.** What business / product outcome do you expect?
2. **Identify the user behavior.** What will users do differently if the bet works?
3. **Choose the leading indicator.** What early signal reflects that behavior?
4. **Name the segment.** Narrow enough to be measurable and to exclude noise.
5. **Set thresholds.** The "right" threshold reflects what level of change justifies the investment.
6. **Set the timeframe.** Shorter than the quarter; long enough for signal.
7. **Write the kill clause.** The falsification condition.
8. **Sanity check.** Can the team honestly commit to the kill clause? If not, rewrite it.

## Review cadence

Once the hypothesis is written, schedule reads at the specified cadence (usually weekly or biweekly). Each read produces one of three decisions:

- **On track**: continue; next read at schedule.
- **Borderline**: investigate what's not working; adjust if possible.
- **Off track / approaching kill**: escalate; decide whether to kill or pivot.

Teams that write hypotheses but never review them have done the theater without the discipline.

## Anti-patterns

- **Hypothesis without kill clause**: commitment disguised as experiment.
- **Vague thresholds**: "substantially better" is not a threshold.
- **Lagging-only indicators**: you find out whether the bet worked after the quarter ends.
- **Segment too broad**: "users" is not measurable; "new paying users in month 1" is.
- **Multiple metrics in one clause**: "X or Y or Z" is not a single falsifiable condition; pick one primary.
- **Rewriting thresholds mid-flight**: moving the threshold when it's about to be missed. The point of pre-committing is to commit.

## Integration with the team

Once hypotheses are written, they become the steering wheel for team rituals:

- **Weekly**: read the leading indicator. On/borderline/off.
- **Monthly**: review the quarter's hypotheses — which are on track, which are killed, which are new.
- **Quarterly**: retrospective on how many hypotheses were killed (too few is a bad sign — it means the team isn't making real bets).

The health of the hypothesis portfolio is itself a signal. Teams that never kill a bet are either miraculous or not actually making bets.
