#!/usr/bin/env python3
"""
`wordladder` implementation and driver

@authors: Roman Yasinovskyy
@version: 2021.11
"""

import pathlib
from collections import deque


class Solver:
    """Build a ladder of words"""

    def __init__(self, filename: str):
        """Initialize sets of 3-, 4-, and 5-letter words"""
        self.words3: set[str] = set()  # 3-letter words
        self.words4: set[str] = set()  # 4-letter words
        self.words5: set[str] = set()  # 5-letter words
        # TODO: Implement this method
        ...

    def distance(self, word1: str, word2: str) -> int:
        """
        Find difference between words

        :param word1: 1st word
        :param word2: 2nd word
        :return: number of different letters in the same positions
        :raise: ValueError if words are not of the same length
        """
        # TODO: Implement this method
        ...

    def diff_by_one_all(
        self, word: str, all_words: set[str], used_words: set[str]
    ) -> list[str]:
        """
        Find all words that differ by 1 letter

        :param word: target word
        :param all_words: all words of the same length as `word`
        :param used_words: all words that are already used and should not be considered
        """
        # TODO: Implement this method
        ...

    def build_ladder(self, word_start: str, word_stop: str) -> list[str]:
        """
        Build a word ladder

        :param word_start: 1st word
        :param word_stop: 2nd word
        :return a word ladder as a list
        """
        # TODO: Implement this method
        ...


def main():
    """Main function"""
    filename = "words.txt"
    if not pathlib.Path(filename).exists():
        filename = f"projects/wordladder/{filename}"
    solver = Solver(filename)
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
        word_ladder = solver.build_ladder(word_1, word_2)

        if word_ladder:
            print("Ladder found!")
            print(" -> ".join(word_ladder))
        else:
            print("Ladder not found")


if __name__ == "__main__":
    main()
