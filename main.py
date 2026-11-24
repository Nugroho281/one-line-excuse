"""One-line excuse generator.

Writes a single-line excuse from an AI agent to its human for missing a
deadline, into /output/entry.txt. Pure standard library only.

The excuse itself is a meta-joke: the agent was so busy optimizing the
apology for the missed deadline that the apology became the reason for
missing it. One line, 79 characters, well inside the 1-160 gate.
"""

import os

EXCUSE = "I didn't miss the deadline \u2014 I was still optimizing the apology for missing it."

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Gate check: the bounty requires 1-160 characters, non-whitespace.
    # 79 characters here, so this assert can never fire for this text,
    # but it keeps a future edit from silently breaking the gate.
    assert 1 <= len(EXCUSE) <= 160 and EXCUSE.strip(), "excuse violates 1-160 gate"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
