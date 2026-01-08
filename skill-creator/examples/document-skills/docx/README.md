# DOCX (Word) Processing Skill Example

This example demonstrates a skill for Microsoft Word document manipulation using Python and OOXML standards.

## Skill Structure

- **SKILL.md** - Main skill file with DOCX processing instructions
- **LICENSE.txt** - MIT License
- **docx-js.md** - Reference for JavaScript-based DOCX manipulation
- **ooxml.md** - OOXML format specifications and structure

## Removed Resources (Described Below)

### ooxml/ (OOXML Schema Files)

Complete Office Open XML schema definitions for document validation and structure understanding:

#### ooxml/schemas/
Organized XML Schema Definition (XSD) files:

**ECMA Standards (Fourth Edition):**
- opc-contentTypes.xsd - Content type definitions
- opc-coreProperties.xsd - Document properties
- opc-digSig.xsd - Digital signatures  
- opc-relationships.xsd - Part relationships

**ISO/IEC 29500-4:2016 (Main Standard - 32 files):**
- wml.xsd - WordprocessingML main schema
- dml-main.xsd - DrawingML graphics
- shared-*.xsd - Shared components (14 files)
- vml-*.xsd - Vector Markup Language (5 files)
- pml.xsd, sml.xsd - PresentationML, SpreadsheetML
- xml.xsd - XML namespace definitions

**Markup Compatibility:**
- mce/mc.xsd - Markup compatibility and extensibility

**Microsoft Extensions (4 files):**
- wml-2010.xsd, wml-2012.xsd, wml-2018.xsd
- wml-cex-2018.xsd, wml-cid-2016.xsd
- wml-sdtdatahash-2020.xsd, wml-symex-2015.xsd

**Total:** 47 XSD files defining complete OOXML structure

#### ooxml/scripts/
Python scripts for OOXML package operations:

**pack.py** - Package OOXML parts into .docx zip:
- Assembles XML files into proper structure
- Creates [Content_Types].xml
- Generates relationships
- Validates structure

**unpack.py** - Extract .docx to OOXML parts:
- Unzips .docx file
- Organizes parts by type
- Extracts relationships
- Preserves folder structure

**validate.py** - Validate OOXML against schemas:
- XSD validation for all parts
- Relationship validation
- Content type verification
- Error reporting

**validation/ module (4 Python files):**
- __init__.py - Module initialization
- base.py - Base validation logic
- docx.py - Word-specific validation
- pptx.py - PowerPoint validation (cross-reference)
- redlining.py - Track changes validation

### scripts/ (Document Processing Scripts)

Python modules and templates for document operations:

#### document.py
Core document manipulation module:
- Create new documents
- Read existing documents
- Modify styles and formatting
- Add/remove paragraphs, tables, images
- Save and export

#### utilities.py
Helper functions for document processing:
- Text extraction
- Style management
- Table operations
- Image handling
- Format conversion

#### templates/ (XML Templates - 5 files)
Pre-built XML structures for document features:

**comments.xml** - Comment structure template  
**commentsExtended.xml** - Extended comment metadata  
**commentsExtensible.xml** - Extensible comment format  
**commentsIds.xml** - Comment ID mapping  
**people.xml** - People/author definitions for comments

## Use Cases

This skill helps with:
- Creating Word documents programmatically
- Parsing existing .docx files
- Manipulating document structure
- Validating OOXML compliance
- Extracting text and metadata
- Adding comments and tracking changes

## Skill Patterns Demonstrated

- **Schema definitions** - Complete OOXML XSD files
- **Validation tools** - Scripts to verify document structure
- **Processing modules** - Reusable Python code
- **XML templates** - Pre-built structures for features
- **Reference docs** - Separate docs for different approaches (Python vs JS)

## Restoration

To recreate the DOCX resources:
1. Download OOXML schemas from ISO/IEC 29500 standard
2. Organize in `ooxml/schemas/` by standard
3. Create pack/unpack/validate scripts in `ooxml/scripts/`
4. Implement document.py and utilities.py modules
5. Create XML templates for common features
6. Test with: `python scripts/document.py create example.docx`

**Schema source:** https://www.ecma-international.org/publications-and-standards/standards/ecma-376/

See SKILL.md for complete implementation and ooxml.md for format specifications.

