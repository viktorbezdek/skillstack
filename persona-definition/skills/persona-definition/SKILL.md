---
name: persona-definition
description: Create individual user personas and customer archetypes — with demographics, goals, pain points, behaviors, and empathy maps — to represent the humans a product or system is built for. Use when the user asks to define personas, create user archetypes, describe target users, build empathy maps, or characterize the audience for a product or design decision. NOT for mapping stakeholders across an organization, RACI charts, or influence analysis (use persona-mapping). NOT for designing research interview flows (use elicitation).
---

# Persona Definition

Create research-backed user personas that drive product and documentation decisions. A persona is a composite archetype grounded in observed behavior, not a fictional character invented by the team. Personas without evidence are opinions with names.

## When to Use

- Defining who the product is for before building features
- Creating user archetypes for a new product or feature
- Building empathy maps to understand user emotional landscape
- Characterizing the audience for documentation or design decisions
- Aligning a team on who they're building for
- Evaluating whether a feature serves a real user need

## When NOT to Use

- Mapping stakeholders across an organization with power/interest (use persona-mapping)
- Creating RACI charts or influence analysis (use persona-mapping)
- Designing research interview flows (use elicitation)
- Identifying what users need (jobs, wants vs needs) (use user-needs-identification)
- Writing value propositions (use value-proposition-design)

## Decision Tree

```
What persona problem are you solving?
│
├─ Creating new personas
│  ├─ Quick alignment needed, no research yet? → Proto-persona (low detail)
│  ├─ Agile team, need direction for MVP? → Lean persona (medium detail)
│  └─ Strategic decisions, high stakes? → Full persona (high detail, evidence-backed)
│
├─ Validating existing personas
│  ├─ No research behind them? → Rebuild from interviews/behavior data
│  ├─ Personas are aspirational? → Replace with behavior-observed personas
│  └─ Too many personas? → Consolidate to 3-5; merge overlapping ones
│
├─ Using personas for decisions
│  ├─ Feature prioritization? → Check against persona goals and pain points
│  ├─ Content/UX decisions? → Check against persona behaviors and context
│  └─ Stakeholder alignment? → Use empathy map to build shared understanding
│
└─ Persona vs stakeholder question
   ├─ "Who is the user?" → Persona definition (this skill)
   └─ "Who has power/influence?" → Persona mapping (different skill)
```

## Persona Types

| Type | Purpose | Detail | Research Required |
|------|---------|--------|-------------------|
| Proto-persona | Quick alignment | Low | None (team assumption) |
| Lean persona | Agile, MVPs | Medium | Some (3-5 interviews) |
| Full persona | Strategic decisions | High | Extensive (10+ interviews, behavior data) |

## Core Components

1. **Demographics**: Name, age, role, tech proficiency
2. **Goals**: Primary, secondary, experience goals
3. **Pain Points**: Blockers, unmet needs, frustrations
4. **Behaviors**: Habits, decision-making, preferences
5. **Context**: Environment, devices, constraints

## Empathy Map

```
    SAYS         |      THINKS
-----------------+------------------
    DOES         |      FEELS
```

- **Says**: Direct quotes from interviews
- **Thinks**: What they believe but may not say aloud
- **Does**: Observable actions and behaviors
- **Feels**: Emotional state — frustrations, fears, satisfactions

## Persona Template

```markdown
# [Name]
> "[Quote from real user]"

| Attribute | Value |
|-----------|-------|
| Role | [job] |
| Tech Savvy | [1-5] |
| Primary Goal | [goal] |

## Goals
1. Primary: [objective]
2. Avoid: [prevention]

## Pain Points
- [frustration 1]
- [frustration 2]

## Behaviors
- [habit 1]
- [decision-making pattern]

## Context
- Environment: [office/remote/field]
- Devices: [primary + secondary]
- Time constraints: [when and how they use the product]

## Needs from Documentation
- [format preference]
- [detail level]
```

## Anti-Patterns

| Anti-Pattern | Problem | Solution |
|---|---|---|
| Aspirational personas | Describes who you wish users were, not who they are | Build from observed behavior and interviews, not team ideals |
| Too many personas | 8+ personas means no one can remember them; decisions dilute | Aim for 3-5 primary personas; merge overlapping ones |
| Demographic-only personas | Age/role without goals or behaviors tells you nothing about product needs | Always include goals, pain points, and behavioral patterns |
| Static personas | Personas created once and never updated as understanding evolves | Review quarterly; update when new research contradicts assumptions |
| Fictional details as evidence | "Meet Sarah, 34, who loves yoga" — decoration, not data | Use real interview quotes and observed behaviors as evidence |
| One persona per team member | Each stakeholder projects their favorite user; no shared understanding | Build personas collaboratively from shared research |
| Personas without scenarios | Persona exists but never connects to a use case | Pair each persona with 2-3 key scenarios they encounter |

## Related Skills

- **persona-mapping** — Stakeholder analysis with Power-Interest matrix, RACI charts, influence mapping
- **user-needs-identification** (product-thinking) — Separate functional/emotional/social jobs; surface latent needs
- **elicitation** — Design interview protocols for gathering persona research data
- **value-proposition-design** (product-thinking) — Map personas to pains/gains on the Value Proposition Canvas
