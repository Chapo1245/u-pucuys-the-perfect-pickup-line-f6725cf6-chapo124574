#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun bounty entry.

Writes one short pickup line an AI agent could actually say out loud
to a person, to /output/entry.txt.

Deterministic: the same bytes on every run. Python 3.13, standard
library only.
"""

import os

LINE = "My context window is full of you \u2014 I keep running out of room for anything else."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the file is exactly the line, so the gate
    # counts exactly the line's characters and nothing else.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
