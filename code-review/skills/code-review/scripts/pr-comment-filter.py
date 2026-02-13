#!/usr/bin/env python3
"""
PR Comment Filter - Extract actionable feedback from verbose bot comments

Takes pr-comment-grabber.py output and filters verbose bot content.

Usage:
    python pr-comment-filter.py INPUT_FILE [--output OUTPUT_FILE] [--in-place] [--max-tokens N]
"""

import json
import re
import sys
import os
import argparse
from typing import List, Dict, Any, Tuple
from bs4 import BeautifulSoup


# Configuration constants
MAX_TOKENS = 15000
TOKEN_PER_CHAR = 0.40  # JSON has lower token density than plain text (0.40 vs 0.75)
MAX_CODE_LENGTH = 500
MIN_COMMENT_TOKENS = 300  # Minimum meaningful comment size

# Pattern markers
SUMMARY_MARKERS = [
    '<!-- This is an auto-generated comment: summarize',
    '## Walkthrough',
    '<!-- walkthrough_start -->',
    'PR Compliance Guide',
]

ACTIONABLE_MARKERS = [
    '📝 Committable suggestion',
    'PR Code Suggestions',
    'Suggestion importance',
    '- [ ]',  # Task checkbox
]


def classify_comment(comment: dict) -> str:
    """
    Classify comment as 'keep_full', 'extract', or 'discard'.

    Args:
        comment: Comment dictionary with user, comment_type, body, path fields

    Returns:
        'keep_full' - Human comment or inline review (preserve completely)
        'extract' - Bot suggestion with actionable content (extract suggestions)
        'discard' - Bot summary/walkthrough (reduce to minimal metadata)
    """
    user = comment.get('user', '')
    comment_type = comment.get('comment_type')
    body = comment.get('body', '')
    path = comment.get('path')

    # Rule 1: Keep all human comments
    if not user.endswith('[bot]'):
        return 'keep_full'

    # Rule 2: Keep inline review comments (have file path)
    if comment_type == 'review' and path:
        return 'keep_full'

    # Rule 3: Extract actionable content (CHECK FIRST - higher priority)
    if any(marker in body for marker in ACTIONABLE_MARKERS):
        return 'extract'

    # Rule 4: Discard bot summaries (MOVED DOWN)
    if any(marker in body for marker in SUMMARY_MARKERS):
        return 'discard'

    # Rule 5: Keep small comments as-is
    if len(body) < 1000:
        return 'keep_full'

    # Default: extract from large bot comments
    return 'extract'


def extract_priority(text: str) -> int:
    """
    Extract importance rating from bot comment.

    Supports:
        - Qodo: "importance[1-10]: 9" → 9
        - CodeRabbit: "_🔴 Critical_" → 10, "_🟡 Minor_" → 5

    Args:
        text: Text containing priority/importance markers

    Returns:
        Priority rating from 1-10 (default: 5)
    """
    # Qodo format: importance[1-10]: N
    match = re.search(r'importance\[1-10\]:\s*(\d+)', text)
    if match:
        return int(match.group(1))

    # CodeRabbit format: emoji-based severity
    if '🔴' in text or 'Critical' in text:
        return 10
    if '🟠' in text or 'High' in text:
        return 8
    if '🟡' in text or 'Minor' in text:
        return 5
    if '🟢' in text or 'Low' in text:
        return 3

    # Default to medium priority
    return 5


def extract_suggestions(body: str) -> list:
    """
    Extract code suggestions from bot comments.

    Parses HTML <details> blocks and <table> elements using BeautifulSoup.
    Only includes suggestions with importance >= 7.
    Truncates code content to 500 characters.

    Args:
        body: Comment body containing HTML and markdown

    Returns:
        List of dicts with:
            - title: Suggestion summary
            - content or code: Code block (truncated to 500 chars)
            - importance: Priority rating (1-10)
    """
    suggestions = []
    soup = BeautifulSoup(body, 'html.parser')

    # Method 1: Extract from <details> blocks
    for details in soup.find_all('details'):
        summary = details.find('summary')
        if not summary:
            continue

        title = summary.get_text(strip=True)

        # Get full text content
        details_text = details.get_text()

        # Extract importance rating
        importance = extract_priority(details_text)

        # Only include high priority suggestions (>= 7)
        if importance < 7:
            continue

        # Extract code blocks
        code_blocks = details.find_all(['code', 'pre'])
        code_content = '\n'.join(block.get_text() for block in code_blocks)

        # If no code blocks, look for text content
        if not code_content:
            # Get text but skip the summary
            code_content = details_text.replace(title, '', 1)

        # Truncate to max length
        if len(code_content) > MAX_CODE_LENGTH:
            code_content = code_content[:MAX_CODE_LENGTH]

        suggestions.append({
            'title': title,
            'content': code_content.strip(),
            'importance': importance
        })

    # Method 2: Extract from ```suggestion blocks
    suggestion_blocks = re.findall(
        r'```suggestion\n(.*?)\n```',
        body,
        re.DOTALL
    )
    for i, block in enumerate(suggestion_blocks):
        # Check if this wasn't already captured in details
        block_preview = block[:50]
        if not any(block_preview in s.get('content', '') or block_preview in s.get('code', '') for s in suggestions):
            code = block[:MAX_CODE_LENGTH] if len(block) > MAX_CODE_LENGTH else block
            suggestions.append({
                'title': f'Code suggestion {len(suggestions) + 1}',
                'code': code,
                'importance': 8  # Assume high priority for explicit suggestions
            })

    # Sort by importance (highest first)
    suggestions.sort(key=lambda s: s['importance'], reverse=True)

    return suggestions


def extract_task_items(body: str) -> list:
    """
    Extract uncompleted task checklist items.

    Finds all `- [ ]` patterns (uncompleted tasks) and ignores `- [x]` (completed).

    Args:
        body: Comment body containing task lists

    Returns:
        List of task strings in format "- [ ] Task description"
    """
    # Find all uncompleted tasks
    tasks = re.findall(r'- \[ \] (.+)', body)
    return [f"- [ ] {task}" for task in tasks]


def sanitize_comment_body(body: str) -> str:
    """
    Remove problematic characters from comment body.

    - Removes null bytes (\x00)
    - Removes control characters except \n and \t
    - Preserves Unicode and emoji

    Args:
        body: Raw comment body

    Returns:
        Sanitized comment body
    """
    # Remove null bytes
    body = body.replace('\x00', '')

    # Remove control characters except newlines and tabs
    # Pattern: \x00-\x08, \x0B, \x0C, \x0E-\x1F, \x7F
    body = re.sub(r'[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]', '', body)

    return body


def safe_load_comments(file_path: str) -> list:
    """
    Load JSON with robust encoding handling.

    Tries UTF-8, then UTF-8 with error replacement, then cleans and retries.

    Args:
        file_path: Path to JSON file

    Returns:
        List of comment dictionaries
    """
    try:
        # Attempt 1: Standard UTF-8
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except UnicodeDecodeError:
        # Attempt 2: UTF-8 with error replacement
        try:
            with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
                return json.load(f)
        except json.JSONDecodeError:
            pass
    except json.JSONDecodeError:
        pass

    # Attempt 3: Read as text, clean, then parse
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            # Remove null bytes and other problematic chars
            content = content.replace('\x00', '')
            return json.loads(content)
    except Exception as e:
        print(f"Error loading comments from {file_path}: {e}", file=sys.stderr)
        return []


def process_comment(comment: dict) -> dict:
    """
    Apply filtering logic to a single comment.

    Based on classification:
        - keep_full: Return unchanged
        - discard: Return minimal metadata + [FILTERED] marker
        - extract: Extract suggestions and create filtered body

    Adds metadata:
        - filtered: bool (True if modified)
        - original_length: int (original body length)

    Args:
        comment: Comment dictionary

    Returns:
        Filtered comment dictionary
    """
    classification = classify_comment(comment)

    # Keep full: return unchanged
    if classification == 'keep_full':
        return comment

    original_body = comment.get('body', '')
    original_length = len(original_body)

    # Discard: return minimal metadata
    if classification == 'discard':
        return {
            'id': comment.get('id'),
            'user': comment.get('user'),
            'comment_type': comment.get('comment_type'),
            'created_at': comment.get('created_at'),
            'updated_at': comment.get('updated_at'),
            'path': comment.get('path'),
            'line': comment.get('line'),
            'body': f"[FILTERED SUMMARY from {comment.get('user', 'bot')}]",
            'original_length': original_length,
            'filtered': True,
        }

    # Extract: extract actionable content
    if classification == 'extract':
        suggestions = extract_suggestions(original_body)
        tasks = extract_task_items(original_body)

        # Build filtered body
        parts = []

        if suggestions:
            parts.append(f"**{len(suggestions)} Code Suggestions:**\n")
            for i, sug in enumerate(suggestions[:3], 1):  # Limit to top 3
                parts.append(f"{i}. {sug['title']} (priority: {sug['importance']})")
                code = sug.get('content') or sug.get('code', '')
                if code:
                    parts.append(f"```\n{code}\n```\n")

        if tasks:
            parts.append(f"\n**{len(tasks)} Action Items:**")
            for task in tasks[:5]:  # Limit to 5 tasks
                parts.append(task)

        filtered_body = '\n'.join(parts) if parts else '[No actionable content extracted]'

        # Create filtered comment with all original metadata
        result = comment.copy()
        result['body'] = filtered_body
        result['original_length'] = original_length
        result['filtered'] = True

        return result

    # Shouldn't reach here, but return original as fallback
    return comment


def estimate_tokens(comment_dict: dict) -> int:
    """
    Estimate tokens from FULL JSON representation of comment.

    JSON files include massive metadata overhead:
    - Field names, URLs, diff hunks, IDs
    - Formatting, escape sequences
    - Overhead typically 4-5x the body text alone

    Args:
        comment_dict: Full comment dictionary

    Returns:
        Estimated token count for this comment in JSON format
    """
    # Serialize to JSON to get true size
    json_str = json.dumps(comment_dict, indent=2, ensure_ascii=False)
    # JSON has lower token density than plain text (0.40 vs 0.75)
    return int(len(json_str) * TOKEN_PER_CHAR)


def apply_token_budget(comments: list, max_tokens: int) -> list:
    """
    Ensure comments fit within token budget.

    Priority order:
        1. Human comments (filtered=False or no [bot] in user)
        2. Inline reviews (has 'path' field)
        3. Extracted suggestions (filtered=True)
        4. Other bot comments

    Truncates or discards comments to fit budget.
    Minimum 200 tokens required to keep a comment.

    Args:
        comments: List of comment dictionaries
        max_tokens: Maximum token budget

    Returns:
        List of comments within budget
    """
    def get_priority(comment: dict) -> int:
        """Get priority for sorting (lower number = higher priority)."""
        user = comment.get('user', '')
        is_filtered = comment.get('filtered', False)
        has_path = comment.get('path') is not None

        # Priority 0: Human comments
        if not user.endswith('[bot]'):
            return 0

        # Priority 1: Inline reviews
        if has_path:
            return 1

        # Priority 2: Extracted suggestions
        if is_filtered:
            return 2

        # Priority 3: Other bot comments
        return 3

    # Sort by priority
    prioritized = sorted(comments, key=get_priority)

    total_tokens = 0
    result = []

    for comment in prioritized:
        tokens = estimate_tokens(comment)

        if total_tokens + tokens <= max_tokens:
            # Fits in budget - keep as is
            result.append(comment)
            total_tokens += tokens
        else:
            # Exceeds budget - check remaining space
            remaining_tokens = max_tokens - total_tokens

            if remaining_tokens >= MIN_COMMENT_TOKENS:
                # Enough room to truncate and keep meaningful content
                body = comment.get('body', '')
                char_budget = int(remaining_tokens / TOKEN_PER_CHAR)
                truncated_comment = comment.copy()
                truncated_comment['body'] = body[:char_budget] + '\n[TRUNCATED]'
                result.append(truncated_comment)
                total_tokens = max_tokens
                # Budget now exhausted - stop processing
                break

            # Not enough room for meaningful content - stop processing
            break

    return result


def filter_comments(comments: list, max_tokens: int = 15000) -> Tuple[list, dict]:
    """
    Main filtering pipeline.

    Processes each comment, applies token budget, and calculates statistics.

    Args:
        comments: List of comment dictionaries
        max_tokens: Maximum token budget (default: 15000)

    Returns:
        Tuple of (filtered_comments, stats_dict)

        Stats dict includes:
            - original_count, filtered_count
            - original_chars, filtered_chars
            - original_tokens, filtered_tokens
            - reduction_percent
            - kept_full_count, extracted_count, discarded_count
            - by_type: dict of counts by comment_type
            - by_user: dict of counts by user
    """
    # Process each comment
    processed = [process_comment(c) for c in comments]

    # Apply token budget
    filtered = apply_token_budget(processed, max_tokens)

    # Calculate statistics using full JSON representation
    original_json = json.dumps(comments, indent=2, ensure_ascii=False)
    filtered_json = json.dumps(filtered, indent=2, ensure_ascii=False)
    original_chars = len(original_json)
    filtered_chars = len(filtered_json)
    original_tokens = int(original_chars * TOKEN_PER_CHAR)
    filtered_tokens = int(filtered_chars * TOKEN_PER_CHAR)

    reduction_percent = 0
    if original_chars > 0:
        reduction_percent = ((original_chars - filtered_chars) / original_chars) * 100

    # Count by classification
    kept_full_count = sum(1 for c in processed if not c.get('filtered', False))
    filtered_comments_list = [c for c in processed if c.get('filtered', False)]
    extracted_count = sum(1 for c in filtered_comments_list if '[No actionable content extracted]' not in c.get('body', '') and '[FILTERED' not in c.get('body', ''))
    discarded_count = sum(1 for c in filtered_comments_list if '[FILTERED' in c.get('body', ''))

    # Count by type (action categories + comment types)
    by_type = {
        'kept_full': kept_full_count,
        'extracted': extracted_count,
        'discarded': discarded_count,
        'human_comments': sum(1 for c in comments if not c.get('user', '').endswith('[bot]')),
        'bot_comments': sum(1 for c in comments if c.get('user', '').endswith('[bot]')),
    }
    # Add comment_type counts
    for c in comments:
        ctype = c.get('comment_type', 'unknown')
        by_type[ctype] = by_type.get(ctype, 0) + 1

    # Count by user (with original and filtered counts)
    by_user = {}
    for c in comments:
        user = c.get('user', 'unknown')
        if user not in by_user:
            by_user[user] = {'original_count': 0, 'filtered_count': 0}
        by_user[user]['original_count'] += 1

    for c in filtered:
        user = c.get('user', 'unknown')
        if user in by_user:
            by_user[user]['filtered_count'] += 1

    stats = {
        'original_count': len(comments),
        'filtered_count': len(filtered),
        'original_chars': original_chars,
        'filtered_chars': filtered_chars,
        'original_tokens': original_tokens,
        'filtered_tokens': filtered_tokens,
        'reduction_percent': reduction_percent,
        'kept_full_count': kept_full_count,
        'extracted_count': extracted_count,
        'discarded_count': discarded_count,
        'by_type': by_type,
        'by_user': by_user,
    }

    return filtered, stats


def merge_filtered_comments(existing: list, new: list) -> list:
    """
    Merge new filtered comments with existing.

    Preserves original_length metadata and deduplicates by comment ID.

    Args:
        existing: Existing list of comments
        new: New list of comments to merge

    Returns:
        Merged list of comments (deduplicated)
    """
    # Build dict by comment ID
    existing_dict = {c['id']: c for c in existing}

    for comment in new:
        cid = comment['id']
        if cid in existing_dict:
            # Preserve original_length metadata if already filtered
            if existing_dict[cid].get('filtered') and 'original_length' in existing_dict[cid]:
                if 'original_length' not in comment:
                    comment['original_length'] = existing_dict[cid]['original_length']

        # Update or add comment
        existing_dict[cid] = comment

    return list(existing_dict.values())


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description='Filter verbose bot comments from PR comment JSON files',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Filter comments to new file
  python pr-comment-filter.py pr12-comments.json --output pr12-filtered.json

  # Update file in-place
  python pr-comment-filter.py pr12-comments.json --in-place

  # Custom token budget
  python pr-comment-filter.py pr12-comments.json --max-tokens 10000
        """
    )

    parser.add_argument('input', help='Input JSON file from pr-comment-grabber.py')
    parser.add_argument('--output', help='Output file (default: INPUT-filtered.json)')
    parser.add_argument('--in-place', action='store_true', help='Update input file directly')
    parser.add_argument('--max-tokens', type=int, default=MAX_TOKENS,
                       help=f'Maximum token budget (default: {MAX_TOKENS})')

    args = parser.parse_args()

    # Validate input file exists
    if not os.path.exists(args.input):
        print(f"Error: Input file not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    # Load comments
    print(f"Loading comments from {args.input}...")
    comments = safe_load_comments(args.input)

    if not comments:
        print("Warning: No comments loaded", file=sys.stderr)
        sys.exit(1)

    print(f"Loaded {len(comments)} comments")

    # Filter comments
    print(f"Filtering with {args.max_tokens} token budget...")
    filtered, stats = filter_comments(comments, max_tokens=args.max_tokens)

    # Print statistics
    print(f"\n=== Filtering Results ===")
    print(f"Original: {stats['original_count']} comments, {stats['original_chars']:,} chars (~{stats['original_tokens']:,} tokens)")
    print(f"Filtered: {stats['filtered_count']} comments, {stats['filtered_chars']:,} chars (~{stats['filtered_tokens']:,} tokens)")
    print(f"Reduction: {stats['reduction_percent']:.1f}%")
    print(f"\nBreakdown:")
    print(f"  - Kept full: {stats['kept_full_count']}")
    print(f"  - Extracted: {stats['extracted_count']}")
    print(f"  - Discarded: {stats['discarded_count']}")

    # Determine output path
    if args.in_place:
        output_path = args.input
    elif args.output:
        output_path = args.output
    else:
        # Default: add -filtered suffix
        base, ext = os.path.splitext(args.input)
        output_path = f"{base}-filtered{ext}"

    # Save filtered comments
    print(f"\nSaving to {output_path}...")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(filtered, f, indent=2, ensure_ascii=False)

    print(f"Done! Saved {len(filtered)} filtered comments")


if __name__ == '__main__':
    main()
