---
name: ontology-design
description: Design formal knowledge models — classes, properties, relationships, hierarchies, and semantic graphs — for knowledge representation and reasoning. Use when the user asks to build an ontology, design a knowledge graph, model entity relationships formally, define class hierarchies, create a taxonomy for semantic reasoning, or structure data for RDF/OWL. NOT for CMS content types, editorial workflows, or publishing structures (use content-modelling). NOT for naming conventions or terminology standards across docs (use consistency-standards).
---

# Ontology Design

Model domain knowledge through classes, properties, and relationships. An ontology is not a database schema — it encodes meaning, not just structure. A well-designed ontology enables reasoning (inferring new facts from existing ones), not just storage.

## When to Use

- Building a knowledge graph that requires formal class hierarchies
- Designing semantic models where relationships carry meaning (not just foreign keys)
- Creating taxonomies that enable automated reasoning or inference
- Modeling domains where "is-a" and "has-a" distinctions matter
- Structuring data for RDF/OWL or semantic web technologies
- Designing type systems where inheritance and composition have semantic weight

## When NOT to Use

- CMS content types, editorial workflows, or publishing structures (use content-modelling)
- Naming conventions or terminology standards across docs (use consistency-standards)
- Database schema design for CRUD applications (use database schema tools)
- API data models (use API design or TypeScript/Python type definitions)
- Simple key-value or document storage (no ontology needed)

## Decision Tree

```
What are you modeling?
│
├─ Entities with "is-a" relationships (inheritance)?
│  ├─ Need automated reasoning over the hierarchy? → Yes, ontology
│  └─ Just need type categories in code? → No, use enum/interface in code
│
├─ Relationships between entities with semantic meaning?
│  ├─ Need to infer new relationships? → Yes, ontology with reasoning
│  └─ Just need to join tables? → No, use database schema
│
├─ Taxonomy with formal classification?
│  ├─ Multiple inheritance or overlapping categories? → Yes, ontology
│  └─ Simple flat categories? → No, use tags or enums
│
├─ Need RDF/OWL/SPARQL?
│  └─ Yes → Ontology design (this skill)
│
└─ Not sure if ontology or schema
   ├─ Does "Dog is-a Animal" enable reasoning beyond code type checks? → Ontology
   └─ Just storing data with relationships? → Database schema
```

## Core Components

| Component | Purpose | Example |
|-----------|---------|---------|
| Class | Category of things | `Person`, `Product` |
| Property | Attribute of class | `name`, `price` |
| Relationship | Connection between classes | `owns`, `partOf` |
| Instance | Specific entity | `John`, `iPhone15` |
| Axiom | Rule that constrains interpretation | `Person ⊓ hasChild ≥ 1 → Parent` |

## Relationship Types

| Type | Notation | Example | Inverse |
|------|----------|---------|---------|
| Is-a (inheritance) | `subClassOf` | Dog is-a Animal | — |
| Has-a (composition) | `hasPart` | Car has-a Engine | `partOf` |
| Uses (association) | `uses` | Person uses Tool | `usedBy` |
| Instance-of | `type` | Fido instance-of Dog | — |
| Causes (causation) | `causes` | Smoking causes Disease | `causedBy` |

Always define inverse relationships where they exist. Missing inverses break traversal and reasoning.

## Taxonomy Levels

```
Kingdom
  └── Phylum
        └── Class
              └── Order
                    └── Family
                          └── Genus
                                └── Species
```

Rule: taxonomies deeper than 7 levels become unmaintainable. If you need more, consider faceted classification instead.

## Design Template

```markdown
## Class: [Name]

**Description**: [purpose]
**Parent**: [superclass]

### Properties
| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | yes | Unique identifier |
| name | string | yes | Display name |

### Relationships
| Relation | Target | Cardinality | Inverse |
|----------|--------|-------------|---------|
| belongsTo | Category | many-to-one | contains |
| contains | Item | one-to-many | belongsTo |
```

## Design Principles

- **MECE**: Mutually exclusive, collectively exhaustive
- **Single inheritance preferred**: Avoid diamond problem; use composition for shared behavior
- **Normalize**: Reduce redundancy; each fact stated once
- **Domain-driven**: Match real-world concepts, not implementation artifacts
- **Define inverses**: Every bidirectional relationship needs both directions
- **Constrain cardinality**: State minimum and maximum explicitly (1..*, 0..1, etc.)
- **Separate taxonomy from ontology**: Taxonomy classifies; ontology relates

## Anti-Patterns

| Anti-Pattern | Problem | Solution |
|---|---|---|
| God class (too many responsibilities) | Class becomes a catch-all; reasoning produces false inferences | Split into focused classes; use composition over inheritance |
| Orphan classes (no relationships) | Class exists in isolation; no reasoning possible | Connect via at least one relationship or place in hierarchy |
| Circular dependencies | A depends on B depends on A; reasoning loops | Break cycle by extracting shared concept into a third class |
| Over-abstraction | Generic classes like `Thing` or `Entity` add no semantic value | Only abstract when subclasses share meaningful properties |
| Missing inverses | Traversal works in one direction only; queries fail | Define inverse for every bidirectional relationship |
| Diamond inheritance | Class inherits from two parents that share an ancestor | Prefer single inheritance + composition; use mixins/traits if needed |
| Confusing is-a with has-a | "Car is-a Wheel" instead of "Car has-a Wheel" | Is-a = "every X is also a Y"; Has-a = "X contains Y as a part" |
| Modeling implementation, not domain | Classes mirror database tables or API endpoints | Model the domain concepts; map to implementation separately |
| Ignoring temporal aspects | "Person lives-at Address" with no time range | Add valid-from/valid-to for facts that change over time |

## Related Skills

- **content-modelling** — CMS content types, editorial workflows, publishing structures
- **consistency-standards** — Naming conventions and terminology standards
- **memory-systems** — Knowledge graph storage and retrieval for agents
