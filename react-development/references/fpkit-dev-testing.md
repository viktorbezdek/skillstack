# Testing Guide

## Overview

This guide shows how to test applications and custom components built with @fpkit/acss using **Vitest** and **React Testing Library**. fpkit components are already tested, so focus your tests on your custom logic, compositions, and integrations.

---

## Setup

### Installation

```bash
npm install -D vitest @testing-library/react @testing-library/user-event @testing-library/jest-dom jsdom
```

### Vitest Configuration

```javascript
// vitest.config.ts
import { defineConfig } from 'vitest/config'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  test: {
    environment: 'jsdom',
    globals: true,
    setupFiles: './src/test/setup.ts',
  },
})
```

### Setup File

```typescript
// src/test/setup.ts
import { expect, afterEach } from 'vitest'
import { cleanup } from '@testing-library/react'
import * as matchers from '@testing-library/jest-dom/matchers'

expect.extend(matchers)

afterEach(() => {
  cleanup()
})
```

### Package.json Scripts

```json
{
  "scripts": {
    "test": "vitest",
    "test:ui": "vitest --ui",
    "test:coverage": "vitest --coverage"
  }
}
```

---

## Basic Testing Patterns

### Rendering Tests

Test that your composed components render correctly:

```typescript
import { render, screen } from '@testing-library/react'
import { describe, it, expect } from 'vitest'
import { Button } from '@fpkit/acss'

describe('Custom Button Usage', () => {
  it('renders button with custom content', () => {
    render(<Button>Click me</Button>)
    expect(screen.getByText('Click me')).toBeInTheDocument()
  })

  it('renders button with custom className', () => {
    render(<Button className="custom-btn">Click me</Button>)
    const button = screen.getByRole('button')
    expect(button).toHaveClass('custom-btn')
  })
})
```

### Testing Composed Components

Focus tests on how your components integrate with fpkit:

```typescript
import { Badge, Button } from '@fpkit/acss'

// Your composed component
const StatusButton = ({ status, children }) => (
  <Button>
    {children}
    <Badge variant={status}>{status}</Badge>
  </Button>
)

// Your tests
describe('StatusButton', () => {
  it('renders button with status badge', () => {
    render(<StatusButton status="active">Server</StatusButton>)

    // Test composition
    expect(screen.getByRole('button')).toBeInTheDocument()
    expect(screen.getByText('Server')).toBeInTheDocument()
    expect(screen.getByText('active')).toBeInTheDocument()
  })

  it('passes props to underlying button', () => {
    const handleClick = vi.fn()
    render(
      <StatusButton status="inactive" onClick={handleClick}>
        Server
      </StatusButton>
    )

    const button = screen.getByRole('button')
    await userEvent.click(button)

    expect(handleClick).toHaveBeenCalledTimes(1)
  })
})
```

---

## Query Best Practices

### Query Priority

Use queries in this order:

1. **getByRole** (best) - Most accessible query
2. **getByLabelText** - For form controls
3. **getByText** - For non-interactive content
4. **getByTestId** (last resort) - When no other query works

```typescript
// ✅ Good - query by role
const button = screen.getByRole('button', { name: 'Submit' })

// ✅ Good - query by label
const input = screen.getByLabelText('Email')

// ✅ Good - query by text
const heading = screen.getByText('Welcome')

// ⚠️ Use sparingly - test ID
const custom = screen.getByTestId('custom-element')
```

### Common Queries

```typescript
// Buttons
screen.getByRole('button')
screen.getByRole('button', { name: 'Submit' })

// Links
screen.getByRole('link', { name: 'Home' })

// Headings
screen.getByRole('heading', { level: 1 })
screen.getByRole('heading', { name: 'Title' })

// Form controls
screen.getByLabelText('Email')
screen.getByPlaceholderText('Enter email...')
screen.getByRole('textbox')

// Text content
screen.getByText('Hello')
screen.getByText(/hello/i) // Case-insensitive

// Test IDs
screen.getByTestId('custom-id')
```

### Multiple Elements

```typescript
// Get all matching elements
const buttons = screen.getAllByRole('button')
expect(buttons).toHaveLength(3)

// Query (returns null if not found)
const button = screen.queryByRole('button')
expect(button).not.toBeInTheDocument()

// Find (async, waits for element)
const button = await screen.findByRole('button')
expect(button).toBeInTheDocument()
```

---

## Event Testing

### User Interactions

```typescript
import { userEvent } from '@testing-library/user-event'

describe('User Interactions', () => {
  it('calls onClick handler when clicked', async () => {
    const handleClick = vi.fn()
    render(<Button onClick={handleClick}>Click me</Button>)

    const button = screen.getByRole('button')
    await userEvent.click(button)

    expect(handleClick).toHaveBeenCalledTimes(1)
  })

  it('handles keyboard activation', async () => {
    const handleClick = vi.fn()
    render(<Button onClick={handleClick}>Click me</Button>)

    const button = screen.getByRole('button')
    button.focus()
    await userEvent.keyboard('{Enter}')

    expect(handleClick).toHaveBeenCalled()
  })

  it('handles hover events', async () => {
    const handleHover = vi.fn()
    render(<Button onMouseEnter={handleHover}>Hover me</Button>)

    const button = screen.getByRole('button')
    await userEvent.hover(button)

    expect(handleHover).toHaveBeenCalled()
  })
})
```

### Testing Disabled State (aria-disabled Pattern)

fpkit Button uses `aria-disabled` instead of native `disabled`. Test both the attribute and prevented interactions:

```typescript
describe('Disabled Button', () => {
  it('has aria-disabled attribute when disabled', () => {
    render(<Button disabled>Click me</Button>)

    const button = screen.getByRole('button')
    expect(button).toHaveAttribute('aria-disabled', 'true')
  })

  it('prevents onClick when disabled', async () => {
    const handleClick = vi.fn()
    render(<Button disabled onClick={handleClick}>Click me</Button>)

    const button = screen.getByRole('button')
    await userEvent.click(button)

    // fpkit's useDisabledState hook prevents the click
    expect(handleClick).not.toHaveBeenCalled()
  })

  it('remains in tab order when disabled', async () => {
    render(
      <>
        <Button>First</Button>
        <Button disabled>Disabled</Button>
        <Button>Third</Button>
      </>
    )

    // Tab through all buttons (disabled stays in tab order)
    await userEvent.tab()
    expect(screen.getByText('First')).toHaveFocus()

    await userEvent.tab()
    expect(screen.getByText('Disabled')).toHaveFocus() // ✅ Still focusable!

    await userEvent.tab()
    expect(screen.getByText('Third')).toHaveFocus()
  })

  it('has .is-disabled className when disabled', () => {
    render(<Button disabled>Click me</Button>)

    const button = screen.getByRole('button')
    expect(button).toHaveClass('is-disabled')
  })
})
```

### Form Interactions

```typescript
describe('Form Interactions', () => {
  it('handles text input', async () => {
    const handleChange = vi.fn()
    render(<Input onChange={handleChange} />)

    const input = screen.getByRole('textbox')
    await userEvent.type(input, 'Hello')

    expect(input).toHaveValue('Hello')
    expect(handleChange).toHaveBeenCalledTimes(5) // Once per character
  })

  it('handles form submission', async () => {
    const handleSubmit = vi.fn((e) => e.preventDefault())
    render(
      <form onSubmit={handleSubmit}>
        <Input name="email" />
        <Button type="submit">Submit</Button>
      </form>
    )

    const input = screen.getByRole('textbox')
    const submitBtn = screen.getByRole('button')

    await userEvent.type(input, 'test@example.com')
    await userEvent.click(submitBtn)

    expect(handleSubmit).toHaveBeenCalled()
  })
})
```

---

## Testing Component States

### Disabled State

See the "Testing Disabled State (aria-disabled Pattern)" section above for comprehensive disabled state testing examples.

### Loading State

```typescript
const LoadingButton = ({ loading, onClick, children }) => {
  return (
    <Button disabled={loading} onClick={onClick}>
      {loading ? 'Loading...' : children}
    </Button>
  )
}

describe('LoadingButton', () => {
  it('shows loading text when loading', () => {
    render(<LoadingButton loading>Submit</LoadingButton>)
    expect(screen.getByText('Loading...')).toBeInTheDocument()
    expect(screen.queryByText('Submit')).not.toBeInTheDocument()
  })

  it('disables button while loading', () => {
    render(<LoadingButton loading>Submit</LoadingButton>)
    const button = screen.getByRole('button')
    expect(button).toHaveAttribute('aria-disabled', 'true')
  })
})
```

### Conditional Rendering

```typescript
describe('Conditional Rendering', () => {
  it('shows error message when error exists', () => {
    const { rerender } = render(<Input />)
    expect(screen.queryByRole('alert')).not.toBeInTheDocument()

    rerender(<Input error="Invalid input" />)
    expect(screen.getByRole('alert')).toHaveTextContent('Invalid input')
  })

  it('renders different content based on prop', () => {
    const { rerender } = render(
      <Notification inline>Message</Notification>
    )
    expect(screen.getByRole('alert')).toBeInTheDocument()

    rerender(<Notification isOpen>Message</Notification>)
    expect(screen.getByRole('dialog')).toBeInTheDocument()
  })
})
```

---

## Accessibility Testing

### ARIA Attributes

```typescript
describe('Accessibility', () => {
  it('has correct ARIA label', () => {
    render(
      <Button aria-label="Close dialog">
        <Icon name="close" />
      </Button>
    )

    const button = screen.getByRole('button', { name: 'Close dialog' })
    expect(button).toBeInTheDocument()
  })

  it('has correct ARIA description', () => {
    render(
      <>
        <Button aria-describedby="hint">Submit</Button>
        <div id="hint">This will save your changes</div>
      </>
    )

    const button = screen.getByRole('button')
    expect(button).toHaveAttribute('aria-describedby', 'hint')
  })
})
```

### Keyboard Navigation

```typescript
describe('Keyboard Navigation', () => {
  it('is focusable with Tab key', async () => {
    render(<Button>Click me</Button>)

    const button = screen.getByRole('button')
    expect(button).not.toHaveFocus()

    await userEvent.tab()
    expect(button).toHaveFocus()
  })

  it('navigates through multiple buttons', async () => {
    render(
      <>
        <Button>First</Button>
        <Button>Second</Button>
        <Button>Third</Button>
      </>
    )

    const [first, second, third] = screen.getAllByRole('button')

    await userEvent.tab()
    expect(first).toHaveFocus()

    await userEvent.tab()
    expect(second).toHaveFocus()

    await userEvent.tab()
    expect(third).toHaveFocus()
  })

  it('closes dialog on Escape key', async () => {
    const handleClose = vi.fn()
    render(
      <Dialog isOpen onClose={handleClose}>
        Content
      </Dialog>
    )

    await userEvent.keyboard('{Escape}')
    expect(handleClose).toHaveBeenCalled()
  })
})
```

### Automated Accessibility Testing

```bash
npm install -D jest-axe
```

```typescript
import { axe, toHaveNoViolations } from 'jest-axe'

expect.extend(toHaveNoViolations)

describe('Accessibility Violations', () => {
  it('should not have accessibility violations', async () => {
    const { container } = render(
      <div>
        <Button>Click me</Button>
        <Link href="/page">Navigate</Link>
      </div>
    )

    const results = await axe(container)
    expect(results).toHaveNoViolations()
  })

  it('composed component has no violations', async () => {
    const { container } = render(
      <StatusButton status="active">Server</StatusButton>
    )

    const results = await axe(container)
    expect(results).toHaveNoViolations()
  })
})
```

---

## Testing Link Security Features

fpkit Link components automatically add security attributes for external links. Test that these security features work correctly:

```typescript
import { Link } from '@fpkit/acss'
import { render, screen } from '@testing-library/react'

describe('Link Security', () => {
  it('automatically adds noopener noreferrer to external links', () => {
    render(
      <Link href="https://example.com" target="_blank">
        External Site
      </Link>
    )

    const link = screen.getByRole('link')
    const rel = link.getAttribute('rel')

    expect(rel).toContain('noopener')
    expect(rel).toContain('noreferrer')
  })

  it('preserves custom rel values while adding security', () => {
    render(
      <Link href="https://example.com" target="_blank" rel="nofollow">
        Sponsored Link
      </Link>
    )

    const link = screen.getByRole('link')
    const rel = link.getAttribute('rel')

    // All three should be present
    expect(rel).toContain('noopener')
    expect(rel).toContain('noreferrer')
    expect(rel).toContain('nofollow')
  })

  it('adds prefetch when enabled', () => {
    render(
      <Link href="https://example.com" target="_blank" prefetch>
        Fast Link
      </Link>
    )

    const link = screen.getByRole('link')
    const rel = link.getAttribute('rel')

    expect(rel).toContain('prefetch')
    expect(rel).toContain('noopener')
    expect(rel).toContain('noreferrer')
  })

  it('does not add security attrs to internal links', () => {
    render(
      <Link href="/internal-page">
        Internal Link
      </Link>
    )

    const link = screen.getByRole('link')
    const rel = link.getAttribute('rel')

    // Should be null or not contain security tokens
    expect(rel).not.toContain('noopener')
    expect(rel).not.toContain('noreferrer')
  })
})
```

### Testing Link Accessibility

```typescript
describe('Link Accessibility', () => {
  it('supports ref forwarding for focus management', () => {
    const ref = React.createRef<HTMLAnchorElement>()
    render(
      <Link ref={ref} href="/page">
        Skip to content
      </Link>
    )

    expect(ref.current).toBeInstanceOf(HTMLAnchorElement)
    ref.current?.focus()
    expect(ref.current).toHaveFocus()
  })

  it('onClick captures all activation methods', async () => {
    const handleClick = vi.fn()
    render(
      <Link href="/products" onClick={handleClick}>
        Products
      </Link>
    )

    const link = screen.getByRole('link')

    // Test mouse click
    await userEvent.click(link)
    expect(handleClick).toHaveBeenCalledTimes(1)

    // Test keyboard activation
    link.focus()
    await userEvent.keyboard('{Enter}')
    expect(handleClick).toHaveBeenCalledTimes(2) // ✅ onClick fires for keyboard!
  })
})
```

---

## Async Testing

### Waiting for Elements

```typescript
describe('Async Rendering', () => {
  it('shows success message after action', async () => {
    const SuccessComponent = () => {
      const [success, setSuccess] = useState(false)
      return (
        <>
          <Button onClick={() => setTimeout(() => setSuccess(true), 100)}>
            Submit
          </Button>
          {success && <div role="alert">Success!</div>}
        </>
      )
    }

    render(<SuccessComponent />)

    const button = screen.getByRole('button')
    await userEvent.click(button)

    // Wait for success message to appear
    const alert = await screen.findByRole('alert')
    expect(alert).toHaveTextContent('Success!')
  })
})
```

### Testing Loading States

```typescript
import { waitFor } from '@testing-library/react'

describe('Loading States', () => {
  it('shows loading then content', async () => {
    const DataComponent = () => {
      const [loading, setLoading] = useState(true)
      const [data, setData] = useState(null)

      useEffect(() => {
        setTimeout(() => {
          setData('Loaded data')
          setLoading(false)
        }, 100)
      }, [])

      if (loading) return <div>Loading...</div>
      return <div>{data}</div>
    }

    render(<DataComponent />)

    // Initially shows loading
    expect(screen.getByText('Loading...')).toBeInTheDocument()

    // Wait for loading to disappear
    await waitFor(() => {
      expect(screen.queryByText('Loading...')).not.toBeInTheDocument()
    })

    // Data is displayed
    expect(screen.getByText('Loaded data')).toBeInTheDocument()
  })
})
```

---

## Testing Compound Components

```typescript
import { Card } from '@fpkit/acss'

describe('Card Component Usage', () => {
  it('renders card with all sub-components', () => {
    render(
      <Card>
        <Card.Header>
          <Card.Title>Title</Card.Title>
        </Card.Header>
        <Card.Content>Content</Card.Content>
        <Card.Footer>
          <Button>Action</Button>
        </Card.Footer>
      </Card>
    )

    expect(screen.getByText('Title')).toBeInTheDocument()
    expect(screen.getByText('Content')).toBeInTheDocument()
    expect(screen.getByRole('button', { name: 'Action' })).toBeInTheDocument()
  })

  it('renders card without optional sections', () => {
    render(
      <Card>
        <Card.Content>Just content</Card.Content>
      </Card>
    )

    expect(screen.getByText('Just content')).toBeInTheDocument()
    // Header and footer should not exist
  })
})
```

---

## Mock Functions

### Creating and Using Mocks

```typescript
import { vi } from 'vitest'

describe('Mocking', () => {
  it('mocks onClick handler', async () => {
    const handleClick = vi.fn()
    render(<Button onClick={handleClick}>Click me</Button>)

    await userEvent.click(screen.getByRole('button'))

    expect(handleClick).toHaveBeenCalledTimes(1)
  })

  it('mocks with return value', () => {
    const mockFn = vi.fn(() => 'mocked value')
    const result = mockFn()

    expect(result).toBe('mocked value')
    expect(mockFn).toHaveBeenCalled()
  })

  it('mocks with arguments', async () => {
    const handleChange = vi.fn()
    render(<Input onChange={handleChange} />)

    const input = screen.getByRole('textbox')
    await userEvent.type(input, 'test')

    expect(handleChange).toHaveBeenCalledWith(
      expect.objectContaining({
        target: expect.objectContaining({ value: 't' })
      })
    )
  })
})
```

---

## Test Organization

### Describe Blocks

```typescript
describe('CustomComponent', () => {
  describe('rendering', () => {
    it('renders with default props', () => {
      // Test
    })

    it('renders with custom props', () => {
      // Test
    })
  })

  describe('interactions', () => {
    it('handles click events', async () => {
      // Test
    })

    it('handles keyboard events', async () => {
      // Test
    })
  })

  describe('accessibility', () => {
    it('has proper ARIA attributes', () => {
      // Test
    })

    it('is keyboard navigable', async () => {
      // Test
    })
  })

  describe('states', () => {
    it('shows loading state', () => {
      // Test
    })

    it('shows error state', () => {
      // Test
    })
  })
})
```

### Test Naming

```typescript
// ✅ Good - descriptive and clear
it('calls onClick handler when button is clicked')
it('shows error message when validation fails')
it('disables submit button while form is submitting')
it('renders badge with correct variant')

// ❌ Bad - vague or redundant
it('works correctly')
it('test button')
it('should show message') // "should" is redundant
```

---

## Common Testing Patterns

### Testing Custom Props

```typescript
const CustomButton = ({ loading, error, ...props }) => (
  <Button
    {...props}
    disabled={loading}
    style={{ '--btn-bg': error ? 'red' : undefined }}
  >
    {loading ? 'Loading...' : props.children}
  </Button>
)

describe('CustomButton Props', () => {
  it('shows loading state', () => {
    render(<CustomButton loading>Submit</CustomButton>)
    expect(screen.getByText('Loading...')).toBeInTheDocument()
  })

  it('applies error styling', () => {
    render(<CustomButton error>Submit</CustomButton>)
    const button = screen.getByRole('button')
    expect(button).toHaveStyle({ '--btn-bg': 'red' })
  })
})
```

### Testing Composition

```typescript
const ActionCard = ({ title, onAction }) => (
  <Card>
    <Card.Title>{title}</Card.Title>
    <Card.Footer>
      <Button onClick={onAction}>Perform Action</Button>
    </Card.Footer>
  </Card>
)

describe('ActionCard Composition', () => {
  it('renders composed structure', () => {
    render(<ActionCard title="Test Card" onAction={vi.fn()} />)

    expect(screen.getByText('Test Card')).toBeInTheDocument()
    expect(screen.getByRole('button')).toBeInTheDocument()
  })

  it('calls action handler', async () => {
    const handleAction = vi.fn()
    render(<ActionCard title="Test" onAction={handleAction} />)

    await userEvent.click(screen.getByRole('button'))
    expect(handleAction).toHaveBeenCalled()
  })
})
```

---

## Best Practices

### ✅ Do

- **Test behavior, not implementation** - Focus on what users experience
- **Use accessible queries** - `getByRole`, `getByLabelText`
- **Test integration** - How components work together
- **Test user interactions** - Clicks, typing, keyboard navigation
- **Test accessibility** - ARIA attributes, keyboard support
- **Use meaningful test names** - Describe what's being tested
- **Keep tests focused** - One concept per test

### ❌ Don't

- **Don't test fpkit internals** - fpkit components are already tested
- **Don't test styling details** - Unless critical to functionality
- **Don't use implementation details** - Avoid querying by class names
- **Don't test third-party libraries** - Trust they're tested
- **Don't write redundant tests** - If fpkit tests it, you don't need to

---

## Running Tests

```bash
# Run all tests
npm test

# Run tests in watch mode
npm test -- --watch

# Run with coverage
npm run test:coverage

# Run with UI
npm run test:ui

# Run specific test file
npm test -- button.test.tsx

# Update snapshots
npm test -- -u
```

---

## Additional Resources

- **[Vitest Documentation](https://vitest.dev/)** - Test runner
- **[Testing Library Docs](https://testing-library.com/docs/react-testing-library/intro/)** - Query and interaction APIs
- **[jest-axe](https://github.com/nickcolley/jest-axe)** - Automated accessibility testing
- **[Common Testing Mistakes](https://kentcdodds.com/blog/common-mistakes-with-react-testing-library)** - Best practices

---

## Related Guides

- **[Accessibility Guide](./accessibility.md)** - Accessibility patterns to test
- **[Composition Guide](./composition.md)** - Patterns to test in compositions
- **[Architecture Guide](./architecture.md)** - Component patterns and structure

---

**Remember**: Focus your tests on **your application logic and composed components**. fpkit components are thoroughly tested, so trust their functionality and test how you use them together.
