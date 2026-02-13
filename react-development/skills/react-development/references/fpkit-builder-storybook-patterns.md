# Storybook Patterns

## Overview

fpkit uses Storybook for component development, documentation, and interactive testing. This guide documents story structure, play functions, and documentation patterns.

---

## Story File Structure

### Basic Structure

```typescript
import type { Meta, StoryObj } from '@storybook/react'
import { within, userEvent, expect } from '@storybook/test'
import { Button } from './button'
import './button.scss'  // Always import component styles

const meta = {
  title: 'FP.React Components/Buttons',
  component: Button,
  tags: ['beta'],  // or 'rc', 'stable', 'accessible'
  args: {
    children: 'Click me',
  },
  parameters: {
    actions: { argTypesRegex: '^on.*' },
  },
} satisfies Meta<typeof Button>

export default meta
type Story = StoryObj<typeof meta>

export const Default: Story = {}
```

---

## Meta Configuration

### Title Organization

Use hierarchical titles for organization:

```typescript
// Core components
title: 'FP.React Components/Buttons'
title: 'FP.React Components/Forms/Input'

// Layout components
title: 'FP.React Components/Layout/Card'

// Navigation
title: 'FP.React Components/Navigation/Nav'
```

### Tags

Use tags to indicate component maturity:

```typescript
tags: ['stable']      // Production-ready, well-tested
tags: ['beta']        // Feature-complete, undergoing testing
tags: ['rc']          // Release candidate, final testing
tags: ['accessible']  // WCAG AA compliant
tags: ['autodocs']    // Auto-generate documentation
```

### Default Args

Set sensible defaults for all stories:

```typescript
args: {
  children: 'Button Text',
  type: 'button',
  onClick: fn(),  // Mock function from @storybook/test
}
```

### Parameters

```typescript
parameters: {
  // Auto-detect event handlers (onClick, onChange, etc.)
  actions: { argTypesRegex: '^on.*' },

  // Add documentation
  docs: {
    description: {
      component: 'A flexible button component with multiple variants.',
    },
  },

  // Layout configuration
  layout: 'centered',  // or 'fullscreen', 'padded'
}
```

---

## Story Variants

### Default Story

```typescript
export const Default: Story = {
  // Uses args from meta
}
```

### Story with Args

```typescript
export const Primary: Story = {
  args: {
    variant: 'primary',
    children: 'Primary Button',
  },
}

export const Secondary: Story = {
  args: {
    variant: 'secondary',
    children: 'Secondary Button',
  },
}
```

### Story with Custom Render

```typescript
export const WithIcon: Story = {
  render: () => (
    <Button>
      <Icon name="check" />
      <span>Submit</span>
    </Button>
  ),
}

export const Multiple: Story = {
  render: () => (
    <div style={{ display: 'flex', gap: '1rem' }}>
      <Button variant="primary">Save</Button>
      <Button variant="secondary">Cancel</Button>
      <Button variant="tertiary">Reset</Button>
    </div>
  ),
}
```

### Size Variants

```typescript
export const Small: Story = {
  args: {
    'data-btn': 'small',
    children: 'Small Button',
  },
}

export const Medium: Story = {
  args: {
    'data-btn': 'medium',
    children: 'Medium Button',
  },
}

export const Large: Story = {
  args: {
    'data-btn': 'large',
    children: 'Large Button',
  },
}
```

### State Variants

```typescript
export const Disabled: Story = {
  args: {
    disabled: true,
    children: 'Disabled Button',
  },
}

export const Loading: Story = {
  args: {
    loading: true,
    children: 'Loading...',
  },
}
```

---

## Play Functions

Play functions provide automated interaction testing within Storybook.

### Basic Play Function

```typescript
export const ButtonComponent: Story = {
  play: async ({ canvasElement, step }) => {
    const canvas = within(canvasElement)
    const button = canvas.getByRole('button')

    await step('Button is rendered', async () => {
      expect(button).toBeInTheDocument()
    })

    await step('Button is clicked', async () => {
      await userEvent.click(button)
    })
  },
}
```

### Testing Keyboard Navigation

```typescript
play: async ({ canvasElement, step }) => {
  const canvas = within(canvasElement)
  const button = canvas.getByRole('button')

  await step('Button gets focus on tab', async () => {
    await userEvent.tab()
    expect(button).toHaveFocus()
  })

  await step('Button activates with Enter key', async () => {
    await userEvent.keyboard('{Enter}')
  })

  await step('Button activates with Space key', async () => {
    await userEvent.keyboard(' ')
  })
}
```

### Testing Hover States

```typescript
play: async ({ canvasElement, step }) => {
  const canvas = within(canvasElement)
  const button = canvas.getByRole('button')

  await step('Button responds to hover', async () => {
    await userEvent.hover(button)
    expect(button).toHaveClass('hover')  // If applicable
  })

  await step('Button responds to unhover', async () => {
    await userEvent.unhover(button)
  })
}
```

### Testing Form Interactions

```typescript
play: async ({ canvasElement, step }) => {
  const canvas = within(canvasElement)
  const input = canvas.getByRole('textbox')
  const submitButton = canvas.getByRole('button', { name: /submit/i })

  await step('User types into input', async () => {
    await userEvent.type(input, 'test@example.com')
    expect(input).toHaveValue('test@example.com')
  })

  await step('User submits form', async () => {
    await userEvent.click(submitButton)
  })
}
```

### Testing Accessibility

```typescript
play: async ({ canvasElement, step }) => {
  const canvas = within(canvasElement)
  const button = canvas.getByRole('button')

  await step('Has accessible name', async () => {
    expect(button).toHaveAccessibleName('Click me')
  })

  await step('Has correct ARIA attributes', async () => {
    expect(button).toHaveAttribute('aria-disabled', 'false')
  })

  await step('Is keyboard accessible', async () => {
    await userEvent.tab()
    expect(button).toHaveFocus()
  })
}
```

---

## Documentation Stories

### CSS Variable Customization

```typescript
export const Customization: Story = {
  render: () => (
    <div
      style={{
        '--btn-primary-bg': '#7c3aed',
        '--btn-primary-color': 'white',
        '--btn-radius': '2rem',
        '--btn-padding-inline': '2rem',
      } as React.CSSProperties}
    >
      <Button variant="primary">Custom Styled</Button>
    </div>
  ),
  parameters: {
    docs: {
      description: {
        story: `
Customize button appearance using CSS variables:
- \`--btn-primary-bg\`: Background color
- \`--btn-primary-color\`: Text color
- \`--btn-radius\`: Border radius
- \`--btn-padding-inline\`: Horizontal padding
        `,
      },
    },
  },
}
```

### Before/After Comparisons

```typescript
export const EnabledVsDisabled: Story = {
  render: () => (
    <div style={{ display: 'flex', gap: '1rem', alignItems: 'center' }}>
      <Button>Enabled</Button>
      <Button disabled>Disabled</Button>
    </div>
  ),
  parameters: {
    docs: {
      description: {
        story: 'Comparison of enabled and disabled button states.',
      },
    },
  },
}
```

---

## ArgTypes Configuration

### Controlling Props

```typescript
const meta = {
  title: 'Components/Button',
  component: Button,
  argTypes: {
    variant: {
      control: 'select',
      options: ['primary', 'secondary', 'tertiary'],
      description: 'Visual style variant',
      table: {
        defaultValue: { summary: 'primary' },
        type: { summary: 'string' },
      },
    },
    size: {
      control: 'radio',
      options: ['small', 'medium', 'large'],
    },
    disabled: {
      control: 'boolean',
    },
    onClick: {
      action: 'clicked',
    },
  },
} satisfies Meta<typeof Button>
```

### Hiding Props

```typescript
argTypes: {
  // Hide internal props from controls
  ref: { table: { disable: true } },
  as: { table: { disable: true } },

  // Or just hide from controls, keep in docs
  className: { control: false },
}
```

---

## Compound Component Stories

### Card with Sub-Components

```typescript
export const CompleteCard: Story = {
  render: () => (
    <Card>
      <Card.Title>Card Title</Card.Title>
      <Card.Content>
        This is the card content area. It can contain any React children.
      </Card.Content>
      <Card.Footer>
        <Button variant="primary">Action</Button>
        <Button variant="secondary">Cancel</Button>
      </Card.Footer>
    </Card>
  ),
}

export const HeaderOnly: Story = {
  render: () => (
    <Card>
      <Card.Title>Simple Card</Card.Title>
    </Card>
  ),
}

export const InteractiveCard: Story = {
  render: () => (
    <Card
      interactive
      onClick={() => alert('Card clicked!')}
      aria-label="Interactive card"
    >
      <Card.Title>Click Me</Card.Title>
      <Card.Content>This entire card is clickable.</Card.Content>
    </Card>
  ),
  play: async ({ canvasElement, step }) => {
    const canvas = within(canvasElement)
    const card = canvas.getByRole('button')

    await step('Card is keyboard accessible', async () => {
      await userEvent.tab()
      expect(card).toHaveFocus()
    })

    await step('Card activates on Enter', async () => {
      await userEvent.keyboard('{Enter}')
    })
  },
}
```

---

## Style Import Pattern

**Always import component SCSS in stories:**

```typescript
import { Button } from './button'
import './button.scss'  // Required for styles to load
```

This ensures styles are loaded in Storybook's isolated iframe.

---

## Mock Functions

Use `fn()` from `@storybook/test` for event handlers:

```typescript
import { fn } from '@storybook/test'

const meta = {
  component: Button,
  args: {
    onClick: fn(),  // Auto-logged in Actions panel
    onPointerDown: fn(),
    onPointerOver: fn(),
  },
} satisfies Meta<typeof Button>
```

---

## Documentation Parameters

### Component Description

```typescript
parameters: {
  docs: {
    description: {
      component: `
A flexible button component that supports multiple variants, sizes, and states.

## Features
- Multiple style variants (primary, secondary, tertiary)
- Size options (small, medium, large)
- Disabled state with \`aria-disabled\`
- Full keyboard accessibility

## Accessibility
- Uses semantic \`<button>\` element
- Keyboard navigable (Tab, Enter, Space)
- Screen reader compatible
- WCAG 2.1 Level AA compliant
      `,
    },
  },
}
```

### Story Description

```typescript
export const CustomStyling: Story = {
  render: () => { /* ... */ },
  parameters: {
    docs: {
      description: {
        story: `
This example demonstrates how to customize button appearance using CSS variables.
Override the following variables in your stylesheet or inline styles:
- \`--btn-bg\`: Background color
- \`--btn-color\`: Text color
- \`--btn-radius\`: Border radius
        `,
      },
    },
  },
}
```

---

## Best Practices

### ✅ Do

- **Import component styles** in every story file
- **Use play functions** to test interactions
- **Test keyboard navigation** for interactive components
- **Document CSS variables** in Customization stories
- **Use descriptive story names** (not "Story1", "Story2")
- **Add tags** to indicate component status
- **Test accessibility** with play functions
- **Organize stories** logically (default, variants, states, examples)

### ❌ Don't

- Skip importing SCSS files
- Create stories without any interactivity examples
- Forget to test keyboard navigation
- Use placeholder text like "Lorem ipsum" extensively
- Create overly complex stories
- Duplicate story code (use render functions)
- Skip documentation parameters
- Test implementation details in play functions

---

## Story Organization Pattern

Organize stories from simple to complex:

```typescript
// 1. Default/Basic
export const Default: Story = {}

// 2. Variants
export const Primary: Story = {}
export const Secondary: Story = {}
export const Tertiary: Story = {}

// 3. Sizes
export const Small: Story = {}
export const Medium: Story = {}
export const Large: Story = {}

// 4. States
export const Disabled: Story = {}
export const Loading: Story = {}
export const Error: Story = {}

// 5. Compositions
export const WithIcon: Story = {}
export const MultipleButtons: Story = {}

// 6. Customization
export const CustomStyling: Story = {}
export const DarkTheme: Story = {}
```

---

## Running Storybook

### Development

```bash
# Start Storybook dev server
npm run storybook

# Start on different port
npm run storybook -- --port 6007
```

### Building

```bash
# Build static Storybook
npm run build-storybook

# Build to custom directory
npm run build-storybook -- --output-dir ./docs
```

### Testing

```bash
# Run play function tests
npm run test-storybook

# Run in CI mode
npm run test-storybook -- --ci
```

---

## Addons Used in fpkit

### A11y Addon

Tests accessibility violations in real-time:

```typescript
// Automatically enabled for all stories
// View results in "Accessibility" panel
```

### Actions Addon

Logs event handler calls:

```typescript
parameters: {
  actions: { argTypesRegex: '^on.*' },
}
```

### Docs Addon

Auto-generates documentation:

```typescript
tags: ['autodocs']
```

### Tag Badges Addon

Shows component status badges:

```typescript
tags: ['beta', 'accessible']  // Shows badges in Storybook UI
```

---

## Resources

- [Storybook Documentation](https://storybook.js.org/docs)
- [Play Function Testing](https://storybook.js.org/docs/react/writing-stories/play-function)
- [Testing Library in Storybook](https://storybook.js.org/docs/react/writing-tests/importing-stories-in-tests)
- [Accessibility Addon](https://storybook.js.org/addons/@storybook/addon-a11y)
