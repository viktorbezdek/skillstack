# Coverage Targets and Validation

**When to consult**: Ensuring test completeness, coverage configuration, validation checklist

---

## Coverage Requirement: >90%

**Project standard**: ALL features must achieve >90% test coverage across:
- Lines
- Branches
- Functions
- Statements

**This is MANDATORY, not optional.**

---

## Vitest Coverage Configuration

**File**: `vitest.config.ts`

```typescript
import { defineConfig } from 'vitest/config'

export default defineConfig({
  test: {
    coverage: {
      provider: 'v8',
      reporter: ['text', 'json', 'html'],
      exclude: [
        'node_modules/',
        '.next/',
        'dist/',
        '**/*.config.ts',
        '**/*.d.ts',
      ],
      thresholds: {
        lines: 90,
        branches: 90,
        functions: 90,
        statements: 90,
      },
    },
    environment: 'jsdom', // For React component tests
    setupFiles: ['./src/test/setup.ts'],
  },
})
```

**Validate config exists BEFORE creating tests.**

---

## Running Coverage

```bash
# Run tests with coverage
npm run test:coverage

# Expected output during RED phase:
# Coverage: 0% (no implementation exists yet)

# After implementation (GREEN phase):
# Coverage: 95.2% ✅ (meets threshold)
```

---

## Coverage by Layer

### Entities Layer

**Target**: 100% (Pure validation, easy to cover)

```bash
# Check entities coverage
npm run test:coverage -- features/{feature}/entities.test.ts

# Should cover:
# - All schema validations
# - All error cases
# - All derived schemas (Create, Update, Query)
```

**If <100%**: Missing validation tests for some fields.

### Use Cases Layer

**Target**: >95% (Core business logic)

```bash
# Check use case coverage
npm run test:coverage -- features/{feature}/use-cases/

# Should cover:
# - Happy paths
# - All validation branches
# - All authorization paths
# - All business rule branches
# - All error handling paths
```

**If <95%**: Missing edge cases or error scenarios.

### Services Layer

**Target**: >90% (Data access)

```bash
# Check service coverage
npm run test:coverage -- features/{feature}/services/

# Should cover:
# - All CRUD operations
# - All query variations
# - Error handling
# - Data transformations
```

**If <90%**: Missing tests for some service methods.

### API Layer

**Target**: >90% (Controllers)

```bash
# Check API coverage
npm run test:coverage -- app/api/{feature}/

# Should cover:
# - All HTTP methods
# - All authentication paths
# - All validation scenarios
# - All authorization paths
# - All error responses
```

**If <90%**: Missing tests for some endpoints or error cases.

---

## Coverage Validation Checklist

### Phase 1: During Test Creation (RED)

- [ ] vitest.config.ts has coverage thresholds configured
- [ ] Coverage provider is 'v8'
- [ ] Coverage reporters include ['text', 'json', 'html']
- [ ] Thresholds set to 90% for all metrics
- [ ] Running `npm run test:coverage` shows 0% (expected - no implementation)

### Phase 2: After Implementation (GREEN)

- [ ] Entities: 100% coverage
- [ ] Use cases: >95% coverage
- [ ] Services: >90% coverage
- [ ] API routes: >90% coverage
- [ ] No coverage gaps in critical paths
- [ ] All error branches covered

### Phase 3: Coverage Report Analysis

```bash
# Generate HTML report
npm run test:coverage

# Open report
open coverage/index.html

# Check:
# - Red lines = Not covered
# - Yellow lines = Partially covered
# - Green lines = Fully covered
```

**Action**: Add tests for red/yellow lines until green.

---

## Common Coverage Gaps

### Gap 1: Uncovered Error Branches

```typescript
// Missing test for error case
try {
  await service.create(data)
} catch (error) {
  // This branch NOT covered ❌
  throw new Error('Failed to create')
}
```

**Fix**: Add test that throws error from service.

### Gap 2: Uncovered Default Cases

```typescript
// Missing test for default case
switch (type) {
  case 'A': return handleA()
  case 'B': return handleB()
  default: return handleDefault() // NOT covered ❌
}
```

**Fix**: Add test for unexpected type value.

### Gap 3: Uncovered Edge Cases

```typescript
// Missing test for empty array
if (items.length === 0) {
  return [] // NOT covered ❌
}
```

**Fix**: Add test with empty array.

---

## Coverage != Quality

**Important**: 100% coverage doesn't mean perfect tests.

**Good coverage includes**:
- All logical branches tested
- All error paths tested
- All edge cases tested
- Meaningful assertions

**Bad coverage**:
- Tests that don't assert anything
- Tests that mock everything
- Tests that test mocks, not logic

**Example of bad test**:
```typescript
it('calls service', async () => {
  mockService.create.mockResolvedValue({} as any)
  await createEntity(data, mockService)
  expect(mockService.create).toHaveBeenCalled() // Not testing logic!
})
```

**Example of good test**:
```typescript
it('validates input before calling service', async () => {
  await expect(
    createEntity(invalidData, mockService)
  ).rejects.toThrow('Validation failed')

  expect(mockService.create).not.toHaveBeenCalled() // Asserts behavior!
})
```

---

## Coverage Reports

### Text Reporter (Console)

```
------|---------|----------|---------|---------|-------------------
File  | % Stmts | % Branch | % Funcs | % Lines | Uncovered Line #s
------|---------|----------|---------|---------|-------------------
All   |   95.23 |    91.67 |   94.44 |   95.23 |
 entities.ts    | 100.00 |  100.00 |  100.00 | 100.00 |
 createTask.ts  |  96.67 |   92.86 |  100.00 |  96.67 | 45
 task.service.ts|  92.31 |   85.71 |   88.89 |  92.31 | 78,92
------|---------|----------|---------|---------|-------------------
```

**Red flags**: <90% in any column, many uncovered lines.

### HTML Reporter (Detailed)

- Shows exact lines not covered
- Highlights branches not taken
- Interactive exploration

**Use when**: Need to identify exact gaps.

---

## Validation Scripts

### verify-coverage-config.sh

```bash
#!/bin/bash
# Verify vitest.config.ts has correct thresholds

if ! grep -q "lines: 90" vitest.config.ts; then
  echo "❌ Coverage threshold for lines not set to 90%"
  exit 1
fi

if ! grep -q "provider: 'v8'" vitest.config.ts; then
  echo "❌ Coverage provider not set to v8"
  exit 1
fi

echo "✅ Coverage configuration valid"
```

### check-coverage-threshold.sh

```bash
#!/bin/bash
# Run tests and check if threshold is met

npm run test:coverage --silent

if [ $? -eq 0 ]; then
  echo "✅ Coverage thresholds met"
else
  echo "❌ Coverage below threshold"
  exit 1
fi
```

---

## Best Practices

1. **Configure thresholds BEFORE creating tests** - Prevent future surprises
2. **Aim for 95%+** - 90% is minimum, higher is better
3. **Review HTML report** - Find exact coverage gaps
4. **Test behavior, not implementation** - Coverage is means, not end
5. **Don't game coverage** - Meaningful tests only
6. **Update thresholds gradually** - Can increase as codebase matures

---

**Remember**: Coverage is a tool to find gaps, not a goal in itself.
