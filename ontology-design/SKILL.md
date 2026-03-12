---
name: ontology-design
description: Design knowledge models with classes, properties, relationships, and taxonomies for structured data representation.
triggers:
  - ontology
  - taxonomy
  - knowledge model
  - semantic modeling
  - class hierarchy
  - entity relationships
---

# Ontology Design

Model domain knowledge through classes, properties, and relationships.

## Core Components

| Component | Purpose | Example |
|-----------|---------|---------|
| Class | Category of things | `Person`, `Product` |
| Property | Attribute of class | `name`, `price` |
| Relationship | Connection between classes | `owns`, `partOf` |
| Instance | Specific entity | `John`, `iPhone15` |

## Relationship Types

| Type | Notation | Example |
|------|----------|---------|
| Is-a (inheritance) | `subClassOf` | Dog is-a Animal |
| Has-a (composition) | `hasPart` | Car has-a Engine |
| Uses (association) | `uses` | Person uses Tool |
| Instance-of | `type` | Fido instance-of Dog |

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
| Relation | Target | Cardinality |
|----------|--------|-------------|
| belongsTo | Category | many-to-one |
| contains | Item | one-to-many |
```

## Design Principles

- **MECE**: Mutually exclusive, collectively exhaustive
- **Single inheritance preferred**: Avoid diamond problem
- **Normalize**: Reduce redundancy
- **Domain-driven**: Match real-world concepts

## Anti-Patterns

- God class (too many responsibilities)
- Orphan classes (no relationships)
- Circular dependencies
- Over-abstraction

