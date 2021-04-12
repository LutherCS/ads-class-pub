#!/usr/bin/env python3
"""
`morse` implementation

@authors: Roman Yasinovskyy
@version: 2021.4
"""

from typing import Union
from pythonds3.trees import BinaryTree


class Coder:
    """Morse code encoder and decoder"""

    def __init__(self, file_in: str):
        self.morse_tree = BinaryTree("")

        with open(file_in) as morse_file:
            for line in morse_file:
                letter, code = line.split()
                self.follow_and_insert(code, letter)

    def follow_and_insert(self, code_str: str, letter: str) -> None:
        """
        Follow the tree and insert a letter

        @param code_str: morse code sequence
        @param letter: letter corresponding to the `code_str`
        """
        raise NotImplementedError

    def follow_and_retrieve(self, code_str: str) -> str:
        """
        Follow the tree and retrieve a letter

        @param code_str: morse code sequence
        @return letter corresponding to the `code_str`
        @raises ValueError if the code is not found
        """
        raise NotImplementedError

    def find_path(self, tree: BinaryTree, letter: str, path: str) -> Union[bool, str]:
        """
        Find a path to the letter
        Encoder's helper function

        @param tree: Morse tree
        @param letter: letter to encode
        @param path: path to the letter
        @return path to the letter
        """
        raise NotImplementedError

    def encode(self, msg: str) -> str:
        """
        Encode a message
        
        @param msg: text to encode
        @return Morse code representation of the the message
        """
        raise NotImplementedError

    def decode(self, code: str) -> str:
        """
        Decode a message

        @param code: Morse code sequence to decode
        @return text corresponding to the code
        """
        raise NotImplementedError
