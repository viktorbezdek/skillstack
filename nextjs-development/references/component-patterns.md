# Component Patterns

## Complete UI Component Guide for MyJKKN

This document provides comprehensive patterns for building UI components using Shadcn/UI, TanStack Table, React Hook Form, and Zod validation.

## Component File Structure

For every module, create these components in `app/(routes)/[module]/_components/`:

```
_components/
├── data-table-schema.ts         # Zod validation schema
├── columns.tsx                   # TanStack Table column definitions
├── [entity]-data-table.tsx       # Data table wrapper component
├── [entity]-form.tsx             # Create/Edit form
├── [entity]-filters.tsx          # Search and filter controls
└── row-actions.tsx               # Edit/Delete action menu
```

## 1. Zod Validation Schema

**File**: `data-table-schema.ts`

```typescript
import { z } from 'zod';

// Schema for course entity
export const courseSchema = z.object({
  id: z.string().uuid(),
  institution_id: z.string().uuid(),
  department_id: z.string().uuid(),
  code: z.string().min(1).max(50),
  name: z.string().min(1).max(255),
  description: z.string().nullable(),
  credits: z.number().int().min(0).max(10),
  is_active: z.boolean(),
  created_at: z.string(),
  updated_at: z.string(),
});

export type CourseRow = z.infer<typeof courseSchema>;

// Form validation schema (stricter rules)
export const courseFormSchema = z.object({
  code: z.string()
    .min(1, 'Code is required')
    .max(50, 'Code must be less than 50 characters')
    .regex(/^[A-Z0-9-]+$/, 'Code must contain only uppercase letters, numbers, and hyphens'),
  name: z.string()
    .min(1, 'Name is required')
    .max(255, 'Name must be less than 255 characters'),
  description: z.string().optional(),
  credits: z.coerce.number()
    .int('Credits must be a whole number')
    .min(0, 'Credits cannot be negative')
    .max(10, 'Credits cannot exceed 10'),
  department_id: z.string()
    .uuid('Please select a department'),
});

export type CourseFormValues = z.infer<typeof courseFormSchema>;
```

## 2. Table Column Definitions

**File**: `columns.tsx`

```typescript
'use client';

import { ColumnDef } from '@tanstack/react-table';
import { Checkbox } from '@/components/ui/checkbox';
import { Badge } from '@/components/ui/badge';
import { Button } from '@/components/ui/button';
import { ArrowUpDown } from 'lucide-react';
import type { Course } from '@/types/courses';
import { RowActions } from './row-actions';

export const columns: ColumnDef<Course>[] = [
  // Selection column
  {
    id: 'select',
    header: ({ table }) => (
      <Checkbox
        checked={table.getIsAllPageRowsSelected()}
        onCheckedChange={(value) => table.toggleAllPageRowsSelected(!!value)}
        aria-label="Select all"
      />
    ),
    cell: ({ row }) => (
      <Checkbox
        checked={row.getIsSelected()}
        onCheckedChange={(value) => row.toggleSelected(!!value)}
        aria-label="Select row"
      />
    ),
    enableSorting: false,
    enableHiding: false,
  },

  // Code column with sorting
  {
    accessorKey: 'code',
    header: ({ column }) => (
      <Button
        variant="ghost"
        onClick={() => column.toggleSorting(column.getIsSorted() === 'asc')}
      >
        Code
        <ArrowUpDown className="ml-2 h-4 w-4" />
      </Button>
    ),
    cell: ({ row }) => (
      <div className="font-medium">{row.getValue('code')}</div>
    ),
  },

  // Name column
  {
    accessorKey: 'name',
    header: ({ column }) => (
      <Button
        variant="ghost"
        onClick={() => column.toggleSorting(column.getIsSorted() === 'asc')}
      >
        Name
        <ArrowUpDown className="ml-2 h-4 w-4" />
      </Button>
    ),
    cell: ({ row }) => {
      const name = row.getValue('name') as string;
      const description = row.original.description;
      return (
        <div>
          <div className="font-medium">{name}</div>
          {description && (
            <div className="text-sm text-muted-foreground line-clamp-1">
              {description}
            </div>
          )}
        </div>
      );
    },
  },

  // Credits column
  {
    accessorKey: 'credits',
    header: 'Credits',
    cell: ({ row }) => (
      <div className="text-center">{row.getValue('credits')}</div>
    ),
  },

  // Status column
  {
    accessorKey: 'is_active',
    header: 'Status',
    cell: ({ row }) => {
      const isActive = row.getValue('is_active') as boolean;
      return (
        <Badge variant={isActive ? 'default' : 'secondary'}>
          {isActive ? 'Active' : 'Inactive'}
        </Badge>
      );
    },
    filterFn: (row, id, value) => {
      return value.includes(row.getValue(id));
    },
  },

  // Created date column
  {
    accessorKey: 'created_at',
    header: 'Created',
    cell: ({ row }) => {
      const date = new Date(row.getValue('created_at'));
      return (
        <div className="text-sm text-muted-foreground">
          {date.toLocaleDateString()}
        </div>
      );
    },
  },

  // Actions column
  {
    id: 'actions',
    cell: ({ row }) => <RowActions row={row} />,
    enableHiding: false,
  },
];
```

## 3. Data Table Component

**File**: `[entity]-data-table.tsx`

```typescript
'use client';

import { useState } from 'react';
import {
  ColumnDef,
  ColumnFiltersState,
  SortingState,
  VisibilityState,
  flexRender,
  getCoreRowModel,
  getFilteredRowModel,
  getPaginationRowModel,
  getSortedRowModel,
  useReactTable,
} from '@tanstack/react-table';
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from '@/components/ui/table';
import {
  DropdownMenu,
  DropdownMenuCheckboxItem,
  DropdownMenuContent,
  DropdownMenuTrigger,
} from '@/components/ui/dropdown-menu';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { ChevronDown } from 'lucide-react';

interface DataTableProps<TData, TValue> {
  columns: ColumnDef<TData, TValue>[];
  data: TData[];
}

export function CourseDataTable<TData, TValue>({
  columns,
  data,
}: DataTableProps<TData, TValue>) {
  const [sorting, setSorting] = useState<SortingState>([]);
  const [columnFilters, setColumnFilters] = useState<ColumnFiltersState>([]);
  const [columnVisibility, setColumnVisibility] = useState<VisibilityState>({});
  const [rowSelection, setRowSelection] = useState({});

  const table = useReactTable({
    data,
    columns,
    onSortingChange: setSorting,
    onColumnFiltersChange: setColumnFilters,
    getCoreRowModel: getCoreRowModel(),
    getPaginationRowModel: getPaginationRowModel(),
    getSortedRowModel: getSortedRowModel(),
    getFilteredRowModel: getFilteredRowModel(),
    onColumnVisibilityChange: setColumnVisibility,
    onRowSelectionChange: setRowSelection,
    state: {
      sorting,
      columnFilters,
      columnVisibility,
      rowSelection,
    },
  });

  return (
    <div className="space-y-4">
      {/* Toolbar */}
      <div className="flex items-center justify-between">
        <div className="flex flex-1 items-center space-x-2">
          <Input
            placeholder="Search courses..."
            value={(table.getColumn('name')?.getFilterValue() as string) ?? ''}
            onChange={(event) =>
              table.getColumn('name')?.setFilterValue(event.target.value)
            }
            className="h-8 w-[150px] lg:w-[250px]"
          />
        </div>

        <DropdownMenu>
          <DropdownMenuTrigger asChild>
            <Button variant="outline" size="sm" className="ml-auto">
              Columns <ChevronDown className="ml-2 h-4 w-4" />
            </Button>
          </DropdownMenuTrigger>
          <DropdownMenuContent align="end">
            {table
              .getAllColumns()
              .filter((column) => column.getCanHide())
              .map((column) => {
                return (
                  <DropdownMenuCheckboxItem
                    key={column.id}
                    className="capitalize"
                    checked={column.getIsVisible()}
                    onCheckedChange={(value) =>
                      column.toggleVisibility(!!value)
                    }
                  >
                    {column.id}
                  </DropdownMenuCheckboxItem>
                );
              })}
          </DropdownMenuContent>
        </DropdownMenu>
      </div>

      {/* Table */}
      <div className="rounded-md border">
        <Table>
          <TableHeader>
            {table.getHeaderGroups().map((headerGroup) => (
              <TableRow key={headerGroup.id}>
                {headerGroup.headers.map((header) => {
                  return (
                    <TableHead key={header.id}>
                      {header.isPlaceholder
                        ? null
                        : flexRender(
                            header.column.columnDef.header,
                            header.getContext()
                          )}
                    </TableHead>
                  );
                })}
              </TableRow>
            ))}
          </TableHeader>
          <TableBody>
            {table.getRowModel().rows?.length ? (
              table.getRowModel().rows.map((row) => (
                <TableRow
                  key={row.id}
                  data-state={row.getIsSelected() && 'selected'}
                >
                  {row.getVisibleCells().map((cell) => (
                    <TableCell key={cell.id}>
                      {flexRender(
                        cell.column.columnDef.cell,
                        cell.getContext()
                      )}
                    </TableCell>
                  ))}
                </TableRow>
              ))
            ) : (
              <TableRow>
                <TableCell
                  colSpan={columns.length}
                  className="h-24 text-center"
                >
                  No results.
                </TableCell>
              </TableRow>
            )}
          </TableBody>
        </Table>
      </div>

      {/* Pagination */}
      <div className="flex items-center justify-between px-2">
        <div className="flex-1 text-sm text-muted-foreground">
          {table.getFilteredSelectedRowModel().rows.length} of{' '}
          {table.getFilteredRowModel().rows.length} row(s) selected.
        </div>
        <div className="flex items-center space-x-6 lg:space-x-8">
          <div className="flex items-center space-x-2">
            <p className="text-sm font-medium">Rows per page</p>
            <select
              className="h-8 w-[70px] rounded-md border border-input bg-transparent px-2 py-1 text-sm"
              value={table.getState().pagination.pageSize}
              onChange={(e) => {
                table.setPageSize(Number(e.target.value));
              }}
            >
              {[10, 20, 30, 40, 50].map((pageSize) => (
                <option key={pageSize} value={pageSize}>
                  {pageSize}
                </option>
              ))}
            </select>
          </div>
          <div className="flex w-[100px] items-center justify-center text-sm font-medium">
            Page {table.getState().pagination.pageIndex + 1} of{' '}
            {table.getPageCount()}
          </div>
          <div className="flex items-center space-x-2">
            <Button
              variant="outline"
              size="sm"
              onClick={() => table.previousPage()}
              disabled={!table.getCanPreviousPage()}
            >
              Previous
            </Button>
            <Button
              variant="outline"
              size="sm"
              onClick={() => table.nextPage()}
              disabled={!table.getCanNextPage()}
            >
              Next
            </Button>
          </div>
        </div>
      </div>
    </div>
  );
}
```

## 4. Form Component

**File**: `[entity]-form.tsx`

```typescript
'use client';

import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { useRouter } from 'next/navigation';
import { Button } from '@/components/ui/button';
import {
  Form,
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from '@/components/ui/form';
import { Input } from '@/components/ui/input';
import { Textarea } from '@/components/ui/textarea';
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '@/components/ui/select';
import { toast } from 'sonner';
import { CourseService } from '@/lib/services/courses/course-service';
import { courseFormSchema, type CourseFormValues } from './data-table-schema';
import type { Course, Department } from '@/types/courses';

interface CourseFormProps {
  mode: 'create' | 'edit';
  initialData?: Course;
  departments: Department[];
  institutionId: string;
}

export function CourseForm({
  mode,
  initialData,
  departments,
  institutionId,
}: CourseFormProps) {
  const router = useRouter();

  const form = useForm<CourseFormValues>({
    resolver: zodResolver(courseFormSchema),
    defaultValues: initialData
      ? {
          code: initialData.code,
          name: initialData.name,
          description: initialData.description || '',
          credits: initialData.credits,
          department_id: initialData.department_id,
        }
      : {
          code: '',
          name: '',
          description: '',
          credits: 3,
          department_id: '',
        },
  });

  const onSubmit = async (data: CourseFormValues) => {
    try {
      if (mode === 'create') {
        await CourseService.createCourse({
          ...data,
          institution_id: institutionId,
        });
        toast.success('Course created successfully');
      } else {
        await CourseService.updateCourse({
          id: initialData!.id,
          ...data,
        });
        toast.success('Course updated successfully');
      }

      router.push('/academic/courses');
      router.refresh();
    } catch (error) {
      const message = error instanceof Error ? error.message : 'An error occurred';
      toast.error(message);
      console.error('[course-form] Error:', error);
    }
  };

  return (
    <Form {...form}>
      <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-6">
        <div className="grid gap-4 md:grid-cols-2">
          {/* Code Field */}
          <FormField
            control={form.control}
            name="code"
            render={({ field }) => (
              <FormItem>
                <FormLabel>Course Code *</FormLabel>
                <FormControl>
                  <Input
                    placeholder="CS101"
                    {...field}
                    className="uppercase"
                  />
                </FormControl>
                <FormDescription>
                  Unique code for the course (e.g., CS101, MATH201)
                </FormDescription>
                <FormMessage />
              </FormItem>
            )}
          />

          {/* Credits Field */}
          <FormField
            control={form.control}
            name="credits"
            render={({ field }) => (
              <FormItem>
                <FormLabel>Credits *</FormLabel>
                <FormControl>
                  <Input
                    type="number"
                    min="0"
                    max="10"
                    {...field}
                  />
                </FormControl>
                <FormDescription>
                  Number of credits (0-10)
                </FormDescription>
                <FormMessage />
              </FormItem>
            )}
          />
        </div>

        {/* Name Field */}
        <FormField
          control={form.control}
          name="name"
          render={({ field }) => (
            <FormItem>
              <FormLabel>Course Name *</FormLabel>
              <FormControl>
                <Input placeholder="Introduction to Programming" {...field} />
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
        />

        {/* Department Field */}
        <FormField
          control={form.control}
          name="department_id"
          render={({ field }) => (
            <FormItem>
              <FormLabel>Department *</FormLabel>
              <Select onValueChange={field.onChange} defaultValue={field.value}>
                <FormControl>
                  <SelectTrigger>
                    <SelectValue placeholder="Select a department" />
                  </SelectTrigger>
                </FormControl>
                <SelectContent>
                  {departments.map((dept) => (
                    <SelectItem key={dept.id} value={dept.id}>
                      {dept.name}
                    </SelectItem>
                  ))}
                </SelectContent>
              </Select>
              <FormMessage />
            </FormItem>
          )}
        />

        {/* Description Field */}
        <FormField
          control={form.control}
          name="description"
          render={({ field }) => (
            <FormItem>
              <FormLabel>Description</FormLabel>
              <FormControl>
                <Textarea
                  placeholder="Course description..."
                  className="resize-none"
                  rows={4}
                  {...field}
                />
              </FormControl>
              <FormDescription>
                Optional course description
              </FormDescription>
              <FormMessage />
            </FormItem>
          )}
        />

        {/* Submit Buttons */}
        <div className="flex justify-end gap-4">
          <Button
            type="button"
            variant="outline"
            onClick={() => router.back()}
          >
            Cancel
          </Button>
          <Button type="submit" disabled={form.formState.isSubmitting}>
            {form.formState.isSubmitting
              ? mode === 'create'
                ? 'Creating...'
                : 'Updating...'
              : mode === 'create'
              ? 'Create Course'
              : 'Update Course'}
          </Button>
        </div>
      </form>
    </Form>
  );
}
```

## 5. Row Actions Component

**File**: `row-actions.tsx`

```typescript
'use client';

import { Row } from '@tanstack/react-table';
import { useState } from 'react';
import { useRouter } from 'next/navigation';
import { MoreHorizontal, Pencil, Trash } from 'lucide-react';
import { Button } from '@/components/ui/button';
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from '@/components/ui/dropdown-menu';
import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
} from '@/components/ui/alert-dialog';
import { toast } from 'sonner';
import { CourseService } from '@/lib/services/courses/course-service';
import { CanEdit, CanDelete } from '@/components/permissions/permission-guard';
import type { Course } from '@/types/courses';

interface RowActionsProps {
  row: Row<Course>;
}

export function RowActions({ row }: RowActionsProps) {
  const router = useRouter();
  const course = row.original;
  const [showDeleteDialog, setShowDeleteDialog] = useState(false);
  const [isDeleting, setIsDeleting] = useState(false);

  const handleEdit = () => {
    router.push(`/academic/courses/${course.id}/edit`);
  };

  const handleDelete = async () => {
    try {
      setIsDeleting(true);
      await CourseService.deleteCourse(course.id);
      toast.success('Course deleted successfully');
      router.refresh();
    } catch (error) {
      toast.error('Failed to delete course');
      console.error('[row-actions] Delete error:', error);
    } finally {
      setIsDeleting(false);
      setShowDeleteDialog(false);
    }
  };

  return (
    <>
      <DropdownMenu>
        <DropdownMenuTrigger asChild>
          <Button
            variant="ghost"
            className="flex h-8 w-8 p-0 data-[state=open]:bg-muted"
          >
            <MoreHorizontal className="h-4 w-4" />
            <span className="sr-only">Open menu</span>
          </Button>
        </DropdownMenuTrigger>
        <DropdownMenuContent align="end" className="w-[160px]">
          <CanEdit module="academic.courses">
            <DropdownMenuItem onClick={handleEdit}>
              <Pencil className="mr-2 h-4 w-4" />
              Edit
            </DropdownMenuItem>
          </CanEdit>

          <CanDelete module="academic.courses">
            <DropdownMenuSeparator />
            <DropdownMenuItem
              onClick={() => setShowDeleteDialog(true)}
              className="text-destructive"
            >
              <Trash className="mr-2 h-4 w-4" />
              Delete
            </DropdownMenuItem>
          </CanDelete>
        </DropdownMenuContent>
      </DropdownMenu>

      <AlertDialog open={showDeleteDialog} onOpenChange={setShowDeleteDialog}>
        <AlertDialogContent>
          <AlertDialogHeader>
            <AlertDialogTitle>Are you sure?</AlertDialogTitle>
            <AlertDialogDescription>
              This will permanently delete the course "{course.name}". This
              action cannot be undone.
            </AlertDialogDescription>
          </AlertDialogHeader>
          <AlertDialogFooter>
            <AlertDialogCancel disabled={isDeleting}>Cancel</AlertDialogCancel>
            <AlertDialogAction
              onClick={handleDelete}
              disabled={isDeleting}
              className="bg-destructive text-destructive-foreground hover:bg-destructive/90"
            >
              {isDeleting ? 'Deleting...' : 'Delete'}
            </AlertDialogAction>
          </AlertDialogFooter>
        </AlertDialogContent>
      </AlertDialog>
    </>
  );
}
```

## Component Testing

```typescript
// __tests__/components/course-form.test.tsx
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { CourseForm } from '../course-form';

describe('CourseForm', () => {
  const mockDepartments = [
    { id: '1', name: 'Computer Science' },
    { id: '2', name: 'Mathematics' },
  ];

  it('should render form fields', () => {
    render(
      <CourseForm
        mode="create"
        departments={mockDepartments}
        institutionId="123"
      />
    );

    expect(screen.getByLabelText(/course code/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/course name/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/credits/i)).toBeInTheDocument();
  });

  it('should validate required fields', async () => {
    render(
      <CourseForm
        mode="create"
        departments={mockDepartments}
        institutionId="123"
      />
    );

    const submitButton = screen.getByText(/create course/i);
    fireEvent.click(submitButton);

    await waitFor(() => {
      expect(screen.getByText(/code is required/i)).toBeInTheDocument();
    });
  });
});
```

## Summary Checklist

For every component set:

- [ ] Zod schema in data-table-schema.ts
- [ ] Column definitions with sorting and filtering
- [ ] Data table with pagination and visibility controls
- [ ] Form with React Hook Form and validation
- [ ] Row actions with edit/delete
- [ ] Permission guards on actions
- [ ] Loading states for async operations
- [ ] Error handling with toast notifications
- [ ] Proper TypeScript typing
- [ ] Accessibility attributes (aria-label, etc.)
- [ ] Responsive design (mobile-friendly)
- [ ] Console logging with module prefix

This ensures all components are consistent, accessible, and maintainable.
