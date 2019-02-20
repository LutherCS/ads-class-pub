#!/usr/bin/env python3
"""
Exercise Zoo classes
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Class Animal"""

    @abstractmethod
    def __init__(self, spec_init, age_init, color_init):
        """Animal __init__"""
        self._spec = spec_init
        self._age = age_init
        self._color = color_init

    @abstractmethod
    def sound(self):
        """Make some noise"""
        pass

    def __str__(self):
        """__str__"""
        return "{} {} ({} yo)".format(self._color, self._spec, self._age)


class Bird(Animal):
    """Class Bird"""

    @abstractmethod
    def __init__(self, spec_init, age_init, color_init, flying_init):
        """Bird __init__"""
        # TODO: Invoke __init__ of the superclass
        # TODO: Initialize self._flying
        raise NotImplementedError

    def __str__(self):
        """___str__"""
        if self._flying:
            return "Flying " + super().__str__()
        else:
            return "Non-flying " + super().__str__()


class Mammal(Animal):
    """Class Mammal"""

    @abstractmethod
    def __init__(self, spec_init, age_init, color_init, habitat_init):
        """Mammal __init__"""
        # TODO: Invoke __init__ of the superclass
        # TODO: If habitat_init is "Land", "Sea", "Air" or "Tree", initialize self._habitat, else raise a ValueError
        raise NotImplementedError


class Parrot(Bird):
    """Parrot class"""

    def __init__(self, age_init, color_init, talking_init):
        """Parrot __init__"""
        # TODO: Invoke __init__ of the superclass
        # TODO: Initialize self._talking
        raise NotImplementedError

    def sound(self):
        """Making Parrot noise"""
        if self._talking:
            return "'Polly wants a cracker'"
        else:
            return "nothing"


class Penguin(Bird):
    """Penguin class"""

    def __init__(self, age_init, color_init):
        """Penguin __init__"""
        super().__init__("Penguin", age_init, color_init, False)

    def sound(self):
        """Making Penguin noise"""
        return "nothing"


class Canine(Mammal):
    """Class Canine"""

    @abstractmethod
    def __init__(self, spec_init, age_init, color_init, habitat_init):
        """Canine __init__"""
        super().__init__(spec_init, age_init, color_init, habitat_init)


class Feline(Mammal):
    """Class Feline"""

    @abstractmethod
    def __init__(self, spec_init, age_init, color_init, habitat_init):
        super().__init__(spec_init, age_init, color_init, habitat_init)

    def sound(self):
        """Making Feline noise"""
        return "Meow!"


class Dog(Canine):
    """Class Dog"""

    def __init__(self, age_init, color_init):
        """Dog __init__"""
        # TODO: Invoke __init__ of the superclass. All dogs live on Land
        raise NotImplementedError

    def sound(self):
        """Making Dog noise"""
        # TODO: All dogs say "Woof!"
        raise NotImplementedError


class HouseCat(Feline):
    """Class HouseCat"""

    def __init__(self, age_init, color_init):
        """HouseCat __init__"""
        super().__init__("House Cat", age_init, color_init, "Land")


class BobCat(Feline):
    """Class BobCat"""

    def __init__(self, age_, color_, habitat_):
        """BobCat __init__"""
        # TODO: Invoke __init__ of the superclass
        raise NotImplementedError

    def __str__(self):
        """BobCat __str__"""
        # TODO: Return a string to match the expected output
        raise NotImplementedError
