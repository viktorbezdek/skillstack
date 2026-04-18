---
name: content-modelling
description: Design CMS content models — content types, fields, editorial workflows, governance rules, and COPE (Create Once, Publish Everywhere) patterns — for structured, multi-channel publishing. Use when the user asks to design a content model, define content types in a CMS, structure fields for editorial content, plan a headless CMS architecture, or design content reuse across channels. NOT for formal knowledge graphs, OWL/RDF ontologies, or semantic modeling (use ontology-design). NOT for naming conventions or taxonomy standards across code (use consistency-standards).
---

# Content Modelling

Design structured content models for reusable, multi-channel content.

## When to Use / Not Use

**Use when:**
- Designing a CMS schema for a new project
- Defining content types with fields, constraints, and relationships
- Planning editorial workflows (draft, review, publish, archive)
- Building multi-channel content systems (web, mobile, email, API)
- Migrating from page-based to structured content models
- Establishing naming conventions for content types and fields

**Do NOT use when:**
- Building formal ontologies with classes, properties, and inference rules -> use `ontology-design`
- Standardizing naming conventions across code and documentation -> use `consistency-standards`
- Designing API schemas and endpoints -> use `api-design`

## Decision Tree

```
What are you modeling?
├── CMS content types (what fields, what relationships)
│   ├── New system? -> Start with content inventory, then type design (§Field Types, §Relationship Types)
│   └── Existing system with problems? -> Audit for anti-patterns first (§Anti-Patterns)
├── Multi-channel publishing (same content, different outputs)
│   └── Need COPE? -> Use semantic fields, not layout fields (§Design Principles)
├── Editorial workflow (who reviews, when, how)
│   └── Need lifecycle model? -> Define status enum + transition rules (§Content Model Template)
├── Terminology standardization (what to call things)
│   └── Naming conventions only? -> Use `consistency-standards` instead
└── Formal knowledge model with reasoning?
    └── Use `ontology-design` instead
```

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

### Relationship Decision Guide

| Question | If Yes | If No |
|----------|--------|-------|
| Does the related content exist independently? | Use Reference | Use Embedded |
| Will it be edited in one place and propagate? | Use Reference | Use Embedded |
| Is it a tree structure? | Use Hierarchical | — |

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

| Anti-Pattern | Problem | Solution |
|---|---|---|
| Page-based models | Content tied to specific layouts; cannot reuse across channels | Redesign with semantic fields; remove all layout-specific fields (heroImage position, sidebar width) from content types |
| HTML in rich text fields | Content renders incorrectly on mobile or in email; mixes content with presentation | Enforce rich text fields as semantic markup only; strip layout HTML in migration; use structured blocks |
| Monolithic content type | One "General Content" type with 40 optional fields; authors confused about which to fill | Decompose into specific types based on field usage analysis; each type gets only its relevant fields |
| Redundant fields | Same data in multiple places; drift on updates | Single-source via references or variables; if data changes, update once |
| Missing lifecycle | Content jumps from draft to published with no review; stale content never archived | Add status enum with transition rules and required review steps |
| Presentation in model | `heroImage` on a Guide type that not all channels render | Move to separate MediaAsset reference; rendering layer decides what to show |
