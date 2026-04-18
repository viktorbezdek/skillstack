# Content Modelling

> **v1.0.12** | Design content models with types, fields, relationships, and governance rules for structured content systems -- COPE patterns, editorial workflows, and CMS schema architecture.
> 1 skill | 13 trigger evals, 3 output evals

## The Problem

Content systems fail when they are designed around pages instead of content. A marketing team builds their CMS with page-based models -- "Homepage," "About Page," "Blog Post Page" -- with HTML embedded directly in rich text fields. It works for the website. Then the mobile app needs the same content in a different layout. Then the email system needs a subset. Then the partner API needs structured data. Every new channel requires duplicating and reformatting content because the model was designed for one output format, not for the content itself.

The consequences cascade. A product description exists in 5 places with 5 slightly different versions. When the price changes, someone updates 3 of the 5 and misses 2. A content type called "General Content" becomes a dumping ground with 40 optional fields because nobody designed specific types for specific content. Editorial workflows break because there is no lifecycle model -- content goes from "draft" to "published" with no review step, no scheduling, and no archival process.

The root cause is that most teams skip content modeling entirely and jump straight to building CMS templates. They define content by what it looks like on a specific page rather than what it is. This conflation of content with presentation makes every future adaptation expensive and error-prone.

## The Solution

This plugin provides a structured approach to content modeling that separates content from presentation. It covers the fundamental concepts -- content types, fields, relationships, and instances -- and provides patterns for designing content that works across channels, teams, and time.

The core principle is COPE: Create Once, Publish Everywhere. Content types use semantic fields (what the content IS) rather than layout fields (how it LOOKS). A "Product" type has `name`, `description`, `price`, and `category` fields -- not "hero image position" or "sidebar widget." This makes the same content available to websites, mobile apps, emails, APIs, and channels that do not exist yet.

The skill covers field type selection (when to use rich text vs. short text, references vs. embeds), relationship modeling (reference, embedded, hierarchical), naming conventions, editorial workflow design, and governance rules. It provides a content model template that teams can fill in for each content type, producing a documented schema that serves as the contract between content creators and developers.

## Context to Provide

Content models need to reflect your actual content, channels, and editorial reality. The more detail you provide about what content exists, who creates it, and where it appears, the more precisely the types, fields, and workflows will be designed.

**What information to include in your prompt:**

- **Content inventory**: What types of content exist? (articles, products, authors, categories, reviews, events, FAQs, case studies) -- list all distinct types, not just the main one
- **Relationships**: How do content types connect? ("A recipe has many ingredients, belongs to one category, has one author, and can appear in multiple collections")
- **Output channels**: Where does content appear? (website, mobile app, email newsletter, in-app help, partner API) -- multi-channel requirements change the field design significantly
- **Author roles**: Who creates and edits content? (technical writers, marketers, external contributors, developers) -- affects workflow complexity
- **Editorial workflow**: How does content move from draft to published? Are there review stages? Approvals? Scheduling?
- **Current pain points**: What is broken with the current system? (content duplicated across 5 places, "General Content" type with 40 fields, no archival process, mobile gets wrong data)
- **CMS platform**: Contentful, Sanity, Strapi, WordPress, custom -- affects what field types and relationship patterns are available

**What makes results better:**
- Listing every content type, not just the main one -- a "Product" type depends on knowing that "Category," "Brand," "Review," and "Variant" also exist
- Specifying your output channels explicitly -- a content type that only feeds a website can include layout assumptions; one that feeds a mobile app, email, and API cannot
- Describing a real pain point ("our product description exists in 5 places with 5 slightly different versions and they drift apart") produces targeted COPE design
- Sharing your current CMS schema (even informally: "we have a Page type with these fields: ...") enables a migration-oriented design rather than starting from scratch

**What makes results worse:**
- Designing for one page layout ("I need a hero banner with three feature cards") -- this is page design, not content modeling
- Requesting a "General Content" type that can hold anything -- the skill will push back and ask what specific types you actually need
- Omitting the channel list -- field design decisions are fundamentally different for single-channel vs. multi-channel systems

**Template prompt:**
```
Design a content model for [domain / project]. Content types: [list all distinct types]. Relationships: [type A] has many [type B], [type C] belongs to one [type D]. Output channels: [website / mobile app / email / API / in-app help -- list all]. Author roles: [who creates content]. Editorial workflow: [describe review and approval stages]. Current pain: [what is broken today]. CMS platform: [Contentful / Sanity / Strapi / custom / not yet decided].
```

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Page-based models tied to specific layouts | Semantic content types that work across any channel |
| HTML embedded in content fields, mixing content with presentation | Clean field types: short text, rich text, media, references -- no markup |
| One "General Content" type with 40 optional fields | Specific types for specific content, each with only relevant fields |
| Same content duplicated across 5 systems with drift | COPE: single source of truth, published to all channels from one model |
| No lifecycle -- content jumps from draft to published | Editorial workflow: draft -> review -> scheduled -> published -> archived |
| Unpredictable naming: `BlogPost`, `blog_entry`, `BLOG-ITEM` | Convention: PascalCase types, camelCase fields, kebab-case slugs |

## Installation

Add the SkillStack marketplace and install:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install content-modelling@skillstack
```

### Verify installation

After installing, test with:

```
Design a content model for a knowledge base with articles, categories, authors, and related content recommendations
```

## Quick Start

1. Install the plugin using the commands above
2. Ask: `Design a content model for a SaaS product documentation site with guides, API references, changelogs, and tutorials`
3. The skill produces content types with fields, relationships, validation rules, and editorial workflow
4. Refine: `Add a content reuse strategy -- installation steps should be maintainable in one place but appear in multiple guides`
5. Validate: `Review the model for anti-patterns -- are we accidentally tying content to specific page layouts?`

---

## System Overview

```
+-----------------------------------------------------------+
|                 content-modelling skill                     |
+-----------------------------------------------------------+
|                                                             |
|  Content Types        Relationships        Governance       |
|  +---------------+    +---------------+    +-------------+  |
|  | Type design   |    | Reference     |    | Workflow    |  |
|  | Field types   |    | Embedded      |    | Validation  |  |
|  | Constraints   |    | Hierarchical  |    | Naming      |  |
|  | Lifecycle     |    | Cardinality   |    | COPE rules  |  |
|  +---------------+    +---------------+    +-------------+  |
|                                                             |
|  Patterns: COPE | Atomic Content | Semantic Fields          |
+-----------------------------------------------------------+
```

## What's Inside

| Component | Type | Description |
|---|---|---|
| `content-modelling` | Skill | Content type design, field types, relationships, naming conventions, COPE patterns, editorial workflows |

### Component Spotlights

#### content-modelling (skill)

**What it does:** Activates when you need to design CMS content models, define content types with fields and relationships, plan editorial workflows, or establish governance rules for structured content systems. Provides templates and patterns for building content that is reusable, multi-channel, and maintainable.

**Input -> Output:** Content requirements (what content exists, who creates it, where it appears) -> Content type definitions with fields, relationships, validation rules, naming conventions, and editorial workflow.

**When to use:**
- Designing a CMS schema for a new project
- Defining content types with fields, constraints, and relationships
- Planning editorial workflows (draft, review, publish, archive)
- Building multi-channel content systems (web, mobile, email, API)
- Migrating from page-based to structured content models
- Establishing naming conventions for content types and fields

**When NOT to use:**
- Building formal ontologies with classes, properties, and inference rules -> use `ontology-design`
- Standardizing naming conventions across code and documentation -> use `consistency-standards`
- Designing API schemas and endpoints -> use `api-design`

**Try these prompts:**

```
Design a content model for an e-commerce product catalog. Types: Product, ProductVariant (size/color combinations with separate SKU and stock), Category (hierarchical, up to 3 levels), Brand, Review (customer-submitted, needs moderation), Collection (curated groupings for campaigns). The same content must feed our website, mobile app, and a point-of-sale kiosk. Variants have their own price and stock per combination. CMS: Contentful.
```

```
I'm migrating our blog from WordPress to a headless CMS (Sanity). Design the content types to support: the website (full article with sidebar), a mobile app (title, summary, and body only), and a weekly email newsletter (title, summary, and featured image). Our current WordPress has post, category, tag, and author. We have 1,200 existing posts to migrate.
```

```
Our CMS has a "Page" content type with 35 optional fields and it's used for blog posts, landing pages, case studies, and product pages. Authors are confused about which fields to fill in. Help me decompose it into specific types. Here are the 35 fields: [paste field list]. Show field usage analysis and the new type boundaries.
```

```
Design a four-stage editorial workflow for our multi-author SaaS documentation site. Authors: technical writers (draft), engineers (technical review), editor (editorial review), then published with scheduling. Content types that need this workflow: Guide, Tutorial, API Reference. Some content (like Changelog entries) only needs one review step. Include status transition rules and who can approve each transition.
```

---

## Prompt Patterns

### Good Prompts vs Bad Prompts

| Bad (vague, won't activate well) | Good (specific, activates reliably) |
|---|---|
| "Design my CMS" | "Design content types for a recipe website: recipes, ingredients, categories, authors, collections, and meal plans" |
| "What fields do I need?" | "Define the field types for a Product content type: it needs name, description (formatted), price, SKU, images (multiple), and category relationship" |
| "Make it work on mobile" | "Design a COPE content model where the same product content feeds our website, mobile app, in-store kiosk, and partner API" |

### Structured Prompt Templates

**For content type design:**
```
Design a content model for [domain/project]. Content types needed: [list types]. Relationships: [type A] has many [type B], [type C] belongs to [type D]. Each type needs: fields with types and constraints, lifecycle definition, and validation rules.
```

**For migration from page-based models:**
```
We have [N] page types in our current CMS: [list types]. Each is tied to a specific page layout. Help me restructure into content-first types that work across [channels]. Current pain point: [specific problem].
```

**For editorial workflow design:**
```
Design an editorial workflow for [content type]. Authors: [roles]. Review process: [steps]. Publication: [immediate/scheduled/approval-gated]. Archival: [policy].
```

### Prompt Anti-Patterns

- **Designing content for one page layout**: "The homepage needs a hero banner, three feature cards, and a testimonial slider" -- this is page design, not content modeling. Ask instead: "What content types do we need for marketing content that appears on the homepage and can be reused on landing pages?"
- **Putting HTML in field definitions**: "I need a rich text field that includes the sidebar layout" -- content fields should contain content, not layout instructions. Presentation is the rendering layer's job.
- **One type for everything**: "Create a General Content type that can hold any kind of content" -- this produces an unusable type with dozens of optional fields. Design specific types for specific content.

## Real-World Walkthrough

**Starting situation:** You are building a headless CMS for a B2B SaaS documentation site. The content needs to serve a marketing website, a developer docs portal, an in-app help system, and a knowledge base. Currently, content lives in a monolithic WordPress instance with page-based templates, making reuse across channels impossible.

**Step 1: Content type inventory.** You ask: "Design a content model for our SaaS docs. We need: product guides, API reference entries, tutorials, changelogs, FAQ items, and marketing pages." The skill produces six content types, each with a purpose statement, expected instance count, and lifecycle definition.

**Step 2: Field design for the Guide type.** The skill defines the Guide content type:
- `title` (short text, required, max 100 chars)
- `slug` (short text, required, URL-safe, unique within parent category)
- `summary` (short text, required, max 300 chars -- for search results and cards)
- `body` (rich text, required -- the actual guide content, NO layout markup)
- `author` (reference to Author, required)
- `category` (reference to Category, many-to-one)
- `relatedGuides` (reference to Guide, many-to-many, max 5)
- `difficulty` (enum: beginner/intermediate/advanced)
- `status` (enum: draft/review/published/archived)
- `publishedAt` (date, required when status = published)

The skill explains why `summary` is a separate field rather than auto-generated from `body`: different channels need different summary lengths, and a human-written summary is always better than a truncated paragraph.

**Step 3: Relationship modeling.** The skill designs the relationship structure: Guides belong to Categories (hierarchical), Guides reference Authors (linked, author exists independently), Guides contain SEO Metadata (embedded, metadata only exists within the guide), and Guides link to related Guides (reference, bidirectional). The skill explains the choice: embedded for SEO Metadata because it has no independent existence, but reference for Authors because an author can be edited once and the change propagates everywhere.

**Step 4: COPE design.** You ask: "How do I serve the same content to 4 channels?" The skill designs the approach: every content type uses semantic fields only. The Guide type has `body` (rich text without layout), `summary`, `difficulty`, and `category` -- none of which assume a specific rendering. The website renders `body` in a full-width layout with a sidebar nav. The in-app help system renders `summary` in a tooltip with a link to the full `body`. The mobile app renders `body` in a reader-optimized view. All from the same source content.

**Step 5: Editorial workflow.** The skill designs a four-stage workflow for Guides: draft (author writes), technical review (engineer verifies accuracy), editorial review (writer checks clarity and style), published (goes live with `publishedAt` timestamp). Status transitions are enforced: you cannot publish without passing both reviews. Archived guides remain accessible via direct URL but are removed from navigation and search.

**Step 6: Naming convention.** Types use PascalCase (`BlogPost`), fields use camelCase (`publishedAt`), slugs use kebab-case (`getting-started`). The skill flags that the existing WordPress instance uses inconsistent naming and provides a migration mapping.

**Gotchas discovered:** The initial model put `heroImage` on the Guide type, which is a presentation concern (not all channels show a hero image). The skill recommended moving it to a separate `MediaAsset` reference that the website rendering layer can use but that does not pollute the content model with layout assumptions.

## Usage Scenarios

### Scenario 1: E-commerce product catalog

**Context:** You are building a headless commerce platform where product content feeds the website, mobile app, and point-of-sale system.

**You say:** "Design a content model for an e-commerce catalog: products with variants (size, color), categories, brands, reviews, and collections."

**The skill provides:**
- Product type with semantic fields (no layout assumptions)
- Variant modeling: Product -> Variant (embedded) with SKU, price, stock per combination
- Category hierarchy with parent-child relationships
- Review type with author reference, rating constraint (1-5), and moderation status
- Collection type for curated product groupings

**You end up with:** A content model that serves the website product page, the mobile browse experience, and the POS lookup screen from the same product data.

### Scenario 2: Breaking up a monolithic content type

**Context:** Your CMS has a "Page" type with 35 fields. Authors are confused about which fields to fill in for different content.

**You say:** "Our Page type has 35 optional fields and is used for everything. Help me decompose it into specific types."

**The skill provides:**
- Analysis of field usage patterns to identify natural type boundaries
- New types: LandingPage (8 fields), BlogPost (10 fields), CaseStudy (12 fields), ProductPage (9 fields)
- Migration plan: map existing instances to new types based on which fields they use
- Validation rules that make per-type required fields actually required

**You end up with:** Four focused types instead of one bloated one, each with clear purpose and only the fields that type needs.

### Scenario 3: Designing a multi-language content model

**Context:** Your documentation needs to support English, Spanish, and Japanese with locale-specific variations.

**You say:** "Add multi-language support to our content model. Some content is translated, some is locale-specific, and some is universal (like code samples)."

**The skill provides:**
- Localization strategy: base content type with locale-specific overrides
- Universal fields (code samples, screenshots) vs. localized fields (body text, title)
- Fallback chain: Japanese -> English -> default content
- Locale-aware slug generation for SEO

**You end up with:** A content model where translators only touch locale-specific fields, code samples are maintained once, and missing translations gracefully fall back.

---

## Decision Logic

**When to use reference vs embedded relationships?**

Reference (linked): when the related content has independent existence and should be editable in one place. An Author referenced by 50 Guides should be a reference -- updating the author's bio updates it everywhere. Embedded: when the content only exists within its parent. SEO Metadata for a Guide has no independent purpose -- embed it. Hierarchical: for parent-child tree structures like documentation categories.

**When does this skill activate vs ontology-design or consistency-standards?**

Content-modelling designs CMS schemas: content types, fields, and editorial workflows. Ontology-design models formal knowledge with classes, properties, and inference rules. Consistency-standards handles naming conventions and terminology. If you need a CMS schema for a blog, use content-modelling. If you need an RDF ontology for a knowledge graph, use ontology-design. If you need naming rules for your codebase, use consistency-standards.

## Failure Modes & Edge Cases

| Failure | Symptom | Recovery |
|---|---|---|
| Page-based content types | Content cannot be reused across channels without reformatting | Redesign with semantic fields; remove all layout-specific fields from content types |
| HTML in rich text fields | Content renders incorrectly on mobile or in email | Enforce rich text fields as semantic markup only; strip layout HTML in migration |
| Missing lifecycle definitions | Content goes from draft to published with no review; stale content never archived | Add status enum with transition rules and required review steps |
| Monolithic content type | 40 optional fields; authors do not know which to fill in | Decompose into specific types based on field usage analysis |

## Ideal For

- **CMS architects designing new content systems** who need structured types, relationships, and governance from the start
- **Teams migrating from page-based CMS to headless** who need to restructure content for multi-channel delivery
- **Content strategists planning editorial workflows** who need lifecycle definitions, review stages, and governance rules
- **Developers building multi-channel content APIs** who need content models that work for web, mobile, email, and third-party integrations

## Not For

- **Formal knowledge modeling** -- for ontologies with inference rules, SPARQL, and semantic reasoning, use `ontology-design`
- **Naming convention standardization** -- for terminology glossaries and code style guides, use `consistency-standards`
- **API endpoint design** -- for REST/GraphQL/gRPC schema design, use `api-design`

## Related Plugins

- **consistency-standards** -- Naming conventions that keep content types and fields uniformly named
- **ontology-design** -- Formal knowledge modeling when content needs semantic precision
- **api-design** -- Design APIs that serve the content models this plugin defines
- **navigation-design** -- Information architecture for content hierarchies
- **ux-writing** -- Microcopy and interface text patterns for content governance

---

*SkillStack plugin by [Viktor Bezdek](https://github.com/viktorbezdek) -- licensed under MIT.*
