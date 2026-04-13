# Frontend Design

> **v1.1.23** | Development | 25 iterations

> Build beautiful, accessible, production-grade user interfaces with Tailwind CSS, Radix UI, and shadcn/ui -- design systems, tokens, WCAG compliance, and Figma-to-code workflows in one plugin.

## The Problem

Building a polished frontend means mastering at least five specialist domains simultaneously: CSS styling, accessible component behavior, design token architecture, responsive layout, and visual quality evaluation. Each domain has its own documentation, best practices, and tooling. A developer building a dashboard card needs to know Tailwind utilities for styling, Radix UI primitives for accessible dropdowns, CSS variable architecture for dark mode, WCAG contrast ratios for text readability, and responsive breakpoints for mobile layout -- all for a single component.

The knowledge is scattered across dozens of documentation sites, tutorials, and blog posts. The Tailwind docs explain utilities but not how to structure a design token system. The Radix UI docs explain accessible primitives but not how to style them with Tailwind. The WCAG spec defines contrast requirements but not how to implement them in a component library. The result is that developers spend more time context-switching between docs than writing code, and the gaps between domains produce components that look right but fail accessibility audits, work on desktop but break on mobile, or use hardcoded colors that cannot be themed.

Design token pipelines add another layer of complexity. When a designer updates colors in Figma, those changes need to flow through extraction, transformation, and validation before landing in CSS variables -- and the naming conventions must follow a three-tier architecture (primitives, semantics, components) to support dark mode and theming. Without automation, this pipeline is manual, error-prone, and typically abandoned after the first sprint.

## The Solution

This plugin consolidates expertise from 11 specialized frontend/UI skills into a single reference covering the full Tailwind CSS + Radix UI + shadcn/ui stack. Instead of navigating between documentation sites, Claude has immediate access to utility references, component patterns, accessibility guidelines, design token architecture, responsive patterns, and UI evaluation tooling -- all structured to work together.

The three-pillar architecture provides a clear mental model: Tailwind CSS for styling (zero runtime overhead, design tokens for colors/spacing/typography), Radix UI for behavior (WAI-ARIA compliant primitives with keyboard navigation and focus management), and shadcn/ui for complete components (pre-built components combining Tailwind styling with Radix behavior that you own and customize).

Beyond reference material, the plugin ships 30+ runnable scripts: `extract_tokens.py` pulls design tokens from Figma, `transform_tokens.py` generates CSS/SCSS/TypeScript output, `validate_tokens.py` catches naming violations, `audit_accessibility.sh` runs WCAG compliance checks, `evaluate-ui.ts` scores UI quality with Playwright, and `compare-variations.ts` produces quantitative A/B comparisons of design alternatives. Component templates provide starting points for buttons, inputs, composed components, stories, tests, and TypeScript types.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Developer context-switches between Tailwind docs, Radix docs, shadcn docs, and WCAG spec to build one component | All five domains consolidated in a single skill with a decision tree routing to the right reference |
| Dark mode requires manually defining every color twice -- once for light, once for dark | Three-tier token architecture: primitives are immutable, semantic tokens swap, components inherit automatically |
| Accessibility is checked after the component ships (if at all) | WCAG 2.2 checklist and Radix UI's built-in ARIA guarantees make accessibility a build-time concern |
| Design token updates from Figma are manual, error-prone, and typically abandoned | Automated pipeline: `extract_tokens.py` -> `transform_tokens.py` -> `validate_tokens.py` |
| Design decisions are subjective -- "I think version A looks better" | `evaluate-ui.ts` and `compare-variations.ts` produce quantitative quality scores for objective comparison |
| New components start from scratch every time | Component templates with TypeScript types, Storybook stories, and test files already wired up |

## Installation

Add the SkillStack marketplace, then install this plugin:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install frontend-design@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when your prompts mention frontend design, UI/UX, Tailwind CSS, design tokens, accessibility, or component libraries.

## Quick Start

1. Install the plugin using the commands above
2. Open a Claude Code session in your project
3. Type: `Build a responsive dashboard card component with dark mode support using shadcn/ui and Tailwind`
4. Claude produces a complete component with the three-tier CSS variable architecture for light/dark theming, responsive layout with Tailwind breakpoints, and accessible keyboard interaction via Radix primitives
5. Next, try: `Set up a design token pipeline from our Figma file` to automate the extraction-transformation-validation workflow

## What's Inside

Large single-skill plugin with one SKILL.md, 58 reference files, 30+ scripts, component templates, design token templates, 13 trigger eval cases, and 3 output eval cases.

| Domain | References | What It Covers |
|---|---|---|
| **Accessibility** | 4 files | WCAG 2.2 guidelines, accessibility checklist, accessible component patterns, audit procedures |
| **Architecture** | 4 files | Component patterns, composition patterns, file organization, integration patterns |
| **Design Tokens** | 5 files | CSS variable guide, three-tier token architecture, W3C DTCG spec, Figma extraction, naming conventions |
| **Tailwind CSS** | 4 files | Utilities reference, responsive patterns, customization guide, common patterns |
| **shadcn/ui** | 5 files | Component reference, theming, accessibility integration, advanced usage, data tables |
| **Radix UI** | 1 file | Full primitive reference with ARIA guarantees |
| **Testing** | 4 files | Testing patterns, Storybook integration, Playwright evaluation, setup guide |
| **Performance** | 3 files | Core Web Vitals, performance optimization, loading and error states |
| **Visual Design** | 4 files | Design principles, style guide template, animation patterns, canvas design system |
| **Other** | 24 files | Form patterns, routing, data fetching, troubleshooting, anti-patterns, complete examples |

### Scripts

| Script | Purpose |
|---|---|
| `extract_tokens.py` | Extract design tokens from Figma via API |
| `transform_tokens.py` | Transform tokens into CSS, SCSS, or TypeScript output |
| `validate_tokens.py` | Validate token naming and structure against conventions |
| `audit_accessibility.sh` | Run WCAG accessibility audit against your app |
| `evaluate-ui.ts` | Playwright-based automated UI quality evaluation |
| `compare-variations.ts` | Quantitative A/B comparison of design variations |
| `generate_component.sh` | Scaffold new components with templates |
| `setup_design_system.sh` | Initialize a complete design system from scratch |
| `scaffold_component.py` | Component scaffolding with types and tests |
| `shadcn_add.py` | Add shadcn/ui components to a project |

### frontend-design

**What it does:** Activates when you ask about building UI components, implementing design systems, styling with Tailwind or CSS, creating accessible interfaces, extracting design tokens from Figma, evaluating UI quality, or working with shadcn/ui and Radix UI. Routes through a decision tree to load only the relevant references from the 58-file library, keeping context lean while providing specialist-depth answers.

**Try these prompts:**

```
Build a settings page with a sidebar navigation, form fields, and a save button -- use shadcn/ui components with dark mode support
```

```
Our designer just exported new tokens from Figma -- set up the extraction pipeline and validate the naming conventions
```

```
Audit this page for WCAG AA compliance -- I need to know every contrast failure, missing ARIA label, and keyboard navigation gap
```

```
I have two design options for the onboarding flow -- evaluate them objectively and tell me which one is better and why
```

```
Set up a component library from scratch with Tailwind, Radix UI, and shadcn/ui -- include TypeScript types, Storybook stories, and test scaffolding
```

## Real-World Walkthrough

You are building the admin dashboard for a SaaS analytics product. The dashboard needs a data table with sorting, filtering, and pagination; a sidebar navigation with collapsible sections; a dark/light theme toggle; and WCAG AA compliance because your enterprise customers require accessibility. Your design team has a Figma file with the color palette, typography scale, and spacing values.

You start by asking Claude: **"Set up the design system foundation for our admin dashboard -- we have a Figma file with tokens and need Tailwind + shadcn/ui + dark mode."**

Claude activates the frontend-design skill and begins with the **design token pipeline**. It walks you through running `extract_tokens.py --file-key YOUR_FIGMA_KEY` to pull the raw tokens from Figma, `transform_tokens.py tokens.json --format css` to generate CSS variables, and `validate_tokens.py tokens.json` to catch any naming violations. The output is a three-tier CSS variable architecture:

```css
:root {
  /* Tier 1: Primitives (from Figma, immutable) */
  --gray-50: 250 250 250;
  --gray-900: 24 24 27;
  --blue-500: oklch(0.55 0.22 264);

  /* Tier 2: Semantic (theme-aware) */
  --background: var(--gray-50);
  --foreground: var(--gray-900);
  --primary: var(--blue-500);

  /* Tier 3: Component */
  --card-padding: 1.5rem;
  --table-row-height: 3rem;
}

.dark {
  --background: var(--gray-900);
  --foreground: var(--gray-50);
}
```

The key insight: only Tier 2 (semantic) tokens change between themes. Primitives are immutable color values; component tokens reference semantics. When the designer adds a new theme, only the semantic layer changes.

Next, you ask: **"Build the data table component with sorting, filtering, and pagination."**

Claude loads the `data-tables.md` and `shadcn-components.md` references. It produces a complete `DataTable` component using shadcn/ui's Table primitives with TanStack Table for headless sorting and filtering logic. The component uses Tailwind utilities for styling, Radix UI's built-in keyboard navigation (arrow keys move between cells, Enter activates sort), and the semantic tokens from your design system. The pagination component uses `Button` variants with proper `aria-label` attributes ("Go to page 2", "Go to next page").

You then ask: **"Now build the sidebar navigation with collapsible sections."**

Claude loads the `composition-patterns.md` and `accessibility-patterns.md` references. It produces a `Sidebar` component using Radix UI's Collapsible primitive for the expandable sections. Each section has a trigger button with `aria-expanded`, the content panel uses `aria-hidden`, and keyboard users can Tab through the navigation items and use Space/Enter to expand sections. The sidebar is responsive -- on mobile it becomes a slide-out drawer using Radix UI's Dialog primitive, triggered by a hamburger menu.

With the components built, you ask: **"Run an accessibility audit on the dashboard."**

Claude references the accessibility checklist and walks through each requirement: semantic HTML (the sidebar uses `<nav>`, the main content uses `<main>`, the table uses `<table>` with proper `<thead>` and `<tbody>`), keyboard accessibility (all interactive elements are reachable via Tab, sort headers respond to Enter), ARIA attributes (the collapsible sections have `aria-expanded`, the table has `aria-sort` on sortable columns), contrast ratios (the semantic tokens are validated against WCAG AA 4.5:1 for text), and focus indicators (visible focus rings on all interactive elements).

The audit catches two issues. First, the filter input is missing an `aria-label` -- it has a visual placeholder but no accessible name for screen readers. Second, the pagination's "..." ellipsis element is read by screen readers as "dot dot dot" instead of being hidden with `aria-hidden="true"`. Claude fixes both inline.

Finally, you ask: **"Compare the current dashboard layout with an alternative that uses a top navigation instead of a sidebar."**

Claude references the `playwright-evaluation.md` and produces instructions for using `compare-variations.ts`. The script captures screenshots of both layouts at three breakpoints (mobile, tablet, desktop), measures visual hierarchy scores, counts the number of clicks to reach key actions, and produces a quantitative comparison. The sidebar layout scores higher on desktop (more visible navigation items, fewer clicks to sub-pages) while the top navigation scores higher on mobile (more vertical content space). Claude recommends keeping the sidebar with a responsive breakpoint that switches to top navigation on mobile -- a pattern documented in the `RESPONSIVE_PATTERNS.md` reference.

The result: a complete admin dashboard with design tokens extracted from Figma, a three-tier CSS variable architecture supporting dark mode, WCAG AA compliant components, and quantitative data supporting the layout decision -- built in a fraction of the time it would take to piece together guidance from five different documentation sites.

## Usage Scenarios

### Scenario 1: Building a component from scratch with accessibility

**Context:** You need a dropdown menu for a user profile icon that includes settings, preferences, and sign-out options.

**You say:** "Build an accessible dropdown menu for user profile actions using shadcn/ui"

**The skill provides:**
- Complete component using Radix UI's DropdownMenu primitive with shadcn/ui styling
- Keyboard navigation (arrow keys, Escape to close, Enter to select)
- Proper ARIA attributes (role, aria-haspopup, aria-expanded)
- Tailwind styling with dark mode support via semantic tokens

**You end up with:** A production-ready dropdown menu that passes WCAG AA and works with keyboard, mouse, and screen readers.

### Scenario 2: Setting up a Figma-to-code token pipeline

**Context:** Your design team maintains a Figma file with the brand's color palette, typography scale, and spacing. Every time they update, you manually copy values into CSS.

**You say:** "Automate our design token pipeline from Figma to CSS variables with validation"

**The skill provides:**
- Script chain: `extract_tokens.py` -> `transform_tokens.py` -> `validate_tokens.py`
- Three-tier token architecture setup (primitives, semantics, components)
- Naming convention validation rules
- CI integration guidance for automated token updates

**You end up with:** An automated pipeline where Figma changes flow through extraction, transformation, and validation before landing in your CSS -- with naming violations caught before they merge.

### Scenario 3: Achieving WCAG AA compliance on an existing UI

**Context:** Your enterprise customer requires accessibility compliance and your current UI has never been audited.

**You say:** "Audit our settings page for WCAG AA compliance and fix every issue you find"

**The skill provides:**
- Systematic checklist: semantic HTML, keyboard accessibility, ARIA attributes, contrast ratios, focus indicators, skip links
- Specific findings with code-level fixes (e.g., "Line 42: input missing aria-label")
- Radix UI primitives that provide accessibility guarantees out of the box
- Contrast validation against the 4.5:1 text ratio and 3:1 UI component ratio

**You end up with:** A fully compliant page with each fix documented and the accessibility checklist verified.

### Scenario 4: Evaluating two design alternatives objectively

**Context:** Your team is debating between a card-based layout and a list-based layout for the product catalog page. The discussion is going in circles.

**You say:** "Compare these two layout options with quantitative evaluation -- card grid vs. list view for our product catalog"

**The skill provides:**
- Playwright-based UI evaluation using `evaluate-ui.ts` for automated quality scoring
- A/B comparison via `compare-variations.ts` with screenshots at multiple breakpoints
- Metrics: visual hierarchy, information density, click depth, responsive behavior
- Recommendation with quantitative backing

**You end up with:** Data-driven layout decision with scores for each option across multiple criteria, ending the subjective debate.

### Scenario 5: Scaffolding a component library for a new project

**Context:** You are starting a new project and need a complete component library with consistent theming, accessibility, and testing from day one.

**You say:** "Set up a complete component library from scratch -- Tailwind, shadcn/ui, design tokens, Storybook, and testing"

**The skill provides:**
- `setup_design_system.sh` to initialize the full stack
- Three-tier token architecture with CSS variables for theming
- Component templates with TypeScript types, Storybook stories, and test files
- File organization following the architecture reference
- Quality gates: token validation, accessibility audit, UI evaluation

**You end up with:** A ready-to-build component library where every new component starts with types, stories, and tests pre-configured.

## Ideal For

- **Frontend developers building with the Tailwind + Radix + shadcn/ui stack** -- the three-pillar architecture and 58 reference files cover every aspect of this stack in one place
- **Teams that need WCAG AA compliance** -- accessibility checklist, Radix UI's built-in ARIA guarantees, and the audit script catch issues at build time, not in a compliance review
- **Design system engineers maintaining token pipelines** -- the Figma extraction scripts and three-tier token architecture automate what most teams do manually
- **Tech leads evaluating UI quality objectively** -- Playwright-based evaluation and A/B comparison scripts replace subjective design debates with quantitative data
- **Developers starting new frontend projects** -- scaffolding scripts and component templates get you to a production-quality foundation in minutes

## Not For

- **React component logic, hooks, or state management** -- this plugin covers styling and visual design, not React internals. Use [react-development](../react-development/) for hooks, context, reducers, and component lifecycle
- **Next.js routing, SSR, or server components** -- use [nextjs-development](../nextjs-development/) for App Router, Server Components, and Next.js framework patterns
- **Backend API design** -- use [api-design](../api-design/) for REST, GraphQL, and gRPC patterns

## How It Works Under the Hood

The plugin consolidates expertise from 11 specialized frontend/UI skills into a single SKILL.md with a decision tree that routes queries to the appropriate references. The decision tree has five branches:

1. **Creating new UI components** -- routes to component patterns, shadcn/ui references, and scaffolding scripts
2. **Styling existing UI** -- routes to Tailwind utilities, CSS variables, and theming references
3. **Design system work** -- routes to design token references and extraction/transformation scripts
4. **Accessibility concerns** -- routes to WCAG guidelines, accessibility patterns, and audit scripts
5. **Evaluating/testing UI** -- routes to Playwright evaluation scripts and comparison tooling

The 58 reference files are loaded progressively -- Claude reads only the references relevant to the current query. A question about building a dropdown loads `shadcn-components.md` and `accessibility-patterns.md` but not `DESIGN_TOKENS.md` or `performance.md`. This keeps context lean while providing specialist depth on demand.

The 30+ scripts provide automation for tasks that would otherwise be manual: Figma token extraction, CSS validation, accessibility auditing, UI quality scoring, component scaffolding, and design system initialization.

## Related Plugins

- **[React Development](../react-development/)** -- Hooks, state management, and React component architecture -- pairs with this plugin (design the UI here, implement the logic there)
- **[Next.js Development](../nextjs-development/)** -- App Router, Server Components, SSR, and Next.js framework patterns
- **[TypeScript Development](../typescript-development/)** -- Type system patterns, generics, and TypeScript best practices for type-safe components
- **[API Design](../api-design/)** -- REST, GraphQL, and gRPC API design for the backend that feeds your frontend

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
