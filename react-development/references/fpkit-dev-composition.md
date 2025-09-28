# Component Composition Guide

This guide explains how to build custom components by composing existing @fpkit/acss components, following React best practices for reusability and maintainability.

## Table of Contents

- [Why Composition?](#why-composition)
- [Composition vs Creation Decision Tree](#composition-vs-creation-decision-tree)
- [Common Composition Patterns](#common-composition-patterns)
- [Anti-Patterns to Avoid](#anti-patterns-to-avoid)
- [Real-World Examples](#real-world-examples)

---

## Why Composition?

**Composition over duplication** is a core principle in React development. When building custom components using @fpkit/acss, you should prefer composing existing components rather than creating from scratch.

### Benefits

- ✅ **Consistency**: Reusing existing components ensures UI consistency across your application
- ✅ **Maintainability**: Bug fixes and improvements in fpkit components propagate to your composed components automatically
- ✅ **Reduced Code**: Less code to write, test, and maintain
- ✅ **Tested Components**: Leverage existing test coverage from fpkit
- ✅ **Faster Development**: Build complex UIs from proven primitives
- ✅ **Accessibility**: Inherit WCAG-compliant patterns from fpkit components

---

## Composition vs Creation Decision Tree

Use this decision tree to determine whether to compose, extend, or create new:

```
┌─────────────────────────────────────┐
│ New Component Need: "ComponentName" │
└──────────────┬──────────────────────┘
               │
               ▼
    ┌──────────────────────┐
    │ Does fpkit have a    │  YES → Use fpkit component directly
    │ component that meets │        Customize with CSS variables
    │ the need exactly?    │
    └──────┬───────────────┘
           │ NO
           ▼
    ┌──────────────────────┐
    │ Can it be built by   │  YES → Compose existing components
    │ combining 2+ fpkit   │        Import and combine
    │ components?          │
    └──────┬───────────────┘
           │ NO
           ▼
    ┌──────────────────────┐
    │ Can I extend an      │  YES → Wrap fpkit component
    │ fpkit component with │        Add custom logic/styling
    │ additional features? │
    └──────┬───────────────┘
           │ NO
           ▼
    ┌──────────────────────┐
    │ Create custom        │
    │ component from       │
    │ scratch using fpkit  │
    │ styling patterns     │
    └─────────────────────┘
```

---

## Common Composition Patterns

### Pattern 1: Container + Content

**When to use**: Wrapping fpkit components with additional structure or layout.

```tsx
import { Badge, Button } from '@fpkit/acss'

export const StatusButton = ({ status, children, ...props }) => {
  return (
    <Button {...props}>
      {children}
      <Badge variant={status}>{status}</Badge>
    </Button>
  )
}

// Usage
<StatusButton status="success">Complete</StatusButton>
```

**Use Cases**: IconButton, TaggedCard, LabeledInput, NotificationButton

---

### Pattern 2: Conditional Composition

**When to use**: Different component combinations based on props or state.

```tsx
import { Alert, Modal } from '@fpkit/acss'

export const Notification = ({ variant, inline, children, onClose, ...props }) => {
  if (inline) {
    return (
      <Alert variant={variant} onClose={onClose}>
        {children}
      </Alert>
    )
  }

  return (
    <Modal isOpen={props.isOpen} onClose={onClose}>
      <Alert variant={variant}>{children}</Alert>
    </Modal>
  )
}

// Usage
<Notification inline variant="success">Saved!</Notification>
<Notification isOpen={showModal} variant="error" onClose={handleClose}>
  Error occurred
</Notification>
```

**Use Cases**: ResponsiveNav (mobile menu vs desktop nav), AdaptiveDialog, ConditionalAlert

---

### Pattern 3: Enhanced Wrapper

**When to use**: Adding behavior/features around an existing fpkit component.

```tsx
import { Button } from '@fpkit/acss'
import { useState } from 'react'

export const LoadingButton = ({ loading, onClick, children, ...props }) => {
  const [isLoading, setIsLoading] = useState(loading)

  const handleClick = async (e) => {
    setIsLoading(true)
    try {
      await onClick?.(e)
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <Button {...props} disabled={isLoading || props.disabled} onClick={handleClick}>
      {isLoading && <span aria-label="Loading">⏳</span>}
      <span style={{ opacity: isLoading ? 0.6 : 1 }}>{children}</span>
    </Button>
  )
}

// Usage
<LoadingButton onClick={handleSubmit}>Submit Form</LoadingButton>
```

**Accessibility Note**: fpkit Button uses `aria-disabled` instead of native `disabled`, which means:
- ✅ Disabled buttons stay in tab order (better for screen readers)
- ✅ onClick is automatically prevented when disabled
- ✅ Automatic `.is-disabled` className applied
- ✅ Focus management maintained

**Use Cases**: ConfirmButton, TooltipButton, LoadingButton, DebounceInput

---

### Pattern 4: List of Components

**When to use**: Rendering multiple instances of the same fpkit component.

```tsx
import { Tag } from '@fpkit/acss'

export const TagList = ({ tags, onRemove, ...props }) => {
  return (
    <div className="tag-list" {...props}>
      {tags.map((tag) => (
        <Tag
          key={tag.id}
          onClose={onRemove ? () => onRemove(tag) : undefined}
        >
          {tag.label}
        </Tag>
      ))}
    </div>
  )
}

// Usage
<TagList
  tags={[
    { id: 1, label: 'React' },
    { id: 2, label: 'TypeScript' },
  ]}
  onRemove={handleRemoveTag}
/>
```

**Use Cases**: ButtonGroup, BadgeList, BreadcrumbTrail, PillGroup

---

### Pattern 5: Compound Component

**When to use**: Multiple related fpkit components that work together.

```tsx
import { Card, Button } from '@fpkit/acss'

export const ActionCard = ({ title, children, actions, ...props }) => {
  return (
    <Card {...props}>
      <Card.Header>
        <Card.Title>{title}</Card.Title>
      </Card.Header>
      <Card.Content>{children}</Card.Content>
      {actions && (
        <Card.Footer>
          {actions.map((action, i) => (
            <Button key={i} {...action} />
          ))}
        </Card.Footer>
      )}
    </Card>
  )
}

// Usage
<ActionCard
  title="Confirm Action"
  actions={[
    { children: 'Cancel', variant: 'secondary', onClick: handleCancel },
    { children: 'Confirm', variant: 'primary', onClick: handleConfirm },
  ]}
>
  Are you sure you want to proceed?
</ActionCard>
```

**Use Cases**: FormDialog, ArticleCard, ProductCard, SettingsSection

---

## Anti-Patterns to Avoid

### ❌ Anti-Pattern 1: Over-Composition

**Problem**: Too many nested layers make the component hard to understand and debug.

```tsx
// ❌ Bad: Too many wrappers
<OuterWrapper>
  <MiddleContainer>
    <InnerBox>
      <ContentWrapper>
        <Button>Click</Button>
      </ContentWrapper>
    </InnerBox>
  </MiddleContainer>
</OuterWrapper>

// ✅ Good: Simplified structure
<Container>
  <Button>Click</Button>
</Container>
```

**Rule**: Keep composition depth ≤ 3 levels when possible.

---

### ❌ Anti-Pattern 2: Prop Drilling Through Composition

**Problem**: Passing props through multiple layers of composed components.

```tsx
// ❌ Bad: Props passed through many layers
<Wrapper theme={theme} size={size} variant={variant}>
  <Container theme={theme} size={size}>
    <Button theme={theme} size={size} variant={variant} />
  </Container>
</Wrapper>

// ✅ Good: Use context or reduce composition depth
const ThemeContext = createContext()

<ThemeProvider value={{ theme, size, variant }}>
  <Wrapper>
    <Container>
      <Button />
    </Container>
  </Wrapper>
</ThemeProvider>
```

**Rule**: If passing >3 props through >2 levels, consider context or refactoring.

---

### ❌ Anti-Pattern 3: Duplicating Instead of Composing

**Problem**: Copy-pasting component logic instead of reusing fpkit components.

```tsx
// ❌ Bad: Duplicating Badge logic
export const Status = ({ variant, children }) => {
  return (
    <span className={`status status-${variant}`}>
      {children}
    </span>
  )
}

// ✅ Good: Reuse fpkit Badge component
import { Badge } from '@fpkit/acss'

export const Status = ({ variant, children }) => {
  return <Badge variant={variant}>{children}</Badge>
}
```

**Rule**: If your code looks similar to an fpkit component, reuse that component instead.

---

### ❌ Anti-Pattern 4: Composing Incompatible Components

**Problem**: Forcing components together that create accessibility or semantic issues.

```tsx
// ❌ Bad: Button inside Link creates nested interactive elements (a11y violation)
import { Button, Link } from '@fpkit/acss'

<Link href="/page">
  <Button>Click me</Button>
</Link>

// ✅ Good: Use Button with polymorphic 'as' prop
<Button as="a" href="/page">
  Click me
</Button>
```

**Rule**: Check component APIs for polymorphic props (`as`) and compatibility before composing.

---

## Real-World Examples

### Example 1: AlertDialog (Composition)

**Need**: "Create an AlertDialog component that shows alerts in a modal"

**Analysis**:
- fpkit has `Alert` component ✓
- fpkit has `Dialog` component ✓
- Can be composed from both

**Implementation**:

```tsx
import { Alert, Dialog } from '@fpkit/acss'

export const AlertDialog = ({ variant, title, children, ...dialogProps }) => {
  return (
    <Dialog {...dialogProps}>
      <Alert variant={variant}>
        {title && <strong>{title}</strong>}
        {children}
      </Alert>
    </Dialog>
  )
}

// Usage
<AlertDialog
  isOpen={showDialog}
  onClose={handleClose}
  variant="error"
  title="Error"
>
  An error occurred. Please try again.
</AlertDialog>
```

---

### Example 2: IconButton (Composition)

**Need**: "Create an IconButton component with text and icon"

**Analysis**:
- fpkit has `Button` component ✓
- Icons can be added as children ✓
- Can be composed

**Implementation**:

```tsx
import { Button } from '@fpkit/acss'

export const IconButton = ({ icon, children, iconPosition = 'left', ...props }) => {
  return (
    <Button {...props}>
      {iconPosition === 'left' && <span className="icon">{icon}</span>}
      {children}
      {iconPosition === 'right' && <span className="icon">{icon}</span>}
    </Button>
  )
}

// Usage
<IconButton icon="💾" variant="primary">
  Save Changes
</IconButton>

<IconButton icon="→" iconPosition="right" variant="secondary">
  Next
</IconButton>
```

---

### Example 3: TagInput (Compound Composition)

**Need**: "Create a TagInput component that allows adding/removing tags"

**Analysis**:
- fpkit has `Tag` component ✓
- Standard `input` element for text entry
- Complex interaction → compose with custom logic

**Implementation**:

```tsx
import { Tag } from '@fpkit/acss'
import { useState } from 'react'

export const TagInput = ({ value = [], onChange, placeholder, ...props }) => {
  const [inputValue, setInputValue] = useState('')

  const addTag = () => {
    if (inputValue.trim() && !value.includes(inputValue.trim())) {
      onChange?.([...value, inputValue.trim()])
      setInputValue('')
    }
  }

  const removeTag = (tagToRemove) => {
    onChange?.(value.filter((tag) => tag !== tagToRemove))
  }

  return (
    <div className="tag-input" {...props}>
      <div className="tag-list">
        {value.map((tag) => (
          <Tag key={tag} onClose={() => removeTag(tag)}>
            {tag}
          </Tag>
        ))}
      </div>
      <input
        type="text"
        value={inputValue}
        onChange={(e) => setInputValue(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === 'Enter') {
            e.preventDefault()
            addTag()
          }
        }}
        placeholder={placeholder || 'Add tag...'}
      />
    </div>
  )
}

// Usage
<TagInput
  value={tags}
  onChange={setTags}
  placeholder="Add technology..."
/>
```

---

### Example 4: ConfirmButton (Enhanced Wrapper)

**Need**: "Button that requires confirmation before executing action"

**Implementation**:

```tsx
import { Button, Dialog } from '@fpkit/acss'
import { useState } from 'react'

export const ConfirmButton = ({
  confirmTitle = 'Confirm Action',
  confirmMessage = 'Are you sure?',
  onConfirm,
  children,
  ...props
}) => {
  const [showConfirm, setShowConfirm] = useState(false)

  const handleConfirm = () => {
    setShowConfirm(false)
    onConfirm?.()
  }

  return (
    <>
      <Button {...props} onClick={() => setShowConfirm(true)}>
        {children}
      </Button>

      <Dialog isOpen={showConfirm} onClose={() => setShowConfirm(false)}>
        <h2>{confirmTitle}</h2>
        <p>{confirmMessage}</p>
        <div className="dialog-actions">
          <Button variant="secondary" onClick={() => setShowConfirm(false)}>
            Cancel
          </Button>
          <Button variant="primary" onClick={handleConfirm}>
            Confirm
          </Button>
        </div>
      </Dialog>
    </>
  )
}

// Usage
<ConfirmButton
  variant="danger"
  confirmTitle="Delete Account"
  confirmMessage="This action cannot be undone. Are you sure?"
  onConfirm={handleDeleteAccount}
>
  Delete Account
</ConfirmButton>
```

---

## Styling Composed Components

When composing fpkit components, you can customize styles using CSS variables:

```tsx
import { Button, Badge } from '@fpkit/acss'

export const PriorityButton = ({ priority, children, ...props }) => {
  return (
    <Button
      {...props}
      style={{
        '--btn-padding-inline': '2rem',
        '--btn-gap': '0.75rem',
      }}
    >
      {children}
      <Badge
        variant={priority === 'high' ? 'error' : 'default'}
        style={{
          '--badge-fs': '0.75rem',
        }}
      >
        {priority}
      </Badge>
    </Button>
  )
}
```

See the [CSS Variables Guide](./css-variables.md) for complete customization options.

---

## TypeScript Support

fpkit components are fully typed. When composing, preserve type safety:

```tsx
import { Button, ButtonProps } from '@fpkit/acss'
import { ReactNode } from 'react'

interface LoadingButtonProps extends ButtonProps {
  loading?: boolean
  loadingText?: ReactNode
}

export const LoadingButton = ({
  loading,
  loadingText = 'Loading...',
  children,
  ...props
}: LoadingButtonProps) => {
  return (
    <Button {...props} disabled={loading || props.disabled}>
      {loading ? loadingText : children}
    </Button>
  )
}
```

**Key Points:**
- **Extend ButtonProps**: Inherits all Button props including `disabled`, `onClick`, `aria-*`, etc.
- **Spread ...props**: Preserves fpkit's `aria-disabled` pattern and accessibility features
- **Type safety**: TypeScript ensures you can't pass invalid props to the Button

---

## Testing Composed Components

When testing compositions, focus on integration rather than unit testing fpkit components (they're already tested):

```tsx
import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { TagInput } from './tag-input'

describe('TagInput', () => {
  it('adds tag on Enter key', async () => {
    const handleChange = vi.fn()
    render(<TagInput value={[]} onChange={handleChange} />)

    const input = screen.getByPlaceholderText('Add tag...')
    await userEvent.type(input, 'React{Enter}')

    expect(handleChange).toHaveBeenCalledWith(['React'])
  })

  it('removes tag on close', async () => {
    const handleChange = vi.fn()
    render(<TagInput value={['React']} onChange={handleChange} />)

    const closeButton = screen.getByRole('button', { name: /close/i })
    await userEvent.click(closeButton)

    expect(handleChange).toHaveBeenCalledWith([])
  })
})
```

See the [Testing Guide](./testing.md) for more patterns.

---

## Guidelines Summary

| Scenario | Approach | Strategy |
|----------|----------|----------|
| Exact match exists | Use directly | Customize with CSS variables |
| 2+ components can be combined | Compose | Import and combine |
| Similar to existing | Wrap/extend | Add custom logic around fpkit component |
| Needs custom UI | Create from scratch | Follow fpkit styling patterns |
| Complex multi-part UI | Compound composition | Use multiple related components |

---

## Best Practices

### ✅ Do

- **Start with fpkit components** - Check what exists before building custom
- **Preserve accessibility** - Keep ARIA attributes and keyboard navigation from fpkit components
- **Use CSS variables** - Customize appearance without modifying component structure
- **Document composition** - Note which fpkit components are used in JSDoc comments
- **Test integration** - Focus tests on how composed parts work together
- **Export cleanly** - Re-export composed components from a single file

### ❌ Don't

- **Don't duplicate fpkit logic** - If it exists in fpkit, reuse it
- **Don't break accessibility** - Nested interactive elements, missing ARIA attributes
- **Don't over-compose** - Keep composition depth reasonable (≤3 levels)
- **Don't prop drill** - Use context or reduce composition depth
- **Don't ignore polymorphism** - Use `as` prop instead of wrapping

---

## Next Steps

- **[CSS Variables Guide](./css-variables.md)** - Learn how to customize fpkit components
- **[Accessibility Guide](./accessibility.md)** - Ensure compositions remain accessible
- **[Architecture Guide](./architecture.md)** - Understand fpkit component patterns
- **[Testing Guide](./testing.md)** - Learn testing strategies for composed components

---

**Remember**: Composition is about smart reuse. Don't compose for the sake of it – compose when it creates clearer, more maintainable code that leverages the tested, accessible primitives from @fpkit/acss.
