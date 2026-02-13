---
name: react-development
description: Build production-grade React applications with Next.js App Router, shadcn/ui components, optimized hooks, and Bulletproof React architecture.
triggers:
  - React
  - React component
  - React hook
  - useState
  - useEffect
  - shadcn
  - JSX
  - TSX
  - useReducer
  - useContext
  - React testing
---

# React Development Skill

A comprehensive skill for building modern React applications, covering component architecture, hooks optimization, Next.js patterns, and code quality auditing.

---

## Overview

This skill combines expertise from 7 specialized React development skills:

1. **Next.js Module Builder** - Full-stack development with Next.js 15 App Router + Supabase
2. **shadcn/ui Component Library** - Component architecture with Tailwind CSS and CVA
3. **fpkit Component Builder** - Building library components for @fpkit/acss
4. **Bulletproof React Auditor** - Code quality auditing against best practices
5. **fpkit Developer** - Using @fpkit/acss components in applications
6. **React Hooks Advanced** - Advanced hooks patterns and optimization
7. **React Hooks Best Practices** - Hooks anti-patterns and correct usage

---

## Quick Start

### When to Use This Skill

Use this skill when:
- Building React applications with Next.js App Router
- Creating reusable component libraries
- Optimizing React hooks usage
- Auditing React codebase quality
- Implementing accessible, well-tested components
- Setting up shadcn/ui or fpkit component systems

### Decision Tree

```
What are you building?
|
+-- Full-stack Next.js app?
|   --> See: Next.js Architecture (Section 1)
|
+-- Component library?
|   +-- Using shadcn/ui? --> See: shadcn/ui Patterns (Section 2)
|   +-- Using fpkit? --> See: fpkit Patterns (references/extended-patterns.md)
|
+-- Optimizing existing React code?
|   +-- Hooks issues? --> See: Hooks Best Practices (Section 3)
|   +-- Architecture audit? --> See: Bulletproof Audit (references/extended-patterns.md)
```

---

## Section 1: Next.js Architecture

### 5-Layer Architecture

```
Types --> Services --> Hooks --> Components --> Pages

src/
  types/           # TypeScript interfaces (database.types.ts)
  lib/services/    # Server-side data access (users.service.ts)
  hooks/           # Client-side data hooks (use-users.ts)
  components/      # UI components (user-card.tsx)
  app/             # Routes and pages (app/users/page.tsx)
```

### Key Patterns

**Services Layer** (Server-side only):
```typescript
// lib/services/users.service.ts
import { createClient } from '@/lib/supabase/server'

export async function getUsers() {
  const supabase = await createClient()
  const { data, error } = await supabase.from('users').select('*')
  if (error) throw error
  return data
}
```

**Hooks Layer** (Client-side):
```typescript
// hooks/use-users.ts
'use client'
import { useQuery } from '@tanstack/react-query'

export function useUsers() {
  return useQuery({
    queryKey: ['users'],
    queryFn: () => fetch('/api/users').then(r => r.json())
  })
}
```

---

## Section 2: shadcn/ui Component Architecture

### CVA Variants Pattern

```typescript
import { cva, type VariantProps } from 'class-variance-authority'

const buttonVariants = cva(
  'inline-flex items-center justify-center rounded-md text-sm font-medium',
  {
    variants: {
      variant: {
        default: 'bg-primary text-primary-foreground',
        secondary: 'bg-secondary text-secondary-foreground',
        outline: 'border border-input bg-background',
      },
      size: {
        default: 'h-10 px-4 py-2',
        sm: 'h-9 rounded-md px-3',
        lg: 'h-11 rounded-md px-8',
      },
    },
    defaultVariants: { variant: 'default', size: 'default' },
  }
)
```

### Scripts
- `scripts/shadcn-setup-tailwind.py` - Generate Tailwind config with shadcn defaults
- `scripts/shadcn-generate-component.py` - Scaffold new shadcn-style components

---

## Section 3: React Hooks Best Practices

### Core Principle

> "The best hook is the one you don't need to write."

### Common Anti-Patterns

**Derived State**: Don't use `useState` + `useEffect` for derived values. Calculate during render instead.

**Event Response**: Don't use `useEffect` for user actions. Handle in event handlers directly.

**Props-to-State**: Don't sync props to state. Use `key` prop for component reset.

**Premature Memoization**: Don't `useMemo`/`useCallback` cheap operations. Just calculate them.

### When to Use Memoization

Only use `useMemo`/`useCallback` when:
1. Expensive computation (O(n log n) or worse)
2. Callback passed to memoized child component
3. Value used in dependency array of other hooks

### Dependency Array Rules

1. Include all reactive values used inside the effect
2. Use functional updates to avoid state dependencies
3. Use refs for values that shouldn't trigger re-runs
4. Never suppress ESLint exhaustive-deps warnings

---

## Best Practices Summary

### Do
- Use the 5-layer architecture for Next.js apps
- Calculate derived values during render (not in effects)
- Handle user actions in event handlers
- Use React Query/SWR for server state
- Keep components < 300 lines
- Use CSS variables for theming
- Follow accessibility patterns (WCAG 2.1 AA)

### Don't
- Store derived state with useState + useEffect
- Use useEffect for event responses
- Sync props to state (use key for reset)
- Prematurely memoize cheap operations
- Suppress ESLint exhaustive-deps warnings
- Create components with > 10 props
- Skip keyboard accessibility

See [Extended Patterns](references/extended-patterns.md) for fpkit component development, Bulletproof React auditing, detailed hooks anti-patterns, templates, and complete file reference.

---

## Resources

- [Next.js Documentation](https://nextjs.org/docs)
- [shadcn/ui](https://ui.shadcn.com/)
- [fpkit Repository](https://github.com/shawn-sandy/acss)
- [Bulletproof React](https://github.com/alan2207/bulletproof-react)
- [React Docs - Rules of Hooks](https://react.dev/reference/rules/rules-of-hooks)
- [TanStack Query](https://tanstack.com/query)
- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
