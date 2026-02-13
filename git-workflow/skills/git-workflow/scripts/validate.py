#!/usr/bin/env python3
"""
Simple commit message validator for git hooks.

Usage:
  As git hook:    cp validate.py .git/hooks/commit-msg && chmod +x .git/hooks/commit-msg
  Standalone:     python validate.py --message "feat: add feature"
  From file:      python validate.py commit-msg-file
"""

import sys
import re


def validate_commit(message):
    """Validate commit message, return (is_valid, error_message)."""
    
    header = message.split('\n')[0]
    
    # Special formats are always valid
    if (header.startswith('Merge branch') or 
        header.startswith('Revert') or 
        header == 'chore: init'):
        return True, None
    
    # Standard format
    pattern = (
        r'^(feat|fix|refactor|perf|style|test|docs|build|ops|chore)'
        r'(\([a-z0-9-]+\))?'
        r'!?'
        r': '
        r'.{1,100}$'
    )
    
    if not re.match(pattern, header):
        return False, (
            f"Invalid format: {header}\n\n"
            f"Expected: <type>(<scope>): <description>\n"
            f"Example:  feat(auth): add login\n\n"
            f"Valid types: feat, fix, refactor, perf, style, test, docs, build, ops, chore"
        )
    
    # Additional checks
    desc = header.split(': ', 1)[1]
    
    if desc[0].isupper():
        return False, "Description should start with lowercase"
    
    if desc.endswith('.'):
        return False, "Description should not end with period"
    
    return True, None


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Validate conventional commits')
    parser.add_argument('file', nargs='?', help='Commit message file')
    parser.add_argument('--message', help='Validate message directly')
    args = parser.parse_args()
    
    # Get message
    if args.message:
        message = args.message
    elif args.file:
        with open(args.file) as f:
            message = f.read()
    else:
        message = sys.stdin.read()
    
    # Validate
    valid, error = validate_commit(message.strip())
    
    if valid:
        print("✓ Valid commit message")
        sys.exit(0)
    else:
        print(f"✗ {error}")
        sys.exit(1)


if __name__ == '__main__':
    main()
