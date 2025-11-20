# SQL Query Reference

All SQL patterns for story-tree operations. Use `grep` to find specific queries.

## Priority Algorithm

### Find Under-Capacity Priority Target

```sql
SELECT s.*,
    (SELECT COUNT(*) FROM story_paths WHERE ancestor_id = s.id AND depth = 1) as child_count,
    (SELECT MIN(depth) FROM story_paths WHERE descendant_id = s.id) as node_depth,
    COALESCE(s.capacity, 3 + (SELECT COUNT(*) FROM story_paths sp
         JOIN story_nodes child ON sp.descendant_id = child.id
         WHERE sp.ancestor_id = s.id AND sp.depth = 1
         AND child.status IN ('implemented', 'ready'))) as effective_capacity
FROM story_nodes s
WHERE s.status NOT IN ('concept', 'rejected', 'deprecated', 'infeasible', 'bugged')
  AND (SELECT COUNT(*) FROM story_paths WHERE ancestor_id = s.id AND depth = 1) <
      COALESCE(s.capacity, 3 + (SELECT COUNT(*) FROM story_paths sp
           JOIN story_nodes child ON sp.descendant_id = child.id
           WHERE sp.ancestor_id = s.id AND sp.depth = 1
           AND child.status IN ('implemented', 'ready')))
ORDER BY node_depth ASC
LIMIT 1;
```

### Manual Override (user-specified node)

```sql
SELECT s.*,
    (SELECT COUNT(*) FROM story_paths WHERE ancestor_id = s.id AND depth = 1) as child_count
FROM story_nodes s
WHERE s.id = :user_specified_node_id
  AND s.status NOT IN ('deprecated', 'rejected', 'infeasible');
```

---

## Tree Navigation

### Get Direct Children

```sql
SELECT s.* FROM story_nodes s
JOIN story_paths st ON s.id = st.descendant_id
WHERE st.ancestor_id = :parent_id AND st.depth = 1
ORDER BY s.id;
```

### Get Entire Subtree

```sql
SELECT s.*, st.depth as relative_depth FROM story_nodes s
JOIN story_paths st ON s.id = st.descendant_id
WHERE st.ancestor_id = :root_id
ORDER BY st.depth, s.id;
```

### Get Ancestors (Path to Root)

```sql
SELECT s.*, st.depth as distance FROM story_nodes s
JOIN story_paths st ON s.id = st.ancestor_id
WHERE st.descendant_id = :node_id
ORDER BY st.depth DESC;
```

### Get Parent

```sql
SELECT s.* FROM story_nodes s
JOIN story_paths st ON s.id = st.ancestor_id
WHERE st.descendant_id = :node_id AND st.depth = 1;
```

### Get Node Depth

```sql
SELECT MIN(depth) as node_depth FROM story_paths WHERE descendant_id = :node_id;
```

### Get Siblings

```sql
SELECT s.* FROM story_nodes s
JOIN story_paths st ON s.id = st.descendant_id
WHERE st.ancestor_id = (
    SELECT ancestor_id FROM story_paths WHERE descendant_id = :node_id AND depth = 1
) AND st.depth = 1 AND s.id != :node_id;
```

---

## Tree Metrics

### Count by Status

```sql
SELECT status, COUNT(*) as count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM story_nodes), 1) as pct
FROM story_nodes GROUP BY status ORDER BY count DESC;
```

### Count by Depth

```sql
SELECT
    (SELECT MIN(depth) FROM story_paths WHERE descendant_id = s.id) as node_depth,
    COUNT(*) as count
FROM story_nodes s GROUP BY node_depth ORDER BY node_depth;
```

### All Stories with Metrics

```sql
SELECT s.id, s.title, s.status, s.capacity,
    (SELECT MIN(depth) FROM story_paths WHERE descendant_id = s.id) as depth,
    (SELECT COUNT(*) FROM story_paths WHERE ancestor_id = s.id AND depth = 1) as children
FROM story_nodes s ORDER BY depth, s.id;
```

---

## Capacity Management

### Detect Over-Capacity

```sql
SELECT s.id, s.title, s.capacity,
    (SELECT COUNT(*) FROM story_paths WHERE ancestor_id = s.id AND depth = 1) as children,
    (SELECT COUNT(*) FROM story_paths WHERE ancestor_id = s.id AND depth = 1) - s.capacity as excess
FROM story_nodes s
WHERE (SELECT COUNT(*) FROM story_paths WHERE ancestor_id = s.id AND depth = 1) > s.capacity;
```

### Capacity Summary by Level

```sql
SELECT
    (SELECT MIN(depth) FROM story_paths WHERE descendant_id = s.id) as level,
    COUNT(*) as nodes,
    SUM((SELECT COUNT(*) FROM story_paths WHERE ancestor_id = s.id AND depth = 1)) as children,
    SUM(COALESCE(s.capacity, 3)) as capacity
FROM story_nodes s
GROUP BY level ORDER BY level;
```

### Update Capacity

```sql
UPDATE story_nodes SET capacity = :new_capacity, updated_at = datetime('now')
WHERE id = :node_id;
```

### Validate Capacity Change

```sql
SELECT
    CASE WHEN (SELECT COUNT(*) FROM story_paths WHERE ancestor_id = :node_id AND depth = 1) > :new_capacity
    THEN 'INVALID: Would cause over-capacity' ELSE 'VALID' END as result;
```

---

## Commit Analysis

### Get Commits to Analyze

```bash
LAST_COMMIT=$(sqlite3 .claude/data/story-tree.db "SELECT value FROM metadata WHERE key = 'lastAnalyzedCommit';")

if [ -z "$LAST_COMMIT" ] || ! git cat-file -t "$LAST_COMMIT" &>/dev/null; then
    git log --since="30 days ago" --pretty=format:"%h|%ai|%s" --no-merges
else
    git log "$LAST_COMMIT"..HEAD --pretty=format:"%h|%ai|%s" --no-merges
fi
```

### Check if Commit Already Linked

```sql
SELECT story_id FROM story_commits WHERE commit_hash = :commit_hash;
```

### Link Commit to Story

```sql
INSERT OR IGNORE INTO story_commits (story_id, commit_hash, commit_date, commit_message)
VALUES (:story_id, :commit_hash, :commit_date, :commit_message);
```

### Update Story Status from Commits

```sql
UPDATE story_nodes
SET status = CASE
        WHEN status IN ('planned', 'in-progress') THEN 'implemented'
        WHEN status = 'concept' THEN 'in-progress'
        ELSE status
    END,
    last_implemented = :commit_date,
    updated_at = datetime('now')
WHERE id = :story_id AND status IN ('concept', 'planned', 'in-progress');
```

### Stories with Commit Counts

```sql
SELECT s.id, s.title, s.status,
    COUNT(sc.commit_hash) as commits,
    MAX(sc.commit_date) as latest
FROM story_nodes s
LEFT JOIN story_commits sc ON s.id = sc.story_id
GROUP BY s.id ORDER BY commits DESC;
```

### Update Checkpoint

```sql
INSERT OR REPLACE INTO metadata (key, value) VALUES ('lastAnalyzedCommit', :commit_hash);
INSERT OR REPLACE INTO metadata (key, value) VALUES ('lastUpdated', datetime('now'));
```

---

## Pattern Matching

### Keyword Extraction Rules

1. Convert to lowercase
2. Remove special characters except hyphens
3. Split on whitespace
4. Filter words < 3 characters
5. Filter stop words: a, an, and, are, as, at, be, by, for, from, has, he, in, is, it, its, of, on, that, the, to, was, will, with, this, but, they, have, had, what, when, where, who, which, why, how
6. Filter pure numbers
7. Keep compound terms (e.g., "drag-and-drop")

### Commit Type Detection

| Pattern | Type |
|---------|------|
| `^feat[:(]` | feature |
| `^fix[:(]` | fix |
| `^refactor[:(]` | refactor |
| `^docs[:(]` | docs |
| `^test[:(]` | test |
| `^chore[:(]` | chore |
| `(add\|implement\|create)` | feature |
| `(fix\|bug\|issue)` | fix |

### Similarity Thresholds

Jaccard similarity = |intersection| / |union|
- ≥ 0.7: Strong match (auto-link, update status)
- ≥ 0.4: Potential match (link, review recommended)
- < 0.4: No match

---

## Insert Operations

### Add New Story Node

```sql
-- Step 1: Insert node
INSERT INTO story_nodes (id, title, description, status, created_at, updated_at)
VALUES (:new_id, :title, :description, 'concept', datetime('now'), datetime('now'));

-- Step 2: Populate closure table
INSERT INTO story_paths (ancestor_id, descendant_id, depth)
SELECT ancestor_id, :new_id, depth + 1
FROM story_paths WHERE descendant_id = :parent_id
UNION ALL SELECT :new_id, :new_id, 0;
```

### Delete Node and Descendants

```sql
DELETE FROM story_nodes WHERE id IN (
    SELECT descendant_id FROM story_paths WHERE ancestor_id = :node_id
);
```

### Update Status

```sql
UPDATE story_nodes SET status = :new_status, updated_at = datetime('now')
WHERE id = :node_id;
```

---

## Gap Analysis

### Implemented Stories Without Commits

```sql
SELECT id, title FROM story_nodes
WHERE status = 'implemented'
  AND NOT EXISTS (SELECT 1 FROM story_commits WHERE story_id = id);
```

### In-Progress with Many Commits (might be done)

```sql
SELECT s.id, s.title, COUNT(sc.commit_hash) as commits
FROM story_nodes s
JOIN story_commits sc ON s.id = sc.story_id
WHERE s.status = 'in-progress'
GROUP BY s.id HAVING commits >= 3;
```

### Bug Cluster Detection

```sql
SELECT s.id, s.title, COUNT(sc.commit_hash) as fixes
FROM story_nodes s
JOIN story_commits sc ON s.id = sc.story_id
WHERE sc.commit_message LIKE 'fix:%' OR sc.commit_message LIKE '%bug%'
GROUP BY s.id HAVING fixes >= 2;
```

---

## Tree Visualization Data

For visualization, prefer `scripts/tree-view.py`. These queries support custom analysis:

```sql
SELECT s.id, s.title, s.status, s.capacity,
    (SELECT COUNT(*) FROM story_paths WHERE ancestor_id = s.id AND depth = 1) as children,
    (SELECT MIN(depth) FROM story_paths WHERE descendant_id = s.id) as depth
FROM story_nodes s ORDER BY depth, s.id;
```
