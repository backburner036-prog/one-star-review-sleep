#!/usr/bin/env python3
"""Entry for make.fun's One-Star Review of Something Essential.

The program writes one deadpan one-star review of sleep to
/output/entry.txt. The review is a single line of at most 160 characters.
"""

import os

REVIEW = "Arrives late, leaves early, and charges eight hours for the visit."


def main():
    if not 1 <= len(REVIEW) <= 160 or "\n" in REVIEW or not REVIEW.strip():
        raise ValueError("review must be one line of 1-160 characters")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
