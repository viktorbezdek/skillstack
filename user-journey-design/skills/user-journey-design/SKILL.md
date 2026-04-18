---
name: user-journey-design
description: >-
  Map user journeys with touchpoints, emotional states, pain points, and opportunities
  across the full arc of a user's experience over time. Use when the user asks to map
  a user journey, create a customer journey map, design a service blueprint, document
  touchpoints and friction points, or visualize the end-to-end experience of a user
  across multiple interactions. NOT for static navigation structure or sitemaps
  (use navigation-design). NOT for creating user personas or archetypes (use
  persona-definition). NOT for designing research interview flows (use elicitation).
  NOT for writing microcopy at specific touchpoints (use ux-writing).
---

# User Journey Design

Map complete user experiences from awareness through mastery.

## When to use this skill

- Mapping how a user experiences a product or service end-to-end over time
- Identifying friction points and emotional lows in an existing experience
- Designing a future-state experience for a new feature or product
- Creating service blueprints that show both user and organizational actions
- Documenting the touchpoints between a user and your product

## When NOT to use this skill

- **Static navigation structure or sitemaps** → use `navigation-design`
- **Creating user personas or archetypes** → use `persona-definition`
- **Designing research interviews** → use `elicitation`
- **Writing microcopy for specific UI elements** → use `ux-writing`
- **Technical flow diagrams or process flows** → use workflow/systems tools

---

## Decision tree

```
What are you trying to understand?
  │
  ├─ How users experience our EXISTING product over time
  │   └─ Current-state journey map: observe → document → identify pain points
  │
  ├─ How users SHOULD experience a NEW or redesigned product
  │   └─ Future-state journey map: define ideal → map stages → identify gaps
  │
  ├─ How both the user AND the organization act across touchpoints
  │   └─ Service blueprint: map front-stage (user) + back-stage (org) + support processes
  │
  └─ Where users drop off or struggle in a specific flow
      └─ Focused journey fragment: zoom into the problem stage → map in detail

Journey scope?
  │
  ├─ Full product lifecycle (awareness → mastery)
  │   └─ 5-7 stages, broad but structured
  │
  ├─ Single flow (e.g., checkout, onboarding, API integration)
  │   └─ 3-5 stages, narrow and deep
  │
  └─ Documentation path (getting started, troubleshooting, API reference)
      └─ Use pre-built templates: Getting Started / Troubleshooting / API Integration
```

---

## Journey Types

| Type | Focus | When to use |
|------|-------|-------------|
| Current state | As-is experience | Auditing existing UX, finding friction |
| Future state | To-be design | Redesigning or building new experiences |
| Service blueprint | Org + user view | Aligning front-stage and back-stage processes |

## Core Elements

1. **Stages**: Awareness -> Evaluation -> Onboarding -> Usage -> Mastery
2. **Touchpoints**: Interaction points (where the user meets your product)
3. **Actions**: What users do at each stage
4. **Thoughts**: Questions, assumptions, mental models
5. **Emotions**: Confidence <-> Frustration scale (1-5)
6. **Pain Points**: Friction, confusion, blockers
7. **Opportunities**: Improvements, quick wins, strategic changes

## Journey Template

```markdown
# [Persona] Journey: [Goal]

## Stage 1: [Name]
| Element | Details |
|---------|---------|
| Goal | [what they want at this stage] |
| Actions | [what they do] |
| Touchpoints | [where the interaction happens] |
| Emotion | [1-5 scale: 1=frustrated, 5=confident] |
| Pain Points | [what goes wrong or causes friction] |
| Opportunities | [how to improve the experience] |
```

## Documentation Journeys

**Getting Started**: Land -> Find quickstart -> Setup -> Run example -> Success
**Troubleshooting**: Error -> Search -> Find article -> Try fix -> Resolve
**API Integration**: Discover -> Credentials -> Read ref -> Test -> Production

## Anti-Patterns

1. **Mapping the happy path only** — showing only the ideal flow without error states, detours, or alternative paths. Fix: for each stage, ask "what if this goes wrong?" and map the recovery path.
2. **Journey without a persona** — mapping "the user" instead of a specific persona with defined goals, context, and constraints. Fix: always anchor the journey to a named persona from `persona-definition`.
3. **Ignoring emotional state** — documenting actions and touchpoints but not how the user feels at each stage. Fix: the emotion score is the most actionable data point; friction always correlates with emotional lows.
4. **Too many stages** — 10+ stages make the map unreadable and unfocused. Fix: group into 4-7 major stages; use sub-stages only when zooming into a specific section.
5. **Service blueprint without back-stage** — showing only the user-facing experience without the internal processes that enable it. Fix: a real service blueprint has three layers: front-stage (user sees), back-stage (org does), support processes (systems that enable).
6. **Journey map as artifact, not tool** — creating the map once and never revisiting it. Fix: treat journey maps as living documents; revisit after feature launches, user research, or quarterly reviews.
7. **Mixing personas in one map** — mapping "users" without differentiating personas causes pain points to average out and hide critical differences. Fix: create separate maps per key persona; a power user's troubleshooting journey differs fundamentally from a beginner's.
