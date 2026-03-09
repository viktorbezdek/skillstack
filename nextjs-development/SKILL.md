---
name: nextjs-development
description: |
  Comprehensive Next.js development skill covering App Router (13+/15/16), Server Components, Server Actions,
  Cache Components, data fetching patterns, and module architecture. Use when building modern Next.js applications,
  implementing routing, data fetching, caching strategies, server-side rendering, or working with React Server Components.
  Covers Next.js 16 breaking changes including async params, proxy.ts migration, and "use cache" directive.

  Keywords: Next.js, App Router, Server Components, Client Components, Server Actions, Cache Components,
  use cache, async params, proxy.ts, middleware, layouts, loading states, error boundaries, streaming,
  Suspense, parallel routes, intercepting routes, route groups, metadata API, SEO, data fetching,
  ISR, SSG, SSR, React 19, Tailwind CSS, TypeScript, Supabase, TanStack Query
license: MIT
metadata:
  version: 1.0.0
  merged_from:
    - frontend-development-guidelines-nextjs-tailwind
    - nextjs-module-builder
    - nextjs-app-router---production-patterns
    - nextjs-15-app-router-specialist
    - nextjs-app-router
  nextjs_versions: ["13+", "15", "16"]
  react_versions: ["18", "19", "19.2"]
  node_version: "20.9+"
allowed-tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep", "WebFetch"]
---

# Next.js Development - Comprehensive Guide

A unified skill merging best practices for Next.js development, covering App Router patterns, Server Components, data fetching, caching strategies, and module architecture.

---

## Table of Contents

1. [When to Use This Skill](#when-to-use-this-skill)
2. [Critical Rules](#critical-rules)
3. [Next.js 16 Breaking Changes](#nextjs-16-breaking-changes)
4. [Server vs Client Components](#server-vs-client-components)
5. [App Router Structure](#app-router-structure)
6. [Data Fetching Patterns](#data-fetching-patterns)
7. [Caching Strategies](#caching-strategies)
8. [Server Actions](#server-actions)
9. [Routing Patterns](#routing-patterns)
10. [Module Architecture](#module-architecture)
11. [Metadata & SEO](#metadata--seo)
12. [Performance Optimization](#performance-optimization)
13. [TypeScript Standards](#typescript-standards)
14. [Resources](#resources)

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

```typescript
// WRONG - syntax error
'use client'
export default async function BadComponent() {
  const data = await fetch('/api/data')
  return <div>{data}</div>
}

// CORRECT - use Server Component or useEffect
export default async function GoodComponent() {
  const data = await fetch('/api/data')
  return <div>{data}</div>
}
```

### 4. Always specify cache strategy for fetch()

```typescript
// CORRECT - explicit cache strategy
const data = await fetch('/api/data', { cache: 'no-store' })
const data = await fetch('/api/data', { cache: 'force-cache' })
const data = await fetch('/api/data', { next: { revalidate: 3600 } })

// AVOID - unclear caching behavior
const data = await fetch('/api/data')
```

### 5. Await async APIs in Next.js 16

```typescript
// CORRECT (Next.js 16)
export default async function Page({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params
  const cookieStore = await cookies()
  const headersList = await headers()
}

// WRONG (Next.js 15 pattern - deprecated)
export default function Page({ params }: { params: { id: string } }) {
  const id = params.id // Error in Next.js 16
}
```

---

## Next.js 16 Breaking Changes

### 1. Async Route Parameters

`params`, `searchParams`, `cookies()`, `headers()`, and `draftMode()` are now **async**.

```typescript
// Next.js 16 Pattern
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

```
app/
├── @modal/
│   ├── login/page.tsx
│   └── default.tsx    ← REQUIRED in Next.js 16
└── layout.tsx
```

```typescript
// app/@modal/default.tsx
export default function ModalDefault() {
  return null
}
```

### 4. Cache Components with "use cache"

Next.js 16 introduces opt-in caching:

```typescript
'use cache'

export async function ExpensiveComponent() {
  const data = await fetch('https://api.example.com/data')
  return <div>{data}</div>
}
```

### 5. Updated revalidateTag() API

```typescript
// Next.js 16 - requires second argument
revalidateTag('posts', 'max')

// Cache life profiles: 'max', 'hours', 'days', 'weeks', 'default'
```

---

## Server vs Client Components

### Decision Tree

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

### Server Component (Default)

```typescript
// app/posts/page.tsx
export default async function PostsPage() {
  const posts = await db.post.findMany()
  return (
    <div>
      {posts.map(post => <PostCard key={post.id} post={post} />)}
    </div>
  )
}
```

### Client Component

```typescript
'use client'

import { useState } from 'react'

export function Counter() {
  const [count, setCount] = useState(0)
  return (
    <button onClick={() => setCount(count + 1)}>
      Count: {count}
    </button>
  )
}
```

### Composition Pattern

```typescript
// Server Component imports Client Component
import { InteractiveButton } from './interactive-button'

export default async function Page() {
  const data = await fetch('/api/data').then(r => r.json())
  return (
    <div>
      <h1>{data.title}</h1>
      <InteractiveButton /> {/* Client inside Server */}
    </div>
  )
}
```

---

## App Router Structure

### File Conventions

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
    loading.tsx    # Blog loading state
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

### Layouts

```typescript
// app/layout.tsx - Root Layout
export default function RootLayout({
  children
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>
        <Navigation />
        <main>{children}</main>
        <Footer />
      </body>
    </html>
  )
}

// app/dashboard/layout.tsx - Nested Layout
export default function DashboardLayout({
  children
}: {
  children: React.ReactNode
}) {
  return (
    <div className="dashboard">
      <Sidebar />
      <section>{children}</section>
    </div>
  )
}
```

### Loading & Error States

```typescript
// app/blog/loading.tsx
export default function Loading() {
  return <Skeleton count={3} />
}

// app/blog/error.tsx
'use client'

export default function Error({
  error,
  reset
}: {
  error: Error
  reset: () => void
}) {
  return (
    <div>
      <h2>Something went wrong!</h2>
      <button onClick={reset}>Try again</button>
    </div>
  )
}
```

---

## Data Fetching Patterns

### Server Component Data Fetching

```typescript
// Parallel fetching (recommended)
export default async function Dashboard() {
  const [user, posts, comments] = await Promise.all([
    fetch('/api/user').then(r => r.json()),
    fetch('/api/posts').then(r => r.json()),
    fetch('/api/comments').then(r => r.json()),
  ])

  return (
    <div>
      <UserInfo user={user} />
      <PostsList posts={posts} />
      <CommentsList comments={comments} />
    </div>
  )
}
```

### Streaming with Suspense

```typescript
import { Suspense } from 'react'

export default function Page() {
  return (
    <div>
      <h1>Dashboard</h1>
      <Suspense fallback={<PostsSkeleton />}>
        <Posts /> {/* Streams when ready */}
      </Suspense>
      <Suspense fallback={<CommentsSkeleton />}>
        <Comments /> {/* Streams independently */}
      </Suspense>
    </div>
  )
}

async function Posts() {
  const posts = await fetch('/api/posts').then(r => r.json())
  return <PostList posts={posts} />
}
```

### Client-Side Fetching (TanStack Query)

```typescript
'use client'

import { useSuspenseQuery } from '@tanstack/react-query'

export function Posts() {
  const { data: posts } = useSuspenseQuery({
    queryKey: ['posts'],
    queryFn: () => fetch('/api/posts').then(r => r.json()),
  })

  return <PostList posts={posts} />
}
```

---

## Caching Strategies

### Cache Configuration

```typescript
// No caching (always fresh)
const data = await fetch('/api/data', { cache: 'no-store' })

// Force cache (static)
const data = await fetch('/api/data', { cache: 'force-cache' })

// ISR (revalidate every hour)
const data = await fetch('/api/data', { next: { revalidate: 3600 } })

// Tagged cache
const data = await fetch('/api/posts', { next: { tags: ['posts'] } })
```

### Cache Components (Next.js 16)

```typescript
'use cache'

export async function CachedComponent() {
  const data = await fetch('https://api.example.com/data')
  return <div>{data}</div>
}
```

### Revalidation

```typescript
'use server'

import { revalidateTag, revalidatePath } from 'next/cache'

export async function updatePost(id: string) {
  await db.post.update({ where: { id }, data: { ... } })

  revalidateTag('posts', 'max')  // Next.js 16
  revalidatePath('/blog')
}
```

---

## Server Actions

### Basic Form Action

```typescript
// app/actions.ts
'use server'

import { revalidateTag } from 'next/cache'
import { redirect } from 'next/navigation'

export async function createPost(formData: FormData) {
  const title = formData.get('title') as string
  const content = formData.get('content') as string

  await db.post.create({ data: { title, content } })

  revalidateTag('posts', 'max')
  redirect('/posts')
}

// Usage
export default function NewPostPage() {
  return (
    <form action={createPost}>
      <input name="title" required />
      <textarea name="content" required />
      <button type="submit">Create</button>
    </form>
  )
}
```

### With Loading State

```typescript
'use client'

import { useFormStatus } from 'react-dom'

function SubmitButton() {
  const { pending } = useFormStatus()
  return (
    <button type="submit" disabled={pending}>
      {pending ? 'Creating...' : 'Create'}
    </button>
  )
}
```

### With Validation

```typescript
'use server'

import { z } from 'zod'

const PostSchema = z.object({
  title: z.string().min(3),
  content: z.string().min(10),
})

export async function createPost(formData: FormData) {
  const parsed = PostSchema.safeParse({
    title: formData.get('title'),
    content: formData.get('content'),
  })

  if (!parsed.success) {
    return { errors: parsed.error.flatten().fieldErrors }
  }

  await db.post.create({ data: parsed.data })
  revalidateTag('posts', 'max')
}
```

### Optimistic Updates

```typescript
'use client'

import { useOptimistic } from 'react'

export function LikeButton({ postId, initialLikes }: Props) {
  const [optimisticLikes, addOptimisticLike] = useOptimistic(
    initialLikes,
    (state, amount: number) => state + amount
  )

  async function handleLike() {
    addOptimisticLike(1)
    await likePost(postId)
  }

  return <button onClick={handleLike}>{optimisticLikes} likes</button>
}
```

---

## Routing Patterns

### Dynamic Routes

```typescript
// app/blog/[slug]/page.tsx
export default async function BlogPost({
  params
}: {
  params: Promise<{ slug: string }>
}) {
  const { slug } = await params
  const post = await getPost(slug)
  return <article>{post.content}</article>
}

export async function generateStaticParams() {
  const posts = await getPosts()
  return posts.map(post => ({ slug: post.slug }))
}
```

### Route Groups

```
app/
├── (marketing)/
│   ├── layout.tsx    # Marketing layout
│   ├── about/page.tsx    # /about
│   └── contact/page.tsx  # /contact
├── (shop)/
│   ├── layout.tsx    # Shop layout
│   └── products/page.tsx # /products
```

### Parallel Routes

```typescript
// app/dashboard/layout.tsx
export default function Layout({
  children,
  analytics,
  team,
}: {
  children: React.ReactNode
  analytics: React.ReactNode
  team: React.ReactNode
}) {
  return (
    <div className="grid">
      <main>{children}</main>
      <aside>{analytics}</aside>
      <aside>{team}</aside>
    </div>
  )
}
```

### Route Handlers (API)

```typescript
// app/api/posts/route.ts
import { NextResponse } from 'next/server'

export async function GET() {
  const posts = await db.post.findMany()
  return NextResponse.json(posts)
}

export async function POST(request: Request) {
  const body = await request.json()
  const post = await db.post.create({ data: body })
  return NextResponse.json(post, { status: 201 })
}

// app/api/posts/[id]/route.ts
export async function GET(
  request: Request,
  { params }: { params: Promise<{ id: string }> }
) {
  const { id } = await params
  const post = await db.post.findUnique({ where: { id } })

  if (!post) {
    return NextResponse.json({ error: 'Not found' }, { status: 404 })
  }

  return NextResponse.json(post)
}
```

---

## Module Architecture

For building complete feature modules with CRUD operations, follow the 5-layer pattern:

### Layer Structure

```
app/(routes)/[module]/
├── page.tsx                    # List view
├── new/page.tsx               # Create form
├── [id]/
│   ├── page.tsx              # Detail view
│   └── edit/page.tsx         # Edit form
└── _components/
    ├── data-table-schema.ts
    ├── columns.tsx
    ├── [entity]-form.tsx
    └── row-actions.tsx

lib/services/[module]/
└── [entity]-service.ts

hooks/[module]/
└── use-[entity].ts

types/
└── [module].ts
```

### Types Layer

```typescript
// types/posts.ts
export interface Post {
  id: string
  title: string
  content: string
  is_active: boolean
  created_at: string
  updated_at: string
}

export interface CreatePostDto {
  title: string
  content: string
}

export interface UpdatePostDto {
  id: string
  title?: string
  content?: string
  is_active?: boolean
}
```

### Service Layer

```typescript
// lib/services/posts/post-service.ts
export class PostService {
  static async getPosts(filters: PostFilters = {}, page = 1, pageSize = 10) {
    let query = supabase.from('posts').select('*', { count: 'exact' })

    if (filters.search) {
      query = query.ilike('title', `%${filters.search}%`)
    }

    const from = (page - 1) * pageSize
    query = query.range(from, from + pageSize - 1)

    const { data, error, count } = await query
    if (error) throw error

    return { data: data || [], total: count || 0, page, pageSize }
  }

  static async createPost(dto: CreatePostDto) {
    const { data, error } = await supabase
      .from('posts')
      .insert([dto])
      .select()
      .single()

    if (error) throw error
    return data
  }
}
```

---

## Metadata & SEO

### Static Metadata

```typescript
import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: {
    default: 'My App',
    template: '%s | My App'
  },
  description: 'My awesome Next.js app',
  openGraph: {
    title: 'My App',
    description: 'My awesome Next.js app',
    images: ['/og-image.jpg'],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'My App',
  },
}
```

### Dynamic Metadata

```typescript
export async function generateMetadata({
  params
}: {
  params: Promise<{ slug: string }>
}): Promise<Metadata> {
  const { slug } = await params
  const post = await getPost(slug)

  return {
    title: post.title,
    description: post.excerpt,
    openGraph: {
      title: post.title,
      images: [post.coverImage],
    },
  }
}
```

### Sitemap

```typescript
// app/sitemap.ts
import type { MetadataRoute } from 'next'

export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
  const posts = await fetch('/api/posts').then(r => r.json())

  return [
    { url: 'https://example.com', lastModified: new Date(), priority: 1 },
    ...posts.map((post: Post) => ({
      url: `https://example.com/blog/${post.slug}`,
      lastModified: post.updatedAt,
      priority: 0.8,
    })),
  ]
}
```

---

## Performance Optimization

### Lazy Loading

```typescript
import dynamic from 'next/dynamic'

const HeavyChart = dynamic(() => import('./chart'), {
  loading: () => <ChartSkeleton />,
  ssr: false,
})
```

### Image Optimization

```typescript
import Image from 'next/image'

<Image
  src="/hero.jpg"
  alt="Hero"
  width={1200}
  height={600}
  priority // Above the fold
/>

<Image
  src="/photo.jpg"
  alt="Photo"
  fill
  style={{ objectFit: 'cover' }}
  sizes="(max-width: 768px) 100vw, 50vw"
/>
```

### Font Optimization

```typescript
import { Inter } from 'next/font/google'

const inter = Inter({
  subsets: ['latin'],
  display: 'swap',
  variable: '--font-inter',
})

export default function RootLayout({ children }) {
  return (
    <html className={inter.variable}>
      <body>{children}</body>
    </html>
  )
}
```

---

## TypeScript Standards

### Strict Configuration

```json
{
  "compilerOptions": {
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "noImplicitOverride": true,
    "baseUrl": ".",
    "paths": {
      "@/*": ["./*"],
      "@/components/*": ["./app/components/*"],
      "@/lib/*": ["./lib/*"]
    }
  }
}
```

### Component Props

```typescript
interface PostCardProps {
  post: Post
  onDelete?: (id: string) => void
}

export function PostCard({ post, onDelete }: PostCardProps) {
  return (
    <div>
      <h2>{post.title}</h2>
      {onDelete && (
        <button onClick={() => onDelete(post.id)}>Delete</button>
      )}
    </div>
  )
}
```

---

## Resources

### Reference Files

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







