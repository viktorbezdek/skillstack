# React Development

> **v1.1.20** | Development | 22 iterations

> Build production-grade React applications with Next.js App Router, shadcn/ui components, optimized hooks, and Bulletproof React architecture patterns.

## The Problem

React applications start simple and grow complex fast. A team builds a feature with useState and useEffect, and within weeks the component is 500 lines of tangled state synchronization, derived values stored in state that should be computed during render, and effects that fire on every keystroke because the dependency array is wrong. The hooks look correct -- they follow the Rules of Hooks -- but they violate patterns the React docs now explicitly warn against.

Architecture decisions made in the first week compound through the project's lifetime. Without a layered structure, server-side data fetching leaks into components, business logic lives in useEffect chains, and there is no clear boundary between what runs on the server and what runs on the client. Teams end up with components that are impossible to test in isolation because they directly call APIs, manage their own caching, and handle their own error states.

Component libraries suffer a different problem. Teams either build everything from scratch (wasting weeks on accessible dropdowns and date pickers) or adopt a component library without a variant system, leading to one-off CSS overrides scattered across the codebase. When design requirements change, every component needs individual attention because there is no systematic theming or variant architecture.

## The Solution

This plugin combines expertise from seven specialized React development domains into a single skill: Next.js 5-layer architecture, shadcn/ui component patterns with CVA variants, fpkit component library building, Bulletproof React code quality auditing, and advanced hooks optimization. It activates whenever you work with React components, hooks, JSX/TSX files, or Next.js routing.

The skill provides a decision tree that routes you to the right pattern: building a full-stack Next.js app gets you the 5-layer architecture (Types, Services, Hooks, Components, Pages), creating a component library gets you shadcn/ui or fpkit patterns with CVA variants and CSS variables, and optimizing existing code gets you hooks anti-pattern detection and Bulletproof React auditing. Each path includes concrete code patterns, not abstract guidelines.

For hooks specifically, the skill enforces a core principle: "The best hook is the one you don't need to write." It identifies the four most common anti-patterns (derived state in useState+useEffect, event responses in effects, props-to-state synchronization, and premature memoization) and provides the correct alternative for each. The result is simpler, faster components that re-render only when they should.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Components mix data fetching, business logic, and UI rendering in one file | 5-layer architecture separates Types, Services, Hooks, Components, and Pages with clear boundaries |
| Derived values stored in useState+useEffect -- extra re-renders and stale data bugs | Derived values computed during render -- no effects, no stale data, fewer re-renders |
| Component library built from scratch or adopted without a variant system | shadcn/ui with CVA variants provides systematic theming, sizing, and customization |
| Hooks dependency arrays guessed at -- ESLint warnings suppressed | Dependency array rules enforced: include all reactive values, use functional updates, never suppress warnings |
| No way to audit React code quality across a codebase | Bulletproof React auditor scores components against documented best practices |
| useMemo/useCallback applied everywhere "just in case" | Memoization applied only when justified: expensive computation, memoized child props, or dependency array values |

## Installation

Add the SkillStack marketplace, then install this plugin:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install react-development@skillstack
```

### Verify installation

After installing, test with:

```
I have a React component that uses useState and useEffect to keep a filtered list in sync with a search input -- is this the right pattern?
```

The skill should activate and identify this as a derived state anti-pattern, showing how to compute the filtered list during render instead.

## Quick Start

1. **Install** the plugin using the commands above
2. **Describe your situation** naturally: `I'm building a Next.js app with Supabase and need to structure the project properly`
3. The skill **routes you** to the right architecture pattern -- in this case, the 5-layer architecture with server-side services and client-side hooks
4. As you build, **ask about specific patterns**: `How should I handle optimistic updates with React Query?` or `Create a Button component with size and variant props using shadcn/ui patterns`
5. When ready for review, say: `Audit this component for React best practices` to get a Bulletproof React quality assessment

## What's Inside

This is a single-skill plugin combining seven specialized React development domains, backed by 30 reference files and 12 utility scripts.

| Component | Purpose |
|---|---|
| `SKILL.md` | Core methodology -- decision tree, 5-layer architecture, shadcn/ui CVA patterns, hooks anti-patterns, best practices |
| 30 reference files | Deep guidance on Next.js patterns, shadcn/ui, fpkit, hooks optimization, Bulletproof React auditing |
| 12 utility scripts | Component scaffolding, CSS variable validation, hooks analysis, audit engine |

**Eval coverage:** 13 trigger evaluation cases, 3 output evaluation cases.

**Key references:**

| Reference | Topic |
|---|---|
| `nextjs-architecture-patterns.md` | 5-layer architecture, module boundaries, data flow |
| `nextjs-component-patterns.md` | Server/Client component patterns, composition |
| `nextjs-hooks-patterns.md` | React Query integration, custom hooks for Next.js |
| `nextjs-service-patterns.md` | Server-side service layer with Supabase |
| `nextjs-database-patterns.md` | Database access patterns, migrations, row-level security |
| `nextjs-page-patterns.md` | Page layouts, loading states, error boundaries |
| `nextjs-typescript-patterns.md` | TypeScript patterns specific to Next.js + React |
| `nextjs-permission-patterns.md` | Auth and permission patterns with Supabase |
| `shadcn-form-patterns.md` | Form components with React Hook Form + Zod validation |
| `shadcn-data-tables.md` | Data table patterns with sorting, filtering, pagination |
| `shadcn-animation-patterns.md` | Animation patterns with Framer Motion + shadcn |
| `shadcn-testing-setup.md` | Testing setup for shadcn/ui components |
| `hooks-dependency-array.md` | Dependency array rules, common mistakes, solutions |
| `hooks-unnecessary-hooks.md` | Anti-patterns -- hooks you should not write |
| `hooks-custom-hooks.md` | Custom hook composition, testing, and reuse |
| `bulletproof-audit_criteria.md` | Audit scoring criteria and quality thresholds |
| `bulletproof-severity_matrix.md` | Issue severity classification for audits |
| `fpkit-builder-*` | fpkit component library patterns (composition, testing, accessibility, CSS variables, Storybook) |
| `fpkit-dev-*` | fpkit consumer patterns (architecture, composition, accessibility, testing, CSS variables, Storybook) |
| `extended-patterns.md` | Combined reference with fpkit development, Bulletproof auditing, and detailed hooks analysis |

**Key scripts:**

| Script | Purpose |
|---|---|
| `shadcn-generate-component.py` | Scaffold new shadcn-style components with CVA variants |
| `shadcn-setup-tailwind.py` | Generate Tailwind config with shadcn defaults |
| `audit_engine.py` | Bulletproof React code quality audit engine |
| `hooks-analyze-hooks-usage.mjs` | Static analysis of hooks usage patterns |
| `fpkit-builder-scaffold_component.py` | Scaffold fpkit library components |
| `fpkit-builder-validate_css_vars.py` | Validate CSS variable naming and usage |

### react-development

**What it does:** Activates when you work with React components, hooks (useState, useEffect, useReducer, useContext), JSX/TSX files, component architecture, or state management. Routes you to the right pattern based on what you are building -- full-stack Next.js apps, component libraries, or hooks optimization.

**Try these prompts:**

```
Set up a Next.js 15 project with the 5-layer architecture, Supabase, and React Query
```

```
This component uses useState and useEffect to sync a filtered list -- is there a better pattern?
```

```
Create a Button component with shadcn/ui patterns -- I need default, secondary, outline, and ghost variants in three sizes
```

```
Audit this React component for best practices -- it's 400 lines and I suspect it's doing too much
```

```
How do I handle optimistic updates with React Query when the user edits a table row inline?
```

```
My useEffect has 8 items in its dependency array and fires too often -- help me refactor this
```

## Real-World Walkthrough

You are building an internal project management dashboard with Next.js 15 and Supabase. The app needs a project list page with filtering and sorting, a project detail page with task management, and real-time updates when team members modify tasks. Your current prototype has everything in three massive page components.

You open Claude Code and say:

```
I have a Next.js app with three page components that each do their own data fetching, state management, and UI rendering. Help me restructure this properly.
```

The skill activates and presents the **5-layer architecture**:

```
Types --> Services --> Hooks --> Components --> Pages
```

It starts by extracting the **Types layer**. Your Supabase database has `projects`, `tasks`, and `users` tables. The skill generates TypeScript interfaces from your database schema using `database.types.ts`, plus domain-specific types like `ProjectWithTasks` and `TaskWithAssignee` that match your query shapes.

Next comes the **Services layer**. The skill moves all Supabase queries out of components into `lib/services/projects.service.ts` and `lib/services/tasks.service.ts`. Each service function creates a Supabase client using the server-side helper (`createClient` from `@/lib/supabase/server`), executes the query, handles errors, and returns typed data. These functions are server-only -- they never ship to the client bundle.

You ask:

```
How should the client-side components get this data? I need filtering and real-time updates.
```

The skill builds the **Hooks layer** with React Query. A `useProjects` hook wraps a query that fetches via the API route, supporting filter and sort parameters. A `useTasks` hook subscribes to Supabase Realtime for the specific project channel, updating the React Query cache when tasks are created, updated, or deleted. The skill shows how to invalidate the cache on mutations and how to implement optimistic updates for task status changes.

Now you need the task management UI:

```
Create a task board component where users can change task status by clicking a dropdown
```

The skill builds the **Components layer** using shadcn/ui patterns. It creates a `TaskCard` component with CVA variants for different task statuses (todo, in-progress, done, blocked). The status dropdown uses a shadcn `Select` component with proper keyboard accessibility. The component receives task data and callbacks via props -- no data fetching, no state management, just rendering and user interaction forwarding.

You notice the task card component re-renders every time any task on the board changes:

```
TaskCard re-renders even when its specific task hasn't changed. How do I fix this?
```

The skill diagnoses the issue: the `onStatusChange` callback is being recreated on every parent render because it is defined inline. It shows two solutions. First, use `useCallback` in the parent with the task ID in the closure. Second -- and often better -- restructure the component to accept a task ID and look up its own data via the hook, so it only re-renders when its specific task changes. The skill explains when each approach is appropriate: `useCallback` when the component is already memoized with `React.memo`, restructuring when the component manages its own subscription.

After building the core features, you want a quality check:

```
Audit the dashboard components for React best practices
```

The skill runs the Bulletproof React auditor. It flags three issues: (1) the project list page still has an inline `useEffect` that synchronizes URL search params to component state -- this should use `useSearchParams` directly as the source of truth, (2) a `TaskDetails` component has 12 props indicating it needs decomposition, and (3) a utility function in `components/` should move to `lib/utils/`. Each issue includes a severity rating (warning, suggestion) and a specific code change to fix it.

The final dashboard has clean separation: services handle data access, hooks manage client-side state and real-time subscriptions, components render UI with CVA variants, and pages compose everything together. Each layer is independently testable. When you later need to add a mobile view, you only change the Components and Pages layers -- Services and Hooks remain untouched.

## Usage Scenarios

### Scenario 1: Starting a new Next.js project with proper architecture

**Context:** You are starting a SaaS application with Next.js 15, Supabase authentication, and a complex dashboard. You want to avoid the "everything in page components" trap from the start.

**You say:** `Set up a Next.js 15 project with Supabase, React Query, and a proper layered architecture`

**The skill provides:**
- 5-layer project structure with Types, Services, Hooks, Components, and Pages directories
- Supabase client configuration for both server and client contexts
- React Query provider setup with sensible defaults
- TypeScript configuration tuned for Next.js

**You end up with:** A scaffolded project with clear architectural boundaries that scales from MVP to production without structural rewrites.

### Scenario 2: Building a component library with shadcn/ui

**Context:** Your design team has finalized a design system, and you need to implement it as a React component library that other teams will consume.

**You say:** `Create a component library based on shadcn/ui with our custom theme -- I need Button, Input, Select, Dialog, and DataTable to start`

**The skill provides:**
- CVA variant definitions matching your design tokens (colors, spacing, typography)
- Composition patterns using Radix UI primitives under the hood
- CSS variable-based theming for runtime theme switching
- Testing setup with component-level tests and Storybook stories

**You end up with:** A typed, themed, accessible component library that other teams install and customize via CSS variables without forking the source.

### Scenario 3: Fixing hooks anti-patterns in an existing codebase

**Context:** Your React app has grown to 80+ components and performance has degraded. You suspect excessive re-renders but do not know where to start.

**You say:** `My React app re-renders too much. Can you analyze the hooks usage in src/components/ and find anti-patterns?`

**The skill provides:**
- Static analysis of hooks usage patterns via the hooks analyzer script
- Identification of derived state stored in useState+useEffect (compute during render instead)
- Detection of unnecessary memoization on cheap operations
- Dependency array issues causing effects to fire more often than needed

**You end up with:** A prioritized list of hooks to refactor, with before/after code for each, ordered by re-render impact.

### Scenario 4: Auditing code quality with Bulletproof React

**Context:** You are preparing for a code review before a major release. The codebase has grown organically and you want to identify architectural issues before they become technical debt.

**You say:** `Run a Bulletproof React audit on the src/ directory and give me a severity-rated report`

**The skill provides:**
- Audit scoring against documented criteria (component size, prop count, layer violations, testing coverage)
- Severity classification (critical, warning, suggestion) with specific file and line references
- Concrete code changes for each finding
- Summary statistics (components audited, issues found, overall quality score)

**You end up with:** A structured audit report that can be converted into tech debt tickets, prioritized by severity.

## Ideal For

- **Teams building full-stack Next.js applications** -- the 5-layer architecture prevents the common "everything in page components" trap and provides clear boundaries between server and client code
- **Frontend developers building component libraries** -- shadcn/ui and fpkit patterns with CVA variants produce systematic, themeable, accessible components instead of one-off implementations
- **React developers struggling with hooks complexity** -- anti-pattern detection and correct alternatives eliminate the most common sources of excessive re-renders and stale state
- **Tech leads preparing for code reviews** -- the Bulletproof React auditor produces severity-rated reports that identify architectural issues objectively

## Not For

- **Next.js routing, SSR, and server components** -- use [nextjs-development](../nextjs-development/) for App Router-specific patterns, middleware, caching, and data fetching strategies
- **CSS design systems, Tailwind utilities, and accessibility patterns** -- use [frontend-design](../frontend-design/) for visual design systems, CSS architecture, and WCAG compliance
- **Backend API development** -- use [api-design](../api-design/) for REST/GraphQL API patterns and [typescript-development](../typescript-development/) for Node.js server code

## How It Works Under the Hood

The plugin is a single skill that combines expertise from seven React development domains. The SKILL.md body provides the decision tree, core architecture patterns, and hooks best practices -- enough for most React development tasks. When deeper guidance is needed, 30 reference files provide specialized content:

- **Next.js references (8 files):** Architecture, components, hooks, services, database, pages, TypeScript, and permissions -- all specific to Next.js App Router with Supabase
- **shadcn/ui references (4 files):** Form patterns, data tables, animations, and testing setup for shadcn-based component libraries
- **fpkit references (10 files):** Split between library building (builder) and library consuming (dev) -- composition, testing, accessibility, CSS variables, and Storybook
- **Hooks references (3 files):** Dependency arrays, unnecessary hooks, and custom hook patterns
- **Bulletproof React references (2 files):** Audit criteria and severity matrix

Twelve utility scripts support automated workflows: component scaffolding, CSS variable validation, hooks usage analysis, Tailwind config generation, and the Bulletproof React audit engine. These scripts run locally and produce actionable output without external dependencies.

## Related Plugins

- **[Next.js Development](../nextjs-development/)** -- App Router routing, middleware, caching, and server-component patterns
- **[Frontend Design](../frontend-design/)** -- Visual design systems, Tailwind CSS, CSS variables, and accessibility
- **[TypeScript Development](../typescript-development/)** -- TypeScript patterns, generics, Zod validation, and tsconfig
- **[Test-Driven Development](../test-driven-development/)** -- Red-Green-Refactor methodology for testing React components
- **[Testing Framework](../testing-framework/)** -- Test infrastructure setup including Vitest and React Testing Library

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
