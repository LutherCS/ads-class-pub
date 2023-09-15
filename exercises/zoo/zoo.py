#!/usr/bin/env python3
"""
`zoo` implementation and driver

@authors:
"""

import random
from abc import ABC, abstractmethod

random.seed(42)


class Animal(ABC):
    """Class Animal"""

    @abstractmethod
    def __init__(self, spec_init: str, age_init: int, color_init: str):
        """Animal __init__"""
        self._spec = spec_init
        self._age = age_init
        self._color = color_init

    @abstractmethod
    def sound(self):
        """Make some noise"""
        pass

    def __str__(self) -> str:
        """__str__"""
        return f"{self._color} {self._spec} ({self._age} yo)"


class Bird(Animal):
    """Class Bird"""

    @abstractmethod
    def __init__(self, spec_init, age_init: int, color_init: str, flying_init: bool):
        """Bird __init__"""
        # TODO: Invoke __init__ of the superclass
        # TODO: Initialize self._flying
        ...

    def __str__(self) -> str:
        """___str__"""
        if self._flying:
            return "Flying " + super().__str__()
        else:
            return "Non-flying " + super().__str__()


class Mammal(Animal):
    """Class Mammal"""

    @abstractmethod
    def __init__(self, spec_init: str, age_init: int, color_init: str, habitat_init: str):
        """Mammal __init__"""
        # TODO: Invoke __init__ of the superclass
        # TODO: If habitat_init is "Land", "Sea", "Air" or "Tree", initialize self._habitat, else raise a ValueError
        ...


class Parrot(Bird):
    """Parrot class"""

    def __init__(self, age_init: int, color_init: str, talking_init: bool):
        """Parrot __init__"""
        # TODO: Invoke __init__ of the superclass
        # TODO: Initialize self._talking
        ...

    def sound(self) -> str:
        """Making Parrot noise"""
        if self._talking:
            return "Polly wants a cracker"
        else:
            return "nothing"


class Penguin(Bird):
    """Penguin class"""

    def __init__(self, age_init: int, color_init: str):
        """Penguin __init__"""
        super().__init__("Penguin", age_init, color_init, False)

    def sound(self) -> str:
        """Making Penguin noise"""
        return "nothing"


class Canine(Mammal):
    """Class Canine"""

    @abstractmethod
    def __init__(self, spec_init, age_init: int, color_init: str, habitat_init: str):
        """Canine __init__"""
        super().__init__(spec_init, age_init, color_init, habitat_init)


class Feline(Mammal):
    """Class Feline"""

    @abstractmethod
    def __init__(self, spec_init: str, age_init: int, color_init: str, habitat_init: str):
        super().__init__(spec_init, age_init, color_init, habitat_init)

    def sound(self) -> str:
        """Making Feline noise"""
        return "Meow!"


class Dog(Canine):
    """Class Dog"""

    def __init__(self, age_init: int, color_init: str):
        """Dog __init__"""
        # TODO: Invoke __init__ of the superclass. All dogs live on Land
        ...

    def sound(self) -> str:
        """Making Dog noise"""
        # TODO: All dogs say "Woof!"
        ...


class HouseCat(Feline):
    """Class HouseCat"""

    def __init__(self, age_init: int, color_init: str):
        """HouseCat __init__"""
        super().__init__("House Cat", age_init, color_init, "Land")


class BobCat(Feline):
    """Class BobCat"""

    def __init__(self, age_init: int, color_init: str, habitat_init: str):
        """BobCat __init__"""
        # TODO: Invoke __init__ of the superclass
        ...

    def __str__(self) -> str:
        """BobCat __str__"""
        # TODO: Return a string to match the expected output
        ...


def main():
    """Main function"""
    animal_classes = [Parrot, Penguin, Dog, HouseCat, BobCat]
    colors = ["White", "Black", "Red", "Green", "Blue", "Striped"]
    habitats = ["Land", "Sea", "Air", "Tree", "Campus"]
    random_true_false = [True, False]
    zoo = []
    zoo_size = 10
    for _ in range(zoo_size):
        spec = animal_classes[random.randint(0, 4)]
        age = random.randint(1, 10)
        color = random.choice(colors)
        habitat = random.choice(habitats)
        if spec == Parrot:
            new_animal = Parrot(age, color, random.choice(random_true_false))
        elif spec == Penguin:
            new_animal = Penguin(age, color)
        elif spec == Dog:
            new_animal = Dog(age, color)
        elif spec == HouseCat:
            new_animal = HouseCat(age, color)
        else:
            try:
                new_animal = BobCat(age, color, habitat)
            except ValueError as value_error:
                print(habitat + " is " + str(value_error))
                continue
        zoo.append(new_animal)
    print(f"There are {len(zoo)} animals in the zoo")
    for animal in zoo:
        print(f"{animal} says {animal.sound()}")


if __name__ == "__main__":
    main()
