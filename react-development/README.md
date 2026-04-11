# React Development

> **v1.1.20** | Development | 22 iterations

Build production-grade React applications with Next.js App Router, shadcn/ui components, optimized hooks, and Bulletproof React architecture.

## What Problem Does This Solve

React applications accumulate hooks anti-patterns — syncing props to state with useEffect, over-memoizing cheap calculations, creating re-render cascades — that degrade performance and make components hard to reason about. Component architecture also drifts without clear boundaries between server-side services, client-side data hooks, and presentational components. This skill provides the patterns, decision trees, and auditing criteria to build React applications correctly and refactor existing ones to match.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "Structure my Next.js application with Supabase" | 5-layer architecture (Types, Services, Hooks, Components, Pages) with server-side service patterns and client-side TanStack Query hooks |
| "Build a component library with shadcn/ui" | CVA variants pattern for type-safe component variants with Tailwind CSS, plus scaffold scripts for generating shadcn-style components |
| "My useEffect is causing infinite re-renders" | Dependency array rules, functional update patterns, and the anti-pattern catalog (derived state, event response, props-to-state) |
| "Should I use useMemo here?" | Decision criteria: only memoize expensive computations (O(n log n)+), callbacks passed to memoized children, or values in other hooks' dependency arrays |
| "Audit my React codebase for quality issues" | Bulletproof React auditing criteria covering architecture, hooks usage, component size limits (< 300 lines, < 10 props), and accessibility patterns |
| "Help me set up React testing for components and hooks" | Testing patterns for React components including accessible queries and hook testing conventions |

## When NOT to Use This Skill

- Next.js routing, SSR, or server components -- use [nextjs-development](../nextjs-development/) instead
- CSS design systems, Tailwind utilities, or accessibility patterns -- use [frontend-design](../frontend-design/) instead

## Installation

```bash
claude install-plugin github:viktorbezdek/skillstack/react-development
```

## How to Use

**Direct invocation:**

```
Use the react-development skill to ...
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `react`
- `hooks`
- `shadcn`
- `bulletproof-react`

## What's Inside

- **Quick Start** -- Decision tree routing to the right section based on whether you're building a full-stack app, component library, or optimizing existing code.
- **Section 1: Next.js Architecture** -- 5-layer architecture pattern (Types, Services, Hooks, Components, Pages) with concrete service and hook code examples using Supabase and TanStack Query.
- **Section 2: shadcn/ui Component Architecture** -- CVA variants pattern for type-safe Tailwind components, plus Python scaffold scripts for generating Tailwind config and new shadcn-style components.
- **Section 3: React Hooks Best Practices** -- Four core anti-patterns (derived state, event response, props-to-state, premature memoization) with correct alternatives and dependency array rules.
- **Best Practices Summary** -- Consolidated Do/Don't list covering architecture, hooks, state management, component sizing, theming, and accessibility conventions.
- **Resources** -- Links to Next.js docs, shadcn/ui, fpkit, Bulletproof React, React Hooks rules, TanStack Query, and WCAG 2.1 guidelines.

## Version History

- `1.1.20` fix(frontend): disambiguate react-development vs nextjs-development vs frontend-design (6c64693)
- `1.1.19` fix: update plugin count and normalize footer in 31 original plugin READMEs (3ea7c00)
- `1.1.18` fix: change author field from string to object in all plugin.json files (bcfe7a9)
- `1.1.17` fix: rename all claude-skills references to skillstack (19ec8c4)
- `1.1.16` refactor: remove old file locations after plugin restructure (a26a802)
- `1.1.15` docs: update README and install commands to marketplace format (af9e39c)
- `1.1.14` refactor: restructure all 34 skills into proper Claude Code plugin format (7922579)
- `1.1.13` refactor: make each skill an independent plugin with own plugin.json (6de4313)
- `1.1.12` fix: make all shell scripts executable and fix Python syntax errors (61ac964)
- `1.1.11` docs: add detailed README documentation for all 34 skills (7ba1274)

## Related Skills

- **[Api Design](../api-design/)** -- Comprehensive API design skill for REST, GraphQL, gRPC, and Python library architectures. Design endpoints, schemas, aut...
- **[Debugging](../debugging/)** -- Comprehensive debugging skill combining systematic debugging methodology, browser DevTools automation, E2E testing with ...
- **[Frontend Design](../frontend-design/)** -- Comprehensive Frontend Design (UI/UX) skill combining UI design systems, component libraries, CSS/Tailwind styling, acce...
- **[Gws Cli](../gws-cli/)** -- Google Workspace CLI (gws) skill for managing Drive, Gmail, Sheets, Calendar, Docs, Chat, Tasks, and 11 more Workspace A...
- **[Mcp Server](../mcp-server/)** -- Comprehensive MCP (Model Context Protocol) server development skill. Build, configure, and manage MCP servers using Pyth...

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 50 production-grade plugins for Claude Code.
