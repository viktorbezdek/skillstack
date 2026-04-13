# Core Principles

Before creating any skill, internalize these principles from Anthropic's latest best practices:

## 1. Concise is Key

**The context window is a public good shared by everyone.**

Default assumption: Claude is already very smart. Only add information Claude doesn't already have.

**Good** (50 tokens):
```markdown
## Extract PDF text

Use pdfplumber for text extraction:
```python
import pdfplumber
with pdfplumber.open("file.pdf") as pdf:
    text = pdf.pages[0].extract_text()
```
```

**Bad** (150 tokens):
```markdown
## Extract PDF text

PDF (Portable Document Format) files are a common file format that contains
text, images, and other content. To extract text from a PDF, you'll need to
use a library. There are many libraries available for PDF processing...
```

**Conciseness Checklist**:
- [ ] Removed common concept definitions (PDF, JSON, API, etc.)
- [ ] Cut hedge words (basically, essentially, typically)
- [ ] Consolidated or removed excessive examples
- [ ] SKILL.md body < 500 lines (use progressive disclosure if larger)
- [ ] Total tokens < 5000 for SKILL.md

## 2. Build Evaluations First

**Create test scenarios BEFORE extensive documentation.**

Follow evaluation-driven development (EDD):
1. **Identify gaps**: Run Claude on tasks WITHOUT the skill
2. **Document struggles**: Note where Claude hesitates, fails, or asks questions
3. **Create 3-5 test scenarios**: Based on concrete examples
4. **Establish baseline**: Measure performance without the skill
5. **Write minimal docs**: Address ONLY identified gaps
6. **Re-test**: Validate improvements
7. **Iterate**: Repeat until scenarios pass consistently

**Why EDD matters**: Building documentation without testing leads to solving non-existent problems and missing actual user needs.

## 3. Match Degrees of Freedom to Task Fragility

**Analogy**: Think of Claude as a robot exploring a path:
- **Narrow bridge with cliffs** (low freedom): One safe way forward
- **Open field** (high freedom): Many paths lead to success
- **Marked trail** (medium freedom): Recommended path, alternatives exist

**High Freedom** (text instructions):
- Multiple valid approaches exist
- Decisions depend on context
- Use: "Consider", "typically", "common approaches"

**Medium Freedom** (scripts with parameters):
- Preferred pattern exists, some variation acceptable
- Use: "Use X with these options", documented parameters

**Low Freedom** (specific scripts, strict sequence):
- Operations are fragile/error-prone
- Consistency is critical
- Use: ⚠️ warnings, "MUST", "In exact order", numbered steps

## 4. Scripts Should Solve, Not Punt

**Scripts must handle errors explicitly rather than punting to Claude.**

**Bad** (punts to Claude):
```python
def process_file(path):
    return open(path).read()  # Let Claude figure out errors
```

**Good** (solves with fallbacks):
```python
def process_file(path):
    """Process file with comprehensive error handling."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"❌ File not found: {path}")
        print("💡 Check the file path is correct")
        return ''  # Sensible default
    except PermissionError:
        print(f"❌ Cannot access: {path}")
        print("💡 Check file permissions")
        return ''
    except UnicodeDecodeError:
        print(f"❌ Encoding error, trying alternative...")
        try:
            with open(path, 'r', encoding='latin-1') as f:
                return f.read()
        except Exception:
            return ''
```

**Script quality checklist**:
- [ ] All exceptions caught explicitly
- [ ] Helpful error messages for users
- [ ] Sensible fallback behavior provided
- [ ] Recovery guidance included
- [ ] No silent failures

## 5. Test with All Target Models

Different Claude models have different needs:
- **Claude Haiku**: Needs enough guidance (smaller model)
- **Claude Sonnet**: Should be clear and efficient (typical target)
- **Claude Opus**: Should avoid over-explaining (most capable)

Test with all three to ensure broad compatibility.

## Navigation

- [Back to main SKILL.md](../SKILL.md)
- [Evaluation-Driven Development](evaluation_driven_development.md)
- [Degrees of Freedom](degrees_of_freedom.md)
