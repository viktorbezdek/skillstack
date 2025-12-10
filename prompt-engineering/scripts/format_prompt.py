#!/usr/bin/env python3
"""
Prompt Formatter

Cleans up and formats prompts into a consistent structure.
Useful for normalizing prompts before comparison or versioning.

Usage: python format_prompt.py <input_file> [--output <file>] [--style xml|markdown|plain]
"""

import argparse
import re
import textwrap


def normalize_whitespace(text: str) -> str:
    """Clean up whitespace issues."""
    # Normalize line endings
    text = text.replace('\r\n', '\n')
    # Remove trailing whitespace per line
    text = '\n'.join(line.rstrip() for line in text.split('\n'))
    # Collapse 3+ blank lines to 2
    text = re.sub(r'\n{3,}', '\n\n', text)
    # Remove leading/trailing whitespace
    text = text.strip()
    return text


def detect_sections(text: str) -> list:
    """Detect logical sections in the prompt."""
    sections = []
    current_section = {'header': None, 'content': []}

    for line in text.split('\n'):
        # Detect markdown headers
        if re.match(r'^#{1,3}\s+', line):
            if current_section['header'] or current_section['content']:
                sections.append(current_section)
            current_section = {'header': line.strip(), 'content': []}
        # Detect label: value headers
        elif re.match(r'^[A-Z][a-zA-Z\s]{2,30}:\s*$', line):
            if current_section['header'] or current_section['content']:
                sections.append(current_section)
            current_section = {'header': line.strip(), 'content': []}
        else:
            current_section['content'].append(line)

    if current_section['header'] or current_section['content']:
        sections.append(current_section)

    return sections


def format_as_markdown(text: str) -> str:
    """Format prompt with clean markdown structure."""
    text = normalize_whitespace(text)
    sections = detect_sections(text)

    if len(sections) <= 1:
        # No sections detected, just clean up
        return text

    output_lines = []
    for section in sections:
        if section['header']:
            # Ensure consistent header format
            header = section['header'].rstrip(':')
            if not header.startswith('#'):
                header = f"## {header}"
            output_lines.append(header)
        content = '\n'.join(section['content']).strip()
        if content:
            output_lines.append(content)
        output_lines.append('')

    return '\n'.join(output_lines).strip()


def format_as_xml(text: str) -> str:
    """Format prompt with XML tag structure (Claude-optimized)."""
    text = normalize_whitespace(text)
    sections = detect_sections(text)

    if len(sections) <= 1:
        return text

    output_lines = []
    for section in sections:
        if section['header']:
            tag = section['header'].lstrip('#').strip().rstrip(':')
            tag = re.sub(r'[^a-zA-Z0-9_]', '_', tag).lower().strip('_')
            content = '\n'.join(section['content']).strip()
            if content:
                output_lines.append(f"<{tag}>")
                output_lines.append(content)
                output_lines.append(f"</{tag}>")
                output_lines.append('')
        else:
            content = '\n'.join(section['content']).strip()
            if content:
                output_lines.append(content)
                output_lines.append('')

    return '\n'.join(output_lines).strip()


def main():
    parser = argparse.ArgumentParser(description='Format and clean up prompts')
    parser.add_argument('input_file', help='Input prompt file')
    parser.add_argument('--output', '-o', help='Output file (default: stdout)')
    parser.add_argument('--style', choices=['xml', 'markdown', 'plain'],
                        default='plain', help='Output format style')
    args = parser.parse_args()

    with open(args.input_file, 'r') as f:
        text = f.read()

    if args.style == 'markdown':
        result = format_as_markdown(text)
    elif args.style == 'xml':
        result = format_as_xml(text)
    else:
        result = normalize_whitespace(text)

    if args.output:
        with open(args.output, 'w') as f:
            f.write(result)
        print(f"Formatted prompt saved to: {args.output}")
    else:
        print(result)


if __name__ == "__main__":
    main()
