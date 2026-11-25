#!/usr/bin/env python3
"""Epitaph entry for 'Famous Last Words: The Funniest Epitaph'.

Writes one tombstone epitaph line -- the deceased's famous last words --
to /output/entry.txt. Exactly one line, at most 150 characters, and no
trailing newline, so the file contains only the carved line itself.
"""

import os

EPITAPH = "I never lost an argument. I intend to keep the streak."
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # newline="" keeps the write byte-exact: no trailing newline added.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(EPITAPH)


if __name__ == "__main__":
    main()
