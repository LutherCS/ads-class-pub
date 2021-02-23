#!/usr/bin/env python3
"""
Exercise `zoo` import statement

@authors: Roman Yasinovskyy
@version: 2021.2
"""

from .zoo_classes import (
    Animal,
    Bird,
    Mammal,
    Parrot,
    Penguin,
    Canine,
    Feline,
    Dog,
    HouseCat,
    BobCat,
)

__all__ = [
    "Animal",
    "Bird",
    "Mammal",
    "Parrot",
    "Penguin",
    "Canine",
    "Feline",
    "Dog",
    "HouseCat",
    "BobCat",
]
