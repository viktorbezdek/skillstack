# Apollo Federation Architecture Guide

Comprehensive guide for designing and implementing Apollo Federation supergraphs.

## Federation Overview

Apollo Federation enables composing multiple GraphQL services (subgraphs) into a unified API (supergraph) through a gateway.

```
┌─────────────────────────────────────────────┐
│              Client Application             │
└─────────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────┐
│             Apollo Gateway                   │
│         (Query Planning & Routing)           │
└─────────────────────────────────────────────┘
          │           │           │
          ▼           ▼           ▼
┌─────────────┐ ┌─────────────┐ ┌─────────────┐
│   Users     │ │   Orders    │ │   Products  │
│  Subgraph   │ │  Subgraph   │ │  Subgraph   │
└─────────────┘ └─────────────┘ └─────────────┘
```

## Key Concepts

### Entities

Entities are types that can be referenced across subgraphs. They're defined with the `@key` directive.

```graphql
# users-subgraph
type User @key(fields: "id") {
  id: ID!
  email: String!
  name: String!
}

# orders-subgraph
type Order @key(fields: "id") {
  id: ID!
  items: [OrderItem!]!
  customer: User!  # References User from another subgraph
}
```

### Reference Resolvers

When a subgraph needs to reference an entity it doesn't own, it uses a reference resolver:

```typescript
// orders-subgraph
const resolvers = {
  Order: {
    customer: (order) => {
      // Return a reference stub - gateway will resolve the full User
      return { __typename: 'User', id: order.customerId };
    },
  },
  User: {
    // Called by gateway to resolve User references
    __resolveReference: (reference) => {
      // Only resolve what this subgraph owns (if anything)
      return reference;
    },
  },
};
```

### Entity Extensions

Subgraphs can extend entities from other subgraphs:

```graphql
# products-subgraph owns Product
type Product @key(fields: "id") {
  id: ID!
  name: String!
  price: Int!
}

# reviews-subgraph extends Product
extend type Product @key(fields: "id") {
  id: ID! @external
  reviews: [Review!]!
  averageRating: Float
}
```

## Federation Directives

### @key

Defines entity's primary key for cross-subgraph references.

```graphql
# Single key
type User @key(fields: "id") {
  id: ID!
}

# Composite key
type OrderItem @key(fields: "orderId productId") {
  orderId: ID!
  productId: ID!
}

# Multiple keys
type User @key(fields: "id") @key(fields: "email") {
  id: ID!
  email: String!
}
```

### @external

Marks a field as owned by another subgraph.

```graphql
extend type User @key(fields: "id") {
  id: ID! @external
  email: String! @external  # Owned by users-subgraph
  orders: [Order!]!         # Owned by this subgraph
}
```

### @requires

Specifies external fields needed to resolve a field.

```graphql
extend type Product @key(fields: "id") {
  id: ID! @external
  price: Int! @external
  weight: Float! @external
  # Needs price and weight from products-subgraph to calculate
  shippingCost: Float! @requires(fields: "price weight")
}
```

### @provides

Indicates fields a resolver provides for nested entities.

```graphql
type Review @key(fields: "id") {
  id: ID!
  # When resolving author, this subgraph can provide username
  author: User! @provides(fields: "username")
}

extend type User @key(fields: "id") {
  id: ID! @external
  username: String! @external
}
```

### @shareable

Allows multiple subgraphs to resolve the same field.

```graphql
# Both subgraphs can resolve this field
type Product @key(fields: "id") {
  id: ID!
  name: String! @shareable
}
```

### @override

Migrates field ownership between subgraphs.

```graphql
# New subgraph takes over field from old subgraph
type Product @key(fields: "id") {
  id: ID! @external
  inventory: Int! @override(from: "products")
}
```

## Subgraph Design Patterns

### Domain-Driven Boundaries

Organize subgraphs by business domain, not by technical layers.

**Good:**
```
users-subgraph     → User, Profile, Authentication
orders-subgraph    → Order, OrderItem, Payment
products-subgraph  → Product, Category, Inventory
reviews-subgraph   → Review, Rating
```

**Bad:**
```
read-subgraph      → All queries
write-subgraph     → All mutations
auth-subgraph      → Only auth logic
```

### Entity Ownership

Each entity should have one primary owner subgraph:

```graphql
# users-subgraph OWNS User
type User @key(fields: "id") {
  id: ID!
  email: String!
  name: String!
  profile: Profile
  createdAt: DateTime!
}

# orders-subgraph EXTENDS User
extend type User @key(fields: "id") {
  id: ID! @external
  orders: [Order!]!
  totalSpent: Float!
}

# reviews-subgraph EXTENDS User
extend type User @key(fields: "id") {
  id: ID! @external
  reviews: [Review!]!
  reviewCount: Int!
}
```

### Query Distribution

Distribute root query fields to appropriate subgraphs:

```graphql
# users-subgraph
type Query {
  user(id: ID!): User
  users(filter: UserFilter): UserConnection!
  me: User
}

# products-subgraph
type Query {
  product(id: ID!): Product
  products(filter: ProductFilter): ProductConnection!
  searchProducts(query: String!): [Product!]!
}

# orders-subgraph
type Query {
  order(id: ID!): Order
  orders(filter: OrderFilter): OrderConnection!
}
```

## Gateway Configuration

### IntrospectAndCompose (Development)

```typescript
import { ApolloGateway, IntrospectAndCompose } from '@apollo/gateway';

const gateway = new ApolloGateway({
  supergraphSdl: new IntrospectAndCompose({
    subgraphs: [
      { name: 'users', url: 'http://users:4001/graphql' },
      { name: 'products', url: 'http://products:4002/graphql' },
      { name: 'orders', url: 'http://orders:4003/graphql' },
    ],
  }),
});
```

### Managed Federation (Production)

```typescript
import { ApolloGateway } from '@apollo/gateway';

const gateway = new ApolloGateway({
  // Supergraph fetched from Apollo Studio
});

// Configure in Apollo Studio and use APOLLO_KEY env var
```

### Supergraph Composition (Manual)

```yaml
# supergraph.yaml
federation_version: 2
subgraphs:
  users:
    routing_url: http://users:4001/graphql
    schema:
      file: ./subgraphs/users.graphql
  products:
    routing_url: http://products:4002/graphql
    schema:
      file: ./subgraphs/products.graphql
  orders:
    routing_url: http://orders:4003/graphql
    schema:
      file: ./subgraphs/orders.graphql
```

```bash
rover supergraph compose --config supergraph.yaml > supergraph.graphql
```

## Query Planning

The gateway creates query plans to resolve federated queries:

```graphql
query GetOrderDetails($orderId: ID!) {
  order(id: $orderId) {         # orders-subgraph
    id
    items {
      product {                  # products-subgraph
        name
        price
        reviews {                # reviews-subgraph
          rating
          author {               # users-subgraph
            name
          }
        }
      }
    }
    customer {                   # users-subgraph
      name
      email
    }
  }
}
```

**Query Plan:**
1. Fetch `order` from orders-subgraph
2. Fetch `product` references from products-subgraph
3. Parallel: Fetch `reviews` from reviews-subgraph
4. Fetch `author` and `customer` from users-subgraph

## Performance Optimization

### Minimize Cross-Subgraph Requests

```graphql
# Bad - multiple round trips
type Order @key(fields: "id") {
  id: ID!
  customerId: ID!
  customer: User!  # Requires users-subgraph lookup
}

# Better - denormalize when possible
type Order @key(fields: "id") {
  id: ID!
  customerId: ID!
  customerName: String!  # Stored locally
  customer: User!        # Only when full user needed
}
```

### Use @provides for Common Fields

```graphql
# reviews-subgraph already has author data
type Review @key(fields: "id") {
  id: ID!
  content: String!
  author: User! @provides(fields: "name")  # Avoid extra trip
}

extend type User @key(fields: "id") {
  id: ID! @external
  name: String! @external
}
```

### Batch with DataLoader

```typescript
// In each subgraph resolver
const resolvers = {
  User: {
    __resolveReference: async (refs, { loaders }) => {
      // Batch multiple references
      return loaders.userLoader.load(refs.id);
    },
  },
};
```

## Error Handling

### Subgraph Errors

```typescript
// Subgraph resolver
const resolvers = {
  Query: {
    user: async (_, { id }) => {
      const user = await db.user.findById(id);
      if (!user) {
        throw new GraphQLError('User not found', {
          extensions: {
            code: 'USER_NOT_FOUND',
            argumentName: 'id',
          },
        });
      }
      return user;
    },
  },
};
```

### Gateway Error Handling

```typescript
const gateway = new ApolloGateway({
  // ... config
});

const server = new ApolloServer({
  gateway,
  plugins: [
    {
      requestDidStart() {
        return {
          didEncounterErrors({ errors }) {
            errors.forEach((error) => {
              console.error('GraphQL Error:', error);
            });
          },
        };
      },
    },
  ],
});
```

## Testing Federation

### Unit Testing Subgraphs

```typescript
import { buildSubgraphSchema } from '@apollo/subgraph';
import { ApolloServer } from '@apollo/server';

describe('Users Subgraph', () => {
  let server: ApolloServer;

  beforeAll(() => {
    const schema = buildSubgraphSchema([{ typeDefs, resolvers }]);
    server = new ApolloServer({ schema });
  });

  it('resolves user by id', async () => {
    const response = await server.executeOperation({
      query: `
        query GetUser($id: ID!) {
          user(id: $id) {
            id
            name
          }
        }
      `,
      variables: { id: '1' },
    });

    expect(response.body.data?.user).toBeDefined();
  });

  it('resolves __resolveReference', async () => {
    const response = await server.executeOperation({
      query: `
        query {
          _entities(representations: [{ __typename: "User", id: "1" }]) {
            ... on User {
              id
              name
            }
          }
        }
      `,
    });

    expect(response.body.data?._entities[0]).toBeDefined();
  });
});
```

### Integration Testing

```typescript
import { ApolloGateway, IntrospectAndCompose } from '@apollo/gateway';
import { ApolloServer } from '@apollo/server';

describe('Federated Graph', () => {
  let gateway: ApolloGateway;
  let server: ApolloServer;

  beforeAll(async () => {
    gateway = new ApolloGateway({
      supergraphSdl: new IntrospectAndCompose({
        subgraphs: [
          { name: 'users', url: 'http://localhost:4001/graphql' },
          { name: 'orders', url: 'http://localhost:4002/graphql' },
        ],
      }),
    });

    server = new ApolloServer({ gateway });
    await server.start();
  });

  it('resolves cross-subgraph query', async () => {
    const response = await server.executeOperation({
      query: `
        query {
          order(id: "1") {
            id
            customer {
              name
            }
          }
        }
      `,
    });

    expect(response.body.data?.order.customer.name).toBeDefined();
  });
});
```

## Migration Strategies

### Monolith to Federation

1. **Identify Domains** - Group types by business domain
2. **Extract First Subgraph** - Start with least coupled domain
3. **Gradual Migration** - Move types one at a time
4. **Use @override** - Safely transfer field ownership

### Adding New Subgraph

1. Define entity extensions for existing types
2. Add new types owned by subgraph
3. Implement reference resolvers
4. Deploy and compose into supergraph

### Removing Subgraph

1. Migrate entity ownership with @override
2. Remove entity extensions from other subgraphs
3. Update gateway configuration
4. Deprecate and remove subgraph

## Common Pitfalls

### Circular Dependencies

```graphql
# Avoid this
# users-subgraph
type User @key(fields: "id") {
  orders: [Order!]!  # References orders
}

# orders-subgraph
type Order @key(fields: "id") {
  customer: User!    # References users
}

# Solution: One subgraph extends, one owns the relationship
```

### Over-Fetching in Reference Resolvers

```typescript
// Bad - fetches full entity every time
User: {
  __resolveReference: async (ref) => {
    return db.user.findById(ref.id);  // Full query
  },
}

// Good - only resolve requested fields
User: {
  __resolveReference: async (ref, context, info) => {
    const requestedFields = getRequestedFields(info);
    return db.user.findById(ref.id, { select: requestedFields });
  },
}
```

### Missing @external

```graphql
# Wrong - missing @external
extend type User @key(fields: "id") {
  id: ID!          # Should be @external
  orders: [Order!]!
}

# Correct
extend type User @key(fields: "id") {
  id: ID! @external
  orders: [Order!]!
}
```

---

**Last Updated:** 2025-12-16
