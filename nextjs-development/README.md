# Next.js Development

> **v2.0.23** | Development | 26 iterations

Comprehensive Next.js development skill covering App Router (13+/15/16), Server Components, Server Actions, Cache Components, data fetching patterns, and module architecture.

## What Problem Does This Solve

Next.js 13+ introduced the App Router with Server Components, Server Actions, and a completely different caching model — but the rules are non-obvious and violations cause silent runtime failures, stale data, or broken builds. Developers frequently misplace `'use client'` directives, misconfigure cache strategies, or get caught by Next.js 16's breaking changes (async params, deprecated middleware). This skill provides authoritative guidance on every layer of the framework so decisions are correct on the first pass.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "Should this component be a Server Component or Client Component?" | Decision tree based on interactivity, hooks, browser APIs, and data fetching requirements |
| "How do I fetch data in the App Router?" | Quick reference for Server Component async/await, parallel fetching with Promise.all, TanStack Query for client-side, and all four cache strategies |
| "How do I build a form with server-side mutation in Next.js?" | Server Actions quick reference: `'use server'` directive, Zod validation, revalidateTag/revalidatePath, useFormStatus, useOptimistic |
| "My app broke after upgrading to Next.js 16" | Breaking changes guide: async route parameters, proxy.ts replacing middleware.ts, parallel route default.js requirement, updated revalidateTag API |
| "How should I structure a new feature module?" | 5-layer module architecture pattern across app routes, service layer, hooks, types, and feature components |
| "What are the non-negotiable rules I must follow in Next.js?" | Five critical rules covering next/image, Server Component defaults, async Client Components, cache strategy specification, and Next.js 16 async APIs |

## When NOT to Use This Skill

- generic React patterns, hooks, or component logic -- use [react-development](../react-development/) instead
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
Use the nextjs-development skill to ...
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `nextjs`
- `react`
- `server-components`
- `app-router`

## What's Inside

- **When to Use This Skill** -- Scenarios where this skill applies, covering routing, data fetching, caching, Server Actions, and module architecture
- **Critical Rules** -- Five non-negotiable rules whose violation breaks builds or causes runtime errors: next/image, Server Component defaults, async Client Components, cache strategy, and Next.js 16 async APIs
- **Next.js 16 Breaking Changes** -- Five breaking changes with before/after code: async route parameters, proxy.ts replacing middleware, parallel route default.js, `'use cache'` directive, and updated revalidateTag API
- **Server vs Client Components - Decision Tree** -- Branching decision guide based on interactivity, hooks, browser APIs, and data fetching needs
- **App Router File Conventions** -- Complete directory structure reference for layout.tsx, page.tsx, loading.tsx, error.tsx, route groups, parallel routes, and API routes
- **Data Fetching Quick Reference** -- One-line summaries of Server Component fetching, parallel fetching, Suspense streaming, TanStack Query, and all four cache configurations
- **Server Actions Quick Reference** -- Concise rules for form mutation: directive placement, Zod validation, cache invalidation, and optimistic update hooks
- **Module Architecture (5-Layer Pattern)** -- Directory structure for organizing features across routes, service layer, hooks, types, and components

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

- **[Api Design](../api-design/)** -- Comprehensive API design skill for REST, GraphQL, gRPC, and Python library architectures. Design endpoints, schemas, aut...
- **[Debugging](../debugging/)** -- Comprehensive debugging skill combining systematic debugging methodology, browser DevTools automation, E2E testing with ...
- **[Frontend Design](../frontend-design/)** -- Comprehensive Frontend Design (UI/UX) skill combining UI design systems, component libraries, CSS/Tailwind styling, acce...
- **[Gws Cli](../gws-cli/)** -- Google Workspace CLI (gws) skill for managing Drive, Gmail, Sheets, Calendar, Docs, Chat, Tasks, and 11 more Workspace A...
- **[Mcp Server](../mcp-server/)** -- Comprehensive MCP (Model Context Protocol) server development skill. Build, configure, and manage MCP servers using Pyth...

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 50 production-grade plugins for Claude Code.
