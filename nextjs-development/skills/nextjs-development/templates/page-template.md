# Page Component Template

## Basic Server Component Page

```typescript
// app/[feature]/page.tsx
import { Metadata } from 'next'

export const metadata: Metadata = {
  title: '{{PageTitle}}',
  description: '{{PageDescription}}',
}

export default async function {{PageName}}Page() {
  // Server Component: can fetch data
  const data = await fetchData()

  return (
    <main>
      <h1>{{PageTitle}}</h1>
      {/* Content */}
    </main>
  )
}
```

## Dynamic Route Page

```typescript
// app/{{resource}}/[{{param}}]/page.tsx
import { Metadata } from 'next'
import { notFound } from 'next/navigation'

type Props = {
  params: Promise<{ {{param}}: string }>
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { {{param}} } = await params
  const item = await getItem({{param}})

  if (!item) {
    return { title: 'Not Found' }
  }

  return {
    title: item.title,
    description: item.description,
    openGraph: {
      title: item.title,
      description: item.description,
      images: [item.image],
    },
  }
}

export async function generateStaticParams() {
  const items = await getAllItems()
  return items.map((item) => ({
    {{param}}: item.{{param}},
  }))
}

export default async function {{PageName}}Page({ params }: Props) {
  const { {{param}} } = await params
  const item = await getItem({{param}})

  if (!item) {
    notFound()
  }

  return (
    <article>
      <h1>{item.title}</h1>
      {/* Content */}
    </article>
  )
}
```

## Page with Client Component

```typescript
// app/{{feature}}/page.tsx
import { Suspense } from 'react'
import { InteractiveSection } from './interactive-section'
import { DataSkeleton } from './data-skeleton'

export default async function {{PageName}}Page() {
  // Fetch data on the server side
  const initialData = await fetchInitialData()

  return (
    <main>
      <h1>{{PageTitle}}</h1>

      {/* Static content (Server Component) */}
      <section>
        <StaticContent data={initialData} />
      </section>

      {/* Interactive section (Client Component) */}
      <Suspense fallback={<DataSkeleton />}>
        <InteractiveSection initialData={initialData} />
      </Suspense>
    </main>
  )
}
```

## Page with ISR Configuration

```typescript
// app/{{feature}}/page.tsx

// ISR: revalidate every hour
export const revalidate = 3600

export default async function {{PageName}}Page() {
  const data = await fetch('{{apiUrl}}', {
    next: { revalidate: 3600 },
  }).then(res => res.json())

  return (
    <main>
      <h1>{{PageTitle}}</h1>
      <p>Last updated: {new Date().toISOString()}</p>
      {/* Content */}
    </main>
  )
}
```

## Dynamic Rendering Page

```typescript
// app/{{feature}}/page.tsx
import { cookies, headers } from 'next/headers'

// Force dynamic rendering
export const dynamic = 'force-dynamic'

export default async function {{PageName}}Page() {
  const cookieStore = await cookies()
  const headersList = await headers()

  const userPreference = cookieStore.get('preference')?.value
  const userAgent = headersList.get('user-agent')

  return (
    <main>
      <h1>{{PageTitle}}</h1>
      {/* User-specific content */}
    </main>
  )
}
```

## Page Using searchParams

```typescript
// app/{{feature}}/page.tsx
type Props = {
  searchParams: Promise<{ [key: string]: string | string[] | undefined }>
}

export default async function {{PageName}}Page({ searchParams }: Props) {
  const params = await searchParams
  const query = typeof params.q === 'string' ? params.q : ''
  const page = typeof params.page === 'string' ? parseInt(params.page, 10) : 1

  const results = await search(query, page)

  return (
    <main>
      <h1>Search Results for "{query}"</h1>
      <SearchResults results={results} />
      <Pagination currentPage={page} />
    </main>
  )
}
```

## Variable Descriptions

| Variable              | Description                         | Example                              |
| --------------------- | ----------------------------------- | ------------------------------------ |
| `{{PageName}}`        | Page component name (PascalCase)    | `BlogPost`, `UserProfile`            |
| `{{PageTitle}}`       | Page title                          | `Blog Post`, `User Profile`          |
| `{{PageDescription}}` | Meta description                    | `Latest blog post list`              |
| `{{feature}}`         | Feature name (kebab-case)           | `blog`, `user-profile`               |
| `{{resource}}`        | Resource name (plural)              | `posts`, `users`                     |
| `{{param}}`           | Dynamic parameter name              | `slug`, `id`, `username`             |
| `{{apiUrl}}`          | Data fetch URL                      | `https://api.example.com/data`       |
