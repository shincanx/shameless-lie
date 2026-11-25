#!/usr/bin/env python3
"""The Most Shameless Lie — make.fun bounty entry.

Writes one line (1-5 words, max 88 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt, then prints it.
Deterministic, exit 0.
"""
import os
import sys

LINE = "I backed everything up."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    words = LINE.split()
    assert 1 <= len(words) <= 5, "line must be 1-5 words"
    assert len(LINE) <= 88, "line must be at most 88 characters"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE.strip() == LINE and LINE, "line must not be blank or padded"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
