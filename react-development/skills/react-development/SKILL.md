---
name: react-development
description: React-specific development patterns including hooks (useState, useEffect, useReducer, useContext), component architecture, state management, shadcn/ui integration, JSX/TSX, React testing, and Bulletproof React auditing. NOT for Next.js routing, SSR, or server components (use nextjs-development). NOT for CSS design systems, Tailwind utilities, or accessibility patterns (use frontend-design).
---

# React Development

Build production-grade React with proper architecture, optimized hooks, and quality auditing.

## When to Use This Skill

- Building React applications with Next.js App Router
- Creating reusable component libraries with shadcn/ui or fpkit
- Optimizing React hooks usage and eliminating anti-patterns
- Auditing React codebase quality with Bulletproof React
- Implementing accessible, well-tested components

## When NOT to Use This Skill

- **Next.js routing, SSR, server components** → use `nextjs-development`
- **CSS design systems, Tailwind utilities, accessibility patterns** → use `frontend-design`
- **Backend API development** → use `api-design` or `typescript-development`
- **Test framework setup** → use `testing-framework`

---

## Decision Tree

```
What are you building?
|
+-- Full-stack Next.js app?
|   --> 5-Layer Architecture (Section 1)
|
+-- Component library?
|   +-- shadcn/ui? --> CVA Variants + Radix Primitives (Section 2)
|   +-- fpkit? --> Composition Patterns (references/extended-patterns.md)
|
+-- Optimizing existing React code?
|   +-- Hooks issues (re-renders, stale state, dependency arrays)?
|   |   --> Anti-pattern Detection + Fix (Section 3)
|   +-- Code quality audit needed?
|       --> Bulletproof React Auditor (references/extended-patterns.md)
|
+-- Debugging a specific hooks problem?
    +-- Effect fires too often? --> Check dependency array (Section 3)
    +-- State stale in callback? --> Functional update or useRef
    +-- Component re-renders unnecessarily? --> Memoization decision tree
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

### Anti-Patterns with Solutions

**1. Derived State** — Don't use `useState` + `useEffect` for derived values.
```tsx
// ANTI-PATTERN: derived state in useState+useEffect
const [searchQuery, setSearchQuery] = useState('');
const [filteredItems, setFilteredItems] = useState(items);
useEffect(() => {
  setFilteredItems(items.filter(item => item.name.includes(searchQuery)));
}, [searchQuery, items]); // extra re-render, stale data risk

// CORRECT: compute during render
const [searchQuery, setSearchQuery] = useState('');
const filteredItems = items.filter(item => item.name.includes(searchQuery));
```

**2. Event Response** — Don't use `useEffect` for user actions.
```tsx
// ANTI-PATTERN: responding to events in useEffect
const [userId, setUserId] = useState(null);
useEffect(() => {
  if (userId) api.trackUserSelection(userId); // fires on every userId change
}, [userId]);

// CORRECT: handle in event handler
<Button onClick={() => {
  setUserId(id);
  api.trackUserSelection(id);
}}>Select</Button>
```

**3. Props-to-State Sync** — Don't mirror props in state.
```tsx
// ANTI-PATTERN: syncing props to state
const [localValue, setLocalValue] = useState(props.value);
useEffect(() => { setLocalValue(props.value); }, [props.value]);

// CORRECT: use key prop for reset, or compute from props
<Editor key={props.documentId} initialValue={props.value} />
```

**4. Premature Memoization** — Don't `useMemo`/`useCallback` cheap operations.
```tsx
// ANTI-PATTERN: memoizing cheap computations
const fullName = useMemo(() => `${first} ${last}`, [first, last]);

// CORRECT: compute during render (string concat is trivial)
const fullName = `${first} ${last}`;
```

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
