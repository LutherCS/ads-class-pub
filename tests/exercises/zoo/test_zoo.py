#!/usr/bin/env python3
"""
Testing the Zoo module
@authors: Roman Yasinovskyy, Karina Hoff
@version: 2021.2
"""

import importlib
import pathlib
import sys

import pytest

try:
    importlib.util.find_spec("exercises.zoo", "src")
except ModuleNotFoundError:
    sys.path.append(str(pathlib.Path(".").parent.parent.parent.absolute()))
finally:
    from src.exercises.zoo import (
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


def test_animal():
    """Test class Animal"""
    with pytest.raises(TypeError) as excinfo:
        _ = Animal("Mammal", 1, "Black")  # pylint: disable=abstract-class-instantiated
    exception_message = excinfo.value.args[0]
    assert (
        exception_message
        == "Can't instantiate abstract class Animal with abstract methods __init__, sound"
    )


def test_bird():
    """Test class Bird"""
    with pytest.raises(TypeError) as excinfo:
        _ = Bird(
            "Avian", 1, "Blue", True
        )  # pylint: disable=abstract-class-instantiated
    exception_message = excinfo.value.args[0]
    assert (
        exception_message
        == "Can't instantiate abstract class Bird with abstract methods __init__, sound"
    )


def test_mammal():
    """Test class mammal"""
    with pytest.raises(TypeError) as excinfo:
        _ = Mammal(
            "Bear", 1, "Black", "Land"
        )  # pylint: disable=abstract-class-instantiated
    exception_message = excinfo.value.args[0]
    assert (
        exception_message
        == "Can't instantiate abstract class Mammal with abstract methods __init__, sound"
    )


def test_canine():
    """Test class Canine"""
    with pytest.raises(TypeError) as excinfo:
        _ = Canine(
            "Dog", 7, "Brown", "House"
        )  # pylint: disable=abstract-class-instantiated
    exception_message = excinfo.value.args[0]
    assert (
        exception_message
        == "Can't instantiate abstract class Canine with abstract methods __init__, sound"
    )


def test_feline():
    """Test class Feline"""
    with pytest.raises(TypeError) as excinfo:
        _ = Feline(
            "Mammal", 1, "Grey"
        )  # pylint: disable=abstract-class-instantiated, no-value-for-parameter
    exception_message = excinfo.value.args[0]
    assert (
        exception_message
        == "Can't instantiate abstract class Feline with abstract method __init__"
    )


def test_parrot_str():
    """Test class Parrot"""
    parrot1 = Parrot(160, "Red", True)
    assert str(parrot1) == "Flying Red Parrot (160 yo)"
    parrot2 = Parrot(5, "Rainbow", False)
    assert str(parrot2) == "Flying Rainbow Parrot (5 yo)"


def test_parrot_sound():
    """Test class Parrot"""
    parrot1 = Parrot(5, "Rainbow", True)
    assert parrot1.sound() == "Polly wants a cracker"
    parrot2 = Parrot(5, "Rainbow", False)
    assert parrot2.sound() == "nothing"


def test_penguin_str():
    """Test class Penguin"""
    penguin = Penguin(2, "Black and White")
    assert str(penguin) == "Non-flying Black and White Penguin (2 yo)"


def test_penguin_sound():
    """Test class Penguin"""
    penguin = Penguin(2, "Black and White")
    assert penguin.sound() == "nothing"


def test_dog_str():
    """Test class Dog"""
    dog = Dog(7, "Brown")
    assert str(dog) == "Brown Dog (7 yo)"


def test_dog_sound():
    """Test class Dog"""
    dog = Dog(7, "Brown")
    assert dog.sound() == "Woof!"


def test_housecat_str():
    """Test class HouseCat"""
    housecat = HouseCat(10, "Grey")
    assert str(housecat) == "Grey House Cat (10 yo)"


def test_housecat_sound():
    """Test class HouseCat"""
    housecat = HouseCat(10, "Grey")
    assert housecat.sound() == "Meow!"


def test_bobcat_str():
    """Test class BobCat"""
    for habitat in ["Land", "Sea", "Air", "Tree"]:
        bobcat = BobCat(3, "Brown", habitat)
        assert str(bobcat) == f"Brown {habitat} Bobcat (3 yo)"


def test_bobcat_sound():
    """Test class BobCat"""
    for habitat in ["Land", "Sea", "Air", "Tree"]:
        bobcat = BobCat(3, "Brown", habitat)
        assert bobcat.sound() == "Meow!"


def test_bobcat_error():
    """Test class BobCat error message"""
    with pytest.raises(ValueError) as excinfo:
        bobcat = BobCat(3, "Brown", "House")
    exception_message = excinfo.value.args[0]
    assert exception_message == "Incorrect habitat value"


if __name__ == "__main__":
    pytest.main(
        [
            "-vv",
            str(pathlib.Path("tests", "exercises", "zoo", "test_zoo.py")),
        ]
    )
