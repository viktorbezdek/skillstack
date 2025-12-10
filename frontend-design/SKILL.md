---
name: frontend-design
description: Comprehensive Frontend Design (UI/UX) skill combining UI design systems, component libraries, CSS/Tailwind styling, accessibility patterns, and visual design. Use when building user interfaces, implementing design systems, creating responsive layouts, adding accessible components (dialogs, dropdowns, forms, tables), customizing themes and colors, implementing dark mode, building component libraries with React/Vue, or establishing consistent styling patterns. Covers TailwindCSS, shadcn/ui, Radix UI, fpkit, Figma design tokens, and modern React patterns.
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

### Architecture Hierarchy

```
Application Layer
    |
shadcn/ui Components (Beautiful defaults, ready-to-use)
    |
Radix UI Primitives (Accessible behavior, unstyled)
    |
TailwindCSS Utilities (Design system, styling)
```

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

### fpkit Component Scaffolding

```bash
# Analyze component for reuse opportunities
python scripts/recommend_approach.py ComponentName

# Scaffold new component
python scripts/scaffold_component.py AlertBox --path ./components/alert-box

# Scaffold composed component
python scripts/scaffold_component.py StatusButton \
  --mode compose \
  --uses Badge,Button \
  --path ./components/status-button

# Validate CSS variables
python scripts/validate_css_vars.py ./components/alert-box/alert-box.scss
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
# Extract tokens from Figma (requires Figma MCP)
python scripts/extract_tokens.py --file-key YOUR_FIGMA_KEY

# Transform to various formats
python scripts/transform_tokens.py tokens.json --format css
python scripts/transform_tokens.py tokens.json --format scss
python scripts/transform_tokens.py tokens.json --format typescript

# Validate tokens
python scripts/validate_tokens.py tokens.json
```

**Load references:**
- `references/DESIGN_TOKENS.md` - Complete three-tier token system
- `references/token-naming-conventions.md` - Naming standards
- `references/w3c-dtcg-spec.md` - W3C Design Token specification

---

## Styling Patterns

### Tailwind CSS Quick Reference

**Layout:**
```html
<!-- Flexbox -->
<div class="flex items-center justify-between gap-4">

<!-- Grid -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">

<!-- Container -->
<div class="container mx-auto px-4 py-8">
```

**Responsive Design (Mobile-First):**
```html
<!-- Base (mobile) -> sm (640px) -> md (768px) -> lg (1024px) -> xl (1280px) -->
<div class="text-sm md:text-base lg:text-lg">
<div class="grid-cols-1 md:grid-cols-2 lg:grid-cols-3">
<div class="p-4 md:p-6 lg:p-8">
```

**Dark Mode:**
```html
<div class="bg-white dark:bg-gray-900">
<p class="text-gray-900 dark:text-white">
<button class="bg-blue-600 dark:bg-blue-500">
```

**Load references:**
- `references/tailwind-utilities.md` - Complete utility reference
- `references/tailwind-responsive.md` - Responsive patterns
- `references/tailwind-customization.md` - Config and extensions

### CSS Variables for Components

```scss
// fpkit naming pattern: --{component}-{property}
.alert-box {
  padding: var(--alert-padding, 1rem);
  border-radius: var(--alert-radius, 0.375rem);
  background: var(--alert-bg, white);

  // Variants
  &[data-variant="error"] {
    --alert-bg: var(--color-error-50);
    --alert-border: var(--color-error-500);
  }

  // States
  &:hover {
    --alert-bg: var(--alert-hover-bg);
  }
}
```

**Load references:**
- `references/css-variable-guide.md` - Naming conventions
- `references/css-variables.md` - Variable patterns

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

**Load references:**
- `references/accessibility-guidelines.md` - Complete WCAG guide
- `references/accessibility-patterns.md` - Component patterns
- `references/accessibility_checklist.md` - Audit checklist
- `references/shadcn-accessibility.md` - shadcn/ui patterns

---

## Component Patterns

### Modern React Component Structure

```typescript
import React, { useState, useCallback } from 'react';
import { useSuspenseQuery } from '@tanstack/react-query';
import type { FeatureData } from '~/types/feature';

interface MyComponentProps {
  id: number;
  onAction?: () => void;
}

export const MyComponent: React.FC<MyComponentProps> = ({ id, onAction }) => {
  const [state, setState] = useState<string>('');

  const { data } = useSuspenseQuery({
    queryKey: ['feature', id],
    queryFn: () => featureApi.getFeature(id),
  });

  const handleAction = useCallback(() => {
    setState('updated');
    onAction?.();
  }, [onAction]);

  return (
    <div className="p-4">
      {/* Content */}
    </div>
  );
};

export default MyComponent;
```

### Component Composition Patterns

**Pattern 1: Container + Content**
```tsx
import { Button, Badge } from '@fpkit/acss'

export const StatusButton = ({ status, children, ...props }) => (
  <Button {...props}>
    {children}
    <Badge variant={status}>{status}</Badge>
  </Button>
)
```

**Pattern 2: Extended Component**
```tsx
import { Button, type ButtonProps } from '@fpkit/acss'

interface LoadingButtonProps extends ButtonProps {
  loading?: boolean;
  onClickAsync?: (e: React.MouseEvent) => Promise<void>;
}

export const LoadingButton = ({ loading, onClickAsync, children, ...props }) => {
  const [isLoading, setIsLoading] = useState(loading);

  const handleClick = async (e) => {
    if (onClickAsync) {
      setIsLoading(true);
      try {
        await onClickAsync(e);
      } finally {
        setIsLoading(false);
      }
    }
  };

  return (
    <Button {...props} disabled={isLoading || props.disabled} onClick={handleClick}>
      {isLoading ? 'Loading...' : children}
    </Button>
  );
};
```

**Load references:**
- `references/component-patterns.md` - Complete patterns guide
- `references/composition-patterns.md` - Composition strategies
- `references/form-patterns.md` - Form component patterns

---

## UI Evaluation & Testing

### Automated UI Evaluation

```bash
# Comprehensive evaluation
npx tsx scripts/evaluate-ui.ts http://localhost:3000/page \
  --a11y \
  --performance \
  --screenshot \
  --threshold 85

# A/B comparison
npx tsx scripts/compare-variations.ts \
  http://localhost:3000?variant=a \
  http://localhost:3000?variant=b \
  --labels "Traditional,Modern"

# CSS variable validation
python scripts/validate_css_vars.py ./components/
```

### Performance Targets (Core Web Vitals)

| Metric | Good | Needs Improvement | Poor |
|--------|------|-------------------|------|
| LCP (Largest Contentful Paint) | < 2.5s | 2.5s - 4s | > 4s |
| FID (First Input Delay) | < 100ms | 100ms - 300ms | > 300ms |
| CLS (Cumulative Layout Shift) | < 0.1 | 0.1 - 0.25 | > 0.25 |

**Load references:**
- `references/playwright-evaluation.md` - Evaluation patterns
- `references/PERFORMANCE_OPTIMIZATION.md` - Performance guide

---

## File Organization

### Feature-Based Structure (Next.js)

```
app/
  {feature-name}/
    components/    # Feature-specific components
    hooks/         # Custom hooks
    api/           # API service layer
    lib/           # Utilities
    types/         # TypeScript types
    page.tsx       # Page component
    layout.tsx     # Layout (optional)

components/
  ui/              # shadcn/ui components
  shared/          # Truly reusable components

lib/
  utils.ts         # cn() helper, etc.
```

### Component Library Structure

```
packages/
  component-library/
    src/
      components/
        button/
          button.tsx
          button.types.ts
          button.scss
          button.stories.tsx
          button.test.tsx
      index.ts      # Public exports
    package.json
```

---

## Scripts Reference

### Component Generation
- `scripts/scaffold_component.py` - Generate fpkit component structure
- `scripts/init-component.ts` - Generate React/Vue component with tests
- `scripts/generate_component.sh` - Shell-based component generator
- `scripts/generate-component.py` - Python component generator

### Design Tokens
- `scripts/extract_tokens.py` - Extract tokens from Figma
- `scripts/transform_tokens.py` - Transform to CSS/SCSS/TS
- `scripts/validate_tokens.py` - Validate token structure
- `scripts/design_token_generator.py` - Generate token files

### Styling & Validation
- `scripts/validate_css_vars.py` - Validate CSS variable naming
- `scripts/tailwind_config_gen.py` - Generate Tailwind config
- `scripts/analyze_styles.py` - Analyze CSS patterns
- `scripts/validate_consistency.py` - Check style consistency

### UI Evaluation
- `scripts/evaluate-ui.ts` - Playwright-based UI evaluation
- `scripts/compare-variations.ts` - A/B testing comparison
- `scripts/audit_accessibility.sh` - Accessibility audit

### Component Analysis
- `scripts/recommend_approach.py` - Suggest compose/extend/create
- `scripts/analyze_components.py` - Scan component library
- `scripts/suggest_reuse.py` - Find reusable components
- `scripts/add_to_exports.py` - Add exports to index.ts

---

## References Quick Guide

### Core Concepts
| Reference | Use When |
|-----------|----------|
| `DESIGN_TOKENS.md` | Setting up design token system |
| `ui-design-principles.md` | Making design decisions |
| `accessibility-guidelines.md` | Ensuring WCAG compliance |
| `RESPONSIVE_PATTERNS.md` | Building responsive layouts |
| `PERFORMANCE_OPTIMIZATION.md` | Optimizing performance |

### Component Libraries
| Reference | Use When |
|-----------|----------|
| `SHADCN_REFERENCE.md` | Using shadcn/ui components |
| `RADIX_REFERENCE.md` | Using Radix primitives |
| `component-patterns.md` | Designing component APIs |
| `composition-patterns.md` | Composing components |
| `form-patterns.md` | Building forms |

### Styling
| Reference | Use When |
|-----------|----------|
| `tailwind-utilities.md` | Tailwind class reference |
| `tailwind-responsive.md` | Responsive design |
| `tailwind-customization.md` | Customizing Tailwind |
| `css-variable-guide.md` | CSS variable naming |
| `shadcn-theming.md` | Theme customization |

### Testing & Quality
| Reference | Use When |
|-----------|----------|
| `playwright-evaluation.md` | UI evaluation patterns |
| `testing-patterns.md` | Component testing |
| `storybook-patterns.md` | Documenting components |
| `anti-patterns.md` | Avoiding common mistakes |

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
- Document with Storybook stories
- Evaluate with Playwright automation

### Don't
- Use px units (use rem)
- Skip accessibility testing
- Override Radix UI ARIA attributes
- Use dynamic Tailwind class names
- Nest interactive elements (`<button>` in `<a>`)
- Over-compose (keep depth <= 3 levels)
- Ignore Core Web Vitals
- Create components without tests
- Use hardcoded colors/spacing
- Duplicate existing components

---

## Assets & Templates

### Component Templates
- `assets/component-templates/Button.tsx` - Accessible button
- `assets/component-templates/Input.tsx` - Form input
- `assets/templates/component.template.tsx` - Base template
- `assets/templates/component.composed.template.tsx` - Composition template
- `assets/templates/component.extended.template.tsx` - Extension template

### Design Token Templates
- `templates/css-variables.template.css` - CSS output
- `templates/scss-variables.template.scss` - SCSS output
- `templates/typescript-types.template.ts` - TypeScript types
- `templates/w3c-tokens.template.json` - W3C DTCG format
- `assets/design-tokens.json` - Sample tokens
- `assets/design-tokens/tokens.json` - Complete token set

---

## Source Skills

This curated skill combines knowledge from:

1. **Frontend Development Guidelines (Next.js + Tailwind)** - Modern React patterns
2. **UI/UX Design & Development Expert** - TailwindCSS + Radix + shadcn/ui
3. **UI Styling Skill** - shadcn/ui + Tailwind + Canvas design
4. **UI Creator** - UI creation with Playwright evaluation
5. **Frontend Designer** - Design system setup
6. **Style Master: CSS Expert** - CSS analysis and validation
7. **UI Design System** - Design token generation
8. **Figma Design Tokens Generator** - Figma to code workflow
9. **Component Library (shadcn/ui Architecture)** - Component patterns
10. **fpkit Component Builder** - React component library patterns
11. **FPKit Developer** - Application development with fpkit

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






