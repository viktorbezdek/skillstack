# Ontology Design

> **v1.0.10** | Design & UX | 11 iterations

Design knowledge models with classes, properties, relationships, and taxonomies for structured data representation.

## What Problem Does This Solve

Complex domains contain entities that relate to each other in structured ways -- inheritance hierarchies, composition relationships, type systems -- but without a formal model these structures are implicit, inconsistently applied, and hard to query or reason over. Teams end up with ad-hoc data models that grow into "god class" messes with circular dependencies and orphaned entities. Fields get duplicated across types because nobody documented the shared abstraction. This skill provides the vocabulary, design templates, relationship type reference, and principles needed to build rigorous, reusable knowledge models before implementation begins.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "I need to model the domain entities and their relationships for my system" | Class/property/relationship/instance component definitions with a structured design template |
| "How do I represent inheritance between domain concepts?" | Four relationship types: is-a (subClassOf), has-a (hasPart), uses (association), and instance-of with notation and examples |
| "I'm designing a taxonomy -- what levels and structure should I use?" | Taxonomy level hierarchy from Kingdom through Species as a structural model to adapt for any classification system |
| "My domain model has gotten messy with overlapping responsibilities" | MECE principle, single-inheritance guidance, and four anti-patterns to identify and fix |
| "How should I document a class with its properties and relationships?" | Markdown class template with property table (name/type/required/description) and relationship table (relation/target/cardinality) |

## When NOT to Use This Skill

- CMS content types, editorial workflows, or structured content for publishing -- use [content-modelling](../content-modelling/) instead

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install ontology-design@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention the triggers below, or you can invoke it explicitly.

## How to Use

**Direct invocation:**

```
Use the ontology-design skill to model the entity relationships for my e-commerce domain
```

```
Use the ontology-design skill to design a taxonomy for our product catalog
```

```
Use the ontology-design skill to audit my domain model for anti-patterns
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

`ontology` · `knowledge-models` · `taxonomies`

## What's Inside

### Skill: ontology-design

Single-skill plugin with no reference files -- all content is in the main SKILL.md.

| Component | Description |
|---|---|
| **SKILL.md** | Complete ontology design guide covering four core components, four relationship types, taxonomy levels, class design template, four design principles, and four anti-patterns |
| **evals/** | Trigger evaluation and output quality evaluation test suites |

### Key content areas

- **Core Components** -- Reference table defining Class (category of things), Property (attribute of class), Relationship (connection between classes), and Instance (specific entity) with concrete examples like `Person`, `Product`, `owns`, `partOf`
- **Relationship Types** -- Four relationship types with notation and examples: is-a/subClassOf (Dog is-a Animal), has-a/hasPart (Car has-a Engine), uses/association (Person uses Tool), instance-of/type (Fido instance-of Dog)
- **Taxonomy Levels** -- Hierarchical taxonomy structure from Kingdom through Species as a template for designing any classification system
- **Design Template** -- Ready-to-fill markdown class definition with description, parent class, property table (name/type/required/description columns), and relationship table (relation/target/cardinality columns)
- **Design Principles** -- Four guiding principles: MECE (mutually exclusive, collectively exhaustive), single inheritance preferred (avoid diamond problem), normalize (reduce redundancy), domain-driven (match real-world concepts)
- **Anti-Patterns** -- Four structural problems: god class (too many responsibilities), orphan classes (no relationships), circular dependencies, and over-abstraction

## Usage Scenarios

1. **Designing a domain model for a new application.** Start with the core components table to identify your classes, properties, and relationships. Use the design template to document each class with its property table and relationship table, applying the MECE principle to ensure categories don't overlap and collectively cover the domain.

2. **Building a product taxonomy for an e-commerce platform.** The taxonomy levels section provides the structural model. Adapt the Kingdom-to-Species hierarchy to your product categories (e.g., Department > Category > Subcategory > Product Type), using the is-a relationship type for inheritance between levels.

3. **Auditing an existing data model that has become unwieldy.** Run through the four anti-patterns checklist: is any class carrying too many responsibilities (god class)? Are there classes with no relationships to anything (orphans)? Do relationships form cycles (circular dependencies)? Are there abstract classes that add layers without value (over-abstraction)?

4. **Documenting entity relationships for a team handoff.** The design template provides a standardized format that any developer can read: class name, description, parent class, property table with types and required flags, and relationship table with cardinalities. This eliminates the ad-hoc documentation that drifts from implementation.

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

- **[Content Modelling](../content-modelling/)** -- CMS content types and editorial workflows that use ontology concepts for structured publishing
- **[Navigation Design](../navigation-design/)** -- Information architecture that exposes ontology structure to users
- **[Persona Definition](../persona-definition/)** -- User personas whose mental models should align with the ontology
- **[Systems Thinking](../systems-thinking/)** -- Systems analysis that complements entity-relationship modeling with feedback loops and dynamics
- **[Api Design](../api-design/)** -- API design that exposes ontology entities as resources and endpoints

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 50 production-grade plugins for Claude Code.
