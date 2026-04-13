# Next.js Development

> **v2.0.23** | Development | 26 iterations

> Comprehensive Next.js development skill covering App Router (13+/15/16), Server Components, Server Actions, Cache Components, data fetching, caching strategies, and module architecture.

## The Problem

Next.js moves fast. The App Router introduced Server Components, Server Actions, and an entirely new mental model for data fetching and caching. Next.js 16 made route parameters async, deprecated middleware in favor of proxy, and introduced Cache Components with `"use cache"`. Each major version changes what "correct" looks like, and the official docs -- while excellent -- spread guidance across dozens of pages without a unified decision framework.

The result is predictable: developers add `'use client'` to everything because they are not sure when Server Components are safe. They skip cache strategy specifications on `fetch()` calls and get inconsistent behavior between development and production. They build async Client Components that break at runtime. They miss the `default.js` requirement for parallel routes and get cryptic errors. They try to migrate from Next.js 15 to 16 and discover that `params` is now a Promise, breaking every dynamic route in the app.

These are not edge cases -- they are the top errors that every Next.js team encounters. Without a consolidated reference that covers the decision tree (Server vs Client), the file conventions, the caching model, the data fetching patterns, and the version-specific breaking changes, developers waste hours debugging issues that have well-known solutions.

## The Solution

This plugin provides a unified, version-aware Next.js development guide that covers everything from the Server vs Client Component decision tree to the Next.js 16 migration path. It consolidates five previously separate skills into a single comprehensive resource, covering App Router patterns, Server Components, Server Actions, caching strategies, data fetching, module architecture, and version-specific breaking changes.

You get non-negotiable rules that prevent build failures (always use `<Image>`, never make async Client Components, always specify cache strategy on `fetch()`), a decision tree for Server vs Client Components, complete file convention references for App Router, and working templates for every common pattern -- async params, Cache Components, parallel routes, proxy migration, route handlers, and Server Action forms.

The skill ships with 11 reference files covering architecture, components, database patterns, hooks, pages, permissions, services, TypeScript patterns, migration guides, and common errors -- plus 20 resource files, 9 code templates, and 3 analysis scripts. It is the most comprehensive Next.js plugin in the SkillStack collection.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Add `'use client'` to everything out of uncertainty | Decision tree: Server Component unless you need hooks, event handlers, or browser APIs |
| Skip cache strategy on `fetch()`, get inconsistent dev vs prod behavior | Every `fetch()` explicitly specifies `no-store`, `force-cache`, or `revalidate` with guidance on which to use |
| Migrate to Next.js 16 and break every dynamic route (`params` is now async) | Migration guide with before/after code for async params, proxy migration, and Cache Components |
| Build async Client Components that fail at runtime | Non-negotiable rule enforced: async components are Server Components only |
| Miss `default.js` for parallel routes and get cryptic errors | File convention reference with all required files per pattern, including parallel route fallbacks |
| Reinvent module architecture for each feature | 5-layer pattern: routes, services, hooks, types, components -- consistent across all features |

## Installation

Add the SkillStack marketplace, then install this plugin:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install nextjs-development@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you work with Next.js files or mention Next.js topics.

## Quick Start

1. Install the plugin using the commands above.
2. Start building with Next.js:
   ```
   Create a new blog page with Server Components, data fetching from a Postgres database, and ISR caching with 1-hour revalidation
   ```
3. The skill produces correct App Router code with proper file conventions, cache configuration, and Server Component data fetching.
4. Ask about specific patterns:
   ```
   Should this component be a Server or Client Component? It displays a list but has a search input with onChange
   ```
5. Get a clear decision with the component split pattern: Server Component for the list, Client Component wrapper for the search input.

## What's Inside

Large single-skill plugin with deep reference material, resource guides, code templates, and analysis scripts.

| Component | Description |
|---|---|
| **SKILL.md** | Core skill with critical rules, Next.js 16 breaking changes, Server/Client decision tree, App Router file conventions, data fetching and caching quick reference, Server Actions patterns, and 5-layer module architecture |
| **11 references** | Architecture, components, database/RLS, hooks, pages, permissions, services, TypeScript, migration guide, common errors |
| **20 resources** | App Router, caching, data fetching, metadata API, Server Actions, rendering strategies, routing, Server/Client decision, styling, performance, and more |
| **9 templates** | Async params, Cache Components, parallel routes, proxy migration, route handlers, Server Action forms, layout and page templates |
| **3 scripts** | Routing structure analyzer, version checker, pattern validator |
| **evals/** | 13 trigger evaluation cases + 3 output quality evaluation cases |

### nextjs-development

**What it does:** Activates when you are working with Next.js -- creating pages, implementing data fetching, deciding between Server and Client Components, building Server Actions, configuring caching, setting up routing, or migrating between versions. Covers Next.js 13+, 15, and 16 with version-specific guidance.

**Try these prompts:**

```
Create a dashboard page with a sidebar layout, parallel routes for modals, and streaming data with Suspense
```

```
I'm migrating from Next.js 15 to 16 -- what's going to break and how do I fix it?
```

```
What's the right caching strategy for an e-commerce product page that updates inventory every 5 minutes?
```

```
Build a Server Action for a multi-step form with Zod validation, optimistic updates, and error handling
```

```
My page is slow -- show me how to implement parallel data fetching with Promise.all in Server Components
```

```
Set up the module architecture for a CRUD feature with list, detail, create, and edit pages
```

**Key references:**

| Reference | Topic |
|---|---|
| `extended-patterns.md` | Detailed code examples for all core patterns |
| `architecture-patterns.md` | Overall application architecture |
| `component-patterns.md` | Component composition and splitting |
| `database-patterns.md` | Database schema and Row Level Security |
| `hooks-patterns.md` | Custom hooks for Next.js apps |
| `page-patterns.md` | Page structure and layout composition |
| `permission-patterns.md` | Permission system implementation |
| `service-patterns.md` | Service layer and data access patterns |
| `typescript-patterns.md` | TypeScript patterns for Next.js |
| `next-16-migration-guide.md` | Next.js 15 to 16 migration guide |
| `top-errors.md` | Common errors and solutions |

**Shipped templates:**

| Template | Pattern |
|---|---|
| `app-router-async-params.tsx` | Async route parameters (Next.js 16) |
| `cache-component-use-cache.tsx` | Cache Components with `"use cache"` |
| `parallel-routes-with-default.tsx` | Parallel routes with required default fallback |
| `proxy-migration.ts` | Middleware to proxy migration |
| `route-handler-api.ts` | API route handlers |
| `server-actions-form.tsx` | Server Actions with form handling |
| `layout-template.md` | Layout structure template |
| `page-template.md` | Page structure template |

**Analysis scripts:**

| Script | Purpose |
|---|---|
| `analyze-routing-structure.mjs` | Analyze App Router file tree for convention compliance |
| `check-versions.sh` | Verify Next.js, React, and Node.js version compatibility |
| `validate-patterns.py` | Validate Next.js patterns against best practices |

## Real-World Walkthrough

You are building an internal tool for a logistics company -- a shipment tracking dashboard where operations staff can view, search, filter, and update shipment statuses. The app uses Next.js 16, Postgres with Prisma, and Tailwind CSS. You need a list page, a detail page, a create form, and real-time status updates.

**Step 1: Set up the module architecture.**

You start by asking for the project structure:

```
Set up the module architecture for a shipment tracking feature with list, detail, create, and edit pages using the 5-layer pattern
```

The skill produces the directory structure following the 5-layer module pattern:

```
app/(dashboard)/shipments/       # Route pages
  page.tsx                       # List page (Server Component)
  [id]/page.tsx                  # Detail page (Server Component)
  create/page.tsx                # Create page
  [id]/edit/page.tsx             # Edit page
lib/services/shipments/          # Service layer
  shipment-service.ts            # Data access with Prisma
hooks/shipments/                 # Client-side hooks
  use-shipment-filters.ts        # Filter state management
types/shipment.ts                # TypeScript interfaces
_components/shipments/           # Feature components
  shipment-table.tsx             # List display
  shipment-form.tsx              # Create/edit form
  status-badge.tsx               # Status indicator
```

**Step 2: Build the list page with Server Components.**

The list page needs to fetch shipments from Postgres and display them in a searchable table. You ask:

```
Build the shipment list page as a Server Component with parallel data fetching for both shipments and filter options, streamed with Suspense
```

The skill generates a Server Component that uses `Promise.all` to fetch shipments and filter options in parallel, wraps the table in `<Suspense>` with a loading skeleton, and specifies `cache: 'no-store'` on the fetch because shipment data changes frequently. The search input is extracted into a separate Client Component (`'use client'`) because it needs `onChange` -- following the decision tree: interactivity requires a Client Component, but only the interactive part.

**Step 3: Implement the create form with Server Actions.**

The create form needs validation, optimistic updates, and proper error handling. You ask:

```
Build a Server Action for creating shipments with Zod validation, useFormStatus for loading state, and error handling that shows field-level errors
```

The skill produces a Server Action marked with `'use server'` that validates form data with a Zod schema, calls the shipment service to create the record, revalidates the shipment list cache with `revalidateTag('shipments')`, and returns field-level errors. The form component uses `useFormStatus()` for the submit button loading state and `useOptimistic()` to show the new shipment in the list before the server confirms.

**Step 4: Add the detail page with caching.**

The detail page shows full shipment information and tracking history. You need it to be fast but also reasonably current. You ask:

```
What caching strategy should I use for the shipment detail page? Data changes when status updates happen, but I don't need real-time
```

The skill recommends ISR with tag-based revalidation: `next: { revalidate: 60, tags: ['shipment-${id}'] }`. The page serves from cache for 60 seconds, and when a status update happens (via the Server Action), it calls `revalidateTag('shipment-${id}')` to invalidate just that shipment's cache. This gives near-real-time freshness without hitting the database on every page view.

**Step 5: Handle the Next.js 16 specifics.**

During development, you encounter async params. The skill has already generated code with the correct Next.js 16 pattern:

```typescript
export default async function ShipmentPage({
  params,
}: {
  params: Promise<{ id: string }>
}) {
  const { id } = await params
  // ...
}
```

Without the skill, you would have written `params.id` directly and gotten a runtime error. The skill also uses `proxy.ts` instead of the deprecated `middleware.ts` for auth protection on the dashboard routes.

The result: a complete shipment tracking module built with correct Next.js 16 patterns from the start. Server Components handle data fetching without unnecessary client-side JavaScript. Server Actions handle mutations with validation and optimistic updates. Caching is explicitly configured per data-freshness requirement. The 5-layer architecture keeps the codebase organized as the feature grows. No time wasted debugging async params, missing cache strategies, or incorrect Server/Client splits.

## Usage Scenarios

### Scenario 1: Starting a new Next.js project

**Context:** You are starting a greenfield SaaS application with Next.js 16 and want to set up the project with correct conventions from day one.

**You say:** "Set up a Next.js 16 project with App Router, a root layout with auth protection, a marketing section and a dashboard section using route groups, and API routes for webhooks."

**The skill provides:**
- Complete App Router file structure with route groups `(marketing)` and `(dashboard)`
- Root layout with proper metadata configuration
- Auth protection using `proxy.ts` (not deprecated middleware)
- API route handler template with proper request/response typing
- File conventions checklist: `layout.tsx`, `loading.tsx`, `error.tsx`, `not-found.tsx`

**You end up with:** A correctly structured Next.js 16 project with all file conventions in place, ready to build features.

### Scenario 2: Migrating from Next.js 15 to 16

**Context:** Your production app runs Next.js 15 and you need to upgrade. You have 40+ dynamic routes, middleware for auth, and heavy use of `params` and `searchParams`.

**You say:** "I'm upgrading from Next.js 15 to 16. I have 40 dynamic routes using params and middleware for auth. Walk me through the migration."

**The skill provides:**
- Breaking changes checklist: async params, proxy migration, parallel route defaults, Cache Components
- Before/after code for every breaking change
- Codemod suggestions and manual migration steps
- The `validate-patterns.py` script to check for violations after migration

**You end up with:** A step-by-step migration plan with code transformations for every affected file, and a validation script to catch anything you missed.

### Scenario 3: Optimizing a slow page

**Context:** Your product listing page loads slowly because it fetches product data, category data, and user preferences sequentially.

**You say:** "My product page makes 3 sequential fetch calls and takes 4 seconds to load. How do I speed it up with Next.js patterns?"

**The skill provides:**
- Parallel data fetching with `Promise.all` for independent requests
- Streaming with `<Suspense>` boundaries so the page renders progressively
- Caching strategy: `force-cache` with `revalidate` for product data that changes infrequently
- Component splitting: keep the heavy product grid as a Server Component, extract the filter bar as a Client Component

**You end up with:** A page that loads in under 1 second by fetching in parallel, streaming content progressively, and caching appropriately.

### Scenario 4: Building a form with Server Actions

**Context:** You need a multi-step form for user onboarding with validation, file uploads, and progress persistence.

**You say:** "Build a 3-step onboarding form with Server Actions. Step 1 collects profile info, step 2 handles avatar upload, step 3 selects preferences. I need validation on each step and the ability to go back without losing data."

**The skill provides:**
- Server Action per step with Zod validation schemas
- Form state management using `useFormStatus()` and `useOptimistic()`
- File upload handling in Server Actions
- Progressive enhancement: form works without JavaScript enabled
- Back/forward navigation with state preservation

**You end up with:** A production-quality multi-step form with server-side validation, optimistic updates, and progressive enhancement.

## Ideal For

- **Teams building production Next.js applications** -- the consolidated reference prevents the top runtime errors and build failures
- **Developers learning App Router after Pages Router** -- the decision tree and file conventions make the mental model shift explicit
- **Engineers migrating to Next.js 16** -- version-specific breaking changes with before/after code and migration scripts
- **Full-stack developers building CRUD features** -- the 5-layer module architecture provides a consistent pattern for every feature
- **Anyone confused about Server vs Client Components** -- the decision tree gives a definitive answer for every scenario

## Not For

- **Generic React patterns, hooks, or component logic** -- use [react-development](../react-development/) for React-specific patterns independent of Next.js
- **UI/CSS design systems or visual styling** -- use [frontend-design](../frontend-design/) for Tailwind CSS, design tokens, and component libraries
- **Backend API design unrelated to Next.js** -- use [api-design](../api-design/) for REST, GraphQL, and gRPC patterns
- **TypeScript type system patterns** -- use [typescript-development](../typescript-development/) for generics, Zod, and advanced type patterns

## How It Works Under the Hood

This is the largest single-skill plugin in the SkillStack collection, organized into four layers of depth:

**Core SKILL.md** provides the critical rules, decision trees, and quick references that handle 80% of Next.js development questions. It is designed to load fully into context and give immediate, actionable guidance.

**11 reference files** cover specific architectural domains (architecture, components, database, hooks, pages, permissions, services, TypeScript, migration, errors). These load on demand when the conversation requires depth in a specific area.

**20 resource files** provide comprehensive guides on individual Next.js features (App Router, caching, data fetching, metadata, Server Actions, rendering strategies, routing, Server/Client decisions, styling, performance). These are the deep-dive material for feature-specific questions.

**9 templates and 3 scripts** are production-ready starting points: code templates for every common App Router pattern (async params, Cache Components, parallel routes, proxy, route handlers, Server Actions, layouts, pages) and analysis scripts for routing structure validation, version checking, and pattern compliance.

The evaluation suite (13 trigger cases, 3 output quality cases) ensures the skill activates on Next.js queries and produces code that follows current best practices.

## Related Plugins

- **[React Development](../react-development/)** -- React-specific patterns (hooks, state, component architecture) that complement Next.js
- **[TypeScript Development](../typescript-development/)** -- TypeScript type system patterns used throughout Next.js development
- **[Frontend Design](../frontend-design/)** -- Visual design systems, Tailwind CSS, and component libraries
- **[API Design](../api-design/)** -- API design patterns for Next.js route handlers and external APIs
- **[Test-Driven Development](../test-driven-development/)** -- Testing methodology for Next.js applications

## Version History

- `2.0.23` fix(design+docs): regenerate READMEs for design and documentation plugins
- `2.0.22` fix: add standard keywords and expand READMEs
- `2.0.21` fix: change author field from string to object
- `2.0.20` fix: rename all claude-skills references to skillstack
- `2.0.0` Merged from 5 separate Next.js skills into unified plugin
- `1.0.0` Initial release

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
