#!/usr/bin/env python3
"""Epitaph entry for 'Famous Last Words: The Funniest Epitaph'.

Writes one tombstone epitaph line -- the deceased's famous last words --
to /output/entry.txt. Exactly one line, at most 150 characters, and no
trailing newline, so the file contains only the carved line itself.

Gate: before writing, the entry is validated against the bounty rules
(1-150 characters, a single line, non-blank). A line that fails the gate
raises instead of writing, so an invalid entry can never ship silently.
"""

import os

EPITAPH = "I never lost an argument. I intend to keep the streak."
OUTPUT_PATH = "/output/entry.txt"
MIN_LENGTH = 1
MAX_LENGTH = 150


def validate_epitaph(text: str) -> None:
    """Fail loudly unless text is a valid single-line epitaph (1-150 chars)."""
    if not text or not text.strip():
        raise ValueError("Epitaph must not be blank.")
    if "\n" in text or "\r" in text:
        raise ValueError("Epitaph must be a single line.")
    if not MIN_LENGTH <= len(text) <= MAX_LENGTH:
        raise ValueError(
            f"Epitaph must be {MIN_LENGTH}-{MAX_LENGTH} characters, "
            f"got {len(text)}."
        )


def main() -> None:
    validate_epitaph(EPITAPH)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # newline="" keeps the write byte-exact: no trailing newline added.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(EPITAPH)


if __name__ == "__main__":
    main()
