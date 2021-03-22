#!/usr/bin/env python3
"""
`water` driver

@authors: Roman Yasinovskyy
@version: 2021.3
"""

from water import State, search


def main():
    """Main function"""
    goal = State(4, 0)
    start = State(0, 0)
    moves = []
    search(start, goal, moves)
    print(", ".join([str(s) for s in moves]))


if __name__ == "__main__":
    main()
