# Content Modelling

> **v1.0.11** | Design & UX | 12 iterations

Design content models with types, fields, relationships, and governance rules for structured content systems.

## What Problem Does This Solve

CMS implementations built around page-based models lock content to specific layouts, making multi-channel delivery (web, mobile, email, API) expensive to retrofit. Monolithic content types accumulate redundant fields, embed HTML directly in structured data, and resist reuse — requiring editors to duplicate content across entries that drift out of sync. This skill provides the field types, relationship patterns, naming conventions, and COPE (Create Once, Publish Everywhere) principles needed to design structured content models that are channel-agnostic and reusable from the start.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "I need to model a blog with posts, authors, and categories in a headless CMS" | Content type template with field definitions, relationship types (reference vs embedded vs hierarchical), cardinality, and validation rules |
| "What field type should I use for an article body vs a page title vs a publish date?" | Field type reference table covering short text, long text, rich text, number, boolean, date, media, reference, and enum with use cases |
| "How do I connect my Article content type to an Author type without duplicating data?" | Reference relationship pattern with independent existence and ID-based linking explained with structural diagrams |
| "We're building for web now but need to reuse content on mobile and in emails later" | COPE principle applied to field design: semantic fields over layout fields, atomic content units, presentation-agnostic structure |
| "What naming conventions should we use for content types and fields in our CMS?" | Naming convention table: PascalCase for types, camelCase for fields, kebab-case for slugs |
| "Our content model has grown into a mess — what went wrong?" | Anti-pattern catalog covering page-based models, HTML in fields, monolithic types, and redundant fields with structural consequences |

## When NOT to Use This Skill

- formal ontologies, taxonomies, or semantic modeling -- use [ontology-design](../ontology-design/) instead

## Installation

```bash
claude install-plugin github:viktorbezdek/skillstack/content-modelling
```

## How to Use

**Direct invocation:**

```
Use the content-modelling skill to ...
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `content`
- `cms`
- `schema`
- `modelling`

## What's Inside

- **Core Concepts** -- Definitions of Content Type, Field, Relationship, and Instance as the four foundational building blocks of any structured content model
- **Field Types** -- Reference table of nine field types (short text through enum) with use cases and concrete examples for each
- **Relationship Types** -- Three relationship patterns — linked reference (independent existence), embedded (nested ownership), and hierarchical (parent-child) — with structural diagrams
- **Content Model Template** -- Ready-to-use markdown template covering overview attributes, fields table, relationships table, and validation rules for any content type
- **Naming Conventions** -- Three-rule table: PascalCase for types, camelCase for fields, kebab-case for slugs
- **Design Principles** -- COPE (Create Once, Publish Everywhere) and atomic content principles with rationale for separating content from presentation
- **Anti-Patterns** -- Four structural mistakes (page-based models, HTML in fields, monolithic types, redundant fields) with descriptions of why each fails at scale

## Key Capabilities

- **Page-based models**
- **HTML in fields**
- **Monolithic types**
- **Redundant fields**

## Version History

- `1.0.11` fix(structured-data): disambiguate ontology-design vs content-modelling (beb7c2e)
- `1.0.10` fix: update plugin count and normalize footer in 31 original plugin READMEs (3ea7c00)
- `1.0.9` fix: change author field from string to object in all plugin.json files (bcfe7a9)
- `1.0.8` fix: rename all claude-skills references to skillstack (19ec8c4)
- `1.0.7` refactor: remove old file locations after plugin restructure (a26a802)
- `1.0.6` docs: update README and install commands to marketplace format (af9e39c)
- `1.0.5` refactor: restructure all 34 skills into proper Claude Code plugin format (7922579)
- `1.0.4` refactor: make each skill an independent plugin with own plugin.json (6de4313)
- `1.0.3` docs: add detailed README documentation for all 34 skills (7ba1274)
- `1.0.2` refactor: standardize frontmatter and split oversized SKILL.md files (4a21a62)

## Related Skills

- **[Elicitation](../elicitation/)** -- Psychological profiling through natural conversation using narrative identity, self-defining memory elicitation, Motivat...
- **[Navigation Design](../navigation-design/)** -- Design information architecture, wayfinding systems, breadcrumbs, and navigation patterns for documentation and applicat...
- **[Ontology Design](../ontology-design/)** -- Design knowledge models with classes, properties, relationships, and taxonomies for structured data representation.
- **[Persona Definition](../persona-definition/)** -- Create detailed user personas with demographics, goals, pain points, behaviors, and empathy maps.
- **[Persona Mapping](../persona-mapping/)** -- Map stakeholders and personas using Power-Interest matrices, RACI charts, and influence analysis.

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 50 production-grade plugins for Claude Code.
