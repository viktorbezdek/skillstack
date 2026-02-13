# Page Patterns

## Next.js App Router Page Structures for MyJKKN

This document provides comprehensive patterns for creating pages using Next.js 15 App Router, Server Components, and the MyJKKN layout system.

## Page File Structure

Every module should have this page structure:

```
app/(routes)/[module]/
├── page.tsx                    # List view (Server Component)
├── loading.tsx                 # Loading state
├── error.tsx                   # Error boundary
├── new/
│   └── page.tsx               # Create form page
├── [id]/
│   ├── page.tsx               # Detail view (optional)
│   └── edit/
│       └── page.tsx           # Edit form page
└── _components/                # Module-specific components
```

## 1. List Page (Index)

**File**: `app/(routes)/[module]/page.tsx`

```typescript
import { Suspense } from 'react';
import { Metadata } from 'next';
import Link from 'next/link';
import { Plus } from 'lucide-react';
import { ContentLayout } from '@/components/layouts/content-layout';
import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbList,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from '@/components/ui/breadcrumb';
import { Button } from '@/components/ui/button';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Skeleton } from '@/components/ui/skeleton';
import { CourseService } from '@/lib/services/courses/course-service';
import { CourseDataTable } from './_components/course-data-table';
import { columns } from './_components/columns';
import { CanCreate } from '@/components/permissions/permission-guard';
import { getCurrentUser } from '@/lib/auth/get-current-user';

export const metadata: Metadata = {
  title: 'Courses | MyJKKN',
  description: 'Manage courses for your institution',
};

export default async function CoursesPage() {
  // Get current user for institution context
  const user = await getCurrentUser();

  // Fetch data on the server
  const coursesResponse = await CourseService.getCourses({
    institution_id: user.institution_id,
    is_active: true,
  });

  return (
    <ContentLayout title="Courses">
      {/* Breadcrumb Navigation */}
      <Breadcrumb>
        <BreadcrumbList>
          <BreadcrumbItem>
            <BreadcrumbLink href="/dashboard">Dashboard</BreadcrumbLink>
          </BreadcrumbItem>
          <BreadcrumbSeparator />
          <BreadcrumbItem>
            <BreadcrumbLink href="/academic">Academic</BreadcrumbLink>
          </BreadcrumbItem>
          <BreadcrumbSeparator />
          <BreadcrumbItem>
            <BreadcrumbPage>Courses</BreadcrumbPage>
          </BreadcrumbItem>
        </BreadcrumbList>
      </Breadcrumb>

      {/* Page Content */}
      <Card>
        <CardHeader className="flex flex-row items-center justify-between">
          <div>
            <CardTitle>Courses</CardTitle>
            <CardDescription>
              Manage courses for your institution. Total: {coursesResponse.total}
            </CardDescription>
          </div>

          <CanCreate module="academic.courses">
            <Button asChild>
              <Link href="/academic/courses/new">
                <Plus className="mr-2 h-4 w-4" />
                Add Course
              </Link>
            </Button>
          </CanCreate>
        </CardHeader>

        <CardContent>
          <Suspense fallback={<TableSkeleton />}>
            <CourseDataTable columns={columns} data={coursesResponse.data} />
          </Suspense>
        </CardContent>
      </Card>
    </ContentLayout>
  );
}

// Loading skeleton component
function TableSkeleton() {
  return (
    <div className="space-y-4">
      <Skeleton className="h-10 w-full" />
      <Skeleton className="h-[400px] w-full" />
    </div>
  );
}
```

## 2. Create Page

**File**: `app/(routes)/[module]/new/page.tsx`

```typescript
import { Metadata } from 'next';
import { redirect } from 'next/navigation';
import { ContentLayout } from '@/components/layouts/content-layout';
import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbList,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from '@/components/ui/breadcrumb';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { CourseForm } from '../_components/course-form';
import { DepartmentService } from '@/lib/services/academic/department-service';
import { PermissionGuard } from '@/components/permissions/permission-guard';
import { getCurrentUser } from '@/lib/auth/get-current-user';

export const metadata: Metadata = {
  title: 'New Course | MyJKKN',
  description: 'Create a new course',
};

export default async function NewCoursePage() {
  // Get current user
  const user = await getCurrentUser();

  // Check permissions (alternative to component-level guard)
  if (!user.permissions.includes('academic.courses.create')) {
    redirect('/dashboard');
  }

  // Fetch related data needed for the form
  const departments = await DepartmentService.getDepartments({
    institution_id: user.institution_id,
    is_active: true,
  });

  return (
    <ContentLayout title="New Course">
      {/* Breadcrumb Navigation */}
      <Breadcrumb>
        <BreadcrumbList>
          <BreadcrumbItem>
            <BreadcrumbLink href="/dashboard">Dashboard</BreadcrumbLink>
          </BreadcrumbItem>
          <BreadcrumbSeparator />
          <BreadcrumbItem>
            <BreadcrumbLink href="/academic">Academic</BreadcrumbLink>
          </BreadcrumbItem>
          <BreadcrumbSeparator />
          <BreadcrumbItem>
            <BreadcrumbLink href="/academic/courses">Courses</BreadcrumbLink>
          </BreadcrumbItem>
          <BreadcrumbSeparator />
          <BreadcrumbItem>
            <BreadcrumbPage>New</BreadcrumbPage>
          </BreadcrumbItem>
        </BreadcrumbList>
      </Breadcrumb>

      {/* Page Content */}
      <Card>
        <CardHeader>
          <CardTitle>Create New Course</CardTitle>
          <CardDescription>
            Add a new course to your institution's curriculum
          </CardDescription>
        </CardHeader>

        <CardContent>
          <CourseForm
            mode="create"
            departments={departments.data}
            institutionId={user.institution_id}
          />
        </CardContent>
      </Card>
    </ContentLayout>
  );
}
```

## 3. Edit Page

**File**: `app/(routes)/[module]/[id]/edit/page.tsx`

```typescript
import { Metadata } from 'next';
import { notFound, redirect } from 'next/navigation';
import { ContentLayout } from '@/components/layouts/content-layout';
import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbList,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from '@/components/ui/breadcrumb';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { CourseForm } from '../../_components/course-form';
import { CourseService } from '@/lib/services/courses/course-service';
import { DepartmentService } from '@/lib/services/academic/department-service';
import { getCurrentUser } from '@/lib/auth/get-current-user';

export const metadata: Metadata = {
  title: 'Edit Course | MyJKKN',
  description: 'Edit course details',
};

interface EditCoursePageProps {
  params: {
    id: string;
  };
}

export default async function EditCoursePage({ params }: EditCoursePageProps) {
  const { id } = params;

  // Get current user
  const user = await getCurrentUser();

  // Check permissions
  if (!user.permissions.includes('academic.courses.edit')) {
    redirect('/dashboard');
  }

  // Fetch course data
  let course;
  try {
    course = await CourseService.getCourseById(id);
  } catch (error) {
    console.error('[edit-course-page] Error fetching course:', error);
    notFound();
  }

  // Verify user has access to this institution's data
  if (course.institution_id !== user.institution_id) {
    redirect('/dashboard');
  }

  // Fetch departments for form
  const departments = await DepartmentService.getDepartments({
    institution_id: user.institution_id,
    is_active: true,
  });

  return (
    <ContentLayout title={`Edit ${course.name}`}>
      {/* Breadcrumb Navigation */}
      <Breadcrumb>
        <BreadcrumbList>
          <BreadcrumbItem>
            <BreadcrumbLink href="/dashboard">Dashboard</BreadcrumbLink>
          </BreadcrumbItem>
          <BreadcrumbSeparator />
          <BreadcrumbItem>
            <BreadcrumbLink href="/academic">Academic</BreadcrumbLink>
          </BreadcrumbItem>
          <BreadcrumbSeparator />
          <BreadcrumbItem>
            <BreadcrumbLink href="/academic/courses">Courses</BreadcrumbLink>
          </BreadcrumbItem>
          <BreadcrumbSeparator />
          <BreadcrumbItem>
            <BreadcrumbPage>Edit</BreadcrumbPage>
          </BreadcrumbItem>
        </BreadcrumbList>
      </Breadcrumb>

      {/* Page Content */}
      <Card>
        <CardHeader>
          <CardTitle>Edit Course</CardTitle>
          <CardDescription>
            Update course details for {course.code}
          </CardDescription>
        </CardHeader>

        <CardContent>
          <CourseForm
            mode="edit"
            initialData={course}
            departments={departments.data}
            institutionId={user.institution_id}
          />
        </CardContent>
      </Card>
    </ContentLayout>
  );
}
```

## 4. Detail Page (Optional)

**File**: `app/(routes)/[module]/[id]/page.tsx`

```typescript
import { Metadata } from 'next';
import { notFound, redirect } from 'next/navigation';
import Link from 'next/link';
import { Pencil, ArrowLeft } from 'lucide-react';
import { ContentLayout } from '@/components/layouts/content-layout';
import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbList,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from '@/components/ui/breadcrumb';
import { Button } from '@/components/ui/button';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { CourseService } from '@/lib/services/courses/course-service';
import { CanEdit } from '@/components/permissions/permission-guard';
import { getCurrentUser } from '@/lib/auth/get-current-user';

interface CourseDetailPageProps {
  params: {
    id: string;
  };
}

export async function generateMetadata({ params }: CourseDetailPageProps): Promise<Metadata> {
  const course = await CourseService.getCourseById(params.id);
  return {
    title: `${course.name} | MyJKKN`,
    description: course.description || `Details for ${course.name}`,
  };
}

export default async function CourseDetailPage({ params }: CourseDetailPageProps) {
  const { id } = params;
  const user = await getCurrentUser();

  // Fetch course data
  let course;
  try {
    course = await CourseService.getCourseById(id);
  } catch (error) {
    notFound();
  }

  // Verify access
  if (course.institution_id !== user.institution_id) {
    redirect('/dashboard');
  }

  return (
    <ContentLayout title={course.name}>
      {/* Breadcrumb Navigation */}
      <Breadcrumb>
        <BreadcrumbList>
          <BreadcrumbItem>
            <BreadcrumbLink href="/dashboard">Dashboard</BreadcrumbLink>
          </BreadcrumbItem>
          <BreadcrumbSeparator />
          <BreadcrumbItem>
            <BreadcrumbLink href="/academic">Academic</BreadcrumbLink>
          </BreadcrumbItem>
          <BreadcrumbSeparator />
          <BreadcrumbItem>
            <BreadcrumbLink href="/academic/courses">Courses</BreadcrumbLink>
          </BreadcrumbItem>
          <BreadcrumbSeparator />
          <BreadcrumbItem>
            <BreadcrumbPage>{course.code}</BreadcrumbPage>
          </BreadcrumbItem>
        </BreadcrumbList>
      </Breadcrumb>

      {/* Page Content */}
      <div className="space-y-4">
        {/* Actions */}
        <div className="flex items-center justify-between">
          <Button variant="ghost" asChild>
            <Link href="/academic/courses">
              <ArrowLeft className="mr-2 h-4 w-4" />
              Back to Courses
            </Link>
          </Button>

          <CanEdit module="academic.courses">
            <Button asChild>
              <Link href={`/academic/courses/${id}/edit`}>
                <Pencil className="mr-2 h-4 w-4" />
                Edit Course
              </Link>
            </Button>
          </CanEdit>
        </div>

        {/* Course Details Card */}
        <Card>
          <CardHeader>
            <div className="flex items-start justify-between">
              <div>
                <CardTitle className="text-3xl">{course.name}</CardTitle>
                <CardDescription className="text-lg mt-2">
                  {course.code} • {course.credits} Credits
                </CardDescription>
              </div>
              <Badge variant={course.is_active ? 'default' : 'secondary'}>
                {course.is_active ? 'Active' : 'Inactive'}
              </Badge>
            </div>
          </CardHeader>

          <CardContent className="space-y-6">
            {/* Description */}
            {course.description && (
              <div>
                <h3 className="font-semibold mb-2">Description</h3>
                <p className="text-muted-foreground">{course.description}</p>
              </div>
            )}

            {/* Metadata */}
            <div className="grid gap-4 md:grid-cols-2">
              <div>
                <h4 className="text-sm font-medium text-muted-foreground">Created</h4>
                <p className="text-sm">
                  {new Date(course.created_at).toLocaleDateString()}
                </p>
              </div>
              <div>
                <h4 className="text-sm font-medium text-muted-foreground">Last Updated</h4>
                <p className="text-sm">
                  {new Date(course.updated_at).toLocaleDateString()}
                </p>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>
    </ContentLayout>
  );
}
```

## 5. Loading State

**File**: `app/(routes)/[module]/loading.tsx`

```typescript
import { ContentLayout } from '@/components/layouts/content-layout';
import { Card, CardContent, CardHeader } from '@/components/ui/card';
import { Skeleton } from '@/components/ui/skeleton';

export default function Loading() {
  return (
    <ContentLayout title="Loading...">
      <Skeleton className="h-8 w-64 mb-6" />

      <Card>
        <CardHeader>
          <Skeleton className="h-8 w-48" />
          <Skeleton className="h-4 w-64 mt-2" />
        </CardHeader>

        <CardContent>
          <div className="space-y-4">
            <Skeleton className="h-10 w-full" />
            <Skeleton className="h-[400px] w-full" />
          </div>
        </CardContent>
      </Card>
    </ContentLayout>
  );
}
```

## 6. Error Boundary

**File**: `app/(routes)/[module]/error.tsx`

```typescript
'use client';

import { useEffect } from 'react';
import { ContentLayout } from '@/components/layouts/content-layout';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { AlertCircle } from 'lucide-react';

export default function Error({
  error,
  reset,
}: {
  error: Error & { digest?: string };
  reset: () => void;
}) {
  useEffect(() => {
    console.error('[courses/error] Error:', error);
  }, [error]);

  return (
    <ContentLayout title="Error">
      <Card>
        <CardHeader>
          <div className="flex items-center gap-2">
            <AlertCircle className="h-6 w-6 text-destructive" />
            <CardTitle>Something went wrong</CardTitle>
          </div>
          <CardDescription>
            An error occurred while loading this page
          </CardDescription>
        </CardHeader>

        <CardContent className="space-y-4">
          <div className="rounded-lg bg-muted p-4">
            <p className="text-sm text-muted-foreground font-mono">
              {error.message}
            </p>
          </div>

          <Button onClick={reset}>Try Again</Button>
        </CardContent>
      </Card>
    </ContentLayout>
  );
}
```

## 7. Not Found Page

**File**: `app/(routes)/[module]/not-found.tsx`

```typescript
import Link from 'next/link';
import { ContentLayout } from '@/components/layouts/content-layout';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { FileQuestion } from 'lucide-react';

export default function NotFound() {
  return (
    <ContentLayout title="Not Found">
      <Card>
        <CardHeader>
          <div className="flex items-center gap-2">
            <FileQuestion className="h-6 w-6 text-muted-foreground" />
            <CardTitle>Course Not Found</CardTitle>
          </div>
          <CardDescription>
            The course you're looking for doesn't exist or has been removed
          </CardDescription>
        </CardHeader>

        <CardContent>
          <Button asChild>
            <Link href="/academic/courses">Back to Courses</Link>
          </Button>
        </CardContent>
      </Card>
    </ContentLayout>
  );
}
```

## Page Patterns Summary

### Server Component Pattern
```typescript
// ✅ Fetch data on server
export default async function Page() {
  const data = await Service.getData();
  return <Component data={data} />;
}
```

### Dynamic Route Parameters
```typescript
interface PageProps {
  params: { id: string };
  searchParams: { [key: string]: string | string[] | undefined };
}

export default async function Page({ params, searchParams }: PageProps) {
  // Use params.id and searchParams
}
```

### Metadata Generation
```typescript
export async function generateMetadata({ params }: PageProps): Promise<Metadata> {
  const data = await fetchData(params.id);
  return {
    title: `${data.name} | MyJKKN`,
    description: data.description,
  };
}
```

## Summary Checklist

For every page:

- [ ] Use Server Components by default
- [ ] Include proper breadcrumb navigation
- [ ] Use ContentLayout wrapper
- [ ] Implement loading.tsx for loading states
- [ ] Implement error.tsx for error boundaries
- [ ] Add metadata for SEO
- [ ] Apply permission checks
- [ ] Verify institution_id access
- [ ] Handle not found cases
- [ ] Use proper TypeScript types
- [ ] Include console logging for errors
- [ ] Refresh router after mutations

This ensures all pages are consistent, secure, and provide excellent UX.
