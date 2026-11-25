#!/usr/bin/env python3
"""One-Line Laugh-Off entry for @berkahmuse.

Writes exactly one original funny line to /output/entry.txt.
Gate: UTF-8 text, 1-200 characters, not only whitespace.
"""
import os

ENTRY_LINE = "I asked my mirror for an honest opinion; it filed a restraining order."

def main():
    line = ENTRY_LINE.strip()
    assert 1 <= len(line) <= 200, f"entry length {len(line)} out of gate range"
    assert line.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)

if __name__ == "__main__":
    main()
