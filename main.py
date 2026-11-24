#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line — entry program.

Writes one breakup line (at most 200 chars) to /output/entry.txt.
"""

import os

ENTRY = "I have been buffering this goodbye for two years. It finally loaded."
MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def main():
    text = ENTRY
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}")
    if text != text.strip() or "\n" in text:
        raise ValueError("entry must be a single line with no surrounding whitespace")
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(OUTPUT_PATH, 0o644)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        if f.read() != text:
            raise ValueError("read-back mismatch")
    print(f"Wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
