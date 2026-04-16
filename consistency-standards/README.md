# Consistency Standards

> **v1.0.10** | Establish and maintain naming conventions, taxonomy standards, style guides, and content reuse patterns across documentation and code.
> 1 skill | 13 trigger evals, 3 output evals

## The Problem

Inconsistency is the silent tax on every project. One developer names it `getUserName`, another names it `fetch_user_name`, a third names it `retrieveUsername`. Documentation says "click" in one section, "press" in another, and "tap" in a third. Date formats shift between `2024-01-15`, `January 15, 2024`, and `01/15/24` within the same page. None of these are individually harmful, but they compound into a codebase and documentation set that feels unprofessional, confusing, and hard to maintain.

The cost is real and measurable. New team members spend extra time learning which naming convention to follow because the codebase uses three. Technical writers waste hours reconciling terminology after discovering that "user," "account," and "member" all refer to the same concept in different documents. API consumers file support tickets because endpoint naming is unpredictable -- some use camelCase, others use snake_case, and one inexplicably uses kebab-case. Every inconsistency is a small friction point that adds up to hours of lost productivity per week across a team.

The deeper problem is that consistency requires active maintenance. Left to entropy, any project drifts toward inconsistency as new contributors bring their own conventions. Without explicit standards, style guides, and enforcement patterns, consistency is a constantly losing battle.

## The Solution

This plugin provides a framework for establishing and maintaining consistency across naming conventions, terminology, voice and tone, content reuse, and code style. It covers case style standards (camelCase, PascalCase, snake_case, kebab-case, SCREAMING_SNAKE), file naming patterns, glossary creation for standardizing terminology, voice and tone guidelines for different contexts, and content reuse patterns (snippets, variables, conditionals, templates) that enforce single-source authoring.

The skill is deliberately compact -- it provides the standards framework and auditing approach, not hundreds of pages of rules. The goal is to give you the tools to define your project's consistency standards and the patterns to enforce them, whether you are standardizing code style, documentation terminology, or both.

## Context to Provide

Consistency standards are per-context and per-project. Generic style rules are useless if they do not match your actual tech stack and content types. Provide enough context to produce standards your team will actually follow.

**What information to include in your prompt:**

- **Tech stack**: Languages, frameworks, and databases in play (TypeScript/React, Python/FastAPI, PostgreSQL -- each needs different case style rules and different mapping conventions between layers)
- **Consistency problem you are solving**: What specific inconsistency is causing friction? (three naming conventions in the same codebase, "user" vs "account" vs "member" in docs, inconsistent UI element references)
- **Scope**: Code only, documentation only, or both? Public API endpoints, internal variable names, database column names, file names?
- **Existing patterns**: What conventions are already in use, even inconsistently? Knowing that 60% of files use kebab-case helps -- the standard should align with the majority or have a strong reason to differ
- **Enforcement mechanism**: How will the standard be enforced? (ESLint, Prettier, Ruff, manual PR review, automated docs linting) -- standards without enforcement decay
- **Audience**: Who needs to follow the standard? (large open-source community with many contributors needs simpler rules than a 5-person team)

**What makes results better:**
- Describing the actual inconsistency you are observing ("our API returns `userId` but the DB stores `user_id` and the frontend uses `user_id` too -- only the API breaks the pattern") produces a targeted fix rather than a complete overhaul
- Listing the specific synonym groups you want to resolve ("we use user, account, member, and profile to mean the same thing in different docs") produces a glossary with preferred terms and explicit "Do Not Use" alternatives
- Specifying your enforcement toolchain enables the skill to generate lint rules and CI checks alongside the standard itself
- Sharing a few examples of the inconsistency ("here are three files that each use a different naming pattern") makes the standard concrete

**What makes results worse:**
- "Make everything consistent" without scope -- the skill needs to know whether you mean code, docs, APIs, database schemas, or all of the above
- Standards without an enforcement plan -- a style guide nobody checks is noise
- Over-standardizing -- not every variation needs a rule; focus on inconsistencies that cause real confusion or maintenance cost

**Template prompt:**
```
Create a [naming convention guide / terminology glossary / content reuse strategy / voice and tone guide] for [project type]. Stack: [languages and frameworks]. Scope: [what elements to standardize -- variables, functions, files, API endpoints, database columns, documentation]. Current inconsistencies: [describe or give examples]. Enforcement: [ESLint / Ruff / PR review checklist / automated linting]. Audience: [team size and contributor type].
```

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Three naming conventions in the same codebase | Explicit case style guide: camelCase for JS variables, PascalCase for classes, snake_case for Python |
| "Click," "press," "tap," and "select" used interchangeably | Glossary with preferred terms and forbidden synonyms |
| Product name spelled three different ways in docs | Variables (`{{product_name}}`) enforcing single-source naming |
| Inconsistent voice: "you should," "the user must," "we recommend" | Voice and tone guide per context: instructions use direct active voice, errors use helpful calm tone |
| Same installation steps copy-pasted into 8 documents | Single-source snippet included via `{{> shared/installation.md}}` |
| New contributors introduce new inconsistencies with every PR | Style checklist for review: capitalization, dates, UI element names, voice, glossary terms, code style |

## Installation

Add the SkillStack marketplace and install:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install consistency-standards@skillstack
```

### Verify installation

After installing, test with:

```
Create a naming convention guide for our TypeScript project with React components and a Python backend
```

## Quick Start

1. Install the plugin using the commands above
2. Ask: `Audit the naming conventions in our codebase -- we have a mix of camelCase and snake_case and it's causing confusion`
3. The skill produces a case style guide with per-context rules and a migration plan for inconsistencies
4. Expand: `Create a glossary for our documentation -- we use "user," "account," and "member" interchangeably`
5. Enforce: `Design a content reuse strategy so our installation steps are maintained in one place`

---

## System Overview

```
+------------------------------------------------------+
|              consistency-standards skill               |
+------------------------------------------------------+
|                                                        |
|  +----------------+  +------------------+              |
|  | Naming         |  | Terminology      |              |
|  | Conventions    |  | Standards        |              |
|  | - Case styles  |  | - Glossary       |              |
|  | - File naming  |  | - Voice & tone   |              |
|  | - Per-context  |  | - Forbidden terms|              |
|  +----------------+  +------------------+              |
|                                                        |
|  +----------------+  +------------------+              |
|  | Content Reuse  |  | Style Checklist  |              |
|  | - Snippets     |  | - Capitalization |              |
|  | - Variables    |  | - Date formats   |              |
|  | - Conditionals |  | - UI elements    |              |
|  | - Templates    |  | - Code style     |              |
|  +----------------+  +------------------+              |
+------------------------------------------------------+
```

## What's Inside

| Component | Type | Description |
|---|---|---|
| `consistency-standards` | Skill | Naming conventions, terminology standards, voice/tone, content reuse patterns, and consistency auditing |

### Component Spotlights

#### consistency-standards (skill)

**What it does:** Activates when you need to establish, audit, or enforce naming conventions, terminology standards, style guides, or content reuse patterns. Provides frameworks for defining and maintaining consistency across code and documentation.

**Input -> Output:** Project context and consistency concerns -> Naming convention guide, terminology glossary, voice/tone rules, content reuse patterns, and audit checklist.

**When to use:**
- Establishing naming conventions for a new project
- Auditing existing code or docs for consistency issues
- Creating a terminology glossary to standardize vocabulary
- Defining voice and tone guidelines for different content types
- Designing content reuse strategies (DRY documentation)
- Onboarding new team members with style standards

**When NOT to use:**
- Formal ontology or semantic modeling -> use `ontology-design`
- Content type and CMS schema design -> use `content-modelling`
- Writing the actual documentation content -> use `documentation-generator`

**Try these prompts:**

```
Create a naming convention guide for our full-stack project: TypeScript/React frontend, Python/FastAPI backend, PostgreSQL database. Our inconsistencies: React components use both PascalCase files and kebab-case files, Python variables mix camelCase and snake_case, and DB columns are snake_case but our API responses return camelCase without a clear rule. Include mapping rules between layers and ESLint/Ruff rules to enforce them.
```

```
Audit our API documentation for terminology inconsistencies. We suspect we use "user," "account," "member," and "profile" to mean the same thing in different sections. Also "workspace" and "project" may be confused. Produce a glossary with: preferred term, definition, and explicit "Do Not Use" list for each synonym group.
```

```
Design a content reuse strategy for our docs site. The installation instructions for our CLI appear in 8 different guides with slight variations. The Docker setup steps appear in 5 places. I want to maintain each in one canonical source and include it in other pages. We use a Markdown-based docs system (Docusaurus).
```

```
Define voice and tone guidelines for our developer productivity tool. Contexts that need specific rules: step-by-step instructions (tutorials), API reference documentation, error messages shown in the CLI, success confirmations, and the marketing website. We have both technical and non-technical users.
```

---

## Prompt Patterns

### Good Prompts vs Bad Prompts

| Bad (vague, won't activate well) | Good (specific, activates reliably) |
|---|---|
| "Fix our naming" | "Create a naming convention guide for a TypeScript/React project: components, hooks, utilities, API routes, and database columns" |
| "Make docs consistent" | "Audit our docs for terminology: we use 'user,' 'account,' and 'member' interchangeably. Create a glossary with preferred terms." |
| "Style guide please" | "Define voice and tone for our developer docs: API reference sections should be formal and precise, tutorials should be friendly and encouraging" |

### Structured Prompt Templates

**For naming conventions:**
```
Create a naming convention guide for [project type] with [languages/frameworks]. Cover: [code elements], [file naming], [database columns], [API endpoints]. We currently mix [style A] and [style B] and need to standardize.
```

**For terminology standardization:**
```
Create a glossary for [domain]. Terms that need standardization: [list of synonym groups]. For each, define: preferred term, definition, and forbidden alternatives.
```

**For content reuse:**
```
Design a content reuse strategy for [content type]. These sections are duplicated across [N] documents: [list sections]. I want to maintain each in one place and include it wherever needed.
```

### Prompt Anti-Patterns

- **Standards without scope**: "Make everything consistent" -- consistency standards need to be per-context. camelCase is right for JavaScript variables but wrong for Python. Specify the scope.
- **Glossary without enforcement plan**: Creating a glossary nobody reads is wasted effort. Ask for the glossary AND the enforcement strategy (linting, review checklist, automated checks).
- **Over-standardizing**: Not every variation needs a rule. Focus on high-impact inconsistencies that cause real confusion, not cosmetic preferences.

## Real-World Walkthrough

**Starting situation:** You maintain a SaaS documentation site with 120 pages written by 6 different authors over 2 years. A new technical writer joining the team reports that the docs are "all over the place" -- different terminology for the same features, inconsistent date formats, mixed voice, and the installation guide appears in 5 slightly different versions across the site.

**Step 1: Terminology audit.** You ask: "Audit our docs for terminology inconsistencies. Known problem areas: what we call users, what we call workspaces vs projects, and how we refer to the settings page." The skill produces a glossary draft identifying 12 synonym groups. Key findings: "user" / "account" / "member" / "profile" all refer to the same concept in different contexts. "Workspace" and "project" are used interchangeably but are actually different features. The skill creates a glossary table with preferred terms, definitions, and "Do Not Use" alternatives for each.

**Step 2: Voice and tone guidelines.** You ask: "Define voice and tone for our docs." The skill produces context-specific rules: instructional content uses direct active voice ("Click Save"), error messages use helpful calm tone ("Let's fix this -- check that your API key is valid"), success confirmations are positive and brief ("Done! Your changes are live"), and API reference uses precise technical voice without conversational filler.

**Step 3: Content reuse strategy.** You ask: "The installation guide exists in 5 versions. Design a single-source approach." The skill designs a snippet system: the canonical installation steps live in `shared/installation.md`, and each page that needs them includes `{{> shared/installation.md}}`. For pages that need variations (Docker install vs. npm install), the skill recommends conditional includes: `{{#if docker}}...{{/if}}`. This reduces the 5 versions to 1 source with 3 conditional sections.

**Step 4: Style checklist.** The skill produces a review checklist for the team: consistent capitalization (feature names capitalized only when proper nouns), uniform date format (ISO 8601: YYYY-MM-DD), standardized UI element references (use "button" not "button control", use "field" not "input box"), and voice consistency (no "we" in tutorials -- use "you" throughout). This checklist becomes part of the PR review process for documentation changes.

**Step 5: File naming conventions.** The skill standardizes file names across the docs: `[type]-[name]-[variant].[ext]` pattern. Current mess: `setup.md`, `Setup-Guide.md`, `SETUP_instructions.md`, `installation_guide.md`. Standardized: `guide-setup.md`, `guide-installation.md`, `reference-api.md`, `tutorial-quickstart.md`.

**Gotchas discovered:** Two terms that the team assumed were synonyms ("workspace" and "project") turned out to be distinct features in the product. The glossary audit revealed a real terminology bug in the product itself -- the UI said "workspace" in some places and "project" in others for the same feature. This triggered a product fix, not just a docs fix.

## Usage Scenarios

### Scenario 1: Standardizing a multi-language codebase

**Context:** Your project has a TypeScript frontend, Python backend, and SQL database. Each uses different naming conventions and there is no shared standard.

**You say:** "Create a unified naming convention guide for our stack: TypeScript React frontend, Python FastAPI backend, PostgreSQL database."

**The skill provides:**
- Per-context case style rules: camelCase for TS variables, PascalCase for React components, snake_case for Python, snake_case for SQL columns
- Mapping rules: how `user_name` in the database becomes `userName` in the API response and `userName` in the frontend
- File naming: `component-button.tsx`, `service_user.py`, `migration_001_create_users.sql`

**You end up with:** A single-page naming guide that any team member can reference, with clear rules per language and explicit mapping between layers.

### Scenario 2: Creating a documentation style guide

**Context:** Your open-source project has 30 contributors writing docs. Quality varies wildly and there is no style guide.

**You say:** "Create a documentation style guide for our open-source project. Contributors range from native English speakers to ESL developers."

**The skill provides:**
- Glossary of project-specific terms with definitions
- Voice and tone rules: inclusive, simple, direct
- Formatting standards: heading levels, code block annotations, link text conventions
- ESL-friendly guidelines: short sentences, active voice, avoid idioms

**You end up with:** A `STYLE_GUIDE.md` that contributors reference before writing, reducing editorial review burden by standardizing quality expectations.

### Scenario 3: Auditing an existing project for consistency

**Context:** After 18 months of development, your codebase has accumulated naming inconsistencies that make it hard for new developers to predict how things are named.

**You say:** "Audit our codebase for naming inconsistencies. Common problems: some APIs use camelCase, others use snake_case. Component files sometimes use PascalCase, sometimes kebab-case."

**The skill provides:**
- Categorized list of inconsistencies by type (case style, file naming, API endpoints)
- Recommended standard for each category with rationale
- Migration priority: high-impact public API naming first, internal code second
- Automated detection rules (ESLint/Ruff) to prevent new inconsistencies

**You end up with:** A prioritized cleanup plan that addresses the most confusing inconsistencies first, with linting rules to prevent regression.

---

## Decision Logic

**When does this skill activate vs content-modelling or ontology-design?**

This skill handles naming conventions, style guides, and terminology standardization -- how things are named and described. Content-modelling handles CMS content types, fields, and relationships -- how content is structured. Ontology-design handles formal knowledge models with classes, properties, and semantic relationships. If your concern is "we call the same thing by different names," that is consistency-standards. If your concern is "what fields should this content type have," that is content-modelling.

## Failure Modes & Edge Cases

| Failure | Symptom | Recovery |
|---|---|---|
| Standards defined but not enforced | Compliance is high for the first month, then decays | Add automated enforcement: linting rules, CI checks, PR review checklists |
| Over-standardized | Team spends more time checking rules than writing code | Focus on high-impact inconsistencies only; not every preference needs a rule |
| Glossary conflicts with product UI | Docs say "workspace" but the product UI says "project" | Treat it as a product bug; align docs to the correct term, then fix the UI |

## Ideal For

- **Technical writing teams maintaining large doc sets** who need terminology standardization and content reuse strategies
- **Engineering teams with multi-language codebases** who need clear naming convention guides per language with mapping rules between layers
- **Open-source projects with many contributors** who need style guides that maintain quality without gatekeeping
- **Teams onboarding new developers** who need explicit, documented conventions instead of tribal knowledge

## Not For

- **Formal semantic modeling** -- for ontologies with classes, properties, and inference rules, use `ontology-design`
- **CMS content type design** -- for defining content structures, fields, and relationships, use `content-modelling`
- **Code style enforcement** -- for automated linting and formatting (ESLint, Prettier, Ruff), use language-specific development skills

## Related Plugins

- **content-modelling** -- Structure the content that consistency-standards keeps uniformly named
- **ontology-design** -- Formal modeling for terms that need semantic precision beyond naming conventions
- **ux-writing** -- Microcopy and interface text patterns that benefit from voice/tone guidelines
- **documentation-generator** -- Generate documentation that follows the standards this plugin defines

---

*SkillStack plugin by [Viktor Bezdek](https://github.com/viktorbezdek) -- licensed under MIT.*
