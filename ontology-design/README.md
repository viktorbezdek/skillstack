# Ontology Design

> Design knowledge models with classes, properties, relationships, and taxonomies for structured data representation.

## Overview

Every software system embeds a model of the world, whether it is explicitly designed or accidentally accumulated. Ontology Design provides the vocabulary and methodology to make that model intentional. This skill covers the core building blocks of knowledge modeling -- classes, properties, relationships, and instances -- and shows how to assemble them into coherent, maintainable domain models.

The skill emphasizes practical design over academic formalism. It provides ready-to-use templates for defining classes and their relationships, enumerates the fundamental relationship types (is-a, has-a, uses, instance-of), and encodes design principles like MECE (mutually exclusive, collectively exhaustive) and single inheritance preference. It also catalogs anti-patterns such as god classes, orphan classes, and circular dependencies.

Within the SkillStack collection, Ontology Design is the foundational modeling skill. It underpins navigation design (the taxonomy drives the navigation hierarchy), persona definition (user types form an ontology), and MCP server development (the domain model determines what tools expose).

## What's Included

This skill is a single-file skill contained entirely in `SKILL.md`. It provides:

- Core component taxonomy (Class, Property, Relationship, Instance)
- Relationship type reference (Is-a, Has-a, Uses, Instance-of)
- Taxonomy hierarchy template
- Class design template with properties and relationships
- Design principles (MECE, single inheritance, normalization, domain-driven)
- Anti-pattern catalog

## Key Features

- Four core ontology components defined with purpose and examples
- Four relationship types with notation and real-world examples
- Taxonomy hierarchy diagram from Kingdom to Species (adaptable to any domain)
- Ready-to-use class definition template with properties table and relationship table
- Cardinality specification for relationships (one-to-one, one-to-many, many-to-one, many-to-many)
- Design principles that prevent common modeling mistakes
- Anti-pattern identification for early detection of structural problems

## Usage Examples

**Model a domain from scratch:**
```
Design an ontology for an e-commerce platform. Define classes for Product, Category, Customer, Order, and Review. Specify properties, relationships with cardinality, and inheritance hierarchies.
```

**Refactor an existing data model:**
```
Our database has grown organically and has redundant tables and unclear relationships. Analyze the schema and propose a clean ontology with proper inheritance, normalized properties, and explicit relationship types.
```

**Create a taxonomy for content classification:**
```
Design a taxonomy for classifying technical documentation. We need categories for tutorials, guides, API references, changelogs, and troubleshooting articles. Apply MECE principles to ensure completeness without overlap.
```

**Validate a class hierarchy:**
```
Review this class hierarchy for anti-patterns. Check for god classes with too many responsibilities, orphan classes with no relationships, circular dependencies, and over-abstraction.
```

**Map domain concepts to API resources:**
```
We have this domain ontology for a project management tool. Map each class to REST API resources, determine which properties become fields vs. embedded objects vs. linked resources, and specify the relationship endpoints.
```

## Quick Start

1. **Identify domain concepts** -- List the key entities in your domain (nouns that matter to your business).

2. **Define classes** -- Use the class template to document each entity with its description, parent class, properties (name, type, required, description), and relationships (relation, target, cardinality).

3. **Establish relationships** -- Choose the correct relationship type for each connection: is-a for inheritance, has-a for composition, uses for association, instance-of for concrete entities.

4. **Apply MECE** -- Verify that sibling classes at each level of the hierarchy are mutually exclusive and collectively exhaustive.

5. **Check for anti-patterns** -- Scan for god classes, orphan classes, circular dependencies, and over-abstraction.

6. **Iterate with stakeholders** -- Domain models are living artifacts. Revisit as requirements evolve.

## Related Skills

- **navigation-design** -- Turn your taxonomy into a navigation hierarchy
- **persona-definition** -- User types form their own ontology; model them rigorously
- **persona-mapping** -- Map stakeholder relationships using ontology thinking
- **mcp-server** -- Domain models determine what tools your MCP server exposes
- **outcome-orientation** -- Align your ontology with measurable business outcomes

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) — `/plugin install ontology-design@skillstack` — 46 production-grade plugins for Claude Code.
