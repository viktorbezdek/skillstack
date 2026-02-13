---
name: prioritization
description: Apply prioritization frameworks including RICE, MoSCoW, ICE scoring, and effort-impact matrices for decision-making.
triggers:
  - prioritization
  - RICE
  - MoSCoW
  - ICE
  - backlog ranking
  - effort-impact analysis
---

# Prioritization

Make better decisions about what to do first.

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

- HiPPO (Highest Paid Person's Opinion)
- Recency bias (latest request wins)
- Squeaky wheel (loudest customer)
- Sunk cost (already invested, must continue)

