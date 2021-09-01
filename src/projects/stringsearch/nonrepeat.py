#!/usr/bin/env python3
"""
`stringsearch` implementation and driver

@authors: 
"""


def find_non_repeat(a_string: str) -> str:
    """
    Finds the first non-repeating character in a string

    Implementation using a `dictionary`

    :param a_string: string to search
    :returns: the first unique character in the string
    :raises: ValueError is there are no unique characters

    >>> find_non_repeat("aaab")
    'b'
    >>> find_non_repeat("asuilhtrfasjkncasuielhfnj")
    't'
    >>> find_non_repeat("uendhjsuehjfnae")
    'd'
    """
    # TODO: Implement this function
    ...


def main():
    """Main function"""
    the_string = "abxba"
    result = find_non_repeat(the_string)
    print(f"{result} is the first non-repeating character in {the_string}")


if __name__ == "__main__":
    main()
