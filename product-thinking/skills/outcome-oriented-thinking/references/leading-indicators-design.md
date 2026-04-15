# Leading Indicators — Design

Leading indicators predict the lagging outcome. They are the steering signals that let teams act mid-quarter rather than discovering failure at the end. A product bet without a leading indicator is a bet without a dashboard — by the time the outcome moves, the quarter is over.

## Leading vs lagging — the distinction

| Kind | Signal speed | Purpose |
|---|---|---|
| Leading | Days / weeks | Predict; enable course correction |
| Lagging | Weeks / quarters | Confirm; prove outcome achieved |

Neither is superior. Both are needed. Leading without lagging is false signal (you never confirm real outcome). Lagging without leading is blind flying (you discover failure too late to act).

## Design process

### Step 1 — state the expected outcome (lagging)

Start with the lagging outcome you expect. Be specific and measurable.

- ❌ "Activation improves."
- ✅ "Quarterly activation rate rises from 32% to 45%."

### Step 2 — hypothesize the user behavior

What user behavior, if it occurs, would cause the lagging outcome? The behavior should be:
- Specific (a named action).
- Frequent (observable in days, not months).
- Causal (the behavior plausibly causes the outcome).

- Lagging: "quarterly activation rises from 32% to 45%."
- Hypothesized behavior: "new users complete the first-value milestone within 7 days of signup."

### Step 3 — define the leading indicator

The leading indicator measures the hypothesized behavior directly.

- Hypothesized behavior: "complete first-value milestone within 7 days."
- Leading indicator: "% of new users completing first-value milestone within 7 days."

Cadence: readable weekly.

### Step 4 — set the threshold

Define what success looks like on the leading indicator. The threshold should predict the lagging outcome.

- Leading: "% of new users completing first-value milestone within 7 days."
- Threshold: "≥ 40% within 4 weeks of bet launch."

### Step 5 — set the kill condition

Define what failure looks like.

- Kill: "Below 20% after 4 weeks — reverse the bet."

The kill condition is the most-skipped step and the most valuable. It turns the bet into a falsifiable hypothesis rather than a commitment.

## Criteria for a good leading indicator

1. **Causal (not just correlated)**. The behavior plausibly causes the outcome, not just co-occurs.
2. **Measurable weekly**. If the dashboard updates quarterly, the indicator is not leading — it is lagging in disguise.
3. **Behavioral (not sentiment)**. NPS and CSAT can be leading for some outcomes, but behavioral signals are stronger predictors.
4. **Not gameable**. Can the team move the indicator without actually improving the outcome? If yes, pick a different indicator.
5. **Attributable**. The team can trace indicator movements to their work.

## Examples — good vs bad

### B2B SaaS: "increase quarterly retention"

| Indicator | Leading? | Why |
|---|---|---|
| Monthly active users | Lagging | Too slow, too aggregate |
| Weekly feature-X usage among new cohort | Leading ✅ | Specific, weekly, behavioral |
| NPS score | Lagging (sentiment) | Slow feedback, not behavioral |
| Time-to-first-value | Leading ✅ | Measurable at signup + 7 days |

### Consumer app: "increase 30-day retention"

| Indicator | Leading? | Why |
|---|---|---|
| 30-day retention | Lagging (is the outcome) | Slow, confirms only |
| Day-1 return rate | Leading ✅ | Readable by day 2 |
| Session length | Weak leading | Correlated but not strongly causal |
| Habit-forming action in week 1 | Leading ✅ | Behavioral, predictive |

### Marketplace: "increase GMV"

| Indicator | Leading? | Why |
|---|---|---|
| GMV | Lagging | The outcome |
| Supply-side listings added | Weak leading | More listings ≠ more transactions |
| Search-to-transaction rate | Leading ✅ | Predictive, weekly-measurable |
| First-time-buyer repeat rate (30 days) | Leading ✅ | Predicts retention and GMV |

## Common mistakes

- **Lagging-only metrics.** Team tracks retention and revenue, no weekly signal. Mid-quarter course correction is impossible.
- **Vanity metrics as leading.** Signups and page views rise without predicting outcomes. Pick behaviors tied to customer value, not volume.
- **Correlated, not causal.** The indicator moves with the outcome historically but the team cannot explain why. Risk: the indicator moves without the outcome following.
- **Non-attributable indicators.** The indicator changes with market conditions; the team cannot trace movement to their work. Frustrating to act on.
- **Gameable indicators.** The team can move the number without improving the outcome (e.g., changing the definition of "active" to include lower-activity users).

## Leading indicators for different bet types

### Acquisition bet

- Lagging: quarterly new-paid-customers.
- Leading: qualified-lead rate per week; demo-to-trial conversion; trial-to-paid rate at 14 days.

### Activation bet

- Lagging: quarterly activation rate.
- Leading: day-7 milestone completion; time-to-first-value; onboarding completion rate.

### Retention bet

- Lagging: 30- or 90-day retention.
- Leading: week-1 return rate; feature-X adoption in first 30 days; first-response time (support).

### Monetization bet

- Lagging: ARPU, LTV.
- Leading: upgrade prompt conversion rate; feature-X usage among paying tier; expansion at 30-day renewal.

### Referral bet

- Lagging: k-factor.
- Leading: invite-send rate within 7 days of signup; invite-accept rate.

## Cadence and review

Leading indicators earn their keep in review meetings. Set a weekly or bi-weekly cadence:

- Read the leading indicator.
- Compare to the hypothesized threshold.
- Decide: on-track (continue), borderline (investigate), off-track (course correct or approach kill).

Teams that set leading indicators but never review them have invested in analytics without getting the feedback loop. The loop is the product.
