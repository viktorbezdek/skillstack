# Persona Mapping

> **v1.0.10** | Design & UX | 11 iterations

Map stakeholders and personas using Power-Interest matrices, RACI charts, and influence analysis.

## What Problem Does This Solve

Organizations fail at change management when they don't know who holds power, who cares about outcomes, and who needs to be kept in the loop. Without a structured approach to stakeholder analysis, critical decision-makers get blindsided, resistant influencers derail projects, and communications go to the wrong people in the wrong way. This skill provides frameworks for mapping organizational relationships before they bite you.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "Help me figure out who to involve in this initiative" | Power-Interest matrix to categorize stakeholders into Manage Closely, Keep Satisfied, Keep Informed, and Monitor quadrants |
| "Who is responsible for approving vs. doing this work?" | RACI chart template to assign Responsible, Accountable, Consulted, and Informed roles per task |
| "I need to plan communication for each stakeholder group" | Stakeholder template with influence/interest/attitude ratings and engagement strategy fields |
| "How do I prioritize which stakeholders need the most attention?" | Salience model ranking stakeholders by Power, Legitimacy, and Urgency combinations |
| "I need to map all the people impacted by this product launch" | Structured stakeholder inventory with engagement frequency, channel, and key messaging per person |
| "Some stakeholders are resistant — how do I handle them?" | Attitude classification (Supportive/Neutral/Resistant) with tailored engagement strategies |

## When NOT to Use This Skill

- creating individual user personas, empathy maps, or customer archetypes -- use [persona-definition](../persona-definition/) instead

## Installation

```bash
claude install-plugin github:viktorbezdek/skillstack/persona-mapping
```

## How to Use

**Direct invocation:**

```
Use the persona-mapping skill to ...
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `stakeholders`
- `raci`
- `influence-mapping`

## What's Inside

- **Power-Interest Matrix** -- A 2x2 grid (High/Low Power vs. High/Low Interest) that determines the right engagement strategy for each stakeholder quadrant.
- **RACI Matrix** -- Defines Responsible, Accountable, Consulted, and Informed roles per task, ensuring exactly one accountable person per decision.
- **Stakeholder Template** -- A structured profile capturing influence, interest, attitude, communication frequency, channel, and key messages for each stakeholder.
- **Salience Model** -- Prioritizes stakeholders by their combination of Power, Legitimacy, and Urgency attributes, from Definitive (all three) down to Latent (one attribute).

## Key Capabilities

- **Influence**
- **Interest**
- **Attitude**
- **Frequency**
- **Channel**
- **Key messages**

## Version History

- `1.0.10` fix(personas): disambiguate persona-definition vs persona-mapping (a5f9c9d)
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

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 49 production-grade plugins for Claude Code.
