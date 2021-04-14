#!/usr/bin/env python3
"""
`wordladder` driver

@authors: Roman Yasinovskyy
@version: 2021.4
"""

from wordladder import Solver


def main():
    """Main function"""
    solver = Solver("data/projects/wordladder/words.txt")
    all_combinations = [
        ("elk", "elf"),
        ("elf", "elk"),
        ("odd", "peg"),
        ("tar", "pit"),
        ("milk", "mint"),
        ("memo", "koko"),
        ("myxo", "zuza"),
        ("snob", "rynd"),
        ("tenor", "xenon"),
        ("start", "spark"),
        ("camel", "amigo"),
        ("water", "stone"),
        ("abc", "xyz"),
        ("gizmo", "mulch"),
        ("tutor", "xenon"),
        ("peace", "piece"),
    ]
    for word_1, word_2 in all_combinations:
        print(f"Let's turn {word_1} into {word_2}")
        word_ladder = solver.build_ladder(word_1, word_2, debug=False)

        if word_ladder:
            print("Ladder found!")
            print(" -> ".join(word_ladder))
        else:
            print("Ladder not found")


if __name__ == "__main__":
    main()
