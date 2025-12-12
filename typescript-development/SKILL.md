---
name: typescript-development
description: Comprehensive TypeScript development skill covering type system mastery, runtime validation (Zod, TypeBox, Valibot), framework integration (React 19, Next.js 16, NestJS, React Native), architecture patterns (Clean Architecture, DI, repository patterns), security, tsconfig optimization, and testing strategies. Use when writing TypeScript code, designing type-safe APIs, configuring TypeScript projects, implementing advanced generics, or auditing TypeScript code quality.
---

# TypeScript Development - Comprehensive Skill

A complete TypeScript development skill combining best practices, patterns, and tooling for modern TypeScript development across all application types.

## Overview

This merged skill provides comprehensive TypeScript guidance covering:
- **Type System Mastery**: Advanced types, generics, conditional types, mapped types, template literals
- **Runtime Validation**: Zod, TypeBox, Valibot patterns and comparisons
- **Framework Integration**: React 19, Next.js 16, NestJS, React Native
- **Architecture Patterns**: Clean Architecture, dependency injection, repository patterns
- **Security**: Type-safe validation, branded types, sensitive data handling
- **Configuration**: tsconfig.json optimization, module resolution, strict mode
- **Testing**: Unit testing with mocks, integration testing strategies

## Core TypeScript Principles

### Strict Mode Always
```json
{
  "compilerOptions": {
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "exactOptionalPropertyTypes": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true,
    "noPropertyAccessFromIndexSignature": true
  }
}
```

### No `any` Policy
- Use `unknown` for truly unknown types
- Use generics for flexible but type-safe code
- Use type assertions only with validation
- Use `// @ts-expect-error` with comment explaining why

### Type-Only Imports
```typescript
import type { User, Config } from './types';
import { createUser } from './utils';
```

## Type System Patterns

### Discriminated Unions for State
```typescript
type AsyncState<T> =
  | { status: 'idle' }
  | { status: 'loading' }
  | { status: 'success'; data: T }
  | { status: 'error'; error: Error };

function handleState<T>(state: AsyncState<T>) {
  switch (state.status) {
    case 'idle': return 'Waiting...';
    case 'loading': return 'Loading...';
    case 'success': return state.data; // TypeScript knows data exists
    case 'error': return state.error.message;
  }
}
```

### Conditional Types
```typescript
type NonNullableProps<T> = {
  [K in keyof T]: NonNullable<T[K]>
};

type ExtractArrayType<T> = T extends (infer U)[] ? U : never;
type StringKeys<T> = Extract<keyof T, string>;
```

### Mapped Types with Modifiers
```typescript
type Mutable<T> = { -readonly [K in keyof T]: T[K] };
type Required<T> = { [K in keyof T]-?: T[K] };
type ReadonlyDeep<T> = {
  readonly [K in keyof T]: T[K] extends object ? ReadonlyDeep<T[K]> : T[K]
};
```

### Template Literal Types
```typescript
type HttpMethod = 'GET' | 'POST' | 'PUT' | 'DELETE';
type ApiRoute = `/api/${string}`;
type EventName = `on${Capitalize<string>}`;

type CSSProperty = `${string}-${string}`;
type HexColor = `#${string}`;
```

### Branded Types for Type Safety
```typescript
declare const __brand: unique symbol;
type Brand<T, B> = T & { [__brand]: B };

type UserId = Brand<string, 'UserId'>;
type Email = Brand<string, 'Email'>;
type SafeSQL = Brand<string, 'SafeSQL'>;

function createUserId(id: string): UserId {
  if (!id.match(/^usr_[a-z0-9]+$/)) throw new Error('Invalid user ID');
  return id as UserId;
}
```

## Runtime Validation

### Zod (Recommended for Most Cases)
```typescript
import { z } from 'zod';

const userSchema = z.object({
  id: z.string().uuid(),
  email: z.string().email(),
  name: z.string().min(1).max(100),
  role: z.enum(['admin', 'user', 'guest']),
  metadata: z.record(z.unknown()).optional()
});

type User = z.infer<typeof userSchema>;

// Validation with error handling
function validateUser(data: unknown): User {
  return userSchema.parse(data);
}

// Safe validation
const result = userSchema.safeParse(data);
if (result.success) {
  console.log(result.data);
} else {
  console.error(result.error.flatten());
}
```

### TypeBox (Best for OpenAPI/JSON Schema)
```typescript
import { Type, Static } from '@sinclair/typebox';
import { TypeCompiler } from '@sinclair/typebox/compiler';

const UserSchema = Type.Object({
  id: Type.String({ format: 'uuid' }),
  email: Type.String({ format: 'email' }),
  role: Type.Union([
    Type.Literal('admin'),
    Type.Literal('user')
  ])
});

type User = Static<typeof UserSchema>;
const validator = TypeCompiler.Compile(UserSchema);

if (validator.Check(data)) {
  // data is typed as User
}
```

### Valibot (Smallest Bundle Size)
```typescript
import * as v from 'valibot';

const UserSchema = v.object({
  id: v.pipe(v.string(), v.uuid()),
  email: v.pipe(v.string(), v.email()),
  age: v.pipe(v.number(), v.minValue(0), v.maxValue(150))
});

type User = v.InferOutput<typeof UserSchema>;
```

### Validation Library Decision Tree
| Requirement | Choice |
|-------------|--------|
| General API validation | Zod |
| OpenAPI/JSON Schema needed | TypeBox |
| Bundle size critical | Valibot |
| Maximum performance | TypeBox with compiled validators |
| Form validation in React | Zod + react-hook-form |

## Type Guards and Narrowing

### Custom Type Guards
```typescript
function isUser(value: unknown): value is User {
  return (
    typeof value === 'object' &&
    value !== null &&
    'id' in value &&
    'email' in value
  );
}

function isNonNullable<T>(value: T): value is NonNullable<T> {
  return value !== null && value !== undefined;
}

// Array filtering with type guard
const users = items.filter(isUser);
const validItems = items.filter(isNonNullable);
```

### Assertion Functions
```typescript
function assertIsString(value: unknown): asserts value is string {
  if (typeof value !== 'string') {
    throw new TypeError('Expected string');
  }
}

function assertDefined<T>(value: T | undefined | null): asserts value is T {
  if (value === undefined || value === null) {
    throw new Error('Value must be defined');
  }
}
```

## React Integration Patterns

### Generic Component Props
```typescript
interface ListProps<T> {
  items: T[];
  renderItem: (item: T, index: number) => React.ReactNode;
  keyExtractor: (item: T) => string;
  emptyMessage?: string;
}

function List<T>({ items, renderItem, keyExtractor, emptyMessage }: ListProps<T>) {
  if (items.length === 0) return <p>{emptyMessage ?? 'No items'}</p>;
  return (
    <ul>
      {items.map((item, i) => (
        <li key={keyExtractor(item)}>{renderItem(item, i)}</li>
      ))}
    </ul>
  );
}
```

### Typed Event Handlers
```typescript
type InputChangeHandler = React.ChangeEventHandler<HTMLInputElement>;
type FormSubmitHandler = React.FormEventHandler<HTMLFormElement>;

const handleChange: InputChangeHandler = (e) => {
  setValue(e.target.value); // e.target is typed
};
```

### Custom Hooks with Generics
```typescript
function useLocalStorage<T>(key: string, initialValue: T) {
  const [value, setValue] = useState<T>(() => {
    const stored = localStorage.getItem(key);
    return stored ? JSON.parse(stored) : initialValue;
  });

  useEffect(() => {
    localStorage.setItem(key, JSON.stringify(value));
  }, [key, value]);

  return [value, setValue] as const;
}
```

## Clean Architecture Pattern

### Layer Structure
```
src/
├── core/           # Domain entities (no dependencies)
├── domain/         # Repository interfaces, service interfaces
├── application/    # Use cases (business logic)
├── infrastructure/ # Implementations (Prisma, external APIs)
└── presentation/   # Controllers, routes, middleware
```

### Repository Interface
```typescript
export interface IUserRepository {
  create(data: CreateUserData): Promise<User>;
  findById(id: string): Promise<User | null>;
  findByEmail(email: string): Promise<User | null>;
  update(id: string, data: Partial<CreateUserData>): Promise<User>;
  delete(id: string): Promise<void>;
}
```

### Use Case Pattern
```typescript
@injectable()
export class CreateUserUseCase {
  constructor(
    @inject('IUserRepository') private userRepo: IUserRepository,
    @inject('ILogger') private logger: ILogger
  ) {}

  async execute(input: CreateUserInput): Promise<User> {
    this.logger.info('Creating user', { email: input.email });

    const validation = createUserSchema.safeParse(input);
    if (!validation.success) {
      throw new ValidationError(validation.error.errors[0].message);
    }

    const existing = await this.userRepo.findByEmail(input.email);
    if (existing) {
      throw new ConflictError('Email already registered');
    }

    return this.userRepo.create(validation.data);
  }
}
```

## Error Handling

### Result Type Pattern
```typescript
type Result<T, E = Error> =
  | { success: true; data: T }
  | { success: false; error: E };

function divide(a: number, b: number): Result<number, string> {
  if (b === 0) return { success: false, error: 'Division by zero' };
  return { success: true, data: a / b };
}

const result = divide(10, 2);
if (result.success) {
  console.log(result.data); // Type: number
} else {
  console.error(result.error); // Type: string
}
```

### Custom Error Classes
```typescript
export class AppError extends Error {
  constructor(
    message: string,
    public readonly code: string,
    public readonly statusCode: number = 500
  ) {
    super(message);
    this.name = this.constructor.name;
  }
}

export class ValidationError extends AppError {
  constructor(message: string) {
    super(message, 'VALIDATION_ERROR', 400);
  }
}

export class NotFoundError extends AppError {
  constructor(resource: string) {
    super(`${resource} not found`, 'NOT_FOUND', 404);
  }
}
```

## Configuration Best Practices

### tsconfig.json for Modern Projects
```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "lib": ["ES2022"],
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "exactOptionalPropertyTypes": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true,
    "noPropertyAccessFromIndexSignature": true,
    "skipLibCheck": true,
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true,
    "outDir": "./dist",
    "rootDir": "./src",
    "isolatedModules": true,
    "esModuleInterop": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,
    "verbatimModuleSyntax": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist", "**/*.test.ts"]
}
```

### Path Aliases
```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"],
      "@components/*": ["src/components/*"],
      "@utils/*": ["src/utils/*"],
      "@types/*": ["src/types/*"]
    }
  }
}
```

## Testing Patterns

### Mock Factory
```typescript
export function createMockRepository<T>(): jest.Mocked<T> {
  return {
    create: jest.fn(),
    findById: jest.fn(),
    findByEmail: jest.fn(),
    update: jest.fn(),
    delete: jest.fn()
  } as unknown as jest.Mocked<T>;
}

export function createMockLogger(): jest.Mocked<ILogger> {
  return {
    info: jest.fn(),
    warn: jest.fn(),
    error: jest.fn(),
    debug: jest.fn()
  };
}
```

### Use Case Testing
```typescript
describe('CreateUserUseCase', () => {
  let useCase: CreateUserUseCase;
  let mockUserRepo: jest.Mocked<IUserRepository>;
  let mockLogger: jest.Mocked<ILogger>;

  beforeEach(() => {
    mockUserRepo = createMockRepository<IUserRepository>();
    mockLogger = createMockLogger();
    useCase = new CreateUserUseCase(mockUserRepo, mockLogger);
  });

  it('should create user with valid input', async () => {
    const input = { email: 'test@example.com', name: 'Test' };
    const expected = { id: '1', ...input, createdAt: new Date() };

    mockUserRepo.findByEmail.mockResolvedValue(null);
    mockUserRepo.create.mockResolvedValue(expected);

    const result = await useCase.execute(input);

    expect(result).toEqual(expected);
    expect(mockUserRepo.create).toHaveBeenCalledWith(input);
  });

  it('should throw on duplicate email', async () => {
    mockUserRepo.findByEmail.mockResolvedValue({ id: '1' } as User);

    await expect(useCase.execute({ email: 'taken@example.com' }))
      .rejects.toThrow(ConflictError);
  });
});
```

## Utility Types Reference

### Built-in Utility Types
```typescript
// Partial - all properties optional
type PartialUser = Partial<User>;

// Required - all properties required
type RequiredConfig = Required<Config>;

// Readonly - all properties readonly
type ReadonlyUser = Readonly<User>;

// Pick - select specific properties
type UserPreview = Pick<User, 'id' | 'name'>;

// Omit - exclude specific properties
type CreateUser = Omit<User, 'id' | 'createdAt'>;

// Record - dictionary type
type UserMap = Record<string, User>;

// Extract - extract from union
type StringOrNumber = Extract<string | number | boolean, string | number>;

// Exclude - exclude from union
type OnlyString = Exclude<string | number | boolean, number | boolean>;

// NonNullable - remove null/undefined
type DefiniteString = NonNullable<string | null | undefined>;

// ReturnType - function return type
type ApiResponse = ReturnType<typeof fetchUser>;

// Parameters - function parameters
type FetchParams = Parameters<typeof fetchUser>;

// Awaited - unwrap Promise
type User = Awaited<Promise<User>>;
```

## Resources

This skill includes comprehensive reference materials:

### References
- `references/advanced-types.md` - Conditional types, mapped types, template literals
- `references/advanced-patterns-2025.md` - Latest TypeScript patterns
- `references/runtime-validation.md` - Zod, TypeBox, Valibot deep dive
- `references/decision-trees.md` - Type vs interface, validation library choice
- `references/configuration.md` - tsconfig.json optimization
- `references/troubleshooting.md` - Common errors and solutions
- `references/security-examples.md` - Branded types, sensitive data patterns
- `references/advanced-patterns.md` - Builder pattern, typed events
- `references/typescript-standards.md` - Strict mode, naming conventions
- `references/typescript-patterns.md` - React Native specific patterns
- `references/examples.md` - Complete feature implementation examples
- `references/reference.md` - Clean Architecture, API patterns

### Scripts
- `scripts/typescript-validator.js` - TypeScript configuration validation

### Templates
- `templates/typescript-config.json` - Recommended tsconfig.json template

### Examples
- `examples/nestjs-typeorm-api/` - Complete NestJS + TypeORM REST API example
  - `src/main.ts` - Application entry point
  - `src/app.module.ts` - Root module configuration
  - `src/users/` - Complete users module with CRUD operations

## Decision Trees

### Type vs Interface
```
Need to extend primitives/unions? → Type alias
Need declaration merging? → Interface
Need mapped types? → Type alias
Defining object shape? → Either works, be consistent
```

### unknown vs any
```
External data (API, user input)? → unknown + validation
Library interop requiring any? → Use with immediate narrowing
Generic constraint? → unknown as default
Truly dynamic? → Consider discriminated union first
```

### Generics vs Union Types
```
Related types with shared operations? → Generics
Distinct types with different handling? → Union
Need type preservation through transforms? → Generics
Fixed set of known types? → Union
```

## Common Patterns Quick Reference

| Pattern | Use Case |
|---------|----------|
| Discriminated Union | State machines, API responses |
| Branded Types | IDs, validated strings |
| Type Guards | Runtime type checking |
| Assertion Functions | Throwing validation |
| Mapped Types | Transforming object types |
| Conditional Types | Type-level logic |
| Template Literals | String pattern types |
| Result Type | Error handling without exceptions |
| Repository Pattern | Data access abstraction |
| Use Case Pattern | Business logic encapsulation |

## Version Compatibility

This skill targets:
- TypeScript 5.x (5.9 features included)
- React 18/19
- Next.js 14/15/16
- Node.js 20+
- NestJS 10+

All patterns are compatible with both ESM and CommonJS module systems.






