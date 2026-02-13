# GraphQL Schema Patterns

Best practices and patterns for designing GraphQL schemas.

## Naming Conventions

### Types
- **PascalCase** for type names: `User`, `BlogPost`, `OrderItem`
- Suffix input types with `Input`: `CreateUserInput`, `UpdatePostInput`
- Suffix payload types with `Payload`: `CreateUserPayload`, `DeletePostPayload`
- Suffix connection types with `Connection`: `UserConnection`, `PostConnection`
- Suffix edge types with `Edge`: `UserEdge`, `PostEdge`

### Fields
- **camelCase** for field names: `firstName`, `createdAt`, `isPublished`
- Boolean fields: prefix with `is`, `has`, `can`: `isActive`, `hasComments`, `canEdit`
- Avoid abbreviations: `firstName` not `fName`

### Enums
- **SCREAMING_SNAKE_CASE** for enum values: `PENDING`, `IN_PROGRESS`, `COMPLETED`
- Prefix with type context if needed: `ORDER_STATUS_PENDING`

### Arguments
- **camelCase** for argument names: `first`, `after`, `orderBy`
- Pagination: use Relay convention (`first`, `last`, `before`, `after`)
- Filtering: use clear names (`where`, `filter`, `search`)

## Type Design Patterns

### Object Types

```graphql
"""
User account with profile information.
All users must have a verified email address.
"""
type User {
  "Unique identifier"
  id: ID!

  "Email address (unique, verified)"
  email: String!

  "Display name"
  name: String

  "User's profile settings"
  profile: Profile

  "Posts authored by this user"
  posts(first: Int, after: String): PostConnection!

  "Account creation timestamp"
  createdAt: DateTime!

  "Last update timestamp"
  updatedAt: DateTime!
}
```

**Best Practices:**
- Always include descriptions for types and fields
- Use `ID!` for identifiers (not `String!` or `Int!`)
- Include timestamps (`createdAt`, `updatedAt`)
- Prefer object types over primitive types for flexibility

### Input Types

```graphql
"""
Input for creating a new user account.
"""
input CreateUserInput {
  "Email address (must be unique)"
  email: String!

  "Password (min 8 characters)"
  password: String!

  "Display name"
  name: String
}

"""
Input for updating user account.
All fields are optional - only provided fields are updated.
"""
input UpdateUserInput {
  "New email address"
  email: String

  "New display name"
  name: String

  "Profile updates"
  profile: UpdateProfileInput
}
```

**Best Practices:**
- Create mutations use required fields
- Update mutations use optional fields
- Nest related inputs for complex updates
- Document constraints in descriptions

### Payload Types

```graphql
"""
Result of createUser mutation.
"""
type CreateUserPayload {
  "The created user"
  user: User

  "Errors that occurred during creation"
  errors: [CreateUserError!]
}

type CreateUserError {
  "Error code for programmatic handling"
  code: CreateUserErrorCode!

  "Human-readable error message"
  message: String!

  "Field that caused the error"
  field: String
}

enum CreateUserErrorCode {
  EMAIL_ALREADY_EXISTS
  INVALID_PASSWORD
  INVALID_EMAIL_FORMAT
}
```

**Benefits:**
- Clear success/error handling
- Type-safe error codes
- Field-level error information
- Extensible without breaking changes

## Pagination Patterns

### Relay-Style Cursor Pagination

```graphql
type Query {
  users(
    first: Int
    after: String
    last: Int
    before: String
  ): UserConnection!
}

type UserConnection {
  "List of user edges"
  edges: [UserEdge!]!

  "Pagination information"
  pageInfo: PageInfo!

  "Total count of users"
  totalCount: Int!
}

type UserEdge {
  "The user"
  node: User!

  "Cursor for this edge"
  cursor: String!
}

type PageInfo {
  "Has more items after last edge"
  hasNextPage: Boolean!

  "Has more items before first edge"
  hasPreviousPage: Boolean!

  "Cursor of first edge"
  startCursor: String

  "Cursor of last edge"
  endCursor: String
}
```

**When to Use:**
- Large datasets (100+ items)
- Real-time data (items may be added/removed)
- Infinite scroll UIs

### Simple Offset Pagination

```graphql
type Query {
  users(
    limit: Int = 10
    offset: Int = 0
  ): UserList!
}

type UserList {
  items: [User!]!
  totalCount: Int!
  hasMore: Boolean!
}
```

**When to Use:**
- Small datasets
- Traditional page-based UIs
- Simpler implementation needs

## Relationship Patterns

### One-to-One

```graphql
type User {
  id: ID!
  profile: Profile
}

type Profile {
  id: ID!
  user: User!
  bio: String
  avatar: String
}
```

### One-to-Many

```graphql
type User {
  id: ID!
  posts(first: Int, after: String): PostConnection!
}

type Post {
  id: ID!
  author: User!
}
```

### Many-to-Many

```graphql
type Post {
  id: ID!
  tags: [Tag!]!
}

type Tag {
  id: ID!
  posts(first: Int, after: String): PostConnection!
}

# Consider a join type for additional metadata
type PostTag {
  post: Post!
  tag: Tag!
  addedAt: DateTime!
  addedBy: User!
}
```

## Query Organization

### Root Query

```graphql
type Query {
  # Single resource lookups
  user(id: ID!): User
  post(id: ID!): Post

  # Current user
  me: User

  # List queries with pagination and filtering
  users(
    first: Int
    after: String
    filter: UserFilter
    orderBy: UserOrderBy
  ): UserConnection!

  posts(
    first: Int
    after: String
    filter: PostFilter
    orderBy: PostOrderBy
  ): PostConnection!

  # Search
  search(query: String!, types: [SearchType!]): SearchResults!
}
```

### Filtering

```graphql
input PostFilter {
  authorId: ID
  published: Boolean
  createdAfter: DateTime
  createdBefore: DateTime
  tags: [String!]
}

input UserFilter {
  search: String
  role: UserRole
  isActive: Boolean
}
```

### Ordering

```graphql
input PostOrderBy {
  field: PostOrderField!
  direction: OrderDirection!
}

enum PostOrderField {
  CREATED_AT
  UPDATED_AT
  TITLE
  VIEW_COUNT
}

enum OrderDirection {
  ASC
  DESC
}
```

## Mutation Patterns

### Standard CRUD

```graphql
type Mutation {
  # Create
  createPost(input: CreatePostInput!): CreatePostPayload!

  # Update
  updatePost(id: ID!, input: UpdatePostInput!): UpdatePostPayload!

  # Delete
  deletePost(id: ID!): DeletePostPayload!

  # Bulk operations
  deletePosts(ids: [ID!]!): DeletePostsPayload!
}
```

### Action Mutations

```graphql
type Mutation {
  # Publish a draft post
  publishPost(id: ID!): PublishPostPayload!

  # Archive a post
  archivePost(id: ID!): ArchivePostPayload!

  # Like a post
  likePost(id: ID!): LikePostPayload!

  # Unlike a post
  unlikePost(id: ID!): UnlikePostPayload!
}
```

## Custom Scalars

```graphql
# Common custom scalars
scalar DateTime    # ISO 8601 datetime
scalar Date        # ISO 8601 date
scalar Time        # ISO 8601 time
scalar Email       # Valid email address
scalar URL         # Valid URL
scalar JSON        # Arbitrary JSON
scalar UUID        # UUID v4
scalar BigInt      # Large integers
scalar Decimal     # Precise decimals
scalar PhoneNumber # E.164 phone format
```

## Directives

### Built-in Directives

```graphql
type User {
  # Deprecated field
  username: String @deprecated(reason: "Use 'name' instead")
  name: String
}

query GetUser($includeEmail: Boolean!) {
  user(id: "1") {
    name
    # Conditional inclusion
    email @include(if: $includeEmail)
  }
}
```

### Custom Directives

```graphql
# Schema directives
directive @auth(requires: Role!) on FIELD_DEFINITION

type Query {
  users: [User!]! @auth(requires: ADMIN)
  me: User @auth(requires: USER)
}

# Validation directives
directive @length(min: Int, max: Int) on INPUT_FIELD_DEFINITION

input CreatePostInput {
  title: String! @length(min: 1, max: 200)
  content: String! @length(min: 10)
}
```

## Versioning Strategies

### Additive Changes (Recommended)

```graphql
# Version 1
type User {
  id: ID!
  name: String!
}

# Version 2 - Add new field (non-breaking)
type User {
  id: ID!
  name: String!
  displayName: String  # New optional field
}
```

### Deprecation

```graphql
type User {
  # Old field - deprecated but still works
  name: String! @deprecated(reason: "Use 'displayName' field. Will be removed 2025-01-01")

  # New field
  displayName: String!
}
```

### Never Do

- Remove fields without deprecation period
- Change field types
- Make optional fields required
- Change enum values

## Anti-Patterns to Avoid

### Avoid Generic Types

```graphql
# Bad
type Response {
  success: Boolean!
  data: JSON
  error: String
}

# Good
type CreateUserPayload {
  user: User
  errors: [CreateUserError!]
}
```

### Avoid Deep Nesting

```graphql
# Bad - allows unbounded depth
type User {
  friends: [User!]!  # friends.friends.friends...
}

# Good - use pagination
type User {
  friends(first: Int, after: String): FriendConnection!
}
```

### Avoid N+1 Design

```graphql
# Bad - separate queries needed
type Query {
  user(id: ID!): User
  userPosts(userId: ID!): [Post!]!
}

# Good - include in type
type User {
  posts(first: Int): [Post!]!
}
```

---

**Last Updated:** 2025-12-16
