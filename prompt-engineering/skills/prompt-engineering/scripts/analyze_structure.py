#!/usr/bin/env python3
"""
Prompt Structure Analyzer

Static analysis of prompt structure and completeness.
This does NOT evaluate prompt quality (that requires LLM judgment).
It checks for the presence of common structural elements.

Usage: python analyze_structure.py <prompt_file> [--json]
"""

import json
import re
import sys
import argparse
from typing import Dict, List


def analyze_prompt(text: str) -> Dict:
    """Analyze structural elements of a prompt."""
    
    lines = text.strip().split('\n')
    words = text.split()
    word_count = len(words)
    line_count = len(lines)
    
    # Detect structural elements
    elements = {
        'has_role': _detect_role(text),
        'has_context': _detect_context(text),
        'has_task': _detect_task(text),
        'has_output_format': _detect_output_format(text),
        'has_examples': _detect_examples(text),
        'has_constraints': _detect_constraints(text),
        'has_sections': _detect_sections(text),
    }
    
    # Compute stats
    present = sum(1 for v in elements.values() if v)
    total = len(elements)
    
    # Detect potential issues
    issues = []
    if word_count < 20:
        issues.append("Very short prompt — likely needs more specificity")
    if word_count > 3000:
        issues.append("Very long prompt — consider trimming or decomposing")
    if not elements['has_role']:
        issues.append("No role/expertise assignment detected")
    if not elements['has_output_format']:
        issues.append("No output format specification detected")
    if not elements['has_examples'] and word_count > 100:
        issues.append("No examples detected — few-shot examples improve consistency")
    
    # Detect vague language
    vague_terms = _detect_vague_language(text)
    if vague_terms:
        issues.append(f"Vague language detected: {', '.join(vague_terms[:5])}")
    
    return {
        'stats': {
            'word_count': word_count,
            'line_count': line_count,
            'char_count': len(text),
        },
        'elements': elements,
        'element_score': f"{present}/{total}",
        'issues': issues,
        'vague_terms': vague_terms,
    }


def _detect_role(text: str) -> bool:
    patterns = [
        r'you are (?:a |an )',
        r'act as (?:a |an )',
        r'as (?:a |an )\w+ (?:expert|specialist|analyst|engineer|consultant)',
        r'role:\s',
        r'persona:\s',
        r'expertise:\s',
    ]
    return any(re.search(p, text, re.IGNORECASE) for p in patterns)


def _detect_context(text: str) -> bool:
    patterns = [
        r'(?:context|background|situation|scenario):\s',
        r'(?:given|assuming|based on)\s(?:that|the)',
    ]
    return any(re.search(p, text, re.IGNORECASE) for p in patterns)


def _detect_task(text: str) -> bool:
    patterns = [
        r'(?:task|objective|goal|mission|assignment):\s',
        r'(?:please |now )?(?:analyze|create|write|generate|design|build|evaluate|review)',
    ]
    return any(re.search(p, text, re.IGNORECASE) for p in patterns)


def _detect_output_format(text: str) -> bool:
    patterns = [
        r'(?:format|output|structure|template):\s',
        r'(?:present|format|structure|organize)\s(?:as|in|using)',
        r'(?:respond|reply|answer)\s(?:in|with|using)',
        r'(?:json|markdown|table|bullet|list|csv|xml)',
    ]
    return any(re.search(p, text, re.IGNORECASE) for p in patterns)


def _detect_examples(text: str) -> bool:
    patterns = [
        r'(?:example|sample|illustration|instance)[s]?\s*[\d:]',
        r'(?:for example|e\.g\.|such as|like this)',
        r'input:.*output:',
        r'before:.*after:',
    ]
    return any(re.search(p, text, re.IGNORECASE | re.DOTALL) for p in patterns)


def _detect_constraints(text: str) -> bool:
    patterns = [
        r'(?:constraint|requirement|limitation|restriction|rule)[s]?:\s',
        r'(?:must|should|shall|need to|required to)',
        r'(?:do not|don\'t|avoid|never|always)',
        r'(?:maximum|minimum|at least|at most|no more than)',
    ]
    return any(re.search(p, text, re.IGNORECASE) for p in patterns)


def _detect_sections(text: str) -> bool:
    """Detect if prompt uses structured sections (headers, numbered items)."""
    header_count = len(re.findall(r'^#{1,3}\s', text, re.MULTILINE))
    numbered_count = len(re.findall(r'^\d+[\.\)]\s', text, re.MULTILINE))
    label_count = len(re.findall(r'^[A-Z][a-zA-Z\s]+:\s', text, re.MULTILINE))
    return (header_count >= 2) or (numbered_count >= 3) or (label_count >= 3)


def _detect_vague_language(text: str) -> List[str]:
    """Find vague terms that reduce prompt effectiveness."""
    vague_patterns = {
        'good': r'\bgood\b',
        'nice': r'\bnice\b',
        'thing(s)': r'\bthings?\b',
        'stuff': r'\bstuff\b',
        'some': r'\bsome\b(?!\w)',
        'various': r'\bvarious\b',
        'appropriate': r'\bappropriate\b',
        'relevant': r'\brelevant\b',
        'proper': r'\bproper\b',
        'suitable': r'\bsuitable\b',
    }
    found = []
    text_lower = text.lower()
    for label, pattern in vague_patterns.items():
        if re.search(pattern, text_lower):
            found.append(label)
    return found


def main():
    parser = argparse.ArgumentParser(description='Analyze prompt structure')
    parser.add_argument('prompt_file', help='Path to file containing the prompt')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    args = parser.parse_args()

    with open(args.prompt_file, 'r') as f:
        text = f.read()

    result = analyze_prompt(text)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"\n{'='*50}")
        print("PROMPT STRUCTURE ANALYSIS")
        print(f"{'='*50}")
        print(f"\nStats: {result['stats']['word_count']} words, {result['stats']['line_count']} lines")
        print(f"Element coverage: {result['element_score']}")
        print(f"\nElements detected:")
        for k, v in result['elements'].items():
            label = k.replace('has_', '').replace('_', ' ').title()
            print(f"  {'✓' if v else '✗'} {label}")
        if result['issues']:
            print(f"\nIssues ({len(result['issues'])}):")
            for issue in result['issues']:
                print(f"  ⚠ {issue}")
        else:
            print("\nNo structural issues detected.")
        print(f"\n{'='*50}\n")
        print("Note: This is static structural analysis only.")
        print("Use LLM-as-judge evaluation for quality assessment.\n")


if __name__ == "__main__":
    main()
