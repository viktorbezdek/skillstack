# Architecture Patterns

## MyJKKN 5-Layer Architecture

This document provides detailed architectural guidance for building feature modules following MyJKKN's standardized approach for Next.js 15 + Supabase applications.

## Core Architecture Principles

### 1. Separation of Concerns

Each layer has a distinct responsibility:

- **Types Layer**: Data contracts and interfaces
- **Service Layer**: Business logic and data access
- **Hooks Layer**: State management and side effects
- **Components Layer**: UI presentation and user interaction
- **Pages Layer**: Routing and layout composition

### 2. Unidirectional Data Flow

```
Pages (Server Components)
  ↓ fetch data, handle actions
Components (Client Components)
  ↓ use hooks for state
Hooks Layer
  ↓ call services
Service Layer
  ↓ interact with
Supabase Database
```

### 3. Type Safety Throughout

```typescript
// Types define the contract
interface User { id: string; name: string; }

// Services enforce the contract
class UserService {
  static async getUser(id: string): Promise<User> { }
}

// Hooks maintain type safety
function useUser(id: string): { user: User | null; loading: boolean } { }

// Components receive typed props
function UserCard({ user }: { user: User }) { }

// Pages coordinate typed data flow
async function UserPage({ params }: { params: { id: string } }) {
  const user: User = await UserService.getUser(params.id);
  return <UserCard user={user} />;
}
```

## Layer-by-Layer Design Patterns

### Types Layer (`types/[module].ts`)

**Purpose**: Define data contracts for the entire module

**Pattern**:
```typescript
// 1. Main entity interface (matches database schema)
export interface Entity {
  // Database fields
  id: string;
  institution_id: string;

  // Business fields
  name: string;
  description: string | null;

  // Metadata fields
  is_active: boolean;
  created_at: string;
  updated_at: string;
  created_by?: string;
  updated_by?: string;
}

// 2. Create DTO (user input only)
export interface CreateEntityDto {
  institution_id: string;
  name: string;
  description?: string;
}

// 3. Update DTO (partial + id)
export interface UpdateEntityDto {
  id: string;
  name?: string;
  description?: string;
  is_active?: boolean;
}

// 4. Filter interface (query parameters)
export interface EntityFilters {
  institution_id?: string;
  search?: string;
  is_active?: boolean;
  created_after?: string;
}

// 5. Response interface (paginated results)
export interface EntityResponse {
  data: Entity[];
  total: number;
  page: number;
  pageSize: number;
}
```

### Service Layer (`lib/services/[module]/[entity]-service.ts`)

**Purpose**: Encapsulate all database operations and business logic

**Pattern**:
```typescript
import { createClientSupabaseClient } from '@/lib/supabase/client';
import type { Entity, CreateEntityDto, UpdateEntityDto, EntityFilters, EntityResponse } from '@/types/[module]';

export class EntityService {
  private static supabase = createClientSupabaseClient();

  // Pattern: List with pagination and filters
  static async getEntities(
    filters: EntityFilters = {},
    page = 1,
    pageSize = 10
  ): Promise<EntityResponse> {
    // Implementation follows service-patterns.md
  }

  // Pattern: Get single by ID
  static async getEntityById(id: string): Promise<Entity> {
    // Implementation follows service-patterns.md
  }

  // Pattern: Create with validation
  static async createEntity(dto: CreateEntityDto): Promise<Entity> {
    // Implementation follows service-patterns.md
  }

  // Pattern: Update with partial data
  static async updateEntity(dto: UpdateEntityDto): Promise<Entity> {
    // Implementation follows service-patterns.md
  }

  // Pattern: Soft delete (preferred) or hard delete
  static async deleteEntity(id: string): Promise<boolean> {
    // Implementation follows service-patterns.md
  }
}
```

### Hooks Layer (`hooks/[module]/use-[entity].ts`)

**Purpose**: Manage client-side state and orchestrate service calls

**Pattern**:
```typescript
'use client';

import { useState, useEffect, useCallback } from 'react';
import { EntityService } from '@/lib/services/[module]/[entity]-service';
import type { Entity, EntityFilters } from '@/types/[module]';

export function useEntities(filters: EntityFilters = {}) {
  const [entities, setEntities] = useState<Entity[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const fetchEntities = useCallback(async () => {
    // Implementation follows hooks-patterns.md
  }, [filters]);

  useEffect(() => {
    fetchEntities();
  }, [fetchEntities]);

  return { entities, loading, error, refetch: fetchEntities };
}
```

### Components Layer (`app/(routes)/[module]/_components/`)

**Purpose**: Reusable UI components with clear props interfaces

**Pattern**:
```typescript
// Component files in this layer:
// - columns.tsx - Table column definitions
// - [entity]-data-table.tsx - Data table component
// - [entity]-form.tsx - Create/Edit form
// - [entity]-filters.tsx - Search and filter UI
// - row-actions.tsx - Action buttons/menu
// - data-table-schema.ts - Zod validation

// See component-patterns.md for full implementations
```

### Pages Layer (`app/(routes)/[module]/`)

**Purpose**: Route handlers, layout composition, and data fetching

**Pattern**:
```typescript
// app/(routes)/[module]/page.tsx - List view
export default async function EntitiesPage() {
  return (
    <ContentLayout>
      <Breadcrumb />
      <EntityDataTable />
    </ContentLayout>
  );
}

// app/(routes)/[module]/new/page.tsx - Create page
export default function NewEntityPage() {
  return (
    <PermissionGuard module="[module].[entity]" action="create">
      <ContentLayout>
        <Breadcrumb />
        <EntityForm mode="create" />
      </ContentLayout>
    </PermissionGuard>
  );
}

// app/(routes)/[module]/[id]/edit/page.tsx - Edit page
export default async function EditEntityPage({ params }: { params: { id: string } }) {
  const entity = await EntityService.getEntityById(params.id);

  return (
    <PermissionGuard module="[module].[entity]" action="edit">
      <ContentLayout>
        <Breadcrumb />
        <EntityForm mode="edit" initialData={entity} />
      </ContentLayout>
    </PermissionGuard>
  );
}

// See page-patterns.md for full implementations
```

## Cross-Cutting Concerns

### Error Handling Strategy

**Service Layer**:
```typescript
try {
  const { data, error } = await this.supabase.from('entities').select('*');
  if (error) throw error;
  return data;
} catch (error) {
  console.error('[module/entity] Error fetching:', error);
  throw error; // Re-throw to let caller handle
}
```

**Hooks Layer**:
```typescript
try {
  setLoading(true);
  setError(null);
  const data = await EntityService.getEntities();
  setEntities(data);
} catch (err) {
  const message = err instanceof Error ? err.message : 'Failed to fetch';
  setError(message);
  toast.error(message); // User-friendly notification
} finally {
  setLoading(false);
}
```

### Loading States

**Consistent loading indicators**:
```typescript
// In hooks
const [loading, setLoading] = useState(false);

// In components
{loading ? <Skeleton /> : <DataTable />}

// In pages with suspense
<Suspense fallback={<LoadingSpinner />}>
  <DataTable />
</Suspense>
```

### Logging Standards

**Format**: `[module/entity] Action: details`

```typescript
// Success logs
console.log('[academic/courses] Created course:', course.id);

// Warning logs
console.warn('[academic/courses] Invalid filter:', filters);

// Error logs
console.error('[academic/courses] Failed to delete:', error);
```

## Module Communication Patterns

### When modules need to interact:

**1. Shared Types** (preferred):
```typescript
// types/shared.ts
export interface Institution {
  id: string;
  name: string;
}

// Both modules import from shared types
import type { Institution } from '@/types/shared';
```

**2. Service Composition**:
```typescript
// Course service needs institution data
import { InstitutionService } from '@/lib/services/institution/institution-service';

export class CourseService {
  static async createCourse(dto: CreateCourseDto) {
    // Validate institution exists
    const institution = await InstitutionService.getById(dto.institution_id);
    if (!institution) throw new Error('Institution not found');

    // Proceed with course creation
    return this.supabase.from('courses').insert([dto]);
  }
}
```

**3. Avoid Direct Database Joins Across Modules**:
```typescript
// ❌ BAD: Direct join across module boundaries
const { data } = await supabase
  .from('courses')
  .select('*, institutions(*)')
  .eq('id', id);

// ✅ GOOD: Fetch separately and compose
const course = await CourseService.getById(id);
const institution = await InstitutionService.getById(course.institution_id);
return { ...course, institution };
```

## File Organization Best Practices

### Module Directory Structure

```
app/(routes)/[module]/
├── page.tsx                          # List view (Server Component)
├── loading.tsx                       # Loading state for the module
├── error.tsx                         # Error boundary
├── new/
│   └── page.tsx                     # Create form page
├── [id]/
│   ├── page.tsx                     # Detail view (optional)
│   └── edit/
│       └── page.tsx                 # Edit form page
└── _components/                      # Module-specific components
    ├── columns.tsx                  # TanStack Table columns
    ├── data-table-schema.ts         # Zod validation
    ├── [entity]-data-table.tsx      # Data table wrapper
    ├── [entity]-form.tsx            # Create/Edit form
    ├── [entity]-filters.tsx         # Filter controls
    └── row-actions.tsx              # Row action menu

lib/services/[module]/
└── [entity]-service.ts              # Service class

hooks/[module]/
├── use-[entity].ts                  # Main hook (list)
├── use-[entity]-form.ts             # Form submission hook
└── use-[entity]-delete.ts           # Delete action hook

types/
└── [module].ts                      # All module types
```

### Naming Conventions Reference

| Type | Convention | Example |
|------|-----------|---------|
| Files | kebab-case | `course-service.ts` |
| Directories | kebab-case | `academic-courses/` |
| Components | PascalCase | `CourseForm` |
| Classes | PascalCase | `CourseService` |
| Functions | camelCase | `getCourses` |
| Hooks | camelCase with `use` prefix | `useCourses` |
| Types/Interfaces | PascalCase | `Course`, `CreateCourseDto` |
| Constants | UPPER_SNAKE_CASE | `MAX_PAGE_SIZE` |
| Props interfaces | PascalCase with `Props` suffix | `CourseFormProps` |

## Testing Strategy

### Unit Tests for Services
```typescript
// __tests__/services/course-service.test.ts
describe('CourseService', () => {
  it('should fetch courses with filters', async () => {
    const result = await CourseService.getCourses({ is_active: true });
    expect(result.data).toBeInstanceOf(Array);
  });
});
```

### Integration Tests for Hooks
```typescript
// __tests__/hooks/use-courses.test.tsx
import { renderHook, waitFor } from '@testing-library/react';

describe('useCourses', () => {
  it('should load courses', async () => {
    const { result } = renderHook(() => useCourses());
    await waitFor(() => expect(result.current.loading).toBe(false));
    expect(result.current.courses).toHaveLength(10);
  });
});
```

### E2E Tests for Pages
```typescript
// e2e/courses.spec.ts
import { test, expect } from '@playwright/test';

test('should create a new course', async ({ page }) => {
  await page.goto('/academic/courses/new');
  await page.fill('[name="name"]', 'Test Course');
  await page.click('[type="submit"]');
  await expect(page).toHaveURL(/\/academic\/courses$/);
});
```

## Performance Optimization Patterns

### Server Component Data Fetching
```typescript
// Use Server Components for initial data fetch
export default async function CoursesPage() {
  const courses = await CourseService.getCourses(); // No client-side overhead
  return <CoursesList initialData={courses} />;
}
```

### Client Component Optimization
```typescript
// Memoize expensive computations
const filteredCourses = useMemo(() => {
  return courses.filter(c => c.name.includes(search));
}, [courses, search]);

// Debounce API calls
const debouncedSearch = useDebounce(search, 500);
useEffect(() => {
  if (debouncedSearch) {
    fetchCourses({ search: debouncedSearch });
  }
}, [debouncedSearch]);
```

### Database Query Optimization
```typescript
// Select only needed fields
.select('id, name, is_active')

// Use indexes for filters
.eq('institution_id', id) // Ensure index exists

// Limit results
.range(0, 9) // First 10 results
```

## Security Best Practices

### Row-Level Security (RLS)
```sql
-- Ensure RLS is enabled
ALTER TABLE entities ENABLE ROW LEVEL SECURITY;

-- Users can only see their institution's data
CREATE POLICY "Users view own institution"
  ON entities FOR SELECT
  USING (institution_id = auth.jwt()->>'institution_id');
```

### Input Validation
```typescript
// Validate on client and server
import { z } from 'zod';

const CreateCourseSchema = z.object({
  name: z.string().min(1).max(255),
  institution_id: z.string().uuid(),
});

// In service
static async createCourse(dto: CreateCourseDto) {
  const validated = CreateCourseSchema.parse(dto); // Throws if invalid
  // Proceed with creation
}
```

### Permission Checks
```typescript
// Check permissions before mutations
<PermissionGuard module="academic.courses" action="create">
  <Button onClick={handleCreate}>Create Course</Button>
</PermissionGuard>
```

## Migration and Versioning

### Database Migrations
```sql
-- migrations/001_create_courses.sql
CREATE TABLE courses (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  institution_id UUID NOT NULL REFERENCES institutions(id),
  name VARCHAR(255) NOT NULL,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_courses_institution ON courses(institution_id);
```

### Type Versioning
```typescript
// When schema changes, version your types
export interface CourseV1 {
  id: string;
  name: string;
}

export interface CourseV2 extends CourseV1 {
  description: string;
}

// Use type alias for current version
export type Course = CourseV2;
```

## Common Pitfalls to Avoid

### ❌ Don't Mix Server and Client Logic
```typescript
// BAD: Service call in client component
'use client';
export function CourseList() {
  useEffect(() => {
    CourseService.getCourses(); // This creates a client-side Supabase instance
  }, []);
}
```

### ❌ Don't Bypass Type Safety
```typescript
// BAD: Using 'any'
const data: any = await supabase.from('courses').select('*');

// GOOD: Use proper types
const data: Course[] = await CourseService.getCourses();
```

### ❌ Don't Forget Error Handling
```typescript
// BAD: No error handling
const courses = await CourseService.getCourses();

// GOOD: Handle errors
try {
  const courses = await CourseService.getCourses();
} catch (error) {
  console.error('[courses] Failed to fetch:', error);
  toast.error('Failed to load courses');
}
```

### ❌ Don't Hardcode Permissions
```typescript
// BAD: Hardcoded role check
if (user.role === 'admin') {
  return <CreateButton />;
}

// GOOD: Use permission system
<CanCreate module="academic.courses">
  <CreateButton />
</CanCreate>
```

## Summary Checklist

Before completing a module, verify:

- [ ] All five layers are implemented
- [ ] Types match database schema exactly
- [ ] Services have proper error handling
- [ ] Hooks manage loading and error states
- [ ] Components are properly typed
- [ ] Pages use correct routing patterns
- [ ] Permissions are applied everywhere
- [ ] Logging uses correct format
- [ ] RLS policies are configured
- [ ] Code follows naming conventions
- [ ] No `any` types used
- [ ] Tests cover critical paths
- [ ] Performance is acceptable
- [ ] Security is validated

This architecture ensures consistency, maintainability, and scalability across all MyJKKN modules.
