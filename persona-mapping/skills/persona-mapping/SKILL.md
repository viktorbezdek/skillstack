---
name: persona-mapping
description: Map stakeholders across organizations using Power-Interest matrices, RACI charts, influence analysis, and salience models to understand who has authority, who is affected, and how to engage each group. Use when the user asks to map stakeholders, create a RACI matrix, analyze organizational influence, identify decision-makers, prioritize who to involve, or plan stakeholder communication. NOT for individual user personas or empathy maps for product design (use persona-definition). NOT for designing the product's target audience (use persona-definition).
---

# Persona Mapping

Map stakeholders by influence, interest, and responsibility. Stakeholder analysis prevents predictable failures: over-communicating with people who don't care, under-communicating with those who can block, and assigning accountability so ambiguously that nobody owns decisions.

## When to Use

- Mapping stakeholders for a new project or initiative
- Creating RACI charts for cross-functional work
- Analyzing blockers and influence dynamics
- Designing engagement strategies for different stakeholder types
- Identifying latent stakeholders who could emerge as risks
- Planning communication cadence and channels per stakeholder group

## When NOT to Use

- Creating individual user personas with demographics, goals, and empathy maps (use persona-definition)
- Designing the product's target audience (use persona-definition)
- Designing user journeys across touchpoints (use user-journey-design)
- Prioritizing features or initiatives (use prioritization)
- Assessing project risks beyond stakeholder dynamics (use risk-management)

## Decision Tree

```
What stakeholder problem are you solving?
│
├─ New project/initiative — who matters?
│  ├─ Need initial categorization? → Power-Interest Matrix
│  ├─ Need role clarity on tasks? → RACI Chart
│  └─ Need nuanced prioritization? → Salience Model
│
├─ Stakeholder dynamics problem
│  ├─ Someone is blocking? → Power-Interest placement + engagement strategy
│  ├─ RACI confusion? → Enforce single Accountable per task
│  ├─ Latent stakeholder risk? → Salience Model to surface dormant power
│  └─ Resistant stakeholder? → Calibrate engagement to move resistant → neutral
│
├─ Communication planning
│  ├─ Equal updates to everyone? → Wrong; segment by Power-Interest quadrant
│  ├─ Who gets consulted vs informed? → RACI distinguishes 2-way vs 1-way
│  └─ What cadence per stakeholder? → Match to quadrant (closely vs satisfied vs informed vs monitor)
│
└─ Which tool to use?
   ├─ Quick initial map? → Power-Interest Matrix
   ├─ Task-level responsibility? → RACI Chart
   ├─ Complex org dynamics? → Salience Model
   └─ Full stakeholder plan? → All three (Power-Interest → RACI → Salience)
```

## Power-Interest Matrix

```
    HIGH INTEREST
         |
  KEEP   |   MANAGE
SATISFIED|   CLOSELY
         |
LOW -----+----- HIGH POWER
         |
 MONITOR |    KEEP
         |   INFORMED
    LOW INTEREST
```

### Engagement by Quadrant

| Quadrant | Strategy | Frequency | Channel |
|----------|----------|-----------|---------|
| High Power, High Interest (Manage Closely) | Active partnership, seek input on key decisions | Weekly or more | 1:1 meetings, decision reviews |
| High Power, Low Interest (Keep Satisfied) | Minimal but sufficient; don't surprise them | Bi-weekly or monthly | Executive summary, dashboard |
| Low Power, High Interest (Keep Informed) | Regular updates; channel their interest productively | Monthly | Newsletter, async updates |
| Low Power, Low Interest (Monitor) | Watch for changes; don't over-invest | Quarterly | Mass communication |

### Common Placement Mistakes

- DevOps lead placed as "Low Interest" when they can block deployment (should be High Power, High Interest)
- Frontend team marked "Informed" on API contracts they consume (should be at least Consulted)
- Executive sponsor placed as "Manage Closely" when they prefer "Keep Satisfied" (over-communication wastes their time)

## RACI Matrix

| Role | Definition | Per Task |
|------|------------|----------|
| **R**esponsible | Does work | 1+ |
| **A**ccountable | Decides | Exactly 1 |
| **C**onsulted | Input (2-way) | 0+ |
| **I**nformed | Updates (1-way) | 0+ |

### RACI Rules

1. **One Accountable per task** — if two people are Accountable, nobody is
2. **Consulted ≠ Everyone** — limit to those with legitimate expertise
3. **Most stakeholders should be Informed** — not Consulted
4. **Responsible does the work** — multiple Responsible is fine if scope is clear

### RACI Template

```markdown
| Task | [Person A] | [Person B] | [Person C] | [Person D] |
|------|-----------|-----------|-----------|-----------|
| Architecture design | R | C | C | A |
| API contract definition | R | C | I | I |
| Infrastructure changes | I | R | I | A |
```

## Salience Model

| Attributes | Type | Priority | Action |
|------------|------|----------|--------|
| Power + Legitimacy + Urgency | Definitive | Highest | Immediate attention; primary decision-maker |
| Power + Legitimacy | Dominant | High | Active management; key influencer |
| Legitimacy + Urgency | Dependent | Medium | Give voice; they're affected and urgent but lack power |
| Power + Urgency | Dangerous | Medium | Can act unilaterally; manage carefully |
| Single attribute | Latent | Low | Monitor; may escalate |

## Stakeholder Template

```markdown
## Stakeholder: [Name]

- **Role**: [title/team]
- **Influence**: High/Med/Low
- **Interest**: High/Med/Low
- **Attitude**: Supportive/Neutral/Resistant

### Engagement Strategy
- **Frequency**: [cadence]
- **Channel**: [method]
- **Key messages**: [emphasis]
- **Goal**: [desired attitude shift, e.g., "Neutral → Supportive"]
```

## Anti-Patterns

| Anti-Pattern | Problem | Solution |
|---|---|---|
| Multiple Accountable per task | Nobody makes the final decision; decisions delayed or contradictory | Enforce single Accountable; if contested, escalate to project sponsor |
| Everyone marked Consulted | Every decision requires 8 approvals; project grinds to halt | Limit Consulted to those with legitimate expertise; most should be Informed |
| Latent stakeholders ignored | A VP who was never mapped shows up in week 8 with veto power | Ask "who else could be affected?" at each phase gate; re-map quarterly |
| Resistant stakeholders avoided | Resistant stakeholder sabotages through back-channel influence | Engage early with specific objections; goal is neutral, not supportive |
| Static map in dynamic environment | Org restructures or departures make the map outdated | Review at each milestone; update when org changes occur |
| Power-Interest placement without evidence | "I think they have high power" without verifying | Cross-check: can they block? Can they approve budget? Do others defer to them? |
| RACI without tasks | "Create a RACI" without specifying deliverables produces a generic matrix | Always define the task/deliverable list first, then assign RACI |
| Equal communication to all | 30 stakeholders get the same update; most ignore, key ones miss critical info | Segment by quadrant; tailor frequency, channel, and message per group |

## Related Skills

- **persona-definition** — Create individual user personas with demographics, goals, and empathy maps
- **outcome-orientation** — Define outcomes that stakeholders align on
- **risk-management** — Stakeholder risks are one input to broader project risk assessment
- **prioritization** — Stakeholder input informs what to prioritize, but frameworks are separate
