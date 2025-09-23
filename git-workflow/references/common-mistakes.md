# Common Mistakes

Pitfalls identified through testing. Check this list before outputting stories.

---

## 1. Vague Stories

**Wrong:**
```markdown
### 1.2.3: Improve UX
**As a** user **I want** better experience **So that** I'm happier
```

**Right:**
```markdown
### 1.2.3: Add keyboard shortcuts to document table
**As a** lawyer reviewing documents
**I want** keyboard shortcuts (arrow keys, T for tag, F for flag)
**So that** I can review 40% faster without reaching for mouse

**Acceptance Criteria:**
- [ ] Arrow keys navigate next/previous
- [ ] 'T' opens tagging menu
- [ ] Shortcuts shown in help (?)

**Related context**: Commits a1b2c3d show keyboard handling in UploadTable.vue
```

**Fix:** Reference git commits, use specific user roles, measurable benefits, testable criteria.

---

## 2. Ignoring Priority Algorithm

**Wrong:** "Node 1.3.2.1 is empty (0/3), so highest priority."

**Right:** Depth takes precedence over fill rate.

Given:
- Root (5/10, depth 0) ← **PRIORITY** (shallowest)
- Node 1.2 (0/5, depth 1)
- Node 1.3.2.1 (0/3, depth 3)

Root wins despite higher fill rate. Breadth-first growth creates balanced portfolios.

---

## 3. Not Matching Commits First

**Wrong:** Generate stories without checking if commits should update existing stories.

**Right:** Always run Step 2 (git analysis) before Step 5 (generation).

```bash
git log --since="30 days ago" --pretty=format:"%h|%s" --no-merges
# Match to existing stories
# Update status from in-progress → implemented if match found
```

---

## 4. Uniform Capacity

**Wrong:** Every story gets capacity 5.

**Right:**

| Story Type | Capacity |
|------------|----------|
| Simple UI component | 2-3 |
| Feature with workflow | 5-8 |
| Major feature area | 8-12 |
| Cross-cutting concern | 10-15 |

---

## 5. Skipping Quality Checks

Before output, verify ALL:
- [ ] Clear basis in commits or gap analysis
- [ ] Specific and actionable
- [ ] Testable acceptance criteria
- [ ] No duplicates
- [ ] Complete user story format

If ANY fails, revise before outputting.

---

## 6. Hypothetical vs Real Data

**Rule:** Always work with actual codebase. Don't mix hypothetical stories with real backlog.

---

## 7. Wrong SQL Table Names

**Correct names:**
- `story_nodes` (not `stories`)
- `story_paths` (not `story_tree`)
- `story_commits` (not `story_node_commits`)
- Column: `title` (not `story` or `name`)

Test queries against actual database before using.

---

## 8. Using sqlite3 CLI Command

**Wrong:**
```bash
sqlite3 .claude/data/story-tree.db "SELECT * FROM story_nodes;"
```

**Right:** Use Python's sqlite3 module (sqlite3 CLI is NOT available):
```python
python -c "
import sqlite3
conn = sqlite3.connect('.claude/data/story-tree.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM story_nodes')
print(cursor.fetchall())
conn.close()
"
```

---

## 9. Wrong Script Paths

**Wrong:**
```bash
python scripts/tree-view.py
```

**Right:** Scripts are in the skill directory, not project root:
```bash
python .claude/skills/story-tree/scripts/tree-view.py
```

---

## 10. Trial-and-Error Execution

**Wrong:** Running commands hoping one works, then fixing errors.

**Right:** Read the skill's Environment Requirements section FIRST, then execute with correct approach.

---

## Quick Checklist

Before executing:
- [ ] Read Environment Requirements section
- [ ] Using Python sqlite3 module (NOT sqlite3 CLI)
- [ ] Using full paths to skill scripts

Before outputting stories:
- [ ] Stories are specific with testable criteria
- [ ] Used priority algorithm (shallower first)
- [ ] Matched commits before generating new stories
- [ ] Capacity estimates vary by complexity
- [ ] All quality checks passed
- [ ] Used real git data
- [ ] SQL queries validated
