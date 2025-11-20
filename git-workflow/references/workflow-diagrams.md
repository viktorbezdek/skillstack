# Story Tree Workflow Diagrams

This document provides visual representations of the key workflows and data structures used by the story-tree skill system.

**Document structure:** Conceptual model → Data storage → Operational workflows

---

## Table of Contents

1. [Definitions](#definitions)
2. [Three-Field Workflow Model](#three-field-workflow-model)
   - Stage Transitions
   - Multi-Faceted Stage Meanings
   - Hold States
   - Disposition States
3. [Database Architecture](#database-architecture)
   - Closure Table Data Structure
   - Closure Table Path Example
   - Node Insertion Process
   - Dynamic Capacity Calculation
4. [Skill Workflows](#skill-workflows)
   - Main Update Workflow
   - Priority Algorithm Decision Flow
   - Git Commit Analysis Process
   - Story Generation Flow

---

## Definitions

| Term | Definition |
|------|------------|
| **Story node** | A unit of work in the hierarchical backlog—can be an epic, feature, capability, or task depending on depth. May have its own direct work AND children simultaneously. |
| **Stage** | The current workflow phase of a story (e.g., `concept`, `approved`, `active`, `implemented`); represents multi-faceted state covering both own work and children's work |
| **Hold reason** | A temporary blocking state that preserves the current stage (e.g., `blocked`, `paused`, `polish`, `wishlist`) |
| **Disposition** | A terminal state indicating the story will not progress further (e.g., `rejected`, `deprecated`, `archived`) |
| **Closure table** | A database pattern that stores all ancestor-descendant relationships, enabling efficient hierarchy queries |
| **Capacity** | The maximum number of children a node can have; grows dynamically based on completed work |
| **Depth** | A node's level in the tree (root=0, features=1, capabilities=2, tasks=3+) |
| **Fill rate** | Ratio of current children to capacity; used for prioritization |
| **Checkpoint** | The last analyzed git commit hash; enables incremental scanning |

---

## Three-Field Workflow Model

Stories progress through stages, with holds and dispositions as orthogonal states. The three fields work together:

- **stage**: Where the story is in the normal workflow
- **hold_reason**: Why work is temporarily stopped (nullable)
- **disposition**: Why the story was terminated (nullable)

### Stage Transitions (Normal Workflow)

```mermaid
stateDiagram-v2
    [*] --> concept: New idea created

    concept --> approved: Human approves

    approved --> planned: Plan created

    planned --> active: Dependencies met, work begins

    active --> reviewing: Code complete

    reviewing --> verifying: Review passed

    verifying --> implemented: Verification passed

    implemented --> ready: Fully tested

    ready --> released: Shipped

    released --> [*]
```

### Multi-Faceted Stage Meanings

Each stage represents multiple facets that apply simultaneously. A node can have its own direct work AND organize child work at the same time—these are not mutually exclusive.

| Stage | Facets (all apply at once) |
|-------|----------------------------|
| `concept` | New idea proposed |
| `approved` | Ready for own implementation planning; ready to receive child concept proposals |
| `planned` | Own implementation planned; dependencies verified; children have been approved |
| `active` | Own code in progress; children's code in progress |
| `reviewing` | Own code under review; reviewing child code |
| `verifying` | Own implementation being tested; verifying integration with children |
| `implemented` | Own code complete; all children implemented and integrated |
| `ready` | Own work fully tested; entire subtree fully tested |
| `released` | Shipped |

**Key insight:** A node cannot reach `implemented` until both its own work is complete AND all children have reached `implemented` or later. This keeps attention focused on incomplete work rather than dispersing it up the hierarchy.

### Hold States (Temporary, Preserves Stage)

```mermaid
mindmap
  root((Any Stage))
    queued
      Awaiting automated processing
      Clear: Algorithm runs
    pending
      Awaiting human decision
      Clear: Human decides
    paused
      Work paused
      Clear: Resume work
    blocked
      Missing dependency
      Clear: Unblocked
    broken
      Issues found
      Clear: Fixed
    polish
      Needs refinement
      Clear: Refinement complete
    wishlist
      Indefinite hold, maybe someday
      Clear: Priority increases
```

### Disposition States (Terminal)

```mermaid
stateDiagram-v2
    state "Any Stage" as any

    any --> rejected: Not pursuing
    any --> infeasible: Cannot build
    any --> legacy: Superseded
    any --> deprecated: No longer relevant
    any --> archived: Preserved only

    rejected --> [*]
    infeasible --> [*]
    legacy --> [*]
    deprecated --> [*]
    archived --> [*]
```

---

## Database Architecture

### Closure Table Data Structure

The closure table pattern stores all ancestor-descendant relationships, enabling efficient hierarchy queries without recursion.

```mermaid
erDiagram
    story_nodes {
        text id PK
        text title
        text description
        int capacity
        text stage
        text hold_reason
        text disposition
        int human_review
        text project_path
        text last_implemented
        text created_at
        text updated_at
    }

    story_paths {
        text ancestor_id FK
        text descendant_id FK
        int depth
    }

    story_commits {
        text story_id FK
        text commit_hash PK
        text commit_date
        text commit_message
    }

    metadata {
        text key PK
        text value
    }

    story_nodes ||--o{ story_paths : "ancestor"
    story_nodes ||--o{ story_paths : "descendant"
    story_nodes ||--o{ story_commits : "linked"
```

### Closure Table Path Example

This diagram illustrates how the closure table stores paths for a simple three-node hierarchy.

```mermaid
flowchart TD
    subgraph Tree Structure
        ROOT[root] --> N1[1.1]
        N1 --> N2[1.1.1]
    end

    subgraph Closure Table Entries
        direction LR
        P1["(root, root, 0)"]
        P2["(root, 1.1, 1)"]
        P3["(root, 1.1.1, 2)"]
        P4["(1.1, 1.1, 0)"]
        P5["(1.1, 1.1.1, 1)"]
        P6["(1.1.1, 1.1.1, 0)"]
    end

    ROOT -.-> P1
    ROOT -.-> P2
    ROOT -.-> P3
    N1 -.-> P4
    N1 -.-> P5
    N2 -.-> P6
```

Each entry represents a path from ancestor to descendant with the distance between them. Self-references (depth 0) ensure every node appears in queries. This structure allows finding all descendants or ancestors with a single query.

### Node Insertion Process

Adding a new node requires updating both the nodes table and the closure table.

```mermaid
sequenceDiagram
    participant S as Skill
    participant N as story_nodes
    participant P as story_paths

    S->>N: INSERT new node (id, title, description, status)
    N-->>S: Node created

    S->>P: SELECT all paths where descendant = parent_id
    P-->>S: Return parent's ancestor paths

    S->>P: INSERT paths with new_id as descendant, depth + 1
    P-->>S: Ancestor paths copied

    S->>P: INSERT self-reference (new_id, new_id, 0)
    P-->>S: Self-reference added

    Note over S,P: Node is now fully integrated into tree hierarchy
```

### Dynamic Capacity Calculation

Capacity grows organically based on completed work rather than speculation.

```mermaid
flowchart LR
    subgraph Formula
        BASE[Base: 3] --> PLUS[+]
        PLUS --> IMPL[Count of implemented/ready children]
        IMPL --> RESULT[= Effective Capacity]
    end

    subgraph Example
        E1["New node: 3 + 0 = 3"]
        E2["1 child done: 3 + 1 = 4"]
        E3["3 children done: 3 + 3 = 6"]
    end

    RESULT --> E1
    RESULT --> E2
    RESULT --> E3
```

---

## Skill Workflows

### Main Update Workflow

The primary workflow executes when the skill receives an update command. It proceeds through seven sequential steps.

```mermaid
flowchart TD
    START([User invokes skill]) --> STALE{Database > 3 days old?}
    STALE -->|Yes| FORCE[Force full update first]
    FORCE --> STEP1
    STALE -->|No| STEP1

    STEP1[Step 1: Load Current Tree] --> DB_EXISTS{Database exists?}
    DB_EXISTS -->|No| INIT[Initialize new database]
    INIT --> SEED[Seed root node from project metadata]
    SEED --> STEP2
    DB_EXISTS -->|Yes| STEP2

    STEP2[Step 2: Analyze Git Commits] --> CHECKPOINT{Valid checkpoint exists?}
    CHECKPOINT -->|Yes| INCREMENTAL[Incremental scan from checkpoint]
    CHECKPOINT -->|No| FULL[Full 30-day scan]
    INCREMENTAL --> MATCH
    FULL --> MATCH
    MATCH[Match commits to stories] --> UPDATE_STATUS[Update story statuses]
    UPDATE_STATUS --> SAVE_CHECKPOINT[Save new checkpoint]
    SAVE_CHECKPOINT --> STEP3

    STEP3[Step 3: Calculate Tree Metrics] --> METRICS[Query depth, child count, fill rate per node]
    METRICS --> STEP4

    STEP4[Step 4: Identify Priority Target] --> FILTER[Filter eligible nodes]
    FILTER --> SORT[Sort by depth then fill rate]
    SORT --> SELECT[Select top priority node]
    SELECT --> STEP5

    STEP5[Step 5: Generate Stories] --> CONTEXT[Gather parent and sibling context]
    CONTEXT --> GENERATE[Generate 1-3 concept stories]
    GENERATE --> VALIDATE[Validate against quality checks]
    VALIDATE --> STEP6

    STEP6[Step 6: Update Tree] --> INSERT[Insert new nodes]
    INSERT --> CLOSURE[Populate closure table paths]
    CLOSURE --> TIMESTAMP[Update lastUpdated metadata]
    TIMESTAMP --> STEP7

    STEP7[Step 7: Output Report] --> REPORT([Generate summary report])
```

## Priority Algorithm Decision Flow

The priority algorithm determines which node should receive new children. Depth takes absolute precedence over fill rate.

```mermaid
flowchart TD
    START([Find priority target]) --> QUERY[Query all nodes]
    QUERY --> FILTER{Node eligible?}

    FILTER -->|stage = concept| SKIP[Skip this node]
    FILTER -->|hold_reason set| SKIP
    FILTER -->|disposition set| SKIP
    SKIP --> NEXT_NODE[Check next node]
    NEXT_NODE --> FILTER

    FILTER -->|stage != concept,<br/>no hold, no disposition| CAPACITY{Under capacity?}
    CAPACITY -->|No| SKIP
    CAPACITY -->|Yes| ADD[Add to candidates]
    ADD --> NEXT_NODE

    NEXT_NODE -->|No more nodes| SORT[Sort candidates]
    SORT --> DEPTH[Primary: Sort by depth ascending]
    DEPTH --> FILL[Secondary: Sort by fill rate ascending]
    FILL --> RESULT([Return first candidate])

    style RESULT fill:#90EE90
```

## Git Commit Analysis Process

The skill analyzes git history to detect implementation progress and update story statuses.

```mermaid
flowchart TD
    START([Begin git analysis]) --> GET_CHECKPOINT[Get lastAnalyzedCommit from metadata]
    GET_CHECKPOINT --> HAS_CHECKPOINT{Checkpoint exists?}

    HAS_CHECKPOINT -->|No| FULL_SCAN[Run: git log --since 30 days ago]
    HAS_CHECKPOINT -->|Yes| VALIDATE[Validate checkpoint in git history]

    VALIDATE --> VALID{Commit still exists?}
    VALID -->|No| LOG_REASON[Log: checkpoint rebased away]
    LOG_REASON --> FULL_SCAN
    VALID -->|Yes| INCREMENTAL[Run: git log checkpoint..HEAD]

    FULL_SCAN --> PARSE
    INCREMENTAL --> PARSE

    PARSE[Parse commit hash, date, message] --> FOREACH[For each commit]

    FOREACH --> EXTRACT[Extract keywords from message]
    EXTRACT --> QUERY_STORIES[Query non-deprecated stories]
    QUERY_STORIES --> COMPARE[Compare keywords via Jaccard similarity]

    COMPARE --> THRESHOLD{Similarity >= 0.7?}
    THRESHOLD -->|Yes| STRONG[Strong match: link and update status]
    THRESHOLD -->|No| WEAK{Similarity >= 0.4?}
    WEAK -->|Yes| POTENTIAL[Potential match: link only]
    WEAK -->|No| NO_MATCH[No match]

    STRONG --> NEXT_COMMIT
    POTENTIAL --> NEXT_COMMIT
    NO_MATCH --> NEXT_COMMIT

    NEXT_COMMIT[Process next commit] --> MORE{More commits?}
    MORE -->|Yes| FOREACH
    MORE -->|No| SAVE[Save newest commit as checkpoint]
    SAVE --> DONE([Analysis complete])
```

## Story Generation Flow

When a priority target is identified, the skill generates contextually appropriate stories.

```mermaid
flowchart TD
    START([Generate stories for target node]) --> GET_DEPTH[Determine target node depth]

    GET_DEPTH --> DEPTH0{Depth 0 - Root?}
    DEPTH0 -->|Yes| ROOT_CONTEXT[Read project vision]
    ROOT_CONTEXT --> GEN_FEATURES[Generate major feature concepts]

    DEPTH0 -->|No| DEPTH1{Depth 1 - Feature?}
    DEPTH1 -->|Yes| FEATURE_CONTEXT[Read feature description]
    FEATURE_CONTEXT --> GEN_CAPABILITIES[Generate capability concepts]

    DEPTH1 -->|No| DETAIL_CONTEXT[Read parent capability]
    DETAIL_CONTEXT --> GEN_DETAILS[Generate implementation concepts]

    GEN_FEATURES --> SIBLINGS
    GEN_CAPABILITIES --> SIBLINGS
    GEN_DETAILS --> SIBLINGS

    SIBLINGS[Review existing sibling nodes] --> GIT_CONTEXT[Analyze relevant git commits]
    GIT_CONTEXT --> CREATE[Create 1-3 new story concepts]

    CREATE --> LIMIT{Exceeded 3 stories?}
    LIMIT -->|Yes| TRIM[Trim to maximum 3]
    LIMIT -->|No| FORMAT
    TRIM --> FORMAT

    FORMAT[Format as user stories] --> QUALITY{Pass quality checks?}

    QUALITY -->|No| REVISE[Revise story content]
    REVISE --> QUALITY

    QUALITY -->|Yes| OUTPUT([Return generated stories])

    style OUTPUT fill:#90EE90
```
