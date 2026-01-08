# Example: Creating a Skill for `jq` JSON Processor

This example demonstrates the complete workflow for creating a skill from documentation.

## Phase 1: Documentation Gathering

**Tool:** jq - Command-line JSON processor

**Documentation Source:** https://jqlang.github.io/jq/manual/

**Extraction method:**
```bash
# Extract main manual page
crwl https://jqlang.github.io/jq/manual/ -o markdown > jq_manual.md

# Extract tutorial
crwl https://jqlang.github.io/jq/tutorial/ -o markdown > jq_tutorial.md

# Combine
cat jq_manual.md jq_tutorial.md > jq_docs.md
```

## Phase 2: Documentation Analysis

### 1. Tool Overview

**Primary purpose:** Process, filter, and transform JSON data from command line

**Key capabilities:**
- Filter JSON by keys/values
- Transform data structure
- Combine multiple JSON files
- Validate JSON format
- Format and pretty-print

**Use cases:**
- API response processing
- Log file analysis
- Configuration file manipulation
- Data extraction from JSON
- JSON validation

**Target audience:** Developers, DevOps engineers, data analysts

### 2. Command/API Patterns

**Command structure:** `jq [OPTIONS] 'FILTER' [FILES...]`

**Common patterns:**
```bash
# Basic selection
jq '.key'
jq '.key.nested'
jq '.array[0]'

# Array operations
jq '.[] | .name'          # Iterate and extract
jq 'map(.name)'           # Map transformation
jq 'select(.age > 30)'    # Filter

# Pipe combinations
jq '.items[] | select(.active) | .name'
```

**Common flags:**
- `-r` / `--raw-output` - Output raw text (not JSON-quoted)
- `-c` / `--compact-output` - Compact instead of pretty-printed
- `-s` / `--slurp` - Read entire input into array
- `-n` / `--null-input` - Don't read input, use null
- `-e` / `--exit-status` - Set exit code based on output

### 3. Workflows

**Workflow 1: Extract specific fields from JSON**

Prerequisites: Valid JSON input

Steps:
1. Identify target field path (e.g., `.users[].email`)
2. Run `jq '.users[].email' data.json`
3. Optionally use `-r` for raw output (no quotes)

Expected output: List of email addresses

**Workflow 2: Transform JSON structure**

Prerequisites: Understanding input and desired output structure

Steps:
1. Design transformation filter
2. Test with sample data
3. Apply to full dataset
4. Validate output structure

Example:
```bash
# Input: [{"name": "John", "age": 30}]
# Desired: [{"user": "John", "years": 30}]
jq 'map({user: .name, years: .age})' input.json
```

**Workflow 3: Combine multiple JSON files**

Prerequisites: JSON files to merge

Steps:
1. Use `-s` to slurp files into array
2. Combine with appropriate filter
3. Output merged result

Example:
```bash
jq -s 'add' file1.json file2.json file3.json > merged.json
```

### 4. Pitfalls & Gotchas

**Pitfall 1: Quoted strings in output**

Description: Output has extra quotes around strings
Cause: Default jq output is JSON-formatted
Detection: Strings appear as `"value"` instead of `value`
Prevention: Use `-r` flag for raw text output
Solution: Re-run with `jq -r 'filter' input.json`

**Pitfall 2: Empty output on valid filter**

Description: Filter returns nothing but should match
Cause: Incorrect key path or array iteration
Detection: No output or `null` when data exists
Prevention: Test filter step-by-step from root
Solution:
1. Start with `.` to see full structure
2. Add one key at a time (`.key`, `.key.nested`)
3. For arrays, use `.[]` to iterate
4. Verify each step produces expected output

**Pitfall 3: Invalid JSON input**

Description: `parse error` message
Cause: Input is not valid JSON
Detection: Error message indicates line/column
Prevention: Validate JSON before processing
Solution:
1. Run through JSON validator (or `jq .` with no filter)
2. Fix syntax errors
3. Retry

**Pitfall 4: Confusing null vs empty**

Description: Unexpected `null` values
Cause: Referenced keys don't exist
Detection: Output contains `null`
Prevention: Use `select()` to filter, or `// default` for fallback
Solution: `jq '.key // "default"'` or `jq 'select(.key != null)'`

**Pitfall 5: Exit code confusion**

Description: Script continues even though jq found no matches
Cause: Default jq exit code is 0 even with no output
Detection: No output but script proceeds
Prevention: Use `-e` flag to exit 1 on empty/false/null
Solution: `jq -e 'filter' || echo "No matches found"`

### 5. Best Practices

**Filter Construction:**
- Start simple, build complexity incrementally
- Test each step with sample data
- Use pipe `|` to chain operations clearly
- Comment complex filters

**Performance:**
- For large files, filter early in pipeline
- Use `select()` before `map()` when possible
- Avoid unnecessary array iteration

**Error Handling:**
- Use `-e` for script error checking
- Validate JSON before complex transformations
- Handle missing keys with `// default`

**Maintainability:**
- Save complex filters in files
- Use variables (`jq --arg`) for reusable values
- Document filter purpose and assumptions

### 6. Configuration Patterns

jq doesn't use traditional config files, but common patterns:

**Filter files:**
```bash
# Save filter to file
echo '.items[] | select(.active) | .name' > filter.jq

# Use with -f flag
jq -f filter.jq data.json
```

**Variable injection:**
```bash
# Pass variables
jq --arg name "John" '.users[] | select(.name == $name)' data.json
```

### 7. Key Examples

**Extract all email addresses:**
```bash
jq -r '.users[].email' users.json
```

**Filter and transform:**
```bash
jq 'map(select(.age > 30) | {name, email})' users.json
```

**Merge objects:**
```bash
jq -s 'add' file1.json file2.json
```

**Pretty-print:**
```bash
cat compact.json | jq .
```

**Validate JSON:**
```bash
jq . input.json || echo "Invalid JSON"
```

## Phase 3: Skill Design Brainstorming

### Helper Scripts

**1. validate_json.sh**
- Purpose: Validate JSON files before processing
- Inputs: File path(s)
- Outputs: Validation report
- Prevents: Parse errors from invalid JSON

Logic:
1. For each file
2. Run `jq . "$file" > /dev/null`
3. Report pass/fail
4. Exit with status code

**2. test_filter.sh**
- Purpose: Test jq filter on sample data
- Inputs: Filter string, sample JSON
- Outputs: Filter result or error
- Prevents: Running complex filter on large data without testing

Logic:
1. Accept filter and sample data
2. Run jq with filter
3. Show result with colors
4. Suggest next steps if null/empty

**3. generate_filter.py**
- Purpose: Interactive filter builder
- Inputs: User prompts for desired extraction
- Outputs: Generated jq filter
- Prevents: Syntax errors in complex filters

Logic:
1. Ask about input structure
2. Ask about desired output
3. Generate filter
4. Test with sample
5. Output working filter

### Config Templates

**1. common_filters.txt**
```
# Common jq filters for reference

# Extract all values of a key
.[] | .key

# Filter by condition
.[] | select(.age > 30)

# Map to new structure
map({name: .name, id: .id})

# Get unique values
[.[] | .category] | unique

# Count items
.[] | length

# Combine arrays
add

# Default for missing keys
.key // "default"
```

**2. filter_template.jq**
```
# Filter: [Description]
# Input: [Expected structure]
# Output: [Resulting structure]

# Main filter
. |
  # Step 1: [Description]
  PLACEHOLDER |
  # Step 2: [Description]
  PLACEHOLDER
```

### Guardrails

**Guardrail 1: Validate JSON First**

Type: Prerequisite check
Purpose: Prevent parse errors
Implementation: Mandatory workflow in SKILL.md

Workflow:
1. Validate JSON: `jq . input.json` (or validation script)
2. If valid, proceed with filter
3. If invalid, fix and retry

Error message: "❌ Invalid JSON. Fix syntax before applying filter."

**Guardrail 2: Test Filter on Sample**

Type: Validation gate
Purpose: Prevent running wrong filter on large datasets
Implementation: Recommended workflow

Workflow:
1. Create sample.json with representative data
2. Test filter: `jq 'filter' sample.json`
3. Verify output is correct
4. Apply to full dataset

**Guardrail 3: Use -e for Scripts**

Type: Best practice reminder
Purpose: Proper error handling in automation
Implementation: Tip section + examples

Pattern:
```bash
# In scripts, use -e to exit on empty
if jq -e '.items[] | select(.active)' data.json > results.json; then
  echo "Found active items"
else
  echo "No active items found"
fi
```

### Checklists

**First-Time Setup:**
- [ ] jq is installed (`which jq`)
- [ ] Version is recent (`jq --version`)
- [ ] Basic filter works (`echo '{}' | jq .`)
- [ ] Tested with sample JSON

**Before Processing:**
- [ ] JSON is validated
- [ ] Filter tested on sample
- [ ] Output format is correct (raw vs JSON)
- [ ] Exit status handling configured (if scripting)

**Troubleshooting:**
- [ ] Is input valid JSON? (run `jq .`)
- [ ] Is filter syntax correct? (test incrementally)
- [ ] Are keys spelled correctly? (check with `.`)
- [ ] For arrays, using `.[]` to iterate?
- [ ] Need `-r` for raw output?
- [ ] Need `-e` for error detection?

### Reference Structure

**SKILL.md sections:**
- Prerequisites (installation check)
- Quick start (basic examples)
- Core tasks (common operations)
- Command reference (flags)
- Proven patterns (complete workflows)
- Troubleshooting (quick fixes)
- Helper scripts
- Workflow requirements
- Tips

**references/ files:**

**cli-reference.md:**
- All flags documented
- Filter syntax reference
- Built-in functions
- Operators

**patterns.md:**
- Data extraction patterns
- Transformation patterns
- Filtering patterns
- Aggregation patterns

**troubleshooting.md:**
- Parse errors
- Empty output
- Null handling
- Performance issues

## Phase 4: Artifact Creation

### Directory Structure

```
~/.claude/skills/jq/
├── SKILL.md
├── references/
│   ├── cli-reference.md
│   ├── patterns.md
│   └── troubleshooting.md
├── scripts/
│   ├── validate_json.sh
│   ├── test_filter.sh
│   ├── generate_filter.py
│   └── README.md
└── templates/
    ├── common_filters.txt
    └── filter_template.jq
```

### Generated Artifacts

**validate_json.sh:**
```bash
#!/usr/bin/env bash
set -euo pipefail

# validate_json.sh - Validate JSON files

GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

if [ $# -eq 0 ]; then
    echo "Usage: $0 FILE [FILE...]"
    exit 1
fi

exit_code=0

for file in "$@"; do
    if [ ! -f "$file" ]; then
        echo -e "${RED}❌ File not found: $file${NC}"
        exit_code=1
        continue
    fi

    if jq . "$file" > /dev/null 2>&1; then
        echo -e "${GREEN}✅ Valid JSON: $file${NC}"
    else
        echo -e "${RED}❌ Invalid JSON: $file${NC}"
        exit_code=1
    fi
done

exit $exit_code
```

**test_filter.sh:**
```bash
#!/usr/bin/env bash
# test_filter.sh - Test jq filter on sample data

if [ $# -ne 2 ]; then
    echo "Usage: $0 'FILTER' SAMPLE_JSON"
    echo "Example: $0 '.users[].name' sample.json"
    exit 1
fi

filter="$1"
sample="$2"

echo "Testing filter: $filter"
echo "On file: $sample"
echo "---"

if jq "$filter" "$sample"; then
    echo "---"
    echo "✅ Filter succeeded"
else
    echo "---"
    echo "❌ Filter failed"
    echo "💡 Try simplifying the filter step by step"
    exit 1
fi
```

**(Additional scripts would be created similarly)**

## Phase 5: SKILL.md Creation

```yaml
---
name: jq
description: Process, filter, and transform JSON data from command line using jq. Handles JSON validation, field extraction, data transformation, and formatting. USE WHEN user says 'process JSON', 'parse JSON', 'filter JSON', 'transform JSON', 'jq command', or needs JSON manipulation. Keywords - jq, JSON, filter, transform, parse, query.
---

# jq - JSON Processor Guide

Process, filter, and transform JSON data from the command line with powerful filtering and transformation capabilities.

## Quick Start

```bash
# Pretty-print JSON
jq . input.json

# Extract field
jq '.name' data.json

# Extract from array
jq '.[0].email' users.json

# Filter and extract
jq '.[] | select(.active) | .name' items.json
```

## Core Tasks

### Validate JSON

```bash
# Check if file is valid JSON
jq . input.json

# With validation script
./scripts/validate_json.sh input.json
```

### Extract Fields

```bash
# Single field
jq '.fieldName' data.json

# Nested field
jq '.user.email' data.json

# Array element
jq '.items[0]' data.json

# All array values
jq '.items[].name' data.json
```

...
```

*(Complete SKILL.md would follow the template)*

## Phase 6: Integration & Testing

### Added to KAI.md

```xml
<skill>
<name>jq</name>
<description>Process, filter, and transform JSON data from command line using jq. Handles JSON validation, field extraction, data transformation, and formatting. USE WHEN user says 'process JSON', 'parse JSON', 'filter JSON', 'transform JSON', 'jq command', or needs JSON manipulation. Keywords - jq, JSON, filter, transform, parse, query.</description>
<location>user</location>
</skill>
```

### Test Results

**Activation test:** ✅ Skill activates with "process JSON" and "use jq"

**Helper scripts:** ✅ All scripts work correctly
- validate_json.sh: Correctly identifies valid/invalid JSON
- test_filter.sh: Tests filters and provides helpful output

**Templates:** ✅ Common filters reference is accurate

**Workflows:** ✅ Proven patterns execute successfully

**File references:** ✅ All links resolve correctly

### Iteration Notes

**Improvements made:**
1. Added more examples for array operations (frequently needed)
2. Expanded troubleshooting for "empty output" (common issue)
3. Created quick reference card for common filters
4. Added tip about `-e` flag for scripting

## Conclusion

This example demonstrates the complete process from documentation to production-ready skill. The resulting jq skill:
- Prevents common mistakes (JSON validation, filter testing)
- Automates error-prone tasks (validation script)
- Provides quick references (common filters template)
- Includes comprehensive examples
- Documents proven workflows

Users can now use jq effectively without memorizing syntax or making common mistakes.
