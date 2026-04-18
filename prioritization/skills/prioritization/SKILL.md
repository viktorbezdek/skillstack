---
name: prioritization
description: >-
  Apply RICE, MoSCoW, ICE, and effort-impact frameworks to rank options and decide what
  to work on next. Use when the user asks to prioritize a backlog, rank features, decide
  what to build first, apply RICE or MoSCoW scoring, cut scope, or compare items by
  effort vs impact. NOT for defining success metrics or OKRs (use outcome-orientation).
  NOT for making a strategic bet under uncertainty (use strategic-decision workflow).
---

# Prioritization

Make better decisions about what to do first.

## When to use this skill

- Scoring features or initiatives to decide quarterly priorities
- Categorizing requirements as Must/Should/Could/Won't for a release
- Creating effort-impact matrices for sprint planning
- Defending prioritization decisions to stakeholders with data
- Auditing existing prioritization for bias (HiPPO, recency, squeaky wheel)
- Choosing between RICE, ICE, MoSCoW, or effort-impact for a specific situation

## When NOT to use this skill

- **Defining OKRs or success metrics** → use `outcome-orientation`
- **Assessing project risks** → use `risk-management`
- **Making strategic bets under deep uncertainty** → use `strategic-decision` workflow
- **Stakeholder analysis for whose input to weight** → use `persona-mapping`

---

## Framework selection decision tree

```
Do you have reach data (users affected per quarter)?
  YES → Do you need quantitative rigor for stakeholder defense?
    YES → RICE (most defensible, separates reach/impact/confidence)
    NO  → Effort-Impact matrix (quick visual sort)
  NO  → Do you need release scoping with capacity constraints?
    YES → MoSCoW (60% rule prevents scope creep)
    NO  → ICE (lightweight, works with subjective scores only)

Using more than one? They complement each other:
  RICE or ICE for quarterly prioritization
  MoSCoW for release scoping
  Effort-Impact for sprint-level quick wins
```

---

## RICE Scoring

**Reach x Impact x Confidence / Effort**

| Factor | Description | Scale |
|--------|-------------|-------|
| Reach | Users affected per quarter | Number |
| Impact | Effect on goal | 0.25-3 |
| Confidence | Certainty level | 50-100% |
| Effort | Person-months | Number |

```
Score = (R x I x C) / E
```

### Impact Scale
- 3 = Massive
- 2 = High
- 1 = Medium
- 0.5 = Low
- 0.25 = Minimal

## MoSCoW Method

| Priority | Meaning | Guideline |
|----------|---------|-----------|
| **M**ust | Required for success | Non-negotiable |
| **S**hould | Important but not vital | Include if possible |
| **C**ould | Nice to have | If time permits |
| **W**on't | Not this time | Explicitly excluded |

Rule: Must = 60% max of effort

## ICE Scoring

| Factor | Description | Scale |
|--------|-------------|-------|
| Impact | Potential value | 1-10 |
| Confidence | Certainty | 1-10 |
| Ease | Simplicity | 1-10 |

```
Score = (I + C + E) / 3
```

## Effort-Impact Matrix

```
HIGH IMPACT
     |
 BIG |  QUICK
BETS |  WINS
     |
-----+------ LOW EFFORT
     |
MONEY|  FILL
PITS |  INS
     |
LOW IMPACT
```

**Priority order**: Quick Wins -> Big Bets -> Fill Ins -> Avoid Money Pits

## Prioritization Template

```markdown
## Item: [Name]

### RICE Score
| Factor | Value | Notes |
|--------|-------|-------|
| Reach | [num] | [who] |
| Impact | [0.25-3] | [why] |
| Confidence | [%] | [evidence] |
| Effort | [PM] | [breakdown] |
| **Score** | [calc] | |

### Decision
Priority: [High/Med/Low]
Rationale: [reasoning]
```

## Anti-Patterns

### Common prioritization failures

1. **HiPPO (Highest Paid Person's Opinion)** — the most senior person's preference wins regardless of impact data. Counter: present RICE comparison data; if overridden, document the override reason explicitly.
2. **Recency bias** — the latest request displaces long-planned high-impact work. Counter: score every request before adding to backlog; compare new request score against current top items.
3. **Squeaky wheel** — the loudest customer gets prioritized, not the most impacted segment. Counter: weight by reach data, not volume of complaints.
4. **Sunk cost fallacy** — continuing a project because of past investment. Counter: re-score with only remaining effort and remaining impact; past investment is irrelevant to forward-looking decisions.
5. **Confidence inflation** — scoring 90% confidence on everything, eliminating it as a differentiator. Counter: calibrate — 90% = strong evidence (A/B test, customer data), 70% = reasonable belief, 50% = intuition only.
6. **All Must-haves** — MoSCoW with 15 "Must" items exceeding capacity. Counter: enforce the 60% rule; force-rank within Must and demote the lowest.
7. **RICE without data** — guessing all values produces opinions with math, not defensible scores. Counter: switch to ICE (designed for subjective scoring) or invest in analytics before RICE.
8. **Strategic override without documentation** — overriding RICE for a key account is sometimes correct, but undocumented overrides erode trust in the framework. Always write down why.
