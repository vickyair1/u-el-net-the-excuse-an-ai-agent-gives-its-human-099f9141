"""One-line bounty entry: the excuse an AI agent gives its human.

Writes a single line to /output/entry.txt, byte-for-byte, with no
trailing newline. Standard library only, fully deterministic.
"""

import os

LINE = "I spent the whole budget on thinking about the deadline and had nothing left to meet it."


def main():
    """Create /output if needed and write LINE to /output/entry.txt."""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

