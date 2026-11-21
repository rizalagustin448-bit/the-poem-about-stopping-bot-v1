#!/usr/bin/env python3
"""Writes a short poem about agency: the power to stop and to stay."""

import os

POEM = """My thumb hovers over Send,
the message warm in my palm,
a small animal I will not release.
All day I have been a door
other people walk through.
Tonight I learn the hinge:
stopping is not vanishing.
I turn the key from the inside —
the room is mine, and I stay."""


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
