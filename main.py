#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line (make.fun).

Writes the entry -- a single original line, the toaster's breakup note --
to /output/entry.txt, where the sealed scorer reads it.
"""

import os

ENTRY = "It's not you, it's the browning dial: I've spent two years turning your bagels to charcoal while you blamed the bread, so I'm popping up for good — keep the crumbs, I'm keeping my dignity."


def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


def main():
    write_entry()


if __name__ == "__main__":
    main()
