# Styling Guide

Modern styling patterns for using Tailwind CSS with Next.js and responsive design.

---

## Tailwind CSS Basics

### Inline Utility Classes

Tailwind uses utility-first CSS with inline classes. No need for separate style files unless component is complex.

```typescript
// Simple component with Tailwind classes
export const Button = ({ children, variant = 'primary' }) => {
    return (
        <button
            className={clsx(
                'px-4 py-2 rounded-md font-semibold transition-colors',
                variant === 'primary' && 'bg-blue-600 text-white hover:bg-blue-700',
                variant === 'secondary' && 'bg-gray-200 text-gray-900 hover:bg-gray-300',
            )}
        >
            {children}
        </button>
    );
};
```

### When to Use Custom CSS

**For reusable styles or complex animations:**

Create a CSS file alongside the component:

```typescript
// MyComponent.tsx
import styles from './MyComponent.module.css';

export const MyComponent = () => {
    return <div className={styles.container}>Content</div>;
};
```

```css
/* MyComponent.module.css */
.container {
    @apply flex flex-col gap-4;
    animation: slideIn 0.3s ease-out;
}

@keyframes slideIn {
    from {
        opacity: 0;
        transform: translateY(-10px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
```

---

## Responsive Design with Tailwind

### Breakpoint Prefixes

```typescript
<div className="w-full md:w-1/2 lg:w-1/3">
    Responsive Width
</div>
```

**Tailwind Breakpoints (in ChoreQuest):**
- `sm`: 640px
- `md`: 768px
- `lg`: 1024px
- `xl`: 1280px
- `2xl`: 1536px

### Mobile-First Approach

Always start with mobile styles, then add larger breakpoints:

```typescript
// ✅ CORRECT - Mobile first
<div className="flex flex-col gap-2 md:flex-row md:gap-4">
    <div className="w-full md:w-1/2">Column 1</div>
    <div className="w-full md:w-1/2">Column 2</div>
</div>

// ❌ WRONG - Desktop first
<div className="flex flex-row gap-4 md:flex-col md:gap-2">
    {/* Harder to maintain */}
</div>
```

### Common Responsive Patterns

**Text Sizing:**
```typescript
<h1 className="text-4xl sm:text-5xl md:text-6xl font-bold">
    Responsive Heading
</h1>
```

**Grid Layouts:**
```typescript
<div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
    {/* Auto-responsive grid */}
</div>
```

**Container Padding:**
```typescript
<div className="px-4 sm:px-6 md:px-8 lg:px-12">
    {/* Responsive padding */}
</div>
```

---

## Using clsx for Conditional Classes

ChoreQuest uses `clsx` to manage conditional Tailwind classes:

```typescript
import clsx from 'clsx';

export const Badge = ({ variant, children }) => {
    return (
        <span
            className={clsx(
                'px-2 py-1 rounded text-sm font-medium',
                {
                    'bg-green-100 text-green-800': variant === 'success',
                    'bg-red-100 text-red-800': variant === 'error',
                    'bg-blue-100 text-blue-800': variant === 'info',
                    'bg-yellow-100 text-yellow-800': variant === 'warning',
                }
            )}
        >
            {children}
        </span>
    );
};
```

---

## Color System & Variables

### Using CSS Variables (if defined)

Check `globals.css` for CSS custom properties:

```typescript
<div className="bg-primary text-primary-foreground">
    Uses CSS variables
</div>
```

### Or Use Tailwind Color Names

```typescript
<div className="bg-slate-100 text-slate-900">
    Standard Tailwind Colors
</div>
```

---

## Flexbox & Layout

### Flex Patterns

```typescript
// Row layout with spacing
<div className="flex flex-row items-center gap-4">
    <div>Item 1</div>
    <div>Item 2</div>
</div>

// Column layout
<div className="flex flex-col gap-2">
    <div>Item 1</div>
    <div>Item 2</div>
</div>

// Space between (justify-content: space-between)
<div className="flex justify-between items-center">
    <span>Left</span>
    <span>Right</span>
</div>

// Centered
<div className="flex items-center justify-center">
    Centered content
</div>
```

### Grid Layout

```typescript
// Responsive grid
<div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
    {items.map(item => <div key={item}>{item}</div>)}
</div>

// Fixed 12-column grid
<div className="grid grid-cols-12 gap-4">
    <div className="col-span-6 md:col-span-8">Main</div>
    <div className="col-span-6 md:col-span-4">Sidebar</div>
</div>
```

---

## Spacing

### Padding & Margin

```typescript
// Padding (all sides)
p-2   // padding: 0.5rem (8px)
p-4   // padding: 1rem (16px)

// Padding specific sides
px-4  // padding-left & padding-right
py-2  // padding-top & padding-bottom
pt-4  // padding-top
pr-2  // padding-right

// Margin (same pattern)
m-4, mx-4, my-2, mt-1, etc.

// Gap (flex/grid spacing)
gap-2, gap-x-4, gap-y-1
```

**Unit Reference:** 1 unit = 0.25rem = 4px

---

## Hover, Focus, and State Styles

### Basic State Modifiers

```typescript
<button className="bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 active:bg-blue-800 disabled:opacity-50 disabled:cursor-not-allowed">
    Interactive Button
</button>
```

**Common modifiers:**
- `hover:` - On mouse over
- `focus:` - When focused
- `active:` - When pressed
- `disabled:` - When disabled
- `group-hover:` - When parent hovered

### Dark Mode (if using)

```typescript
<div className="bg-white dark:bg-slate-900 text-slate-900 dark:text-white">
    Adapts to dark mode
</div>
```

---

## Typography

### Text Sizing

```typescript
// Text size (from xs to 9xl)
text-xs    // 12px
text-sm    // 14px
text-base  // 16px
text-lg    // 18px
text-xl    // 20px
text-2xl   // 24px
text-3xl   // 30px
text-4xl   // 36px
```

### Font Weight & Style

```typescript
<p className="font-light">Light</p>
<p className="font-normal">Normal</p>
<p className="font-semibold">Semibold</p>
<p className="font-bold">Bold</p>

<p className="italic">Italic</p>
<p className="underline">Underlined</p>
<p className="line-through">Strikethrough</p>
```

### Line Height

```typescript
<p className="leading-tight">Tight spacing</p>
<p className="leading-normal">Normal spacing</p>
<p className="leading-relaxed">Relaxed spacing</p>
<p className="leading-loose">Loose spacing</p>
```

---

## Borders & Shadows

### Border Styles

```typescript
<div className="border border-gray-300">
    Border
</div>

<div className="border-l-4 border-blue-500">
    Left border
</div>

<div className="border-2 border-dashed border-gray-400">
    Dashed border
</div>
```

### Border Radius

```typescript
rounded      // border-radius: 0.25rem
rounded-md   // border-radius: 0.375rem
rounded-lg   // border-radius: 0.5rem
rounded-full // border-radius: 9999px (circles)
```

### Shadows

```typescript
<div className="shadow">Small shadow</div>
<div className="shadow-md">Medium shadow</div>
<div className="shadow-lg">Large shadow</div>
<div className="shadow-xl">Extra large shadow</div>
<div className="shadow-2xl">2xl shadow</div>
```

---

## Code Style Standards

### Class Organization Order

Organize classes in this order for readability:

1. **Display & Layout** - `flex`, `grid`, `block`, `hidden`
2. **Width & Height** - `w-full`, `h-screen`, `min-h-[400px]`
3. **Padding & Margin** - `p-4`, `m-2`, `gap-4`
4. **Colors & Typography** - `text-white`, `bg-blue-600`, `font-bold`
5. **Borders & Shadows** - `border`, `rounded-lg`, `shadow-md`
6. **Responsive & State** - `md:w-1/2`, `hover:bg-blue-700`

```typescript
// ✅ GOOD - Organized classes
<div className="
    flex flex-col
    w-full h-screen
    p-4 gap-4
    bg-white text-gray-900
    border border-gray-200 rounded-lg shadow-md
    md:flex-row md:p-8
    hover:shadow-lg
">
    Content
</div>

// ❌ AVOID - Random order
<div className="hover:shadow-lg shadow-md md:p-8 p-4 text-gray-900 w-full flex rounded-lg gap-4 h-screen border-gray-200 flex-col bg-white border">
    Content
</div>
```

### Using clsx for Multi-line Classes

When classes are numerous, use clsx for clarity:

```typescript
export const Card = ({ variant, children }) => {
    return (
        <div
            className={clsx(
                'flex flex-col p-4 rounded-lg border shadow-md',
                'hover:shadow-lg transition-shadow',
                {
                    'bg-white text-gray-900': variant === 'light',
                    'bg-gray-900 text-white': variant === 'dark',
                    'bg-blue-50 border-blue-300': variant === 'highlight',
                }
            )}
        >
            {children}
        </div>
    );
};
```

---

## Arbitrary Values

When Tailwind doesn't have a value, use square brackets:

```typescript
// Custom width
<div className="w-[482px]">Custom width</div>

// Custom colors
<div className="bg-[#1f2937]">Custom color</div>

// Custom spacing
<div className="mt-[37px]">Custom margin</div>

// Custom sizes with calc
<div className="max-h-[calc(100vh-200px)]">Custom height</div>
```

---

## Performance Tips

1. **Avoid dynamic class names** - Always define classes statically
   ```typescript
   // ❌ AVOID
   className={`text-${color}`}

   // ✅ DO THIS
   const colorMap = { red: 'text-red-500', blue: 'text-blue-500' };
   className={colorMap[color]}
   ```

2. **Use PurgeCSS** - Tailwind automatically removes unused styles in production

3. **CSS Modules for complex styles** - Don't bloat JSX with dozens of classes

---

## Common Patterns in ChoreQuest

Check existing components for patterns:

- **Admin dashboard** - Responsive grid layouts
- **Quest cards** - Shadow & hover effects
- **Buttons** - Variant patterns with clsx
- **Forms** - Input styling with focus states
- **Navigation** - Responsive menu handling

---

## Summary

**Styling Checklist:**
- ✅ Use Tailwind utility classes
- ✅ Mobile-first responsive design (sm:, md:, lg:)
- ✅ Use clsx for conditional classes
- ✅ Organize classes logically
- ✅ Custom CSS modules for complex styles
- ✅ Avoid dynamic class generation
- ❌ No inline style objects (use Tailwind or CSS)
- ❌ No old CSS-in-JS approaches

**See Also:**
- [component-patterns.md](component-patterns.md) - Component structure
- [complete-examples.md](complete-examples.md) - Full component examples
