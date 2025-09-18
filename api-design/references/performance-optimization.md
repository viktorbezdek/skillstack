# GraphQL Performance Optimization

Best practices for building high-performance GraphQL APIs.

## N+1 Query Problem

### The Problem

```graphql
query {
  posts {      # 1 query
    title
    author {   # N queries (one per post)
      name
    }
  }
}
```

```sql
-- Without optimization
SELECT * FROM posts;                    -- 1 query
SELECT * FROM users WHERE id = 1;       -- N queries
SELECT * FROM users WHERE id = 2;
SELECT * FROM users WHERE id = 3;
...
```

### Solution: DataLoader

```typescript
import DataLoader from 'dataloader';

// Create loader
const userLoader = new DataLoader<string, User>(async (userIds) => {
  // Single batched query
  const users = await prisma.user.findMany({
    where: { id: { in: [...userIds] } }
  });

  // Return in same order as requested
  const userMap = new Map(users.map(u => [u.id, u]));
  return userIds.map(id => userMap.get(id) ?? null);
});

// Use in resolver
const resolvers = {
  Post: {
    author: (post, _, { loaders }) => {
      return loaders.userLoader.load(post.authorId);
    },
  },
};
```

```sql
-- With DataLoader
SELECT * FROM posts;                           -- 1 query
SELECT * FROM users WHERE id IN (1, 2, 3...);  -- 1 batched query
```

### DataLoader Best Practices

1. **Create fresh loaders per request**
   ```typescript
   context: () => ({
     loaders: {
       userLoader: new DataLoader(batchUsers),
       postLoader: new DataLoader(batchPosts),
     },
   }),
   ```

2. **Handle null results**
   ```typescript
   return userIds.map(id => userMap.get(id) ?? null);
   ```

3. **Batch related entities**
   ```typescript
   const postsByAuthorLoader = new DataLoader<string, Post[]>(
     async (authorIds) => {
       const posts = await prisma.post.findMany({
         where: { authorId: { in: [...authorIds] } }
       });

       // Group by authorId
       const grouped = new Map<string, Post[]>();
       posts.forEach(post => {
         const existing = grouped.get(post.authorId) ?? [];
         grouped.set(post.authorId, [...existing, post]);
       });

       return authorIds.map(id => grouped.get(id) ?? []);
     }
   );
   ```

## Query Complexity Limiting

### Query Complexity Analysis

```typescript
import { createComplexityLimitRule } from 'graphql-validation-complexity';

const complexityLimitRule = createComplexityLimitRule(1000, {
  onCost: (cost) => console.log('Query cost:', cost),
  formatErrorMessage: (cost) =>
    `Query cost ${cost} exceeds maximum 1000`,
});

const server = new ApolloServer({
  typeDefs,
  resolvers,
  validationRules: [complexityLimitRule],
});
```

### Field-Level Complexity

```graphql
type Query {
  user(id: ID!): User           # Cost: 1
  users(first: Int): [User!]!   # Cost: first * 10
}

type User {
  id: ID!                       # Cost: 0
  name: String!                 # Cost: 0
  posts: [Post!]!               # Cost: 50 (expensive)
  friends: [User!]!             # Cost: 100 (very expensive)
}
```

```typescript
const complexityEstimators = [
  {
    type: 'Query',
    field: 'users',
    estimator: (args) => (args.first ?? 10) * 10,
  },
  {
    type: 'User',
    field: 'posts',
    estimator: () => 50,
  },
  {
    type: 'User',
    field: 'friends',
    estimator: () => 100,
  },
];
```

## Query Depth Limiting

### Prevent Deep Nesting

```typescript
import depthLimit from 'graphql-depth-limit';

const server = new ApolloServer({
  typeDefs,
  resolvers,
  validationRules: [depthLimit(5)],
});
```

```graphql
# Depth 5 - Allowed
query {
  user {              # 1
    posts {           # 2
      comments {      # 3
        author {      # 4
          name        # 5
        }
      }
    }
  }
}

# Depth 6 - Blocked
query {
  user {              # 1
    posts {           # 2
      comments {      # 3
        author {      # 4
          friends {   # 5
            name      # 6 - Exceeds limit!
          }
        }
      }
    }
  }
}
```

## Caching Strategies

### Response Caching

```typescript
import responseCachePlugin from '@apollo/server-plugin-response-cache';

const server = new ApolloServer({
  typeDefs,
  resolvers,
  plugins: [
    responseCachePlugin({
      sessionId: (context) => context.user?.id ?? null,
    }),
  ],
});
```

### Cache Hints in Schema

```graphql
type Query {
  user(id: ID!): User @cacheControl(maxAge: 60)
  publicPosts: [Post!]! @cacheControl(maxAge: 300, scope: PUBLIC)
}

type User @cacheControl(maxAge: 60) {
  id: ID!
  name: String!
  email: String! @cacheControl(maxAge: 0)  # Never cache
}
```

### Redis Caching Layer

```typescript
import Redis from 'ioredis';

const redis = new Redis(process.env.REDIS_URL);

const resolvers = {
  Query: {
    user: async (_, { id }) => {
      const cacheKey = `user:${id}`;

      // Check cache
      const cached = await redis.get(cacheKey);
      if (cached) {
        return JSON.parse(cached);
      }

      // Query database
      const user = await prisma.user.findUnique({ where: { id } });

      // Cache for 5 minutes
      if (user) {
        await redis.setex(cacheKey, 300, JSON.stringify(user));
      }

      return user;
    },
  },
};
```

### Apollo Client Caching

```typescript
// Client-side caching
const cache = new InMemoryCache({
  typePolicies: {
    Query: {
      fields: {
        user: {
          read(_, { args, toReference }) {
            return toReference({
              __typename: 'User',
              id: args?.id,
            });
          },
        },
      },
    },
    User: {
      keyFields: ['id'],
      fields: {
        posts: {
          merge(existing = [], incoming) {
            return [...existing, ...incoming];
          },
        },
      },
    },
  },
});
```

## Persisted Queries

### Automatic Persisted Queries (APQ)

```typescript
// Server
import { ApolloServerPluginCacheControl } from '@apollo/server/plugin/cacheControl';

const server = new ApolloServer({
  typeDefs,
  resolvers,
  plugins: [
    ApolloServerPluginCacheControl({
      defaultMaxAge: 60,
    }),
  ],
  persistedQueries: {
    cache: new KeyValueCache(), // Redis recommended
  },
});
```

```typescript
// Client
import { createPersistedQueryLink } from '@apollo/client/link/persisted-queries';
import { sha256 } from 'crypto-hash';

const link = createPersistedQueryLink({ sha256 });
```

### Static Persisted Queries

```json
// persisted-queries.json
{
  "abc123": "query GetUser($id: ID!) { user(id: $id) { id name } }",
  "def456": "mutation CreatePost($input: CreatePostInput!) { createPost(input: $input) { id } }"
}
```

```typescript
// Server validates against whitelist
const server = new ApolloServer({
  typeDefs,
  resolvers,
  persistedQueries: {
    cache: new KeyValueCache(),
  },
  plugins: [
    {
      async requestDidStart() {
        return {
          async didResolveOperation(context) {
            const queryHash = context.request.extensions?.persistedQuery?.sha256Hash;
            if (queryHash && !allowedQueries.has(queryHash)) {
              throw new Error('Query not in allowlist');
            }
          },
        };
      },
    },
  ],
});
```

## Database Optimization

### Select Only Needed Fields

```typescript
// Bad - fetches all columns
const user = await prisma.user.findUnique({
  where: { id },
});

// Good - select only requested fields
const user = await prisma.user.findUnique({
  where: { id },
  select: {
    id: true,
    name: true,
    email: true,
  },
});
```

### Analyze GraphQL Info

```typescript
import { parseResolveInfo, simplifyParsedResolveInfoFragmentType } from 'graphql-parse-resolve-info';

const resolvers = {
  Query: {
    user: async (_, { id }, context, info) => {
      const parsedInfo = parseResolveInfo(info);
      const { fields } = simplifyParsedResolveInfoFragmentType(parsedInfo, returnType);

      // Build select object from requested fields
      const select = Object.keys(fields).reduce((acc, field) => {
        acc[field] = true;
        return acc;
      }, {});

      return prisma.user.findUnique({
        where: { id },
        select,
      });
    },
  },
};
```

### Efficient Pagination

```typescript
// Cursor-based pagination (efficient)
const posts = await prisma.post.findMany({
  take: first,
  skip: after ? 1 : 0,
  cursor: after ? { id: after } : undefined,
  orderBy: { createdAt: 'desc' },
});

// Avoid offset pagination for large datasets
// Offset requires scanning all skipped rows
const posts = await prisma.post.findMany({
  take: limit,
  skip: offset,  // Slow for large offsets
});
```

### Use Database Indexes

```prisma
model Post {
  id        String   @id @default(uuid())
  title     String
  authorId  String
  createdAt DateTime @default(now())
  published Boolean  @default(false)

  // Indexes for common queries
  @@index([authorId])
  @@index([createdAt])
  @@index([published, createdAt])
}
```

## Subscription Optimization

### Filtered Subscriptions

```typescript
import { withFilter } from 'graphql-subscriptions';

const resolvers = {
  Subscription: {
    postCreated: {
      subscribe: withFilter(
        () => pubsub.asyncIterator(['POST_CREATED']),
        (payload, variables, context) => {
          // Only notify relevant users
          if (variables.authorId) {
            return payload.postCreated.authorId === variables.authorId;
          }
          return true;
        }
      ),
    },
  },
};
```

### Throttle Subscription Updates

```typescript
import { throttle } from 'lodash';

const publishThrottled = throttle(
  (event, payload) => pubsub.publish(event, payload),
  100  // Max one publish per 100ms
);
```

### Use Redis PubSub for Scale

```typescript
import { RedisPubSub } from 'graphql-redis-subscriptions';

const pubsub = new RedisPubSub({
  publisher: new Redis(process.env.REDIS_URL),
  subscriber: new Redis(process.env.REDIS_URL),
});
```

## Response Optimization

### Field Trimming

```typescript
// Remove null fields from response
const formatResponse = (response) => {
  return JSON.parse(JSON.stringify(response, (key, value) => {
    return value === null ? undefined : value;
  }));
};
```

### Compression

```typescript
import compression from 'compression';

// Express middleware
app.use(compression());

// Or in Apollo Server
const server = new ApolloServer({
  typeDefs,
  resolvers,
  plugins: [
    {
      requestDidStart() {
        return {
          willSendResponse({ response }) {
            // Response is automatically compressed if Accept-Encoding: gzip
          },
        };
      },
    },
  ],
});
```

## Monitoring and Profiling

### Apollo Studio Tracing

```typescript
const server = new ApolloServer({
  typeDefs,
  resolvers,
  plugins: [
    ApolloServerPluginUsageReporting({
      sendVariableValues: { all: true },
      sendHeaders: { all: true },
    }),
  ],
});
```

### Custom Resolver Timing

```typescript
const resolvers = {
  Query: {
    users: async (_, args, context) => {
      const start = Date.now();

      const result = await prisma.user.findMany();

      const duration = Date.now() - start;
      console.log(`users query: ${duration}ms`);

      return result;
    },
  },
};
```

### Query Logging Plugin

```typescript
const loggingPlugin = {
  async requestDidStart(requestContext) {
    const start = Date.now();
    console.log('Query:', requestContext.request.query);

    return {
      async willSendResponse() {
        const duration = Date.now() - start;
        console.log(`Response time: ${duration}ms`);
      },
      async didEncounterErrors({ errors }) {
        console.error('Errors:', errors);
      },
    };
  },
};
```

## Performance Checklist

### Query Optimization
- [ ] DataLoader for all relationships
- [ ] Query complexity limits
- [ ] Depth limiting
- [ ] Pagination for all lists

### Caching
- [ ] Response caching configured
- [ ] Cache hints on types/fields
- [ ] Redis for distributed caching
- [ ] APQ or static persisted queries

### Database
- [ ] Indexes on foreign keys
- [ ] Select only needed fields
- [ ] Cursor-based pagination
- [ ] Query logging enabled

### Monitoring
- [ ] Apollo Studio connected
- [ ] Resolver timing logged
- [ ] Error tracking configured
- [ ] Performance baselines established

---

**Last Updated:** 2025-12-16
