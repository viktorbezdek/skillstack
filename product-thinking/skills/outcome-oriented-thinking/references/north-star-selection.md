# North Star Selection

The North Star metric (NSM) is a single metric that captures the value customers get from the product. It orients every team's work, filters ambiguous decisions, and signals whether the product is actually working — upstream of revenue.

## What a North Star is and is not

| IS | IS NOT |
|---|---|
| A customer-value metric at the outcome layer | A feature-count or activity metric |
| Actionable — teams can move it | Revenue (that is impact, lagging) |
| Predictive — leads long-term business health | A composite score (unreadable) |
| Single — one metric per product | A pile of KPIs |
| Durable — same metric for many quarters | Changes every planning cycle |

## Five selection criteria

1. **Aligned to customer value.** When the metric rises, customers actually got more value. Not "signups" (users can sign up without getting value); not "features shipped" (output, not value).

2. **Actionable.** The team can move it through their work. A North Star outside the team's influence produces helplessness, not direction.

3. **Predictive of long-term business health.** It leads revenue. Teams measured on revenue alone cannot act on it until it's too late.

4. **Measurable with low effort.** You can read it weekly without a data-engineering project. If the metric requires a quarterly BI analysis to compute, it will not function as a steering wheel.

5. **Understandable.** A new engineer can explain what it measures and why it matters on day one. Composite scores fail this test.

## Worked examples

### Messaging app

**Candidates**: daily active users, messages sent per user, time in app, retention-week-4.

**Choice**: messages sent per weekly active user.

**Why**: DAU measures presence, not value. Messages sent measures the core value exchange (communication). "Per WAU" prevents gaming through bot accounts or inflated sign-ups. Weekly is the right cadence for a messaging app (daily is noisy; monthly misses shifts).

### B2B devtool

**Candidates**: paying accounts, weekly active users, repos connected, repos with ≥3 commits per week.

**Choice**: weekly active repos with ≥3 commits.

**Why**: paying accounts is revenue (impact, lagging). WAU is presence, not use. Repos connected is setup, not ongoing value. Active repos with commits is the signal that the tool is embedded in real work. ≥3 commits separates trial repos from working repos.

### Marketplace

**Candidates**: listings posted, transactions, GMV, repeat-transaction ratio.

**Choice**: successful transactions per month (or GMV from repeat buyers).

**Why**: listings posted is supply-side vanity (a marketplace can have many listings and no transactions). GMV includes one-time transactions that may never repeat. Repeat transactions signal that both supply and demand are receiving value — the definition of marketplace health.

### Content platform

**Candidates**: DAU, video starts, minutes watched, meaningful-sessions (≥5 min).

**Choice**: minutes of content consumed per active user (or meaningful sessions).

**Why**: DAU is presence. Video starts can be accidental. Minutes watched captures value delivered. Meaningful-sessions (≥5 min) excludes drive-bys.

## Anti-North-Stars

- **Vanity metrics**: signups, page views, app installs. They rise without value being delivered.
- **Revenue as NSM**: lagging, not predictive of what caused it. Revenue is impact, downstream of the NSM.
- **Composite scores**: "Engagement = 0.3×A + 0.2×B + …". Unreadable, un-falsifiable, and always drifts based on whichever subcomponent is convenient this quarter.
- **Output metrics**: features shipped, tickets closed, releases deployed. Measures effort, not change.
- **Satisfaction scores alone**: NPS / CSAT are lagging sentiment, not product value.

## Selection workflow

1. **List 5-10 candidate metrics.** Include bad candidates to stress-test.
2. **Score each against the five criteria.** Strong (2) / weak (1) / fails (0).
3. **Rank by total score.** The top candidate is the NSM.
4. **Pressure-test.** For each candidate, ask:
   - Could it go up while customer value goes down? (if yes, the metric is gameable)
   - Could customer value go up while the metric stays flat? (if yes, the metric is under-counting)
5. **Define measurement.** Exact formula, source of truth, cadence, who owns it.
6. **Communicate.** One-sentence explanation: "Our North Star is X because when X rises, customers are getting Y."

## When to change the NSM

Rarely. A NSM should last multiple years unless:

- The product fundamentally shifts (new segment, new category).
- Evidence shows the NSM is gameable or miscalibrated.
- The product category matures and a more specific metric becomes available.

Changing the NSM every planning cycle means it is not a North Star — it is a scoreboard the team moves when inconvenient.

## NSM vs input metrics

The NSM is the outcome. Teams don't usually work directly on the NSM — they work on input metrics that are believed to drive it. Input metrics sit between activities and the NSM and should be revisited when the NSM moves unexpectedly (either direction).

```
Activities → Input metrics → NSM → Business impact
(build)     (proxies)       (value) (revenue)
```

Each team owns one or more input metrics that connect to the NSM. The NSM is the shared destination; input metrics are the team-level handles.
