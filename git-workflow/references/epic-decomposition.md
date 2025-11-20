# Epic Decomposition Workflow

## When to Use `epic` Status

Mark a story as `epic` when:
- Approved by human but too complex for single implementation
- Requires multiple distinct features or phases
- Cannot be estimated confidently as a single unit

## Decomposition Process

1. **Mark parent as `epic`**
   ```sql
   UPDATE story_nodes SET status = 'epic' WHERE id = :story_id;
   ```

2. **Create child stories with `concept` status**
   - Break epic into 2-4 smaller stories
   - Each child must be independently implementable
   - Children start as `concept` - they require their own human approval

3. **Child stories inherit nothing** - Parent approval does NOT cascade:
   - Each child needs separate human review
   - Children may be rejected even if parent was approved
   - This prevents scope creep from approved epics

## Tree Structure

Epics typically appear at mid-levels (depth 2-3). They represent approved scope that needs refinement, not additional work to generate.

**Excluded from generation**: `epic` is excluded from the priority algorithm (Step 3) because:
- Epic nodes already have approved scope
- They need decomposition, not more children at the same level
- Generation targets under-capacity nodes that need new ideas

## `wishlist` Status

Stories marked `wishlist` are:
- Rejected for current development cycle
- Retained for potential future consideration
- Excluded from priority algorithm (like `rejected`)

Use `wishlist` when: "Not now, but maybe later" vs `rejected` for "No, this doesn't fit"
