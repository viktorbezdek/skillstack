# Frontend Design - Extended Patterns & Examples

Detailed code examples, component patterns, and styling references extracted from the core skill.

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
