# Layout Hierarchy Design

## Layout vs Template

| Property        | Layout                              | Template                              |
| --------------- | ----------------------------------- | ------------------------------------- |
| Re-rendering    | Preserved during navigation         | Remounted on every navigation         |
| State retention | Preserved                           | Reset                                 |
| Effect          | Not re-executed                     | Executed on every navigation          |
| Primary use     | Shared UI, heavy initialization     | Page transition animations            |

## Layout Hierarchy Structure

```
app/
├── layout.tsx           # Root Layout (required)
│   ├── (marketing)/
│   │   ├── layout.tsx   # Marketing Layout
│   │   └── page.tsx
│   ├── (dashboard)/
│   │   ├── layout.tsx   # Dashboard Layout
│   │   └── settings/
│   │       ├── layout.tsx  # Settings Layout
│   │       └── page.tsx
```

**Rendering order**:

```
Root Layout
└── Group Layout
    └── Nested Layout
        └── Page
```

## Root Layout

### Required Elements

```typescript
// app/layout.tsx
import { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: {
    default: 'My App',
    template: '%s | My App',  // Template used when overridden by child pages
  },
  description: 'My application description',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
        {children}
      </body>
    </html>
  )
}
```

### Responsibilities of Root Layout

- **Required**: `<html>` and `<body>` tags
- Global CSS
- Font configuration (next/font)
- Site-wide metadata
- Global providers (Theme, Auth, etc.)

### What NOT to Include in Root Layout

- Page-specific navigation
- UI dependent on authentication state
- UI used only by specific Route Groups

## Group Layout

### Implementing Authentication Boundaries

```typescript
// app/(protected)/layout.tsx
import { redirect } from 'next/navigation'
import { auth } from '@/lib/auth'

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
    <div className="flex">
      <Sidebar user={session.user} />
      <main className="flex-1">{children}</main>
    </div>
  )
}
```

### Implementing Shared UI

```typescript
// app/(dashboard)/layout.tsx
export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <div className="min-h-screen">
      <DashboardHeader />
      <div className="flex">
        <DashboardSidebar />
        <main className="flex-1 p-6">{children}</main>
      </div>
    </div>
  )
}
```

## Layout with Parallel Routes

```typescript
// app/dashboard/layout.tsx
export default function DashboardLayout({
  children,
  analytics,
  team,
}: {
  children: React.ReactNode
  analytics: React.ReactNode
  team: React.ReactNode
}) {
  return (
    <div className="grid grid-cols-12 gap-4">
      <main className="col-span-8">{children}</main>
      <aside className="col-span-4 space-y-4">
        {analytics}
        {team}
      </aside>
    </div>
  )
}
```

## Template (Special Cases)

### Page Transition Animations

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
      transition={{ duration: 0.3 }}
    >
      {children}
    </motion.div>
  )
}
```

### Resetting Feedback Forms

```typescript
// app/feedback/template.tsx
// Reset form state on every navigation
export default function FeedbackTemplate({
  children,
}: {
  children: React.ReactNode
}) {
  return <div key={Date.now()}>{children}</div>
}
```

## Design Decision Flow

```
This UI is...
├─ Common across all pages?
│  └─ Yes → Root Layout
├─ Shared across multiple pages?
│  ├─ Needs separation by authentication state?
│  │  └─ Yes → Route Group Layout ((public), (protected), etc.)
│  └─ Shared within a specific feature group?
│     └─ Yes → Group Layout
├─ Needs state reset on navigation?
│  └─ Yes → Template
└─ Page-specific?
   └─ Yes → Implement within the Page
```

## Performance Considerations

### Layout Optimization

```typescript
// ✅ Heavy initialization in Layout (executed only once)
export default async function Layout({ children }: { children: React.ReactNode }) {
  const config = await fetchAppConfig() // Not re-executed on navigation
  return (
    <ConfigProvider config={config}>
      {children}
    </ConfigProvider>
  )
}

// ❌ Heavy processing in Page (executed every time)
export default async function Page() {
  const config = await fetchAppConfig() // Executed on every navigation
  // ...
}
```

### Data Fetch Deduplication

```typescript
// Even if Layout and Page fetch the same data, it is automatically deduplicated
// app/(dashboard)/layout.tsx
export default async function Layout({ children }: { children: React.ReactNode }) {
  const user = await getUser() // This result is cached
  return <UserNav user={user}>{children}</UserNav>
}

// app/(dashboard)/settings/page.tsx
export default async function SettingsPage() {
  const user = await getUser() // Data retrieved from cache (no duplicate request)
  return <SettingsForm user={user} />
}
```

## Checklist

### Root Layout

- [ ] Contains `<html>` and `<body>` tags
- [ ] Global CSS is imported
- [ ] Font is configured with next/font
- [ ] Basic metadata is configured
- [ ] Global providers are set up

### Group Layout

- [ ] Authentication boundaries are properly implemented
- [ ] Shared UI is correctly placed
- [ ] Route Group naming is logical
- [ ] Required metadata is overridden

### General

- [ ] Re-rendering behavior of Layout is understood
- [ ] Template and Layout are used appropriately
- [ ] Heavy processing is placed in Layout
- [ ] Parallel routes are properly received
