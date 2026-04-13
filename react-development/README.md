# React Development

> **v1.1.20** | Development | 22 iterations

> Build production-grade React applications with Next.js App Router, shadcn/ui components, optimized hooks, and Bulletproof React architecture patterns.
> Single skill combining 7 domains + 30 references + 12 scripts + 7 templates + 3 examples

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
| No way to audit React code quality across a codebase | Bulletproof React auditor scores components against documented best practices with severity ratings |
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

---

## System Overview

```
User works with React / Next.js / JSX / TSX / hooks
    │
    ▼
┌──────────────────────────────────────────────────────────┐
│             react-development (skill)                      │
│                                                            │
│  Decision Tree:                                            │
│  ├── Full-stack Next.js app? ──── 5-Layer Architecture     │
│  ├── Component library?                                    │
│  │   ├── shadcn/ui? ──── CVA Variants + Radix Primitives  │
│  │   └── fpkit? ──── @fpkit/acss Composition Patterns      │
│  ├── Hooks optimization? ──── Anti-pattern Detection       │
│  └── Code quality audit? ──── Bulletproof React Auditor    │
│                                                            │
│  ┌───────────────────────────────────────────────────────┐ │
│  │            30 Reference Files (on-demand)              │ │
│  │                                                        │ │
│  │  Next.js (8):  architecture, components, hooks,        │ │
│  │                services, database, pages, TypeScript,   │ │
│  │                permissions                              │ │
│  │  shadcn/ui (4): forms, data tables, animations,        │ │
│  │                  testing setup                          │ │
│  │  fpkit (10):   builder (6) + dev (4) -- composition,   │ │
│  │                testing, accessibility, CSS vars,        │ │
│  │                Storybook                                │ │
│  │  Hooks (3):    dependency arrays, unnecessary hooks,    │ │
│  │                custom hook patterns                     │ │
│  │  Bulletproof (2): audit criteria, severity matrix       │ │
│  │  Extended (1): combined patterns reference              │ │
│  └───────────────────────────────────────────────────────┘ │
│                                                            │
│  ┌────────────────┐  ┌────────────┐  ┌────────────────┐   │
│  │  12 Scripts     │  │ 7 Templates│  │  3 Examples    │   │
│  │  scaffolding,   │  │ component, │  │  audit report, │   │
│  │  CSS validation,│  │ stories,   │  │  hooks good +  │   │
│  │  hooks analysis,│  │ tests,     │  │  bad patterns  │   │
│  │  audit engine,  │  │ types,     │  │                │   │
│  │  Tailwind setup │  │ SCSS       │  │                │   │
│  └────────────────┘  └────────────┘  └────────────────┘   │
└──────────────────────────────────────────────────────────┘
```

## What's Inside

| Component | Type | Purpose |
|---|---|---|
| `react-development` | skill | Decision tree routing to 7 domains: Next.js architecture, shadcn/ui, fpkit, Bulletproof auditing, hooks optimization |
| 8 Next.js references | reference | Architecture, components, hooks, services, database, pages, TypeScript, permissions |
| 4 shadcn/ui references | reference | Form patterns, data tables, animations, testing setup |
| 10 fpkit references | reference | Library building (6) + library consuming (4): composition, testing, accessibility, CSS variables, Storybook |
| 3 hooks references | reference | Dependency arrays, unnecessary hooks, custom hook patterns |
| 2 Bulletproof references | reference | Audit criteria and severity classification matrix |
| `extended-patterns.md` | reference | Combined reference for fpkit development, Bulletproof auditing, and detailed hooks analysis |
| `audit_engine.py` + 10 analyzers | script | Bulletproof React audit engine with analyzers for architecture, state, performance, security, testing, styling, errors, APIs, standards |
| `shadcn-generate-component.py` | script | Scaffold new shadcn-style components with CVA variants |
| `shadcn-setup-tailwind.py` | script | Generate Tailwind config with shadcn defaults |
| `hooks-analyze-hooks-usage.mjs` | script | Static analysis of hooks usage patterns across a codebase |
| fpkit builder scripts (5) | script | Scaffold components, validate CSS variables, analyze components, recommend approaches, suggest reuse |
| 7 component templates | template | Base component, composed component, extended component, test, stories, types, SCSS |
| 3 example files | example | Sample audit report, hooks good patterns, hooks anti-patterns |

**Eval coverage:** 13 trigger evaluation cases, 3 output evaluation cases.

### Component Spotlights

#### react-development (skill)

**What it does:** Activates when you work with React components, hooks (useState, useEffect, useReducer, useContext), JSX/TSX files, component architecture, or state management. Routes you to the right pattern based on what you are building -- full-stack Next.js apps, component libraries, or hooks optimization.

**Input -> Output:** A React development question or task -> Concrete code patterns following the appropriate architecture (5-layer, CVA variants, or optimized hooks), plus quality assessment when requested.

**When to use:** Building React applications with Next.js App Router. Creating reusable component libraries with shadcn/ui or fpkit. Optimizing hooks usage and eliminating anti-patterns. Auditing React codebase quality against Bulletproof React standards.

**When NOT to use:** Next.js routing, SSR, and server components at the framework level (use nextjs-development). CSS design systems, Tailwind utilities, and accessibility patterns (use frontend-design). Backend API development (use api-design or typescript-development).

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

#### audit_engine.py (script)

**CLI:** `python scripts/audit_engine.py --path src/`
**What it produces:** A severity-rated audit report covering component architecture, state management, performance patterns, security practices, testing strategy, styling patterns, error handling, API layer design, and standards compliance. Uses 10 specialized analyzer modules.
**Typical workflow:** Run before a code review or release to get an objective quality assessment with specific file/line references and recommended fixes.

#### shadcn-generate-component.py (script)

**CLI:** `python scripts/shadcn-generate-component.py ComponentName`
**What it produces:** A complete component scaffold: base component with CVA variants, TypeScript types, test file, Storybook story, and SCSS module -- following the 7 template files.
**Typical workflow:** When adding a new component to a shadcn-based library, run this to get a consistent starting point with all required files.

#### hooks-analyze-hooks-usage.mjs (script)

**CLI:** `node scripts/hooks-analyze-hooks-usage.mjs src/`
**What it produces:** A report of hooks usage patterns across the codebase, flagging derived state anti-patterns, unnecessary effects, oversized dependency arrays, and premature memoization.
**Typical workflow:** Run on an existing codebase to find the highest-impact hooks refactoring opportunities.

---

## Prompt Patterns

### Good Prompts vs Bad Prompts

| Bad (vague, underuses the skill) | Good (specific, gets expert guidance) |
|---|---|
| "Help me with React" | "Set up a Next.js 15 project with 5-layer architecture, Supabase auth, and React Query for a task management dashboard" |
| "My component is slow" | "This component re-renders on every parent render even though its props haven't changed -- it has 8 dependency array items in useEffect" |
| "Make a button component" | "Create a Button with shadcn/ui patterns -- default, secondary, outline, ghost variants in sm/md/lg sizes with disabled and loading states" |
| "Review my code" | "Audit this 400-line UserDashboard component for Bulletproof React violations -- I suspect it mixes data fetching with UI rendering" |
| "How do hooks work" | "I'm using useState + useEffect to filter a list whenever a search input changes -- is there a simpler pattern?" |

### Structured Prompt Templates

**For Next.js project architecture:**
```
I'm building a [app type: SaaS dashboard / e-commerce / admin panel] with Next.js 15
and [backend: Supabase / Prisma / external API]. The main features are [list 2-3].
Help me set up the 5-layer architecture with the right data flow.
```

**For component creation:**
```
Create a [ComponentName] component with shadcn/ui patterns.
Variants: [list variants like default, secondary, outline].
Sizes: [sm, md, lg]. States: [disabled, loading, error].
It needs to be accessible and work with [form library / data table / dialog].
```

**For hooks refactoring:**
```
This component uses [describe the hook pattern: useState + useEffect to sync X,
useMemo on every render, etc.]. It causes [problem: too many re-renders,
stale data, dependency array warnings]. Show me the correct pattern.
```

**For code quality audit:**
```
Run a Bulletproof React audit on [path: src/components/ or specific file].
Focus on [concern: component size, state management, layer violations, testing gaps].
Give me a severity-rated report with specific fixes.
```

### Prompt Anti-Patterns

- **Asking about "React" without specifying the context:** Are you building a Next.js app, a component library, or optimizing existing code? The skill routes to entirely different patterns based on the answer. Say what you are building.
- **Describing symptoms instead of showing code:** "My app is slow" gives the skill nothing to diagnose. Instead, describe the specific behavior: "This list component re-renders 200 items every time the parent state changes." Better yet, paste the component code.
- **Asking for hooks advice without showing the dependency array:** The most common hooks problems are dependency-array-shaped. When asking about effects that fire too often or state that goes stale, show the useEffect/useMemo call with its dependency array so the skill can diagnose the specific issue.
- **Requesting shadcn/ui components without specifying variants and states:** Saying "make a button" gets you a basic component. Saying "make a button with 4 variants, 3 sizes, disabled and loading states, and an icon slot" gets you a production-ready component with CVA definitions, proper TypeScript props, and accessibility attributes.

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

---

## Decision Logic

**How does the skill decide which domain to use?**

The skill examines your request and routes to the appropriate React domain:
- Working with Next.js App Router, data fetching, or project structure -> **Next.js 5-Layer Architecture** with server services, client hooks, and typed data flow
- Creating or modifying React components with variants and theming -> **shadcn/ui Patterns** with CVA, Radix primitives, and CSS variables
- Building library components for @fpkit/acss -> **fpkit Patterns** with composition, accessibility, and Storybook integration
- Questions about useState, useEffect, useMemo, or dependency arrays -> **Hooks Best Practices** with anti-pattern detection and correct alternatives
- Requesting code review or quality assessment -> **Bulletproof React Auditor** with severity-rated findings

**When does the skill load references?**

The SKILL.md body contains the decision tree, core architecture patterns, CVA variant syntax, and hooks anti-patterns. References load on demand:
- Next.js architecture question -> the relevant `nextjs-*.md` file (architecture, components, services, etc.)
- shadcn/ui component question -> the relevant `shadcn-*.md` file (forms, data tables, animations, testing)
- fpkit question -> the relevant `fpkit-builder-*.md` or `fpkit-dev-*.md` file
- Hooks deep-dive -> `hooks-dependency-array.md`, `hooks-unnecessary-hooks.md`, or `hooks-custom-hooks.md`
- Audit request -> `bulletproof-audit_criteria.md` and `bulletproof-severity_matrix.md`

**How does memoization guidance work?**

The skill recommends memoization (useMemo/useCallback) only when three conditions are met: (1) the computation is genuinely expensive (O(n log n) or worse), (2) the value is passed as a prop to a memoized child component, or (3) the value is used in a dependency array of another hook. If none of these apply, the skill recommends computing the value during render.

## Failure Modes & Edge Cases

| Failure | Symptom | Recovery |
|---|---|---|
| Component mixes server and client concerns | "use client" directive at the top of a component that also calls server-only APIs (Supabase server client, fs, etc.) | Split into a server component (data fetching) and a client component (interactivity). The skill shows the composition pattern where the server component passes data as props to the client component. |
| Hooks anti-pattern produces stale closures | State values inside useEffect or event handlers are stale -- they show the value from when the closure was created, not the current value | Use functional updates (`setCount(c => c + 1)` instead of `setCount(count + 1)`) or useRef for values that should not trigger re-renders but need current values in callbacks. |
| CVA variants become unmanageable | A component has 6+ variant axes and the combinations produce confusing CSS classes | Decompose the component into smaller, single-responsibility components. A "Card" with variants for size, color, border, shadow, padding, and alignment is really 3 separate concerns that should be composed, not configured. |
| Bulletproof audit produces false positives | The auditor flags patterns that are intentional in your codebase (e.g., a god component that serves as a page layout root) | Use the severity matrix to triage findings. "Suggestion" severity items may be intentional trade-offs. The skill supports annotation comments to mark intentional exceptions. |
| React Query cache and Supabase Realtime conflict | Optimistic updates via React Query get overwritten by Realtime subscription events, causing UI flicker | Coordinate by using Realtime events to invalidate the React Query cache rather than directly updating state. The skill shows the pattern in the Next.js hooks reference. |

## Ideal For

- **Teams building full-stack Next.js applications** -- the 5-layer architecture prevents the common "everything in page components" trap and provides clear boundaries between server and client code
- **Frontend developers building component libraries** -- shadcn/ui and fpkit patterns with CVA variants produce systematic, themeable, accessible components instead of one-off implementations
- **React developers struggling with hooks complexity** -- anti-pattern detection and correct alternatives eliminate the most common sources of excessive re-renders and stale state
- **Tech leads preparing for code reviews** -- the Bulletproof React auditor produces severity-rated reports that identify architectural issues objectively

## Not For

- **Next.js routing, SSR, and server components at the framework level** -- use [nextjs-development](../nextjs-development/) for App Router-specific patterns, middleware, caching, and data fetching strategies
- **CSS design systems, Tailwind utilities, and accessibility patterns** -- use [frontend-design](../frontend-design/) for visual design systems, CSS architecture, and WCAG compliance
- **Backend API development** -- use [api-design](../api-design/) for REST/GraphQL API patterns and [typescript-development](../typescript-development/) for Node.js server code

## Related Plugins

- **[Next.js Development](../nextjs-development/)** -- App Router routing, middleware, caching, and server-component patterns
- **[Frontend Design](../frontend-design/)** -- Visual design systems, Tailwind CSS, CSS variables, and accessibility
- **[TypeScript Development](../typescript-development/)** -- TypeScript patterns, generics, Zod validation, and tsconfig
- **[Test-Driven Development](../test-driven-development/)** -- Red-Green-Refactor methodology for testing React components
- **[Testing Framework](../testing-framework/)** -- Test infrastructure setup including Vitest and React Testing Library

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
