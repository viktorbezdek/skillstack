# XLSX (Excel) Processing Skill Example

This example demonstrates a skill for Microsoft Excel spreadsheet manipulation with formula calculation support.

## Skill Structure

- **SKILL.md** - Main skill file with XLSX processing instructions
- **LICENSE.txt** - MIT License

## Removed Resources (Described Below)

### recalc.py

Python script for Excel formula recalculation:

**Purpose:** Recalculate all formulas in an Excel workbook after data changes

**Features:**
- Parse XLSX file structure
- Extract all formulas from cells
- Evaluate formulas using Python
- Handle Excel function library (SUM, AVERAGE, VLOOKUP, IF, etc.)
- Update calculated values
- Preserve formatting and styles
- Save updated workbook

**Common Excel functions supported:**
- Mathematical: SUM, AVERAGE, MIN, MAX, ROUND, ABS
- Logical: IF, AND, OR, NOT
- Lookup: VLOOKUP, HLOOKUP, INDEX, MATCH
- Text: CONCATENATE, LEFT, RIGHT, MID, LEN, UPPER, LOWER
- Date: TODAY, NOW, DATE, YEAR, MONTH, DAY
- Statistical: COUNT, COUNTA, COUNTIF, STDEV

**Usage:**
```python
python recalc.py input.xlsx output.xlsx
```

**Key challenges:**
- Circular reference detection
- Dependency graph construction
- Excel function compatibility
- Date/time format handling
- Error propagation (#DIV/0!, #REF!, #N/A)

## Use Cases

This skill helps with:
- Recalculating Excel formulas programmatically
- Updating spreadsheets with new data
- Batch processing Excel files
- Formula validation and testing
- Converting Excel calculations to Python
- Automating spreadsheet workflows

## Skill Patterns Demonstrated

- **Single-purpose script** - Focused on one important task
- **Formula engine** - Implements Excel calculation logic
- **File processing** - Read, modify, save XLSX files
- **Error handling** - Manages Excel error states
- **Minimal dependencies** - Simple, focused implementation

## Restoration

To recreate the XLSX script:
1. Install openpyxl: `pip install openpyxl`
2. Create `recalc.py` with:
   - XLSX file parser
   - Formula evaluator
   - Dependency resolver
   - Excel function library
   - Error handling
3. Test with sample spreadsheet containing formulas
4. Handle edge cases (circular refs, errors, dates)

**Dependencies:**
- openpyxl for XLSX file manipulation
- Optional: xlrd for older .xls format

See SKILL.md for complete implementation and formula handling details.

