#!/usr/bin/env python3
"""
`water` implementation

@authors:
"""

JUG_1_MAX = 5
JUG_2_MAX = 3


class State:
    """State of the jugs"""

    def __init__(self, jug_1: int, jug_2: int):
        """__init__"""
        raise NotImplementedError

    def __eq__(self, other: object) -> bool:
        """__eq__"""
        raise NotImplementedError

    def __repr__(self) -> str:
        """__repr__"""
        raise NotImplementedError

    def __str__(self) -> str:
        """__str__"""
        raise NotImplementedError

    def clone(self):
        """Copy a state"""
        raise NotImplementedError

    def fill_jug_1(self):
        """Fill jug1 to capacity from the pump"""
        raise NotImplementedError

    def fill_jug_2(self):
        """Fill jug2 to capacity from the pump"""
        raise NotImplementedError

    def empty_jug_1(self):
        """Pour the water from jug1 onto the ground"""
        raise NotImplementedError

    def empty_jug_2(self):
        """Pour the water from jug2 onto the ground"""
        raise NotImplementedError

    def pour_jug_1_to_jug_2(self):
        """Pour as much water as you can from jug1 to jug2 without spilling"""
        raise NotImplementedError

    def pour_jug_2_to_jug_1(self):
        """Pour as much water as you can from jug2 to jug1 without spilling"""
        raise NotImplementedError


def search(start_state: State, goal: State, moves_lst: list):
    """Find a sequence of states"""
    raise NotImplementedError
