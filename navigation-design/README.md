# Navigation Design

> **v1.0.10** | Design & UX | 11 iterations

Design information architecture, wayfinding systems, breadcrumbs, and navigation patterns for documentation and applications.

## What Problem Does This Solve

Users abandon products and documentation when they cannot find what they need — not because content is missing, but because the structure is unclear, menus are overloaded, or there is no indication of where the user currently is. Poor information architecture forces users to memorize paths instead of recognizing options. This skill provides the structural patterns, rules-of-thumb, and concrete templates for building navigation systems that guide users to their destination without friction.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "How should I structure the navigation for my documentation site?" | Hierarchy (tree), hub-and-spoke, flat, and faceted IA patterns with decision guidance on when each fits |
| "My top nav has too many items and users are getting lost" | The 7±2 rule, global/local/contextual/utility navigation type distinctions, and menu structure patterns |
| "How do I add breadcrumbs to my app?" | Breadcrumb template with clickable-except-current-page convention |
| "I need to create a sitemap for a new product" | Sitemap template covering primary and utility navigation structure |
| "Users can't tell where they are in my app" | Current location indicator patterns and the Recognition over Recall navigation principle |
| "What navigation mistakes should I avoid?" | Anti-patterns catalogue: mystery meat labels, deep nesting, inconsistent placement, missing location indicators |

## Installation

```bash
claude install-plugin github:viktorbezdek/skillstack/navigation-design
```

## How to Use

**Direct invocation:**

```
Use the navigation-design skill to ...
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `navigation`
- `information-architecture`
- `wayfinding`

## What's Inside

- **Navigation Types** -- Reference table of global, local, contextual, utility, and breadcrumb navigation with use cases and examples
- **Information Architecture Patterns** -- Four structural models (hierarchy/tree, hub-and-spoke, flat, faceted) with diagrams showing when each applies
- **Navigation Rules** -- Four core rules (7±2, 3-click, Recognition over Recall, Consistency) with descriptions
- **Breadcrumb Template** -- Ready-to-use breadcrumb trail pattern with the clickable-except-current-page convention
- **Sitemap Template** -- Markdown sitemap scaffold covering primary and utility navigation sections
- **Anti-Patterns** -- Four common navigation failures that break user orientation and how to recognize them

## Version History

- `1.0.10` fix(docs+quality): optimize descriptions for api-design, docs, edge-cases, examples, navigation, standards (6e315cf)
- `1.0.9` fix: update plugin count and normalize footer in 31 original plugin READMEs (3ea7c00)
- `1.0.8` fix: change author field from string to object in all plugin.json files (bcfe7a9)
- `1.0.7` fix: rename all claude-skills references to skillstack (19ec8c4)
- `1.0.6` docs: update README and install commands to marketplace format (af9e39c)
- `1.0.5` refactor: restructure all 34 skills into proper Claude Code plugin format (7922579)
- `1.0.4` refactor: make each skill an independent plugin with own plugin.json (6de4313)
- `1.0.3` docs: add detailed README documentation for all 34 skills (7ba1274)
- `1.0.2` refactor: standardize frontmatter and split oversized SKILL.md files (4a21a62)
- `1.0.1` docs: improve helper skill descriptions and add trigger words (9c0d140)

## Related Skills

- **[Content Modelling](../content-modelling/)** -- Design content models with types, fields, relationships, and governance rules for structured content systems.
- **[Elicitation](../elicitation/)** -- Psychological profiling through natural conversation using narrative identity, self-defining memory elicitation, Motivat...
- **[Ontology Design](../ontology-design/)** -- Design knowledge models with classes, properties, relationships, and taxonomies for structured data representation.
- **[Persona Definition](../persona-definition/)** -- Create detailed user personas with demographics, goals, pain points, behaviors, and empathy maps.
- **[Persona Mapping](../persona-mapping/)** -- Map stakeholders and personas using Power-Interest matrices, RACI charts, and influence analysis.

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 50 production-grade plugins for Claude Code.
