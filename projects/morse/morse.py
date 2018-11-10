"""Morse code encoding and decoding"""
#!/usr/bin/env python3
# encoding: UTF-8


from notes.trees.BinaryTree import BinaryTree


class Coder:
    """Morse Code Encoder/Decoder"""

    def __init__(self, file_in: str):
        """Constructor"""
        raise NotImplementedError

    def follow_and_insert(self, code_str: str, letter: str):
        """Follow the tree and insert a letter"""
        raise NotImplementedError

    def follow_and_retrieve(self, code_str: str):
        """Follow the tree and retrieve a letter"""
        raise NotImplementedError

    def find_path(self, tree: object, letter: str, path: str):
        """Find a key"""
        raise NotImplementedError

    def encode(self, msg: str):
        """Encode a message"""
        raise NotImplementedError

    def decode(self, code: str):
        """Decode a message"""
        raise NotImplementedError


def main():
    morse_coder = Coder("data/projects/morse/morse.txt")
    print("Encoding 'sos'")
    print("Expected: ... --- ...")
    print("Encoded : {}".format(morse_coder.encode("sos")))
    print("---")
    print("Encoding 'data structures'")
    print("Expected: -.. .- - .- ... - .-. ..- -.-. - ..- .-. . ... ")
    print("Encoded : {}".format(morse_coder.encode("data structures")))
    print("---")
    print("Encoding '$$'")
    print("Expected: Error message")
    try:
        print("Encoded : {}".format(morse_coder.encode("$$")))
    except ValueError as ve:
        print("ERROR: {}".format(ve))
    print("---")
    print("Decoding '.... . .-.. .-.. --- --..-- -.-. ... .---- -.... -----'")
    print("Expected: hello,cs160")
    test_str = ".... . .-.. .-.. --- --..-- -.-. ... .---- -.... -----"
    print("Decoded : {}".format(morse_coder.decode(test_str)))


if __name__ == "__main__":
    main()
