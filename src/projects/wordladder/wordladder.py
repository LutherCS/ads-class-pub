#!/usr/bin/env python3
"""
`wordladder` implementation

@authors: Roman Yasinovskyy
@version: 2021.4
"""

from collections import deque
from typing import List, Set


class Solver:
    """Build a ladder of words"""

    def __init__(self, filename: str):
        """Initialize sets of 3-, 4-, and 5-letter words"""
        self.words3: Set[str] = set()  # 3-letter words
        self.words4: Set[str] = set()  # 4-letter words
        self.words5: Set[str] = set()  # 5-letter words
        raise NotImplementedError

    def distance(self, word1: str, word2: str) -> int:
        """
        Find difference between words

        @param word1: 1st word
        @param word2: 2nd word
        @return number of different letters in the same positions
        @raises ValueError if words are not of the same length
        """
        raise NotImplementedError

    def diff_by_one_all(
        self, word: str, all_words: Set[str], used_words: Set[str]
    ) -> List[str]:
        """
        Find all words that differ by 1 letter

        @param word: target word
        @param all_words: all words of the same length as `word`
        @param used_words: all words that are already used and should not be considered
        """
        raise NotImplementedError

    def build_ladder(self, word_start: str, word_stop: str) -> List[str]:
        """
        Build a word ladder

        @param word_start: 1st word
        @param word_stop: 2nd word
        @return a word ladder as a list
        """
        raise NotImplementedError
