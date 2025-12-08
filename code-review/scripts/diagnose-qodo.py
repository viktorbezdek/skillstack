#!/usr/bin/env python3
"""
Diagnostic script to debug why Qodo comments aren't reaching Claude.

Usage:
    python diagnose-qodo.py <pr-comments-file.json>

This will:
1. Count Qodo comments in raw data
2. Show how each Qodo comment is classified
3. Identify which Qodo comments survive filtering
4. Report statistics by classification type
"""

import json
import sys
from pathlib import Path

# Import from existing filter
sys.path.insert(0, str(Path(__file__).parent))
from pr_comment_filter import classify_comment, extract_suggestions, extract_priority


def diagnose_qodo_comments(comments_file):
    """Analyze how Qodo comments are processed."""

    # Load comments
    with open(comments_file, 'r') as f:
        comments = json.load(f)

    # Find all Qodo comments (support multiple variants)
    qodo_users = ['qodo-merge', 'qodo-merge-pro[bot]', 'qodo[bot]']
    qodo_comments = [c for c in comments if any(qodo in c.get('user', '') for qodo in qodo_users)]

    print(f"\n{'='*80}")
    print(f"QODO COMMENT DIAGNOSTIC")
    print(f"{'='*80}\n")

    print(f"Total comments: {len(comments)}")
    print(f"Qodo comments found: {len(qodo_comments)}")

    if not qodo_comments:
        print("\n❌ NO QODO COMMENTS FOUND")
        print("\nBot users in this PR:")
        bot_users = set(c.get('user', '') for c in comments if c.get('user', '').endswith('[bot]'))
        for user in sorted(bot_users):
            print(f"  - {user}")
        return

    print(f"\n{'='*80}")
    print(f"QODO COMMENT BREAKDOWN")
    print(f"{'='*80}\n")

    # Analyze each Qodo comment
    classifications = {'keep_full': [], 'extract': [], 'discard': []}

    for i, comment in enumerate(qodo_comments, 1):
        print(f"\n--- Qodo Comment #{i} ---")
        print(f"User: {comment.get('user')}")
        print(f"Type: {comment.get('comment_type')}")
        print(f"Has path: {comment.get('path') is not None}")
        print(f"Body length: {len(comment.get('body', ''))} chars")

        # Classify
        classification = classify_comment(comment)
        classifications[classification].append(comment)
        print(f"Classification: {classification}")

        # Check for actionable markers
        body = comment.get('body', '')
        actionable_markers = [
            '📝 Committable suggestion',
            'PR Code Suggestions',
            'Suggestion importance',
            '- [ ]',
        ]
        found_markers = [m for m in actionable_markers if m in body]
        if found_markers:
            print(f"Actionable markers found: {found_markers}")

        # Check for summary markers
        summary_markers = [
            '<!-- This is an auto-generated comment: summarize',
            '## Walkthrough',
            '<!-- walkthrough_start -->',
            'PR Compliance Guide',
        ]
        found_summary = [m for m in summary_markers if m in body]
        if found_summary:
            print(f"Summary markers found: {found_summary}")

        # If extract, show what would be extracted
        if classification == 'extract':
            suggestions = extract_suggestions(body)
            print(f"Suggestions extracted: {len(suggestions)}")
            for j, sug in enumerate(suggestions[:3], 1):
                print(f"  {j}. {sug.get('title')} (priority: {sug.get('importance')})")

        # Show priority if present
        priority = extract_priority(body)
        if priority != 5:  # 5 is default
            print(f"Extracted priority: {priority}")

        # Show snippet of body
        snippet = body[:200].replace('\n', ' ')
        print(f"Body snippet: {snippet}...")

    # Summary statistics
    print(f"\n{'='*80}")
    print(f"CLASSIFICATION SUMMARY")
    print(f"{'='*80}\n")

    for classification, items in classifications.items():
        print(f"{classification}: {len(items)} comments")
        if items:
            for comment in items:
                user = comment.get('user', 'unknown')
                ctype = comment.get('comment_type', 'unknown')
                print(f"  - {user} ({ctype})")

    # Check filter survival rate
    print(f"\n{'='*80}")
    print(f"FILTER SURVIVAL ANALYSIS")
    print(f"{'='*80}\n")

    kept_full = len(classifications['keep_full'])
    extracted = len(classifications['extract'])
    discarded = len(classifications['discard'])

    print(f"Will survive filtering: {kept_full + extracted} / {len(qodo_comments)}")
    print(f"  - Kept full: {kept_full}")
    print(f"  - Extracted (may be truncated): {extracted}")
    print(f"  - Discarded: {discarded}")

    if discarded > 0:
        print(f"\n⚠️  WARNING: {discarded} Qodo comments will be DISCARDED")
        print("These comments likely contain summary/walkthrough markers")
        print("Consider adjusting SUMMARY_MARKERS if these contain actionable content")

    if extracted > 0:
        print(f"\n✅ {extracted} Qodo comments will have suggestions extracted")
        print("Note: Only suggestions with importance >= 7 are kept")
        print("Lower priority suggestions will be filtered out")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python diagnose-qodo.py <pr-comments-file.json>")
        sys.exit(1)

    comments_file = sys.argv[1]
    if not Path(comments_file).exists():
        print(f"Error: File not found: {comments_file}")
        sys.exit(1)

    diagnose_qodo_comments(comments_file)
