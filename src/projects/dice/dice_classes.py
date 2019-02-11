#!/usr/bin/env python3
"""
Dice game(s) simulator
"""

import random
from typing import Sequence

random.seed(42)


class Die:
    """Class Die"""

    def __init__(self, possible_values: Sequence) -> None:
        """Class Die constructor"""
        self._all_values = possible_values
        self._value = random.choice(self._all_values)

    @property
    def value(self):
        """Get the die value"""
        raise NotImplementedError

    @value.setter
    def value(self, _):
        """Value property setter"""
        raise ValueError("You must roll the die to change its value")

    def __str__(self):
        """__str__ override"""
        raise NotImplementedError

    def roll(self):
        """Roll the die"""
        raise NotImplementedError


class FrozenDie(Die):
    """A die that cannot be rolled"""

    def __init__(self, possible_values: Sequence) -> None:
        """Class FrozenDie constructor"""
        super().__init__(possible_values)
        self._frozen = False

    @property
    def frozen(self) -> bool:
        """Frozen property getter"""
        raise NotImplementedError

    @frozen.setter
    def frozen(self, new_value: bool) -> None:
        """Frozen property setter"""
        raise NotImplementedError

    def roll(self):
        """Roll the die"""
        raise NotImplementedError


class Cup:
    """Class Cup"""

    def __init__(self, num_dice: int, num_sides: int = 6) -> None:
        """Class FrozenDie constructor"""
        self._dice = [Die(range(1, num_sides + 1)) for _ in range(num_dice)]

    def __iter__(self):
        """Cup iterator"""
        return iter(self._dice)

    def __str__(self) -> str:
        """__str__ override"""
        raise NotImplementedError

    def shake(self) -> None:
        """Shake a cup"""
        raise NotImplementedError

    def add(self, die: object) -> None:
        """Add a die to the cup"""
        raise NotImplementedError

    def remove(self, idx: int):
        """Remove a die from the cup"""
        return self._dice.pop(idx)

    def roll(self, *args) -> None:
        """Roll specific dice"""
        raise NotImplementedError
