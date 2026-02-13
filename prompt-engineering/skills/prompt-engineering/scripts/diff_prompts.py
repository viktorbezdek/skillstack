#!/usr/bin/env python3
"""
Prompt Version Diff

Compare two prompt versions side by side with structural diff.
Useful for tracking iterations during prompt refinement.

Usage: python diff_prompts.py <prompt_v1> <prompt_v2> [--output <file>]
"""

import argparse
import difflib
import json
import re
from typing import Dict


def compute_stats(text: str) -> Dict:
    """Compute basic stats for a prompt."""
    words = text.split()
    return {
        'words': len(words),
        'lines': len(text.strip().split('\n')),
        'chars': len(text),
        'sections': len(re.findall(r'^#{1,3}\s|^[A-Z][a-zA-Z\s]+:\s', text, re.MULTILINE)),
    }


def compute_diff(text_a: str, text_b: str) -> Dict:
    """Compute structural differences between two prompts."""
    lines_a = text_a.strip().split('\n')
    lines_b = text_b.strip().split('\n')

    # Line-level diff
    differ = difflib.unified_diff(lines_a, lines_b, lineterm='',
                                   fromfile='version_a', tofile='version_b')
    diff_lines = list(differ)

    # Count changes
    added = sum(1 for l in diff_lines if l.startswith('+') and not l.startswith('+++'))
    removed = sum(1 for l in diff_lines if l.startswith('-') and not l.startswith('---'))

    # Similarity ratio
    matcher = difflib.SequenceMatcher(None, text_a, text_b)
    similarity = matcher.ratio()

    stats_a = compute_stats(text_a)
    stats_b = compute_stats(text_b)

    return {
        'similarity': round(similarity, 3),
        'lines_added': added,
        'lines_removed': removed,
        'stats_a': stats_a,
        'stats_b': stats_b,
        'word_delta': stats_b['words'] - stats_a['words'],
        'diff': '\n'.join(diff_lines),
    }


def main():
    parser = argparse.ArgumentParser(description='Compare two prompt versions')
    parser.add_argument('prompt_a', help='First prompt file (baseline)')
    parser.add_argument('prompt_b', help='Second prompt file (revision)')
    parser.add_argument('--output', '-o', help='Save JSON report to file')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    args = parser.parse_args()

    with open(args.prompt_a, 'r') as f:
        text_a = f.read()
    with open(args.prompt_b, 'r') as f:
        text_b = f.read()

    result = compute_diff(text_a, text_b)

    if args.json or args.output:
        report = json.dumps(result, indent=2)
        if args.output:
            with open(args.output, 'w') as f:
                f.write(report)
            print(f"Report saved to: {args.output}")
        else:
            print(report)
    else:
        print(f"\n{'='*50}")
        print("PROMPT VERSION COMPARISON")
        print(f"{'='*50}")
        print(f"\nSimilarity: {result['similarity']*100:.1f}%")
        print(f"Lines added: +{result['lines_added']}")
        print(f"Lines removed: -{result['lines_removed']}")
        print(f"Word delta: {result['word_delta']:+d} ({result['stats_a']['words']} → {result['stats_b']['words']})")
        print(f"\n--- Diff ---")
        if result['diff']:
            print(result['diff'])
        else:
            print("(no differences)")
        print(f"\n{'='*50}\n")


if __name__ == "__main__":
    main()
