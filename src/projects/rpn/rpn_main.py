#!/usr/bin/env python3
"""
Reverse Polish Notation demo
"""

import random
from rpn import rpn_calc


def main():
    """Main function"""
    checksum = rpn_calc("data/projects/rpn/rpn_input_1.txt")
    print(f"Checksum is {checksum:.2f}")


if __name__ == "__main__":
    main()
