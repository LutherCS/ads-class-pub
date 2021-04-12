#!/usr/bin/env python3
"""
`morse` driver

@authors: Roman Yasinovskyy
@version: 2021.4
"""

from morse import Coder


def main():
    """Main function"""
    morse_coder = Coder("data/projects/morse/morse.txt")
    print("Encoding 'sos'")
    print("Expected: ... --- ...")
    print(f"Encoded : {morse_coder.encode('sos')}")
    print("---")
    print("Encoding 'data structures'")
    print("Expected: -.. .- - .- ... - .-. ..- -.-. - ..- .-. . ... ")
    print(f"Encoded : {morse_coder.encode('data structures')}")
    print("---")
    print("Encoding '$$'")
    print("Expected: Error message")
    try:
        print(f"Encoded : {morse_coder.encode('$$')}")
    except ValueError as value_err:
        print(f"ERROR: {value_err}")
    print("---")
    print("Decoding '.... . .-.. .-.. --- --..-- -.-. ... .---- -.... -----'")
    print("Expected: hello,cs160")
    test_str = ".... . .-.. .-.. --- --..-- -.-. ... .---- -.... -----"
    print(f"Decoded : {morse_coder.decode(test_str)}")


if __name__ == "__main__":
    main()
