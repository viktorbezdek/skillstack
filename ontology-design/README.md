# Ontology Design

> **v1.0.10** | Design & UX | 11 iterations

Design knowledge models with classes, properties, relationships, and taxonomies for structured data representation.

## What Problem Does This Solve

Complex domains contain entities that relate to each other in structured ways — inheritance hierarchies, composition relationships, type systems — but without a formal model these structures are implicit, inconsistently applied, and hard to query or reason over. Ad-hoc data models grow into "god class" messes with circular dependencies and orphaned entities. This skill provides the vocabulary, design templates, and principles needed to build rigorous, reusable knowledge models before implementation begins.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "I need to model the domain entities and their relationships for my system" | Class/property/relationship/instance component definitions with a structured design template |
| "How do I represent inheritance between domain concepts?" | Is-a (subClassOf), has-a (hasPart), uses (association), and instance-of relationship type reference |
| "I'm designing a taxonomy — what levels and structure should I use?" | Taxonomy level hierarchy from Kingdom through Species as a structural model to adapt |
| "My domain model has gotten messy with overlapping responsibilities" | MECE principle, single-inheritance guidance, and the four anti-patterns to identify and fix |
| "How should I document a class with its properties and relationships?" | Markdown class template with property table (name/type/required/description) and relationship table (relation/target/cardinality) |
| "What makes a good ontology vs a bad one?" | Design principles (MECE, normalize, domain-driven) and anti-patterns (god class, orphan classes, circular dependencies, over-abstraction) |

## When NOT to Use This Skill

- CMS content types, editorial workflows, or structured content for publishing -- use [content-modelling](../content-modelling/) instead

## Installation

```bash
claude install-plugin github:viktorbezdek/skillstack/ontology-design
```

## How to Use

**Direct invocation:**

```
Use the ontology-design skill to ...
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `ontology`
- `knowledge-models`
- `taxonomies`

## What's Inside

- **Core Components** -- Reference table of Class, Property, Relationship, and Instance with purpose and concrete examples
- **Relationship Types** -- Four relationship types (is-a, has-a, uses, instance-of) with notation and examples
- **Taxonomy Levels** -- Hierarchical taxonomy structure from Kingdom to Species as a template for any classification system
- **Design Template** -- Markdown class definition template with property table and relationship table ready to fill in
- **Design Principles** -- Four guiding principles: MECE, single inheritance, normalization, and domain-driven modeling
- **Anti-Patterns** -- Four structural problems that degrade ontology quality: god class, orphan classes, circular dependencies, and over-abstraction

## Version History

- `1.0.10` fix(structured-data): disambiguate ontology-design vs content-modelling (beb7c2e)
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
- **[Navigation Design](../navigation-design/)** -- Design information architecture, wayfinding systems, breadcrumbs, and navigation patterns for documentation and applicat...
- **[Persona Definition](../persona-definition/)** -- Create detailed user personas with demographics, goals, pain points, behaviors, and empathy maps.
- **[Persona Mapping](../persona-mapping/)** -- Map stakeholders and personas using Power-Interest matrices, RACI charts, and influence analysis.

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 49 production-grade plugins for Claude Code.
