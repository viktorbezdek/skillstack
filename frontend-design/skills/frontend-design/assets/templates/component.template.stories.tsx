import type { Meta, StoryObj } from '@storybook/react'
import { within, userEvent, expect, fn } from '@storybook/test'
import { {{ComponentName}} } from './{{component-name}}'
import './{{component-name}}.scss'

const meta = {
  title: 'FP.React Components/{{ComponentName}}',
  component: {{ComponentName}},
  tags: ['beta'],  // Change to 'stable' when ready
  args: {
    children: '{{ComponentName}} content',
    // Add default args here
  },
  parameters: {
    actions: { argTypesRegex: '^on.*' },
    docs: {
      description: {
        component: `
A flexible {{ComponentName}} component that [describe purpose].

## Features
- Feature 1
- Feature 2
- Fully accessible
- Customizable with CSS variables

## Accessibility
- Keyboard navigable
- Screen reader compatible
- WCAG 2.1 Level AA compliant
        `,
      },
    },
  },
} satisfies Meta<typeof {{ComponentName}}>

export default meta
type Story = StoryObj<typeof meta>

/**
 * Default {{ComponentName}} component
 */
export const Default: Story = {
  play: async ({ canvasElement, step }) => {
    const canvas = within(canvasElement)
    const element = canvas.getByText('{{ComponentName}} content')

    await step('Component is rendered', async () => {
      expect(element).toBeInTheDocument()
    })

    // TODO: Add more interaction tests here
  },
}

/**
 * Primary variant
 */
export const Primary: Story = {
  args: {
    variant: 'primary',
    children: 'Primary {{ComponentName}}',
  },
}

/**
 * Secondary variant
 */
export const Secondary: Story = {
  args: {
    variant: 'secondary',
    children: 'Secondary {{ComponentName}}',
  },
}

/**
 * Small size
 */
export const Small: Story = {
  args: {
    size: 'small',
    children: 'Small {{ComponentName}}',
  },
}

/**
 * Medium size (default)
 */
export const Medium: Story = {
  args: {
    size: 'medium',
    children: 'Medium {{ComponentName}}',
  },
}

/**
 * Large size
 */
export const Large: Story = {
  args: {
    size: 'large',
    children: 'Large {{ComponentName}}',
  },
}

/**
 * Multiple {{ComponentName}} components
 */
export const Multiple: Story = {
  render: () => (
    <div style={{ display: 'flex', gap: '1rem', flexWrap: 'wrap' }}>
      <{{ComponentName}} variant="primary">Primary</{{ComponentName}}>
      <{{ComponentName}} variant="secondary">Secondary</{{ComponentName}}>
      <{{ComponentName}}>Default</{{ComponentName}}>
    </div>
  ),
}

/**
 * Customizing with CSS variables
 */
export const Customization: Story = {
  render: () => (
    <div
      style={{
        '--{{component-name}}-bg': '#7c3aed',
        '--{{component-name}}-color': 'white',
        '--{{component-name}}-radius': '1rem',
        '--{{component-name}}-padding-inline': '2rem',
      } as React.CSSProperties}
    >
      <{{ComponentName}}>Custom Styled {{ComponentName}}</{{ComponentName}}>
    </div>
  ),
  parameters: {
    docs: {
      description: {
        story: `
Customize appearance using CSS variables:

\`\`\`css
--{{component-name}}-bg: Background color
--{{component-name}}-color: Text color
--{{component-name}}-radius: Border radius
--{{component-name}}-padding-inline: Horizontal padding
--{{component-name}}-padding-block: Vertical padding
\`\`\`
        `,
      },
    },
  },
}

/**
 * Accessibility testing with keyboard navigation
 */
export const AccessibilityTest: Story = {
  render: () => (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
      <{{ComponentName}} as="button" type="button">
        Focusable {{ComponentName}}
      </{{ComponentName}}>
      <{{ComponentName}} as="a" href="#test">
        Link {{ComponentName}}
      </{{ComponentName}}>
    </div>
  ),
  play: async ({ canvasElement, step }) => {
    const canvas = within(canvasElement)

    await step('Elements are keyboard accessible', async () => {
      const button = canvas.getByRole('button')
      const link = canvas.getByRole('link')

      await userEvent.tab()
      expect(button).toHaveFocus()

      await userEvent.tab()
      expect(link).toHaveFocus()
    })
  },
}
