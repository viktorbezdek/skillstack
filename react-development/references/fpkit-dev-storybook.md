# Storybook Guide

## Overview

This guide shows how to document custom components and compositions built with @fpkit/acss using Storybook. Whether you're building an internal component library or documenting your application components, Storybook provides an excellent development and documentation environment.

---

## Setup

### Installation

```bash
npm install -D @storybook/react @storybook/react-vite @storybook/test storybook
```

### Initialize Storybook

```bash
npx storybook init
```

### Configuration

```javascript
// .storybook/main.ts
import type { StorybookConfig } from '@storybook/react-vite'

const config: StorybookConfig = {
  stories: ['../src/**/*.stories.@(js|jsx|ts|tsx|mdx)'],
  addons: [
    '@storybook/addon-links',
    '@storybook/addon-essentials',
    '@storybook/addon-interactions',
  ],
  framework: {
    name: '@storybook/react-vite',
    options: {},
  },
}

export default config
```

### Import fpkit Styles

```javascript
// .storybook/preview.ts
import '@fpkit/acss/libs/index.css'

export default {
  parameters: {
    actions: { argTypesRegex: '^on.*' },
    controls: {
      matchers: {
        color: /(background|color)$/i,
        date: /Date$/,
      },
    },
  },
}
```

---

## Basic Story Structure

### Creating Your First Story

```typescript
// components/CustomButton.stories.tsx
import type { Meta, StoryObj } from '@storybook/react'
import { Button } from '@fpkit/acss'

// Your custom composed component
const CustomButton = ({ loading, children, ...props }) => (
  <Button {...props} disabled={loading}>
    {loading ? 'Loading...' : children}
  </Button>
)

const meta = {
  title: 'Components/CustomButton',
  component: CustomButton,
  tags: ['autodocs'],
  args: {
    children: 'Click me',
    loading: false,
  },
  argTypes: {
    loading: {
      control: 'boolean',
      description: 'Shows loading state',
    },
    onClick: {
      action: 'clicked',
    },
  },
} satisfies Meta<typeof CustomButton>

export default meta
type Story = StoryObj<typeof meta>

export const Default: Story = {}

export const Loading: Story = {
  args: {
    loading: true,
  },
}
```

---

## Story Patterns

### Default Story

The simplest story uses the default args from `meta`:

```typescript
export const Default: Story = {}
```

### Story with Custom Args

Override specific args for different variants:

```typescript
export const Primary: Story = {
  args: {
    variant: 'primary',
    children: 'Primary Action',
  },
}

export const Secondary: Story = {
  args: {
    variant: 'secondary',
    children: 'Secondary Action',
  },
}

export const Disabled: Story = {
  args: {
    disabled: true,
    children: 'Disabled Button',
  },
}
```

### Story with Custom Render

For complex compositions:

```typescript
import { Button, Badge } from '@fpkit/acss'

export const WithBadge: Story = {
  render: (args) => (
    <Button {...args}>
      <span>{args.children}</span>
      <Badge>New</Badge>
    </Button>
  ),
  args: {
    children: 'Featured',
  },
}

export const MultipleButtons: Story = {
  render: () => (
    <div style={{ display: 'flex', gap: '1rem' }}>
      <Button variant="primary">Save</Button>
      <Button variant="secondary">Cancel</Button>
      <Button variant="tertiary">Reset</Button>
    </div>
  ),
}
```

---

## Documenting Composed Components

### Card Composition Example

```typescript
// components/ActionCard.stories.tsx
import type { Meta, StoryObj } from '@storybook/react'
import { Card, Button } from '@fpkit/acss'

const ActionCard = ({ title, children, actions }) => (
  <Card>
    <Card.Header>
      <Card.Title>{title}</Card.Title>
    </Card.Header>
    <Card.Content>{children}</Card.Content>
    <Card.Footer>
      {actions.map((action, i) => (
        <Button key={i} {...action} />
      ))}
    </Card.Footer>
  </Card>
)

const meta = {
  title: 'Compositions/ActionCard',
  component: ActionCard,
  tags: ['autodocs'],
  parameters: {
    docs: {
      description: {
        component: `
ActionCard is a composition of fpkit Card, Button, and sub-components.
It provides a consistent layout for cards with title, content, and action buttons.

**Composed from:**
- Card (fpkit)
- Card.Header (fpkit)
- Card.Title (fpkit)
- Card.Content (fpkit)
- Card.Footer (fpkit)
- Button (fpkit)
        `,
      },
    },
  },
} satisfies Meta<typeof ActionCard>

export default meta
type Story = StoryObj<typeof meta>

export const Default: Story = {
  args: {
    title: 'Confirm Action',
    children: 'Are you sure you want to proceed with this action?',
    actions: [
      { children: 'Cancel', variant: 'secondary' },
      { children: 'Confirm', variant: 'primary' },
    ],
  },
}

export const SingleAction: Story = {
  args: {
    title: 'Notification',
    children: 'Your changes have been saved successfully.',
    actions: [
      { children: 'OK', variant: 'primary' },
    ],
  },
}
```

---

## CSS Variable Customization Stories

Show how users can customize your components:

```typescript
export const CustomStyling: Story = {
  render: () => (
    <div
      style={{
        '--btn-primary-bg': '#7c3aed',
        '--btn-primary-color': 'white',
        '--btn-radius': '2rem',
        '--btn-padding-inline': '3rem',
      } as React.CSSProperties}
    >
      <Button variant="primary">Custom Styled Button</Button>
    </div>
  ),
  parameters: {
    docs: {
      description: {
        story: `
Customize appearance using CSS variables:
- \`--btn-primary-bg\`: Background color
- \`--btn-primary-color\`: Text color
- \`--btn-radius\`: Border radius
- \`--btn-padding-inline\`: Horizontal padding

See the [CSS Variables Guide](/docs/guides/css-variables.md) for all available variables.
        `,
      },
    },
  },
}

export const ThemeExample: Story = {
  render: () => (
    <>
      <div
        className="light-theme"
        style={{
          '--btn-bg': 'white',
          '--btn-color': '#333',
          padding: '2rem',
          background: '#f9f9f9',
        } as React.CSSProperties}
      >
        <Button>Light Theme Button</Button>
      </div>

      <div
        className="dark-theme"
        style={{
          '--btn-bg': '#2d2d2d',
          '--btn-color': '#f0f0f0',
          padding: '2rem',
          background: '#1a1a1a',
          marginTop: '1rem',
        } as React.CSSProperties}
      >
        <Button>Dark Theme Button</Button>
      </div>
    </>
  ),
  parameters: {
    docs: {
      description: {
        story: 'Theme-based customization using scoped CSS variables.',
      },
    },
  },
}
```

---

## Interactive Testing with Play Functions

Play functions enable automated interaction testing in Storybook:

```typescript
import { within, userEvent, expect } from '@storybook/test'

export const InteractiveTest: Story = {
  play: async ({ canvasElement, step }) => {
    const canvas = within(canvasElement)
    const button = canvas.getByRole('button')

    await step('Button is rendered', async () => {
      expect(button).toBeInTheDocument()
      expect(button).toHaveTextContent('Click me')
    })

    await step('Button responds to click', async () => {
      await userEvent.click(button)
      // Check for expected behavior
    })

    await step('Button is keyboard accessible', async () => {
      await userEvent.tab()
      expect(button).toHaveFocus()
    })
  },
}
```

### Form Interaction Example

```typescript
export const FormInteraction: Story = {
  render: () => {
    const [value, setValue] = useState('')
    const [submitted, setSubmitted] = useState(false)

    return (
      <div>
        <Input
          value={value}
          onChange={(e) => setValue(e.target.value)}
          placeholder="Enter email..."
        />
        <Button
          onClick={() => setSubmitted(true)}
          disabled={!value}
        >
          Submit
        </Button>
        {submitted && <Alert variant="success">Form submitted!</Alert>}
      </div>
    )
  },
  play: async ({ canvasElement, step }) => {
    const canvas = within(canvasElement)
    const input = canvas.getByPlaceholderText('Enter email...')
    const button = canvas.getByRole('button')

    await step('User types into input', async () => {
      await userEvent.type(input, 'test@example.com')
      expect(input).toHaveValue('test@example.com')
    })

    await step('Submit button becomes enabled', async () => {
      expect(button).not.toHaveAttribute('aria-disabled', 'true')
    })

    await step('User submits form', async () => {
      await userEvent.click(button)
      expect(canvas.getByRole('alert')).toHaveTextContent('Form submitted!')
    })
  },
}
```

---

## ArgTypes Configuration

Control how props appear in Storybook controls:

```typescript
const meta = {
  component: CustomButton,
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
      description: 'Button size',
    },
    disabled: {
      control: 'boolean',
      description: 'Disables the button',
    },
    loading: {
      control: 'boolean',
      description: 'Shows loading state',
    },
    onClick: {
      action: 'clicked',
      description: 'Click event handler',
    },
    // Hide internal props
    ref: { table: { disable: true } },
    as: { table: { disable: true } },
  },
} satisfies Meta<typeof CustomButton>
```

---

## Documentation Parameters

### Component Description

```typescript
const meta = {
  title: 'Components/StatusButton',
  component: StatusButton,
  parameters: {
    docs: {
      description: {
        component: `
# StatusButton

A button component with an integrated status badge.

## Features
- Built on fpkit Button
- Includes Badge for status indication
- Fully accessible
- Customizable via CSS variables

## Usage
\`\`\`tsx
<StatusButton status="active" onClick={handleClick}>
  Server Status
</StatusButton>
\`\`\`

## Composed Components
- **Button** - Base interactive element
- **Badge** - Status indicator

See [Composition Guide](/docs/guides/composition.md) for composition patterns.
        `,
      },
    },
  },
} satisfies Meta<typeof StatusButton>
```

### Story Description

```typescript
export const Primary: Story = {
  args: {
    variant: 'primary',
  },
  parameters: {
    docs: {
      description: {
        story: 'Primary variant for high-emphasis actions.',
      },
    },
  },
}
```

---

## Organizing Stories

### Title Hierarchy

```typescript
// Group by category
title: 'Components/Buttons/CustomButton'
title: 'Components/Forms/SearchInput'
title: 'Compositions/Cards/ActionCard'

// Or by feature
title: 'Features/Authentication/LoginForm'
title: 'Features/Dashboard/StatsCard'

// Or by page
title: 'Pages/Home/HeroSection'
title: 'Pages/Settings/ProfileCard'
```

### Tags

```typescript
tags: ['autodocs']      // Auto-generate documentation
tags: ['stable']        // Production-ready
tags: ['beta']          // Testing phase
tags: ['composition']   // fpkit composition
```

---

## Accessibility Testing in Storybook

### Basic Accessibility Test

```typescript
export const AccessibilityTest: Story = {
  play: async ({ canvasElement, step }) => {
    const canvas = within(canvasElement)
    const button = canvas.getByRole('button')

    await step('Has accessible name', async () => {
      expect(button).toHaveAccessibleName()
    })

    await step('Is keyboard navigable', async () => {
      await userEvent.tab()
      expect(button).toHaveFocus()
    })

    await step('Activates with Enter key', async () => {
      await userEvent.keyboard('{Enter}')
    })

    await step('Activates with Space key', async () => {
      button.focus()
      await userEvent.keyboard(' ')
    })
  },
}
```

### ARIA Attributes Test

```typescript
export const AriaAttributesTest: Story = {
  args: {
    'aria-label': 'Close dialog',
    'aria-describedby': 'hint',
  },
  play: async ({ canvasElement, step }) => {
    const canvas = within(canvasElement)
    const button = canvas.getByRole('button')

    await step('Has ARIA label', async () => {
      expect(button).toHaveAttribute('aria-label', 'Close dialog')
    })

    await step('Has ARIA description', async () => {
      expect(button).toHaveAttribute('aria-describedby', 'hint')
    })
  },
}
```

---

## State Comparison Stories

Show different states side-by-side:

```typescript
export const AllStates: Story = {
  render: () => (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
      <div>
        <h3>Default</h3>
        <Button>Default Button</Button>
      </div>

      <div>
        <h3>Hover</h3>
        <Button className="hover">Hover State</Button>
      </div>

      <div>
        <h3>Focus</h3>
        <Button className="focus">Focus State</Button>
      </div>

      <div>
        <h3>Disabled</h3>
        <Button disabled>Disabled Button</Button>
      </div>

      <div>
        <h3>Loading</h3>
        <Button disabled>Loading...</Button>
      </div>
    </div>
  ),
  parameters: {
    docs: {
      description: {
        story: 'Comparison of all button states',
      },
    },
  },
}
```

---

## Best Practices

### ✅ Do

- **Document compositions** - Show which fpkit components you're using
- **Include play functions** - Test interactions automatically
- **Show CSS customization** - Demonstrate variable usage
- **Test accessibility** - Keyboard navigation, ARIA attributes
- **Use descriptive titles** - Clear hierarchy and organization
- **Add component descriptions** - Explain purpose and usage
- **Show state variants** - Default, hover, disabled, loading, error
- **Document props** - Use argTypes for prop documentation
- **Include usage examples** - Code snippets in descriptions

### ❌ Don't

- **Don't duplicate fpkit stories** - Focus on your custom logic
- **Don't overcomplicate** - Keep stories simple and focused
- **Don't skip accessibility** - Always test keyboard and screen readers
- **Don't forget CSS imports** - Import fpkit styles in preview
- **Don't use vague titles** - Be specific about what's being demonstrated

---

## Running Storybook

```bash
# Start Storybook dev server
npm run storybook

# Build Storybook static site
npm run build-storybook

# Serve built Storybook
npx http-server storybook-static
```

---

## Example: Complete Story File

```typescript
import type { Meta, StoryObj } from '@storybook/react'
import { within, userEvent, expect, fn } from '@storybook/test'
import { Button, Badge } from '@fpkit/acss'

// Your composed component
const NotificationButton = ({ count, onClick }) => (
  <Button onClick={onClick} aria-label={`Notifications (${count} unread)`}>
    <span aria-hidden="true">🔔</span>
    {count > 0 && (
      <Badge aria-hidden="true">{count}</Badge>
    )}
  </Button>
)

const meta = {
  title: 'Compositions/NotificationButton',
  component: NotificationButton,
  tags: ['autodocs', 'composition'],
  args: {
    count: 3,
    onClick: fn(),
  },
  argTypes: {
    count: {
      control: 'number',
      description: 'Number of unread notifications',
    },
    onClick: {
      action: 'clicked',
      description: 'Click handler',
    },
  },
  parameters: {
    docs: {
      description: {
        component: `
# NotificationButton

A button displaying notification count with a badge.

**Composed from:**
- Button (fpkit)
- Badge (fpkit)

**Accessibility:**
- Uses \`aria-label\` to announce count to screen readers
- Visual elements hidden from screen readers with \`aria-hidden\`
        `,
      },
    },
  },
} satisfies Meta<typeof NotificationButton>

export default meta
type Story = StoryObj<typeof meta>

export const Default: Story = {}

export const NoNotifications: Story = {
  args: {
    count: 0,
  },
}

export const ManyNotifications: Story = {
  args: {
    count: 99,
  },
}

export const CustomStyling: Story = {
  render: (args) => (
    <div
      style={{
        '--btn-padding-inline': '1.5rem',
        '--badge-bg': '#ef4444',
      } as React.CSSProperties}
    >
      <NotificationButton {...args} />
    </div>
  ),
  args: {
    count: 5,
  },
}

export const InteractiveTest: Story = {
  args: {
    count: 3,
  },
  play: async ({ canvasElement, step, args }) => {
    const canvas = within(canvasElement)
    const button = canvas.getByRole('button')

    await step('Has accessible label with count', async () => {
      expect(button).toHaveAttribute('aria-label', 'Notifications (3 unread)')
    })

    await step('Shows badge with count', async () => {
      expect(canvas.getByText('3')).toBeInTheDocument()
    })

    await step('Calls onClick when clicked', async () => {
      await userEvent.click(button)
      expect(args.onClick).toHaveBeenCalledTimes(1)
    })

    await step('Is keyboard accessible', async () => {
      await userEvent.tab()
      expect(button).toHaveFocus()

      await userEvent.keyboard('{Enter}')
      expect(args.onClick).toHaveBeenCalledTimes(2)
    })
  },
}
```

---

## Additional Resources

- **[Storybook Documentation](https://storybook.js.org/docs)** - Official Storybook docs
- **[Testing with Storybook](https://storybook.js.org/docs/writing-tests)** - Play functions and interaction testing
- **[Storybook Addons](https://storybook.js.org/addons)** - Extend functionality
- **[Component Story Format](https://storybook.js.org/docs/api/csf)** - CSF 3.0 specification

---

## Related Guides

- **[Composition Guide](./composition.md)** - Component composition patterns
- **[Testing Guide](./testing.md)** - Testing composed components
- **[Accessibility Guide](./accessibility.md)** - Accessibility testing patterns
- **[CSS Variables Guide](./css-variables.md)** - Styling customization

---

**Remember**: Storybook is for documenting **your components and compositions**. fpkit components already have stories in the fpkit Storybook - focus on showcasing how you use and compose them in your application.
