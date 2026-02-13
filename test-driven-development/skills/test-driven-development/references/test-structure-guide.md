# Test Structure and Organization Guide

**When to consult**: Organizing test suites, naming conventions, Arrange-Act-Assert pattern

---

## Arrange-Act-Assert Pattern

**Structure EVERY test with clear sections:**

```typescript
it('creates entity with valid data', async () => {
  // Arrange - Setup
  const createData = { field1: 'Test Value' }
  const expectedEntity = { id: 'uuid', ...createData }
  mockService.create.mockResolvedValue(expectedEntity)

  // Act - Execute
  const result = await createEntity(createData, mockService)

  // Assert - Verify
  expect(result).toEqual(expectedEntity)
  expect(mockService.create).toHaveBeenCalledWith(createData)
  expect(mockService.create).toHaveBeenCalledTimes(1)
})
```

**Why**: Clear separation makes tests readable and maintainable.

---

## Test Naming Conventions

### Descriptive Test Names

```typescript
// ❌ WRONG - Vague
it('works', () => {})
it('test 1', () => {})

// ✅ CORRECT - Specific, describes behavior
it('creates entity with valid data', () => {})
it('rejects creation with missing required field', () => {})
it('allows admin to update any entity in organization', () => {})
```

**Formula**: `should [action] [context/condition]`

### Describe Block Organization

```typescript
describe('createEntity', () => {
  describe('happy path', () => {
    it('creates entity with valid data', () => {})
    it('returns created entity with generated id', () => {})
  })

  describe('validation', () => {
    it('rejects invalid data', () => {})
    it('rejects missing required field', () => {})
  })

  describe('authorization', () => {
    it('allows creation in own organization', () => {})
    it('rejects unauthorized access', () => {})
  })

  describe('business rules', () => {
    it('enforces unique constraint', () => {})
    it('applies default values', () => {})
  })

  describe('error handling', () => {
    it('handles database errors', () => {})
    it('handles unexpected errors', () => {})
  })

  describe('edge cases', () => {
    it('handles unicode characters', () => {})
    it('handles maximum length strings', () => {})
  })
})
```

**Benefits**: Tests are organized by concern, easy to navigate.

---

## One Concern Per Test

```typescript
// ❌ WRONG - Testing multiple concerns
it('creates and validates entity', async () => {
  const result = await createEntity(validData)
  expect(result).toBeDefined()

  await expect(createEntity(invalidData)).rejects.toThrow()
})

// ✅ CORRECT - Separate tests for separate concerns
it('creates entity with valid data', async () => {
  const result = await createEntity(validData)
  expect(result).toBeDefined()
})

it('rejects invalid data', async () => {
  await expect(createEntity(invalidData)).rejects.toThrow()
})
```

**Why**: Failed test clearly identifies the problem.

---

## Test File Organization

### File Structure

```
features/
└── tasks/
    ├── entities.ts
    ├── entities.test.ts           # ← Entity validation tests
    ├── use-cases/
    │   ├── createTask.ts
    │   ├── createTask.test.ts      # ← Use case tests
    │   ├── getTask.ts
    │   └── getTask.test.ts
    ├── services/
    │   ├── task.service.ts
    │   └── task.service.test.ts    # ← Service tests
    └── components/
        └── TaskForm.test.tsx        # ← Component tests (if needed)
```

**Rule**: Test file lives next to implementation file with `.test.ts` suffix.

### Test Imports

```typescript
// ✅ CORRECT - Clear imports
import { describe, it, expect, vi, beforeEach } from 'vitest'
import { createTask } from './createTask'
import type { TaskService } from '../services/task.service'

// Mock dependencies
vi.mock('../services/task.service')
```

---

## Lifecycle Hooks

```typescript
describe('createTask', () => {
  let mockService: jest.Mocked<TaskService>

  // Runs BEFORE ALL tests in this describe block
  beforeAll(() => {
    // One-time setup (rarely needed)
  })

  // Runs BEFORE EACH test
  beforeEach(() => {
    // Fresh mock for each test
    mockService = {
      create: vi.fn(),
      getById: vi.fn(),
    }
    vi.clearAllMocks()
  })

  // Runs AFTER EACH test
  afterEach(() => {
    // Cleanup if needed
  })

  // Runs AFTER ALL tests
  afterAll(() => {
    // Final cleanup (rarely needed)
  })
})
```

**Best practice**: Use `beforeEach` for mock setup, keeps tests isolated.

---

## Assertion Patterns

### Equality Assertions

```typescript
// Exact equality
expect(result).toBe(42)
expect(result).toEqual({ id: 'uuid', name: 'Test' })

// Partial matching
expect(result).toEqual(expect.objectContaining({
  id: expect.any(String),
  name: 'Test',
}))

// Array assertions
expect(result).toHaveLength(3)
expect(result).toContain(item)
```

### Mock Assertions

```typescript
// Call count
expect(mockFn).toHaveBeenCalled()
expect(mockFn).toHaveBeenCalledTimes(1)
expect(mockFn).not.toHaveBeenCalled()

// Call arguments
expect(mockFn).toHaveBeenCalledWith(arg1, arg2)
expect(mockFn).toHaveBeenLastCalledWith(arg1)

// Return values
expect(mockFn).toHaveReturned()
expect(mockFn).toHaveReturnedWith(value)
```

### Async Assertions

```typescript
// Promise resolution
await expect(promise).resolves.toBe(value)
await expect(promise).resolves.toEqual(object)

// Promise rejection
await expect(promise).rejects.toThrow()
await expect(promise).rejects.toThrow('specific error')
await expect(promise).rejects.toThrow(ErrorClass)
```

---

## Common Anti-Patterns

### Too Many Assertions

```typescript
// ❌ WRONG - Hard to debug which assertion failed
it('creates and validates entity', () => {
  expect(result.id).toBeDefined()
  expect(result.name).toBe('Test')
  expect(result.userId).toBe('user-123')
  expect(result.createdAt).toBeInstanceOf(Date)
  expect(mockService.create).toHaveBeenCalled()
  expect(mockService.create).toHaveBeenCalledWith(data)
})

// ✅ CORRECT - Focused assertion
it('creates entity with valid data', () => {
  expect(result).toEqual(expect.objectContaining({
    id: expect.any(String),
    name: 'Test',
    userId: 'user-123',
  }))
})

it('calls service with correct data', () => {
  expect(mockService.create).toHaveBeenCalledWith(data)
})
```

### Shared State Between Tests

```typescript
// ❌ WRONG - Tests depend on each other
let createdId: string

it('creates entity', () => {
  createdId = result.id
})

it('retrieves entity', () => {
  const result = await getEntity(createdId) // Depends on previous test!
})

// ✅ CORRECT - Each test is independent
it('creates entity', () => {
  const result = await createEntity(data)
  expect(result.id).toBeDefined()
})

it('retrieves entity', () => {
  const mockId = 'test-id'
  const result = await getEntity(mockId)
  expect(result.id).toBe(mockId)
})
```

---

## Test Coverage Organization

```typescript
// Complete coverage template for use cases
describe('createEntity', () => {
  describe('happy path', () => {
    // Success scenarios
  })

  describe('validation', () => {
    // Input validation tests
  })

  describe('authorization', () => {
    // Permission tests
  })

  describe('business rules', () => {
    // Domain logic tests
  })

  describe('error handling', () => {
    // Error scenarios
  })

  describe('edge cases', () => {
    // Boundary conditions
  })
})
```

**Goal**: >90% coverage across all scenarios.

---

## Best Practices Summary

1. **Use Arrange-Act-Assert** - Clear test structure
2. **Descriptive names** - Tests document behavior
3. **One concern per test** - Easy to debug
4. **Organize with describe blocks** - Logical grouping
5. **Mock in beforeEach** - Fresh mocks per test
6. **Assert specific behaviors** - Not implementation details
7. **Keep tests isolated** - No shared state
8. **Focus assertions** - One logical assertion per test

---

**Your tests are documentation** - Make them readable and maintainable.
