# Mermaid Cheat Sheet

Complete syntax reference for the Mermaid diagrams most useful for engineering documentation. Paste-ready snippets with the conventions explained.

## Flowchart

```mermaid
flowchart TD
    Start([Start]) --> Check{Is input valid?}
    Check -->|No| Error[Return 400]
    Check -->|Yes| Lookup[Lookup in cache]
    Lookup --> Hit{Cache hit?}
    Hit -->|Yes| Return[Return cached]
    Hit -->|No| Fetch[Fetch from DB]
    Fetch --> Store[Store in cache]
    Store --> Return
    Return --> End([End])
    Error --> End
```

### Direction

- `TD` / `TB` — top to bottom
- `LR` — left to right
- `BT` / `RL` — **avoid**; readers expect TD or LR

### Node shapes

| Syntax | Shape | Use for |
|---|---|---|
| `A[Label]` | Rectangle | Action / step |
| `A(Label)` | Rounded rectangle | Action / step (softer) |
| `A([Label])` | Stadium | Start / end |
| `A[[Label]]` | Subroutine | Sub-process |
| `A[(Label)]` | Cylinder | Database / storage |
| `A((Label))` | Circle | State |
| `A{Label}` | Rhombus | Decision |
| `A{{Label}}` | Hexagon | Preparation / setup |
| `A[/Label/]` | Parallelogram | Input / output |
| `A[\Label\]` | Parallelogram alt | Input / output |

### Arrows

| Syntax | Type |
|---|---|
| `A --> B` | Solid arrow |
| `A ==> B` | Thick solid arrow (emphasis) |
| `A -.-> B` | Dashed arrow |
| `A --x B` | Arrow with X (termination) |
| `A --o B` | Arrow with circle (aggregation) |
| `A -- text --> B` | Labeled arrow |
| `A -->|text| B` | Alternate labeled arrow |

### Subgraphs

```mermaid
flowchart LR
    subgraph Frontend
        Web[Web App]
        Mobile[Mobile App]
    end
    subgraph Backend
        API[API Server]
        DB[(Database)]
    end
    Web --> API
    Mobile --> API
    API --> DB
```

## Sequence diagram

```mermaid
sequenceDiagram
    autonumber
    participant U as User
    participant API as API Server
    participant DB as Database
    participant Cache as Redis

    U->>API: POST /login
    API->>Cache: Get session
    alt Cache hit
        Cache-->>API: session
    else Cache miss
        API->>DB: Query user
        DB-->>API: user row
        API->>Cache: Set session
    end
    API-->>U: 200 OK + token
```

### Arrows

| Syntax | Type |
|---|---|
| `A->>B: msg` | Solid arrow (synchronous) |
| `A-->>B: msg` | Dashed arrow (async / return) |
| `A-xB: msg` | Arrow with X (failed / terminated) |
| `A-)B: msg` | Open arrow (async message) |

### Control flow

```mermaid
sequenceDiagram
    A->>B: request
    alt success path
        B-->>A: ok
    else failure path
        B-->>A: error
    end

    loop every minute
        A->>B: ping
        B-->>A: pong
    end

    par fan out
        A->>B: task 1
    and
        A->>C: task 2
    end

    opt optional step
        A->>B: maybe
    end

    Note over A,B: shared note
```

### Useful directives

- `autonumber` — numbers each step (adds referenceability).
- `participant X as "Long name"` — short ID, full label.
- `activate A` / `deactivate A` — shows lifelines.

## State diagram

```mermaid
stateDiagram-v2
    [*] --> Draft
    Draft --> Reviewing: submit
    Reviewing --> Draft: reject
    Reviewing --> Accepted: approve
    Accepted --> Superseded: new ADR
    Accepted --> [*]
    Superseded --> [*]
```

### Composite states

```mermaid
stateDiagram-v2
    [*] --> Processing
    state Processing {
        [*] --> Fetching
        Fetching --> Transforming: fetched
        Transforming --> Storing: transformed
        Storing --> [*]
    }
    Processing --> Done
    Done --> [*]
```

### Parallel regions

```mermaid
stateDiagram-v2
    [*] --> Running
    state Running {
        [*] --> UIActive
        UIActive --> UIIdle
        --
        [*] --> DataFlowing
        DataFlowing --> DataStalled
    }
```

## ER diagram

```mermaid
erDiagram
    USER ||--o{ ORDER : places
    ORDER ||--|{ LINE_ITEM : contains
    ORDER }o--|| ADDRESS : "ships to"
    USER {
        uuid id PK
        string email UK
        string name
        timestamp created_at
    }
    ORDER {
        uuid id PK
        uuid user_id FK
        decimal total
        timestamp created_at
    }
    LINE_ITEM {
        uuid id PK
        uuid order_id FK
        uuid product_id FK
        int quantity
        decimal price
    }
    ADDRESS {
        uuid id PK
        string street
        string city
        string country
    }
```

### Cardinality

| Syntax | Meaning |
|---|---|
| `||--||` | Exactly one to exactly one |
| `||--o{` | One to zero-or-many |
| `||--|{` | One to one-or-many |
| `}o--o{` | Zero-or-many to zero-or-many |
| `}|--|{` | One-or-many to one-or-many |

Read left-to-right: `A ||--o{ B` = "one A has zero-or-many B".

### Key types

- `PK` — primary key
- `FK` — foreign key
- `UK` — unique key

## Class diagram

```mermaid
classDiagram
    class Animal {
        +String name
        +int age
        +speak() void
    }
    class Dog {
        +String breed
        +bark() void
    }
    class Cat {
        -Boolean purring
        +meow() void
    }
    Animal <|-- Dog
    Animal <|-- Cat
    Dog "1" o-- "0..*" Toy : owns
```

### Relationships

| Syntax | Meaning |
|---|---|
| `<|--` | Inheritance |
| `<|..` | Realization (implements) |
| `o--` | Aggregation |
| `*--` | Composition |
| `<--` | Association |
| `..>` | Dependency |

### Visibility

- `+` public
- `-` private
- `#` protected
- `~` package

## Git graph

```mermaid
gitGraph
    commit
    commit
    branch feature
    checkout feature
    commit
    commit
    checkout main
    merge feature
    commit
```

## Pie chart

```mermaid
pie title Deploy methods
    "CI/CD pipeline" : 72
    "Manual" : 23
    "Scheduled" : 5
```

## Quadrant chart

```mermaid
quadrantChart
    title Prioritization — effort vs impact
    x-axis Low effort --> High effort
    y-axis Low impact --> High impact
    quadrant-1 Do first
    quadrant-2 Plan for
    quadrant-3 Delete
    quadrant-4 Quick wins
    Option A: [0.3, 0.8]
    Option B: [0.7, 0.6]
    Option C: [0.2, 0.2]
```

## Journey map

```mermaid
journey
    title User onboarding
    section Discover
      Land on site: 4: User
      Read docs: 3: User
    section Sign up
      Create account: 5: User
      Verify email: 2: User
      Complete profile: 4: User
    section First value
      Run first query: 5: User
```

## Configuration tips

### Themes

Add at top of diagram:

```
%%{init: {'theme':'base', 'themeVariables': { 'primaryColor': '#fff' }}}%%
```

Available themes: `default`, `neutral`, `dark`, `forest`, `base` (customizable).

### Rendering notes

- GitHub renders Mermaid natively in `.md` files and PR descriptions.
- GitLab renders natively.
- Notion renders in code blocks with `mermaid` language tag.
- VS Code needs the Mermaid extension for preview.
- For static export: `@mermaid-js/mermaid-cli` (`mmdc -i input.mmd -o output.svg`).

## Common mistakes

- **BT/RL direction** — readers expect TD or LR; inverse directions feel wrong.
- **Missing arrow labels** — every arrow in a decision flow should be labeled.
- **Too many nodes** — over ~15 nodes becomes unreadable; split or abstract.
- **Mixed shapes for same meaning** — pick one shape per concept (e.g., rounded rect = action always).
- **No legend for non-standard shapes** — unusual shapes without explanation confuse readers.
- **alt without end** — Mermaid won't render; every `alt` needs an `end`.
- **Unescaped special characters** — `<`, `>`, `|` in labels break rendering; use HTML entities or rewrite.
