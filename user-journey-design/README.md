# User Journey Design

> **v1.0.10** | Design & UX | 11 iterations

Design user journey maps with touchpoints, emotional states, pain points, and opportunities.

## What Problem Does This Solve

Product teams often optimize individual screens while missing the friction that accumulates across the full experience — the confusion between discovering a product and successfully using it for the first time, or the drop-off between onboarding and sustained engagement. User journey mapping makes that cross-stage friction visible by mapping what users do, think, feel, and struggle with at every touchpoint, so improvements can be prioritized where they reduce the most pain rather than where they are easiest to implement.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "Map out what a new user experiences from first hearing about the product to being a power user" | A stage-by-stage journey (Awareness -> Evaluation -> Onboarding -> Usage -> Mastery) with the structured template for goals, actions, touchpoints, emotion scores, and opportunities |
| "Where are users getting frustrated during API integration?" | An API integration journey (Discover -> Credentials -> Read ref -> Test -> Production) with pain point and opportunity analysis per stage |
| "I need to compare the current experience with the redesigned one" | Current-state vs. future-state journey types with side-by-side structure |
| "We need to see both the user's path and the internal org steps that support it" | Service blueprint format that layers front-stage user actions over back-stage organizational touchpoints |
| "What questions should I ask in user research to fill in a journey map?" | Touchpoint, action, thought, and emotion elements that guide interview and observation questions |
| "Help me find where to invest in documentation improvements" | Getting-started and troubleshooting journey templates revealing where doc gaps create user drop-off |

## When NOT to Use This Skill

- creating personas

## Installation

```bash
claude install-plugin github:viktorbezdek/skillstack/user-journey-design
```

## How to Use

**Direct invocation:**

```
Use the user-journey-design skill to ...
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `user-journey`
- `touchpoints`
- `experience-mapping`

## What's Inside

- **Journey Types** -- Three formats: current-state (as-is experience), future-state (to-be design), and service blueprint (combined user and organizational view).
- **Core Elements** -- The seven building blocks of every stage: stages, touchpoints, actions, thoughts, emotions (on a confidence-to-frustration scale), pain points, and opportunities.
- **Journey Template** -- Filled markdown template with a table structure for documenting all seven elements at each stage, ready to copy and populate.
- **Documentation Journeys** -- Three pre-built journey outlines for common technical documentation flows: Getting Started, Troubleshooting, and API Integration.

## Version History

- `1.0.10` fix(strategy+ux): optimize descriptions for outcome, prioritization, risk, systems, journey, ux-writing (9661735)
- `1.0.9` fix: update plugin count and normalize footer in 31 original plugin READMEs (3ea7c00)
- `1.0.8` fix: change author field from string to object in all plugin.json files (bcfe7a9)
- `1.0.7` fix: rename all claude-skills references to skillstack (19ec8c4)
- `1.0.6` docs: update README and install commands to marketplace format (af9e39c)
- `1.0.5` refactor: restructure all 34 skills into proper Claude Code plugin format (7922579)
- `1.0.4` refactor: make each skill an independent plugin with own plugin.json (6de4313)
- `1.0.3` docs: add detailed README documentation for all 34 skills (7ba1274)
- `1.0.2` refactor: standardize frontmatter and split oversized SKILL.md files (4a21a62)
- `1.0.1` docs: improve strategic skill descriptions (f59b24a)

## Related Skills

- **[Content Modelling](../content-modelling/)** -- Design content models with types, fields, relationships, and governance rules for structured content systems.
- **[Elicitation](../elicitation/)** -- Psychological profiling through natural conversation using narrative identity, self-defining memory elicitation, Motivat...
- **[Navigation Design](../navigation-design/)** -- Design information architecture, wayfinding systems, breadcrumbs, and navigation patterns for documentation and applicat...
- **[Ontology Design](../ontology-design/)** -- Design knowledge models with classes, properties, relationships, and taxonomies for structured data representation.
- **[Persona Definition](../persona-definition/)** -- Create detailed user personas with demographics, goals, pain points, behaviors, and empathy maps.

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 50 production-grade plugins for Claude Code.
