# Hooks Patterns

## React Hooks for Data Management in MyJKKN

This document provides comprehensive patterns for creating custom React hooks to manage state, data fetching, and side effects in Next.js client components.

## Basic Data Fetching Hook

### List Hook with Pagination

```typescript
'use client';

import { useState, useEffect, useCallback } from 'react';
import { CourseService } from '@/lib/services/courses/course-service';
import type { Course, CourseFilters } from '@/types/courses';
import { usePermissions } from '@/hooks/use-permissions';
import { toast } from 'sonner';

export function useCourses(initialFilters: CourseFilters = {}) {
  // State
  const [courses, setCourses] = useState<Course[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [total, setTotal] = useState(0);
  const [page, setPage] = useState(1);
  const pageSize = 10;

  // Get user context
  const { userProfile } = usePermissions();

  // Fetch function
  const fetchCourses = useCallback(async () => {
    try {
      setLoading(true);
      setError(null);

      // Auto-apply institution filter from user context
      const effectiveFilters: CourseFilters = {
        ...initialFilters,
        institution_id: initialFilters.institution_id || userProfile?.institution_id
      };

      const response = await CourseService.getCourses(
        effectiveFilters,
        page,
        pageSize
      );

      setCourses(response.data);
      setTotal(response.total);

      console.log('[hooks/courses] Fetched', response.data.length, 'courses');
    } catch (err) {
      const message = err instanceof Error ? err.message : 'Failed to fetch courses';
      setError(message);
      toast.error(message);
      console.error('[hooks/courses] Fetch error:', err);
    } finally {
      setLoading(false);
    }
  }, [initialFilters, page, pageSize, userProfile?.institution_id]);

  // Fetch on mount and when dependencies change
  useEffect(() => {
    if (userProfile?.institution_id) {
      fetchCourses();
    }
  }, [fetchCourses, userProfile?.institution_id]);

  return {
    courses,
    loading,
    error,
    total,
    page,
    setPage,
    pageSize,
    totalPages: Math.ceil(total / pageSize),
    refetch: fetchCourses
  };
}
```

### Single Item Hook

```typescript
'use client';

import { useState, useEffect } from 'react';
import { CourseService } from '@/lib/services/courses/course-service';
import type { Course } from '@/types/courses';
import { toast } from 'sonner';

export function useCourse(id: string | null) {
  const [course, setCourse] = useState<Course | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!id) {
      setCourse(null);
      return;
    }

    const fetchCourse = async () => {
      try {
        setLoading(true);
        setError(null);

        const data = await CourseService.getCourseById(id);
        setCourse(data);

        console.log('[hooks/course] Fetched course:', id);
      } catch (err) {
        const message = err instanceof Error ? err.message : 'Failed to fetch course';
        setError(message);
        toast.error(message);
        console.error('[hooks/course] Fetch error:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchCourse();
  }, [id]);

  return { course, loading, error };
}
```

## Mutation Hooks

### Create Hook

```typescript
'use client';

import { useState } from 'react';
import { CourseService } from '@/lib/services/courses/course-service';
import type { CreateCourseDto, Course } from '@/types/courses';
import { toast } from 'sonner';
import { useRouter } from 'next/navigation';

export function useCreateCourse() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const router = useRouter();

  const createCourse = async (dto: CreateCourseDto): Promise<Course | null> => {
    try {
      setLoading(true);
      setError(null);

      const course = await CourseService.createCourse(dto);

      toast.success('Course created successfully');
      console.log('[hooks/create-course] Created:', course.id);

      // Redirect to list page
      router.push('/academic/courses');
      router.refresh(); // Refresh server components

      return course;
    } catch (err) {
      const message = err instanceof Error ? err.message : 'Failed to create course';
      setError(message);
      toast.error(message);
      console.error('[hooks/create-course] Error:', err);
      return null;
    } finally {
      setLoading(false);
    }
  };

  return {
    createCourse,
    loading,
    error
  };
}
```

### Update Hook

```typescript
'use client';

import { useState } from 'react';
import { CourseService } from '@/lib/services/courses/course-service';
import type { UpdateCourseDto, Course } from '@/types/courses';
import { toast } from 'sonner';
import { useRouter } from 'next/navigation';

export function useUpdateCourse() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const router = useRouter();

  const updateCourse = async (dto: UpdateCourseDto): Promise<Course | null> => {
    try {
      setLoading(true);
      setError(null);

      const course = await CourseService.updateCourse(dto);

      toast.success('Course updated successfully');
      console.log('[hooks/update-course] Updated:', dto.id);

      // Refresh to show updated data
      router.refresh();

      return course;
    } catch (err) {
      const message = err instanceof Error ? err.message : 'Failed to update course';
      setError(message);
      toast.error(message);
      console.error('[hooks/update-course] Error:', err);
      return null;
    } finally {
      setLoading(false);
    }
  };

  return {
    updateCourse,
    loading,
    error
  };
}
```

### Delete Hook

```typescript
'use client';

import { useState } from 'react';
import { CourseService } from '@/lib/services/courses/course-service';
import { toast } from 'sonner';
import { useRouter } from 'next/navigation';

export function useDeleteCourse() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const router = useRouter();

  const deleteCourse = async (id: string): Promise<boolean> => {
    try {
      setLoading(true);
      setError(null);

      await CourseService.deleteCourse(id);

      toast.success('Course deleted successfully');
      console.log('[hooks/delete-course] Deleted:', id);

      // Refresh to update the list
      router.refresh();

      return true;
    } catch (err) {
      const message = err instanceof Error ? err.message : 'Failed to delete course';
      setError(message);
      toast.error(message);
      console.error('[hooks/delete-course] Error:', err);
      return false;
    } finally {
      setLoading(false);
    }
  };

  return {
    deleteCourse,
    loading,
    error
  };
}
```

## Advanced Hook Patterns

### Debounced Search Hook

```typescript
'use client';

import { useState, useEffect, useCallback } from 'react';
import { CourseService } from '@/lib/services/courses/course-service';
import type { Course } from '@/types/courses';
import { useDebounce } from '@/hooks/use-debounce';

export function useCourseSearch() {
  const [searchTerm, setSearchTerm] = useState('');
  const [results, setResults] = useState<Course[]>([]);
  const [loading, setLoading] = useState(false);

  // Debounce search term
  const debouncedSearch = useDebounce(searchTerm, 500);

  const search = useCallback(async (term: string) => {
    if (!term || term.trim().length < 2) {
      setResults([]);
      return;
    }

    try {
      setLoading(true);

      const response = await CourseService.getCourses({ search: term });
      setResults(response.data);

      console.log('[hooks/course-search] Found', response.data.length, 'results');
    } catch (err) {
      console.error('[hooks/course-search] Error:', err);
      setResults([]);
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    search(debouncedSearch);
  }, [debouncedSearch, search]);

  return {
    searchTerm,
    setSearchTerm,
    results,
    loading
  };
}
```

### Optimistic Update Hook

```typescript
'use client';

import { useState, useTransition } from 'react';
import { CourseService } from '@/lib/services/courses/course-service';
import type { Course, UpdateCourseDto } from '@/types/courses';
import { toast } from 'sonner';

export function useOptimisticCourse(initialCourse: Course) {
  const [course, setCourse] = useState(initialCourse);
  const [isPending, startTransition] = useTransition();

  const updateCourse = async (updates: Partial<UpdateCourseDto>) => {
    // Optimistically update UI
    const previousCourse = course;
    setCourse({ ...course, ...updates });

    try {
      // Perform actual update
      const updated = await CourseService.updateCourse({
        id: course.id,
        ...updates
      });

      // Update with server response
      startTransition(() => {
        setCourse(updated);
      });

      toast.success('Course updated');
    } catch (err) {
      // Revert on error
      setCourse(previousCourse);
      toast.error('Failed to update course');
      console.error('[hooks/optimistic-course] Error:', err);
    }
  };

  return {
    course,
    updateCourse,
    isPending
  };
}
```

### Infinite Scroll Hook

```typescript
'use client';

import { useState, useEffect, useCallback, useRef } from 'react';
import { CourseService } from '@/lib/services/courses/course-service';
import type { Course, CourseFilters } from '@/types/courses';
import { toast } from 'sonner';

export function useInfiniteCourses(filters: CourseFilters = {}) {
  const [courses, setCourses] = useState<Course[]>([]);
  const [page, setPage] = useState(1);
  const [hasMore, setHasMore] = useState(true);
  const [loading, setLoading] = useState(false);
  const observer = useRef<IntersectionObserver | null>(null);

  const loadMore = useCallback(async () => {
    if (loading || !hasMore) return;

    try {
      setLoading(true);

      const response = await CourseService.getCourses(filters, page, 20);

      setCourses(prev => [...prev, ...response.data]);
      setHasMore(response.data.length === 20);
      setPage(prev => prev + 1);

      console.log('[hooks/infinite-courses] Loaded page', page);
    } catch (err) {
      toast.error('Failed to load more courses');
      console.error('[hooks/infinite-courses] Error:', err);
    } finally {
      setLoading(false);
    }
  }, [filters, page, hasMore, loading]);

  // Intersection observer callback
  const lastCourseRef = useCallback((node: HTMLElement | null) => {
    if (loading) return;

    if (observer.current) observer.current.disconnect();

    observer.current = new IntersectionObserver(entries => {
      if (entries[0].isIntersecting && hasMore) {
        loadMore();
      }
    });

    if (node) observer.current.observe(node);
  }, [loading, hasMore, loadMore]);

  return {
    courses,
    loading,
    hasMore,
    lastCourseRef
  };
}
```

## Form Integration Hooks

### React Hook Form Integration

```typescript
'use client';

import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';
import type { CreateCourseDto } from '@/types/courses';
import { useCreateCourse } from './use-create-course';

const CourseFormSchema = z.object({
  code: z.string().min(1, 'Code is required').max(50),
  name: z.string().min(1, 'Name is required').max(255),
  description: z.string().optional(),
  credits: z.coerce.number().int().min(0).max(10),
  department_id: z.string().uuid('Select a department'),
});

type CourseFormData = z.infer<typeof CourseFormSchema>;

export function useCourseForm(institutionId: string) {
  const { createCourse, loading } = useCreateCourse();

  const form = useForm<CourseFormData>({
    resolver: zodResolver(CourseFormSchema),
    defaultValues: {
      code: '',
      name: '',
      description: '',
      credits: 3,
      department_id: '',
    },
  });

  const onSubmit = async (data: CourseFormData) => {
    const dto: CreateCourseDto = {
      ...data,
      institution_id: institutionId,
    };

    await createCourse(dto);
  };

  return {
    form,
    onSubmit: form.handleSubmit(onSubmit),
    loading
  };
}
```

## Real-time Data Hooks

### Supabase Real-time Hook

```typescript
'use client';

import { useState, useEffect } from 'react';
import { createClientSupabaseClient } from '@/lib/supabase/client';
import type { Course } from '@/types/courses';
import { toast } from 'sonner';

export function useCourseRealtime(institutionId: string) {
  const [courses, setCourses] = useState<Course[]>([]);
  const supabase = createClientSupabaseClient();

  useEffect(() => {
    // Initial fetch
    const fetchCourses = async () => {
      const { data } = await supabase
        .from('courses')
        .select('*')
        .eq('institution_id', institutionId);

      if (data) setCourses(data);
    };

    fetchCourses();

    // Subscribe to changes
    const channel = supabase
      .channel('courses_changes')
      .on(
        'postgres_changes',
        {
          event: '*',
          schema: 'public',
          table: 'courses',
          filter: `institution_id=eq.${institutionId}`
        },
        (payload) => {
          console.log('[hooks/course-realtime] Change detected:', payload);

          if (payload.eventType === 'INSERT') {
            setCourses(prev => [...prev, payload.new as Course]);
            toast.success('New course added');
          } else if (payload.eventType === 'UPDATE') {
            setCourses(prev =>
              prev.map(c => c.id === payload.new.id ? payload.new as Course : c)
            );
          } else if (payload.eventType === 'DELETE') {
            setCourses(prev => prev.filter(c => c.id !== payload.old.id));
            toast.info('Course removed');
          }
        }
      )
      .subscribe();

    return () => {
      supabase.removeChannel(channel);
    };
  }, [institutionId, supabase]);

  return { courses };
}
```

## State Management Hooks

### Local Storage Sync Hook

```typescript
'use client';

import { useState, useEffect } from 'react';

export function useLocalStorage<T>(key: string, initialValue: T) {
  const [value, setValue] = useState<T>(() => {
    if (typeof window === 'undefined') return initialValue;

    try {
      const item = window.localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch (error) {
      console.error('[hooks/local-storage] Error reading:', error);
      return initialValue;
    }
  });

  useEffect(() => {
    try {
      window.localStorage.setItem(key, JSON.stringify(value));
    } catch (error) {
      console.error('[hooks/local-storage] Error saving:', error);
    }
  }, [key, value]);

  return [value, setValue] as const;
}

// Usage
export function useCourseFilters() {
  const [filters, setFilters] = useLocalStorage<CourseFilters>(
    'course-filters',
    { is_active: true }
  );

  return { filters, setFilters };
}
```

## Hook Testing

### Testing Custom Hooks

```typescript
// __tests__/hooks/use-courses.test.tsx
import { renderHook, waitFor } from '@testing-library/react';
import { useCourses } from '@/hooks/courses/use-courses';

// Mock service
jest.mock('@/lib/services/courses/course-service', () => ({
  CourseService: {
    getCourses: jest.fn().mockResolvedValue({
      data: [
        { id: '1', name: 'Course 1' },
        { id: '2', name: 'Course 2' }
      ],
      total: 2,
      page: 1,
      pageSize: 10
    })
  }
}));

describe('useCourses', () => {
  it('should fetch courses', async () => {
    const { result } = renderHook(() => useCourses());

    expect(result.current.loading).toBe(true);

    await waitFor(() => {
      expect(result.current.loading).toBe(false);
    });

    expect(result.current.courses).toHaveLength(2);
    expect(result.current.total).toBe(2);
  });

  it('should handle pagination', async () => {
    const { result } = renderHook(() => useCourses());

    await waitFor(() => {
      expect(result.current.loading).toBe(false);
    });

    result.current.setPage(2);

    await waitFor(() => {
      expect(result.current.page).toBe(2);
    });
  });
});
```

## Hook Organization

### Folder Structure

```
hooks/
├── courses/
│   ├── use-courses.ts           # List hook
│   ├── use-course.ts            # Single item hook
│   ├── use-create-course.ts     # Create mutation
│   ├── use-update-course.ts     # Update mutation
│   ├── use-delete-course.ts     # Delete mutation
│   ├── use-course-form.ts       # Form integration
│   └── use-course-search.ts     # Search hook
└── shared/
    ├── use-debounce.ts          # Debounce utility
    ├── use-local-storage.ts     # Local storage sync
    └── use-permissions.ts       # Permission checking
```

## Summary Checklist

For every hook:

- [ ] Use 'use client' directive
- [ ] Proper TypeScript types for params and returns
- [ ] Loading and error state management
- [ ] Toast notifications for user feedback
- [ ] Console logging with module prefix
- [ ] Cleanup in useEffect return functions
- [ ] Dependencies array optimization
- [ ] Re-fetch capability
- [ ] Integration with user context (permissions, institution)
- [ ] Error handling with try-catch
- [ ] Router integration for navigation
- [ ] Proper return type interfaces

This ensures all hooks are consistent, performant, and maintainable.
