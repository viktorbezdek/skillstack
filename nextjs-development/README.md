# Next.js Development

> Comprehensive Next.js development skill covering App Router (13+/15/16), Server Components, Server Actions, Cache Components, data fetching patterns, and module architecture.

## Overview

Next.js has become the dominant React framework for production applications, but its rapid evolution -- from Pages Router to App Router, from `getServerSideProps` to Server Components, from middleware to proxy -- creates a moving target for developers. This skill consolidates best practices across Next.js 13+, 15, and 16 into a single authoritative reference.

The skill covers critical decisions every Next.js developer faces: when to use Server vs. Client Components, how to structure data fetching, which caching strategy to apply, and how to organize code into maintainable modules. It includes non-negotiable rules (always use `<Image>`, never make async Client Components, always specify cache strategy) alongside flexible architectural patterns.

As part of the SkillStack collection, this skill is the go-to resource for any project built on Next.js. It pairs with MCP Server Development for building backend tooling and with ontology/persona skills for designing the user experience that Next.js delivers.

## What's Included

### References

- `extended-patterns.md` -- Detailed code examples for all patterns in the skill
- `architecture-patterns.md` -- Overall application architecture guidance
- `component-patterns.md` -- Server and Client Component patterns
- `database-patterns.md` -- Database schema design and Row-Level Security (RLS)
- `hooks-patterns.md` -- Custom React hooks patterns
- `page-patterns.md` -- Page structure and layout patterns
- `permission-patterns.md` -- Permission and authorization system design
- `service-patterns.md` -- Service layer patterns for data access
- `typescript-patterns.md` -- TypeScript type patterns for Next.js
- `next-16-migration-guide.md` -- Migration guide from Next.js 15 to 16
- `top-errors.md` -- Common errors and their solutions

### Resources

- `app-router-complete.md` -- Complete App Router guide
- `caching-strategies.md` -- Deep dive into caching (ISR, "use cache", revalidation)
- `common-patterns.md` -- Frequently used Next.js patterns
- `complete-examples.md` -- End-to-end code examples
- `component-patterns.md` -- Component design patterns
- `data-fetching-complete.md` -- Comprehensive data fetching patterns
- `data-fetching.md` -- Data fetching quick reference
- `file-organization.md` -- File and folder organization conventions
- `layout-hierarchy.md` -- Layout nesting and hierarchy
- `loading-and-error-states.md` -- Loading UI and error boundary patterns
- `metadata-api.md` -- Metadata and SEO API guide
- `performance.md` -- Performance optimization techniques
- `rendering-strategies.md` -- SSG, ISR, SSR, and Streaming rendering strategies
- `routing-guide.md` -- Routing fundamentals
- `routing-patterns.md` -- Advanced routing patterns (parallel routes, intercepting routes)
- `server-actions-complete.md` -- Complete Server Actions guide
- `server-client-decision.md` -- Server vs. Client Component decision guide
- `styling-guide.md` -- Styling with Tailwind CSS and CSS Modules
- `typescript-standards.md` -- TypeScript coding standards

### Templates

- `app-router-async-params.tsx` -- Async params pattern for Next.js 16
- `cache-component-use-cache.tsx` -- Cache Components with "use cache" directive
- `parallel-routes-with-default.tsx` -- Parallel routes with required default.tsx
- `proxy-migration.ts` -- Middleware to proxy migration pattern
- `route-handler-api.ts` -- Route handler (API route) template
- `server-actions-form.tsx` -- Server Actions with form handling
- `layout-template.md` -- Layout file template
- `page-template.md` -- Page file template
- `package.json` -- Recommended package.json configuration

### Scripts

- `analyze-routing-structure.mjs` -- Analyze an existing App Router directory structure
- `check-versions.sh` -- Check Next.js, React, and Node.js versions
- `validate-patterns.py` -- Validate Next.js patterns against best practices

## Key Features

- Server vs. Client Component decision tree with clear rules
- Next.js 16 breaking changes coverage (async params, proxy migration, "use cache")
- Five-layer module architecture pattern (routes, services, hooks, types, components)
- Data fetching patterns for Server Components, Suspense streaming, and TanStack Query
- Caching strategy guidance (no-store, force-cache, ISR, revalidateTag)
- Server Actions with Zod validation, optimistic UI, and form status
- App Router file conventions and routing patterns (parallel, intercepting, route groups)
- Production-ready templates for every common pattern

## Usage Examples

**Create a new feature module:**
```
Create a blog feature module with list, detail, create, and edit pages. Use the 5-layer architecture pattern with Server Components for data fetching, Server Actions for mutations, and Zod validation.
```

**Migrate from Next.js 15 to 16:**
```
Migrate our app from Next.js 15 to 16. Update all route parameters to use async params, replace middleware.ts with proxy.ts, add default.tsx to parallel routes, and convert eligible components to use "use cache".
```

**Implement data fetching with streaming:**
```
Set up data fetching for our dashboard page. Use parallel fetching with Promise.all for independent data, wrap slow components in Suspense boundaries for streaming, and add proper loading.tsx and error.tsx files.
```

**Add Server Actions for a form:**
```
Create a contact form using Server Actions. Include Zod schema validation, useFormStatus for the submit button loading state, useOptimistic for immediate UI feedback, and revalidateTag after successful submission.
```

**Audit component boundaries:**
```
Review our app directory and identify components that should be Server Components but are marked 'use client'. Check for unnecessary client-side data fetching that could be moved to Server Components.
```

## Quick Start

1. **Check your versions** -- Run `scripts/check-versions.sh` to verify Next.js, React, and Node.js compatibility.

2. **Start with Server Components** -- Every component is a Server Component by default. Only add `'use client'` when you need hooks, event handlers, or browser APIs.

3. **Use the decision tree** -- When unsure about Server vs. Client, walk through the decision tree in SKILL.md.

4. **Pick a caching strategy** -- Every `fetch()` call must specify `cache: 'no-store'`, `cache: 'force-cache'`, or `next: { revalidate: N }`.

5. **Follow the 5-layer pattern** -- Organize features into routes, services, hooks, types, and components directories.

6. **Copy a template** -- Use files from `templates/` as starting points for pages, layouts, route handlers, and Server Actions.

## Related Skills

- **mcp-server** -- Build backend MCP tools that Next.js Server Actions can consume
- **ontology-design** -- Design the data models that Next.js pages render
- **navigation-design** -- Plan the information architecture that App Router implements
- **outcome-orientation** -- Define success metrics for your Next.js application

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) — `/plugin install nextjs-development@skillstack` -- 34 production-grade skills for Claude Code.
