# PPTX (PowerPoint) Processing Skill Example

This example demonstrates a skill for Microsoft PowerPoint presentation manipulation using Python and OOXML standards.

## Skill Structure

- **SKILL.md** - Main skill file with PPTX processing instructions
- **LICENSE.txt** - MIT License
- **html2pptx.md** - Reference for HTML to PowerPoint conversion
- **ooxml.md** - OOXML format specifications (same as DOCX)

## Removed Resources (Described Below)

### ooxml/ (Shared OOXML Schema Files - 47 files)

Same complete OOXML schemas as DOCX skill (PresentationML uses same base standards).  
See docx/README.md for full schema file listing.

Key schemas for PPTX:
- pml.xsd - PresentationML main schema
- dml-*.xsd - DrawingML for slides and graphics (8 files)
- shared-*.xsd - Common components (14 files)

### scripts/ (Presentation Processing Scripts - 5 files)

Python scripts for PowerPoint operations:

#### html2pptx.js
JavaScript implementation for HTML to PPTX conversion:
- Parse HTML structure
- Convert to slide layout
- Map CSS styles to PowerPoint formatting
- Handle images and media
- Generate .pptx output

**Use case:** Convert web content or Markdown to presentations

#### inventory.py
Analyze presentation structure:
- List all slides with titles
- Extract slide layouts and masters
- Inventory media files (images, videos)
- Report on fonts and styles used
- Export structure to JSON

#### rearrange.py
Reorder and reorganize slides:
- Move slides by index
- Duplicate slides
- Delete slides by criteria
- Reorder based on rules
- Batch operations

#### replace.py
Find and replace content in presentations:
- Text replacement across all slides
- Image substitution
- Update placeholders
- Replace formatting
- Bulk updates

#### thumbnail.py
Generate slide thumbnails:
- Export slides as images
- Configurable size and quality
- Batch thumbnail generation
- Preview generation for web

## Use Cases

This skill helps with:
- Creating PowerPoint presentations programmatically
- Converting HTML/Markdown to slides
- Analyzing presentation structure
- Batch slide operations
- Generating thumbnails
- Content replacement across slides

## Skill Patterns Demonstrated

- **Multi-language** - Both Python and JavaScript implementations
- **Schema validation** - Same OOXML standards as Word
- **Batch operations** - Scripts for bulk slide processing
- **Conversion tools** - HTML to PPTX transformation
- **Analysis tools** - Inventory and structure examination

## Restoration

To recreate the PPTX resources:
1. Reuse OOXML schemas from DOCX (same standards)
2. Create html2pptx.js for HTML conversion
3. Implement inventory.py, rearrange.py, replace.py, thumbnail.py
4. Test with: `python scripts/inventory.py presentation.pptx`
5. Node.js for html2pptx.js: `node scripts/html2pptx.js input.html output.pptx`

**Dependencies:**
- python-pptx for Python scripts
- Node.js + xmlbuilder for html2pptx.js

See SKILL.md for complete implementation and html2pptx.md for conversion details.

