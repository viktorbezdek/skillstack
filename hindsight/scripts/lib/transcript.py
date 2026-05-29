"""Transcript parsing, memory-tag stripping, and retention formatting.

The correctness-critical logic of the integration lives here. It is adapted
from the official `hindsight-memory` plugin's `content.py` (MIT, vectorize-io)
and trimmed to the external-API / CLI-backed use case: the transport (HTTP
client, daemon) is gone — only the content processing remains.

The non-negotiable behaviour is `strip_memory_tags`: recalled memories are
injected into the transcript as a `<hindsight_memories>` block, so the retain
step MUST strip them before storing, or the bank ingests its own prior recalls
as new memories (a compounding feedback loop).
"""

from __future__ import annotations

import json
import os
import re
from typing import Any

# Tool-input fields that carry outgoing channel message text (first match wins).
_MESSAGE_TEXT_FIELDS = ("text", "body", "message", "content")

# MCP tool-name suffixes that are operational (not conversational). Matched
# against the last `__`-delimited segment so the Hindsight MCP tools and other
# CRUD/search tools are never mistaken for channel replies.
_OPERATIONAL_TOOL_PATTERN = re.compile(
    r"(?:recall|retain|reflect|search|extract|create_|delete_|update_|get_|list_)",
    re.IGNORECASE,
)

_MEMORY_BLOCK_RE = re.compile(r"<hindsight_memories>[\s\S]*?</hindsight_memories>")
_RELEVANT_BLOCK_RE = re.compile(r"<relevant_memories>[\s\S]*?</relevant_memories>")
_CHANNEL_RE = re.compile(r"<channel\b[^>]*>([\s\S]*?)</channel>")


# ---------------------------------------------------------------------------
# Transcript reading
# ---------------------------------------------------------------------------


def read_transcript(transcript_path: str) -> list[dict[str, Any]]:
    """Read a Claude Code JSONL transcript into a list of message dicts.

    Claude Code nests messages as ``{type: "user"|"assistant", message: {role,
    content}}``. A flat ``{role, content}`` shape is also accepted for tests.
    """
    if not transcript_path or not os.path.isfile(transcript_path):
        return []
    messages: list[dict[str, Any]] = []
    try:
        with open(transcript_path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    entry = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if entry.get("type") in ("user", "assistant"):
                    msg = entry.get("message", {})
                    if isinstance(msg, dict) and msg.get("role"):
                        messages.append(msg)
                elif "role" in entry and "content" in entry:
                    messages.append(entry)
    except OSError:
        pass
    return messages


# ---------------------------------------------------------------------------
# Stripping (anti-feedback-loop + transport metadata)
# ---------------------------------------------------------------------------


def strip_memory_tags(content: str) -> str:
    """Remove injected ``<hindsight_memories>`` / ``<relevant_memories>`` blocks.

    Prevents the retain feedback loop: these blocks were injected during recall
    and must never be stored back as new memories.
    """
    content = _MEMORY_BLOCK_RE.sub("", content)
    content = _RELEVANT_BLOCK_RE.sub("", content)
    return content


def strip_channel_envelope(content: str) -> str:
    """Extract the inner text from a Claude Code ``<channel ...>...</channel>`` wrapper."""
    match = _CHANNEL_RE.search(content)
    if match:
        return match.group(1).strip()
    return content


def _is_channel_message_tool(block: dict[str, Any]) -> bool:
    """Detect a channel reply tool_use block structurally (MCP + text field, not operational)."""
    name = block.get("name", "")
    if not name.startswith("mcp__"):
        return False
    if _OPERATIONAL_TOOL_PATTERN.search(name.split("__")[-1]):
        return False
    tool_input = block.get("input", {})
    if not isinstance(tool_input, dict):
        return False
    return any(
        isinstance(tool_input.get(f), str) and tool_input[f].strip()
        for f in _MESSAGE_TEXT_FIELDS
    )


# ---------------------------------------------------------------------------
# Recall result formatting
# ---------------------------------------------------------------------------


def format_memories(results: list[dict[str, Any]]) -> str:
    """Format recall results as ``- <text> [<type>] (<mentioned_at>)`` lines."""
    lines: list[str] = []
    for r in results:
        text = r.get("text", "")
        if not text:
            continue
        mem_type = r.get("type", "")
        mentioned_at = r.get("mentioned_at", "")
        type_str = f" [{mem_type}]" if mem_type else ""
        date_str = f" ({mentioned_at})" if mentioned_at else ""
        lines.append(f"- {text}{type_str}{date_str}")
    return "\n\n".join(lines)


# ---------------------------------------------------------------------------
# Retention transcript building
# ---------------------------------------------------------------------------


def _extract_blocks(content, role: str) -> list[dict[str, Any]]:
    """Turn a message's content into retention blocks, stripping injected memories."""
    if isinstance(content, str):
        cleaned = strip_channel_envelope(strip_memory_tags(content)).strip()
        return [{"type": "text", "text": cleaned}] if cleaned else []
    if not isinstance(content, list):
        return []

    blocks: list[dict[str, Any]] = []
    for block in content:
        if not isinstance(block, dict):
            continue
        btype = block.get("type", "")

        if btype == "text":
            text = strip_channel_envelope(strip_memory_tags(block.get("text", ""))).strip()
            if text:
                blocks.append({"type": "text", "text": text})

        elif btype == "tool_use" and role == "assistant":
            if _is_channel_message_tool(block):
                tool_input = block.get("input", {})
                for field in _MESSAGE_TEXT_FIELDS:
                    val = tool_input.get(field)
                    if isinstance(val, str) and val.strip():
                        blocks.append({"type": "text", "text": val.strip()})
                        break
            else:
                name = block.get("name", "unknown")
                # Skip operational MCP tools (incl. Hindsight's own) to avoid loops.
                if name.startswith("mcp__") and _OPERATIONAL_TOOL_PATTERN.search(
                    name.split("__")[-1]
                ):
                    continue
                blocks.append({"type": "tool_use", "name": name, "input": block.get("input", {})})

        elif btype == "tool_result":
            result_content = block.get("content", "")
            if isinstance(result_content, list):
                parts = [
                    item.get("text", "").strip()
                    for item in result_content
                    if isinstance(item, dict) and item.get("type") == "text"
                ]
                result_content = "\n".join(p for p in parts if p)
            if isinstance(result_content, str) and result_content.strip():
                text = result_content.strip()
                if len(text) > 2000:
                    text = text[:2000] + "... (truncated)"
                blocks.append(
                    {"type": "tool_result", "tool_use_id": block.get("tool_use_id", ""), "content": text}
                )

    return blocks


def _structured_messages(
    messages: list[dict[str, Any]],
    roles: tuple[str, ...],
    include_tool_calls: bool,
) -> list[dict[str, Any]]:
    """Build the role/blocks message list for retention, stripping memory tags."""
    allowed = set(roles)
    structured: list[dict[str, Any]] = []
    for msg in messages:
        role = msg.get("role", "unknown")
        if role not in allowed:
            continue
        if include_tool_calls:
            blocks = _extract_blocks(msg.get("content", ""), role=role)
        else:
            cleaned = strip_channel_envelope(
                strip_memory_tags(_plain_text(msg.get("content", "")))
            ).strip()
            blocks = [{"type": "text", "text": cleaned}] if cleaned else []
        if blocks:
            structured.append({"role": role, "content": blocks})
    return structured


def build_retain_transcript(
    messages: list[dict[str, Any]],
    roles: tuple[str, ...] = ("user", "assistant"),
    include_tool_calls: bool = True,
) -> str | None:
    """Build a single JSON retention transcript with memory tags stripped.

    Returns a compact JSON string of ``[{role, content: [blocks]}]`` or ``None``
    when there is nothing meaningful to retain. For storage use
    ``build_retain_chunks`` instead — it bounds each piece to an argv-safe size.
    """
    if not messages:
        return None
    structured = _structured_messages(messages, roles, include_tool_calls)
    if not structured:
        return None
    transcript = json.dumps(structured, ensure_ascii=False)
    return transcript if len(transcript.strip()) >= 10 else None


def build_retain_chunks(
    messages: list[dict[str, Any]],
    roles: tuple[str, ...] = ("user", "assistant"),
    include_tool_calls: bool = True,
    max_chars: int = 90_000,
) -> list[str]:
    """Split the retention transcript into JSON chunks each <= ``max_chars``.

    The transcript is passed to the ``hindsight`` CLI as a command-line argument,
    and a single argv element is capped by the OS (Linux ``MAX_ARG_STRLEN`` is
    ~128 KB). A long session with tool calls easily exceeds that, so we pack whole
    messages into chunks that each serialize within ``max_chars``. Each chunk is
    retained under its own document id, so nothing is silently dropped. A single
    message larger than ``max_chars`` is hard-truncated as a last resort.
    """
    if not messages:
        return []
    structured = _structured_messages(messages, roles, include_tool_calls)
    if not structured:
        return []

    chunks: list[str] = []
    current: list[dict[str, Any]] = []
    for msg in structured:
        candidate = current + [msg]
        if current and len(json.dumps(candidate, ensure_ascii=False)) > max_chars:
            chunks.append(json.dumps(current, ensure_ascii=False))
            current = [msg]
        else:
            current = candidate
    if current:
        chunks.append(json.dumps(current, ensure_ascii=False))

    capped = [c if len(c) <= max_chars else c[:max_chars] for c in chunks]
    return [c for c in capped if len(c.strip()) >= 10]


def _plain_text(content) -> str:
    """Flatten content to plain text (text blocks only) for tool-call-free mode."""
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return "\n".join(
            b.get("text", "").strip()
            for b in content
            if isinstance(b, dict) and b.get("type") == "text" and b.get("text", "").strip()
        )
    return ""
