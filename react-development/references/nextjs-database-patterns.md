# Database Patterns

## Supabase Database Design for MyJKKN

This document provides comprehensive database design patterns, schema conventions, and Row-Level Security (RLS) policies for building consistent, secure, and performant database structures.

## Table Design Patterns

### Standard Table Structure

Every table should follow this standard structure:

```sql
CREATE TABLE entities (
  -- Primary Key
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),

  -- Institution Context (multi-tenancy)
  institution_id UUID NOT NULL REFERENCES institutions(id) ON DELETE CASCADE,

  -- Business Fields
  name VARCHAR(255) NOT NULL,
  description TEXT,
  code VARCHAR(50),

  -- Status Management
  is_active BOOLEAN DEFAULT true,

  -- Audit Fields
  created_at TIMESTAMPTZ DEFAULT NOW() NOT NULL,
  updated_at TIMESTAMPTZ DEFAULT NOW() NOT NULL,
  created_by UUID REFERENCES users(id),
  updated_by UUID REFERENCES users(id)
);
```

### Field Naming Conventions

| Field Type | Convention | Example |
|-----------|-----------|---------|
| Primary Key | `id` | `id UUID` |
| Foreign Key | `[table]_id` | `institution_id`, `user_id` |
| Boolean | `is_[state]` or `has_[feature]` | `is_active`, `has_verified` |
| Timestamps | `[action]_at` | `created_at`, `updated_at` |
| References | `[action]_by` | `created_by`, `approved_by` |
| Code/Identifier | `code` or `[entity]_code` | `code`, `course_code` |

## Common Field Patterns

### Required Audit Fields

Every table should include:

```sql
-- Timestamps with timezone
created_at TIMESTAMPTZ DEFAULT NOW() NOT NULL,
updated_at TIMESTAMPTZ DEFAULT NOW() NOT NULL,

-- User tracking
created_by UUID REFERENCES users(id),
updated_by UUID REFERENCES users(id),

-- Status flag
is_active BOOLEAN DEFAULT true
```

### Multi-Tenancy Pattern

All tenant-specific tables must include:

```sql
institution_id UUID NOT NULL REFERENCES institutions(id) ON DELETE CASCADE,
```

**Index**: Always index `institution_id` for performance:
```sql
CREATE INDEX idx_entities_institution ON entities(institution_id);
```

### Soft Delete Pattern

Prefer soft deletes over hard deletes:

```sql
-- Add deleted_at field
deleted_at TIMESTAMPTZ,
deleted_by UUID REFERENCES users(id),

-- Queries filter out deleted records
WHERE deleted_at IS NULL
```

Alternative: Use `is_active` flag:
```sql
is_active BOOLEAN DEFAULT true,

-- Mark as inactive instead of deleting
UPDATE entities SET is_active = false WHERE id = '...';
```

## Relationships and Foreign Keys

### One-to-Many Relationship

```sql
-- Parent table
CREATE TABLE departments (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  institution_id UUID NOT NULL REFERENCES institutions(id),
  name VARCHAR(255) NOT NULL
);

-- Child table
CREATE TABLE courses (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  institution_id UUID NOT NULL REFERENCES institutions(id),
  department_id UUID NOT NULL REFERENCES departments(id) ON DELETE CASCADE,
  name VARCHAR(255) NOT NULL
);

-- Index foreign key
CREATE INDEX idx_courses_department ON courses(department_id);
```

### Many-to-Many Relationship

```sql
-- First entity
CREATE TABLE students (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  institution_id UUID NOT NULL REFERENCES institutions(id),
  name VARCHAR(255) NOT NULL
);

-- Second entity
CREATE TABLE courses (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  institution_id UUID NOT NULL REFERENCES institutions(id),
  name VARCHAR(255) NOT NULL
);

-- Junction table
CREATE TABLE student_courses (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  institution_id UUID NOT NULL REFERENCES institutions(id),
  student_id UUID NOT NULL REFERENCES students(id) ON DELETE CASCADE,
  course_id UUID NOT NULL REFERENCES courses(id) ON DELETE CASCADE,

  -- Additional fields specific to the relationship
  enrolled_at TIMESTAMPTZ DEFAULT NOW(),
  grade VARCHAR(5),
  status VARCHAR(20) DEFAULT 'active',

  -- Prevent duplicate enrollments
  UNIQUE(student_id, course_id),

  -- Audit fields
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Indexes for both directions
CREATE INDEX idx_student_courses_student ON student_courses(student_id);
CREATE INDEX idx_student_courses_course ON student_courses(course_id);
CREATE INDEX idx_student_courses_institution ON student_courses(institution_id);
```

### Self-Referencing Relationship

```sql
-- Hierarchical structure (e.g., org chart, categories)
CREATE TABLE departments (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  institution_id UUID NOT NULL REFERENCES institutions(id),
  parent_department_id UUID REFERENCES departments(id) ON DELETE SET NULL,
  name VARCHAR(255) NOT NULL,
  level INTEGER DEFAULT 0,

  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Index for hierarchy queries
CREATE INDEX idx_departments_parent ON departments(parent_department_id);
```

## Indexing Strategies

### When to Create Indexes

Create indexes for:

1. **Foreign keys** (always)
```sql
CREATE INDEX idx_courses_department ON courses(department_id);
```

2. **Frequently filtered columns**
```sql
CREATE INDEX idx_courses_active ON courses(is_active);
CREATE INDEX idx_courses_institution ON courses(institution_id);
```

3. **Compound queries** (multiple columns)
```sql
-- For queries like: WHERE institution_id = ? AND is_active = true
CREATE INDEX idx_courses_institution_active ON courses(institution_id, is_active);
```

4. **Search fields**
```sql
-- For text search
CREATE INDEX idx_courses_name_trgm ON courses USING gin(name gin_trgm_ops);
```

5. **Sorting columns**
```sql
-- For ORDER BY created_at DESC
CREATE INDEX idx_courses_created_at ON courses(created_at DESC);
```

### Index Patterns

```sql
-- Single column index
CREATE INDEX idx_courses_code ON courses(code);

-- Composite index (order matters!)
CREATE INDEX idx_courses_inst_dept ON courses(institution_id, department_id);

-- Partial index (for filtered queries)
CREATE INDEX idx_courses_active_only ON courses(institution_id)
  WHERE is_active = true;

-- Text search index (PostgreSQL full-text search)
CREATE INDEX idx_courses_search ON courses USING gin(to_tsvector('english', name));
```

## Constraints and Validation

### Check Constraints

```sql
-- Validate email format
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  email VARCHAR(255) CHECK (email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$'),
  age INTEGER CHECK (age >= 0 AND age <= 150)
);

-- Validate enum values
CREATE TABLE courses (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  status VARCHAR(20) CHECK (status IN ('draft', 'published', 'archived'))
);

-- Validate date ranges
CREATE TABLE events (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  start_date DATE NOT NULL,
  end_date DATE NOT NULL,
  CHECK (end_date >= start_date)
);
```

### Unique Constraints

```sql
-- Single column unique
CREATE TABLE institutions (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  code VARCHAR(50) UNIQUE NOT NULL
);

-- Composite unique (within institution)
CREATE TABLE courses (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  institution_id UUID NOT NULL REFERENCES institutions(id),
  code VARCHAR(50) NOT NULL,
  UNIQUE(institution_id, code)
);
```

### NOT NULL Constraints

```sql
-- Required fields
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  email VARCHAR(255) NOT NULL,
  name VARCHAR(255) NOT NULL,
  institution_id UUID NOT NULL REFERENCES institutions(id)
);
```

## Row-Level Security (RLS) Policies

### Enable RLS on Every Table

```sql
-- Enable RLS
ALTER TABLE entities ENABLE ROW LEVEL SECURITY;
```

### Standard RLS Policies

#### 1. Read Policy (SELECT)

```sql
-- Users can only view records from their institution
CREATE POLICY "Users view own institution records"
  ON entities
  FOR SELECT
  USING (
    institution_id = (
      SELECT institution_id FROM users
      WHERE id = auth.uid()
    )
  );

-- Alternative: Using JWT claim
CREATE POLICY "Users view own institution records"
  ON entities
  FOR SELECT
  USING (
    institution_id::text = auth.jwt()->>'institution_id'
  );
```

#### 2. Create Policy (INSERT)

```sql
-- Users can only create records for their institution
CREATE POLICY "Users create own institution records"
  ON entities
  FOR INSERT
  WITH CHECK (
    institution_id = (
      SELECT institution_id FROM users
      WHERE id = auth.uid()
    )
  );

-- With role check
CREATE POLICY "Admins and faculty can create"
  ON entities
  FOR INSERT
  WITH CHECK (
    institution_id = (SELECT institution_id FROM users WHERE id = auth.uid())
    AND EXISTS (
      SELECT 1 FROM users
      WHERE id = auth.uid()
      AND role IN ('super_admin', 'admin', 'faculty')
    )
  );
```

#### 3. Update Policy (UPDATE)

```sql
-- Users can only update records from their institution
CREATE POLICY "Users update own institution records"
  ON entities
  FOR UPDATE
  USING (
    institution_id = (
      SELECT institution_id FROM users
      WHERE id = auth.uid()
    )
  )
  WITH CHECK (
    institution_id = (
      SELECT institution_id FROM users
      WHERE id = auth.uid()
    )
  );

-- With role-based restrictions
CREATE POLICY "Admins can update"
  ON entities
  FOR UPDATE
  USING (
    institution_id = (SELECT institution_id FROM users WHERE id = auth.uid())
    AND EXISTS (
      SELECT 1 FROM users
      WHERE id = auth.uid()
      AND role IN ('super_admin', 'admin')
    )
  );
```

#### 4. Delete Policy (DELETE)

```sql
-- Only admins can delete
CREATE POLICY "Only admins can delete"
  ON entities
  FOR DELETE
  USING (
    institution_id = (SELECT institution_id FROM users WHERE id = auth.uid())
    AND EXISTS (
      SELECT 1 FROM users
      WHERE id = auth.uid()
      AND role IN ('super_admin', 'admin')
    )
  );
```

### Complete RLS Example

```sql
-- Create table
CREATE TABLE courses (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  institution_id UUID NOT NULL REFERENCES institutions(id),
  name VARCHAR(255) NOT NULL,
  code VARCHAR(50) NOT NULL,
  is_active BOOLEAN DEFAULT true,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW(),
  created_by UUID REFERENCES users(id),
  updated_by UUID REFERENCES users(id)
);

-- Enable RLS
ALTER TABLE courses ENABLE ROW LEVEL SECURITY;

-- SELECT: All authenticated users in same institution
CREATE POLICY "Users view own institution courses"
  ON courses
  FOR SELECT
  USING (
    institution_id::text = auth.jwt()->>'institution_id'
  );

-- INSERT: Only admins and faculty
CREATE POLICY "Admins and faculty create courses"
  ON courses
  FOR INSERT
  WITH CHECK (
    institution_id::text = auth.jwt()->>'institution_id'
    AND (auth.jwt()->>'role')::text IN ('super_admin', 'admin', 'faculty')
  );

-- UPDATE: Only admins and faculty
CREATE POLICY "Admins and faculty update courses"
  ON courses
  FOR UPDATE
  USING (
    institution_id::text = auth.jwt()->>'institution_id'
    AND (auth.jwt()->>'role')::text IN ('super_admin', 'admin', 'faculty')
  );

-- DELETE: Only admins
CREATE POLICY "Only admins delete courses"
  ON courses
  FOR DELETE
  USING (
    institution_id::text = auth.jwt()->>'institution_id'
    AND (auth.jwt()->>'role')::text IN ('super_admin', 'admin')
  );
```

## Database Functions and Triggers

### Auto-Update Timestamp Trigger

```sql
-- Create function to update timestamp
CREATE OR REPLACE FUNCTION update_updated_at()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Apply to table
CREATE TRIGGER update_entities_updated_at
  BEFORE UPDATE ON entities
  FOR EACH ROW
  EXECUTE FUNCTION update_updated_at();
```

### Audit Log Trigger

```sql
-- Create audit log table
CREATE TABLE audit_log (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  table_name VARCHAR(255) NOT NULL,
  record_id UUID NOT NULL,
  action VARCHAR(10) NOT NULL,
  old_data JSONB,
  new_data JSONB,
  changed_by UUID REFERENCES users(id),
  changed_at TIMESTAMPTZ DEFAULT NOW()
);

-- Create audit function
CREATE OR REPLACE FUNCTION audit_trigger()
RETURNS TRIGGER AS $$
BEGIN
  INSERT INTO audit_log (
    table_name,
    record_id,
    action,
    old_data,
    new_data,
    changed_by
  ) VALUES (
    TG_TABLE_NAME,
    COALESCE(NEW.id, OLD.id),
    TG_OP,
    CASE WHEN TG_OP = 'DELETE' THEN to_jsonb(OLD) ELSE NULL END,
    CASE WHEN TG_OP != 'DELETE' THEN to_jsonb(NEW) ELSE NULL END,
    auth.uid()
  );
  RETURN COALESCE(NEW, OLD);
END;
$$ LANGUAGE plpgsql;

-- Apply to table
CREATE TRIGGER audit_courses
  AFTER INSERT OR UPDATE OR DELETE ON courses
  FOR EACH ROW
  EXECUTE FUNCTION audit_trigger();
```

## Query Optimization Patterns

### Efficient Pagination

```sql
-- Use OFFSET and LIMIT with index
SELECT * FROM courses
WHERE institution_id = '...'
ORDER BY created_at DESC
LIMIT 10 OFFSET 20;

-- Better: Use cursor-based pagination
SELECT * FROM courses
WHERE institution_id = '...'
  AND created_at < '2025-10-30T00:00:00Z'
ORDER BY created_at DESC
LIMIT 10;
```

### Efficient Counting

```sql
-- Slow: Full count
SELECT COUNT(*) FROM courses WHERE institution_id = '...';

-- Fast: Use query with count option in Supabase
const { data, count } = await supabase
  .from('courses')
  .select('*', { count: 'exact' })
  .eq('institution_id', id)
  .range(0, 9);
```

### Efficient Text Search

```sql
-- Create trigram index
CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE INDEX idx_courses_name_trgm ON courses USING gin(name gin_trgm_ops);

-- Use ILIKE with index
SELECT * FROM courses
WHERE name ILIKE '%search%';

-- Or use full-text search
SELECT * FROM courses
WHERE to_tsvector('english', name) @@ plainto_tsquery('english', 'search');
```

## Common Table Examples

### Academic Module Tables

```sql
-- Departments
CREATE TABLE departments (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  institution_id UUID NOT NULL REFERENCES institutions(id),
  code VARCHAR(50) NOT NULL,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  is_active BOOLEAN DEFAULT true,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW(),
  UNIQUE(institution_id, code)
);

-- Programs
CREATE TABLE programs (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  institution_id UUID NOT NULL REFERENCES institutions(id),
  department_id UUID NOT NULL REFERENCES departments(id) ON DELETE CASCADE,
  code VARCHAR(50) NOT NULL,
  name VARCHAR(255) NOT NULL,
  duration_years INTEGER NOT NULL,
  is_active BOOLEAN DEFAULT true,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW(),
  UNIQUE(institution_id, code)
);

-- Courses
CREATE TABLE courses (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  institution_id UUID NOT NULL REFERENCES institutions(id),
  department_id UUID NOT NULL REFERENCES departments(id) ON DELETE CASCADE,
  code VARCHAR(50) NOT NULL,
  name VARCHAR(255) NOT NULL,
  credits INTEGER NOT NULL,
  description TEXT,
  is_active BOOLEAN DEFAULT true,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW(),
  UNIQUE(institution_id, code)
);

CREATE INDEX idx_courses_institution ON courses(institution_id);
CREATE INDEX idx_courses_department ON courses(department_id);
CREATE INDEX idx_courses_active ON courses(is_active);
```

## Migration Best Practices

### Creating Migrations

```sql
-- Migration file: 001_create_courses_table.sql

-- Create table
CREATE TABLE courses (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  institution_id UUID NOT NULL REFERENCES institutions(id),
  name VARCHAR(255) NOT NULL,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Create indexes
CREATE INDEX idx_courses_institution ON courses(institution_id);

-- Enable RLS
ALTER TABLE courses ENABLE ROW LEVEL SECURITY;

-- Create policies
CREATE POLICY "Users view own institution courses"
  ON courses FOR SELECT
  USING (institution_id::text = auth.jwt()->>'institution_id');

-- Create triggers
CREATE TRIGGER update_courses_updated_at
  BEFORE UPDATE ON courses
  FOR EACH ROW
  EXECUTE FUNCTION update_updated_at();

-- Add comments
COMMENT ON TABLE courses IS 'Stores course information for all institutions';
COMMENT ON COLUMN courses.code IS 'Unique course code within institution';
```

### Altering Tables Safely

```sql
-- Add column with default
ALTER TABLE courses ADD COLUMN IF NOT EXISTS description TEXT;

-- Add NOT NULL constraint safely
ALTER TABLE courses ADD COLUMN new_field VARCHAR(255);
UPDATE courses SET new_field = 'default_value' WHERE new_field IS NULL;
ALTER TABLE courses ALTER COLUMN new_field SET NOT NULL;

-- Rename column
ALTER TABLE courses RENAME COLUMN old_name TO new_name;

-- Drop column
ALTER TABLE courses DROP COLUMN IF EXISTS old_column;
```

## Database Naming Cheatsheet

```
Table Names:          plural_snake_case     (courses, student_enrollments)
Column Names:         singular_snake_case   (name, institution_id)
Primary Keys:         id
Foreign Keys:         [table]_id            (course_id, user_id)
Junction Tables:      [table1]_[table2]     (student_courses)
Indexes:              idx_[table]_[column]  (idx_courses_institution)
Constraints:          [table]_[column]_[type] (courses_code_unique)
Triggers:             [action]_[table]_[event] (update_courses_updated_at)
Functions:            [verb]_[description]  (update_updated_at)
```

## Testing Database Patterns

### Test RLS Policies

```sql
-- Set session user
SET LOCAL role authenticated;
SET LOCAL request.jwt.claim.sub = 'user-uuid';
SET LOCAL request.jwt.claim.institution_id = 'institution-uuid';

-- Test SELECT
SELECT * FROM courses; -- Should only return user's institution courses

-- Reset
RESET role;
```

### Test Constraints

```sql
-- Test unique constraint
INSERT INTO courses (institution_id, code, name) VALUES ('uuid', 'CS101', 'Intro');
INSERT INTO courses (institution_id, code, name) VALUES ('uuid', 'CS101', 'Intro'); -- Should fail

-- Test check constraint
INSERT INTO courses (institution_id, code, name, credits) VALUES ('uuid', 'CS102', 'Test', -1); -- Should fail
```

## Summary Checklist

For every new table:

- [ ] Primary key `id UUID` with `uuid_generate_v4()`
- [ ] `institution_id` for multi-tenancy
- [ ] Audit fields (`created_at`, `updated_at`, etc.)
- [ ] `is_active` for soft deletes
- [ ] Proper foreign keys with `ON DELETE` actions
- [ ] Unique constraints where needed
- [ ] Check constraints for validation
- [ ] Indexes on foreign keys and filter columns
- [ ] RLS enabled with appropriate policies
- [ ] Updated_at trigger applied
- [ ] Comments on table and complex columns
- [ ] Migration file created and tested

This ensures every table follows MyJKKN standards for security, performance, and maintainability.
