# Vitest Mocking Patterns

**Source**: Context7 `/vitest-dev/vitest` (topic: "mocking vi.mock vi.spyOn best practices")

**When to consult**: Creating unit/integration tests, mocking dependencies

---

## Core Mocking Strategies

### vi.mock() - Module-Level Mocking

**Use when**: Mocking entire modules or exported functions

```typescript
// Mock entire module
vi.mock('./example.js', () => ({
  method: vi.fn(),
  SomeClass: vi.fn()
}))

// Use in test
import { method } from './example.js'
method.mockReturnValue(42)
```

**Key points**:
- Hoisted to top of file automatically
- Replaces entire module exports
- Good for mocking use cases, services

### vi.spyOn() - Method-Level Spying

**Use when**: Tracking calls on existing objects/methods

```typescript
import * as exports from './example.js'

const spy = vi.spyOn(exports, 'method')
spy.mockImplementation(() => 'mocked')

expect(spy).toHaveBeenCalled()
```

**Key points**:
- Tracks calls while optionally changing behavior
- Can restore original implementation
- Good for partial mocking

### vi.fn() - Mock Functions

**Use when**: Creating mock callbacks or simple function mocks

```typescript
const mockCallback = vi.fn()
someFunction(mockCallback)

expect(mockCallback).toHaveBeenCalledWith(expectedArg)
expect(mockCallback).toHaveBeenCalledTimes(1)
```

---

## Supabase Client Mocking Pattern

**Critical for all service tests:**

```typescript
const createSupabaseMock = () => {
  const selectMock = vi.fn()
  const eqMock = vi.fn()
  const singleMock = vi.fn()

  const queryBuilder = {
    select: selectMock.mockReturnThis(),
    eq: eqMock.mockReturnThis(),
    single: singleMock.mockReturnThis(),
  }

  const supabase = {
    from: vi.fn(() => queryBuilder),
    auth: { getUser: vi.fn() },
  } as unknown as SupabaseClient

  return { supabase, mocks: { selectMock, eqMock, singleMock } }
}

// Usage
const { supabase, mocks } = createSupabaseMock()
mocks.singleMock.mockResolvedValue({ data: mockData, error: null })
```

---

## Mock Cleanup

**Always clean up between tests:**

```typescript
import { beforeEach, afterEach, vi } from 'vitest'

beforeEach(() => {
  // Setup fresh mocks
  vi.clearAllMocks()
})

afterEach(() => {
  // Restore originals if needed
  vi.restoreAllMocks()
})
```

---

## Common Patterns

### Pattern: Mock Implementation Once

```typescript
const spy = vi.spyOn(object, 'method')
spy.mockImplementationOnce(() => 'first call')
spy.mockImplementationOnce(() => 'second call')
```

### Pattern: Mock Constructor

```typescript
// MUST use function or class keyword (not arrow function)
vi.spyOn(cart, 'Apples')
  .mockImplementation(function () {
    this.getApples = () => 0
  })
  // OR
  .mockImplementation(class MockApples {
    getApples() { return 0 }
  })
```

### Pattern: Mock Return Values

```typescript
mockFunction.mockReturnValue(42)
mockFunction.mockResolvedValue(Promise.resolve(42))
mockFunction.mockRejectedValue(new Error('Failed'))
```

---

## Testing Best Practices

1. **Mock externals, not internals** - Mock at module boundaries
2. **Use mockReturnThis() for chaining** - Query builders need this
3. **Clear mocks between tests** - Prevent test pollution
4. **Verify mock calls** - Assert correct arguments passed
5. **Don't mock what you're testing** - Only mock dependencies

---

**Latest patterns**: Query Context7 `/vitest-dev/vitest` for updates
