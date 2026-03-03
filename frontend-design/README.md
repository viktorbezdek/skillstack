# Frontend Design

> Comprehensive Frontend Design (UI/UX) skill combining design systems, component libraries, CSS/Tailwind styling, accessibility patterns, and visual design for beautiful, accessible, and performant user interfaces.

## Overview

Building modern frontend interfaces requires expertise across multiple domains: design systems, component architecture, CSS frameworks, accessibility compliance, responsive design, and performance optimization. This skill consolidates knowledge from 11 specialized frontend/UI skills into a single comprehensive resource, covering the full stack from design tokens to production deployment.

The Frontend Design skill is for developers and designers building user interfaces with React, Vue, or Next.js. It provides the three-pillar architecture (TailwindCSS for styling, Radix UI for accessible behavior, shadcn/ui for pre-built components) along with scripts for token extraction, component scaffolding, accessibility auditing, and UI quality evaluation. Whether you are initializing a new design system, adding accessible components, or optimizing Core Web Vitals, this skill has the references and tooling you need.

As part of the SkillStack collection, this skill draws on example-design for component documentation, edge-case-coverage for form validation patterns, and integrates with debugging for visual regression testing with Playwright. Its 107 total resource files make it the largest skill in the collection.

## What's Included

### References

- `references/TAILWIND_REFERENCE.md` - Complete TailwindCSS utility reference
- `references/tailwind-utilities.md` - Tailwind utility class quick reference
- `references/tailwind-customization.md` - Extending and customizing Tailwind configuration
- `references/tailwind-responsive.md` - Responsive design patterns with Tailwind
- `references/RADIX_REFERENCE.md` - Radix UI primitives reference
- `references/SHADCN_REFERENCE.md` - shadcn/ui component reference
- `references/shadcn-components.md` - shadcn/ui component catalog and usage
- `references/shadcn-theming.md` - shadcn/ui theming and customization
- `references/shadcn-accessibility.md` - Accessibility features in shadcn/ui components
- `references/DESIGN_TOKENS.md` - Design token system architecture and usage
- `references/token-naming-conventions.md` - Token naming conventions and standards
- `references/frontend-design_tokens.md` - Frontend-specific design token patterns
- `references/w3c-dtcg-spec.md` - W3C Design Token Community Group specification
- `references/css-variables.md` - CSS custom properties reference and patterns
- `references/css-variable-guide.md` - Guide to using CSS variables effectively
- `references/accessibility-guidelines.md` - WCAG 2.2 accessibility guidelines
- `references/accessibility-patterns.md` - Accessible component implementation patterns
- `references/accessibility.md` - Accessibility overview and checklist
- `references/accessibility_checklist.md` - Detailed accessibility audit checklist
- `references/component-patterns.md` - Component architecture patterns
- `references/component_library.md` - Component library setup and management
- `references/composition-patterns.md` - Component composition strategies
- `references/composition.md` - Composition design principles
- `references/ui-component-patterns.md` - UI-specific component patterns
- `references/fpkit-component-patterns.md` - fpkit component library patterns
- `references/common-patterns.md` - Frequently used frontend patterns
- `references/complete-examples.md` - End-to-end component examples
- `references/RESPONSIVE_PATTERNS.md` - Responsive design pattern reference
- `references/frontend-responsive_patterns.md` - Frontend-specific responsive patterns
- `references/PERFORMANCE_OPTIMIZATION.md` - Core Web Vitals and performance optimization
- `references/performance.md` - Performance best practices
- `references/CUSTOMIZATION.md` - Design system customization guide
- `references/INTEGRATION_PATTERNS.md` - Integration patterns between UI layers
- `references/integration-examples.md` - Concrete integration code examples
- `references/extended-patterns.md` - Advanced patterns, file organization, and scripts reference
- `references/architecture.md` - Frontend architecture principles
- `references/file-organization.md` - File and directory organization conventions
- `references/styling-guide.md` - Styling methodology and conventions
- `references/style-guide-template.md` - Style guide documentation template
- `references/typescript-standards.md` - TypeScript standards for UI components
- `references/ui-design-principles.md` - Core UI design principles
- `references/canvas-design-system.md` - Canvas-based design system reference
- `references/ui-canvas-design-system.md` - UI canvas design system patterns
- `references/animation-patterns.md` - Animation and transition patterns
- `references/anti-patterns.md` - Common frontend anti-patterns to avoid
- `references/form-patterns.md` - Form design and validation patterns
- `references/data-tables.md` - Data table component patterns
- `references/data-fetching.md` - Data fetching strategies for UI
- `references/loading-and-error-states.md` - Loading, error, and empty state patterns
- `references/routing-guide.md` - Client-side routing patterns
- `references/advanced-usage.md` - Advanced component usage patterns
- `references/storybook-patterns.md` - Storybook story patterns
- `references/storybook.md` - Storybook setup and configuration
- `references/testing-patterns.md` - Component testing patterns
- `references/testing-setup.md` - Test environment setup
- `references/testing.md` - Testing strategy overview
- `references/playwright-evaluation.md` - Playwright UI evaluation patterns
- `references/figma-mcp-tools.md` - Figma MCP integration tools
- `references/troubleshooting.md` - Common frontend issues and solutions

### Scripts

- `scripts/shadcn_add.py` - Automate adding shadcn/ui components
- `scripts/ui-styling-shadcn_add.py` - UI styling variant of shadcn component adder
- `scripts/scaffold_component.py` - Scaffold new fpkit components with full structure
- `scripts/generate-component.py` - Generate component files from templates
- `scripts/generate_component.sh` - Shell-based component generator
- `scripts/init-component.ts` - TypeScript component initializer
- `scripts/extract_tokens.py` - Extract design tokens from Figma files
- `scripts/transform_tokens.py` - Transform tokens to CSS, SCSS, or JSON format
- `scripts/validate_tokens.py` - Validate design token files for correctness
- `scripts/design_token_generator.py` - Generate design token files
- `scripts/design-token-generator.ts` - TypeScript design token generator
- `scripts/validate_css_vars.py` - Validate CSS custom property usage
- `scripts/fpkit-developer-validate_css_vars.py` - fpkit-specific CSS variable validator
- `scripts/audit_accessibility.sh` - Run accessibility audits on components
- `scripts/evaluate-ui.ts` - Evaluate UI quality with Playwright
- `scripts/compare-variations.ts` - A/B compare UI variations
- `scripts/analyze_components.py` - Analyze component structure and dependencies
- `scripts/analyze_styles.py` - Analyze style usage and redundancy
- `scripts/suggest_improvements.py` - Suggest UI improvement opportunities
- `scripts/suggest_reuse.py` - Identify component reuse opportunities
- `scripts/recommend_approach.py` - Recommend frontend approach for requirements
- `scripts/validate_consistency.py` - Validate design consistency across components
- `scripts/add_to_exports.py` - Add new components to barrel exports
- `scripts/setup_design_system.sh` - Initialize a new design system project
- `scripts/setup-tailwind.py` - Set up Tailwind CSS configuration
- `scripts/tailwind_config_gen.py` - Generate Tailwind config from design tokens
- `scripts/ui-styling-tailwind_config_gen.py` - UI styling Tailwind config generator
- `scripts/generate_styleguide.py` - Generate style guide documentation
- `scripts/sync-docs.sh` - Sync component documentation
- `scripts/utils.py` - Shared utility functions

### Templates

- `templates/css-variables.template.css` - CSS custom properties template
- `templates/scss-variables.template.scss` - SCSS variables template
- `templates/typescript-types.template.ts` - TypeScript type definitions template
- `templates/documentation.template.md` - Component documentation template
- `templates/w3c-tokens.template.json` - W3C DTCG token format template

### Assets

- `assets/design-tokens/tokens.json` - Sample design token definitions
- `assets/design-tokens.json` - Design tokens in flat format
- `assets/component-templates/Button.tsx` - Button component template
- `assets/component-templates/Input.tsx` - Input component template
- `assets/component-templates/README.md` - Component templates documentation
- `assets/templates/component.template.tsx` - Base component template
- `assets/templates/component.composed.template.tsx` - Composed component template
- `assets/templates/component.extended.template.tsx` - Extended component template
- `assets/templates/component.template.scss` - Component SCSS template
- `assets/templates/component.template.stories.tsx` - Storybook stories template
- `assets/templates/component.template.test.tsx` - Component test template
- `assets/templates/component.template.types.ts` - Component types template

## Key Features

- Three-pillar architecture: TailwindCSS (styling) + Radix UI (behavior/a11y) + shadcn/ui (pre-built components)
- Three-tier design token system (primitives, semantics, components) with Figma-to-code workflow
- WCAG 2.2 accessibility compliance with automated auditing and accessible component patterns
- 57+ reference files covering every frontend concern from animation to routing to testing
- 30+ automation scripts for component scaffolding, token management, accessibility auditing, and UI evaluation
- Playwright-based UI quality evaluation and A/B variation comparison
- Responsive design patterns with mobile-first approach and dark mode support
- Component library scaffolding for fpkit and shadcn/ui with TypeScript type safety
- Performance optimization guidance targeting Core Web Vitals

## Usage Examples

**Create a new UI component:**
```
Build an accessible dropdown menu component with Radix UI and Tailwind styling.
```
Uses Radix UI primitives for keyboard navigation and ARIA compliance, applies Tailwind utilities for styling, and generates the component with proper TypeScript types following the component patterns reference.

**Set up a design system from Figma:**
```
Extract design tokens from our Figma file and set up the token pipeline.
```
Runs extract_tokens.py to pull tokens from Figma, transform_tokens.py to generate CSS/SCSS/JSON output, and validate_tokens.py to verify correctness, following the three-tier token architecture.

**Add shadcn/ui components:**
```
Add a form with validation using shadcn/ui, React Hook Form, and Zod.
```
Uses shadcn_add.py to install form components, then builds the form following form-patterns.md with proper validation, error states, and accessibility attributes.

**Audit accessibility:**
```
Run an accessibility audit on our component library.
```
Executes audit_accessibility.sh to check WCAG 2.2 compliance, identifies contrast ratio failures, missing ARIA labels, keyboard navigation gaps, and generates a prioritized fix list.

**Evaluate UI quality:**
```
Evaluate the visual quality of our dashboard page and suggest improvements.
```
Runs evaluate-ui.ts with Playwright to capture and analyze the page, scoring layout consistency, spacing, typography, and color usage, then provides specific improvement recommendations.

## Quick Start

1. **Initialize shadcn/ui with Tailwind**:
   ```bash
   npx shadcn@latest init
   npx shadcn@latest add button card dialog form
   ```

2. **Or use the automation script**:
   ```bash
   python scripts/shadcn_add.py button card dialog form
   ```

3. **Extract design tokens from Figma** (if using a design system):
   ```bash
   python scripts/extract_tokens.py --file-key YOUR_FIGMA_KEY
   python scripts/transform_tokens.py tokens.json --format css
   ```

4. **Scaffold a new component**:
   ```bash
   python scripts/scaffold_component.py MyComponent
   ```

5. **Run an accessibility audit**:
   ```bash
   ./scripts/audit_accessibility.sh
   ```

6. **Consult the decision tree** in SKILL.md to find the right reference for your specific task.

## Related Skills

- **example-design** -- Create effective code examples for component documentation and storybook stories
- **edge-case-coverage** -- Handle form validation edge cases, error states, and boundary conditions
- **debugging** -- Debug UI issues with Chrome DevTools and Playwright visual regression testing
- **documentation-generator** -- Generate component library documentation and style guides
- **docker-containerization** -- Containerize frontend build pipelines

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) — `/plugin install frontend-design@skillstack` — 46 production-grade plugins for Claude Code.
