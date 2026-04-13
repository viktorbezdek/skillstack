# Consistency Standards

> **v1.0.10** | Quality & Testing | 11 iterations

> Establish and enforce uniform naming conventions, terminology, style guides, and content reuse patterns across documentation and code -- eliminating synonym sprawl, mixed voice, and inconsistent formatting.

## The Problem

A codebase uses `getUserName` in one file, `get_user_name` in another, and `fetchUserName` in a third -- all doing the same thing. Documentation says "click" in one section, "press" in the next, and "tap" in the mobile guide. The API returns `created_at` on one endpoint and `createdAt` on another. A new developer joins and cannot tell which naming convention is official because there are three in active use.

Inconsistency accumulates invisibly. Each individual decision -- camelCase here, snake_case there -- seems harmless. But the compound effect is a codebase where naming cannot be predicted, documentation where terminology confuses rather than clarifies, and onboarding where new team members spend weeks learning which variant is "correct" in which context. Search breaks because the same concept has five names. Content cannot be reused because every document uses different formatting. Style reviews become subjective arguments because there is no documented standard.

The cost is not just aesthetics. Inconsistent APIs cause integration bugs. Inconsistent terminology causes user confusion. Inconsistent file naming breaks automated tooling. And the longer inconsistency persists, the harder it is to fix -- every fix is a breaking change somewhere.

## The Solution

This plugin provides structured patterns for establishing and maintaining consistency: case style rules mapped to specific contexts (camelCase for JS variables, PascalCase for components, snake_case for Python and databases, kebab-case for URLs), file naming templates with type-name-variant conventions, terminology glossaries with "do not use" columns that eliminate synonym sprawl, voice and tone guidelines per context (direct for instructions, helpful for errors, brief for success), content reuse patterns (snippets, variables, conditionals, templates), and a style checklist for auditing existing content.

The skill does not just document conventions -- it provides the anti-patterns to watch for (synonym sprawl, inconsistent capitalization, mixed voice, orphaned content) and the DRY documentation patterns (single-source components, shared includes, template variables) that prevent inconsistency from recurring.

You describe your project's context -- "we have a TypeScript API with Python microservices and React frontend" -- and get a consistent naming convention map that covers every layer, a glossary template for your domain terms, and a style checklist tailored to your stack.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Three naming conventions in active use across the codebase | One documented convention per context (camelCase for JS, snake_case for Python, kebab-case for URLs) |
| Documentation says "click," "press," "tap," and "select" interchangeably | Glossary with canonical terms and "do not use" alternatives |
| Each document uses different voice (you/we/user/one) | Consistent voice per context: direct for instructions, helpful for errors |
| Same content copy-pasted across 5 documents, drifting over time | Single-source content reuse with snippets, variables, and template includes |
| No way to audit existing content for consistency | Style checklist covering capitalization, date formats, UI element names, code style |
| New developers guess which convention to follow | Documented standards that answer "which case style for what?" definitively |

## Installation

Add the SkillStack marketplace, then install:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install consistency-standards@skillstack
```

### Verify Installation

After installing, test with:

```
Create a naming convention standard for our TypeScript monorepo with React frontend and Node.js API
```

The skill activates automatically when you mention naming conventions, style guides, terminology, or consistency.

## Quick Start

1. Install the plugin using the commands above.
2. Describe your consistency need:
   ```
   Our codebase mixes camelCase and snake_case everywhere -- help me establish a naming standard
   ```
3. The skill produces a case style map for your stack, a file naming convention, and a glossary template.
4. Audit existing content:
   ```
   Audit our API documentation for terminology inconsistencies and mixed voice
   ```
5. You get a list of specific violations with corrections and a style checklist to prevent recurrence.

## What's Inside

This is a focused single-skill plugin with no references -- the SKILL.md body contains the complete methodology.

| Component | Purpose |
|---|---|
| **consistency-standards** skill | Naming conventions (5 case styles with usage rules), file naming templates, terminology glossary pattern, voice and tone guidelines, content reuse patterns (4 types), DRY documentation with includes/variables, style checklist, anti-patterns |

**Eval coverage:** 13 trigger eval cases + 3 output eval cases.

### How to Use: consistency-standards

**What it does:** Guides you through establishing uniform naming conventions, terminology standards, voice and tone guidelines, and content reuse patterns. Activates when you need to create or enforce naming rules, build glossaries, standardize documentation voice, audit content for consistency, or set up content reuse patterns. Provides specific rules for every case style (camelCase, PascalCase, snake_case, kebab-case, SCREAMING_SNAKE) mapped to appropriate contexts.

**Try these prompts:**

```
Create a comprehensive naming convention standard for our full-stack TypeScript project -- files, variables, classes, URLs, database columns, and CSS
```

```
Build a terminology glossary for our payment processing documentation -- we use "charge," "payment," "transaction," and "purchase" inconsistently
```

```
Audit our README files for voice consistency -- some use "you," others use "we," and some are passive
```

```
Design a content reuse strategy for our docs -- we have the same authentication instructions copy-pasted in 8 different guides
```

```
What naming convention should I use for React components, hooks, utility functions, types, and test files?
```

## Real-World Walkthrough

Your team maintains a SaaS product with a React frontend, Node.js API, Python data pipeline, and PostgreSQL database. Over two years, three different naming conventions have emerged because each developer brought their preferences. The frontend uses `PascalCase` for components (correct) but also `camelCase` for file names (some files) and `kebab-case` (other files). The API uses `camelCase` for JSON responses but the database columns are `snake_case`, and the ORM mapping is inconsistent. Documentation refers to the same feature as "workspace," "project," "team space," and "organization" depending on who wrote the section.

You start by establishing the naming standard:

```
Create a naming convention for our stack -- React frontend, Node.js Express API, Python data pipeline, PostgreSQL database
```

The skill produces a comprehensive case style map:

**Frontend (TypeScript/React):**
- Components: `PascalCase` (`UserProfile.tsx`)
- Hooks: `camelCase` with `use` prefix (`useAuthentication.ts`)
- Utilities: `camelCase` (`formatCurrency.ts`)
- Constants: `SCREAMING_SNAKE_CASE` (`MAX_RETRIES`)
- CSS classes: `kebab-case` (`user-profile-card`)
- File naming: `PascalCase` for components, `camelCase` for utilities, `kebab-case` for styles

**API (Node.js/Express):**
- JSON response fields: `camelCase` (`createdAt`, `userName`)
- Route paths: `kebab-case` (`/api/v1/user-profiles`)
- Variables and functions: `camelCase`
- Environment variables: `SCREAMING_SNAKE_CASE`

**Data Pipeline (Python):**
- Variables and functions: `snake_case` (`get_user_name`)
- Classes: `PascalCase` (`DataProcessor`)
- Constants: `SCREAMING_SNAKE_CASE`
- File naming: `snake_case` (`data_processor.py`)

**Database (PostgreSQL):**
- Tables: `snake_case`, plural (`user_profiles`)
- Columns: `snake_case` (`created_at`)
- Indexes: `idx_` prefix (`idx_user_profiles_email`)

The ORM mapping layer explicitly translates between database `snake_case` and API `camelCase` -- this is documented as the boundary convention.

Next, the terminology problem:

```
Build a glossary for our product -- we use "workspace," "project," "team space," and "organization" to mean the same thing
```

The skill produces a glossary with the pattern:

| Term | Definition | Do Not Use |
|------|------------|------------|
| workspace | A container for projects and team members | project, team space, organization, group |
| member | A person with access to a workspace | user, team member, participant |
| project | A collection of tasks within a workspace | board, folder, channel |

Each entry has the canonical term, a clear definition, and a "Do Not Use" column listing the synonyms that must be replaced. The glossary gets committed to the repository and referenced in the contribution guidelines.

You then audit the existing documentation:

```
Audit our docs/ folder for consistency against these standards
```

The audit reveals: 23 instances of "project" used where "workspace" is the correct term, 8 instances of mixed voice (switching between "you" and "we" mid-paragraph), 4 different date formats (`Jan 5, 2025`, `2025-01-05`, `January 5`, `01/05/2025`), and 3 documents with copy-pasted authentication instructions that have drifted.

For the authentication duplication, the skill sets up a content reuse pattern: a single `shared/authentication.md` file with the canonical instructions, included in each guide using the template pattern `{{> shared/authentication.md}}`. When the auth flow changes, you update one file instead of finding and fixing 8.

The style checklist becomes part of the PR review process. Every documentation PR is checked against: consistent capitalization, uniform date format (ISO 8601: `2025-01-05`), glossary terms used correctly, single voice throughout (second person "you" for instructions), and code style matching the project convention.

Six months later, onboarding time for new developers has dropped noticeably -- they do not spend the first week asking "which naming convention do we use?" because the answer is documented, enforced, and consistent.

## Usage Scenarios

### Scenario 1: Establishing naming conventions for a new project

**Context:** You are starting a new monorepo with multiple languages and want to establish naming rules before the codebase grows.

**You say:** "Set up naming conventions for our new monorepo -- Kotlin backend, React frontend, and shared TypeScript libraries"

**The skill provides:**
- Case style map for each language layer (Kotlin conventions, React conventions, TypeScript library conventions)
- File naming templates with type-name-variant pattern
- Boundary conventions for data serialization between layers
- Constants and environment variable standards
- Convention documentation template for the repo

**You end up with:** A documented naming standard committed to the repository that every developer follows from day one, preventing the three-convention drift that happens organically.

### Scenario 2: Fixing terminology sprawl in documentation

**Context:** Your product documentation uses five different words for the same feature. Customer support tickets frequently cite confusion about terminology.

**You say:** "We have terminology sprawl in our docs -- 'workspace,' 'project,' 'team,' and 'group' all mean the same thing. Help me standardize"

**The skill provides:**
- Glossary template with canonical term, definition, and "do not use" alternatives
- Audit pattern for finding all instances of non-canonical terms
- Search-and-replace plan ordered by document priority
- Process for handling terms that are ambiguous (workspace vs project when they are different things)

**You end up with:** A canonical glossary, a list of specific replacements to make across the documentation, and a process for maintaining terminology consistency going forward.

### Scenario 3: Setting up content reuse to eliminate copy-paste

**Context:** Your getting-started guide, API reference, and tutorial all contain the same authentication instructions, and they have drifted apart over time.

**You say:** "We have the same auth instructions in 6 documents and they've all drifted -- set up single-source content reuse"

**The skill provides:**
- Single-source component patterns (snippet, variable, conditional, template)
- DRY documentation structure using includes and variables
- Migration plan for consolidating drifted copies into one source
- Variable pattern for product names and versions that change

**You end up with:** A shared content directory with single-source components included across all documents, so changes propagate automatically and drift is impossible.

## Ideal For

- **Teams starting new projects** -- establishing naming conventions before the codebase grows prevents the costly cleanup needed when three conventions compete
- **Documentation teams fighting terminology sprawl** -- glossary patterns with "do not use" columns eliminate the ambiguity that confuses users and support teams
- **Organizations with multi-language stacks** -- the case style mapping across languages and the boundary convention for serialization answer "which style where?" definitively
- **Anyone maintaining copy-pasted content across documents** -- the DRY documentation patterns with includes and variables eliminate drift and reduce maintenance

## Not For

- **Code formatting and linting** -- use language-specific formatters (Prettier, Black, gofmt) and linters for automated style enforcement
- **API design conventions (endpoint naming, status codes)** -- use [api-design](../api-design/) for REST, GraphQL, and gRPC conventions
- **Content modeling and CMS architecture** -- use [content-modelling](../content-modelling/) for content types, fields, and editorial workflows

## How It Works Under the Hood

The plugin is a single-skill plugin with no reference documents -- the SKILL.md body is compact and self-contained.

The skill covers four areas: **naming conventions** (five case styles with context-specific usage rules, file naming templates), **terminology standards** (glossary template with canonical terms and banned synonyms, voice and tone guidelines per context), **content reuse patterns** (four component types: snippets, variables, conditionals, templates, plus DRY documentation with includes), and **consistency auditing** (style checklist with six verification points, four documented anti-patterns).

The compact structure means the full methodology loads into every session without requiring reference document lookups. Simple questions ("what case style for React components?") are answered from the case style table. Complex questions ("set up a glossary and content reuse for our docs") use the full terminology and DRY documentation sections.

## Related Plugins

- **[Content Modelling](../content-modelling/)** -- CMS content models, editorial workflows, and structured content architecture
- **[UX Writing](../ux-writing/)** -- Microcopy, error messages, and interface text patterns
- **[Ontology Design](../ontology-design/)** -- Formal knowledge models with classes, properties, and taxonomies
- **[Navigation Design](../navigation-design/)** -- Information architecture and wayfinding patterns

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
