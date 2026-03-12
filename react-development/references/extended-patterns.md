# React Development - Extended Patterns & Examples

Detailed component patterns, hooks guidance, fpkit development, and audit criteria extracted from the core skill.

## fpkit Component Development

### Building fpkit Library Components

For developers building the @fpkit/acss library itself.

**Component Structure:**
```
src/components/
  component-name/
    component-name.tsx        # Component implementation
    component-name.types.ts   # TypeScript types
    component-name.scss       # Styles with CSS variables
    component-name.test.tsx   # Vitest tests
    component-name.stories.tsx # Storybook documentation
```

**CSS Variable Naming Convention:**
```scss
--{component}-{element}-{variant}-{property}-{modifier}

// Examples:
--btn-bg                      // Base button background
--btn-primary-bg              // Primary variant background
--btn-hover-bg                // Hover state background
--btn-focus-outline-offset    // Focus state modifier
```

**Approved Abbreviations:**
- `bg` - background
- `fs` - font-size
- `fw` - font-weight
- `radius` - border-radius
- `gap` - gap

**Full Words Required:**
- padding, padding-inline, padding-block
- margin, margin-inline, margin-block
- color, border, display, width, height

**Scripts:**
- `scripts/fpkit-builder-scaffold_component.py` - Scaffold new components
- `scripts/fpkit-builder-validate_css_vars.py` - Validate CSS variable naming
- `scripts/fpkit-builder-analyze_components.py` - Analyze component patterns
- `scripts/fpkit-builder-suggest_reuse.py` - Find reuse opportunities

**Reference Files:**
- `references/fpkit-builder-component-patterns.md`
- `references/fpkit-builder-composition-patterns.md`
- `references/fpkit-builder-css-variable-guide.md`
- `references/fpkit-builder-accessibility-patterns.md`
- `references/fpkit-builder-testing-patterns.md`
- `references/fpkit-builder-storybook-patterns.md`

### Using fpkit Components in Applications

**Composition Example:**
```tsx
import { Button, Badge } from '@fpkit/acss'

export interface StatusButtonProps extends React.ComponentProps<typeof Button> {
  status: 'active' | 'inactive' | 'pending'
}

export const StatusButton = ({ status, children, ...props }: StatusButtonProps) => {
  return (
    <Button {...props}>
      {children}
      <Badge variant={status}>{status}</Badge>
    </Button>
  )
}
```

**CSS Customization:**
```css
/* Global overrides */
:root {
  --btn-radius: 0.25rem;
  --btn-primary-bg: #0066cc;
}

/* Scoped overrides */
.custom-button {
  --btn-padding-inline: 2rem;
}
```

**Reference Files:**
- `references/fpkit-dev-composition.md`
- `references/fpkit-dev-css-variables.md`
- `references/fpkit-dev-accessibility.md`
- `references/fpkit-dev-architecture.md`
- `references/fpkit-dev-testing.md`
- `references/fpkit-dev-storybook.md`

---

## Bulletproof React Auditing

### Audit Categories

1. **Project Structure** - Feature-based organization
2. **Component Architecture** - Size limits, prop counts, composition
3. **State Management** - Appropriate tools for each state type
4. **API Layer** - Data fetching patterns
5. **Testing Strategy** - Test coverage and patterns
6. **Styling Patterns** - CSS organization
7. **Error Handling** - Error boundaries, recovery
8. **Performance** - Optimization patterns
9. **Security** - Best practices
10. **Standards Compliance** - Code quality

### Key Checks

**Component Size:**
- Components should be < 300 lines
- Props should be < 7-10

**State Management:**
- Use React Query/SWR for server state
- Use Zustand/Jotai for global state
- Keep state as local as possible

**Scripts:**
- `scripts/audit_engine.py` - Main audit orchestration
- `scripts/analyzers/` - Category-specific analyzers

**Reference Files:**
- `references/bulletproof-audit_criteria.md`
- `references/bulletproof-severity_matrix.md`

---

## React Hooks Anti-Patterns (Detailed)

### 1. Derived State with useState + useEffect
```tsx
// BAD
const [total, setTotal] = useState(0)
useEffect(() => {
  setTotal(items.reduce((sum, i) => sum + i.price, 0))
}, [items])

// GOOD - Calculate during render
const total = items.reduce((sum, i) => sum + i.price, 0)
```

### 2. useEffect for Event Response
```tsx
// BAD - Effect chain for user action
useEffect(() => {
  if (query) fetch(`/api/search?q=${query}`)
}, [query])

// GOOD - Handle in event handler
const handleSubmit = async () => {
  const results = await fetch(`/api/search?q=${query}`)
}
```

### 3. Props-to-State Sync
```tsx
// BAD - Sync props to state
const [content, setContent] = useState(initialContent)
useEffect(() => {
  setContent(initialContent)
}, [initialContent])

// GOOD - Use key for reset
// Parent: <Editor key={documentId} initialContent={doc.content} />
```

### 4. Premature Memoization
```tsx
// BAD - Unnecessary for cheap operations
const fullName = useMemo(
  () => `${firstName} ${lastName}`,
  [firstName, lastName]
)

// GOOD - Just calculate it
const fullName = `${firstName} ${lastName}`
```

### When to Use Memoization

Only use `useMemo`/`useCallback` when:
1. Expensive computation (O(n log n) or worse)
2. Callback passed to memoized child component
3. Value used in dependency array of other hooks

### Dependency Array Rules

1. **Include all reactive values** used inside the effect
2. **Use functional updates** to avoid state dependencies
3. **Use refs** for values that shouldn't trigger re-runs
4. **Never suppress ESLint warnings** - fix the underlying issue

---

## Templates

Component templates for rapid scaffolding:

- `templates/component.template.tsx` - Base component template
- `templates/component.template.types.ts` - TypeScript types template
- `templates/component.template.scss` - SCSS styles template
- `templates/component.template.test.tsx` - Vitest test template
- `templates/component.template.stories.tsx` - Storybook story template
- `templates/component.composed.template.tsx` - Composed component template
- `templates/component.extended.template.tsx` - Extended component template

---

## File Reference

### References (29 files)

**Next.js:** nextjs-architecture-patterns.md, nextjs-service-patterns.md, nextjs-hooks-patterns.md, nextjs-component-patterns.md, nextjs-page-patterns.md, nextjs-database-patterns.md, nextjs-permission-patterns.md, nextjs-typescript-patterns.md

**shadcn/ui:** shadcn-form-patterns.md, shadcn-data-tables.md, shadcn-animation-patterns.md, shadcn-testing-setup.md

**fpkit Builder:** fpkit-builder-component-patterns.md, fpkit-builder-composition-patterns.md, fpkit-builder-css-variable-guide.md, fpkit-builder-accessibility-patterns.md, fpkit-builder-testing-patterns.md, fpkit-builder-storybook-patterns.md

**fpkit Developer:** fpkit-dev-composition.md, fpkit-dev-css-variables.md, fpkit-dev-accessibility.md, fpkit-dev-architecture.md, fpkit-dev-testing.md, fpkit-dev-storybook.md

**Bulletproof React:** bulletproof-audit_criteria.md, bulletproof-severity_matrix.md

**Hooks:** hooks-unnecessary-hooks.md, hooks-custom-hooks.md, hooks-dependency-array.md

### Scripts (18+ files)

- audit_engine.py + analyzers/
- fpkit-builder-*.py (6 scripts)
- fpkit-dev-*.py/.sh (2 scripts)
- shadcn-*.py (2 scripts)
- hooks-analyze-hooks-usage.mjs

### Examples (3 files)

- hooks-good-patterns.tsx
- hooks-anti-patterns.tsx
- bulletproof-sample_audit_report.md
