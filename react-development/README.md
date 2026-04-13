# React Development

> **v1.1.20** | Development | 22 iterations

Build production-grade React applications with Next.js App Router, shadcn/ui components, optimized hooks, and Bulletproof React architecture.

## What Problem Does This Solve

React applications accumulate hooks anti-patterns -- syncing props to state with useEffect, over-memoizing cheap calculations, creating re-render cascades -- that degrade performance and make components impossible to reason about. Component architecture also drifts without clear boundaries between server-side services, client-side data hooks, and presentational components. Codebases grow past the point where "just add another useEffect" works, but teams lack the decision framework to know when memoization matters, when to reach for a custom hook, and when to leave things simple. This skill provides the patterns, anti-pattern catalog, auditing criteria, and scaffold tooling to build React applications correctly and refactor existing ones back to health.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "Structure my Next.js application with Supabase" | 5-layer architecture (Types, Services, Hooks, Components, Pages) with server-side service patterns and client-side TanStack Query hooks |
| "Build a component library with shadcn/ui" | CVA variants pattern for type-safe component variants with Tailwind CSS, plus scaffold scripts for component and Tailwind config generation |
| "My useEffect is causing infinite re-renders" | Dependency array rules, functional update patterns, and the anti-pattern catalog: derived state, event response, props-to-state, premature memoization |
| "Should I use useMemo here?" | Decision criteria: only memoize expensive computations (O(n log n)+), callbacks passed to memoized children, or values in other hooks' dependency arrays |
| "Audit my React codebase for quality issues" | Bulletproof React auditing criteria covering architecture, hooks, component size (<300 lines, <10 props), and WCAG 2.1 AA accessibility |

## When NOT to Use This Skill

- Next.js routing, SSR, or server components -- use [nextjs-development](../nextjs-development/) instead
- CSS design systems, Tailwind utilities, or accessibility patterns -- use [frontend-design](../frontend-design/) instead

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install react-development@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention the triggers below, or you can invoke it explicitly.

## How to Use

**Direct invocation:**

```
Use the react-development skill to audit my hooks usage
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `react`
- `hooks`
- `useState`
- `useEffect`
- `shadcn`
- `bulletproof-react`

## What's Inside

This is a single-skill plugin that combines expertise from 7 specialized React development areas: Next.js Module Builder, shadcn/ui Component Library, fpkit Component Builder, Bulletproof React Auditor, fpkit Developer, React Hooks Advanced, and React Hooks Best Practices.

| Component | Purpose |
|---|---|
| `SKILL.md` | Decision tree, 5-layer Next.js architecture, shadcn/ui CVA pattern, hooks anti-pattern catalog, Do/Don't best practices |
| **References -- Next.js** | |
| `references/nextjs-architecture-patterns.md` | Architecture patterns for Next.js App Router |
| `references/nextjs-component-patterns.md` | Component patterns specific to Next.js |
| `references/nextjs-hooks-patterns.md` | Hook patterns in the context of Next.js |
| `references/nextjs-page-patterns.md` | Page and layout patterns |
| `references/nextjs-service-patterns.md` | Server-side service layer patterns |
| `references/nextjs-database-patterns.md` | Database access patterns (Supabase, Drizzle) |
| `references/nextjs-permission-patterns.md` | Permission and auth patterns |
| `references/nextjs-typescript-patterns.md` | TypeScript patterns for Next.js |
| **References -- Hooks** | |
| `references/hooks-custom-hooks.md` | When and how to build custom hooks |
| `references/hooks-dependency-array.md` | Dependency array rules and gotchas |
| `references/hooks-unnecessary-hooks.md` | Hooks you should not write (derived state, event response) |
| **References -- shadcn/ui** | |
| `references/shadcn-form-patterns.md` | Form patterns with React Hook Form + Zod |
| `references/shadcn-data-tables.md` | Data table patterns with TanStack Table |
| `references/shadcn-animation-patterns.md` | Animation patterns with Framer Motion |
| `references/shadcn-testing-setup.md` | Testing setup for shadcn components |
| **References -- fpkit** | |
| `references/fpkit-builder-*` | Component building, accessibility, CSS variables, composition, Storybook, testing patterns for fpkit |
| `references/fpkit-dev-*` | Application development with fpkit components |
| **References -- Auditing** | |
| `references/bulletproof-audit_criteria.md` | Audit criteria for Bulletproof React architecture |
| `references/bulletproof-severity_matrix.md` | Severity classification for audit findings |
| `references/extended-patterns.md` | Full reference for fpkit development, Bulletproof auditing, and detailed hooks patterns |
| **Scripts** | |
| `scripts/shadcn-setup-tailwind.py` | Generate Tailwind config with shadcn defaults |
| `scripts/shadcn-generate-component.py` | Scaffold new shadcn-style components |
| `scripts/hooks-analyze-hooks-usage.mjs` | Analyze hooks usage patterns in a codebase |
| `scripts/audit_engine.py` | Automated React codebase audit engine |
| `scripts/fpkit-builder-*.py` | Component analysis, scaffolding, CSS variable validation, reuse suggestions |
| **Examples and Templates** | |
| `examples/hooks-anti-patterns.tsx` | Concrete anti-pattern code examples |
| `examples/hooks-good-patterns.tsx` | Correct alternatives to anti-patterns |
| `templates/component.template.*` | Component, story, test, types, and SCSS templates |

## Usage Scenarios

**Scenario 1 -- Structuring a new Next.js + Supabase app.** You are starting a full-stack application. The skill provides the 5-layer architecture (Types -> Services -> Hooks -> Components -> Pages) with concrete code for server-side Supabase service functions and client-side TanStack Query hooks, ensuring clean separation between data fetching and presentation.

**Scenario 2 -- Fixing a re-render cascade.** Your component tree re-renders on every keystroke. The skill diagnoses the anti-pattern (likely props synced to state via useEffect, or unnecessary memoization), provides the correct alternative (calculate derived values during render, handle events in event handlers), and explains the dependency array rules that prevent future issues.

**Scenario 3 -- Building a component library.** You need a shared component system with variants. The skill provides the CVA (class-variance-authority) pattern for type-safe Tailwind variants, generates scaffolding with `shadcn-generate-component.py`, and sets up testing with accessible query patterns.

**Scenario 4 -- Auditing an existing React codebase.** Your codebase has grown organically and you suspect quality issues. The Bulletproof React audit engine analyzes architecture, hooks usage, component sizing, state management, security practices, and accessibility compliance, producing a severity-classified report with fix recommendations.

**Scenario 5 -- Custom hook design.** You are unsure whether to extract logic into a custom hook. The skill applies the decision criteria: does the logic involve reactive state? Would multiple components reuse it? If the answer to both is no, keep it as a plain function. If yes, the `hooks-custom-hooks.md` reference guides the extraction.

## Related Skills

- **[Nextjs Development](../nextjs-development/)** -- App Router, Server Components, Server Actions, and Next.js-specific patterns.
- **[Frontend Design](../frontend-design/)** -- UI design systems, Tailwind CSS utilities, component libraries, and accessibility.
- **[Typescript Development](../typescript-development/)** -- TypeScript type system patterns, generics, Zod validation.
- **[Testing Framework](../testing-framework/)** -- React Testing Library setup, Playwright E2E, and Vitest configuration.
- **[Test Driven Development](../test-driven-development/)** -- Red-Green-Refactor workflow for React component and hook testing.

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 52 production-grade plugins for Claude Code.
