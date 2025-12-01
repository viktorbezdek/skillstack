# Service Layer Patterns

## Complete Service Layer Implementation Guide

This document provides comprehensive patterns for implementing the service layer in MyJKKN applications, covering all database operations, business logic, and Supabase integration.

## Service Class Structure

### Basic Service Template

```typescript
import { createClientSupabaseClient } from '@/lib/supabase/client';
import type {
  Course,
  CreateCourseDto,
  UpdateCourseDto,
  CourseFilters,
  CoursesResponse
} from '@/types/courses';

export class CourseService {
  // Singleton Supabase client
  private static supabase = createClientSupabaseClient();

  // CRUD operations
  static async getCourses(filters?: CourseFilters, page?: number, pageSize?: number): Promise<CoursesResponse> {}
  static async getCourseById(id: string): Promise<Course> {}
  static async createCourse(dto: CreateCourseDto): Promise<Course> {}
  static async updateCourse(dto: UpdateCourseDto): Promise<Course> {}
  static async deleteCourse(id: string): Promise<boolean> {}
}
```

## CRUD Operations

### 1. GET with Pagination and Filters

```typescript
/**
 * Fetch courses with pagination and filtering
 * @param filters - Filter criteria
 * @param page - Page number (1-indexed)
 * @param pageSize - Number of items per page
 * @returns Paginated courses response
 */
static async getCourses(
  filters: CourseFilters = {},
  page: number = 1,
  pageSize: number = 10
): Promise<CoursesResponse> {
  try {
    // Start with base query
    let query = this.supabase
      .from('courses')
      .select('*', { count: 'exact' }); // Include total count

    // Apply filters
    if (filters.institution_id) {
      query = query.eq('institution_id', filters.institution_id);
    }

    if (filters.department_id) {
      query = query.eq('department_id', filters.department_id);
    }

    if (filters.is_active !== undefined) {
      query = query.eq('is_active', filters.is_active);
    }

    // Text search across multiple fields
    if (filters.search) {
      query = query.or(
        `name.ilike.%${filters.search}%,code.ilike.%${filters.search}%,description.ilike.%${filters.search}%`
      );
    }

    // Range filters
    if (filters.min_credits !== undefined) {
      query = query.gte('credits', filters.min_credits);
    }

    if (filters.max_credits !== undefined) {
      query = query.lte('credits', filters.max_credits);
    }

    // Date filters
    if (filters.created_after) {
      query = query.gte('created_at', filters.created_after);
    }

    if (filters.created_before) {
      query = query.lte('created_at', filters.created_before);
    }

    // Pagination
    const from = (page - 1) * pageSize;
    const to = from + pageSize - 1;
    query = query.range(from, to);

    // Sorting
    query = query.order('created_at', { ascending: false });

    // Execute query
    const { data, error, count } = await query;

    if (error) {
      console.error('[courses/service] Error fetching courses:', error);
      throw new Error(`Failed to fetch courses: ${error.message}`);
    }

    return {
      data: data || [],
      total: count || 0,
      page,
      pageSize,
      totalPages: Math.ceil((count || 0) / pageSize)
    };
  } catch (error) {
    console.error('[courses/service] Unexpected error fetching courses:', error);
    throw error;
  }
}
```

### 2. GET Single by ID

```typescript
/**
 * Fetch a single course by ID
 * @param id - Course UUID
 * @returns Course entity
 * @throws Error if course not found
 */
static async getCourseById(id: string): Promise<Course> {
  try {
    const { data, error } = await this.supabase
      .from('courses')
      .select('*')
      .eq('id', id)
      .single();

    if (error) {
      if (error.code === 'PGRST116') {
        throw new Error('Course not found');
      }
      console.error('[courses/service] Error fetching course by ID:', error);
      throw new Error(`Failed to fetch course: ${error.message}`);
    }

    console.log('[courses/service] Fetched course:', id);
    return data;
  } catch (error) {
    console.error('[courses/service] Unexpected error fetching course:', error);
    throw error;
  }
}
```

### 3. GET with Joins

```typescript
/**
 * Fetch course with related data
 * @param id - Course UUID
 * @returns Course with department information
 */
static async getCourseWithDepartment(id: string): Promise<CourseWithDepartment> {
  try {
    const { data, error } = await this.supabase
      .from('courses')
      .select(`
        *,
        department:departments (
          id,
          name,
          code
        )
      `)
      .eq('id', id)
      .single();

    if (error) {
      console.error('[courses/service] Error fetching course with department:', error);
      throw new Error(`Failed to fetch course: ${error.message}`);
    }

    return data;
  } catch (error) {
    console.error('[courses/service] Unexpected error:', error);
    throw error;
  }
}
```

### 4. CREATE

```typescript
/**
 * Create a new course
 * @param dto - Course creation data
 * @returns Created course entity
 */
static async createCourse(dto: CreateCourseDto): Promise<Course> {
  try {
    // Optional: Additional validation
    if (!dto.name || dto.name.trim().length === 0) {
      throw new Error('Course name is required');
    }

    // Insert record
    const { data, error } = await this.supabase
      .from('courses')
      .insert([{
        ...dto,
        created_at: new Date().toISOString(),
        updated_at: new Date().toISOString(),
      }])
      .select()
      .single();

    if (error) {
      // Handle unique constraint violations
      if (error.code === '23505') {
        throw new Error('A course with this code already exists');
      }

      console.error('[courses/service] Error creating course:', error);
      throw new Error(`Failed to create course: ${error.message}`);
    }

    console.log('[courses/service] Created course:', data.id);
    return data;
  } catch (error) {
    console.error('[courses/service] Unexpected error creating course:', error);
    throw error;
  }
}
```

### 5. UPDATE

```typescript
/**
 * Update an existing course
 * @param dto - Course update data
 * @returns Updated course entity
 */
static async updateCourse(dto: UpdateCourseDto): Promise<Course> {
  try {
    const { id, ...updates } = dto;

    // Add updated_at timestamp
    const updateData = {
      ...updates,
      updated_at: new Date().toISOString(),
    };

    const { data, error } = await this.supabase
      .from('courses')
      .update(updateData)
      .eq('id', id)
      .select()
      .single();

    if (error) {
      if (error.code === 'PGRST116') {
        throw new Error('Course not found');
      }

      if (error.code === '23505') {
        throw new Error('A course with this code already exists');
      }

      console.error('[courses/service] Error updating course:', error);
      throw new Error(`Failed to update course: ${error.message}`);
    }

    console.log('[courses/service] Updated course:', id);
    return data;
  } catch (error) {
    console.error('[courses/service] Unexpected error updating course:', error);
    throw error;
  }
}
```

### 6. DELETE (Soft Delete)

```typescript
/**
 * Soft delete a course by setting is_active to false
 * @param id - Course UUID
 * @returns Success boolean
 */
static async deleteCourse(id: string): Promise<boolean> {
  try {
    const { error } = await this.supabase
      .from('courses')
      .update({
        is_active: false,
        updated_at: new Date().toISOString(),
      })
      .eq('id', id);

    if (error) {
      console.error('[courses/service] Error deleting course:', error);
      throw new Error(`Failed to delete course: ${error.message}`);
    }

    console.log('[courses/service] Deleted course:', id);
    return true;
  } catch (error) {
    console.error('[courses/service] Unexpected error deleting course:', error);
    throw error;
  }
}
```

### 7. DELETE (Hard Delete)

```typescript
/**
 * Permanently delete a course
 * WARNING: This operation cannot be undone
 * @param id - Course UUID
 * @returns Success boolean
 */
static async permanentlyDeleteCourse(id: string): Promise<boolean> {
  try {
    const { error } = await this.supabase
      .from('courses')
      .delete()
      .eq('id', id);

    if (error) {
      console.error('[courses/service] Error permanently deleting course:', error);
      throw new Error(`Failed to delete course: ${error.message}`);
    }

    console.log('[courses/service] Permanently deleted course:', id);
    return true;
  } catch (error) {
    console.error('[courses/service] Unexpected error:', error);
    throw error;
  }
}
```

## Advanced Query Patterns

### Batch Operations

```typescript
/**
 * Create multiple courses in a single transaction
 * @param dtos - Array of course creation data
 * @returns Created courses
 */
static async createCourses(dtos: CreateCourseDto[]): Promise<Course[]> {
  try {
    const timestamp = new Date().toISOString();
    const coursesData = dtos.map(dto => ({
      ...dto,
      created_at: timestamp,
      updated_at: timestamp,
    }));

    const { data, error } = await this.supabase
      .from('courses')
      .insert(coursesData)
      .select();

    if (error) {
      console.error('[courses/service] Error creating multiple courses:', error);
      throw new Error(`Failed to create courses: ${error.message}`);
    }

    console.log('[courses/service] Created', data.length, 'courses');
    return data;
  } catch (error) {
    console.error('[courses/service] Unexpected error:', error);
    throw error;
  }
}
```

### Conditional Queries

```typescript
/**
 * Get courses with conditional joins
 * @param includeDepar tment - Whether to include department data
 * @param includeFaculty - Whether to include faculty data
 */
static async getCoursesWithRelations(
  filters: CourseFilters = {},
  includeDepar tment: boolean = false,
  includeFaculty: boolean = false
): Promise<Course[]> {
  try {
    // Build select clause dynamically
    let selectClause = '*';

    if (includeDepartment) {
      selectClause += ', department:departments(id, name, code)';
    }

    if (includeFaculty) {
      selectClause += ', faculty:users(id, name, email)';
    }

    let query = this.supabase
      .from('courses')
      .select(selectClause);

    // Apply filters
    if (filters.institution_id) {
      query = query.eq('institution_id', filters.institution_id);
    }

    const { data, error } = await query;

    if (error) {
      console.error('[courses/service] Error fetching courses with relations:', error);
      throw new Error(`Failed to fetch courses: ${error.message}`);
    }

    return data;
  } catch (error) {
    console.error('[courses/service] Unexpected error:', error);
    throw error;
  }
}
```

### Aggregation Queries

```typescript
/**
 * Get course statistics
 * @param institutionId - Institution UUID
 * @returns Course statistics
 */
static async getCourseStats(institutionId: string): Promise<CourseStats> {
  try {
    // Get total count
    const { count: totalCount, error: countError } = await this.supabase
      .from('courses')
      .select('*', { count: 'exact', head: true })
      .eq('institution_id', institutionId);

    if (countError) throw countError;

    // Get active count
    const { count: activeCount, error: activeError } = await this.supabase
      .from('courses')
      .select('*', { count: 'exact', head: true })
      .eq('institution_id', institutionId)
      .eq('is_active', true);

    if (activeError) throw activeError;

    // Get average credits
    const { data: avgData, error: avgError } = await this.supabase
      .rpc('get_average_credits', { institution_id: institutionId });

    if (avgError) throw avgError;

    return {
      total: totalCount || 0,
      active: activeCount || 0,
      inactive: (totalCount || 0) - (activeCount || 0),
      averageCredits: avgData || 0,
    };
  } catch (error) {
    console.error('[courses/service] Error fetching course stats:', error);
    throw error;
  }
}
```

### Search with Ranking

```typescript
/**
 * Full-text search with relevance ranking
 * @param searchTerm - Search term
 * @param institutionId - Institution UUID
 * @returns Ranked search results
 */
static async searchCourses(
  searchTerm: string,
  institutionId: string
): Promise<Course[]> {
  try {
    const { data, error } = await this.supabase
      .rpc('search_courses', {
        search_term: searchTerm,
        institution_id: institutionId
      });

    if (error) {
      console.error('[courses/service] Error searching courses:', error);
      throw new Error(`Search failed: ${error.message}`);
    }

    return data;
  } catch (error) {
    console.error('[courses/service] Unexpected error:', error);
    throw error;
  }
}

// Database function for full-text search
// CREATE FUNCTION search_courses(search_term text, institution_id uuid)
// RETURNS SETOF courses AS $$
// BEGIN
//   RETURN QUERY
//   SELECT *
//   FROM courses
//   WHERE courses.institution_id = search_courses.institution_id
//     AND (
//       to_tsvector('english', name) @@ plainto_tsquery('english', search_term)
//       OR to_tsvector('english', coalesce(description, '')) @@ plainto_tsquery('english', search_term)
//       OR code ILIKE '%' || search_term || '%'
//     )
//   ORDER BY
//     ts_rank(to_tsvector('english', name || ' ' || coalesce(description, '')), plainto_tsquery('english', search_term)) DESC;
// END;
// $$ LANGUAGE plpgsql;
```

## Error Handling Patterns

### Comprehensive Error Handling

```typescript
/**
 * Fetch course with detailed error handling
 */
static async getCourseWithErrorHandling(id: string): Promise<Course> {
  try {
    // Validate input
    if (!id || id.trim().length === 0) {
      throw new Error('Course ID is required');
    }

    // Execute query
    const { data, error } = await this.supabase
      .from('courses')
      .select('*')
      .eq('id', id)
      .single();

    // Handle Supabase errors
    if (error) {
      // Not found
      if (error.code === 'PGRST116') {
        throw new Error(`Course with ID ${id} not found`);
      }

      // Permission denied
      if (error.code === '42501') {
        throw new Error('You do not have permission to view this course');
      }

      // Network error
      if (error.message.includes('network')) {
        throw new Error('Network error. Please check your connection.');
      }

      // Generic error
      console.error('[courses/service] Supabase error:', error);
      throw new Error(`Database error: ${error.message}`);
    }

    // Validate response
    if (!data) {
      throw new Error('No data returned from database');
    }

    console.log('[courses/service] Successfully fetched course:', id);
    return data;

  } catch (error) {
    // Log for debugging
    console.error('[courses/service] Error in getCourseWithErrorHandling:', {
      courseId: id,
      error: error instanceof Error ? error.message : 'Unknown error',
      stack: error instanceof Error ? error.stack : undefined
    });

    // Re-throw for caller to handle
    throw error;
  }
}
```

### Custom Error Classes

```typescript
// Define custom error types
export class CourseNotFoundError extends Error {
  constructor(id: string) {
    super(`Course with ID ${id} not found`);
    this.name = 'CourseNotFoundError';
  }
}

export class CourseValidationError extends Error {
  constructor(message: string) {
    super(message);
    this.name = 'CourseValidationError';
  }
}

export class CoursePermissionError extends Error {
  constructor(message: string) {
    super(message);
    this.name = 'CoursePermissionError';
  }
}

// Use in service methods
static async getCourseById(id: string): Promise<Course> {
  try {
    if (!id) {
      throw new CourseValidationError('Course ID is required');
    }

    const { data, error } = await this.supabase
      .from('courses')
      .select('*')
      .eq('id', id)
      .single();

    if (error) {
      if (error.code === 'PGRST116') {
        throw new CourseNotFoundError(id);
      }
      if (error.code === '42501') {
        throw new CoursePermissionError('You do not have permission to view this course');
      }
      throw error;
    }

    return data;
  } catch (error) {
    console.error('[courses/service] Error fetching course:', error);
    throw error;
  }
}
```

## Transaction Patterns

### Using Supabase RPC for Transactions

```typescript
/**
 * Create course with enrollment limit
 * Uses database function to ensure atomicity
 */
static async createCourseWithEnrollmentLimit(
  courseDto: CreateCourseDto,
  maxEnrollment: number
): Promise<Course> {
  try {
    const { data, error } = await this.supabase
      .rpc('create_course_with_limit', {
        course_data: courseDto,
        max_enrollment: maxEnrollment
      });

    if (error) {
      console.error('[courses/service] Error creating course with limit:', error);
      throw new Error(`Failed to create course: ${error.message}`);
    }

    console.log('[courses/service] Created course with enrollment limit:', data.id);
    return data;
  } catch (error) {
    console.error('[courses/service] Unexpected error:', error);
    throw error;
  }
}

// Database function
// CREATE OR REPLACE FUNCTION create_course_with_limit(
//   course_data jsonb,
//   max_enrollment integer
// )
// RETURNS courses AS $$
// DECLARE
//   new_course courses;
// BEGIN
//   INSERT INTO courses (institution_id, name, code, credits)
//   VALUES (
//     (course_data->>'institution_id')::uuid,
//     course_data->>'name',
//     course_data->>'code',
//     (course_data->>'credits')::integer
//   )
//   RETURNING * INTO new_course;
//
//   INSERT INTO course_enrollment_limits (course_id, max_students)
//   VALUES (new_course.id, max_enrollment);
//
//   RETURN new_course;
// END;
// $$ LANGUAGE plpgsql;
```

## Caching Patterns

### In-Memory Cache

```typescript
export class CourseService {
  private static supabase = createClientSupabaseClient();
  private static cache = new Map<string, { data: Course; timestamp: number }>();
  private static CACHE_TTL = 5 * 60 * 1000; // 5 minutes

  /**
   * Get course by ID with caching
   */
  static async getCourseById(id: string, useCache: boolean = true): Promise<Course> {
    // Check cache
    if (useCache) {
      const cached = this.cache.get(id);
      if (cached && Date.now() - cached.timestamp < this.CACHE_TTL) {
        console.log('[courses/service] Returning cached course:', id);
        return cached.data;
      }
    }

    // Fetch from database
    const { data, error } = await this.supabase
      .from('courses')
      .select('*')
      .eq('id', id)
      .single();

    if (error) throw error;

    // Update cache
    this.cache.set(id, { data, timestamp: Date.now() });

    console.log('[courses/service] Fetched and cached course:', id);
    return data;
  }

  /**
   * Invalidate cache for a course
   */
  static invalidateCache(id: string): void {
    this.cache.delete(id);
    console.log('[courses/service] Invalidated cache for:', id);
  }

  /**
   * Clear entire cache
   */
  static clearCache(): void {
    this.cache.clear();
    console.log('[courses/service] Cleared all cache');
  }
}
```

## Testing Services

### Mock Service for Testing

```typescript
// __tests__/services/course-service.test.ts
import { CourseService } from '@/lib/services/courses/course-service';

// Mock Supabase client
jest.mock('@/lib/supabase/client', () => ({
  createClientSupabaseClient: jest.fn(() => ({
    from: jest.fn(() => ({
      select: jest.fn().mockReturnThis(),
      eq: jest.fn().mockReturnThis(),
      single: jest.fn().mockResolvedValue({
        data: { id: '123', name: 'Test Course' },
        error: null
      })
    }))
  }))
}));

describe('CourseService', () => {
  it('should fetch course by ID', async () => {
    const course = await CourseService.getCourseById('123');
    expect(course.id).toBe('123');
    expect(course.name).toBe('Test Course');
  });
});
```

## Summary Checklist

For every service method:

- [ ] Proper TypeScript typing for parameters and return values
- [ ] Try-catch error handling
- [ ] Descriptive error messages
- [ ] Console logging with module prefix
- [ ] Input validation where appropriate
- [ ] Supabase error code handling
- [ ] Documentation with JSDoc comments
- [ ] Consistent naming conventions
- [ ] Re-throw errors for caller handling
- [ ] Transaction safety for multi-step operations
- [ ] Pagination for list endpoints
- [ ] Filtering and sorting support
- [ ] Proper timestamp handling

This ensures all service methods are robust, maintainable, and consistent across the application.
