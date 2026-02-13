# TypeScript Development - Extended Patterns & Examples

Detailed code examples, architecture patterns, and reference material extracted from the core skill.

## Runtime Validation - Detailed Examples

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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
