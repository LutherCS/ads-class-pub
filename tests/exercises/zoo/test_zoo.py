#!/usr/bin/env python3
"""
Testing the Zoo module
@authors: Roman Yasinovskyy, Karina Hoff
@updated: 2019
"""

import pytest
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

class TestAnimalsMethods:
    """Testing module Animal"""

    @pytest.fixture(scope="function", autouse=True)
    def setup_class(self):
        """Setting up"""

    def test_animal(self):
        """Test class Animal"""
        with pytest.raises(TypeError) as excinfo:
            _ = Animal("Mammal", 1, "Black")  # pylint: disable=abstract-class-instantiated
        exception_message = excinfo.value.args[0]
        assert (
            exception_message
            == "Can't instantiate abstract class Animal with abstract methods __init__, sound"
        )

    def test_bird(self):
        """Test class Bird"""
        with pytest.raises(TypeError) as excinfo:
            _ = Bird("Avian", 1, "Blue", True)  # pylint: disable=abstract-class-instantiated
        exception_message = excinfo.value.args[0]
        assert (
            exception_message
            == "Can't instantiate abstract class Bird with abstract methods __init__, sound"
        )

    def test_mammal(self):
        """Test class mammal"""
        with pytest.raises(TypeError) as excinfo:
            _ = Mammal("Bear", 1, "Black", "Land")  # pylint: disable=abstract-class-instantiated
        exception_message = excinfo.value.args[0]
        assert (
            exception_message
            == "Can't instantiate abstract class Mammal with abstract methods __init__, sound"
        )

    def test_parrot(self):
        """Test class Parrot"""
        parrot = Parrot(5, "Rainbow", True)
        assert parrot.sound() == "'Polly wants a cracker'"
        parrot = Parrot(5, "Rainbow", False)
        assert parrot.sound() == "nothing"
        assert parrot.__str__() == "Flying Rainbow Parrot (5 yo)"

    def test_penguin(self):
        """Test class Penguin"""
        penguin = Penguin(2, "Black and White")
        assert penguin.sound() == "nothing"
        assert penguin.__str__() == "Non-flying Black and White Penguin (2 yo)"

    def test_canine(self):
        """Test class Canine"""
        with pytest.raises(TypeError) as excinfo:
            _ = Canine("Dog", 7, "Brown", "House")  # pylint: disable=abstract-class-instantiated
        exception_message = excinfo.value.args[0]
        assert (
            exception_message
            == "Can't instantiate abstract class Canine with abstract methods __init__, sound"
        )

    def test_feline(self):
        """Test class Feline"""
        with pytest.raises(TypeError) as excinfo:
            _ = Feline("Mammal", 1, "Grey")  # pylint: disable=abstract-class-instantiated, no-value-for-parameter
        exception_message = excinfo.value.args[0]
        assert (
            exception_message
            == "Can't instantiate abstract class Feline with abstract methods __init__"
        )

    def test_dog(self):
        """Test class Dog"""
        dog = Dog(7, "Brown")
        assert dog.sound() == "Woof!"
        assert dog.__str__() == "Brown Dog (7 yo)"

    def test_housecat(self):
        """Test class HouseCat"""
        housecat = HouseCat(10, "Grey")
        assert housecat.sound() == "Meow!"
        assert housecat.__str__() == "Grey House Cat (10 yo)"

    def test_bobcat(self):
        """Test class BobCat"""
        # Correct values for habitat
        for habitat in ["Land", "Sea", "Air", "Tree"]:
            bobcat = BobCat(3, "Brown", habitat)
            assert bobcat.sound() == "Meow!"
            assert bobcat.__str__() == ("Brown {} Bobcat (3 yo)".format(habitat))
        # Incorrect value for habitat
        with pytest.raises(ValueError) as excinfo:
            bobcat = BobCat(3, "Brown", "House")
        exception_message = excinfo.value.args[0]
        assert exception_message == "Incorrect habitat value"


if __name__ == "__main__":
    pytest.main(["-v", "test_zoo.py"])
