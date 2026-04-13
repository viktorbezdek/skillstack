# PDF Processing Skill Example

This example demonstrates a skill for PDF manipulation, form filling, and text extraction.

## Skill Structure

- **SKILL.md** - Main skill file with PDF processing instructions
- **LICENSE.txt** - MIT License  
- **forms.md** - Reference doc on PDF form handling
- **reference.md** - Comprehensive PDF processing reference

## Removed Resources (Described Below)

### scripts/ (8 Python scripts)

Python scripts for various PDF operations:

#### check_bounding_boxes.py
Validate PDF element positions and boundaries:
- Extract bounding box coordinates for text, images, forms
- Verify element positioning
- Detect overlapping elements
- Export coordinates to JSON

#### check_bounding_boxes_test.py
Unit tests for bounding box validation:
- Test coordinate extraction
- Validate positioning logic
- Test edge cases (rotated pages, scaled content)

#### check_fillable_fields.py
Inspect PDF form fields:
- List all form fields with types
- Extract field properties (required, read-only, etc.)
- Identify field relationships and dependencies
- Export field metadata

#### convert_pdf_to_images.py
Convert PDF pages to image files:
- Page-by-page conversion
- Configurable DPI and format (PNG, JPEG)
- Batch conversion support
- Quality optimization

#### create_validation_image.py
Generate visual validation overlays:
- Highlight form fields on PDF pages
- Show bounding boxes for verification
- Create comparison images
- Useful for QA and debugging

#### extract_form_field_info.py
Extract detailed form field information:
- Field names, types, values
- Export to JSON/CSV
- Relationship mapping
- JavaScript actions on fields

#### fill_fillable_fields.py
Fill PDF form fields programmatically:
- Map data to field names
- Handle various field types (text, checkbox, radio, dropdown)
- Preserve formatting
- Generate filled PDF

#### fill_pdf_form_with_annotations.py
Fill forms with visual annotations:
- Add form data as overlays
- Highlight filled fields
- Add notes and comments
- Create annotated output

**Common dependencies:**
- PyPDF2 or pypdf for PDF manipulation
- pdf2image for page conversion
- Pillow for image processing
- reportlab for PDF generation

## Use Cases

This skill helps with:
- Extracting text from PDFs
- Filling PDF forms programmatically
- Converting PDFs to images
- Validating PDF structure
- Inspecting form fields
- Batch PDF processing

## Skill Patterns Demonstrated

- **Executable scripts** - Python automation for PDF tasks
- **Testing** - Unit tests for validation logic
- **Reference docs** - Separate files for forms and general reference
- **Multiple approaches** - Different ways to achieve similar results
- **Production-ready** - Error handling and edge cases

## Restoration

To recreate the PDF scripts:
1. Install dependencies: `pip install PyPDF2 pdf2image Pillow reportlab`
2. Create each script in `scripts/` directory
3. Implement with proper error handling
4. Add docstrings and usage examples
5. Create test file with pytest

See SKILL.md for complete implementation details and forms.md/reference.md for in-depth documentation.

