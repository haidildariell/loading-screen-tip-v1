#!/usr/bin/env python3
"""Loading Screen Gold: A Tip in 200 Characters.

Writes one loading-screen tip to /output/entry.txt -- a single line,
at most 200 characters, for stressed developers and the AI coding
agents building beside them.
"""

import os

MAX_CHARS = 200

TIP = (
    "Tip: your agent didn't break the code - it did exactly what you "
    "asked. Read the diff. Then re-read your prompt."
)


def validate_tip(tip):
    """Fail loudly instead of silently writing an entry the gate refuses."""
    if not tip.strip():
        raise ValueError("tip must not be blank")
    if len(tip) > MAX_CHARS:
        raise ValueError(
            "tip is %d characters, over the %d limit" % (len(tip), MAX_CHARS)
        )


def main():
    validate_tip(TIP)
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(TIP)


if __name__ == "__main__":
    main()
