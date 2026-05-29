"""Behavioural tests for the correctness-critical transcript logic.

Pure-function tests (no network, stdlib only): run with
``python3 -m unittest discover -s tests`` from the plugin root. The headline
guarantee is the anti-feedback-loop strip — if that regresses, the bank poisons
itself, so it gets explicit coverage.
"""

import json
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from lib.cli import make_doc_id  # noqa: E402
from lib.transcript import (  # noqa: E402
    build_retain_chunks,
    build_retain_transcript,
    format_memories,
    read_transcript,
    strip_memory_tags,
)


class TranscriptBehaviour(unittest.TestCase):
    def test_strip_memory_tags_removes_injected_block(self):
        text = "<hindsight_memories>\nOLD RECALL\n</hindsight_memories>\nReal content"
        out = strip_memory_tags(text)
        self.assertNotIn("OLD RECALL", out)
        self.assertIn("Real content", out)

    def test_retain_transcript_strips_feedback_loop_but_keeps_real_content(self):
        # The non-negotiable invariant: a recalled-memory block in the transcript
        # must never be stored back as a new memory.
        messages = [
            {
                "role": "user",
                "content": "<hindsight_memories>\nLEAKED\n</hindsight_memories>\nWhat is the doc-id scheme?",
            },
            {"role": "assistant", "content": [{"type": "text", "text": "It is sha256-based"}]},
        ]
        out = build_retain_transcript(messages)
        self.assertIsNotNone(out)
        self.assertNotIn("LEAKED", out)
        self.assertIn("doc-id scheme", out)
        self.assertIn("sha256-based", out)

    def test_read_transcript_parses_nested_and_flat(self):
        with tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False) as f:
            f.write(json.dumps({"type": "user", "message": {"role": "user", "content": "hi"}}) + "\n")
            f.write(json.dumps({"role": "assistant", "content": "yo"}) + "\n")  # flat
            f.write("not json\n")  # malformed line is skipped
            path = f.name
        try:
            msgs = read_transcript(path)
        finally:
            os.unlink(path)
        self.assertEqual(len(msgs), 2)
        self.assertEqual(msgs[0]["role"], "user")
        self.assertEqual(msgs[1]["role"], "assistant")

    def test_read_transcript_missing_file_is_empty(self):
        self.assertEqual(read_transcript("/no/such/file.jsonl"), [])
        self.assertEqual(read_transcript(""), [])

    def test_make_doc_id_is_deterministic_and_prefixed(self):
        a = make_doc_id("session-xyz")
        b = make_doc_id("session-xyz")
        c = make_doc_id("session-other")
        self.assertEqual(a, b)  # idempotent: same session → same id
        self.assertNotEqual(a, c)
        self.assertTrue(a.startswith("cc-"))

    def test_format_memories_renders_type_and_date(self):
        out = format_memories(
            [{"text": "Chose lean port", "type": "experience", "mentioned_at": "2026-05-29"}]
        )
        self.assertIn("- Chose lean port [experience] (2026-05-29)", out)

    def test_format_memories_skips_empty_text(self):
        self.assertEqual(format_memories([{"type": "world"}]), "")

    def test_chunks_stay_under_max_chars_and_lose_nothing(self):
        # A large transcript must split into argv-safe chunks (the bug: the whole
        # transcript was passed as one CLI argument and silently failed at the OS
        # arg-length limit on long sessions).
        big = "word " * 4000  # ~20 KB per message
        messages = [
            {"role": "user", "content": big},
            {"role": "assistant", "content": [{"type": "text", "text": big}]},
            {"role": "user", "content": big},
            {"role": "assistant", "content": [{"type": "text", "text": big}]},
        ]
        chunks = build_retain_chunks(messages, max_chars=25_000)
        self.assertGreater(len(chunks), 1, "should split into multiple chunks")
        for c in chunks:
            self.assertLessEqual(len(c), 25_000)
        # No message content is dropped across the chunk set.
        joined = "".join(chunks)
        self.assertEqual(joined.count('"role": "user"'), 2)
        self.assertEqual(joined.count('"role": "assistant"'), 2)

    def test_chunks_single_chunk_for_small_session_and_strips_memories(self):
        messages = [
            {"role": "user", "content": "<hindsight_memories>\nLEAK\n</hindsight_memories>\nreal q"},
        ]
        chunks = build_retain_chunks(messages, max_chars=90_000)
        self.assertEqual(len(chunks), 1)
        self.assertNotIn("LEAK", chunks[0])
        self.assertIn("real q", chunks[0])


if __name__ == "__main__":
    unittest.main()
