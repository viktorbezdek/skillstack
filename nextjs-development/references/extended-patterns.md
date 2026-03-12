# Next.js Extended Patterns & Examples

Detailed code examples and patterns extracted from the core skill for reference.

## Server vs Client Components - Examples

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
