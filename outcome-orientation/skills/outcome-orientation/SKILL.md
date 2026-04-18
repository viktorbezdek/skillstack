---
name: outcome-orientation
description: >-
  Reframe work around measurable outcomes using OKRs, KPIs, and the outcome-vs-output
  distinction. Use when the user asks to define success criteria, write OKRs, set KPIs,
  clarify what "done" means in terms of impact, distinguish outputs from outcomes, or
  make a goal statement measurable and time-bound. NOT for ranking or scoring features by
  priority (use prioritization). NOT for systemic feedback-loop analysis (use systems-thinking).
---

# Outcome Orientation

Focus on results that matter, not just activities completed. Outputs are what you produce. Outcomes are what changes as a result. Impact is the business-level change that outcomes drive. Most teams measure outputs because they're easy to count; measuring outcomes requires defining what "better" looks like before you start.

## When to Use

- Defining success criteria for a project, initiative, or feature
- Writing OKRs (Objectives and Key Results)
- Setting KPIs for a team or product
- Clarifying what "done" means in terms of impact, not deliverables
- Distinguishing outputs from outcomes in planning documents
- Making a vague goal statement measurable and time-bound
- Evaluating whether shipped work actually moved the metric

## When NOT to Use

- Ranking or scoring features by priority (use prioritization)
- Analyzing systemic feedback loops (use systems-thinking)
- Product-strategy outcome hypotheses with North Star metrics (use outcome-oriented-thinking in product-thinking)
- Individual performance reviews (that's HR, not product outcomes)

## Decision Tree

```
What outcome problem are you solving?
│
├─ "Are we measuring the right thing?"
│  ├─ Metric is something we produce? → That's an output; climb to outcome
│  ├─ Metric is something that changes for users? → That's an outcome ✅
│  └─ Metric is something that changes for the business? → That's impact ✅
│
├─ Writing OKRs
│  ├─ Objective is vague? → Make it qualitative but inspiring and directional
│  ├─ Key Result is an activity? → "Run 5 interviews" is output; "Identify top 3 pain points" is outcome
│  ├─ Key Result has no number? → Add baseline + target + timeframe
│  └─ Too many Key Results? → Max 3-5 per Objective; more dilutes focus
│
├─ Setting KPIs
│  ├─ Lagging indicator only? → Add a leading indicator for early signal
│  ├─ Can't measure it weekly? → Too lagging; find a proxy that's faster
│  └─ Multiple teams share same KPI? → Align on one; add team-specific sub-metrics
│
└─ "We shipped the feature but nothing changed"
   ├─ No baseline measurement before launch? → You can't prove change without a baseline
   ├─ Measuring output not outcome? → Reframe: "shipped" → "users completed X"
   └─ No leading indicator? → You waited too long to check; add leading for next bet
```

## Outcomes vs Outputs

| Outputs | Outcomes |
|---------|----------|
| Features shipped | User problems solved |
| Docs written | Users successful |
| Meetings held | Decisions made |
| Code deployed | Revenue generated |
| Interviews conducted | Pain points identified |
| Tests written | Bug escape rate reduced |

**The "So What?" test**: For any deliverable, ask "so what?" until you reach a change in user behavior or business result. If you can't get there, the output has no outcome hypothesis.

## OKR Framework

### Structure
```
Objective: Qualitative goal (inspiring, memorable)
├── KR1: Quantitative measure (specific, measurable)
├── KR2: Quantitative measure
└── KR3: Quantitative measure
```

### OKR Template

```markdown
## Objective: [Inspiring goal]

| Key Result | Baseline | Target | Current |
|------------|----------|--------|---------|
| [Metric 1] | [start] | [end] | [now] |
| [Metric 2] | [start] | [end] | [now] |
| [Metric 3] | [start] | [end] | [now] |

### Initiatives (How)
1. [Activity to drive KRs]
2. [Activity to drive KRs]
```

### Good vs Bad OKRs

| Bad | Good |
|-----|------|
| Launch feature X | Reduce time-to-value by 30% |
| Write 10 docs | 90% of users complete onboarding without help |
| Conduct 5 interviews | Identify top 3 user pain points by end of Q2 |
| Increase traffic | Organic signups grow 40% MoM |

**Diagnostic**: If your Key Result is a task you can check off, it's an output, not an outcome.

## Outcome Metrics

| Category | Lagging (Result) | Leading (Predictor) |
|----------|-----------------|---------------------|
| Revenue | Monthly revenue | Pipeline created |
| Adoption | Active users | Activation rate |
| Quality | Defect rate | Test coverage |
| Satisfaction | NPS score | Support ticket trend |

Rule: **Every initiative needs at least one leading indicator.** Without it, you wait until the lagging indicator moves — by then, the quarter is over.

## Results Chain

```
Activities -> Outputs -> Outcomes -> Impact
(do)         (produce)   (achieve)   (change)
```

Each link must be testable. If "Activities → Outputs" is the only visible link, you're doing work without a theory of change.

## Outcome Definition Checklist

- [ ] Describes end state, not activity
- [ ] Measurable and time-bound
- [ ] Within influence (not full control)
- [ ] Valuable to user/business
- [ ] Achievable but stretching
- [ ] Has at least one leading indicator
- [ ] Baseline is known before work starts

## Anti-Patterns

| Anti-Pattern | Problem | Solution |
|---|---|---|
| Output-as-outcome | "Ship 5 features" counted as success; no behavior change measured | Apply "so what?" test; reframe as user behavior change |
| No baseline | Cannot prove improvement without a before measurement | Measure before you start; even a rough baseline beats none |
| Lagging-only metrics | Find out the bet failed 3 months after you could have acted | Add at least one leading indicator per initiative |
| OKR as task list | Key Results are to-do items, not measurable outcomes | KRs must have numbers: "Reduce X from A to B by date" |
| Too many OKRs | 10 objectives means no focus; everything is a priority | Max 3-5 objectives, 3-5 KRs each; force prioritization |
| Vanity metrics | Page views, signups — they go up regardless of value | Choose metrics tied to user value: activation, retention, revenue |
| Moving targets | Goalposts shift mid-quarter to match results | Lock KRs at quarter start; if context changes, write a new KR |
| No kill condition | Bets never die; teams keep shipping against a failing hypothesis | Add a "we kill this if X hasn't moved by Y" clause |

## Related Skills

- **outcome-oriented-thinking** (product-thinking) — Product-strategy outcomes: North Star, outcome hypotheses with kill clauses
- **prioritization** — Ranking features/initiatives once outcomes are defined
- **systems-thinking** — Feedback loops connecting outputs to outcomes
