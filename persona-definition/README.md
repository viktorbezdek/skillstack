# Persona Definition

> **v1.0.10** | Design & UX | 11 iterations

Create detailed user personas with demographics, goals, pain points, behaviors, and empathy maps.

## What Problem Does This Solve

Product and documentation decisions made without a concrete mental model of the user default to the builder's own assumptions — which rarely match actual users. Without defined personas, teams argue about hypothetical users, over-build for edge cases, and write documentation at the wrong level of technical depth. This skill provides the templates and component breakdown for creating research-backed personas that give teams a shared, specific picture of who they are designing for.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "We need to define who our target user is before we start designing" | Persona type selection (proto, lean, full) based on fidelity needs, plus a structured persona template |
| "Help me create a persona for a developer audience" | Core components breakdown: demographics, goals (primary/secondary/experience), pain points, behaviors, and context |
| "I need to understand what my users think and feel, not just what they do" | Empathy map template (Says/Thinks/Does/Feels quadrant) |
| "How detailed should our personas be for an MVP?" | Three persona type trade-offs: proto-persona for quick alignment, lean for agile/MVP, full for strategic decisions |
| "We built personas before but they just sit in a doc and nobody uses them" | Anti-patterns section covering aspirational personas, persona overload (>5), demographic-only personas, and stale personas |
| "What information should a good persona capture?" | Five core component checklist: demographics, goals, pain points, behaviors, and environment/device/constraint context |

## When NOT to Use This Skill

- mapping stakeholders across organizations, RACI charts, or influence analysis -- use [persona-mapping](../persona-mapping/) instead

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install persona-definition@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention the triggers below, or you can invoke it explicitly.

## How to Use

**Direct invocation:**

```
Use the persona-definition skill to ...
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `personas`
- `user-research`
- `empathy-maps`

## What's Inside

- **Persona Types** -- Three fidelity levels (proto, lean, full) with purpose and detail requirements for each
- **Core Components** -- Five building blocks every persona needs: demographics, goals, pain points, behaviors, and context
- **Empathy Map** -- Four-quadrant template (Says/Thinks/Does/Feels) for capturing the inner experience behind observable behavior
- **Persona Template** -- Ready-to-fill markdown template with attribute table, goals section, pain points list, and documentation needs
- **Anti-Patterns** -- Four persona failure modes that produce documents nobody acts on: aspirational personas, too many personas, demographic-only, and static/never-updated

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
- **[Persona Mapping](../persona-mapping/)** -- Map stakeholders and personas using Power-Interest matrices, RACI charts, and influence analysis.

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 50 production-grade plugins for Claude Code.
