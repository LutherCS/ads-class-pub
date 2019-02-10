#!/usr/bin/env python3
"""String search"""

THE_STRING = "aaab"


def find_non_repeat(a_string: str) -> str:
    """Find the first unique character in a string"""
    for idx, char in enumerate(a_string):
        if char not in a_string[idx + 1 :]:
            return char
    return ""


def main():
    """Main function"""
    print(find_non_repeat(THE_STRING))


if __name__ == "__main__":
    main()
