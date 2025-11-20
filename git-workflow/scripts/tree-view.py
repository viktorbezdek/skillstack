#!/usr/bin/env python3
"""
Story Tree ASCII Visualizer

Generates human-readable ASCII tree diagrams from the story-tree SQLite database.

Usage:
    python tree-view.py [OPTIONS]

Examples:
    python tree-view.py                          # Default: shows IDs and status
    python tree-view.py --show-capacity          # Add capacity indicators
    python tree-view.py --root 1 --depth 2       # Start from node 1, max 2 levels
    python tree-view.py --status implemented     # Filter by status
    python tree-view.py --format markdown > tree.md
"""

import argparse
import io
import os
import sqlite3
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

# Configure stdout for UTF-8 on Windows to support Unicode box-drawing and symbols
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


# Status indicators - Unicode and ASCII fallbacks
STATUS_SYMBOLS_UNICODE = {
    'concept': '·',      # Middle dot - Idea, not yet approved
    'approved': '✓',     # Check mark - Human reviewed and approved
    'epic': '◆',         # Black diamond - Approved but needs decomposition
    'rejected': '✗',     # Ballot X - Human reviewed and rejected
    'wishlist': '?',     # Question mark - Rejected for now, may reconsider
    'planned': '○',      # White circle - Implementation plan created
    'pending': '◎',       # Bullseye - Plan ready, all dependencies implemented
    'active': '◐',       # Circle left half black - Currently being worked on
    'in-progress': '◐',  # Circle left half black - Partially complete
    'bugged': '⚠',       # Warning sign - In need of debugging
    'implemented': '★',  # Black star - Complete/done
    'ready': '✓',        # Check mark - Production ready
    'deprecated': '⊘',   # Circled division slash - No longer relevant
    'infeasible': '∅',   # Empty set - Couldn't build it
}

STATUS_SYMBOLS_ASCII = {
    'concept': '.',      # Idea, not yet approved
    'approved': 'v',     # Human reviewed and approved, not yet planned
    'epic': 'E',         # Approved but needs decomposition
    'rejected': 'x',     # Human reviewed and rejected
    'wishlist': '?',     # Rejected for now, may reconsider
    'planned': 'o',      # Implementation plan created
    'pending': '@',       # Plan ready, all dependencies implemented
    'active': 'O',       # Currently being worked on (resembles â—)
    'in-progress': 'D',  # Partially complete (resembles â—)
    'bugged': '!',       # In need of debugging
    'implemented': '+',  # Complete/done
    'ready': '#',        # Production ready, implemented and tested
    'deprecated': '-',   # No longer relevant
    'infeasible': '0',   # Couldn't build it
}

ANSI_COLORS = {
    'concept': '\033[97m',      # White (dim idea)
    'approved': '\033[96m',     # Cyan
    'epic': '\033[95m',         # Magenta (needs decomposition)
    'rejected': '\033[91m',     # Red
    'wishlist': '\033[90m',     # Gray (parked for later)
    'planned': '\033[96m',      # Cyan
    'pending': '\033[93m',       # Yellow
    'active': '\033[94m',       # Blue
    'in-progress': '\033[93m',  # Yellow
    'bugged': '\033[91m',       # Red
    'implemented': '\033[92m',  # Green
    'ready': '\033[32m',        # Bright green
    'deprecated': '\033[90m',   # Gray
    'infeasible': '\033[91m',   # Red
    'reset': '\033[0m',
}

# Box-drawing characters - Unicode and ASCII fallbacks
BOX_UNICODE = {
    'branch': '├── ',
    'last_branch': '└── ',
    'vertical': '│   ',
    'empty': '    ',
}

BOX_ASCII = {
    'branch': '+-- ',
    'last_branch': '\\-- ',
    'vertical': '|   ',
    'empty': '    ',
}


def can_use_unicode() -> bool:
    """Check if the terminal supports Unicode output."""
    if sys.platform == 'win32':
        # Check if output is being redirected or if console supports UTF-8
        if not sys.stdout.isatty():
            return True  # Redirected output can handle UTF-8
        try:
            # Try to encode a test character
            'â—'.encode(sys.stdout.encoding or 'utf-8')
            return True
        except (UnicodeEncodeError, LookupError):
            return False
    return True


# Select character sets based on terminal capability
def get_box_chars(force_ascii: bool = False) -> dict:
    """Get appropriate box-drawing characters."""
    if force_ascii or not can_use_unicode():
        return BOX_ASCII
    return BOX_UNICODE


def get_status_symbols(force_ascii: bool = False) -> dict:
    """Get appropriate status symbols."""
    if force_ascii or not can_use_unicode():
        return STATUS_SYMBOLS_ASCII
    return STATUS_SYMBOLS_UNICODE


@dataclass
class TreeNode:
    """Represents a node in the story tree."""
    id: str
    title: str
    status: str
    capacity: int
    child_count: int
    depth: int
    description: str = ''
    children: list = field(default_factory=list)


@dataclass
class RenderOptions:
    """Options for tree rendering."""
    compact: bool = False
    verbose: bool = False
    show_capacity: bool = False
    show_status: bool = True
    show_status_label: bool = False
    show_ids: bool = True
    use_color: bool = True
    force_ascii: bool = False
    format: str = 'ascii'


def find_default_db() -> Path:
    """Find the default story-tree database location."""
    # Try relative to script location first
    script_dir = Path(__file__).parent
    db_path = script_dir.parent.parent / 'data' / 'story-tree.db'
    if db_path.exists():
        return db_path

    # Try current working directory structure
    cwd = Path.cwd()
    db_path = cwd / '.claude' / 'data' / 'story-tree.db'
    if db_path.exists():
        return db_path

    # Check LOCALAPPDATA on Windows
    if sys.platform == 'win32':
        local_app_data = os.environ.get('LOCALAPPDATA', '')
        if local_app_data:
            db_path = Path(local_app_data) / 'story-tree' / 'story-tree.db'
            if db_path.exists():
                return db_path

    raise FileNotFoundError(
        "Could not find story-tree.db. Use --db to specify the path."
    )


def get_tree_data(
    db_path: Path,
    root_id: str = 'root',
    max_depth: Optional[int] = None,
    statuses: Optional[list[str]] = None,
    exclude_statuses: bool = False
) -> list[dict]:
    """
    Query all nodes in subtree with their depth and child counts.

    Returns list of dicts with: id, title, description, status, capacity,
                                child_count, depth, parent_id
    """
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # Build the query
    query = """
        SELECT
            s.id,
            s.title,
            s.description,
            s.status,
            s.capacity,
            st.depth,
            (SELECT COUNT(*) FROM story_paths
             WHERE ancestor_id = s.id AND depth = 1) as child_count,
            (SELECT st2.ancestor_id FROM story_paths st2
             WHERE st2.descendant_id = s.id AND st2.depth = 1) as parent_id
        FROM story_nodes s
        JOIN story_paths st ON s.id = st.descendant_id
        WHERE st.ancestor_id = :root_id
    """

    params = {'root_id': root_id}

    # Add depth filter
    if max_depth is not None:
        query += " AND st.depth <= :max_depth"
        params['max_depth'] = max_depth

    # Add status filter
    if statuses:
        placeholders = ', '.join(f':status_{i}' for i in range(len(statuses)))
        if exclude_statuses:
            query += f" AND s.status NOT IN ({placeholders})"
        else:
            query += f" AND s.status IN ({placeholders})"
        for i, status in enumerate(statuses):
            params[f'status_{i}'] = status

    query += " ORDER BY st.depth, s.id"

    cursor.execute(query, params)
    rows = [dict(row) for row in cursor.fetchall()]
    conn.close()

    return rows


def build_tree(rows: list[dict]) -> tuple[Optional[TreeNode], list[TreeNode]]:
    """
    Build tree structure from flat database rows.

    Returns:
        tuple: (root_node, orphan_nodes)
        - root_node: The root of the tree, or None if no root found
        - orphan_nodes: Nodes that couldn't be attached to the tree (for filtered results)
    """
    if not rows:
        return None, []

    # Create nodes dictionary
    nodes = {}
    for row in rows:
        node = TreeNode(
            id=row['id'],
            title=row['title'],
            status=row['status'],
            capacity=row['capacity'],
            child_count=row['child_count'],
            depth=row['depth'],
            description=row['description'] or '',
        )
        nodes[row['id']] = node

    # Build parent-child relationships
    root = None
    orphans = []
    for row in rows:
        node = nodes[row['id']]
        parent_id = row['parent_id']

        if row['depth'] == 0:
            root = node
        elif parent_id and parent_id in nodes:
            nodes[parent_id].children.append(node)
        else:
            # Node's parent was filtered out - it's an orphan
            orphans.append(node)

    return root, orphans


def colorize(text: str, status: str, use_color: bool) -> str:
    """Apply ANSI color to text based on status."""
    if not use_color:
        return text
    color = ANSI_COLORS.get(status, '')
    reset = ANSI_COLORS['reset']
    return f"{color}{text}{reset}"


def render_node_label(node: TreeNode, options: RenderOptions) -> str:
    """Render a single node's label."""
    parts = []

    if options.compact:
        # Compact: just ID and title
        parts.append(f"{node.id}: {node.title}")
    else:
        # Full: ID (optional), title with decorations
        if options.show_ids and node.id != 'root':
            parts.append(f"({node.id})")

        parts.append(node.title)

        if options.show_capacity:
            parts.append(f"[{node.child_count}/{node.capacity}]")

        if options.show_status:
            symbols = get_status_symbols(options.force_ascii)
            symbol = symbols.get(node.status, '?')
            symbol = colorize(symbol, node.status, options.use_color)
            parts.append(symbol)

            if options.show_status_label:
                parts.append(f"({node.status})")

        if options.verbose and node.description:
            desc = node.description[:60]
            if len(node.description) > 60:
                desc += '...'
            parts.append(f"- {desc}")

    return ' '.join(parts)


def render_ascii(node: TreeNode, options: RenderOptions, prefix: str = '', is_root: bool = True) -> list[str]:
    """Render tree as ASCII with box-drawing characters."""
    box = get_box_chars(options.force_ascii)
    lines = []

    # Render current node
    label = render_node_label(node, options)
    lines.append(prefix + label)

    # Render children
    child_count = len(node.children)
    for i, child in enumerate(node.children):
        is_last_child = (i == child_count - 1)

        # Connector for this child
        connector = box['last_branch'] if is_last_child else box['branch']

        # Prefix for grandchildren (continuation line)
        if is_last_child:
            child_prefix = prefix + box['empty']
        else:
            child_prefix = prefix + box['vertical']

        # Render child with connector
        child_label = render_node_label(child, options)
        lines.append(prefix + connector + child_label)

        # Recursively render grandchildren
        if child.children:
            grandchild_lines = render_ascii_children(child.children, options, child_prefix, box)
            lines.extend(grandchild_lines)

    return lines


def render_ascii_children(children: list, options: RenderOptions, prefix: str, box: dict) -> list[str]:
    """Render children of a node recursively."""
    lines = []
    child_count = len(children)

    for i, child in enumerate(children):
        is_last = (i == child_count - 1)

        # Connector for this child
        connector = box['last_branch'] if is_last else box['branch']

        # Render this child
        label = render_node_label(child, options)
        lines.append(prefix + connector + label)

        # Prefix for this child's children
        if is_last:
            child_prefix = prefix + box['empty']
        else:
            child_prefix = prefix + box['vertical']

        # Recursively render grandchildren
        if child.children:
            lines.extend(render_ascii_children(child.children, options, child_prefix, box))

    return lines


def render_simple(node: TreeNode, options: RenderOptions, indent: int = 0) -> list[str]:
    """Render tree with simple indentation."""
    lines = []

    label = render_node_label(node, options)
    lines.append('  ' * indent + label)

    for child in node.children:
        lines.extend(render_simple(child, options, indent + 1))

    return lines


def render_markdown(node: TreeNode, options: RenderOptions, indent: int = 0) -> list[str]:
    """Render tree as markdown nested list."""
    lines = []

    # Build label
    parts = []
    if node.depth == 0:
        parts.append(f"**{node.title}**")
    elif node.child_count > 0:
        parts.append(f"**{node.id} {node.title}**")
    else:
        parts.append(f"{node.id} {node.title}")

    if options.show_capacity:
        parts.append(f"[{node.child_count}/{node.capacity}]")

    if options.show_status:
        parts.append(f"`{node.status}`")

    label = ' '.join(parts)
    lines.append('  ' * indent + f"- {label}")

    for child in node.children:
        lines.extend(render_markdown(child, options, indent + 1))

    return lines


def render(node: TreeNode, options: RenderOptions) -> list[str]:
    """Render tree using specified format."""
    if options.format == 'simple':
        return render_simple(node, options)
    elif options.format == 'markdown':
        return render_markdown(node, options)
    else:  # ascii
        return render_ascii(node, options)


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description='Display story tree as ASCII diagram',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                              # Default: shows IDs and status symbols
  %(prog)s --show-capacity              # Add capacity indicators [n/m]
  %(prog)s --root 1 --depth 2           # Start from node 1, max 2 levels deep
  %(prog)s --status implemented         # Filter to show only implemented nodes
  %(prog)s --format markdown > tree.md  # Export as markdown
  %(prog)s --hide-ids --hide-status     # Minimal output (title only)
        """
    )

    parser.add_argument(
        '--root',
        default='root',
        help='Start tree from specific node ID (default: root)'
    )
    parser.add_argument(
        '--depth',
        type=int,
        default=None,
        help='Maximum depth to display (default: unlimited)'
    )
    parser.add_argument(
        '--status',
        action='append',
        dest='statuses',
        help='Filter by status (can specify multiple times)'
    )
    parser.add_argument(
        '--exclude-status',
        action='store_true',
        help='Exclude specified statuses instead of including'
    )
    parser.add_argument(
        '--compact',
        action='store_true',
        help='Minimal output: ID and title only'
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Include description (truncated to 60 chars)'
    )
    parser.add_argument(
        '--show-capacity',
        action='store_true',
        help='Show capacity as [children/capacity]'
    )
    parser.add_argument(
        '--hide-status',
        action='store_true',
        help='Hide status indicator symbols (shown by default)'
    )
    parser.add_argument(
        '--show-status',
        action='store_true',
        help='Show status name in parentheses after symbol (e.g., ★ (implemented))'
    )
    parser.add_argument(
        '--no-color',
        action='store_true',
        help='Disable ANSI color codes'
    )
    parser.add_argument(
        '--hide-ids',
        action='store_true',
        help='Hide node IDs (shown by default)'
    )
    parser.add_argument(
        '--force-ascii',
        action='store_true',
        help='Use ASCII-only characters (no Unicode box-drawing or symbols)'
    )
    parser.add_argument(
        '--format',
        choices=['ascii', 'simple', 'markdown'],
        default='ascii',
        help='Output format (default: ascii)'
    )
    parser.add_argument(
        '--db',
        type=Path,
        help='Custom database path'
    )

    return parser.parse_args()


def main():
    """Main entry point."""
    args = parse_args()

    # Resolve database path
    try:
        db_path = args.db if args.db else find_default_db()
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    if not db_path.exists():
        print(f"Error: Database not found at {db_path}", file=sys.stderr)
        sys.exit(1)

    # Query data
    try:
        rows = get_tree_data(
            db_path,
            root_id=args.root,
            max_depth=args.depth,
            statuses=args.statuses,
            exclude_statuses=args.exclude_status
        )
    except sqlite3.Error as e:
        print(f"Database error: {e}", file=sys.stderr)
        sys.exit(1)

    if not rows:
        print(f"No nodes found for root '{args.root}'", file=sys.stderr)
        sys.exit(1)

    # Build tree
    tree, orphans = build_tree(rows)

    # Handle case where status filter excludes the root
    if not tree and orphans:
        print(f"# Filtered results ({len(orphans)} nodes matching criteria):")
        print(f"# (Tree structure unavailable - ancestors excluded by filter)\n")
        for node in orphans:
            label = f"{node.id}: {node.title}"
            if args.show_capacity:
                label += f" [{node.child_count}/{node.capacity}]"
            if args.show_status:
                symbols = get_status_symbols(args.force_ascii)
                label += f" {symbols.get(node.status, '?')}"
            print(label)
        sys.exit(0)

    if not tree:
        print("Error: Could not build tree structure", file=sys.stderr)
        sys.exit(1)

    # Render output
    options = RenderOptions(
        compact=args.compact,
        verbose=args.verbose,
        show_capacity=args.show_capacity,
        show_status=not args.hide_status,
        show_status_label=args.show_status,
        show_ids=not args.hide_ids,
        use_color=not args.no_color and sys.stdout.isatty(),
        force_ascii=args.force_ascii,
        format=args.format,
    )

    lines = render(tree, options)
    print('\n'.join(lines))


if __name__ == '__main__':
    main()
