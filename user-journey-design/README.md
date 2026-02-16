# User Journey Design

> Design user journey maps with touchpoints, emotional states, pain points, and opportunities from awareness through mastery.

## Overview

Understanding how users move through a product experience is critical for identifying friction, discovering opportunities, and aligning teams around the customer perspective. This skill provides a structured methodology for mapping complete user journeys across every stage, from initial awareness through evaluation, onboarding, active usage, and eventual mastery.

The skill supports three journey types: current-state maps that document the as-is experience, future-state maps that design the to-be experience, and service blueprints that combine the user perspective with the organizational view. Each journey captures actions, touchpoints, thoughts, emotions, pain points, and improvement opportunities at every stage.

Within the SkillStack collection, this skill works closely with persona-definition (defining who the user is), ux-writing (crafting the interface text at each touchpoint), and navigation-design (structuring the paths users take through a product).

## What's Included

This is a focused skill with all guidance contained in a single SKILL.md file. It does not include separate reference, template, script, or example directories. The journey template, documentation journey patterns, and core element definitions are all embedded directly in the skill definition.

## Key Features

- **Three journey types** covering current-state analysis, future-state design, and service blueprint mapping
- **Seven core elements** tracked at each stage: goals, actions, touchpoints, thoughts, emotions, pain points, and opportunities
- **Five-stage journey model** from Awareness through Evaluation, Onboarding, Usage, and Mastery
- **Emotional mapping** with a 1-5 confidence/frustration scale to quantify user sentiment
- **Documentation-specific journeys** for Getting Started, Troubleshooting, and API Integration flows
- **Structured markdown template** for consistent, shareable journey documentation

## Usage Examples

### Map the onboarding journey for a SaaS product

```
Create a user journey map for a new developer signing up for our API platform. Cover from landing page through first successful API call.
```

Produces a multi-stage journey map with touchpoints (docs site, dashboard, API console), emotional tracking (excitement at sign-up, potential frustration at API key setup), pain points, and specific improvement opportunities.

### Analyze the current-state troubleshooting experience

```
Map the current-state journey for a user encountering a 500 error in our web app. Include their emotional state and pain points at each step.
```

Documents the as-is experience from error encounter through search, documentation lookup, support contact, and resolution, highlighting where users get stuck and where emotions dip.

### Design a future-state onboarding flow

```
Design a future-state journey for our mobile app onboarding. The current flow has a 40% drop-off at step 3 (profile setup). Propose improvements.
```

Creates a to-be journey that restructures the onboarding stages, moves profile setup to a later touchpoint, and includes progressive disclosure to reduce initial friction.

### Create a service blueprint for a support workflow

```
Create a service blueprint for our customer support ticket flow, showing both the user-facing journey and the internal team actions at each stage.
```

Produces a dual-layer map combining the user journey (submit ticket, receive acknowledgment, get updates, resolution) with backstage actions (triage, assignment, investigation, response).

### Map documentation journeys for an API product

```
Map the three key documentation journeys for our REST API: getting started, troubleshooting an integration error, and going to production.
```

Generates three focused journey maps following the built-in documentation patterns (Getting Started, Troubleshooting, API Integration), each with stage-specific touchpoints and emotions.

## Quick Start

1. **Define the persona** - Identify who is taking the journey. Use the persona-definition skill if you need a detailed persona.
2. **Set the goal** - What is the user trying to accomplish? Be specific (e.g., "complete first purchase" not "use the product").
3. **Choose the journey type** - Current state (document what exists), future state (design what should be), or service blueprint (include organizational view).
4. **Map the stages** - Walk through the five stages (Awareness, Evaluation, Onboarding, Usage, Mastery) and fill in the seven elements for each relevant stage.
5. **Rate emotions** - Assign a 1-5 score at each stage to create an emotional curve that visually highlights problem areas.
6. **Identify the top pain points** - Look for stages where emotions dip below 3 and where multiple pain points cluster.
7. **Prioritize opportunities** - Convert each pain point into a specific, actionable improvement opportunity.

## Related Skills

- [persona-definition](../persona-definition/) - Define the users whose journeys you are mapping
- [persona-mapping](../persona-mapping/) - Map personas to product features and touchpoints
- [ux-writing](../ux-writing/) - Write the microcopy and interface text at each journey touchpoint
- [navigation-design](../navigation-design/) - Design the navigation structure users follow through the product
- [outcome-orientation](../outcome-orientation/) - Align journey improvements with measurable business outcomes
- [content-modelling](../content-modelling/) - Model the content structure that supports each journey stage

---

Part of [SkillStack](https://github.com/viktorbezdek/claude-skills) — `/plugin install user-journey-design@claude-skills` — 34 production-grade skills for Claude Code.
