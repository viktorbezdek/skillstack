# Frontend Design

> **v1.1.23** | Development | 25 iterations

> Build beautiful, accessible, production-grade user interfaces with Tailwind CSS, Radix UI, and shadcn/ui -- design systems, tokens, WCAG compliance, and Figma-to-code workflows in one plugin.

## The Problem

Frontend development requires juggling an extraordinary number of concerns simultaneously: visual design, accessibility, responsive layout, dark mode, design tokens, component architecture, performance optimization, and testing. Each concern has its own best practices, tooling, and failure modes. A developer building a single data table needs to think about WCAG 2.2 contrast ratios, keyboard navigation, responsive breakpoints, Tailwind utility classes, Radix UI primitives, and whether the loading state handles zero results.

Without a unified framework, these concerns fragment across separate documentation, blog posts, and tribal knowledge. Teams end up with inconsistent component implementations: one form uses inline styles, another uses CSS modules, a third uses Tailwind with inconsistent spacing tokens. Accessibility is treated as an afterthought -- added after the visual design is complete, at 10x the cost. Design tokens exist in Figma but never make it into code, creating a permanent drift between design and implementation.

The cost shows up in three ways. First, every new component is built from scratch instead of composed from validated primitives, wasting days of developer time. Second, accessibility audits consistently fail because WCAG compliance was not built into the component architecture from the start. Third, design-to-code handoff is manual and lossy -- designers specify tokens in Figma, developers approximate them in code, and the two drift further apart with every sprint.

## The Solution

This plugin consolidates 11 specialized frontend skills into a single comprehensive skill covering the complete frontend design stack. It provides a three-pillar architecture (Tailwind CSS for styling, Radix UI for accessible behavior, shadcn/ui for pre-built components) with a decision tree that routes any frontend question to the right approach and reference material.

The skill ships with 59 reference files covering every major frontend concern: design tokens (W3C DTCG format), accessibility (WCAG 2.2 guidelines and patterns), responsive layout, Tailwind utilities, CSS variables, shadcn/ui components, Radix UI primitives, Storybook integration, performance optimization, form patterns, data tables, animation, routing, file organization, and testing. It includes 30+ automation scripts for common tasks (component scaffolding, token extraction from Figma, accessibility auditing, UI evaluation, CSS validation) and 5 code templates for design tokens and component generation.

The plugin activates when you work on any UI-related task and provides the relevant subset of its knowledge -- not the full 59-reference corpus -- based on what you are building.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Each component built from scratch with inconsistent styling approach (inline, CSS modules, Tailwind) | Three-pillar architecture (Tailwind + Radix + shadcn) with consistent component composition patterns |
| Accessibility added as afterthought; WCAG audits fail and fixes cost 10x the original work | WCAG 2.2 compliance built into component primitives via Radix UI; accessibility checklist applied from the start |
| Design tokens exist in Figma but not in code; design and implementation drift apart every sprint | Figma-to-code pipeline: extract tokens with scripts, validate with automation, generate CSS/SCSS/TS output |
| Dark mode implementation varies per component; some work, some break, some are forgotten | Three-tier token architecture (primitives -> semantics -> components) where only semantic tokens change for dark mode |
| No systematic way to evaluate UI quality; "it looks fine" is the acceptance criteria | Playwright-based UI evaluation scripts, CSS validation tools, and A/B comparison automation |
| Component scaffolding is manual; each developer's file structure is different | Automation scripts generate components with consistent structure, types, tests, and Storybook stories |

## Installation

Add the SkillStack marketplace, then install this plugin:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install frontend-design@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when your prompts mention UI components, design systems, Tailwind, CSS, accessibility, responsive layout, dark mode, shadcn/ui, Radix UI, or design tokens.

## Quick Start

1. Install the plugin using the commands above
2. Open a Claude Code session in your frontend project
3. Type: `Build a responsive dashboard card component with shadcn/ui that handles loading, error, and empty states`
4. Claude produces a complete component using the three-pillar architecture: Tailwind for styling, Radix primitives for accessibility, shadcn/ui Card for the base, with responsive breakpoints and WCAG-compliant contrast
5. Next, try: `Set up a design token system for our project using the three-tier architecture`

---

## System Overview

```
User prompt (build component / design tokens / accessibility / responsive layout)
        |
        v
+------------------+     +----------------------------------+
|  frontend-design |---->| Decision tree routes to:          |
|  skill (SKILL.md)|     | - Component creation workflow     |
+------------------+     | - Styling approach selection      |
                          | - Design system setup             |
                          | - Accessibility audit             |
                          | - UI evaluation/testing           |
                          | - Performance optimization        |
                          +----------------------------------+
                                    |
            +-----------------------+-----------------------+
            |                       |                       |
            v                       v                       v
    59 Reference Files       30+ Scripts              5 Templates
    (loaded on demand)       (automation)             (code gen)
    - Tailwind (4)           - scaffolding            - CSS variables
    - shadcn/ui (4)          - token extraction       - SCSS variables
    - Radix UI (1)           - accessibility audit    - TypeScript types
    - Accessibility (5)      - UI evaluation          - W3C tokens
    - Design tokens (4)      - CSS validation         - Documentation
    - Component patterns (6) - Figma integration
    - Testing (3)            - style analysis
    - Performance (2)        - component generation
    - Responsive (3)
    - Animation (1)
    - Storybook (2)
    - Forms/Data tables (2)
    - ...and more
```

Single-skill plugin with 59 references, 30+ scripts, 5 templates, and component template assets. References are loaded selectively based on the query topic.

## What's Inside

| Component | Type | Count | What It Provides |
|---|---|---|---|
| **frontend-design** | Skill | 1 | Three-pillar architecture, decision tree, quick start, best practices |
| **References** | Reference | 59 | Deep domain knowledge across all frontend concerns |
| **Scripts** | Script | 30+ | Automation for scaffolding, tokens, accessibility, evaluation, validation |
| **Templates** | Template | 5 | Code generation templates for tokens and documentation |
| **Component Templates** | Asset | 6 | Starter templates for components, stories, tests, and types |
| **Design Tokens** | Asset | 1 | Reference token set (JSON) |
| **trigger-evals** | Eval | 13 | 8 positive, 5 negative trigger eval cases |
| **output-evals** | Eval | 3 | Output quality eval cases |

### Component Spotlights

#### frontend-design (skill)

**What it does:** Activates when you work on UI components, design systems, styling, accessibility, responsive layout, or any visual frontend concern. Routes your request through a decision tree to the appropriate workflow and loads only the relevant references from its 59-file knowledge base.

**Input -> Output:** You describe a UI need (component, layout, design system, accessibility fix) -> The skill produces production-ready code using the Tailwind + Radix + shadcn architecture, with WCAG compliance, responsive breakpoints, and proper token usage.

**When to use:**
- Building UI components with React, Vue, or Next.js
- Implementing design systems (shadcn/ui, Radix UI, fpkit)
- Styling with Tailwind CSS, CSS Modules, or CSS-in-JS
- Creating responsive, mobile-first layouts
- Implementing dark mode and theme customization
- Building accessible components (WCAG 2.2 compliance)
- Generating design tokens from Figma
- Evaluating and improving UI quality with Playwright

**When NOT to use:**
- React component logic, hooks, or state management -> use [react-development](../react-development/)
- Next.js routing, SSR, or server components -> use [nextjs-development](../nextjs-development/)
- Backend API development -> use [api-design](../api-design/) or [typescript-development](../typescript-development/)

**Try these prompts:**

```
Build a responsive data table component with sorting, pagination, and keyboard navigation using shadcn/ui
```

```
Set up a three-tier design token system for our project -- primitives, semantics, and component tokens with dark mode support
```

```
Audit this component for WCAG 2.2 AA accessibility compliance. Check contrast, keyboard navigation, and screen reader support.
```

```
Extract design tokens from our Figma file and generate CSS variables, SCSS variables, and TypeScript types
```

```
Create a form with validation using React Hook Form + Zod + shadcn/ui components, including error states and loading states
```

**Key reference categories:**

| Category | References | Topics |
|---|---|---|
| Tailwind CSS | 4 | Utilities, responsive patterns, customization, reference |
| shadcn/ui | 4 | Components, accessibility, theming, reference |
| Accessibility | 5 | WCAG guidelines, patterns, checklist, Radix guarantees |
| Design Tokens | 4 | W3C DTCG spec, naming conventions, token architecture |
| Component Patterns | 6 | Composition, architecture, common patterns, UI canvas |
| Responsive | 3 | Breakpoints, fluid layouts, responsive patterns |
| Testing | 3 | Testing patterns, setup, Playwright evaluation |
| Performance | 2 | Core Web Vitals, optimization strategies |
| Storybook | 2 | Story patterns, integration |
| Forms & Data | 2 | Form patterns, data tables |
| Animation | 1 | Motion patterns and transitions |

#### Scripts (automation tools)

**Component scaffolding:**
- `scaffold_component.py` / `generate_component.sh` / `generate-component.py` -- Generate component boilerplate with consistent file structure
- `shadcn_add.py` -- Add shadcn/ui components with proper configuration
- `init-component.ts` -- TypeScript-based component initialization

**Design tokens:**
- `extract_tokens.py` -- Extract tokens from Figma files
- `transform_tokens.py` -- Transform tokens to CSS/SCSS/TS formats
- `validate_tokens.py` -- Validate token consistency and naming
- `design_token_generator.py` / `design-token-generator.ts` -- Generate token files

**Quality and validation:**
- `audit_accessibility.sh` -- Run WCAG accessibility audit
- `evaluate-ui.ts` -- Evaluate UI quality with Playwright
- `compare-variations.ts` -- A/B compare UI variations
- `validate_css_vars.py` -- Validate CSS variable usage
- `validate_consistency.py` -- Check design consistency

**Analysis and suggestions:**
- `analyze_components.py` / `analyze_styles.py` -- Analyze existing components and styles
- `suggest_improvements.py` / `suggest_reuse.py` -- Suggest improvements and reuse opportunities
- `recommend_approach.py` -- Recommend the right styling approach

#### Templates (code generation)

| Template | Format | Purpose |
|---|---|---|
| `css-variables.template.css` | CSS | CSS custom properties template |
| `scss-variables.template.scss` | SCSS | SCSS variables template |
| `typescript-types.template.ts` | TypeScript | Token type definitions |
| `w3c-tokens.template.json` | JSON | W3C DTCG token format |
| `documentation.template.md` | Markdown | Component documentation |

---

## Prompt Patterns

### Good Prompts vs Bad Prompts

| Bad (vague, won't activate well) | Good (specific, activates reliably) |
|---|---|
| "Make a button" | "Build a Button component with primary, secondary, and ghost variants using shadcn/ui with proper ARIA labels" |
| "Style my page" | "Apply responsive layout to this dashboard: 3-column grid on desktop, single column on mobile, with consistent spacing tokens" |
| "Fix accessibility" | "Audit this Dialog component for WCAG 2.2 AA: check focus trapping, keyboard navigation, screen reader announcements, and color contrast" |
| "Set up design system" | "Initialize a three-tier design token system with primitives (colors, spacing), semantic tokens (background, foreground), and component tokens (button-height, card-padding)" |
| "Make it look good" | "This card component needs visual polish: add hover elevation transition, consistent border-radius from tokens, and proper loading/error/empty states" |

### Structured Prompt Templates

**For component creation:**
```
Build a [component name] component using [shadcn/ui / Radix / custom]. Requirements: [variants, states, interactions]. It should handle: [loading state / error state / empty state / responsive behavior]. Accessibility: [specific WCAG requirements].
```

**For design token setup:**
```
Set up a design token system for [project]. Token source: [Figma / manual / existing CSS]. Output formats needed: [CSS variables / SCSS / TypeScript types]. Include: [dark mode / high contrast / brand themes].
```

**For accessibility audit:**
```
Audit [component/page] for WCAG 2.2 [AA/AAA] compliance. Check: [contrast ratios / keyboard navigation / focus indicators / screen reader labels / ARIA attributes]. Current framework: [React + Tailwind / Vue / etc.].
```

### Prompt Anti-Patterns

- **Skipping the framework context:** "Build a modal" without specifying React, Vue, or vanilla -- the skill needs to know the framework to select the right component library and patterns.
- **Asking for visual design without constraints:** "Make it beautiful" -- beauty is subjective. Specify design tokens, brand guidelines, or reference designs.
- **Requesting React logic instead of styling:** "Implement the state management for this form" -- this skill handles visual design and accessibility, not component logic. Use [react-development](../react-development/) for hooks and state.

## Real-World Walkthrough

You are building a SaaS analytics dashboard. The designer has handed over Figma mockups with a custom color palette, specific spacing values, and a component library that includes cards, charts, data tables, and a sidebar navigation. Your job is to implement this in React with Tailwind CSS, ensuring WCAG AA accessibility and responsive behavior down to tablet.

**Step 1: Token extraction.** You start by asking Claude: **"Extract the design tokens from our Figma file and set up a three-tier token system for this project."**

Claude activates the frontend-design skill and loads the design token references. It guides you through the extraction pipeline: run `extract_tokens.py` with your Figma file key to pull raw tokens, then `transform_tokens.py` to generate CSS custom properties, SCSS variables, and TypeScript type definitions. The three-tier architecture is set up:

```css
:root {
  /* Tier 1: Primitives (immutable) */
  --blue-500: oklch(0.55 0.22 264);
  --gray-50: 250 250 250;
  
  /* Tier 2: Semantics (theme-aware) */
  --background: var(--gray-50);
  --primary: var(--blue-500);
  
  /* Tier 3: Components */
  --card-padding: 1.5rem;
  --sidebar-width: 16rem;
}
.dark {
  --background: var(--gray-900);
}
```

**Step 2: Component scaffolding.** You then ask: **"Build a responsive dashboard card component that shows a metric with a trend indicator, handles loading and error states, and follows our token system."**

Claude produces a Card component using shadcn/ui as the base, Tailwind for styling with your custom tokens, and proper loading/error states. The component is responsive (full-width on mobile, fits a 3-column grid on desktop) and includes ARIA labels for the trend indicator (so screen readers announce "Revenue: $42,000, up 12% from last month").

**Step 3: Data table with accessibility.** Next: **"Build a sortable, paginated data table for user analytics. It needs keyboard navigation and should announce sort changes to screen readers."**

Claude loads the data tables and accessibility references. It produces a table using Radix UI primitives for keyboard navigation (arrow keys to move between cells, Enter to sort) with `aria-sort` attributes that update dynamically. Pagination is keyboard-accessible with proper focus management when the page changes.

**Step 4: Accessibility audit.** You run: **"Audit the entire dashboard for WCAG 2.2 AA compliance."**

Claude walks through the accessibility checklist: contrast ratios on all text (your gray-on-white body text is 4.2:1 -- fails AA for normal text, needs to darken to 4.5:1), keyboard navigation flow (sidebar -> cards -> table with logical tab order), focus indicators (visible on all interactive elements), and screen reader experience (all charts have alt text or aria-described-by fallbacks).

**Step 5: Responsive verification.** Finally: **"Verify the responsive behavior: 3-column card grid on desktop, 2-column on tablet, single column on mobile. Sidebar collapses to a hamburger menu below 768px."**

Claude produces the responsive Tailwind classes (`grid-cols-1 md:grid-cols-2 lg:grid-cols-3`) and the sidebar collapse logic using a Radix Sheet component for the mobile menu, with proper focus trapping and escape-to-close behavior.

You now have a design-token-driven dashboard with consistent styling, WCAG AA compliance, responsive behavior, and accessible components -- built on the three-pillar architecture that ensures all future components follow the same patterns.

## Usage Scenarios

### Scenario 1: Setting up a design system from Figma

**Context:** Your designer has a complete Figma design system with colors, typography, spacing, and component specs. You need to implement it in code as a reusable token system.

**You say:** "Extract design tokens from our Figma file (key: abc123) and generate a three-tier token system with CSS variables, dark mode support, and TypeScript types."

**The skill provides:**
- Figma extraction pipeline using `extract_tokens.py`
- Token transformation to CSS, SCSS, and TypeScript using `transform_tokens.py`
- Three-tier architecture setup (primitives -> semantics -> components)
- Dark mode configuration where only semantic tokens change
- Validation script to ensure token consistency

**You end up with:** A complete design token system that stays synchronized with Figma, generates code in multiple formats, and supports dark mode through semantic token switching.

### Scenario 2: Building an accessible form

**Context:** You need a registration form with email, password, and date of birth fields. It must be WCAG 2.2 AA compliant, validate in real-time, and show clear error messages.

**You say:** "Build a registration form with React Hook Form + Zod + shadcn/ui. Real-time validation, accessible error messages, and proper focus management on validation failure."

**The skill provides:**
- Form component using shadcn/ui Form primitives with Zod schema validation
- ARIA-described-by linking each field to its error message
- Focus management: on submit with errors, focus moves to the first invalid field
- Loading state for the submit button with disabled state and aria-busy
- Keyboard-accessible date picker using Radix Popover

**You end up with:** A production-ready form that validates correctly, announces errors to screen readers, and manages focus for keyboard users.

### Scenario 3: Evaluating and comparing UI variations

**Context:** You have two versions of a landing page and want to compare their visual quality and accessibility before choosing one.

**You say:** "Compare these two landing page variations using the UI evaluation framework. Check visual quality, accessibility, and performance."

**The skill provides:**
- Playwright-based evaluation using `evaluate-ui.ts` for both variations
- Side-by-side comparison using `compare-variations.ts`
- Accessibility audit results for both (contrast, keyboard nav, screen reader)
- Performance metrics (Largest Contentful Paint, Cumulative Layout Shift)
- Recommendation with specific trade-offs between the two designs

**You end up with:** An evidence-based recommendation for which variation to ship, with specific metrics and identified issues to fix in the chosen version.

---

## Decision Logic

The skill uses a decision tree to route your request to the right workflow:

| You are doing... | Workflow | Key references loaded |
|---|---|---|
| Creating a new UI component | Component creation workflow | component-patterns, composition, shadcn-components |
| Styling existing UI | Styling workflow | tailwind-utilities, css-variables, styling-guide |
| Setting up a design system | Design system workflow | DESIGN_TOKENS, token-naming-conventions, w3c-dtcg-spec |
| Accessibility audit/fix | Accessibility workflow | accessibility-guidelines, accessibility-patterns, accessibility_checklist |
| Evaluating/testing UI | Evaluation workflow | playwright-evaluation, testing-patterns |
| Performance optimization | Performance workflow | PERFORMANCE_OPTIMIZATION, performance |
| Responsive layout | Responsive workflow | RESPONSIVE_PATTERNS, tailwind-responsive |

## Failure Modes & Edge Cases

| Failure | Symptom | Recovery |
|---|---|---|
| No framework specified in prompt | Skill defaults to React + Tailwind; output may not match your stack | Specify the framework: "using Vue 3" or "using Svelte with Tailwind" |
| Design tokens not set up in the project | Generated components use token references (var(--primary)) that don't resolve | Run the design token setup first, or ask the skill to generate inline fallback values |
| Figma file key invalid or access denied | Token extraction script fails with API error | Verify the Figma file key and ensure API access token has read permission |
| WCAG AAA requested but not practical | Skill flags AAA contrast (7:1) as impractical for most UI text | Clarify whether you need AA (4.5:1, standard) or AAA (7:1, enhanced). Most production UIs target AA. |
| Component too complex for single prompt | A "build entire dashboard" request produces a surface-level implementation | Break into smaller requests: tokens first, then individual components, then composition and layout |

## Ideal For

- **Frontend developers** building React/Next.js applications who want consistent, accessible component architecture
- **Design system teams** establishing or maintaining a token-based design system with Figma-to-code automation
- **Accessibility-focused teams** who need WCAG 2.2 compliance built into the component layer, not bolted on after
- **Full-stack developers** who need to build quality UI without deep frontend specialization -- the three-pillar architecture provides guardrails
- **Teams using shadcn/ui** who want to go beyond copy-paste and understand the composition patterns that make shadcn components extensible

## Not For

- **React component logic and state management** -- hooks, context, reducers, and data flow. Use [react-development](../react-development/)
- **Next.js routing, SSR, and server components** -- App Router, middleware, data fetching. Use [nextjs-development](../nextjs-development/)
- **Backend API development** -- even if the API serves a frontend. Use [api-design](../api-design/) or [typescript-development](../typescript-development/)

## Related Plugins

- **[React Development](../react-development/)** -- Component logic, hooks, state management, and React patterns
- **[Next.js Development](../nextjs-development/)** -- App Router, SSR, server components, and Next.js-specific patterns
- **[TypeScript Development](../typescript-development/)** -- Type system patterns, generics, and TypeScript tooling
- **[Consistency Standards](../consistency-standards/)** -- Naming conventions and style guides for uniform component naming
- **[Testing Framework](../testing-framework/)** -- Test infrastructure for component testing beyond the UI evaluation scripts included here

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
