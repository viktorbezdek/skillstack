# Next.js Development

> **v2.0.23** | Development | 26 iterations

Comprehensive Next.js development skill covering App Router (13+/15/16), Server Components, Server Actions, Cache Components, data fetching patterns, and module architecture.

## What Problem Does This Solve

Next.js 13+ introduced the App Router with Server Components, Server Actions, and a completely different caching model -- but the rules are non-obvious and violations cause silent runtime failures, stale data, or broken builds. Developers frequently misplace `'use client'` directives, misconfigure cache strategies, pass synchronous params where Next.js 16 requires async, or get caught by breaking changes like middleware deprecation. The framework has deep file-convention magic (layout.tsx, loading.tsx, error.tsx, default.tsx for parallel routes) where missing a single file breaks an entire feature silently. This skill provides authoritative guidance on every layer of the framework so decisions are correct on the first pass.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "Should this component be a Server Component or Client Component?" | Decision tree based on interactivity, hooks, browser APIs, and data fetching requirements |
| "How do I fetch data in the App Router?" | Quick reference for Server Component async/await, parallel fetching with Promise.all, TanStack Query for client-side, and all four cache strategies |
| "How do I build a form with server-side mutation in Next.js?" | Server Actions quick reference: `'use server'` directive, Zod validation, revalidateTag/revalidatePath, useFormStatus, useOptimistic |
| "My app broke after upgrading to Next.js 16" | Breaking changes guide: async route parameters, proxy.ts replacing middleware.ts, parallel route default.js requirement, `'use cache'` directive, updated revalidateTag API |
| "How should I structure a new feature module?" | 5-layer module architecture pattern across app routes, service layer, hooks, types, and feature components |

## When NOT to Use This Skill

- Generic React patterns, hooks, or component logic -- use [react-development](../react-development/) instead
- UI/CSS design systems or visual styling -- use [frontend-design](../frontend-design/) instead

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install nextjs-development@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention the triggers below, or you can invoke it explicitly.

## How to Use

**Direct invocation:**

```
Use the nextjs-development skill to set up a new feature module with CRUD operations
```

```
Use the nextjs-development skill to migrate my middleware to Next.js 16 proxy.ts
```

```
Use the nextjs-development skill to implement caching for my data fetching layer
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

`nextjs` · `react` · `server-components` · `app-router`

## What's Inside

### Skill: nextjs-development

Single-skill plugin with an extensive library of references, resources, templates, and scripts.

| Component | Count | Description |
|---|---|---|
| **SKILL.md** | 1 | Core skill with critical rules, Next.js 16 breaking changes, Server/Client decision tree, App Router file conventions, data fetching reference, Server Actions reference, and 5-layer module architecture |
| **references/** | 11 | Architecture patterns, component patterns, database/RLS patterns, hooks patterns, page patterns, permission patterns, service layer patterns, TypeScript patterns, extended patterns, Next.js 16 migration guide, and top errors with solutions |
| **resources/** | 20 | Deep-dive guides on App Router, caching strategies, data fetching, metadata API, Server Actions, rendering strategies (SSG/ISR/SSR/streaming), routing patterns, server-client decision, component patterns, styling, performance, file organization, and more |
| **templates/** | 9 | Ready-to-use code templates: async params, cache components with `'use cache'`, parallel routes with default.tsx, proxy migration, route handler API, Server Actions forms, layout template, page template |
| **scripts/** | 3 | Routing structure analyzer (mjs), version checker (sh), pattern validator (py) |
| **evals/** | 2 | Trigger evaluation and output quality evaluation test suites |

### Key content areas

- **Five Critical Rules** -- Non-negotiable rules whose violation breaks builds or causes runtime errors: always use `next/image`, Server Components are default, never make async Client Components, always specify cache strategy for fetch(), await async APIs in Next.js 16
- **Next.js 16 Breaking Changes** -- Five breaking changes with before/after code: async route parameters, proxy.ts replacing middleware.ts, parallel route default.js requirement, `'use cache'` directive, and updated revalidateTag API with cache life profiles
- **Server vs Client Decision Tree** -- Step-by-step branching guide: needs interactivity? needs hooks? needs browser APIs? needs to fetch data? Each branch leads to a clear Server or Client recommendation
- **App Router File Conventions** -- Complete directory structure reference for layout.tsx, page.tsx, loading.tsx, error.tsx, not-found.tsx, template.tsx, route groups, parallel routes, and API routes
- **Data Fetching** -- Server Component async/await, parallel fetching with Promise.all, Suspense streaming, TanStack Query for client-side, and all four cache configurations (no-store, force-cache, revalidate, tags)
- **Server Actions** -- Directive placement, form data extraction, Zod validation, cache invalidation with revalidateTag/revalidatePath, useFormStatus for loading states, useOptimistic for optimistic updates
- **Module Architecture** -- 5-layer pattern organizing features across app routes, lib/services, hooks, types, and feature components

## Usage Scenarios

1. **Starting a new Next.js 16 project.** The skill provides the five critical rules as guardrails, the App Router file conventions for structuring your `app/` directory, and the 5-layer module architecture for organizing feature code. The async params template saves you from the most common Next.js 16 migration pitfall.

2. **Migrating from Next.js 15 to 16.** The breaking changes section documents all five changes with before/after code. The proxy migration template provides the exact replacement for deprecated middleware.ts. The migration guide reference covers the full upgrade path.

3. **Implementing a data-heavy dashboard with caching.** Use the data fetching reference to choose between the four cache strategies, the caching strategies resource for deep-dive guidance, and the Server/Client decision tree to determine which components should be Server Components (data fetching) versus Client Components (interactive charts).

4. **Building a form with Server Actions.** The Server Actions reference covers the complete flow: `'use server'` directive placement, Zod validation, revalidateTag for cache invalidation, useFormStatus for loading indicators, and useOptimistic for instant UI feedback. The Server Actions form template provides working starter code.

5. **Debugging a broken build after adding parallel routes.** The top errors reference documents common failures. The parallel routes template shows the required default.tsx file that Next.js 16 demands -- missing it causes silent rendering failures.

## Version History

- `2.0.23` fix(frontend): disambiguate react-development vs nextjs-development vs frontend-design (6c64693)
- `2.0.22` fix: update plugin count and normalize footer in 31 original plugin READMEs (3ea7c00)
- `2.0.21` fix: change author field from string to object in all plugin.json files (bcfe7a9)
- `2.0.20` fix: rename all claude-skills references to skillstack (19ec8c4)
- `2.0.19` refactor: remove old file locations after plugin restructure (a26a802)
- `2.0.18` docs: update README and install commands to marketplace format (af9e39c)
- `2.0.17` refactor: restructure all 34 skills into proper Claude Code plugin format (7922579)
- `2.0.16` refactor: make each skill an independent plugin with own plugin.json (6de4313)
- `2.0.15` fix: resolve broken links, flatten faber scripts, add validate-patterns.py (4647f46)
- `2.0.14` fix: make all shell scripts executable and fix Python syntax errors (61ac964)

## Related Skills

- **[React Development](../react-development/)** -- React-specific patterns (hooks, state management, component architecture) that Next.js builds on
- **[Frontend Design](../frontend-design/)** -- UI/UX design systems, Tailwind CSS, component libraries, and accessibility
- **[TypeScript Development](../typescript-development/)** -- TypeScript patterns and type system features used throughout Next.js code
- **[Api Design](../api-design/)** -- API design patterns for Next.js route handlers and Server Actions
- **[Test Driven Development](../test-driven-development/)** -- TDD methodology for testing Next.js components, Server Actions, and API routes

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 50 production-grade plugins for Claude Code.
