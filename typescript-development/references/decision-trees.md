# TypeScript Decision Trees

This guide helps you make critical TypeScript decisions through clear decision trees and selection criteria.

## Type vs Interface

### Decision Tree

```
Need to define a shape for an object?
|
+- YES -> Is it a public API/library type?
|   |
|   +- YES -> Use `interface`
|   |   - Better error messages
|   |   - Declaration merging for extensibility
|   |   - Conventional for public APIs
|   |
|   +- NO -> Need union types or mapped types?
|       |
|       +- YES -> Use `type`
|       |   - Supports unions, intersections, mapped types
|       |   - More flexible type operations
|       |
|       +- NO -> Use `interface` (default for object shapes)
|           - Slightly better performance
|           - Can extend later if needed
|
+- NO -> Defining primitives, unions, or utilities?
    +- Use `type`
        - Required for non-object types
```

### When to Use `interface`

**Use `interface` when:**
- Defining public API contracts
- Building libraries or shared types
- Need declaration merging for extensibility
- Defining simple object shapes
- Want clearer error messages

```typescript
// Good: Public API
export interface User {
  id: string;
  email: string;
  role: UserRole;
}

// Good: Extensible via declaration merging
interface CustomWindow extends Window {
  myApp: AppInstance;
}

// Good: Clear object shape
interface UserConfig {
  theme: 'light' | 'dark';
  locale: string;
}
```

### When to Use `type`

**Use `type` when:**
- Need union or intersection types
- Using mapped types or conditional types
- Defining utility types
- Working with primitive types
- Creating type aliases

```typescript
// Good: Union types
type Status = 'pending' | 'success' | 'error';

// Good: Mapped types
type Readonly<T> = {
  readonly [K in keyof T]: T[K];
};

// Good: Conditional types
type ApiResponse<T> = T extends { error: any }
  ? { success: false; error: string }
  : { success: true; data: T };

// Good: Intersection types
type AuthenticatedUser = User & { token: string };
```

---

## Generics vs Union Types

### Decision Tree

```
Need to represent multiple possible types?
|
+- Types are related/similar and preserve structure?
|   |
|   +- YES -> Use Generics
|   |   - Type safety maintained
|   |   - Return type matches input type
|   |   - Reusable across different types
|   |
|   +- NO -> Fixed set of unrelated types?
|       +- Use Union Types
|           - Explicit allowed types
|           - No type parameter needed
|
+- Single operation accepts different inputs?
    |
    +- Input type determines output type -> Use Generics
    +- Output type is always same -> Use Union Types
```

### When to Use Generics

**Use generics when:**
- Function output type depends on input type
- Building reusable data structures
- Type relationships must be preserved
- Creating type-safe utilities

```typescript
// Good: Preserves type relationship
function identity<T>(value: T): T {
  return value;
}

const num = identity(42);        // Type: number
const str = identity("hello");   // Type: string

// Good: Type-safe data structure
class Stack<T> {
  private items: T[] = [];

  push(item: T): void {
    this.items.push(item);
  }

  pop(): T | undefined {
    return this.items.pop();
  }
}

// Good: Type-safe API wrapper
async function fetchData<T>(url: string): Promise<T> {
  const response = await fetch(url);
  return response.json();
}

const user = await fetchData<User>("/api/user");
```

### When to Use Union Types

**Use union types when:**
- Fixed set of known types
- Types are unrelated
- Exhaustive type checking needed
- Discriminated unions for state

```typescript
// Good: Fixed set of types
type StringOrNumber = string | number;

function formatValue(value: StringOrNumber): string {
  if (typeof value === "string") {
    return value.toUpperCase();
  }
  return value.toFixed(2);
}

// Good: Discriminated unions
type ApiResult<T> =
  | { success: true; data: T }
  | { success: false; error: string };

// Good: Known states
type LoadingState =
  | { status: 'idle' }
  | { status: 'loading' }
  | { status: 'success'; data: unknown }
  | { status: 'error'; error: string };
```

---

## `unknown` vs `any` Usage Guide

### Decision Tree

```
Dealing with external/unvalidated data?
|
+- YES -> Need type safety?
|   |
|   +- YES -> Use `unknown`
|   |   - Forces validation before use
|   |   - Type-safe
|   |   - Prevents runtime errors
|   |
|   +- NO -> Rapid prototyping/migration?
|       +- Use `any` (temporarily)
|           - Plan to replace with proper types
|           - Document why `any` is used
|
+- NO -> Writing type utilities?
    |
    +- Need to accept anything -> Use `unknown`
    +- Need to disable type checking -> Use `any` (rare)
```

### When to Use `unknown`

**Use `unknown` when:**
- Validating external data (APIs, user input)
- Don't know the type ahead of time
- Building type-safe utilities
- Replacing `any` for safety

```typescript
// Good: API response validation
async function fetchUser(id: string): Promise<User> {
  const response = await fetch(`/api/users/${id}`);
  const data: unknown = await response.json();

  // Must validate before use
  return UserSchema.parse(data); // Using Zod
}

// Good: Safe type guard
function isString(value: unknown): value is string {
  return typeof value === "string";
}

// Good: Error handling
try {
  someOperation();
} catch (error: unknown) {
  if (error instanceof Error) {
    console.error(error.message);
  } else {
    console.error("Unknown error:", error);
  }
}
```

### When to Use `any`

**Use `any` sparingly when:**
- Migrating JavaScript to TypeScript (temporarily)
- Interacting with poorly-typed libraries
- Rapid prototyping (document for later cleanup)
- Intentionally opting out of type checking (rare)

```typescript
// Acceptable: Migration phase
// TODO: Replace with proper types
function legacyFunction(input: any): any {
  // Complex logic being migrated
  return input.someMethod();
}
```

---

## Validation Library Choice

### Decision Tree

```
Need runtime validation for external data?
|
+- What's your primary use case?
|   |
|   +- Full-stack TypeScript with tRPC
|   |   +- Choose Zod
|   |       - Best tRPC integration
|   |       - Rich ecosystem
|   |       - Excellent DX
|   |
|   +- Need OpenAPI/JSON Schema
|   |   +- Choose TypeBox
|   |       - Generates JSON Schema
|   |       - ~10x faster than Zod
|   |       - Fastify integration
|   |
|   +- Edge/serverless functions
|   |   +- Choose Valibot
|   |       - Smallest bundle (~1.4kB)
|   |       - Tree-shakeable
|   |       - ~2x faster than Zod
|   |
|   +- General web apps, forms, APIs
|       +- Choose Zod (default)
|           - Most popular, mature
|           - Great error messages
|           - Rich ecosystem
|
+- NO -> Use TypeScript-only types
```

### Comparison Matrix

| Feature | Zod | TypeBox | Valibot |
|---------|-----|---------|---------|
| **Bundle Size** | ~13.5kB | ~8kB | ~1.4kB |
| **Performance** | Baseline | ~10x faster | ~2x faster |
| **JSON Schema** | No | Native | Via adapter |
| **tRPC Integration** | First-class | Custom | Custom |
| **Error Messages** | Excellent | Good | Good |
| **Tree-shaking** | Partial | Full | Full |
| **OpenAPI** | Via plugin | Native | No |
| **Ecosystem** | Large | Growing | Small |

---

## Type Narrowing Strategy Selection

### Decision Tree

```
Need to narrow a union type to specific case?
|
+- Discriminated union with literal `type` field?
|   +- Use Switch/If on discriminant
|       - Exhaustiveness checking
|       - Clearest intent
|
+- Checking primitive type?
|   +- Use `typeof` guard
|       - Built-in JavaScript
|
+- Checking class instance?
|   +- Use `instanceof` guard
|       - Prototype chain checking
|
+- Custom logic needed?
|   +- Use Type Predicate function
|       - Reusable
|       - Clear intent
|
+- Complex validation?
    +- Use Assertion Function
        - Throws on invalid
        - Acts as guard
```

### Discriminated Unions (Best Practice)

```typescript
type Shape =
  | { kind: "circle"; radius: number }
  | { kind: "rectangle"; width: number; height: number }
  | { kind: "square"; size: number };

function area(shape: Shape): number {
  switch (shape.kind) {
    case "circle":
      return Math.PI * shape.radius ** 2;
    case "rectangle":
      return shape.width * shape.height;
    case "square":
      return shape.size ** 2;
    default:
      // Exhaustiveness check
      const _exhaustive: never = shape;
      throw new Error(`Unhandled shape: ${_exhaustive}`);
  }
}
```

---

## Module Resolution Strategy

### Decision Tree

```
Starting new TypeScript project?
|
+- Node.js project (not bundler)?
|   |
|   +- Node.js 20.6+ (native ESM support)?
|   |   +- Use NodeNext
|   |       - Modern Node.js resolution
|   |       - ESM/CJS interop
|   |
|   +- Older Node.js or CommonJS project?
|       +- Use Node16 or Node
|           - Traditional Node.js resolution
|
+- Bundler (Vite, Webpack, esbuild)?
|   +- Use Bundler
|       - Simplified resolution
|       - Trusts bundler
|
+- Library/Package?
    +- Use NodeNext + "type": "module"
        - Modern package standard
        - Best compatibility
```

### Recommended Settings (2025)

**New Node.js projects:**
```json
{
  "compilerOptions": {
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "verbatimModuleSyntax": true
  }
}
```

**Bundler projects (Vite, Webpack):**
```json
{
  "compilerOptions": {
    "module": "ESNext",
    "moduleResolution": "Bundler",
    "verbatimModuleSyntax": true
  }
}
```

---

## Decision Checklist

Before making TypeScript choices, ask:

1. **Is this a public API?** -> Prefer `interface` over `type`
2. **Do I need type relationships?** -> Use generics, not unions
3. **Is this external data?** -> Use `unknown`, not `any`
4. **Need runtime validation?** -> Choose validation library based on use case
5. **Is this a discriminated union?** -> Use switch on discriminant
6. **What's my module system?** -> Choose appropriate resolution strategy

---

## Related References

- **[Advanced Types](./advanced-types.md)** - Conditional types, mapped types, recursive types
- **[Configuration](./configuration.md)** - Complete tsconfig.json guide
- **[Runtime Validation](./runtime-validation.md)** - Deep dive into Zod, TypeBox, Valibot
- **[Troubleshooting](./troubleshooting.md)** - Common TypeScript issues and fixes
