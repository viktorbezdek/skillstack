# Routing Patterns Reference

## Basic Routing

### Folder Structure and URL Mapping

```
app/
├── page.tsx           → /
├── about/
│   └── page.tsx       → /about
├── blog/
│   ├── page.tsx       → /blog
│   └── [slug]/
│       └── page.tsx   → /blog/hello-world
└── shop/
    └── [...slug]/
        └── page.tsx   → /shop/a/b/c
```

### Special File Priority

```
app/dashboard/
├── layout.tsx     # 1. Wraps first
├── template.tsx   # 2. Wraps inside layout
├── loading.tsx    # 3. Suspense boundary
├── error.tsx      # 4. ErrorBoundary
├── not-found.tsx  # 5. 404 UI
└── page.tsx       # 6. Actual page content
```

## Dynamic Routes

### Single Dynamic Segment [slug]

```typescript
// app/blog/[slug]/page.tsx
export default async function BlogPost({
  params,
}: {
  params: Promise<{ slug: string }>
}) {
  const { slug } = await params
  return <article>{/* Use slug */}</article>
}

// Static path generation (optional)
export async function generateStaticParams() {
  const posts = await getPosts()
  return posts.map((post) => ({ slug: post.slug }))
}
```

### Catch-all Segment [...slug]

```typescript
// app/docs/[...slug]/page.tsx
// /docs/a → { slug: ['a'] }
// /docs/a/b → { slug: ['a', 'b'] }
// /docs/a/b/c → { slug: ['a', 'b', 'c'] }
export default async function DocsPage({
  params,
}: {
  params: Promise<{ slug: string[] }>
}) {
  const { slug } = await params
  return <div>{slug.join('/')}</div>
}
```

### Optional Catch-all [[...slug]]

```typescript
// app/shop/[[...slug]]/page.tsx
// /shop → { slug: undefined }
// /shop/a → { slug: ['a'] }
// /shop/a/b → { slug: ['a', 'b'] }
```

## Route Groups

### Logical Grouping (Does Not Affect URL)

```
app/
├── (marketing)/
│   ├── layout.tsx     # Marketing layout
│   ├── page.tsx       → /
│   └── about/
│       └── page.tsx   → /about
├── (shop)/
│   ├── layout.tsx     # Shop layout
│   └── products/
│       └── page.tsx   → /products
└── (dashboard)/
    ├── layout.tsx     # Dashboard layout (authentication required)
    └── settings/
        └── page.tsx   → /settings
```

### Authentication Boundary Implementation Example

```
app/
├── (public)/           # No authentication required
│   ├── layout.tsx
│   ├── page.tsx        → /
│   └── login/
│       └── page.tsx    → /login
└── (protected)/        # Authentication required
    ├── layout.tsx      # Contains AuthGuard
    ├── dashboard/
    │   └── page.tsx    → /dashboard
    └── settings/
        └── page.tsx    → /settings
```

## Parallel Routes

### @folder Syntax

```
app/dashboard/
├── layout.tsx          # Receives parallel routes
├── page.tsx
├── @analytics/
│   └── page.tsx        # Rendered simultaneously
├── @team/
│   └── page.tsx        # Rendered simultaneously
└── @notifications/
    ├── page.tsx
    └── loading.tsx     # Independent loading state
```

```typescript
// app/dashboard/layout.tsx
export default function DashboardLayout({
  children,
  analytics,
  team,
  notifications,
}: {
  children: React.ReactNode
  analytics: React.ReactNode
  team: React.ReactNode
  notifications: React.ReactNode
}) {
  return (
    <div className="grid grid-cols-3">
      <div>{children}</div>
      <div>{analytics}</div>
      <div>{team}</div>
      <div>{notifications}</div>
    </div>
  )
}
```

## Intercepting Routes

### (..) Syntax

```
app/
├── feed/
│   └── page.tsx            → /feed
├── photo/
│   └── [id]/
│       └── page.tsx        → /photo/123 (direct access)
└── @modal/
    └── (.)photo/
        └── [id]/
            └── page.tsx    → Intercepted in modal
```

### Interception Syntax Reference

| Syntax     | Description                    |
| ---------- | ------------------------------ |
| `(.)`      | Matches the same level         |
| `(..)`     | Matches one level up           |
| `(..)(..)` | Matches two levels up          |
| `(...)`    | Matches from the root          |

## Private Folders

### \_folder (Excluded from Routing)

```
app/
├── _components/        # Not included in routing
│   └── Button.tsx
├── _lib/               # Not included in routing
│   └── utils.ts
└── dashboard/
    └── page.tsx
```

## Project-Specific Structure Example

```
app/
├── api/                        # RESTful API Endpoints
│   ├── webhook/
│   │   └── generic/
│   │       └── route.ts       # POST /api/webhook/generic
│   ├── agent/
│   │   ├── upload/
│   │   │   └── route.ts       # POST /api/agent/upload
│   │   └── poll/
│   │       └── route.ts       # GET /api/agent/poll
│   └── health/
│       └── route.ts           # GET /api/health
├── (public)/
│   ├── layout.tsx
│   └── page.tsx               # Dashboard (/)
└── (dashboard)/
    ├── layout.tsx             # Authentication required layout
    └── settings/
        └── page.tsx           # /settings
```
