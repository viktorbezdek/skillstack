# Content Modelling

> Design content models with types, fields, relationships, and governance rules for structured content systems.

## Overview

Content trapped in page-based layouts cannot be reused, repurposed, or delivered across channels. When content is modelled as structured types with defined fields and relationships, it becomes a strategic asset -- publishable to websites, apps, APIs, and emerging platforms from a single source. This skill provides the frameworks and patterns to design content models that scale.

The Content Modelling skill covers the full lifecycle of structured content architecture: defining content types with appropriate field types (short text, rich text, references, enums), establishing relationships between types (reference, embedded, hierarchical), applying the COPE principle (Create Once, Publish Everywhere), and following atomic content design to eliminate duplication. It includes templates for documenting content types with their fields, constraints, validation rules, and lifecycle states.

Within the SkillStack collection, this skill connects directly to API Design (content models drive API schemas), Consistency Standards (uniform naming for types and fields), and Creative Problem-Solving (innovative approaches to content architecture challenges).

## What's Included

### References
- `api_reference.md` -- Reference documentation template for content modelling APIs and workflows

### Scripts
- `example.py` -- Example helper script placeholder for content modelling automation

### Assets
- `example_asset.txt` -- Asset file placeholder for templates, images, and data files

Note: This skill's primary value is in the comprehensive content modelling framework defined in `SKILL.md`, which includes type definitions, field type catalogs, relationship patterns, naming conventions, and design principles.

## Key Features

- **Content type design**: Templates for defining types with purpose, cardinality, lifecycle, fields, and relationships
- **Field type catalog**: Nine core field types (short text, long text, rich text, number, boolean, date, media, reference, enum) with use cases
- **Relationship patterns**: Reference (linked), embedded (nested), and hierarchical (parent-child) relationship types
- **COPE principle**: Create Once, Publish Everywhere -- separate content from presentation for multi-channel delivery
- **Atomic content design**: Break content into smallest reusable units, compose complex structures from atoms
- **Naming conventions**: PascalCase for types, camelCase for fields, kebab-case for slugs
- **Validation rules**: Field constraints, uniqueness requirements, and conditional validation based on lifecycle state
- **Anti-pattern detection**: Identifies page-based models, HTML in fields, monolithic types, and redundant fields

## Usage Examples

**Design a content model for a blog:**
```
Design a structured content model for a blog with articles,
authors, categories, and tags. Include all field definitions,
relationships, and validation rules.
```
Expected output: Content type definitions for Article, Author, Category, and Tag with field specifications (type, required, constraints), relationship mappings (Article references Author, Category; tags as many-to-many), and validation rules (slug uniqueness, required publishedAt when status is published).

**Model an e-commerce product catalog:**
```
Create a content model for a product catalog with products,
variants, categories, and reviews. Support multi-channel publishing.
```
Expected output: Structured type definitions following COPE principles, with Product as the core type containing embedded Variant types, reference relationships to Category and Brand, and a separate Review type with back-references. Fields are semantic (not layout-based) to support web, mobile, and API delivery.

**Migrate from page-based to structured content:**
```
Our CMS currently has monolithic page types with HTML in fields.
Help us redesign this as a structured content model.
```
Expected output: Analysis of the existing page-based model, identification of embedded content patterns that should be extracted into separate types, a proposed type hierarchy following atomic content principles, and a migration strategy.

**Define content governance rules:**
```
Define governance rules for our content model including lifecycle
states, ownership, validation, and archival policies.
```
Expected output: Lifecycle state definitions (draft, review, published, archived), ownership and permission rules per content type, field-level validation constraints, and automated archival policies with criteria.

**Create a multi-channel content architecture:**
```
Design a content architecture that can serve our website, mobile
app, and third-party API consumers from a single content source.
```
Expected output: Channel-agnostic content types using semantic fields (no layout fields like "sidebar_content"), delivery-layer transformation rules for each channel, and a reference architecture showing how content flows from CMS to each consumer.

## Quick Start

1. **Identify your content** -- List all distinct types of content your system manages
2. **Define content types** -- Use the content model template in SKILL.md to document each type
3. **Choose field types** -- Map each piece of data to the appropriate field type from the catalog
4. **Establish relationships** -- Determine whether connections should be reference, embedded, or hierarchical
5. **Apply COPE** -- Ensure all fields are semantic (what it is) not presentational (where it goes)
6. **Add validation rules** -- Define constraints, required fields, and conditional rules
7. **Review for anti-patterns** -- Check for page-based models, HTML in fields, and duplication

## Related Skills

- **[API Design](../api-design/)** -- Content models define the schemas your APIs will expose
- **[Consistency Standards](../consistency-standards/)** -- Apply uniform naming to content types and fields
- **[Creative Problem-Solving](../creative-problem-solving/)** -- Find innovative solutions to content architecture challenges

---

Part of [SkillStack](https://github.com/viktorbezdek/claude-skills) — `/plugin install content-modelling@claude-skills` -- 34 production-grade skills for Claude Code.
