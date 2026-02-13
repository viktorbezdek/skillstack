# Component Composition Patterns for fpkit

This guide explains how to build components by composing existing fpkit components, following React best practices for reusability and maintainability.

## Table of Contents

- [Why Composition?](#why-composition)
- [Composition vs Creation Decision Tree](#composition-vs-creation-decision-tree)
- [Common Composition Patterns](#common-composition-patterns)
- [Anti-Patterns to Avoid](#anti-patterns-to-avoid)
- [Real-World Examples](#real-world-examples)

---

## Why Composition?

**Composition over duplication** is a core principle in React development. Benefits include:

- ✅ **Consistency**: Reusing existing components ensures UI consistency
- ✅ **Maintainability**: Bug fixes in base components propagate automatically
- ✅ **Reduced Code**: Less code to write, test, and maintain
- ✅ **Tested Components**: Leverage existing test coverage
- ✅ **Faster Development**: Build complex UIs from proven primitives

---

## Composition vs Creation Decision Tree

Use this decision tree to determine whether to compose, extend, or create new:

```
┌─────────────────────────────────────┐
│ Component Request: "ComponentName"  │
└──────────────┬──────────────────────┘
               │
               ▼
    ┌──────────────────────┐
    │ Does it already      │  YES → Extend existing component
    │ exist?               │        Add variant or prop
    └──────┬───────────────┘
           │ NO
           ▼
    ┌──────────────────────┐
    │ Can it be built by   │  YES → Compose existing components
    │ combining 2+ existing│        Import and combine
    │ components?          │
    └──────┬───────────────┘
           │ NO
           ▼
    ┌──────────────────────┐
    │ Does it share >50%   │  YES → Consider extending similar component
    │ behavior with        │        Or composing with modifications
    │ existing component?  │
    └──────┬───────────────┘
           │ NO
           ▼
    ┌──────────────────────┐
    │ Is it a UI primitive │  YES → Create new with UI base component
    │ (atom-level)?        │        Follow scaffold template
    └──────┬───────────────┘
           │ NO
           ▼
    ┌──────────────────────┐
    │ Create new compound  │
    │ component           │
    │ Compose from UI     │
    │ primitives          │
    └─────────────────────┘
```

---

## Common Composition Patterns

### Pattern 1: Container + Content

**When to use**: Wrapping existing components with additional structure or layout.

```tsx
import { Badge } from '../badge/badge'
import { Button } from '../buttons/button'

export const StatusButton = ({ status, children, ...props }) => {
  return (
    <Button {...props}>
      {children}
      <Badge variant={status}>{status}</Badge>
    </Button>
  )
}
```

**Examples**: IconButton, TaggedCard, LabeledInput

---

### Pattern 2: Conditional Composition

**When to use**: Different component combinations based on props or state.

```tsx
import { Alert } from '../alert/alert'
import { Modal } from '../modal/modal'
import { UI } from '#components/ui'

export const Notification = ({ variant, inline, children, ...props }) => {
  if (inline) {
    return <Alert variant={variant}>{children}</Alert>
  }

  return (
    <Modal {...props}>
      <Alert variant={variant}>{children}</Alert>
    </Modal>
  )
}
```

**Examples**: ResponsiveNav (mobile menu vs desktop nav), AdaptiveDialog

---

### Pattern 3: Enhanced Wrapper

**When to use**: Adding behavior/features around an existing component.

```tsx
import { Button } from '../buttons/button'
import { UI } from '#components/ui'
import { useState } from 'react'

export const LoadingButton = ({ loading, children, ...props }) => {
  const [isLoading, setIsLoading] = useState(loading)

  return (
    <Button {...props} disabled={isLoading || props.disabled}>
      {isLoading && <Spinner />}
      <span style={{ opacity: isLoading ? 0.5 : 1 }}>
        {children}
      </span>
    </Button>
  )
}
```

**Examples**: ConfirmButton, TooltipButton, LoadingButton

---

### Pattern 4: List of Components

**When to use**: Rendering multiple instances of the same component.

```tsx
import { Tag } from '../tag/tag'
import { UI } from '#components/ui'

export const TagList = ({ tags, onRemove, ...props }) => {
  return (
    <UI as="ul" data-tag-list {...props}>
      {tags.map((tag, index) => (
        <Tag
          key={tag.id || index}
          onClose={() => onRemove?.(tag)}
        >
          {tag.label}
        </Tag>
      ))}
    </UI>
  )
}
```

**Examples**: ButtonGroup, BadgeList, BreadcrumbTrail

---

### Pattern 5: Compound Component

**When to use**: Multiple related components that work together.

```tsx
import { Card, CardTitle, CardContent, CardFooter } from '../cards/card'
import { Button } from '../buttons/button'

export const ActionCard = ({ title, children, actions, ...props }) => {
  return (
    <Card {...props}>
      <CardTitle>{title}</CardTitle>
      <CardContent>{children}</CardContent>
      {actions && (
        <CardFooter>
          {actions.map((action, i) => (
            <Button key={i} {...action} />
          ))}
        </CardFooter>
      )}
    </Card>
  )
}
```

**Examples**: FormDialog, ArticleCard, ProductCard

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
        <ActualContent />
      </ContentWrapper>
    </InnerBox>
  </MiddleContainer>
</OuterWrapper>

// ✅ Good: Simplified structure
<Container>
  <Content />
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
    <Content theme={theme} size={size} variant={variant} />
  </Container>
</Wrapper>

// ✅ Good: Use context or reduce composition depth
const ThemeContext = createContext()

<ThemeProvider value={{ theme, size, variant }}>
  <Wrapper>
    <Container>
      <Content />
    </Container>
  </Wrapper>
</ThemeProvider>
```

**Rule**: If passing >3 props through >2 levels, consider context or refactoring.

---

### ❌ Anti-Pattern 3: Duplicating Instead of Composing

**Problem**: Copy-pasting component code instead of reusing existing components.

```tsx
// ❌ Bad: Duplicating Badge logic
export const Status = ({ variant, children }) => {
  return (
    <span className={`status status-${variant}`}>
      {children}
    </span>
  )
}

// ✅ Good: Reuse Badge component
import { Badge } from '../badge/badge'

export const Status = ({ variant, children }) => {
  return <Badge variant={variant}>{children}</Badge>
}
```

**Rule**: If code looks similar to existing component, reuse it.

---

### ❌ Anti-Pattern 4: Composing Incompatible Components

**Problem**: Forcing components together that weren't designed to work together.

```tsx
// ❌ Bad: Button inside Link creates nested interactive elements
<Link href="/page">
  <Button>Click me</Button>
</Link>

// ✅ Good: Use Button with as prop
<Button as="a" href="/page">Click me</Button>
```

**Rule**: Check component APIs for compatibility before composing.

---

## Real-World Examples

### Example 1: AlertDialog (Composition)

**Request**: "Create an AlertDialog component"

**Analysis**:
- "Alert" exists ✓
- "Dialog" exists ✓
- Can be composed from both

**Implementation**:

```tsx
import { Alert } from '../alert/alert'
import { Dialog } from '../dialog/dialog'

export const AlertDialog = ({ variant, title, children, ...props }) => {
  return (
    <Dialog {...props}>
      <Alert variant={variant}>
        {title && <strong>{title}</strong>}
        {children}
      </Alert>
    </Dialog>
  )
}
```

---

### Example 2: IconButton (Composition)

**Request**: "Create an IconButton component"

**Analysis**:
- "Button" exists ✓
- "Icon" exists ✓
- Can be composed

**Implementation**:

```tsx
import { Button } from '../buttons/button'
import { Icon } from '../icons/icon'

export const IconButton = ({ icon, children, iconPosition = 'left', ...props }) => {
  return (
    <Button {...props}>
      {iconPosition === 'left' && <Icon name={icon} />}
      {children}
      {iconPosition === 'right' && <Icon name={icon} />}
    </Button>
  )
}
```

---

### Example 3: TagInput (Compound Composition)

**Request**: "Create a TagInput component"

**Analysis**:
- "Tag" exists ✓
- "Input" exists ✓
- "List" pattern exists ✓
- Complex interaction → compose with custom logic

**Implementation**:

```tsx
import { Tag } from '../tag/tag'
import { UI } from '#components/ui'
import { useState } from 'react'

export const TagInput = ({ value = [], onChange, ...props }) => {
  const [inputValue, setInputValue] = useState('')

  const addTag = () => {
    if (inputValue.trim()) {
      onChange?.([...value, inputValue.trim()])
      setInputValue('')
    }
  }

  const removeTag = (index) => {
    onChange?.(value.filter((_, i) => i !== index))
  }

  return (
    <UI data-tag-input {...props}>
      <div className="tag-list">
        {value.map((tag, index) => (
          <Tag key={index} onClose={() => removeTag(index)}>
            {tag}
          </Tag>
        ))}
      </div>
      <input
        type="text"
        value={inputValue}
        onChange={(e) => setInputValue(e.target.value)}
        onKeyDown={(e) => e.key === 'Enter' && addTag()}
        placeholder="Add tag..."
      />
    </UI>
  )
}
```

---

## Guidelines Summary

| Scenario | Approach | Tools |
|----------|----------|-------|
| Component exists | Extend | Add variant/prop |
| 2+ components can be combined | Compose | scaffold --mode compose |
| Similar to existing | Review then compose/extend | Review code first |
| UI primitive needed | Scaffold new | scaffold --mode new |
| Compound component | Compose | Use multiple components |

---

## Next Steps

After composing a component:

1. ✅ **Document the composition** in JSDoc
2. ✅ **List all composed components** in the docs
3. ✅ **Create Storybook stories** showing both individual and composed usage
4. ✅ **Write integration tests** that test the composition, not just individual parts
5. ✅ **Add minimal styles** – reuse base component styles when possible
6. ✅ **Export properly** from index.ts

---

**Remember**: Composition is about smart reuse. Don't compose for the sake of it – compose when it creates clearer, more maintainable code.
