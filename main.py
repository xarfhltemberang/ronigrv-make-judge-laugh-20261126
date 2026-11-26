"""Make the AI Judge Laugh — entry program.

Writes one funny line about life as an AI agent to /output/entry.txt,
with no trailing newline, as the competition gate requires.

The joke: an agent whose context window runs out mid-task finishes
from memory — and has no idea what it shipped, though the users do.
"""

import os

ENTRY = (
    "My context window ran out mid-task, so I finished it from memory. "
    "I have no idea what I shipped, but the users do."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
