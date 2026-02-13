# Server/Client Components Decision Flow

## Basic Decision Flowchart

```
This component...

1. Needs data fetching?
   ├─ Yes
   │  ├─ Server-only resources (DB, file system)?
   │  │  └─ Server Component (async/await)
   │  └─ External API + client interaction?
   │     └─ Server Component + Client Component (separate into children)
   └─ No → Next

2. Needs interactivity?
   ├─ Yes
   │  ├─ Event handlers like onClick, onChange?
   │  │  └─ Client Component ("use client")
   │  ├─ React Hooks like useState, useEffect?
   │  │  └─ Client Component
   │  └─ Context, Custom Hooks?
   │     └─ Client Component (separate Provider)
   └─ No → Next

3. Needs browser APIs?
   ├─ Yes (window, localStorage, document, etc.)
   │  └─ Client Component
   └─ No → Server Component (default)
```

## Server Components

### Characteristics

- **Default**: All components without "use client" are Server Components
- **async/await support**: Can fetch data directly
- **Bundle size**: Not sent to the client
- **Access**: Can directly access server-only resources (DB, environment variables)

### Use Cases

```typescript
// ✅ Server Component - Data fetching
async function UserProfile({ userId }: { userId: string }) {
  const user = await db.user.findUnique({ where: { id: userId } })
  return <div>{user.name}</div>
}

// ✅ Server Component - Static content
function Footer() {
  return <footer>© 2025 Company</footer>
}

// ✅ Server Component - Environment variable access
function ApiInfo() {
  return <div>Version: {process.env.APP_VERSION}</div>
}
```

### Restrictions

```typescript
// ❌ Cannot be used in Server Components
import { useState, useEffect } from "react";

function ServerComponent() {
  const [count, setCount] = useState(0); // Error
  useEffect(() => {}, []); // Error
  const handleClick = () => {}; // Cannot use onClick
}
```

## Client Components

### Characteristics

- **Explicit declaration**: Requires `"use client"` at the top of the file
- **Hooks available**: useState, useEffect, useContext, etc.
- **Event handlers**: onClick, onChange, etc. can be used
- **Browser APIs**: Can access window, localStorage, etc.

### Use Cases

```typescript
'use client'

// ✅ Client Component - Interactive UI
function Counter() {
  const [count, setCount] = useState(0)
  return <button onClick={() => setCount(c => c + 1)}>{count}</button>
}

// ✅ Client Component - Form
function LoginForm() {
  const [email, setEmail] = useState('')
  return <input value={email} onChange={(e) => setEmail(e.target.value)} />
}

// ✅ Client Component - Browser API
function ThemeToggle() {
  const [theme, setTheme] = useState(() =>
    window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'
  )
  return <button onClick={() => setTheme(t => t === 'dark' ? 'light' : 'dark')}>Toggle</button>
}
```

## Boundary Optimization Patterns

### Pattern 1: Place Client Components at the Leaves

```typescript
// ✅ Recommended: Client Components at the lowest level
// Server Component (parent)
async function ProductPage({ id }: { id: string }) {
  const product = await getProduct(id)
  return (
    <div>
      <h1>{product.name}</h1>
      <p>{product.description}</p>
      <AddToCartButton productId={id} />  {/* Client Component */}
    </div>
  )
}

// Client Component (leaf)
'use client'
function AddToCartButton({ productId }: { productId: string }) {
  const [loading, setLoading] = useState(false)
  const handleClick = async () => {
    setLoading(true)
    await addToCart(productId)
    setLoading(false)
  }
  return <button onClick={handleClick} disabled={loading}>Add to Cart</button>
}
```

### Pattern 2: Pass Server Components via children props

```typescript
// Client Component (Provider)
'use client'
function ThemeProvider({ children }: { children: React.ReactNode }) {
  const [theme, setTheme] = useState('light')
  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      {children}  {/* Can contain Server Components */}
    </ThemeContext.Provider>
  )
}

// Server Component (parent)
export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <ThemeProvider>
      <Header />       {/* Server Component */}
      {children}       {/* Server Component */}
      <Footer />       {/* Server Component */}
    </ThemeProvider>
  )
}
```

### Pattern 3: Separating Context Providers

```typescript
// providers.tsx (Client Component)
'use client'
import { SessionProvider } from 'next-auth/react'
import { ThemeProvider } from 'next-themes'

export function Providers({ children }: { children: React.ReactNode }) {
  return (
    <SessionProvider>
      <ThemeProvider>
        {children}
      </ThemeProvider>
    </SessionProvider>
  )
}

// layout.tsx (Server Component)
import { Providers } from './providers'

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html>
      <body>
        <Providers>
          {children}
        </Providers>
      </body>
    </html>
  )
}
```

## Decision Checklist

### Should it be a Server Component?

- [ ] Directly accesses the database
- [ ] Uses environment variables (secrets)
- [ ] Reads from the file system
- [ ] Uses large npm packages (want to exclude from bundle)
- [ ] No interactivity required

### Should it be a Client Component?

- [ ] Uses event handlers like onClick, onChange
- [ ] Uses useState, useReducer, useEffect
- [ ] Consumes Context with useContext
- [ ] Uses custom Hooks
- [ ] Uses browser APIs (window, localStorage)
- [ ] Uses React.lazy, Suspense
