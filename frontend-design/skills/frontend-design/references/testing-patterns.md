# Testing Patterns

## Overview

fpkit uses **Vitest** as the test runner and **React Testing Library** for component testing. This guide documents testing patterns, best practices, and common scenarios.

---

## Test Setup

### Framework Configuration

- **Test Runner**: Vitest
- **Testing Library**: @testing-library/react
- **User Interaction**: @testing-library/user-event
- **Setup File**: `src/test/setup.ts`

### Basic Test Structure

```typescript
import { render, screen } from '@testing-library/react'
import { userEvent } from '@testing-library/user-event'
import { describe, it, expect, vi } from 'vitest'
import { Button } from './button'

describe('Button', () => {
  it('renders with the correct label', () => {
    render(<Button>Click me</Button>)
    expect(screen.getByText('Click me')).toBeInTheDocument()
  })
})
```

---

## Rendering Tests

### Basic Rendering

```typescript
it('renders children correctly', () => {
  render(<Badge>New</Badge>)
  expect(screen.getByText('New')).toBeInTheDocument()
})
```

### With Custom Props

```typescript
it('renders with custom className', () => {
  render(<Button className="custom-btn">Click me</Button>)
  const button = screen.getByRole('button')
  expect(button).toHaveClass('custom-btn')
})
```

### Custom Element Rendering (Polymorphic)

```typescript
it('renders as custom element when "as" prop is provided', () => {
  render(
    <Card as="section" data-testid="card">
      Content
    </Card>
  )
  const card = screen.getByTestId('card')
  expect(card.tagName.toLowerCase()).toBe('section')
})
```

### With Styles

```typescript
it('applies custom styles', () => {
  const style = { backgroundColor: '#000' }
  render(
    <Button data-testid="btn" styles={style}>
      Click me
    </Button>
  )
  const button = screen.getByTestId('btn')
  expect(button).toHaveStyle(style)
})
```

---

## Query Patterns

### Priority Order

Use queries in this priority order (per Testing Library best practices):

1. **Accessible by everyone**: `getByRole`, `getByLabelText`, `getByPlaceholderText`, `getByText`
2. **Semantic queries**: `getByAltText`, `getByTitle`
3. **Test IDs**: `getByTestId` (last resort)

### Common Queries

```typescript
// By role (preferred)
screen.getByRole('button')
screen.getByRole('button', { name: 'Submit' })
screen.getByRole('heading', { level: 2 })

// By text
screen.getByText('Click me')
screen.getByText(/click/i) // Case-insensitive regex

// By label
screen.getByLabelText('Email')

// By test ID (use sparingly)
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

### Click Events

```typescript
it('calls onClick handler when clicked', async () => {
  const handleClick = vi.fn()
  render(<Button onClick={handleClick}>Click me</Button>)

  const button = screen.getByRole('button')
  await userEvent.click(button)

  expect(handleClick).toHaveBeenCalledTimes(1)
})
```

### Keyboard Events

```typescript
it('activates on Enter key', async () => {
  const handleClick = vi.fn()
  render(<Button onClick={handleClick}>Click me</Button>)

  const button = screen.getByRole('button')
  button.focus()
  await userEvent.keyboard('{Enter}')

  expect(handleClick).toHaveBeenCalled()
})

it('activates on Space key', async () => {
  const handleClick = vi.fn()
  render(<Button onClick={handleClick}>Click me</Button>)

  const button = screen.getByRole('button')
  button.focus()
  await userEvent.keyboard(' ')

  expect(handleClick).toHaveBeenCalled()
})
```

### Pointer Events

```typescript
it('handles pointer down event', async () => {
  const handlePointerDown = vi.fn()
  render(<Button onPointerDown={handlePointerDown}>Click me</Button>)

  const button = screen.getByRole('button')
  await userEvent.pointer({ keys: '[MouseLeft>]', target: button })

  expect(handlePointerDown).toHaveBeenCalled()
})

it('handles hover events', async () => {
  const handlePointerOver = vi.fn()
  render(<Button onPointerOver={handlePointerOver}>Hover me</Button>)

  const button = screen.getByRole('button')
  await userEvent.hover(button)

  expect(handlePointerOver).toHaveBeenCalled()
})
```

### Form Events

```typescript
it('handles input change', async () => {
  const handleChange = vi.fn()
  render(<Input onChange={handleChange} />)

  const input = screen.getByRole('textbox')
  await userEvent.type(input, 'Hello')

  expect(input).toHaveValue('Hello')
  expect(handleChange).toHaveBeenCalledTimes(5) // Once per character
})
```

---

## State Testing

### Disabled State

```typescript
describe('disabled state', () => {
  it('has aria-disabled attribute when disabled', () => {
    render(<Button disabled>Click me</Button>)
    const button = screen.getByRole('button')
    expect(button).toHaveAttribute('aria-disabled', 'true')
  })

  it('does not call onClick when disabled', async () => {
    const handleClick = vi.fn()
    render(<Button disabled onClick={handleClick}>Click me</Button>)

    const button = screen.getByRole('button')
    await userEvent.click(button)

    expect(handleClick).not.toHaveBeenCalled()
  })
})
```

### Toggle State

```typescript
it('toggles checked state', async () => {
  const { rerender } = render(<Toggle checked={false} />)
  const toggle = screen.getByRole('switch')
  expect(toggle).toHaveAttribute('aria-checked', 'false')

  rerender(<Toggle checked={true} />)
  expect(toggle).toHaveAttribute('aria-checked', 'true')
})
```

---

## Accessibility Testing

### ARIA Attributes

```typescript
it('has correct ARIA attributes', () => {
  render(
    <Button aria-label="Close dialog" aria-describedby="hint">
      <Icon name="close" />
    </Button>
  )

  const button = screen.getByRole('button')
  expect(button).toHaveAttribute('aria-label', 'Close dialog')
  expect(button).toHaveAttribute('aria-describedby', 'hint')
})
```

### Keyboard Navigation

```typescript
it('is focusable with Tab key', async () => {
  render(<Button>Click me</Button>)

  const button = screen.getByRole('button')
  expect(button).not.toHaveFocus()

  await userEvent.tab()
  expect(button).toHaveFocus()
})
```

### Screen Reader Content

```typescript
it('includes screen reader only text', () => {
  render(
    <Link href="https://example.com" target="_blank">
      External Link
      <span className="sr-only">(opens in new tab)</span>
    </Link>
  )

  expect(screen.getByText(/opens in new tab/i)).toBeInTheDocument()
})
```

### Automated Accessibility Testing

```typescript
import { axe, toHaveNoViolations } from 'jest-axe'

expect.extend(toHaveNoViolations)

it('should not have accessibility violations', async () => {
  const { container } = render(<Button>Click me</Button>)
  const results = await axe(container)
  expect(results).toHaveNoViolations()
})
```

---

## Compound Component Testing

### Sub-Component Rendering

```typescript
describe('Card', () => {
  it('renders Card.Title component', () => {
    render(
      <Card>
        <Card.Title>Test Title</Card.Title>
      </Card>
    )
    expect(screen.getByText('Test Title')).toBeInTheDocument()
  })

  it('renders Card.Content component', () => {
    render(
      <Card>
        <Card.Content>Test Content</Card.Content>
      </Card>
    )
    expect(screen.getByText('Test Content')).toBeInTheDocument()
  })

  it('renders complete card with all sub-components', () => {
    render(
      <Card>
        <Card.Title>Title</Card.Title>
        <Card.Content>Content</Card.Content>
        <Card.Footer>Footer</Card.Footer>
      </Card>
    )

    expect(screen.getByText('Title')).toBeInTheDocument()
    expect(screen.getByText('Content')).toBeInTheDocument()
    expect(screen.getByText('Footer')).toBeInTheDocument()
  })
})
```

---

## Async Testing

### Waiting for Elements

```typescript
it('shows success message after submission', async () => {
  render(<Form />)

  const submitButton = screen.getByRole('button', { name: 'Submit' })
  await userEvent.click(submitButton)

  // Wait for success message to appear
  const successMessage = await screen.findByText('Form submitted successfully')
  expect(successMessage).toBeInTheDocument()
})
```

### Testing Loading States

```typescript
it('shows loading indicator while fetching', async () => {
  render(<DataComponent />)

  // Initially shows loading
  expect(screen.getByText('Loading...')).toBeInTheDocument()

  // Wait for data to load
  await waitFor(() => {
    expect(screen.queryByText('Loading...')).not.toBeInTheDocument()
  })

  // Data is displayed
  expect(screen.getByText('Data loaded')).toBeInTheDocument()
})
```

---

## Mock Functions

### Creating Mocks

```typescript
import { vi } from 'vitest'

// Mock function
const mockFn = vi.fn()

// Mock with return value
const mockFn = vi.fn(() => 'return value')

// Mock with implementation
const mockFn = vi.fn((x) => x * 2)
```

### Assertions

```typescript
expect(mockFn).toHaveBeenCalled()
expect(mockFn).toHaveBeenCalledTimes(3)
expect(mockFn).toHaveBeenCalledWith('arg1', 'arg2')
expect(mockFn).toHaveBeenLastCalledWith('last-arg')
expect(mockFn).toHaveReturnedWith('value')
```

---

## Snapshot Testing

### Basic Snapshot

```typescript
it('matches snapshot', () => {
  const { container } = render(<Button>Click me</Button>)
  expect(container).toMatchSnapshot()
})
```

### Inline Snapshots

```typescript
it('renders with correct text', () => {
  render(<Button>Click me</Button>)
  expect(screen.getByRole('button')).toMatchInlineSnapshot(`
    <button>
      Click me
    </button>
  `)
})
```

### Updating Snapshots

```bash
# Update all snapshots
npm run test:snapshot

# Update snapshots in watch mode
npm test -- -u
```

---

## Test Organization

### Describe Blocks

```typescript
describe('Button', () => {
  describe('rendering', () => {
    it('renders with text')
    it('renders with icon')
  })

  describe('interactions', () => {
    it('handles click events')
    it('handles keyboard events')
  })

  describe('accessibility', () => {
    it('has proper ARIA attributes')
    it('is keyboard navigable')
  })

  describe('states', () => {
    it('shows disabled state')
    it('shows loading state')
  })
})
```

### Test Naming

```typescript
// ✅ Good - descriptive and clear
it('calls onClick handler when clicked')
it('shows error message when validation fails')
it('disables submit button while loading')

// ❌ Bad - vague or redundant
it('works')
it('test button click')
it('should call onClick')  // "should" is redundant
```

---

## Common Testing Patterns

### Testing Conditional Rendering

```typescript
it('renders error message when error prop is provided', () => {
  const { rerender } = render(<Input />)
  expect(screen.queryByRole('alert')).not.toBeInTheDocument()

  rerender(<Input error="Invalid input" />)
  expect(screen.getByRole('alert')).toHaveTextContent('Invalid input')
})
```

### Testing Default Props

```typescript
it('uses default button type when not specified', () => {
  render(<Button>Click me</Button>)
  const button = screen.getByRole('button')
  expect(button).toHaveAttribute('type', 'button')
})
```

### Testing Component Composition

```typescript
it('accepts and renders custom children', () => {
  render(
    <Button>
      <Icon name="check" />
      <span>Submit</span>
    </Button>
  )

  expect(screen.getByText('Submit')).toBeInTheDocument()
  // Icon should also be present in the button
})
```

---

## Coverage Goals

- **Statements**: > 80%
- **Branches**: > 75%
- **Functions**: > 80%
- **Lines**: > 80%

### Running Coverage

```bash
# Run tests with coverage
npm run test:coverage

# View coverage report
open coverage/index.html
```

---

## Best Practices

### ✅ Do

- Test behavior, not implementation
- Use accessible queries (`getByRole`, `getByLabelText`)
- Test user interactions (click, type, tab)
- Test accessibility (ARIA attributes, keyboard navigation)
- Use descriptive test names
- Mock external dependencies
- Test error states and edge cases
- Keep tests focused and simple

### ❌ Don't

- Test implementation details
- Rely on internal component state
- Use `querySelector` or `getElementById` (use Testing Library queries)
- Test styling (use visual regression testing instead)
- Create overly complex test setups
- Share state between tests
- Test third-party libraries
- Skip accessibility testing

---

## Vitest Configuration

### Run Tests

```bash
# Run all tests
npm test

# Run in watch mode
npm test -- --watch

# Run specific file
npm test button.test.tsx

# Run with UI
npm run test:ui
```

### Test Filtering

```bash
# Run tests matching pattern
npm test -- button

# Run only tests with "renders" in the name
npm test -- -t renders
```

---

## Debugging Tests

### Print Component Output

```typescript
import { render, screen, debug } from '@testing-library/react'

it('debugs component', () => {
  render(<Button>Click me</Button>)
  screen.debug() // Prints component HTML to console
})
```

### Query Debugging

```typescript
// Show all available roles
screen.logTestingPlaygroundURL()

// Show what queries are available
screen.getByRole('') // Intentionally empty to see error with suggestions
```

---

## Resources

- [React Testing Library Docs](https://testing-library.com/docs/react-testing-library/intro/)
- [Vitest Docs](https://vitest.dev/)
- [Testing Library Cheatsheet](https://testing-library.com/docs/react-testing-library/cheatsheet)
- [Common Mistakes with Testing Library](https://kentcdodds.com/blog/common-mistakes-with-react-testing-library)
