---
name: nextjs-development
description: Comprehensive Next.js development skill covering App Router (13+/15/16), Server Components, Server Actions, Cache Components, data fetching patterns, and module architecture.
triggers:
  - Next.js
  - App Router
  - Server Components
  - Server Actions
  - SSR
  - SSG
  - ISR
  - middleware
  - layouts
  - parallel routes
license: MIT
metadata:
  merged_from:
  - frontend-development-guidelines-nextjs-tailwind
  - nextjs-module-builder
  - nextjs-app-router---production-patterns
  - nextjs-15-app-router-specialist
  - nextjs-app-router
  nextjs_versions:
  - 13+
  - '15'
  - '16'
  node_version: 20.9+
  react_versions:
  - '18'
  - '19'
  - '19.2'
  version: 1.0.0
allowed-tools:
- Read
- Write
- Edit
- Bash
- Glob
- Grep
- WebFetch
---

# Next.js Development - Comprehensive Guide

A unified skill merging best practices for Next.js development, covering App Router patterns, Server Components, data fetching, caching strategies, and module architecture.

---

## When to Use This Skill

Use this skill when:

- Creating new Next.js pages, layouts, or components
- Implementing data fetching (Server Components, TanStack Query, SWR)
- Deciding between Server and Client Components
- Building Server Actions for forms and mutations
- Implementing caching strategies (ISR, "use cache", revalidation)
- Setting up routing with App Router
- Migrating from Next.js 15 to 16
- Building complete feature modules with CRUD operations
- Optimizing metadata and SEO
- Styling with Tailwind CSS

---

## Critical Rules

These rules are **NON-NEGOTIABLE**. Violations will break builds or cause runtime errors.

### 1. ALWAYS use `<Image>` from `next/image`

```typescript
// CORRECT
import Image from 'next/image'
<Image src="/logo.png" alt="Logo" width={200} height={100} />

// WRONG - BUILD WILL FAIL
<img src="/logo.png" alt="Logo" />
```

### 2. Server Components are DEFAULT

Only add `'use client'` when the component needs:
- React hooks (`useState`, `useEffect`, etc.)
- Event handlers (`onClick`, `onChange`, etc.)
- Browser APIs (`window`, `localStorage`, etc.)

### 3. Never make async Client Components

### 4. Always specify cache strategy for fetch()

```typescript
const data = await fetch('/api/data', { cache: 'no-store' })
const data = await fetch('/api/data', { cache: 'force-cache' })
const data = await fetch('/api/data', { next: { revalidate: 3600 } })
```

### 5. Await async APIs in Next.js 16

```typescript
// CORRECT (Next.js 16)
export default async function Page({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params
  const cookieStore = await cookies()
  const headersList = await headers()
}
```

---

## Next.js 16 Breaking Changes

### 1. Async Route Parameters

`params`, `searchParams`, `cookies()`, `headers()`, and `draftMode()` are now **async**.

```typescript
export default async function Page({
  params,
  searchParams,
}: {
  params: Promise<{ slug: string }>
  searchParams: Promise<{ query: string }>
}) {
  const { slug } = await params
  const { query } = await searchParams
  return <div>{slug}</div>
}
```

### 2. Middleware to Proxy Migration

`middleware.ts` is deprecated. Use `proxy.ts` instead.

```typescript
// proxy.ts (NEW)
import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'

export function proxy(request: NextRequest) {
  const token = request.cookies.get('token')
  if (!token) {
    return NextResponse.redirect(new URL('/login', request.url))
  }
  return NextResponse.next()
}

export const config = {
  matcher: '/dashboard/:path*',
}
```

### 3. Parallel Routes Require default.js

### 4. Cache Components with "use cache"

```typescript
'use cache'

export async function ExpensiveComponent() {
  const data = await fetch('https://api.example.com/data')
  return <div>{data}</div>
}
```

### 5. Updated revalidateTag() API

```typescript
revalidateTag('posts', 'max')
// Cache life profiles: 'max', 'hours', 'days', 'weeks', 'default'
```

---

## Server vs Client Components - Decision Tree

```
Do you need interactivity (onClick, onChange)?
├─ YES → Client Component ('use client')
└─ NO → Server Component (default)

Do you need React hooks (useState, useEffect)?
├─ YES → Client Component
└─ NO → Server Component

Do you need browser APIs (window, localStorage)?
├─ YES → Client Component
└─ NO → Server Component

Do you need to fetch data?
├─ Use Server Component (preferred)
└─ Client Component only if data must be client-side
```

---

## App Router File Conventions

```
app/
  layout.tsx       # Root layout (required)
  page.tsx         # Home page (/)
  loading.tsx      # Loading UI
  error.tsx        # Error boundary
  not-found.tsx    # 404 page
  template.tsx     # Re-rendered layout

  blog/
    layout.tsx     # Blog layout
    page.tsx       # /blog
    [slug]/
      page.tsx     # /blog/[slug]

  (marketing)/     # Route group (no URL effect)
    about/page.tsx # /about

  @modal/          # Parallel route
    login/page.tsx
    default.tsx    # Required fallback

  api/
    users/route.ts # API route
```

---

## Data Fetching Quick Reference

- **Server Components**: `async/await` with `fetch()` or direct DB calls (preferred)
- **Parallel fetching**: `Promise.all([...])` for multiple requests
- **Streaming**: Wrap async components in `<Suspense>` for progressive loading
- **Client-side**: TanStack Query `useSuspenseQuery` for client-fetched data
- **Caching**: `cache: 'no-store'` | `cache: 'force-cache'` | `next: { revalidate: N }` | `next: { tags: [...] }`

---

## Server Actions Quick Reference

- Mark with `'use server'` directive
- Use `formData.get()` for form fields
- Validate with Zod: `schema.safeParse()`
- Call `revalidateTag()` / `revalidatePath()` after mutations
- Use `useFormStatus()` for loading states
- Use `useOptimistic()` for optimistic UI updates

---

## Module Architecture (5-Layer Pattern)

```
app/(routes)/[module]/       # Pages (list, detail, create, edit)
lib/services/[module]/       # Service layer (data access)
hooks/[module]/              # Custom hooks
types/                       # TypeScript interfaces & DTOs
_components/                 # Feature-specific components
```

See [Extended Patterns](references/extended-patterns.md) for detailed code examples of all patterns above.

---

## Resources

### Reference Files

- `references/extended-patterns.md` - Detailed code examples for all patterns
- `references/architecture-patterns.md` - Overall architecture
- `references/component-patterns.md` - Component patterns
- `references/database-patterns.md` - Database schema and RLS
- `references/hooks-patterns.md` - Custom hooks
- `references/page-patterns.md` - Page structure
- `references/permission-patterns.md` - Permission system
- `references/service-patterns.md` - Service layer
- `references/typescript-patterns.md` - TypeScript patterns
- `references/next-16-migration-guide.md` - Migration guide
- `references/top-errors.md` - Common errors and solutions

### Resource Files

- `resources/app-router-complete.md` - App Router guide
- `resources/caching-strategies.md` - Caching deep dive
- `resources/data-fetching-complete.md` - Data fetching patterns
- `resources/metadata-api.md` - Metadata API guide
- `resources/server-actions-complete.md` - Server Actions guide
- `resources/rendering-strategies.md` - SSG, ISR, SSR, Streaming
- `resources/routing-patterns.md` - Routing patterns
- `resources/server-client-decision.md` - Server/Client decision guide

### Templates

- `templates/app-router-async-params.tsx` - Async params pattern
- `templates/cache-component-use-cache.tsx` - Cache Components
- `templates/parallel-routes-with-default.tsx` - Parallel routes
- `templates/proxy-migration.ts` - Proxy migration
- `templates/route-handler-api.ts` - Route handlers
- `templates/server-actions-form.tsx` - Server Actions forms
- `templates/layout-template.md` - Layout templates
- `templates/page-template.md` - Page templates

### Scripts

- `scripts/analyze-routing-structure.mjs` - Analyze routing
- `scripts/check-versions.sh` - Check versions
- `scripts/validate-patterns.py` - Validate Next.js patterns

### Official Documentation

- [Next.js Docs](https://nextjs.org/docs)
- [React Docs](https://react.dev)
- [Tailwind CSS Docs](https://tailwindcss.com/docs)

---

**Skill Version**: 1.0.0
**Next.js Versions**: 13+, 15, 16
**Last Updated**: January 2026
