# Next.js Development

> **v2.0.24** | Development | 26 iterations

---

## The Problem

Next.js moves fast. Between App Router, Server Components, Server Actions, the `"use cache"` directive, async route parameters in Next.js 16, and the middleware-to-proxy migration, keeping up requires constant documentation reading. Teams building production applications face a compounding knowledge problem: the framework's surface area is enormous, breaking changes arrive with each major version, and the wrong architectural decision early (choosing Client Components where Server Components should be default, ignoring cache strategies, using deprecated middleware patterns) creates technical debt that is expensive to unwind.

The pain hits hardest during version transitions. Next.js 16 made `params`, `searchParams`, `cookies()`, `headers()`, and `draftMode()` async -- every page and layout that accesses these APIs needs updating. Middleware is deprecated in favor of `proxy.ts`. Parallel routes now require `default.js` fallbacks. Teams migrating large codebases spend days tracking down build failures that stem from these breaking changes, often discovering them one at a time in production.

Even within a single version, architectural decisions carry high stakes. Server Components are the default, but adding `'use client'` to the wrong component pulls its entire subtree to the client, ballooning bundle size. Cache strategies (`no-store`, `force-cache`, ISR, `"use cache"`) interact in non-obvious ways -- a missing cache directive on a fetch call can cause stale data in production or unnecessary revalidation that degrades performance. Module architecture (where services, hooks, types, and components live) varies across tutorials and blog posts, leaving teams with inconsistent project structures.

Without a comprehensive, version-aware reference covering Next.js 13+, 15, and 16 patterns, teams oscillate between outdated blog posts, incomplete documentation, and trial-and-error. Each developer on the team learns different patterns, creating inconsistency that compounds with project size.

## The Solution

The Next.js Development plugin gives Claude deep, version-aware expertise in Next.js covering App Router, Server Components, Server Actions, caching strategies, data fetching, routing, module architecture, and the full Next.js 16 migration path. It is one of the largest SkillStack plugins -- a single skill backed by 11 reference documents, 20 resource guides, 9 code templates, and 3 analysis scripts.

The plugin covers critical rules (non-negotiable patterns that prevent build failures), the Server vs Client Component decision tree, App Router file conventions, data fetching patterns (Server Components, TanStack Query, SWR, parallel fetching, streaming), Server Actions with Zod validation and optimistic UI, caching strategies from `no-store` to `"use cache"` with revalidation profiles, and the complete 5-layer module architecture pattern.

For Next.js 16 specifically, the plugin provides: async route parameter migration, middleware-to-proxy migration, parallel route `default.js` requirements, `"use cache"` directive usage, and updated `revalidateTag()` API with cache life profiles. Templates provide copy-pasteable starting points for the most common patterns.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Accidentally use `<img>` instead of `next/image` and get build failures | Critical rule enforcement: always `<Image>`, always cache strategy on fetch, always await async APIs |
| Add `'use client'` to components that should be Server Components, bloating bundle size | Server vs Client Component decision tree based on actual needs (hooks, event handlers, browser APIs) |
| Spend days migrating to Next.js 16, discovering breaking changes one by one in production | Complete Next.js 16 migration guide: async params, proxy.ts, default.js, `"use cache"`, updated revalidateTag |
| Inconsistent module architecture across team members | 5-layer module pattern: routes, services, hooks, types, components with clear boundaries |
| Cache strategy chosen by guesswork -- stale data or unnecessary revalidation | Cache strategy decision framework: no-store vs force-cache vs ISR vs "use cache" with revalidation profiles |
| No templates for common patterns -- every developer writes boilerplate from scratch | 9 code templates: async params, cache components, parallel routes, proxy migration, route handlers, Server Actions forms |

## Context to Provide

Next.js patterns change significantly between versions, and the skill's advice is highly version-specific. Always include your version, and include enough specifics about your data flow and component needs to get production-ready code on the first attempt.

**What information to include in your prompt:**
- **Next.js version** -- 13, 14, 15, or 16; this changes params handling, caching directives, and middleware vs proxy patterns significantly
- **Data source and access pattern** -- where the data comes from (Postgres, REST API, GraphQL, external SaaS), how frequently it changes, and whether it is user-specific or shared
- **Component interaction requirements** -- does the component need event handlers, browser APIs, or React hooks? If not, it should be a Server Component -- state this explicitly and the skill will enforce it
- **Caching requirements** -- how stale data can be (seconds, minutes, hours), whether on-demand revalidation is needed (e.g., after a form submit), and whether `"use cache"` or ISR is more appropriate
- **Existing error messages** -- if you are debugging, paste the exact error message from the terminal or browser console; Next.js error messages are specific enough to route to the right fix

**What makes results better:**
- Specifying whether the page is inside a route group, and the current `app/` directory structure for complex routing scenarios
- Describing the complete data flow (where data comes from, which component fetches it, what the child components do with it) rather than asking about one component in isolation
- For migrations, sharing a code snippet of the old pattern alongside the error message -- the skill generates before/after diffs
- Mentioning related features on the same page (e.g., "this page also has a search filter that needs client-side state") so the Server/Client boundary is designed correctly the first time

**What makes results worse:**
- Specifying only the UI without describing the data -- caching and component boundary decisions depend on the data characteristics
- Mixing Next.js version assumptions ("I think I'm on 15 but might be 14") -- run `check-versions.sh` and include the output
- Asking about "React" when you mean Next.js -- Server Components, Server Actions, and the App Router are Next.js concepts; if you need generic React hooks and state, that is a different plugin

**Template prompt -- new page:**
```
Create a Next.js [version] page at app/[route path]/page.tsx.

Data: fetches [describe data] from [source: Postgres / REST API at URL / GraphQL].
Data freshness: [real-time (no-store) / acceptable to be N minutes stale / revalidate on-demand when X happens].
Server vs Client: [fully server-rendered / needs [specific hooks or events] so requires client].
Loading state: [Suspense with skeleton / loading.tsx / none].
Error handling: [error.tsx boundary / inline error state / propagate to parent].
Related components on this page: [describe any interactive elements that need 'use client'].
```

**Template prompt -- migration:**
```
Migrate this Next.js [old version] code to [new version]:
[paste the component or page code]

Error I'm seeing: [paste exact error message]
```

**Template prompt -- caching strategy:**
```
Design the caching strategy for [feature/page]. 

Data: [describe what is fetched and from where]
Freshness requirement: [how stale can the data be?]
Revalidation triggers: [user action / webhook / scheduled / none]
Traffic: [low / medium / high -- affects whether ISR makes sense]
Next.js version: [15 / 16]
```

## Installation

Add the marketplace and install:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install nextjs-development@skillstack
```

### Prerequisites

- Node.js 20.9+
- Next.js 13+ (optimized for 15 and 16)
- React 18, 19, or 19.2

For React-specific patterns (hooks, state management, component architecture), also install `react-development`. For visual design systems and Tailwind CSS, also install `frontend-design`.

### Verify installation

After installing, test with:

```
I'm starting a new Next.js 16 project -- set up the file structure with App Router, a dashboard layout, and a data fetching pattern using Server Components
```

## Quick Start

1. Install the plugin using the commands above
2. Ask: `Create a Next.js page with Server Components that fetches data from an API and handles loading and error states`
3. The skill generates a complete page with proper App Router conventions, Suspense boundaries, and error handling
4. You receive production-ready code following the 5-layer module pattern
5. Next, try: `I need to migrate my middleware.ts to the new proxy.ts pattern in Next.js 16`

---

## System Overview

```
nextjs-development/
├── .claude-plugin/
│   └── plugin.json                    # Plugin manifest
└── skills/
    └── nextjs-development/
        ├── SKILL.md                   # Core skill (critical rules, decision trees, patterns, architecture)
        ├── references/                # 11 deep-dive reference documents
        │   ├── architecture-patterns.md       # Overall architecture patterns
        │   ├── component-patterns.md          # Component design patterns
        │   ├── database-patterns.md           # Database schema and RLS
        │   ├── extended-patterns.md           # Detailed code examples for all patterns
        │   ├── hooks-patterns.md              # Custom hooks patterns
        │   ├── next-16-migration-guide.md     # Next.js 16 migration guide
        │   ├── page-patterns.md               # Page structure patterns
        │   ├── permission-patterns.md         # Permission system patterns
        │   ├── service-patterns.md            # Service layer patterns
        │   ├── top-errors.md                  # Common errors and solutions
        │   └── typescript-patterns.md         # TypeScript patterns
        ├── resources/                 # 20 resource guides
        │   ├── app-router-complete.md         # Complete App Router guide
        │   ├── caching-strategies.md          # Caching deep dive
        │   ├── data-fetching-complete.md      # Data fetching patterns
        │   ├── metadata-api.md                # Metadata API guide
        │   ├── rendering-strategies.md        # SSG, ISR, SSR, Streaming
        │   ├── routing-patterns.md            # Routing patterns
        │   ├── server-actions-complete.md     # Server Actions guide
        │   ├── server-client-decision.md      # Server/Client decision guide
        │   └── ... (12 more)
        ├── templates/                 # 9 code templates
        │   ├── app-router-async-params.tsx     # Async params pattern
        │   ├── cache-component-use-cache.tsx   # Cache Components
        │   ├── parallel-routes-with-default.tsx # Parallel routes
        │   ├── proxy-migration.ts             # Proxy migration
        │   ├── route-handler-api.ts           # Route handlers
        │   ├── server-actions-form.tsx         # Server Actions forms
        │   ├── layout-template.md             # Layout templates
        │   └── page-template.md               # Page templates
        ├── scripts/                   # 3 analysis scripts
        │   ├── analyze-routing-structure.mjs  # Analyze App Router structure
        │   ├── check-versions.sh              # Check Next.js/React/Node versions
        │   └── validate-patterns.py           # Validate Next.js pattern compliance
        └── evals/
            ├── trigger-evals.json     # 13 trigger evaluation cases
            └── evals.json             # 3 output evaluation cases
```

The plugin is a single comprehensive skill backed by a large reference library. The SKILL.md provides critical rules, decision trees, and quick references. References cover architecture, components, database, hooks, pages, permissions, services, TypeScript, migration, and errors. Resources provide complete guides for App Router, caching, data fetching, metadata, rendering, routing, and Server Actions. Templates provide copy-pasteable starting points. Scripts analyze and validate project patterns.

## What's Inside

| Component | Type | Purpose |
|---|---|---|
| `nextjs-development` | Skill | Critical rules, Server/Client decision tree, App Router conventions, data fetching, caching, module architecture |
| 11 reference files | References | Architecture, components, database, hooks, pages, permissions, services, TypeScript, migration, errors |
| 20 resource guides | Resources | Complete guides for App Router, caching, data fetching, metadata, rendering, routing, Server Actions, styling |
| 9 code templates | Templates | Async params, cache components, parallel routes, proxy migration, route handlers, Server Actions forms, layouts, pages |
| 3 scripts | Scripts | Routing structure analysis, version checking, pattern validation |

### Component Spotlight

#### nextjs-development (skill)

**What it does:** Activates when you are building with Next.js. Provides critical build rules, the Server vs Client Component decision tree, App Router file conventions, data fetching patterns, Server Actions with validation, caching strategies, and the 5-layer module architecture pattern. Covers Next.js 13+, 15, and 16 with explicit breaking change documentation.

**Input -> Output:** A Next.js development task (new page, data fetching, migration, caching, routing) -> Production-ready code following App Router conventions with proper cache strategies, Server/Client Component separation, and module architecture.

**When to use:**
- Creating new Next.js pages, layouts, or components
- Implementing data fetching with Server Components, TanStack Query, or SWR
- Deciding between Server and Client Components
- Building Server Actions for forms and mutations
- Implementing caching strategies (ISR, `"use cache"`, revalidation)
- Migrating from Next.js 15 to 16
- Setting up module architecture for feature-scale development

**When NOT to use:**
- Generic React patterns, hooks, or component logic (use `react-development`)
- UI/CSS design systems or visual styling (use `frontend-design`)
- TypeScript language features unrelated to Next.js (use `typescript-development`)
- API design principles unrelated to Next.js route handlers (use `api-design`)

**Try these prompts:**

```
Next.js 16. Create app/(dashboard)/users/page.tsx -- a data table that fetches users from our Postgres database via a service function getUsers(). Columns: name, email, role, created_at, status (active/inactive). Needs: loading skeleton while fetching (Suspense), error boundary if the query fails, no client-side interactivity. Data freshness: revalidate every 5 minutes.
```

```
Next.js 16. Implement ISR for our blog. Post pages at app/blog/[slug]/page.tsx should revalidate every hour (ISR). The homepage at app/page.tsx should revalidate on-demand when a post is published (our CMS sends a webhook). Params are accessed as: const { slug } = await params. Show the full caching setup including the revalidation webhook route handler.
```

```
Migrate these Next.js 15 pages to Next.js 16. I'm getting "params is not iterable" on every page. Here is one example:
export default function ProductPage({ params }: { params: { id: string } }) {
  const { id } = params
  // ...
}
I have 30 pages with this pattern plus 8 layouts. Show me the migration pattern and a script to find all occurrences.
```

```
Design the module architecture for a multi-tenant project management SaaS with Next.js 16. Modules: users (auth + profiles), projects (CRUD + settings), tasks (CRUD + assignments + status), teams (members + roles), billing (plans + invoices). Apply the 5-layer module pattern. Show the full app/ directory structure, service layer organization, type file locations, and component boundaries.
```

```
This component fetches project data from an API and also has a search input with onChange that filters the displayed projects. Should it be a Server Component or Client Component? Next.js 16. If it needs to be split, show me the correct split: which part is the Server Component, which is the Client Component, and how the data passes between them.
```

```
Next.js 16. Build a Server Action for a project creation form. Zod schema: name (string, 2-50 chars), description (string, optional, max 500 chars), visibility (enum: public/private). On success: revalidateTag('projects'), redirect to the new project page. On error: return field-level errors for useFormState. Client-side: useFormStatus for loading state, useOptimistic for immediate list update before server confirms.
```

**Key references:**

| Reference | Topic |
|---|---|
| `extended-patterns.md` | Detailed code examples for all major patterns |
| `next-16-migration-guide.md` | Complete migration guide: async params, proxy.ts, default.js, "use cache" |
| `top-errors.md` | Common build and runtime errors with solutions |
| `architecture-patterns.md` | Overall application architecture patterns |
| `component-patterns.md` | Server/Client Component design patterns |
| `database-patterns.md` | Database schema, RLS, and data access patterns |
| `service-patterns.md` | Service layer implementation patterns |

**Key templates:**

| Template | Purpose |
|---|---|
| `app-router-async-params.tsx` | Next.js 16 async params pattern |
| `cache-component-use-cache.tsx` | `"use cache"` directive usage |
| `server-actions-form.tsx` | Form with Server Actions and validation |
| `proxy-migration.ts` | Middleware to proxy migration |
| `parallel-routes-with-default.tsx` | Parallel routes with required default.js |

**Scripts:**

| Script | Purpose |
|---|---|
| `analyze-routing-structure.mjs` | Analyze your App Router file structure for issues |
| `check-versions.sh` | Verify Next.js, React, and Node.js version compatibility |
| `validate-patterns.py` | Validate code against Next.js pattern best practices |

---

## Prompt Patterns

### Good Prompts vs Bad Prompts

| Bad (vague, won't activate well) | Good (specific, activates reliably) |
|---|---|
| "Help me with React" | "Create a Next.js Server Component that fetches user data and passes it to a Client Component with a search filter" |
| "Fix my page" | "My Next.js 16 page crashes with 'params is not iterable' -- I'm destructuring params without awaiting" |
| "How do I cache things?" | "Implement ISR for my product pages with 1-hour revalidation and on-demand revalidation when products are updated via Server Actions" |
| "Make a form" | "Build a Server Action form with Zod validation, useFormStatus for loading state, and useOptimistic for immediate UI feedback" |
| "Help with routing" | "Set up parallel routes for a dashboard with @analytics and @notifications slots, including default.js fallbacks" |

### Structured Prompt Templates

**For new pages:**
```
Create a Next.js [version] page at [route path] that [data requirement]. It needs [loading state / error boundary / streaming]. The data comes from [source]. User interactions: [list any client-side needs].
```

**For migration:**
```
Migrate [component/page/layout] from Next.js [old version] to [new version]. Current code uses [specific APIs: params, searchParams, middleware, etc.]. Show the before and after.
```

**For caching strategy:**
```
Design the caching strategy for [page/feature]. Data freshness requirements: [how stale is acceptable]. Revalidation triggers: [on-demand events, time-based, or both]. Scale: [traffic level].
```

**For module architecture:**
```
Design the module architecture for [feature] in a Next.js app. The feature needs: [CRUD operations / data fetching / forms / real-time updates]. Related modules: [other features it interacts with].
```

### Prompt Anti-Patterns

- **Asking for React patterns without Next.js context** -- if you need `useState` or `useEffect` guidance without Next.js routing/fetching, use `react-development` instead
- **Requesting "the best" cache strategy without freshness requirements** -- caching depends entirely on how stale data can be; provide acceptable staleness duration and revalidation triggers
- **Mixing Next.js versions in one request** -- specify which version you are targeting (13+, 15, or 16); patterns differ significantly
- **Ignoring the Server Component default** -- starting with `'use client'` and asking how to fetch data is backwards; start with Server Components and only add `'use client'` when you need interactivity

## Real-World Walkthrough

**Starting situation:** You are building a multi-tenant project management SaaS with Next.js 16. The app needs: a dashboard with real-time project stats, a project list with filtering, project detail pages with task management, team member management, and billing settings. You need to establish the architecture, data fetching patterns, and caching strategy before the team starts building features.

**Step 1: Module architecture.** You ask: "Design the module architecture for a project management SaaS with Next.js 16 -- users, projects, tasks, teams, billing."

The skill applies the 5-layer module pattern. For the projects module:
- `app/(routes)/projects/` -- pages (list, `[id]` detail, create, edit)
- `lib/services/projects/` -- service layer with data access functions
- `hooks/projects/` -- custom hooks for client-side state
- `types/projects.ts` -- TypeScript interfaces and DTOs
- `_components/projects/` -- feature-specific components

Each module follows the same structure, creating consistency across the team.

**Step 2: Server vs Client Component split.** You describe the dashboard: "The dashboard shows project stats (server-fetched) and has a search filter for the project list (client-side)." The skill applies the decision tree: the stats display is a Server Component (no interactivity, fetches data), the search filter is a Client Component (needs `useState` and `onChange`). The pattern: Server Component fetches all projects, passes them as props to a Client Component that handles filtering. This keeps the data fetch on the server while enabling interactivity.

**Step 3: Data fetching with Next.js 16 async params.** You build a project detail page. The skill generates the page with `params: Promise<{ id: string }>` (Next.js 16 async requirement), awaits params before use, fetches project data directly in the Server Component, and wraps child components in `<Suspense>` for streaming. The template from `app-router-async-params.tsx` provides the exact pattern.

**Step 4: Caching strategy.** You ask about caching for the project list and dashboard. The skill designs a layered strategy: dashboard stats use `next: { revalidate: 60 }` (acceptable to be 1 minute stale), project list uses `next: { tags: ['projects'] }` with on-demand revalidation via `revalidateTag('projects')` when a project is created/updated, and individual project pages use `"use cache"` with the `'hours'` life profile.

**Step 5: Server Actions for mutations.** You need a project creation form. The skill generates a Server Action with `'use server'`, Zod schema validation (`schema.safeParse()`), database insert, `revalidateTag('projects')` after mutation, and a client-side form using `useFormStatus()` for loading state and `useOptimistic()` for immediate UI feedback. The `server-actions-form.tsx` template provides the complete pattern.

**Step 6: Route structure.** The skill maps out the App Router file structure:
```
app/
  layout.tsx            # Root layout with auth
  (dashboard)/
    page.tsx            # Dashboard
  projects/
    page.tsx            # Project list
    [id]/
      page.tsx          # Project detail
      tasks/page.tsx    # Task list
  settings/
    billing/page.tsx    # Billing
    team/page.tsx       # Team management
```

Each route group uses layouts for shared UI, loading.tsx for Suspense fallbacks, and error.tsx for error boundaries.

**Final outcome:** A complete architectural blueprint with 5-layer module pattern, Server/Client Component split, Next.js 16 async param handling, tiered caching strategy (time-based + on-demand + `"use cache"`), Server Actions with validation and optimistic UI, and App Router file structure. The team can now build features against consistent patterns.

**Gotchas discovered:** The skill flagged that parallel routes (used for the dashboard's @stats and @projects slots) require `default.tsx` fallback files in Next.js 16 -- missing these causes silent rendering failures that are hard to debug.

## Usage Scenarios

### Scenario 1: Migrating from Next.js 15 to 16

**Context:** You have a production Next.js 15 app with 40 pages, many using `params` and `searchParams` synchronously, a `middleware.ts` for auth redirects, and parallel routes without default files.

**You say:** "Migrate my Next.js 15 app to 16. I have 40 pages accessing params synchronously and a middleware.ts for auth."

**The skill provides:**
- Systematic migration checklist: async params, proxy.ts, default.js, "use cache"
- Before/after code for every breaking change
- The `proxy-migration.ts` template for middleware replacement
- The `app-router-async-params.tsx` template for param migration
- Warning about parallel routes needing default.js

**You end up with:** A migration plan you can execute page-by-page with copy-pasteable patterns for each breaking change.

### Scenario 2: Implementing real-time data with caching

**Context:** You need a dashboard that shows mostly static data (refreshed hourly) but includes a live notification count that updates every few seconds.

**You say:** "Build a dashboard with hourly-refreshed stats and a live notification counter. How do I mix static caching with real-time data in the same page?"

**The skill provides:**
- Server Component for stats with `next: { revalidate: 3600 }` (hourly ISR)
- Client Component for notification count using TanStack Query with polling
- Composition pattern: Server Component fetches static data, Client Component island handles real-time
- Suspense boundary wrapping the Client Component for progressive loading

**You end up with:** A hybrid page that caches expensive data fetches while keeping the notification counter live, with proper Suspense boundaries for smooth loading.

### Scenario 3: Building a complete CRUD feature module

**Context:** You need to add a "Teams" feature to your SaaS app -- list teams, create team, edit team, manage members -- following consistent architecture.

**You say:** "Build a complete Teams module with CRUD operations following the 5-layer pattern. I need list, create, edit, and member management pages."

**The skill provides:**
- Route structure: `app/teams/page.tsx`, `app/teams/create/page.tsx`, `app/teams/[id]/page.tsx`, `app/teams/[id]/edit/page.tsx`, `app/teams/[id]/members/page.tsx`
- Service layer: `lib/services/teams/` with `getTeams()`, `getTeam()`, `createTeam()`, `updateTeam()`
- Server Actions: form handlers with Zod validation and revalidation
- Types: `types/teams.ts` with Team, CreateTeamDTO, UpdateTeamDTO interfaces
- Components: `_components/teams/` with TeamList, TeamForm, MemberList

**You end up with:** A complete feature module following the 5-layer pattern that the rest of the team can reference when building other modules.

### Scenario 4: Debugging common Next.js errors

**Context:** Your build fails with "Text content does not match server-rendered HTML" and you see hydration errors in the console.

**You say:** "I'm getting hydration mismatch errors -- 'Text content does not match server-rendered HTML'. The component renders user-specific data."

**The skill provides:**
- Diagnosis: Server Component rendered with server data, Client Component rehydrated with different client data
- Fix: move user-specific rendering to a Client Component wrapped in Suspense
- Alternative: use `useEffect` for client-only data to avoid SSR mismatch
- Reference to `top-errors.md` for the complete error catalog

**You end up with:** A fixed hydration error and understanding of the Server/Client rendering boundary that prevents recurrence.

---

## Decision Logic

**Server Component vs Client Component?**

The skill applies a strict decision tree: Server Components are the default. Only add `'use client'` when the component needs React hooks (`useState`, `useEffect`), event handlers (`onClick`, `onChange`), or browser APIs (`window`, `localStorage`). Data fetching strongly prefers Server Components. Mixed needs (data fetch + interactivity) use the composition pattern: Server Component fetches, passes data as props to a Client Component child.

**Which caching strategy?**

- `cache: 'no-store'` -- data must be fresh on every request (user-specific, real-time)
- `cache: 'force-cache'` -- data rarely changes (static content, configuration)
- `next: { revalidate: N }` -- ISR, acceptable to be N seconds stale (product pages, blog posts)
- `next: { tags: [...] }` -- on-demand revalidation when specific data changes (after mutations)
- `"use cache"` with life profiles -- Next.js 16 component-level caching (`'max'`, `'hours'`, `'days'`, `'weeks'`)

**When to use which data fetching approach?**

- Server Components with `async/await` -- default for most data fetching (preferred)
- `Promise.all([...])` -- parallel fetching of independent data in Server Components
- `<Suspense>` -- streaming for progressive loading of async components
- TanStack Query / SWR -- client-side fetching when data must update without page reload

## Failure Modes & Edge Cases

| Failure | Symptom | Recovery |
|---|---|---|
| Using `<img>` instead of `next/image` | Build failure with ESLint error | Replace with `<Image>` component from `next/image` with width/height |
| Synchronous params in Next.js 16 | Runtime error: params is not iterable | Add `Promise<>` type wrapper and `await` before destructuring |
| Missing `default.tsx` in parallel routes | Silent rendering failure -- slot shows nothing | Add default.tsx that returns null or a fallback UI in every parallel route slot |
| No cache strategy on `fetch()` | Unpredictable caching behavior, stale or always-fresh based on framework defaults | Explicitly specify `cache` or `next` option on every fetch call |
| `'use client'` on data-fetching component | Data fetched on client instead of server, larger bundle, slower page load | Move data fetch to Server Component parent, pass data as props |
| Async Client Component | Build error or unexpected behavior | Never make Client Components async; use `useEffect` or hooks for async client work |

## Performance & Constraints

The plugin has a large reference surface (11 references + 20 resources). The skill loads the SKILL.md core content on activation and pulls references on demand when deeper context is needed. For simple questions (decision tree, critical rules), only the SKILL.md is consulted. For complex tasks (migration, architecture, debugging), relevant references are loaded selectively.

Templates are designed to be copy-pasted and modified -- they follow all critical rules and include TypeScript types. Scripts can be run directly in your project to analyze patterns and validate compliance.

## Ideal For

- **Next.js teams** building production applications who need consistent, version-aware patterns across the team
- **Developers migrating** from Next.js 15 to 16 who need systematic breaking-change coverage and migration templates
- **Solo developers** starting new Next.js projects who want production-grade architecture from day one
- **Teams debugging** Next.js build failures, hydration errors, or caching issues who need a comprehensive error reference
- **Frontend architects** designing module architecture for large Next.js applications with multiple feature areas

## Not For

- **Generic React development** -- hooks, state management, and component patterns without Next.js context use `react-development`
- **Visual design and styling** -- Tailwind CSS, design tokens, and component libraries use `frontend-design`
- **API design principles** -- REST conventions, GraphQL, or gRPC design use `api-design`
- **TypeScript language features** -- type system patterns unrelated to Next.js use `typescript-development`

## Related Plugins

- **react-development** -- React-specific patterns (hooks, state management, component architecture) that complement Next.js development
- **frontend-design** -- visual design systems, Tailwind CSS, and UI component libraries
- **typescript-development** -- TypeScript type system patterns, generics, and Zod integration
- **api-design** -- REST and GraphQL API design for route handlers
- **testing-framework** -- test infrastructure for Next.js applications

---

*SkillStack plugin by [Viktor Bezdek](https://github.com/viktorbezdek) -- licensed under MIT.*
