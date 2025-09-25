# Zod Schema Testing Patterns

**Source**: Context7 `/colinhacks/zod` + project patterns from `entity-design-patterns.md`

**When to consult**: Testing entities, schema validation

---

## Critical Rule: Use .safeParse() NEVER .parse()

```typescript
// ❌ WRONG - Throws error, harder to test
it('validates', () => {
  expect(() => schema.parse(invalidData)).toThrow()
})

// ✅ CORRECT - Returns result object
it('validates', () => {
  const result = schema.safeParse(invalidData)
  expect(result.success).toBe(false)
  if (!result.success) {
    expect(result.error.issues).toHaveLength(1)
    expect(result.error.issues[0].code).toBe('invalid_type')
  }
})
```

---

## Entity Schema Testing Structure

```typescript
import { describe, it, expect } from 'vitest'
import { EntitySchema, EntityCreateSchema, EntityUpdateSchema } from './entities'

describe('EntitySchema', () => {
  describe('valid data', () => {
    it('accepts valid complete entity', () => {
      const validEntity = {
        id: '550e8400-e29b-41d4-a716-446655440000',
        field1: 'Valid Value',
        userId: 'user-id',
        organizationId: 'org-id',
        createdAt: new Date(),
        updatedAt: new Date(),
      }

      const result = EntitySchema.safeParse(validEntity)

      expect(result.success).toBe(true)
      if (result.success) {
        expect(result.data).toEqual(validEntity)
      }
    })
  })

  describe('invalid data', () => {
    // Test EACH validation rule from PRD
  })
})
```

---

## Testing Validation Rules

### UUID Validation

```typescript
it('rejects invalid uuid', () => {
  const invalidEntity = { ...validData, id: 'not-a-uuid' }
  const result = EntitySchema.safeParse(invalidEntity)

  expect(result.success).toBe(false)
  if (!result.success) {
    expect(result.error.issues[0].code).toBe('invalid_string')
    expect(result.error.issues[0].validation).toBe('uuid')
    expect(result.error.issues[0].path).toEqual(['id'])
  }
})
```

### String Length Validation

```typescript
it('rejects string exceeding max length', () => {
  const invalidEntity = { ...validData, field1: 'x'.repeat(201) }
  const result = EntitySchema.safeParse(invalidEntity)

  expect(result.success).toBe(false)
  if (!result.success) {
    expect(result.error.issues[0].code).toBe('too_big')
    expect(result.error.issues[0].maximum).toBe(200)
  }
})

it('rejects string below min length', () => {
  const invalidEntity = { ...validData, field1: 'x' }
  const result = EntitySchema.safeParse(invalidEntity)

  expect(result.success).toBe(false)
  if (!result.success) {
    expect(result.error.issues[0].code).toBe('too_small')
    expect(result.error.issues[0].minimum).toBe(2)
  }
})
```

### Required Field Validation

```typescript
it('rejects missing required field', () => {
  const invalidEntity = { ...validData }
  delete invalidEntity.field1

  const result = EntitySchema.safeParse(invalidEntity)

  expect(result.success).toBe(false)
  if (!result.success) {
    expect(result.error.issues[0].code).toBe('invalid_type')
    expect(result.error.issues[0].path).toEqual(['field1'])
  }
})
```

### Enum Validation

```typescript
it('rejects invalid enum value', () => {
  const invalidEntity = { ...validData, status: 'invalid_status' }
  const result = EntitySchema.safeParse(invalidEntity)

  expect(result.success).toBe(false)
  if (!result.success) {
    expect(result.error.issues[0].code).toBe('invalid_enum_value')
  }
})
```

### Refinement Validation

```typescript
it('validates custom refinement rule', () => {
  const invalidEntity = { ...validData, customField: 'violates-rule' }
  const result = EntitySchema.safeParse(invalidEntity)

  expect(result.success).toBe(false)
  if (!result.success) {
    expect(result.error.issues[0].code).toBe('custom')
    expect(result.error.issues[0].message).toContain('expected message')
  }
})
```

---

## Testing Derived Schemas

### Create Schema (Omits Auto-Generated)

```typescript
describe('EntityCreateSchema', () => {
  it('accepts data without auto-generated fields', () => {
    const createData = {
      field1: 'Valid',
      userId: 'user-id',
      organizationId: 'org-id',
      // id, createdAt, updatedAt omitted
    }

    const result = EntityCreateSchema.safeParse(createData)
    expect(result.success).toBe(true)
  })

  it('rejects data with id field', () => {
    const createData = {
      id: 'should-not-be-here',
      field1: 'Valid',
    }

    const result = EntityCreateSchema.safeParse(createData)
    expect(result.success).toBe(false)
    if (!result.success) {
      expect(result.error.issues[0].code).toBe('unrecognized_keys')
    }
  })
})
```

### Update Schema (Partial)

```typescript
describe('EntityUpdateSchema', () => {
  it('accepts partial data', () => {
    const updateData = { field1: 'Updated' }
    const result = EntityUpdateSchema.safeParse(updateData)
    expect(result.success).toBe(true)
  })

  it('accepts empty object', () => {
    const result = EntityUpdateSchema.safeParse({})
    expect(result.success).toBe(true)
  })

  it('rejects protected fields', () => {
    const updateData = {
      userId: 'should-not-change',
      field1: 'Updated',
    }

    const result = EntityUpdateSchema.safeParse(updateData)
    expect(result.success).toBe(false)
  })
})
```

---

## Common Zod Issue Codes

- `invalid_type` - Wrong data type
- `too_small` / `too_big` - Length/value out of range
- `invalid_string` - String validation failed (email, uuid, url)
- `invalid_enum_value` - Value not in enum
- `unrecognized_keys` - Extra fields not in schema
- `custom` - Refinement/superRefine failed

---

## Testing Best Practices

1. **Always use .safeParse()** - Returns result object, easier to test
2. **Test both success and error branches** - Check result.success first
3. **Verify error codes and paths** - Ensure correct validation triggered
4. **Test ALL validation rules** - Every min, max, regex, refinement
5. **Test edge cases** - Empty strings, null, undefined, max lengths

---

**Latest patterns**: Query Context7 `/colinhacks/zod` for updates
