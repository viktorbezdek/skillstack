---
name: react-development
description: "Build production-grade React applications with Next.js App Router, shadcn/ui components, optimized hooks, and Bulletproof React architecture. Use when: creating a React component, writing a custom React hook, building with shadcn/ui, setting up Next.js pages, auditing React code quality, or optimizing component performance. Triggers: 'React component', 'React hook', 'useState', 'useEffect', 'shadcn', 'component library', 'React testing', 'Next.js component', 'Tailwind component', 'React architecture', 'JSX', 'TSX', 'React app', 'useReducer', 'useContext'."
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
|   +-- Using fpkit? --> See: fpkit Patterns (Section 3)
|
+-- Optimizing existing React code?
|   +-- Hooks issues? --> See: Hooks Best Practices (Section 5)
|   +-- Architecture audit? --> See: Bulletproof Audit (Section 4)
|
+-- Using fpkit components in app?
    --> See: fpkit Developer (Section 3.2)
```

---

## Section 1: Next.js Architecture

### 5-Layer Architecture

For Next.js 15 App Router applications with Supabase backend:

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

**Reference Files:**
- `references/nextjs-architecture-patterns.md` - Full architecture guide
- `references/nextjs-service-patterns.md` - Service layer patterns
- `references/nextjs-hooks-patterns.md` - React Query hook patterns
- `references/nextjs-component-patterns.md` - Component patterns
- `references/nextjs-page-patterns.md` - Page and route patterns
- `references/nextjs-database-patterns.md` - Supabase patterns
- `references/nextjs-permission-patterns.md` - Auth and permissions
- `references/nextjs-typescript-patterns.md` - TypeScript patterns

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
    defaultVariants: {
      variant: 'default',
      size: 'default',
    },
  }
)
```

### Component Pattern

```typescript
export interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement>,
    VariantProps<typeof buttonVariants> {
  asChild?: boolean
}

const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant, size, asChild = false, ...props }, ref) => {
    const Comp = asChild ? Slot : 'button'
    return (
      <Comp
        className={cn(buttonVariants({ variant, size, className }))}
        ref={ref}
        {...props}
      />
    )
  }
)
```

### Scripts

- `scripts/shadcn-setup-tailwind.py` - Generate Tailwind config with shadcn defaults
- `scripts/shadcn-generate-component.py` - Scaffold new shadcn-style components

### Reference Files

- `references/shadcn-form-patterns.md` - Form handling with React Hook Form + Zod
- `references/shadcn-data-tables.md` - TanStack Table patterns
- `references/shadcn-animation-patterns.md` - Framer Motion animations
- `references/shadcn-testing-setup.md` - Testing configuration

---

## Section 3: fpkit Component Development

### 3.1 Building fpkit Library Components

For developers building the @fpkit/acss library itself.

**Component Structure:**
```
src/components/
  component-name/
    component-name.tsx        # Component implementation
    component-name.types.ts   # TypeScript types
    component-name.scss       # Styles with CSS variables
    component-name.test.tsx   # Vitest tests
    component-name.stories.tsx # Storybook documentation
```

**CSS Variable Naming Convention:**
```scss
--{component}-{element}-{variant}-{property}-{modifier}

// Examples:
--btn-bg                      // Base button background
--btn-primary-bg              // Primary variant background
--btn-hover-bg                // Hover state background
--btn-focus-outline-offset    // Focus state modifier
```

**Approved Abbreviations:**
- `bg` - background
- `fs` - font-size
- `fw` - font-weight
- `radius` - border-radius
- `gap` - gap

**Full Words Required:**
- padding, padding-inline, padding-block
- margin, margin-inline, margin-block
- color, border, display, width, height

**Scripts:**
- `scripts/fpkit-builder-scaffold_component.py` - Scaffold new components
- `scripts/fpkit-builder-validate_css_vars.py` - Validate CSS variable naming
- `scripts/fpkit-builder-analyze_components.py` - Analyze component patterns
- `scripts/fpkit-builder-suggest_reuse.py` - Find reuse opportunities

**Reference Files:**
- `references/fpkit-builder-component-patterns.md` - Component patterns
- `references/fpkit-builder-composition-patterns.md` - Composition strategies
- `references/fpkit-builder-css-variable-guide.md` - CSS variable conventions
- `references/fpkit-builder-accessibility-patterns.md` - WCAG compliance
- `references/fpkit-builder-testing-patterns.md` - Testing strategies
- `references/fpkit-builder-storybook-patterns.md` - Documentation patterns

### 3.2 Using fpkit Components in Applications

For developers consuming @fpkit/acss components.

**Composition Example:**
```tsx
import { Button, Badge } from '@fpkit/acss'

export interface StatusButtonProps extends React.ComponentProps<typeof Button> {
  status: 'active' | 'inactive' | 'pending'
}

export const StatusButton = ({ status, children, ...props }: StatusButtonProps) => {
  return (
    <Button {...props}>
      {children}
      <Badge variant={status}>{status}</Badge>
    </Button>
  )
}
```

**CSS Customization:**
```css
/* Global overrides */
:root {
  --btn-radius: 0.25rem;
  --btn-primary-bg: #0066cc;
}

/* Scoped overrides */
.custom-button {
  --btn-padding-inline: 2rem;
}
```

**Reference Files:**
- `references/fpkit-dev-composition.md` - Component composition patterns
- `references/fpkit-dev-css-variables.md` - CSS customization guide
- `references/fpkit-dev-accessibility.md` - Accessibility compliance
- `references/fpkit-dev-architecture.md` - fpkit architecture overview
- `references/fpkit-dev-testing.md` - Testing composed components
- `references/fpkit-dev-storybook.md` - Documenting compositions

**Scripts:**
- `scripts/fpkit-dev-validate_css_vars.py` - Validate custom CSS variables
- `scripts/fpkit-dev-sync-docs.sh` - Sync documentation from fpkit

---

## Section 4: Bulletproof React Auditing

### Audit Categories

1. **Project Structure** - Feature-based organization
2. **Component Architecture** - Size limits, prop counts, composition
3. **State Management** - Appropriate tools for each state type
4. **API Layer** - Data fetching patterns
5. **Testing Strategy** - Test coverage and patterns
6. **Styling Patterns** - CSS organization
7. **Error Handling** - Error boundaries, recovery
8. **Performance** - Optimization patterns
9. **Security** - Best practices
10. **Standards Compliance** - Code quality

### Key Checks

**Component Size:**
- Components should be < 300 lines
- Props should be < 7-10

**State Management:**
- Use React Query/SWR for server state
- Use Zustand/Jotai for global state
- Keep state as local as possible

**Scripts:**
- `scripts/audit_engine.py` - Main audit orchestration
- `scripts/analyzers/` - Category-specific analyzers

**Reference Files:**
- `references/bulletproof-audit_criteria.md` - Audit criteria
- `references/bulletproof-severity_matrix.md` - Issue severity levels

---

## Section 5: React Hooks Best Practices

### Core Principle

> "The best hook is the one you don't need to write."

### Common Anti-Patterns

**1. Derived State with useState + useEffect**
```tsx
// BAD
const [total, setTotal] = useState(0)
useEffect(() => {
  setTotal(items.reduce((sum, i) => sum + i.price, 0))
}, [items])

// GOOD - Calculate during render
const total = items.reduce((sum, i) => sum + i.price, 0)
```

**2. useEffect for Event Response**
```tsx
// BAD - Effect chain for user action
useEffect(() => {
  if (query) fetch(`/api/search?q=${query}`)
}, [query])

// GOOD - Handle in event handler
const handleSubmit = async () => {
  const results = await fetch(`/api/search?q=${query}`)
}
```

**3. Props-to-State Sync**
```tsx
// BAD - Sync props to state
const [content, setContent] = useState(initialContent)
useEffect(() => {
  setContent(initialContent)
}, [initialContent])

// GOOD - Use key for reset
// Parent: <Editor key={documentId} initialContent={doc.content} />
```

**4. Premature Memoization**
```tsx
// BAD - Unnecessary for cheap operations
const fullName = useMemo(
  () => `${firstName} ${lastName}`,
  [firstName, lastName]
)

// GOOD - Just calculate it
const fullName = `${firstName} ${lastName}`
```

### When to Use Memoization

Only use `useMemo`/`useCallback` when:
1. Expensive computation (O(n log n) or worse)
2. Callback passed to memoized child component
3. Value used in dependency array of other hooks

### Dependency Array Rules

1. **Include all reactive values** used inside the effect
2. **Use functional updates** to avoid state dependencies
3. **Use refs** for values that shouldn't trigger re-runs
4. **Never suppress ESLint warnings** - fix the underlying issue

**Scripts:**
- `scripts/hooks-analyze-hooks-usage.mjs` - Analyze hooks usage patterns

**Reference Files:**
- `references/hooks-unnecessary-hooks.md` - Avoiding unnecessary hooks
- `references/hooks-custom-hooks.md` - Custom hook patterns
- `references/hooks-dependency-array.md` - Dependency array management

**Example Files:**
- `examples/hooks-good-patterns.tsx` - Correct patterns
- `examples/hooks-anti-patterns.tsx` - Anti-patterns with corrections

---

## Section 6: Templates

Component templates for rapid scaffolding:

- `templates/component.template.tsx` - Base component template
- `templates/component.template.types.ts` - TypeScript types template
- `templates/component.template.scss` - SCSS styles template
- `templates/component.template.test.tsx` - Vitest test template
- `templates/component.template.stories.tsx` - Storybook story template
- `templates/component.composed.template.tsx` - Composed component template
- `templates/component.extended.template.tsx` - Extended component template

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
- Write tests with React Testing Library

### Don't

- Store derived state with useState + useEffect
- Use useEffect for event responses
- Sync props to state (use key for reset)
- Prematurely memoize cheap operations
- Suppress ESLint exhaustive-deps warnings
- Create components with > 10 props
- Use px units (use rem)
- Skip keyboard accessibility

---

## File Reference

### References (29 files)

**Next.js:**
- nextjs-architecture-patterns.md
- nextjs-service-patterns.md
- nextjs-hooks-patterns.md
- nextjs-component-patterns.md
- nextjs-page-patterns.md
- nextjs-database-patterns.md
- nextjs-permission-patterns.md
- nextjs-typescript-patterns.md

**shadcn/ui:**
- shadcn-form-patterns.md
- shadcn-data-tables.md
- shadcn-animation-patterns.md
- shadcn-testing-setup.md

**fpkit Builder:**
- fpkit-builder-component-patterns.md
- fpkit-builder-composition-patterns.md
- fpkit-builder-css-variable-guide.md
- fpkit-builder-accessibility-patterns.md
- fpkit-builder-testing-patterns.md
- fpkit-builder-storybook-patterns.md

**fpkit Developer:**
- fpkit-dev-composition.md
- fpkit-dev-css-variables.md
- fpkit-dev-accessibility.md
- fpkit-dev-architecture.md
- fpkit-dev-testing.md
- fpkit-dev-storybook.md

**Bulletproof React:**
- bulletproof-audit_criteria.md
- bulletproof-severity_matrix.md

**Hooks:**
- hooks-unnecessary-hooks.md
- hooks-custom-hooks.md
- hooks-dependency-array.md

### Scripts (18+ files)

- audit_engine.py + analyzers/
- fpkit-builder-*.py (6 scripts)
- fpkit-dev-*.py/.sh (2 scripts)
- shadcn-*.py (2 scripts)
- hooks-analyze-hooks-usage.mjs

### Templates (7 files)

- component.template.tsx
- component.template.types.ts
- component.template.scss
- component.template.test.tsx
- component.template.stories.tsx
- component.composed.template.tsx
- component.extended.template.tsx

### Examples (3 files)

- hooks-good-patterns.tsx
- hooks-anti-patterns.tsx
- bulletproof-sample_audit_report.md

---

## Resources

- [Next.js Documentation](https://nextjs.org/docs)
- [shadcn/ui](https://ui.shadcn.com/)
- [fpkit Repository](https://github.com/shawn-sandy/acss)
- [Bulletproof React](https://github.com/alan2207/bulletproof-react)
- [React Docs - Rules of Hooks](https://react.dev/reference/rules/rules-of-hooks)
- [TanStack Query](https://tanstack.com/query)
- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)








