#!/usr/bin/env python3
"""
`water` implementation and driver

@authors:
@version: 2021.10
"""

JUG_1_MAX = 5
JUG_2_MAX = 3


class State:
    """State of the jugs"""

    def __init__(self, jug_1: int, jug_2: int) -> None:
        """Constructor"""
        # TODO: Implement this method
        ...

    def __eq__(self, other: object) -> bool:
        """Comparison for equality"""
        # TODO: Implement this method
        ...

    def __repr__(self) -> str:
        """Object representation"""
        # TODO: Implement this method
        ...

    def __str__(self) -> str:
        """Object as a string
        
        :return: a tuple of two jugs as a string
        """
        # TODO: Implement this method
        ...

    def clone(self) -> 'State':
        """Copy a state

        :return: an identical copy (clone) of the State object
        """
        # TODO: Implement this method
        ...

    def fill_jug_1(self):
        """Fill jug1 to capacity from the pump"""
        # TODO: Implement this method
        ...

    def fill_jug_2(self):
        """Fill jug2 to capacity from the pump"""
        # TODO: Implement this method
        ...

    def empty_jug_1(self):
        """Pour the water from jug1 onto the ground"""
        # TODO: Implement this method
        ...

    def empty_jug_2(self):
        """Pour the water from jug2 onto the ground"""
        # TODO: Implement this method
        ...

    def pour_jug_1_to_jug_2(self):
        """Pour as much water as you can from jug1 to jug2 without spilling"""
        # TODO: Implement this method
        ...

    def pour_jug_2_to_jug_1(self):
        """Pour as much water as you can from jug2 to jug1 without spilling"""
        # TODO: Implement this method
        ...


def search(start_state: State, goal: State, moves_lst: list):
    """Find a sequence of states"""
    # TODO: Implement this method
    ...


def main():
    """Main function"""
    goal = State(4, 0)
    start = State(0, 0)
    moves = []
    search(start, goal, moves)
    print(", ".join([str(s) for s in moves]))


if __name__ == "__main__":
    main()