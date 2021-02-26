#!/usr/bin/env python3
"""
Project `rpn` driver

@authors: Roman Yasinovskyy
@version: 2021.2
"""

from rpn import rpn_calc


def main():
    """Main function"""
    filename = "data/projects/rpn/rpn_input_1.txt"
    print(f"Processing {filename}")
    checksum = rpn_calc(filename)
    print(f"Checksum is {checksum:.2f}")
    print("*" * 30)
    filename = "data/projects/rpn/rpn_input_2.txt"
    print(f"Processing {filename}")
    checksum = rpn_calc(filename)
    print(f"Checksum is {checksum:.2f}")


if __name__ == "__main__":
    main()
