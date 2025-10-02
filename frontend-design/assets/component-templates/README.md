# Component Templates

Production-ready React component templates with accessibility, TypeScript, and best practices built-in.

## Available Templates

### Button.tsx
Full-featured button component with:
- Multiple variants (primary, secondary, ghost, danger)
- Size options (sm, md, lg)
- Loading state with spinner
- Icon support (left or right position)
- Full accessibility (keyboard, focus management, ARIA)

### Input.tsx
Accessible form input with:
- Required label association
- Error state with aria-invalid
- Helper text support
- Size variants
- Required field indicators

## Usage

These templates are meant to be copied and customized for your specific needs.

```bash
# Copy a template to your project
cp Button.tsx /path/to/your/components/

# Or use the init-component.ts script
npx tsx scripts/init-component.ts button --type button
```

## Customization

Each template includes:
- TypeScript interfaces for props
- Accessibility features (ARIA attributes, semantic HTML)
- Tailwind CSS styling (can be adapted to other styling solutions)
- JSDoc comments
- Sensible defaults

Feel free to modify:
- Styling (colors, sizes, spacing)
- Variants and options
- Additional features
- State management approach

## Best Practices

These templates follow:
- WCAG 2.2 Level AA accessibility standards
- React best practices (hooks, composition)
- TypeScript strict mode
- Semantic HTML
- Keyboard navigation support
- Focus management

## Design Tokens

Components use design tokens from `../design-tokens.json`. Update that file to maintain consistency across your design system.
