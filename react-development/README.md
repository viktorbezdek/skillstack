# React Development

> Build production-grade React applications with Next.js App Router, shadcn/ui components, optimized hooks, and Bulletproof React architecture.

## Overview

React development has matured significantly with the rise of Next.js App Router, server components, and modern component libraries like shadcn/ui. However, many developers still struggle with hooks anti-patterns, poor component architecture, and the server/client boundary. This skill encodes expertise from seven specialized React development domains into a single, cohesive resource that produces production-quality React code by default.

This skill is for frontend and full-stack developers building React applications, whether that means a Next.js full-stack app with Supabase, a reusable component library, or optimizing an existing React codebase. It covers architecture, component design, hooks optimization, testing, accessibility, and code quality auditing.

Within the SkillStack collection, React Development is the primary frontend skill. It pairs well with the TDD skill (for component testing workflows), the Code Review skill (for Bulletproof React auditing), and the Python Development skill (when building full-stack applications with Python backends).

## What's Included

### References
- **extended-patterns.md** -- fpkit component development, Bulletproof React auditing, and detailed hooks anti-patterns
- **bulletproof-audit_criteria.md** -- Audit criteria for Bulletproof React code quality assessment
- **bulletproof-severity_matrix.md** -- Severity classification matrix for code quality issues
- **nextjs-architecture-patterns.md** -- Next.js 15 App Router architecture patterns
- **nextjs-component-patterns.md** -- Next.js component design patterns (server/client split)
- **nextjs-database-patterns.md** -- Database access patterns with Supabase
- **nextjs-hooks-patterns.md** -- Hooks patterns specific to Next.js applications
- **nextjs-page-patterns.md** -- Page and layout patterns for App Router
- **nextjs-permission-patterns.md** -- Permission and authorization UI patterns
- **nextjs-service-patterns.md** -- Service layer patterns for server-side data access
- **nextjs-typescript-patterns.md** -- TypeScript patterns for Next.js projects
- **shadcn-animation-patterns.md** -- Animation patterns using shadcn/ui components
- **shadcn-data-tables.md** -- Data table implementation with shadcn/ui
- **shadcn-form-patterns.md** -- Form handling patterns with shadcn/ui and React Hook Form
- **shadcn-testing-setup.md** -- Testing configuration for shadcn/ui components
- **hooks-custom-hooks.md** -- Custom hook design patterns and composition
- **hooks-dependency-array.md** -- Deep dive on dependency array rules and pitfalls
- **hooks-unnecessary-hooks.md** -- Guide to eliminating unnecessary hooks usage
- **fpkit-builder-accessibility-patterns.md** -- Accessibility patterns for fpkit components
- **fpkit-builder-component-patterns.md** -- Component architecture patterns for fpkit
- **fpkit-builder-composition-patterns.md** -- Composition patterns for fpkit
- **fpkit-builder-css-variable-guide.md** -- CSS custom properties guide for fpkit theming
- **fpkit-builder-storybook-patterns.md** -- Storybook integration patterns
- **fpkit-builder-testing-patterns.md** -- Testing patterns for fpkit components
- **fpkit-dev-accessibility.md** -- Accessibility guidelines for fpkit consumers
- **fpkit-dev-architecture.md** -- fpkit architecture overview
- **fpkit-dev-composition.md** -- Component composition with fpkit
- **fpkit-dev-css-variables.md** -- CSS variable usage in fpkit applications
- **fpkit-dev-storybook.md** -- Storybook usage for fpkit development
- **fpkit-dev-testing.md** -- Testing fpkit-based applications

### Scripts
- **audit_engine.py** -- Bulletproof React audit engine for automated code quality analysis
- **shadcn-generate-component.py** -- Scaffold new shadcn-style components with variants
- **shadcn-setup-tailwind.py** -- Generate Tailwind CSS config with shadcn defaults
- **hooks-analyze-hooks-usage.mjs** -- Analyze hooks usage across a React codebase
- **fpkit-builder-add_to_exports.py** -- Add new components to fpkit package exports
- **fpkit-builder-analyze_components.py** -- Analyze existing fpkit component structure
- **fpkit-builder-recommend_approach.py** -- Recommend component implementation approach
- **fpkit-builder-scaffold_component.py** -- Scaffold new fpkit components
- **fpkit-builder-suggest_reuse.py** -- Suggest component reuse opportunities
- **fpkit-builder-validate_css_vars.py** -- Validate CSS variable usage in fpkit
- **fpkit-dev-sync-docs.sh** -- Sync fpkit documentation
- **fpkit-dev-validate_css_vars.py** -- Validate CSS variables in fpkit applications
- **analyzers/** -- 11 specialized audit analyzers: API layer, component architecture, error handling, performance patterns, project structure, security practices, standards compliance, state management, styling patterns, and testing strategy

### Templates
- **component.template.tsx** -- Base React component template
- **component.composed.template.tsx** -- Composed component template (multiple sub-components)
- **component.extended.template.tsx** -- Extended component template with full feature set
- **component.template.scss** -- Component SCSS stylesheet template
- **component.template.stories.tsx** -- Storybook stories template
- **component.template.test.tsx** -- Component test template
- **component.template.types.ts** -- TypeScript types/interfaces template

### Examples
- **bulletproof-sample_audit_report.md** -- Sample Bulletproof React audit report showing expected output format
- **hooks-anti-patterns.tsx** -- Concrete examples of hooks anti-patterns (what NOT to do)
- **hooks-good-patterns.tsx** -- Correct hooks patterns (what TO do)

## Key Features

- **5-layer Next.js architecture**: Types -> Services -> Hooks -> Components -> Pages with clear separation of concerns
- **shadcn/ui component system**: CVA variants, Tailwind CSS theming with CSS variables, and composable component patterns
- **Hooks optimization**: Identifies and eliminates derived state anti-patterns, unnecessary effects, props-to-state syncing, and premature memoization
- **Bulletproof React auditing**: Automated code quality analysis with severity classification across 11 dimensions
- **fpkit component library**: Patterns for building and consuming @fpkit/acss components with accessibility built in
- **Accessibility-first**: WCAG 2.1 AA compliance patterns including keyboard navigation, screen reader support, and ARIA attributes
- **Server/client boundary**: Clear guidance on when to use server components vs. client components in Next.js App Router
- **Component scaffolding**: Scripts and templates for rapidly creating well-structured, tested, documented components

## Usage Examples

Build a Next.js page with the 5-layer architecture:
```
Create a users management page for my Next.js app with Supabase. I need a service layer for data access, a React Query hook for client-side state, and a page component with a data table. Follow the 5-layer architecture.
```

Create a shadcn/ui component with variants:
```
Build a Badge component using shadcn/ui patterns with CVA variants for: default, success, warning, error, and outline. Include size variants (sm, md, lg) and make it accessible.
```

Audit a React codebase:
```
Audit this React component for Bulletproof React best practices. Check for hooks anti-patterns, accessibility issues, performance problems, and proper error handling.
```

Fix hooks anti-patterns:
```
Review this component -- it uses useState + useEffect to derive filtered results from a list. Show me how to fix the derived state anti-pattern and any other hooks issues.
```

Set up a component library:
```
Help me scaffold a new component for our fpkit-based design system. It's a Card component that needs composition (CardHeader, CardBody, CardFooter), CSS variable theming, and Storybook stories.
```

## Quick Start

1. Describe what you are building: a Next.js app, a component library, or optimizing existing React code.
2. The skill selects the right approach via the decision tree: Next.js architecture, shadcn/ui patterns, fpkit patterns, hooks optimization, or Bulletproof audit.
3. For new Next.js features, you get the full 5-layer implementation: types, service, hook, component, and page.
4. For component work, you get scaffolded code with variants, accessibility, tests, and Storybook stories.
5. For optimization, you get specific anti-pattern identification with before/after code examples.

## Related Skills

- **TDD (Test-Driven Development)** -- Write tests for React components using testing-library
- **Code Review** -- Systematic review of React application architecture
- **Python Development** -- Build backend APIs that serve your React frontend
- **Prompt Engineering** -- Design AI-powered features within React applications

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 34 production-grade skills for Claude Code.
