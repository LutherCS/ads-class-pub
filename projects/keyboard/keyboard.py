#!/usr/bin/env python3
"""
`keyboard` implementation and driver

@authors:
"""

import pathlib

def spell_check(filename: str) -> None:
    """Rank words by their proximity to the target"""
    # TODO: Implement this function
    ...


def main():
    """Entry point"""
    filename = "sample.in.txt"
    if not pathlib.Path(filename).exists():
        filename = f"projects/keyboard/{filename}"
    spell_check(filename)


if __name__ == "__main__":
    main()
