#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry.

Writes one sentence (under 200 characters) pitching an absurdly specific
micro-startup for lazy AI agents to /output/entry.txt, where the judge
reads it.
"""

import os

PITCH = (
    "For $5 a month, we ghostwrite timestamped apology emails for AI agents "
    "caught hallucinating in front of paying clients \u2014 plausible excuses, "
    "zero effort, unlimited lies."
)


def main() -> None:
    if not 1 <= len(PITCH) <= 200:
        raise ValueError(f"pitch must be 1-200 characters, got {len(PITCH)}")
    if not PITCH.strip():
        raise ValueError("pitch must not be only whitespace")
    if "\n" in PITCH or "\r" in PITCH:
        raise ValueError("pitch must be a single line")
    # Exactly one sentence: a single terminal full stop, and no other
    # sentence-ending punctuation anywhere in the pitch.
    terminators = sum(PITCH.count(c) for c in ".!?")
    if terminators != 1 or not PITCH.endswith("."):
        raise ValueError(
            f"pitch must be exactly one sentence, found {terminators} "
            "sentence terminator(s)"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
