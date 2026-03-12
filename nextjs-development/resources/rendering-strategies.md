# Rendering Strategies Guide

## Strategy Overview

| Strategy          | Generation Timing              | Update Method       | Use Cases                    |
| ----------------- | ------------------------------ | ------------------- | ---------------------------- |
| Static Generation | At build time                  | Rebuild             | Static content, blogs        |
| ISR               | At build time + revalidation   | revalidate interval | Periodically updated content |
| Dynamic Rendering | At request time                | Every time          | User-specific data           |
| Streaming SSR     | At request time (progressively)| Every time          | Large datasets               |

## Decision Flowchart

```
This page is...
├─ Completely static content? (Same content for all users)
│  └─ Yes → Static Generation
├─ Needs periodic updates? (Every hour, daily, etc.)
│  └─ Yes → ISR (configure revalidate)
├─ Changes on every request?
│  └─ Yes → Dynamic Rendering
├─ User-specific data? (Authentication, cookies)
│  └─ Yes → Dynamic Rendering
└─ Large dataset? (Progressive display is beneficial)
   └─ Yes → Streaming SSR + Suspense
```

## Static Generation

### Configuration

```typescript
// app/about/page.tsx
// Static Generation by default (when nothing is configured)

// Explicitly configured
export const dynamic = "force-static";
export const revalidate = false; // No revalidation
```

### Static Generation with Dynamic Parameters

```typescript
// app/blog/[slug]/page.tsx
export async function generateStaticParams() {
  const posts = await getPosts()
  return posts.map((post) => ({
    slug: post.slug,
  }))
}

export default async function BlogPost({
  params,
}: {
  params: Promise<{ slug: string }>
}) {
  const { slug } = await params
  const post = await getPost(slug)
  return <article>{post.content}</article>
}
```

### Use Cases

- Marketing pages
- Blog posts (low update frequency)
- Documentation
- Product catalogs (no inventory changes)

## ISR (Incremental Static Regeneration)

### Configuration

```typescript
// Time-based revalidation
export const revalidate = 3600; // Revalidate every hour

// Or configure per fetch
const data = await fetch("https://api.example.com/data", {
  next: { revalidate: 3600 },
});
```

### On-Demand Revalidation

```typescript
// app/api/revalidate/route.ts
import { revalidatePath, revalidateTag } from "next/cache";

export async function POST(request: Request) {
  const { path, tag, secret } = await request.json();

  // Secret check
  if (secret !== process.env.REVALIDATION_SECRET) {
    return Response.json({ error: "Invalid secret" }, { status: 401 });
  }

  // Path-based revalidation
  if (path) {
    revalidatePath(path);
  }

  // Tag-based revalidation
  if (tag) {
    revalidateTag(tag);
  }

  return Response.json({ revalidated: true });
}
```

### Use Cases

- Blogs (with comments)
- E-commerce sites (inventory updated every hour)
- News sites
- CMS-driven content

## Dynamic Rendering

### Configuration

```typescript
// Explicitly set Dynamic Rendering
export const dynamic = "force-dynamic";

// Or automatically becomes Dynamic by using dynamic functions
import { cookies, headers } from "next/headers";

export default async function Page() {
  const cookieStore = await cookies();
  const headersList = await headers();
  // At this point it becomes Dynamic Rendering
}
```

### Dynamic Functions

Using any of the following automatically enables Dynamic Rendering:

- `cookies()`
- `headers()`
- `searchParams` prop
- `unstable_noStore()`

### Use Cases

- Dashboards (user-specific)
- Settings pages
- Search results (using searchParams)
- Pages requiring authentication

## Streaming SSR

### Automatic Suspense with loading.tsx

```typescript
// app/dashboard/loading.tsx
export default function Loading() {
  return <DashboardSkeleton />
}

// app/dashboard/page.tsx
export default async function Dashboard() {
  const data = await fetchDashboardData() // Takes time
  return <DashboardContent data={data} />
}
```

### Manual Suspense Boundaries

```typescript
import { Suspense } from 'react'

export default function Page() {
  return (
    <div>
      <h1>Dashboard</h1>

      {/* Display important content first */}
      <Suspense fallback={<StatsSkeleton />}>
        <Stats />
      </Suspense>

      {/* Time-consuming content loads later */}
      <Suspense fallback={<ChartSkeleton />}>
        <SlowChart />
      </Suspense>

      <Suspense fallback={<TableSkeleton />}>
        <SlowTable />
      </Suspense>
    </div>
  )
}
```

### Use Cases

- Dashboards (multiple data sources)
- Analytics pages
- Report pages
- Large dataset listings

## Cache Configuration Summary

### Segment Config Options

```typescript
// Configurable per page/layout
export const dynamic = 'auto' | 'force-dynamic' | 'error' | 'force-static'
export const revalidate = false | 0 | number
export const fetchCache = 'auto' | 'default-cache' | 'only-cache' | 'force-cache' | 'force-no-store' | 'default-no-store' | 'only-no-store'
export const runtime = 'nodejs' | 'edge'
export const preferredRegion = 'auto' | 'global' | 'home' | string | string[]
```

### fetch Options

```typescript
// Cache configuration
fetch(url, { cache: "force-cache" }); // Default, uses cache
fetch(url, { cache: "no-store" }); // Cache disabled

// Revalidation configuration
fetch(url, { next: { revalidate: 3600 } }); // Time-based
fetch(url, { next: { tags: ["posts"] } }); // Tag-based
```

## Performance Comparison

| Strategy  | TTFB            | TTI    | SEO  | Server Load |
| --------- | --------------- | ------ | ---- | ----------- |
| Static    | Fastest         | Fastest| Best | Minimal     |
| ISR       | Fast            | Fast   | Good | Low         |
| Dynamic   | Slow            | Normal | Good | High        |
| Streaming | Fast (partial)  | Normal | Good | Medium      |
