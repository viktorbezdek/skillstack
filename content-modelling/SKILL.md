---
name: content-modelling
description: Design content models with types, fields, relationships, and governance rules for structured content systems. Use when designing CMS schemas, defining content types, planning content reuse, or architecting headless content systems. Triggers include content model, content type, structured content, CMS schema, content architecture, and COPE (Create Once Publish Everywhere).
---

# Content Modelling

Design structured content models for reusable, multi-channel content.

## Core Concepts

| Concept | Definition |
|---------|------------|
| **Content Type** | Template defining structure for similar content |
| **Field** | Single data element within a content type |
| **Relationship** | Connection between content types |
| **Instance** | Specific piece of content based on a type |

## Field Types

| Type | Use Case | Example |
|------|----------|---------|
| Short text | Titles, labels | "Getting Started" |
| Long text | Descriptions | Paragraph content |
| Rich text | Formatted content | Bold, links, lists |
| Number | Quantities | `42` |
| Boolean | Toggles | `true` |
| Date | Timestamps | `2024-01-15` |
| Media | Images, files | `hero.png` |
| Reference | Links to other content | → Author |
| Enum | Fixed choices | `draft|published` |

## Relationship Types

### Reference (Linked)
Content exists independently, linked by ID.
```
Article → Author (reference)
         └─ Author can be edited separately
```

### Embedded
Content nested within parent.
```
Article ⊃ SEO Metadata (embedded)
          └─ Metadata only exists in this article
```

### Hierarchical
Parent-child relationships.
```
Documentation
├── Getting Started
│   ├── Installation
│   └── Configuration
└── API Reference
```

## Content Model Template

```markdown
## Content Type: [Name]

### Overview
| Attribute | Value |
|-----------|-------|
| **Purpose** | [what this type represents] |
| **Cardinality** | [expected instance count] |
| **Lifecycle** | [draft → review → published] |

### Fields
| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| title | Short text | Yes | Max 100 chars |
| slug | Short text | Yes | URL-safe, unique |
| body | Rich text | Yes | - |
| author | Reference | Yes | → Author |
| status | Enum | Yes | draft/published |

### Relationships
| Relation | Type | Target | Cardinality |
|----------|------|--------|-------------|
| author | Reference | Author | 1:1 |
| category | Reference | Category | Many:1 |

### Validation Rules
- `slug` must be unique within parent
- `publishedAt` required when `status = published`
```

## Naming Conventions

| Element | Convention | Example |
|---------|------------|---------|
| Types | PascalCase | `BlogPost` |
| Fields | camelCase | `publishedAt` |
| Slugs | kebab-case | `getting-started` |

## Design Principles

### COPE: Create Once, Publish Everywhere
- Separate content from presentation
- Use semantic fields, not layout fields
- Enable multi-channel delivery

### Atomic Content
- Break content into smallest reusable units
- Compose complex content from atoms
- Avoid duplication

## Anti-Patterns

- **Page-based models**: Tying content to specific pages
- **HTML in fields**: Mixing content with presentation
- **Monolithic types**: One type for everything
- **Redundant fields**: Same data in multiple places
