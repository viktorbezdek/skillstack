# TypeScript Patterns

## Complete TypeScript Standards for MyJKKN

This document provides comprehensive TypeScript patterns, type definitions, and best practices for building type-safe Next.js applications with Supabase.

## Core Type Definitions

### Entity Interface Pattern

The main entity interface should match the database schema exactly:

```typescript
/**
 * Course entity matching the database schema
 * @table courses
 */
export interface Course {
  // Primary identifier
  id: string;

  // Multi-tenancy
  institution_id: string;

  // Business fields
  code: string;
  name: string;
  description: string | null;
  credits: number;
  department_id: string;

  // Status
  is_active: boolean;

  // Audit fields
  created_at: string; // ISO 8601 timestamp
  updated_at: string;
  created_by: string | null;
  updated_by: string | null;
}
```

### DTO (Data Transfer Object) Patterns

#### Create DTO

Contains only fields that users provide during creation:

```typescript
/**
 * DTO for creating a new course
 * Excludes: id, timestamps, and other auto-generated fields
 */
export interface CreateCourseDto {
  institution_id: string;
  department_id: string;
  code: string;
  name: string;
  description?: string; // Optional fields use '?'
  credits: number;
}
```

#### Update DTO

All fields optional except `id`:

```typescript
/**
 * DTO for updating an existing course
 * All fields optional to support partial updates
 */
export interface UpdateCourseDto {
  id: string; // Required to identify the record
  code?: string;
  name?: string;
  description?: string | null; // Can set to null
  credits?: number;
  department_id?: string;
  is_active?: boolean;
}
```

#### Alternative: Using Utility Types

```typescript
// Create DTO: Pick specific fields
export type CreateCourseDto = Pick<
  Course,
  'institution_id' | 'department_id' | 'code' | 'name' | 'credits'
> & {
  description?: string;
};

// Update DTO: Partial except id
export type UpdateCourseDto = Partial<Omit<Course, 'id' | 'created_at' | 'updated_at'>> & {
  id: string;
};
```

### Filter Interfaces

For search and filtering operations:

```typescript
/**
 * Filter options for querying courses
 * All fields optional - apply only when provided
 */
export interface CourseFilters {
  // Exact matches
  institution_id?: string;
  department_id?: string;
  is_active?: boolean;

  // Text search
  search?: string; // Searches name, code, description

  // Range filters
  min_credits?: number;
  max_credits?: number;

  // Date filters
  created_after?: string;
  created_before?: string;
}
```

### Response Interfaces

#### Single Item Response

```typescript
/**
 * Response for a single course fetch
 */
export interface CourseResponse {
  data: Course | null;
  error: string | null;
}
```

#### Paginated List Response

```typescript
/**
 * Paginated response for course lists
 */
export interface CoursesResponse {
  data: Course[];
  total: number;
  page: number;
  pageSize: number;
  totalPages: number;
}
```

#### Action Response

```typescript
/**
 * Response for mutations (create, update, delete)
 */
export interface ActionResponse<T = void> {
  success: boolean;
  data?: T;
  error?: string;
  message?: string;
}

// Usage
const createResponse: ActionResponse<Course> = {
  success: true,
  data: newCourse,
  message: 'Course created successfully'
};
```

## Advanced Type Patterns

### Union Types for Status

```typescript
// Define all possible status values
export type CourseStatus = 'draft' | 'published' | 'archived' | 'inactive';

// Use in interface
export interface Course {
  id: string;
  name: string;
  status: CourseStatus; // Only allows the defined values
}

// In forms
const statuses: CourseStatus[] = ['draft', 'published', 'archived', 'inactive'];
```

### Discriminated Unions

For components that handle multiple states:

```typescript
// Define each state as a distinct type
type LoadingState = {
  status: 'loading';
};

type SuccessState<T> = {
  status: 'success';
  data: T;
};

type ErrorState = {
  status: 'error';
  error: string;
};

// Combine into a union
export type DataState<T> = LoadingState | SuccessState<T> | ErrorState;

// Usage with type narrowing
function CourseDisplay({ state }: { state: DataState<Course> }) {
  if (state.status === 'loading') {
    return <Spinner />;
  }

  if (state.status === 'error') {
    return <ErrorMessage error={state.error} />;
  }

  // TypeScript knows state.data exists here
  return <CourseCard course={state.data} />;
}
```

### Generic Types

For reusable patterns:

```typescript
/**
 * Generic paginated response
 * Works with any entity type
 */
export interface PaginatedResponse<T> {
  data: T[];
  total: number;
  page: number;
  pageSize: number;
}

// Usage
type CoursesPaginated = PaginatedResponse<Course>;
type StudentsPaginated = PaginatedResponse<Student>;

/**
 * Generic filter interface
 */
export interface BaseFilters {
  search?: string;
  is_active?: boolean;
  institution_id?: string;
}

// Extend for specific entities
export interface CourseFilters extends BaseFilters {
  department_id?: string;
  min_credits?: number;
}
```

### Readonly Types

For immutable data:

```typescript
// Make all properties readonly
export type ReadonlyCourse = Readonly<Course>;

// Deep readonly
export type DeepReadonly<T> = {
  readonly [P in keyof T]: DeepReadonly<T[P]>;
};

// Usage
const course: ReadonlyCourse = {
  id: '123',
  name: 'CS101',
  // ...
};

// course.name = 'CS102'; // Error: Cannot assign to 'name' because it is a read-only property
```

## Type Guards

### Basic Type Guards

```typescript
/**
 * Check if value is a valid Course
 */
export function isCourse(value: unknown): value is Course {
  return (
    typeof value === 'object' &&
    value !== null &&
    'id' in value &&
    'name' in value &&
    'institution_id' in value
  );
}

// Usage
function processCourse(data: unknown) {
  if (isCourse(data)) {
    // TypeScript knows data is Course here
    console.log(data.name);
  }
}
```

### Zod Schema as Type Guard

```typescript
import { z } from 'zod';

// Define schema
export const CourseSchema = z.object({
  id: z.string().uuid(),
  institution_id: z.string().uuid(),
  code: z.string().min(1).max(50),
  name: z.string().min(1).max(255),
  credits: z.number().int().min(0).max(10),
  description: z.string().nullable(),
  is_active: z.boolean(),
  created_at: z.string().datetime(),
  updated_at: z.string().datetime(),
});

// Extract type from schema
export type Course = z.infer<typeof CourseSchema>;

// Use for validation
function validateCourse(data: unknown): Course {
  return CourseSchema.parse(data); // Throws if invalid
}

// Safe parse
function safeParseCourse(data: unknown): Course | null {
  const result = CourseSchema.safeParse(data);
  return result.success ? result.data : null;
}
```

## React Component Prop Types

### Component Props Pattern

```typescript
/**
 * Props for CourseCard component
 */
export interface CourseCardProps {
  course: Course;
  onEdit?: (course: Course) => void; // Optional callback
  onDelete?: (id: string) => Promise<void>; // Async callback
  className?: string;
  variant?: 'default' | 'compact' | 'detailed';
}

// Component
export function CourseCard({
  course,
  onEdit,
  onDelete,
  className,
  variant = 'default'
}: CourseCardProps) {
  // Implementation
}
```

### Children Props

```typescript
// For components with children
export interface LayoutProps {
  children: React.ReactNode;
  title: string;
  className?: string;
}

// For render props pattern
export interface DataTableProps<T> {
  data: T[];
  renderRow: (item: T, index: number) => React.ReactNode;
  renderEmpty?: () => React.ReactNode;
}
```

### Generic Component Props

```typescript
/**
 * Generic form props
 * Works with any entity type
 */
export interface FormProps<T> {
  initialData?: T;
  onSubmit: (data: T) => Promise<void>;
  onCancel?: () => void;
  mode: 'create' | 'edit';
}

// Usage
type CourseFormProps = FormProps<CreateCourseDto>;
type StudentFormProps = FormProps<CreateStudentDto>;
```

## Hook Return Types

### Basic Hook Return

```typescript
/**
 * Return type for useCourses hook
 */
export interface UseCoursesReturn {
  courses: Course[];
  loading: boolean;
  error: string | null;
  total: number;
  page: number;
  pageSize: number;
  setPage: (page: number) => void;
  refetch: () => Promise<void>;
}

// Hook implementation
export function useCourses(filters?: CourseFilters): UseCoursesReturn {
  // Implementation
}
```

### Generic Hook Return

```typescript
/**
 * Generic data fetching hook return type
 */
export interface UseDataReturn<T> {
  data: T | null;
  loading: boolean;
  error: string | null;
  refetch: () => Promise<void>;
}

// Generic hook
export function useData<T>(
  fetcher: () => Promise<T>
): UseDataReturn<T> {
  // Implementation
}
```

### Mutation Hook Return

```typescript
/**
 * Return type for mutation hooks (create, update, delete)
 */
export interface UseMutationReturn<TData, TVariables> {
  mutate: (variables: TVariables) => Promise<TData>;
  loading: boolean;
  error: string | null;
  data: TData | null;
  reset: () => void;
}

// Usage
const createCourse = useCreateCourse(); // UseMutationReturn<Course, CreateCourseDto>
await createCourse.mutate({ name: 'CS101', ... });
```

## Service Method Types

### Service Class Pattern

```typescript
/**
 * Course service with strict typing
 */
export class CourseService {
  private static supabase = createClientSupabaseClient();

  /**
   * Fetch paginated courses with filters
   */
  static async getCourses(
    filters: CourseFilters = {},
    page: number = 1,
    pageSize: number = 10
  ): Promise<CoursesResponse> {
    // Implementation
  }

  /**
   * Fetch single course by ID
   */
  static async getCourseById(id: string): Promise<Course> {
    // Implementation
  }

  /**
   * Create a new course
   */
  static async createCourse(dto: CreateCourseDto): Promise<Course> {
    // Implementation
  }

  /**
   * Update existing course
   */
  static async updateCourse(dto: UpdateCourseDto): Promise<Course> {
    // Implementation
  }

  /**
   * Delete course (soft delete)
   */
  static async deleteCourse(id: string): Promise<boolean> {
    // Implementation
  }
}
```

## Form Data Types

### React Hook Form Integration

```typescript
import { UseFormReturn } from 'react-hook-form';
import { z } from 'zod';

// Define form schema
export const CourseFormSchema = z.object({
  code: z.string().min(1, 'Code is required').max(50),
  name: z.string().min(1, 'Name is required').max(255),
  description: z.string().optional(),
  credits: z.coerce.number().int().min(0).max(10),
  department_id: z.string().uuid('Invalid department'),
});

// Extract form data type
export type CourseFormData = z.infer<typeof CourseFormSchema>;

// Props for form component
export interface CourseFormProps {
  initialData?: Course;
  onSubmit: (data: CourseFormData) => Promise<void>;
  form?: UseFormReturn<CourseFormData>;
}
```

## Utility Types

### Commonly Used Utility Types

```typescript
// Pick specific properties
type CourseBasic = Pick<Course, 'id' | 'name' | 'code'>;

// Omit specific properties
type CourseWithoutAudit = Omit<Course, 'created_at' | 'updated_at' | 'created_by' | 'updated_by'>;

// Make all properties optional
type PartialCourse = Partial<Course>;

// Make all properties required
type RequiredCourse = Required<Course>;

// Make all properties readonly
type ImmutableCourse = Readonly<Course>;

// Record type for key-value pairs
type CourseMap = Record<string, Course>; // { [id: string]: Course }

// Extract union type from array
const statuses = ['draft', 'published', 'archived'] as const;
type Status = typeof statuses[number]; // 'draft' | 'published' | 'archived'
```

### Custom Utility Types

```typescript
/**
 * Make specific keys required
 */
export type RequireKeys<T, K extends keyof T> = T & Required<Pick<T, K>>;

// Usage
type CourseWithRequiredDescription = RequireKeys<Course, 'description'>;

/**
 * Make specific keys optional
 */
export type OptionalKeys<T, K extends keyof T> = Omit<T, K> & Partial<Pick<T, K>>;

// Usage
type CourseWithOptionalDescription = OptionalKeys<Course, 'description'>;

/**
 * Extract nullable fields
 */
export type NullableFields<T> = {
  [K in keyof T]: null extends T[K] ? K : never;
}[keyof T];

// Usage
type CourseNullableFields = NullableFields<Course>; // 'description' | 'created_by' | 'updated_by'
```

## Type Organization

### Module Type Structure

```typescript
// types/courses.ts

// ============================================
// Database Entity
// ============================================

export interface Course {
  // ...
}

// ============================================
// DTOs (Data Transfer Objects)
// ============================================

export interface CreateCourseDto {
  // ...
}

export interface UpdateCourseDto {
  // ...
}

// ============================================
// Filters and Queries
// ============================================

export interface CourseFilters {
  // ...
}

export interface CourseSortOptions {
  field: keyof Course;
  direction: 'asc' | 'desc';
}

// ============================================
// Responses
// ============================================

export interface CoursesResponse {
  // ...
}

export interface CourseActionResponse extends ActionResponse<Course> {}

// ============================================
// UI/Component Types
// ============================================

export interface CourseCardProps {
  // ...
}

export interface CourseFormProps {
  // ...
}

// ============================================
// Hook Return Types
// ============================================

export interface UseCoursesReturn {
  // ...
}

// ============================================
// Enums and Constants
// ============================================

export const COURSE_STATUSES = ['draft', 'published', 'archived'] as const;
export type CourseStatus = typeof COURSE_STATUSES[number];
```

## Type Safety Best Practices

### 1. Never Use `any`

```typescript
// ❌ BAD
function processData(data: any) {
  return data.name;
}

// ✅ GOOD
function processData(data: unknown): string {
  if (isCourse(data)) {
    return data.name;
  }
  throw new Error('Invalid data');
}
```

### 2. Use `unknown` Instead of `any`

```typescript
// For API responses
async function fetchCourse(id: string): Promise<Course> {
  const response = await fetch(`/api/courses/${id}`);
  const data: unknown = await response.json();

  // Validate before using
  if (isCourse(data)) {
    return data;
  }

  throw new Error('Invalid course data');
}
```

### 3. Strict Null Checks

```typescript
// Enable in tsconfig.json: "strictNullChecks": true

// Handle null explicitly
function getCourseDescription(course: Course): string {
  // course.description might be null
  return course.description ?? 'No description';
}
```

### 4. Use Type Assertions Sparingly

```typescript
// ❌ BAD: Unsafe assertion
const course = data as Course;

// ✅ GOOD: Validate then assert
const course = isCourse(data) ? data : null;

// ✅ ACCEPTABLE: When you have external guarantee
const course = validatedData as Course; // After Zod validation
```

### 5. Leverage Type Inference

```typescript
// ❌ Redundant type annotation
const courses: Course[] = await CourseService.getCourses();

// ✅ Let TypeScript infer
const courses = await CourseService.getCourses(); // Type inferred from return type
```

## Common Patterns

### Optional Chaining and Nullish Coalescing

```typescript
// Optional chaining
const departmentName = course?.department?.name;

// Nullish coalescing
const description = course.description ?? 'No description';
const credits = course.credits ?? 0;
```

### Type Narrowing

```typescript
function handleCourseAction(action: CourseAction) {
  if (action.type === 'create') {
    // TypeScript knows action.payload is CreateCourseDto
    console.log(action.payload.name);
  } else if (action.type === 'update') {
    // TypeScript knows action.payload is UpdateCourseDto
    console.log(action.payload.id);
  }
}
```

### Const Assertions

```typescript
// Without const assertion
const config = {
  apiUrl: '/api',
  timeout: 5000
}; // Type: { apiUrl: string; timeout: number; }

// With const assertion
const config = {
  apiUrl: '/api',
  timeout: 5000
} as const; // Type: { readonly apiUrl: "/api"; readonly timeout: 5000; }
```

## Testing Types

### Type-Only Imports

```typescript
// Import types without runtime cost
import type { Course } from '@/types/courses';
import type { CourseService } from '@/lib/services/courses/course-service';

// Regular import for values
import { CourseService } from '@/lib/services/courses/course-service';
```

### Testing Utility

```typescript
/**
 * Type test utilities
 */
type Expect<T extends true> = T;
type Equal<X, Y> = (<T>() => T extends X ? 1 : 2) extends <T>() => T extends Y ? 1 : 2
  ? true
  : false;

// Usage in tests
type Test1 = Expect<Equal<CourseFormData['name'], string>>; // ✅ Passes
type Test2 = Expect<Equal<Course['id'], number>>; // ❌ Compile error if wrong
```

## Summary Checklist

For every module:

- [ ] Entity interface matches database schema
- [ ] Create DTO contains only user-provided fields
- [ ] Update DTO has all fields optional except `id`
- [ ] Filter interface for search/filtering
- [ ] Response interfaces for API returns
- [ ] No `any` types used
- [ ] `unknown` used for unvalidated data
- [ ] Type guards for runtime validation
- [ ] Zod schemas for form validation
- [ ] Proper null handling with strict checks
- [ ] Component props interfaces defined
- [ ] Hook return types specified
- [ ] Service methods have return types
- [ ] Types organized logically in files
- [ ] Type imports use `import type` where possible

This ensures complete type safety across the entire application.
