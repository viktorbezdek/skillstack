# Frontend Design

> **v1.1.23** | Development | 25 iterations

Comprehensive Frontend Design (UI/UX) skill combining UI design systems, component libraries, CSS/Tailwind styling, accessibility patterns, and visual design.

## What Problem Does This Solve

Frontend teams routinely reinvent design decisions -- colours, spacing, dark mode tokens, accessible keyboard patterns -- because the knowledge is scattered across specialist areas and rarely consolidated in one place. This skill merges that expertise into a single reference covering the Tailwind CSS + Radix UI + shadcn/ui stack, Figma-to-token extraction, WCAG 2.2 compliance, responsive layout, Storybook patterns, and UI evaluation -- so developers can build consistent, accessible UIs without context-switching across multiple docs.

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install frontend-design@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention the triggers below, or you can invoke it explicitly.

## What's Inside

This is a large single-skill plugin with a SKILL.md, 58 reference files, 30+ scripts, component templates, and design token templates.

### Core Architecture

The skill is organised around three pillars:

| Layer | Technology | Role |
|---|---|---|
| **Styling** | Tailwind CSS | Utility-first CSS with build-time generation, zero runtime overhead, design tokens for colors/spacing/typography |
| **Behavior** | Radix UI | Unstyled accessible component primitives with WAI-ARIA, keyboard navigation, focus management |
| **Components** | shadcn/ui | Complete pre-built components combining Tailwind styling with Radix behavior |

### Reference Files (58 files)

Organised across these domains:

- **Accessibility** -- WCAG 2.2 guidelines, accessibility checklist, accessible component patterns, audit procedures
- **Architecture** -- Component patterns, composition patterns, file organisation, integration patterns
- **Design Tokens** -- CSS variable guide, three-tier token architecture (primitives/semantics/components), W3C DTCG spec, Figma extraction
- **Tailwind** -- Utilities reference, responsive patterns, customisation guide
- **shadcn/ui** -- Component reference, theming, accessibility integration
- **Testing** -- Testing patterns, Storybook integration, Playwright-based UI evaluation
- **Performance** -- Core Web Vitals, performance optimisation, loading and error states

### Scripts (30+ files)

| Script | Purpose |
|---|---|
| `extract_tokens.py` | Extract design tokens from Figma |
| `transform_tokens.py` | Transform tokens into CSS/SCSS/TypeScript |
| `validate_tokens.py` | Validate token naming and structure |
| `audit_accessibility.sh` | Run accessibility audit against WCAG criteria |
| `evaluate-ui.ts` | Playwright-based UI quality evaluation |
| `compare-variations.ts` | A/B comparison of UI design variations |
| `generate_component.sh` | Scaffold new components with templates |
| `setup_design_system.sh` | Set up a complete design system |
| `scaffold_component.py` | Component scaffolding with types and tests |
| `shadcn_add.py` | Add shadcn/ui components to a project |

### Templates

- Component templates (Button.tsx, Input.tsx, composed, extended, stories, tests, types)
- CSS variables template, SCSS variables template, TypeScript types template, W3C tokens template
- Documentation template for components

## How to Use

**Direct invocation:**

```
Use the frontend-design skill to build a dashboard card component with Tailwind and shadcn/ui
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

`frontend` · `ui-ux` · `tailwind` · `accessibility` · `design-tokens`

## Usage Scenarios

**1. Building a dashboard component from scratch.** You need a responsive card grid with dark mode support. The skill provides the shadcn/ui setup commands, a working TypeScript/React example, and the three-tier CSS variable architecture for light/dark theming -- getting you from zero to a polished component in minutes rather than hours.

**2. Setting up a design token pipeline from Figma.** Your designer exports tokens from Figma and you need them in CSS variables, SCSS, and TypeScript types. Use the `extract_tokens.py` -> `transform_tokens.py` -> `validate_tokens.py` pipeline to automate the conversion, with validation catching naming violations before they ship.

**3. Achieving WCAG AA compliance on an existing UI.** Run `audit_accessibility.sh` against your app to get a report of contrast failures, missing ARIA labels, and keyboard navigation gaps. Then use the accessibility patterns reference to fix each finding with the correct Radix UI primitives.

**4. Evaluating two design options objectively.** You have two candidate designs for a settings page and need to decide. Use `evaluate-ui.ts` for automated quality scoring and `compare-variations.ts` for side-by-side A/B evaluation, producing quantitative data for the design review.

**5. Scaffolding a component library for a new project.** Run `setup_design_system.sh` to initialise Tailwind, install Radix UI and shadcn/ui, set up the token architecture, and generate starter components with TypeScript types, Storybook stories, and test files already wired up.

## When to Use / When NOT to Use

**Use when:** You are building UI components, implementing design systems, styling with Tailwind/CSS, creating accessible interfaces, extracting design tokens from Figma, or evaluating UI quality.

**Do NOT use for:**
- **React component logic, hooks, or state management** -- use [react-development](../react-development/)
- **Next.js routing, SSR, or server components** -- use [nextjs-development](../nextjs-development/)

## Related Plugins in SkillStack

- **[API Design](../api-design/)** -- REST, GraphQL, and gRPC API design patterns
- **[Nextjs Development](../nextjs-development/)** -- App Router, Server Components, and Next.js framework patterns
- **[React Development](../react-development/)** -- Hooks, state management, and React component architecture
- **[TypeScript Development](../typescript-development/)** -- Type system patterns, generics, and TypeScript best practices

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
