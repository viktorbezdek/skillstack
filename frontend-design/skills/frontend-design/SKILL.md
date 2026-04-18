---
name: frontend-design
description: Visual design systems, UI/UX styling, Tailwind CSS, CSS variables, component libraries (shadcn/ui, Radix UI), design tokens, accessibility (WCAG), responsive layout, dark mode, and Figma-to-code workflows. NOT for React component logic, hooks, or state management (use react-development). NOT for Next.js routing, SSR, or server components (use nextjs-development).
license: MIT
---

# Frontend Design (UI/UX)

Comprehensive skill for creating beautiful, accessible, and performant user interfaces. This curated skill merges expertise from 11 specialized frontend/UI skills covering design systems, component libraries, CSS frameworks, accessibility patterns, and visual design principles.

## When to Use This Skill

Use this skill when:
- Building UI components with React, Vue, or Next.js
- Implementing design systems (shadcn/ui, Radix UI, fpkit)
- Styling with Tailwind CSS, CSS Modules, or CSS-in-JS
- Creating responsive, mobile-first layouts
- Implementing dark mode and theme customization
- Building accessible components (WCAG 2.2 compliance)
- Generating design tokens from Figma
- Creating component libraries with TypeScript
- Rapid prototyping with immediate visual feedback
- Evaluating and improving UI quality with Playwright
- A/B testing UI variations

---

## Quick Start Decision Tree

```
User Request -> What is the goal?
    |
    +-- Creating new UI component?
    |   +-- Simple component -> Quick Start: Component Creation
    |   +-- Full page/app -> Workflow 1: Full UI Creation
    |   +-- shadcn/ui component -> Use shadcn_add.py script
    |   +-- fpkit component -> Use scaffold_component.py script
    |
    +-- Styling existing UI?
    |   +-- Tailwind CSS -> Load references/tailwind-utilities.md
    |   +-- CSS Variables -> Load references/css-variables.md
    |   +-- Theme customization -> Load references/shadcn-theming.md
    |
    +-- Design system work?
    |   +-- Design tokens from Figma -> Use extract_tokens.py, transform_tokens.py
    |   +-- Token validation -> Use validate_tokens.py
    |   +-- Component library setup -> Load references/component-patterns.md
    |
    +-- Accessibility concerns?
    |   +-- WCAG compliance -> Load references/accessibility-guidelines.md
    |   +-- Audit existing UI -> Use audit_accessibility.sh
    |   +-- Accessible patterns -> Load references/accessibility-patterns.md
    |
    +-- Evaluating/Testing UI?
    |   +-- Quality evaluation -> Use evaluate-ui.ts
    |   +-- A/B comparison -> Use compare-variations.ts
    |   +-- CSS validation -> Use validate_css_vars.py
    |
    +-- Performance optimization?
        +-- Load references/PERFORMANCE_OPTIMIZATION.md
        +-- Core Web Vitals guidance
```

---

## Core Stack Architecture

### The Three Pillars

**Layer 1: TailwindCSS (Styling Foundation)**
- Utility-first CSS framework with build-time generation
- Zero runtime overhead, minimal production bundles
- Design tokens: colors, spacing, typography, breakpoints
- Responsive utilities and dark mode support

**Layer 2: Radix UI (Behavior & Accessibility)**
- Unstyled, accessible component primitives
- WAI-ARIA compliant with keyboard navigation
- Focus management and screen reader support
- Unopinionated - full styling control

**Layer 3: shadcn/ui (Beautiful Components)**
- Pre-built components = Radix primitives + Tailwind styling
- Copy-paste distribution (you own the code)
- Built-in React Hook Form + Zod validation
- Customizable variants with type safety

**Key Principle:** Each layer enhances the one below. Start with Tailwind for styling, add Radix for accessible behavior, use shadcn/ui for complete components.

---

## Quick Start: Component Setup

### shadcn/ui + Tailwind Setup

```bash
# Initialize shadcn/ui (includes Tailwind)
npx shadcn@latest init

# Add components
npx shadcn@latest add button card dialog form

# Or use the automation script
python scripts/shadcn_add.py button card dialog
```

### Basic Component Example

```tsx
import { Button } from "@/components/ui/button"
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card"

export function Dashboard() {
  return (
    <div className="container mx-auto p-6 grid gap-6 md:grid-cols-2 lg:grid-cols-3">
      <Card className="hover:shadow-lg transition-shadow">
        <CardHeader>
          <CardTitle className="text-2xl font-bold">Analytics</CardTitle>
        </CardHeader>
        <CardContent className="space-y-4">
          <p className="text-muted-foreground">View your metrics</p>
          <Button variant="default" className="w-full">
            View Details
          </Button>
        </CardContent>
      </Card>
    </div>
  )
}
```

---

## Design Token System

### Three-Tier Token Architecture

```css
:root {
  /* Tier 1: Primitives (immutable) */
  --gray-50: 250 250 250;
  --gray-900: 24 24 27;
  --blue-500: oklch(0.55 0.22 264);

  /* Tier 2: Semantics (theme-aware) */
  --background: var(--gray-50);
  --foreground: var(--gray-900);
  --primary: var(--blue-500);

  /* Tier 3: Components */
  --button-height: 2.5rem;
  --card-padding: 1.5rem;
}

.dark {
  /* Only semantic tokens change */
  --background: var(--gray-900);
  --foreground: var(--gray-50);
}
```

### Figma to Code Workflow

```bash
python scripts/extract_tokens.py --file-key YOUR_FIGMA_KEY
python scripts/transform_tokens.py tokens.json --format css
python scripts/validate_tokens.py tokens.json
```

**Load references:** `references/DESIGN_TOKENS.md`, `references/token-naming-conventions.md`

---

## Accessibility Standards

### WCAG 2.2 Contrast Requirements

| Level | Normal Text | Large Text | UI Components |
|-------|-------------|------------|---------------|
| AA (Required) | 4.5:1 | 3:1 | 3:1 |
| AAA (Enhanced) | 7:1 | 4.5:1 | 4.5:1 |

### Accessibility Checklist

- [ ] Semantic HTML (`<button>`, `<nav>`, `<main>`, `<article>`)
- [ ] All interactive elements keyboard accessible
- [ ] Proper ARIA attributes (`aria-label`, `aria-describedby`)
- [ ] Visible focus indicators
- [ ] Color contrast meets WCAG AA (4.5:1 for text)
- [ ] Screen reader friendly labels
- [ ] No keyboard traps
- [ ] Skip links for navigation

### Radix UI Built-In Guarantees
- ARIA attributes applied correctly
- Keyboard navigation functional
- Focus management and trapping automatic
- Screen reader compatible

**Load references:** `references/accessibility-guidelines.md`, `references/accessibility-patterns.md`

---

## Best Practices Summary

### Do
- Use semantic HTML elements
- Follow mobile-first responsive design
- Maintain WCAG AA compliance (4.5:1 contrast)
- Use design tokens consistently
- Compose components from primitives
- Test with keyboard navigation
- Validate CSS variables before commit
- Use TypeScript for type safety

### Don't
- Use px units (use rem)
- Skip accessibility testing
- Override Radix UI ARIA attributes
- Use dynamic Tailwind class names
- Nest interactive elements (`<button>` in `<a>`)
- Over-compose (keep depth <= 3 levels)
- Ignore Core Web Vitals
- Use hardcoded colors/spacing

## Anti-Patterns

- **Copy-pasting entire component libraries without understanding** — shadcn/ui is copy-paste by design, but you must understand what you copy; blindly adding 30 components bloats your bundle
- **Overriding Radix ARIA attributes** — Radix provides correct accessibility out of the box; overriding `role` or `aria-*` attributes usually makes things worse, not better
- **Dynamic Tailwind class construction** — `className={\`text-${color}-${shade}\`}` does not work because Tailwind purges unreferenced classes; use `className={variants[color]}` with safelist instead
- **Using px instead of rem** — px does not scale with user font-size preferences; rem respects browser zoom and accessibility settings
- **Skipping focus indicators for aesthetics** — visible focus is a WCAG requirement; style it with `focus-visible:` instead of removing it
- **Nested interactive elements** — `<button>` inside `<a>` or vice versa creates ambiguous activation targets and violates HTML spec
- **Theme tokens that only change colors** — a proper dark mode also adjusts shadows, borders, and opacity; only swapping colors creates jarring, inconsistent dark mode

See [Extended Patterns](references/extended-patterns.md) for detailed component examples, styling patterns, file organization, scripts reference, and reference quick guide.

---

## External Resources

- **TailwindCSS:** https://tailwindcss.com/docs
- **Radix UI:** https://www.radix-ui.com/primitives
- **shadcn/ui:** https://ui.shadcn.com | https://ui.shadcn.com/llms.txt
- **WCAG Guidelines:** https://www.w3.org/WAI/WCAG22/quickref/
- **OKLCH Color Space:** https://evilmartians.com/chronicles/oklch-in-css-why-quit-rgb-hsl
- **WebAIM Contrast Checker:** https://webaim.org/resources/contrastchecker/

---

**Skill Version:** 1.0.0
**Last Updated:** 2025-01-18
**Source Skills:** 11 merged
**Total Resources:** 107 files
