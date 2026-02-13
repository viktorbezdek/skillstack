# Layout Component Template

## Root Layout

```typescript
// app/layout.tsx
import type { Metadata, Viewport } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'

const inter = Inter({
  subsets: ['latin'],
  display: 'swap',
  variable: '--font-inter',
})

export const metadata: Metadata = {
  title: {
    default: '{{SiteName}}',
    template: '%s | {{SiteName}}',
  },
  description: '{{SiteDescription}}',
  keywords: ['{{keyword1}}', '{{keyword2}}'],
  authors: [{ name: '{{AuthorName}}' }],
  creator: '{{CreatorName}}',
  openGraph: {
    type: 'website',
    locale: 'en_US',
    url: '{{SiteUrl}}',
    siteName: '{{SiteName}}',
    images: [
      {
        url: '{{OgImageUrl}}',
        width: 1200,
        height: 630,
        alt: '{{SiteName}}',
      },
    ],
  },
  twitter: {
    card: 'summary_large_image',
    site: '@{{TwitterHandle}}',
    creator: '@{{TwitterHandle}}',
  },
  robots: {
    index: true,
    follow: true,
  },
}

export const viewport: Viewport = {
  width: 'device-width',
  initialScale: 1,
  themeColor: [
    { media: '(prefers-color-scheme: light)', color: '#ffffff' },
    { media: '(prefers-color-scheme: dark)', color: '#000000' },
  ],
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" className={inter.variable}>
      <body className={inter.className}>
        {children}
      </body>
    </html>
  )
}
```

## Root Layout with Providers

```typescript
// app/layout.tsx
import { Providers } from './providers'

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body>
        <Providers>
          {children}
        </Providers>
      </body>
    </html>
  )
}

// app/providers.tsx
'use client'

import { ThemeProvider } from 'next-themes'
import { SessionProvider } from 'next-auth/react'

export function Providers({ children }: { children: React.ReactNode }) {
  return (
    <SessionProvider>
      <ThemeProvider attribute="class" defaultTheme="system" enableSystem>
        {children}
      </ThemeProvider>
    </SessionProvider>
  )
}
```

## Authenticated Group Layout

```typescript
// app/(protected)/layout.tsx
import { redirect } from 'next/navigation'
import { auth } from '@/lib/auth'
import { Sidebar } from '@/components/sidebar'
import { Header } from '@/components/header'

export default async function ProtectedLayout({
  children,
}: {
  children: React.ReactNode
}) {
  const session = await auth()

  if (!session) {
    redirect('/login')
  }

  return (
    <div className="flex min-h-screen">
      <Sidebar user={session.user} />
      <div className="flex flex-1 flex-col">
        <Header user={session.user} />
        <main className="flex-1 p-6">
          {children}
        </main>
      </div>
    </div>
  )
}
```

## Group Layout with Shared UI

```typescript
// app/(marketing)/layout.tsx
import { Header } from '@/components/marketing/header'
import { Footer } from '@/components/marketing/footer'

export default function MarketingLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <>
      <Header />
      <main className="min-h-screen">
        {children}
      </main>
      <Footer />
    </>
  )
}
```

## Parallel Routes Layout

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
    <div className="grid grid-cols-12 gap-6 p-6">
      {/* Main Content */}
      <main className="col-span-8">
        {children}
      </main>

      {/* Side Panel */}
      <aside className="col-span-4 space-y-6">
        <section className="rounded-lg border p-4">
          <h2 className="mb-4 font-semibold">Analytics</h2>
          {analytics}
        </section>

        <section className="rounded-lg border p-4">
          <h2 className="mb-4 font-semibold">Team</h2>
          {team}
        </section>

        <section className="rounded-lg border p-4">
          <h2 className="mb-4 font-semibold">Notifications</h2>
          {notifications}
        </section>
      </aside>
    </div>
  )
}
```

## Metadata Inheritance Layout

```typescript
// app/blog/layout.tsx
import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: {
    default: 'Blog',
    template: '%s | Blog | {{SiteName}}',
  },
  description: 'Latest articles and insights',
  openGraph: {
    type: 'website',
    title: 'Blog',
    description: 'Latest articles and insights',
  },
}

export default function BlogLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <div className="container mx-auto max-w-4xl px-4 py-8">
      {children}
    </div>
  )
}
```

## Template (For Page Transition Animations)

```typescript
// app/template.tsx
'use client'

import { motion } from 'framer-motion'

export default function Template({ children }: { children: React.ReactNode }) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0, y: -20 }}
      transition={{
        type: 'spring',
        stiffness: 260,
        damping: 20,
      }}
    >
      {children}
    </motion.div>
  )
}
```

## Variable Descriptions

| Variable                       | Description      | Example                      |
| ------------------------------ | ---------------- | ---------------------------- |
| `{{SiteName}}`                 | Site name        | `My App`                     |
| `{{SiteDescription}}`          | Site description | `The best web application`   |
| `{{SiteUrl}}`                  | Site URL         | `https://example.com`        |
| `{{OgImageUrl}}`               | OGP image URL    | `https://example.com/og.png` |
| `{{TwitterHandle}}`            | Twitter handle   | `myapp`                      |
| `{{AuthorName}}`               | Author name      | `John Doe`                   |
| `{{CreatorName}}`              | Creator name     | `My Company`                 |
| `{{keyword1}}`, `{{keyword2}}` | SEO keywords     | `web app`, `next.js`         |
