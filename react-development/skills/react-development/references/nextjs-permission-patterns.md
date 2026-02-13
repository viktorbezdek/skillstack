# Permission Patterns

## Complete Permission System Integration for MyJKKN

This document provides comprehensive patterns for implementing role-based access control (RBAC) across your Next.js application.

## Permission System Architecture

### Role Hierarchy

```
super_admin     - Full access to everything across all institutions
  ↓
admin           - Full access within their institution
  ↓
faculty         - Can manage academic content
  ↓
student         - Read-only access to assigned content
```

### Permission Naming Convention

Format: `[module].[entity].[action]`

Examples:
- `academic.courses.view`
- `academic.courses.create`
- `academic.courses.edit`
- `academic.courses.delete`

## 1. Define Permissions

**File**: `lib/sidebarMenuLink.ts` (or dedicated permissions file)

```typescript
/**
 * Permission definitions for all modules
 * Format: [module].[entity].[action]: [allowed_roles]
 */
export const MENU_PERMISSIONS: Record<string, string[]> = {
  // Academic - Courses
  'academic.courses.view': ['super_admin', 'admin', 'faculty', 'student'],
  'academic.courses.create': ['super_admin', 'admin', 'faculty'],
  'academic.courses.edit': ['super_admin', 'admin', 'faculty'],
  'academic.courses.delete': ['super_admin', 'admin'],

  // Academic - Departments
  'academic.departments.view': ['super_admin', 'admin', 'faculty'],
  'academic.departments.create': ['super_admin', 'admin'],
  'academic.departments.edit': ['super_admin', 'admin'],
  'academic.departments.delete': ['super_admin'],

  // Academic - Students
  'academic.students.view': ['super_admin', 'admin', 'faculty'],
  'academic.students.create': ['super_admin', 'admin'],
  'academic.students.edit': ['super_admin', 'admin'],
  'academic.students.delete': ['super_admin'],

  // User Management
  'users.manage': ['super_admin', 'admin'],
  'users.view': ['super_admin', 'admin', 'faculty'],

  // Settings
  'settings.view': ['super_admin', 'admin'],
  'settings.edit': ['super_admin'],
};

/**
 * Check if a role has permission for an action
 */
export function hasPermission(
  module: string,
  action: string,
  userRole: string
): boolean {
  const permissionKey = `${module}.${action}`;
  const allowedRoles = MENU_PERMISSIONS[permissionKey];

  if (!allowedRoles) {
    console.warn(`[permissions] Permission not defined: ${permissionKey}`);
    return false;
  }

  return allowedRoles.includes(userRole);
}

/**
 * Get all permissions for a role
 */
export function getRolePermissions(role: string): string[] {
  return Object.entries(MENU_PERMISSIONS)
    .filter(([, roles]) => roles.includes(role))
    .map(([permission]) => permission);
}
```

## 2. Permission Hook

**File**: `hooks/use-permissions.ts`

```typescript
'use client';

import { useContext } from 'react';
import { UserContext } from '@/components/providers/user-provider';
import { MENU_PERMISSIONS } from '@/lib/sidebarMenuLink';

export interface UserProfile {
  id: string;
  email: string;
  name: string;
  role: string;
  institution_id: string;
  permissions: string[];
}

export function usePermissions() {
  const userProfile = useContext(UserContext);

  /**
   * Check if user has a specific permission
   */
  const hasPermission = (module: string, action: string): boolean => {
    if (!userProfile) return false;

    const permissionKey = `${module}.${action}`;
    return userProfile.permissions.includes(permissionKey);
  };

  /**
   * Check if user can view a module
   */
  const canView = (module: string): boolean => {
    return hasPermission(module, 'view');
  };

  /**
   * Check if user can create in a module
   */
  const canCreate = (module: string): boolean => {
    return hasPermission(module, 'create');
  };

  /**
   * Check if user can edit in a module
   */
  const canEdit = (module: string): boolean => {
    return hasPermission(module, 'edit');
  };

  /**
   * Check if user can delete in a module
   */
  const canDelete = (module: string): boolean => {
    return hasPermission(module, 'delete');
  };

  /**
   * Check if user has any of the specified roles
   */
  const hasRole = (...roles: string[]): boolean => {
    if (!userProfile) return false;
    return roles.includes(userProfile.role);
  };

  return {
    userProfile,
    hasPermission,
    canView,
    canCreate,
    canEdit,
    canDelete,
    hasRole,
    isAdmin: hasRole('super_admin', 'admin'),
    isSuperAdmin: hasRole('super_admin'),
  };
}
```

## 3. Permission Guard Components

**File**: `components/permissions/permission-guard.tsx`

```typescript
'use client';

import { ReactNode } from 'react';
import { usePermissions } from '@/hooks/use-permissions';

interface PermissionGuardProps {
  module: string;
  action: string;
  children: ReactNode;
  fallback?: ReactNode;
}

/**
 * Component that shows children only if user has permission
 */
export function PermissionGuard({
  module,
  action,
  children,
  fallback = null,
}: PermissionGuardProps) {
  const { hasPermission } = usePermissions();

  if (!hasPermission(module, action)) {
    return <>{fallback}</>;
  }

  return <>{children}</>;
}

/**
 * Shorthand component for view permission
 */
export function CanView({ module, children, fallback }: Omit<PermissionGuardProps, 'action'>) {
  return (
    <PermissionGuard module={module} action="view" fallback={fallback}>
      {children}
    </PermissionGuard>
  );
}

/**
 * Shorthand component for create permission
 */
export function CanCreate({ module, children, fallback }: Omit<PermissionGuardProps, 'action'>) {
  return (
    <PermissionGuard module={module} action="create" fallback={fallback}>
      {children}
    </PermissionGuard>
  );
}

/**
 * Shorthand component for edit permission
 */
export function CanEdit({ module, children, fallback }: Omit<PermissionGuardProps, 'action'>) {
  return (
    <PermissionGuard module={module} action="edit" fallback={fallback}>
      {children}
    </PermissionGuard>
  );
}

/**
 * Shorthand component for delete permission
 */
export function CanDelete({ module, children, fallback }: Omit<PermissionGuardProps, 'action'>) {
  return (
    <PermissionGuard module={module} action="delete" fallback={fallback}>
      {children}
    </PermissionGuard>
  );
}

/**
 * Role-based guard component
 */
interface RoleGuardProps {
  roles: string[];
  children: ReactNode;
  fallback?: ReactNode;
}

export function RoleGuard({ roles, children, fallback = null }: RoleGuardProps) {
  const { hasRole } = usePermissions();

  if (!hasRole(...roles)) {
    return <>{fallback}</>;
  }

  return <>{children}</>;
}
```

## 4. Server-Side Permission Checks

**File**: `lib/auth/check-permission.ts`

```typescript
import { redirect } from 'next/navigation';
import { getCurrentUser } from './get-current-user';
import { hasPermission } from '@/lib/sidebarMenuLink';

/**
 * Check permission on server side
 * Throws error if user doesn't have permission
 */
export async function checkPermission(
  module: string,
  action: string
): Promise<void> {
  const user = await getCurrentUser();

  if (!user) {
    redirect('/login');
  }

  if (!hasPermission(module, action, user.role)) {
    console.warn(
      `[auth] Permission denied: ${user.email} attempted ${module}.${action}`
    );
    redirect('/dashboard');
  }
}

/**
 * Check if user has permission (returns boolean)
 */
export async function userHasPermission(
  module: string,
  action: string
): Promise<boolean> {
  try {
    const user = await getCurrentUser();
    if (!user) return false;

    return hasPermission(module, action, user.role);
  } catch (error) {
    console.error('[auth] Error checking permission:', error);
    return false;
  }
}

/**
 * Check multiple permissions (user must have ALL)
 */
export async function checkPermissions(
  permissions: Array<{ module: string; action: string }>
): Promise<void> {
  for (const { module, action } of permissions) {
    await checkPermission(module, action);
  }
}

/**
 * Check if user has any of the specified roles
 */
export async function checkRole(...roles: string[]): Promise<void> {
  const user = await getCurrentUser();

  if (!user) {
    redirect('/login');
  }

  if (!roles.includes(user.role)) {
    console.warn(`[auth] Role check failed: ${user.email} is ${user.role}`);
    redirect('/dashboard');
  }
}
```

## 5. Usage Patterns

### In Client Components

```typescript
'use client';

import { usePermissions } from '@/hooks/use-permissions';
import { CanCreate, CanEdit, CanDelete } from '@/components/permissions/permission-guard';
import { Button } from '@/components/ui/button';

export function CourseActions() {
  const { hasPermission, isAdmin } = usePermissions();

  return (
    <div className="flex gap-2">
      {/* Using hook directly */}
      {hasPermission('academic.courses', 'create') && (
        <Button>Create Course</Button>
      )}

      {/* Using guard components */}
      <CanEdit module="academic.courses">
        <Button>Edit Course</Button>
      </CanEdit>

      <CanDelete module="academic.courses">
        <Button variant="destructive">Delete Course</Button>
      </CanDelete>

      {/* Using role check */}
      {isAdmin && <Button>Admin Only Action</Button>}
    </div>
  );
}
```

### In Server Components (Pages)

```typescript
import { checkPermission, checkRole } from '@/lib/auth/check-permission';
import { getCurrentUser } from '@/lib/auth/get-current-user';

export default async function NewCoursePage() {
  // Method 1: Check permission (redirects if unauthorized)
  await checkPermission('academic.courses', 'create');

  // Method 2: Check role (redirects if unauthorized)
  await checkRole('super_admin', 'admin', 'faculty');

  // Method 3: Manual check
  const user = await getCurrentUser();
  if (!user.permissions.includes('academic.courses.create')) {
    redirect('/dashboard');
  }

  return (
    <div>
      {/* Page content */}
    </div>
  );
}
```

### In API Routes

```typescript
// app/api/courses/route.ts
import { NextRequest, NextResponse } from 'next/server';
import { getCurrentUser } from '@/lib/auth/get-current-user';
import { hasPermission } from '@/lib/sidebarMenuLink';
import { CourseService } from '@/lib/services/courses/course-service';

export async function POST(request: NextRequest) {
  try {
    // Get user
    const user = await getCurrentUser();

    // Check permission
    if (!hasPermission('academic.courses', 'create', user.role)) {
      return NextResponse.json(
        { error: 'Insufficient permissions' },
        { status: 403 }
      );
    }

    // Process request
    const body = await request.json();
    const course = await CourseService.createCourse({
      ...body,
      institution_id: user.institution_id,
    });

    return NextResponse.json(course);
  } catch (error) {
    console.error('[api/courses] Error:', error);
    return NextResponse.json(
      { error: 'Internal server error' },
      { status: 500 }
    );
  }
}
```

## 6. Sidebar Menu Integration

**File**: `lib/sidebarMenuLink.ts`

```typescript
import { LucideIcon } from 'lucide-react';

export interface MenuItem {
  label: string;
  href: string;
  icon?: LucideIcon;
  permission?: string; // e.g., "academic.courses.view"
  submenus?: MenuItem[];
}

export interface MenuGroup {
  groupLabel: string;
  menus: MenuItem[];
}

export const menuList: MenuGroup[] = [
  {
    groupLabel: 'Academic',
    menus: [
      {
        label: 'Courses',
        href: '/academic/courses',
        permission: 'academic.courses.view',
      },
      {
        label: 'Departments',
        href: '/academic/departments',
        permission: 'academic.departments.view',
      },
      {
        label: 'Students',
        href: '/academic/students',
        permission: 'academic.students.view',
      },
    ],
  },
  {
    groupLabel: 'Administration',
    menus: [
      {
        label: 'Users',
        href: '/admin/users',
        permission: 'users.view',
      },
      {
        label: 'Settings',
        href: '/admin/settings',
        permission: 'settings.view',
      },
    ],
  },
];

/**
 * Filter menu items based on user permissions
 */
export function getAccessibleMenus(
  userPermissions: string[]
): MenuGroup[] {
  return menuList
    .map((group) => ({
      ...group,
      menus: group.menus.filter(
        (menu) =>
          !menu.permission || userPermissions.includes(menu.permission)
      ),
    }))
    .filter((group) => group.menus.length > 0);
}
```

## 7. Row-Level Security (RLS) Integration

**Database**: Supabase RLS Policies

```sql
-- Policy using role from JWT
CREATE POLICY "Users view courses from their institution"
  ON courses
  FOR SELECT
  USING (
    institution_id::text = auth.jwt()->>'institution_id'
  );

-- Policy with role check
CREATE POLICY "Admins and faculty can create courses"
  ON courses
  FOR INSERT
  WITH CHECK (
    institution_id::text = auth.jwt()->>'institution_id'
    AND (auth.jwt()->>'role')::text IN ('super_admin', 'admin', 'faculty')
  );

-- Policy for super_admin (cross-institution access)
CREATE POLICY "Super admins can view all courses"
  ON courses
  FOR SELECT
  USING (
    (auth.jwt()->>'role')::text = 'super_admin'
  );
```

## 8. Testing Permissions

```typescript
// __tests__/permissions/permission-guard.test.tsx
import { render, screen } from '@testing-library/react';
import { PermissionGuard } from '@/components/permissions/permission-guard';
import { UserContext } from '@/components/providers/user-provider';

describe('PermissionGuard', () => {
  const mockUser = {
    id: '1',
    email: 'admin@test.com',
    name: 'Admin User',
    role: 'admin',
    institution_id: '1',
    permissions: ['academic.courses.view', 'academic.courses.create'],
  };

  it('should show content when user has permission', () => {
    render(
      <UserContext.Provider value={mockUser}>
        <PermissionGuard module="academic.courses" action="view">
          <div>Protected Content</div>
        </PermissionGuard>
      </UserContext.Provider>
    );

    expect(screen.getByText('Protected Content')).toBeInTheDocument();
  });

  it('should not show content when user lacks permission', () => {
    render(
      <UserContext.Provider value={mockUser}>
        <PermissionGuard module="academic.courses" action="delete">
          <div>Protected Content</div>
        </PermissionGuard>
      </UserContext.Provider>
    );

    expect(screen.queryByText('Protected Content')).not.toBeInTheDocument();
  });

  it('should show fallback when provided', () => {
    render(
      <UserContext.Provider value={mockUser}>
        <PermissionGuard
          module="academic.courses"
          action="delete"
          fallback={<div>No Access</div>}
        >
          <div>Protected Content</div>
        </PermissionGuard>
      </UserContext.Provider>
    );

    expect(screen.getByText('No Access')).toBeInTheDocument();
  });
});
```

## Permission Checklist

For every new module:

- [ ] Define permissions in MENU_PERMISSIONS
- [ ] Add permission checks in all pages
- [ ] Wrap buttons/actions with permission guards
- [ ] Add RLS policies in database
- [ ] Update sidebar menu with permission keys
- [ ] Test all permission levels (super_admin, admin, faculty, student)
- [ ] Document permission requirements
- [ ] Add permission checks in API routes
- [ ] Verify institution_id filtering
- [ ] Test with different user roles

## Common Permission Patterns

```typescript
// ✅ Good: Using permission guards
<CanCreate module="academic.courses">
  <Button>Create</Button>
</CanCreate>

// ✅ Good: Server-side check
await checkPermission('academic.courses', 'create');

// ✅ Good: Hook usage
const { canEdit } = usePermissions();
if (canEdit('academic.courses')) {
  // Show edit button
}

// ❌ Bad: Hardcoded role check
if (user.role === 'admin') {
  // This bypasses the permission system
}

// ❌ Bad: Client-side only check
// Always validate on server for mutations

// ❌ Bad: Missing institution check
// Always verify institution_id matches user
```

## Summary

- **Always** check permissions on both client and server
- **Always** verify institution_id for data access
- **Use** permission guards for UI elements
- **Use** server checks for page access and API routes
- **Implement** RLS policies for database-level security
- **Test** with all user roles
- **Document** permission requirements for each feature

This ensures secure, role-based access control throughout the application.
