# Content Modelling

> **v1.0.11** | Design & UX | 12 iterations

> Design structured content models with content types, fields, relationships, editorial workflows, and COPE (Create Once, Publish Everywhere) patterns for CMS and content platform architecture.

## The Problem

Content teams build their CMS models by imitating their website structure. The "Homepage" content type has a "hero banner" field, a "featured section" field, and a "sidebar" field -- all tightly coupled to a specific page layout. When the business wants the same content on a mobile app, in an email newsletter, or on a partner site, the model cannot deliver it because the content is inseparable from its presentation.

The problems cascade. Blog posts duplicate author bios instead of referencing a shared Author type, so updating an author's title requires editing 200 posts. Product descriptions embed HTML formatting, so the content renders correctly on the website but breaks in the mobile app and email. The documentation section has no hierarchy model, so moving a page means updating hardcoded parent links across dozens of documents. And the editorial workflow is ad hoc -- some content types have draft/published states, others do not, and nobody can find content that was approved but never published.

Content modeling is the foundation that determines whether structured content is reusable, multi-channel, maintainable, and governable. Getting it wrong at the start means rebuilding the entire content architecture later -- a migration that typically takes months and disrupts every team that touches content.

## The Solution

This plugin provides the content modeling methodology: content types (templates defining structure), fields (nine typed data elements from short text to references), three relationship types (referenced, embedded, hierarchical) with cardinality rules, naming conventions (PascalCase for types, camelCase for fields, kebab-case for slugs), editorial workflow lifecycle (draft to review to published), validation rules, and COPE architecture for multi-channel delivery.

The skill enforces design principles that prevent the most common modeling mistakes: separate content from presentation (no layout fields), use semantic fields (not HTML), break content into atomic reusable units, and compose complex content from atoms rather than duplicating. It catches anti-patterns: page-based models, HTML in fields, monolithic types, and redundant data.

You describe your content domain -- "a documentation site with guides, API references, and changelogs" or "an e-commerce platform with products, categories, and reviews" -- and get a complete content model with typed fields, relationship diagrams, validation rules, naming conventions, and editorial workflows. The model is designed for multi-channel delivery from day one.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Page-based content types that mirror the website layout | Semantic content types designed for reuse across channels |
| Author bios duplicated in 200 blog posts | Shared Author type referenced by all content that needs it |
| HTML formatting embedded in content fields | Structured rich text with semantic markup, no presentation coupling |
| No content hierarchy -- parent-child relationships are hardcoded | Hierarchical relationship type with proper parent-child modeling |
| Ad hoc editorial status (some content has draft/published, some does not) | Consistent lifecycle (draft/review/published) across all content types |
| Content works on the website but breaks in mobile app and email | COPE architecture enabling multi-channel delivery from the same content |

## Installation

Add the SkillStack marketplace, then install:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install content-modelling@skillstack
```

### Verify Installation

After installing, test with:

```
Design a content model for a technical documentation site with guides, tutorials, and API references
```

The skill activates automatically when you mention content types, CMS schemas, content modeling, or structured content.

## Quick Start

1. Install the plugin using the commands above.
2. Describe your content domain:
   ```
   I need a content model for a product marketing site -- landing pages, blog posts, case studies, and a team directory
   ```
3. The skill produces content types with typed fields, relationships (Author referenced by posts and case studies, Category linked to posts), validation rules, and editorial workflow.
4. Refine the model:
   ```
   Add multi-language support and make the case studies reusable across landing pages
   ```
5. You get a complete model ready to implement in your CMS, with COPE patterns ensuring content works across web, mobile, and email channels.

## What's Inside

This is a focused single-skill plugin with the complete content modeling methodology in the SKILL.md body.

| Component | Purpose |
|---|---|
| **content-modelling** skill | Core methodology: content types, 9 field types, 3 relationship types (reference/embedded/hierarchical), content model template, naming conventions, COPE architecture, atomic content principles, editorial lifecycle, validation rules, 4 anti-patterns |

**Eval coverage:** 13 trigger eval cases + 3 output eval cases.

### How to Use: content-modelling

**What it does:** Guides you through designing structured content models for CMS platforms, documentation sites, e-commerce systems, and any application that manages structured content. Activates when you mention content types, CMS schemas, content architecture, editorial workflows, structured content, or multi-channel content delivery. Produces complete content models with typed fields, relationships, validation rules, and naming conventions.

**Try these prompts:**

```
Design a content model for a SaaS company website -- we need a blog, documentation, changelog, and team profiles
```

```
I'm building a headless CMS for our e-commerce platform -- model the product catalog with variants, categories, and reviews
```

```
Our content model is a mess -- we have one monolithic "Page" type for everything. Help me refactor into proper content types
```

```
How do I model hierarchical documentation with sections, pages, and sub-pages that can be reordered?
```

```
We need our content to work on web, mobile app, and email -- design the model following COPE principles
```

## Real-World Walkthrough

You are building a developer documentation platform for a SaaS product. The content includes getting-started guides, API reference pages, tutorials with code examples, a changelog, and a glossary. The platform needs to serve the same content on the website, in-product help tooltips, and a mobile companion app.

You start with the content domain analysis:

```
Design a content model for a developer documentation platform -- guides, API reference, tutorials, changelog, and glossary
```

The skill begins by identifying the content types and their relationships. It resists the temptation to create a single "Page" type -- that is the monolithic anti-pattern. Instead, it produces five distinct content types, each with semantic fields.

**Guide** is the primary content type for getting-started and conceptual documentation:

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| title | Short text | Yes | Max 100 chars |
| slug | Short text | Yes | URL-safe, unique within parent |
| body | Rich text | Yes | No HTML, semantic markup only |
| difficulty | Enum | Yes | beginner/intermediate/advanced |
| prerequisites | Reference | No | -> Guide (many) |
| relatedApis | Reference | No | -> ApiEndpoint (many) |
| status | Enum | Yes | draft/review/published |

The `prerequisites` field is a self-reference -- a guide can link to other guides the reader should complete first. The `relatedApis` field links to API reference content, creating cross-references that work in both directions.

**ApiEndpoint** models each API endpoint with structured fields:

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| method | Enum | Yes | GET/POST/PUT/PATCH/DELETE |
| path | Short text | Yes | Must start with / |
| description | Long text | Yes | - |
| parameters | Embedded | No | -> Parameter (many) |
| responseSchema | Long text | No | JSON Schema |
| codeExamples | Embedded | No | -> CodeExample (many) |

Parameters and code examples are **embedded** (not referenced) because they only exist in the context of their parent endpoint. They have no independent lifecycle. This is a key modeling decision -- the skill explains the difference between embedded (content nested within parent, no independent existence) and referenced (content exists independently, linked by ID).

**Tutorial** is similar to Guide but adds sequential structure:

```
Tutorial ⊃ Step (embedded, ordered)
           └─ Each step has: title, body, codeExample, expectedOutput
```

Steps are embedded and ordered because a tutorial's steps have no meaning outside the tutorial and must maintain their sequence.

**Changelog** uses a date-based structure:

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| version | Short text | Yes | Semantic version format |
| date | Date | Yes | - |
| entries | Embedded | Yes | -> ChangeEntry (many) |

Each ChangeEntry has a type (added/changed/fixed/removed), description, and optional link to related API or guide content.

**Glossary** is the simplest type: term (short text, unique), definition (long text), relatedTerms (self-reference), and usedIn (reference to Guide/Tutorial).

The hierarchical structure comes through a **Section** type:

```
Section
├── Getting Started (Guide instances)
│   ├── Installation
│   └── Configuration
├── API Reference (ApiEndpoint instances)
│   ├── Authentication
│   └── Resources
└── Tutorials (Tutorial instances)
```

Sections use the hierarchical relationship type with parent-child references and an `order` field for sorting. Moving a page to a different section means updating one parent reference, not rewriting links.

Now the multi-channel requirement:

```
Make this model work for in-product help tooltips and the mobile app, not just the web docs
```

The skill applies COPE principles. Every field is semantic (no "hero image width" or "sidebar content" fields). The body field uses structured rich text, not HTML. Code examples are separate embedded components with language metadata, so the mobile app can render them differently from the website. The glossary terms can be extracted as tooltip content by querying the API for the term definition.

For the mobile app, the same content model serves a different presentation: guides render as scrollable articles, API references render as expandable cards, and tutorials render as step-by-step wizards. No content duplication -- the headless CMS API serves the same structured content, and each client renders it appropriately.

The editorial workflow applies consistently: all content types follow draft/review/published lifecycle. Validation rules prevent publishing without required fields (e.g., `publishedAt` is required when status is `published`). The changelog type auto-populates the date field.

The complete model is ready to implement in Contentful, Strapi, Sanity, or any headless CMS. The naming conventions (PascalCase types, camelCase fields, kebab-case slugs) are consistent across all types. The relationship diagram shows how everything connects. And the COPE architecture ensures the content investment serves web, mobile, and in-product channels from day one.

## Usage Scenarios

### Scenario 1: Designing a CMS schema from scratch

**Context:** You are building a company website with a headless CMS and need to model the content before configuring the CMS platform.

**You say:** "Design the content model for our company website -- we need pages, blog posts, team members, case studies, and a careers section"

**The skill provides:**
- Five content types with typed fields and validation constraints
- Relationship map (team members referenced by blog posts and case studies, categories linked to posts)
- Embedded vs referenced decision for each relationship
- Editorial workflow with draft/review/published lifecycle
- Naming conventions consistent across all types

**You end up with:** A complete CMS schema document ready to implement in Contentful, Strapi, Sanity, or any headless CMS platform.

### Scenario 2: Refactoring a monolithic content model

**Context:** Your CMS has one "Page" content type used for everything -- blog posts, landing pages, team profiles, and product pages all share the same fields, most of which are optional for most content.

**You say:** "Our CMS uses one Page type for everything -- help me break it into proper content types without losing existing content"

**The skill provides:**
- Analysis of the monolithic type to identify distinct content patterns
- Decomposition into semantic content types based on actual field usage
- Migration strategy: which fields map to which new types
- Shared fields extracted into referenced types (e.g., Author, SEO Metadata)
- Relationship mapping for cross-type references

**You end up with:** A migration plan from monolithic to semantic content types, preserving all existing content while enabling reuse, multi-channel delivery, and proper editorial workflows.

### Scenario 3: Adding multi-channel support to existing content

**Context:** Your content works on the website but the mobile team needs the same content in their app, and the email team needs it in newsletters. The current model has presentation-specific fields.

**You say:** "We need our blog and product content to work on web, mobile, and email -- right now the content has HTML and layout fields baked in"

**The skill provides:**
- COPE architecture assessment identifying presentation-coupled fields
- Field-by-field migration from presentation to semantic fields
- Structured rich text patterns replacing inline HTML
- Multi-channel delivery patterns (same content, different rendering per channel)
- API response design for headless content delivery

**You end up with:** A refactored content model where all content is presentation-independent and deliverable to any channel through the headless CMS API.

## Ideal For

- **Teams building headless CMS implementations** -- the content type methodology prevents the modeling mistakes (page-based types, HTML in fields, monolithic types) that force rebuilds later
- **Content architects designing multi-channel content** -- COPE principles and semantic field design ensure content works across web, mobile, email, and future channels
- **Organizations refactoring legacy CMS content** -- the decomposition patterns break monolithic types into reusable, atomic content types with migration strategies
- **Developers implementing content APIs** -- the relationship types (reference, embedded, hierarchical) and naming conventions translate directly to API schemas and database models

## Not For

- **Formal ontologies, taxonomies, and semantic modeling** -- use [ontology-design](../ontology-design/) for OWL/RDF ontologies with classes, properties, and formal reasoning
- **Naming conventions and terminology standardization** -- use [consistency-standards](../consistency-standards/) for cross-project naming rules and glossary patterns
- **Navigation structure and information architecture** -- use [navigation-design](../navigation-design/) for wayfinding, menu design, and IA patterns

## How It Works Under the Hood

The plugin is a focused single-skill plugin. The SKILL.md body contains the complete content modeling methodology in a compact, immediately usable format.

The skill covers four areas: **content type design** (type templates with purpose, cardinality, lifecycle, fields with types and constraints, relationships with cardinality), **field types** (nine types from short text to reference, each with use cases and examples), **relationship modeling** (reference for independent content, embedded for nested content, hierarchical for parent-child), and **design principles** (COPE architecture, atomic content, anti-patterns to avoid).

The compact structure means simple questions ("what field type for dates?") are answered from the field type table, and complex modeling questions ("design a content model for a documentation platform") use the full template pattern with relationships, validation rules, and COPE principles.

## Related Plugins

- **[Consistency Standards](../consistency-standards/)** -- Naming conventions, terminology standardization, and style guides for content teams
- **[Ontology Design](../ontology-design/)** -- Formal knowledge models with OWL/RDF for semantic modeling beyond CMS content
- **[Navigation Design](../navigation-design/)** -- Information architecture and wayfinding for organizing content hierarchies in user-facing applications
- **[UX Writing](../ux-writing/)** -- Microcopy and interface text patterns for the content that fills the model

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
