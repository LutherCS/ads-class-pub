'''
# Animals class
'''

#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Animal(ABC):
    '''Default animal'''
    @abstractmethod
    def __init__(self, spec, age, color):
        self._spec = spec
        self._age = age
        self._color = color

    @abstractmethod
    def sound(self):
        '''Make noise'''
        pass

    def __str__(self):
        '''Convert to string'''
        return "{} {} ({} yo)".format(self._color, self._spec, self._age)


class Bird(Animal):
    '''Bird class'''
    @abstractmethod
    def __init__(self, spec, age, color, flying):
        # Task 1a: call the constructor of the superclass
        # Task 1b: initialize private property _flying
        raise NotImplementedError


    def __str__(self):
        # Task 1c: if a bird is flying, return "Flying" + super().__str__()
        # Task 1d: if a bird if not a flying one, return "Non-flying " + super().__str__()
        raise NotImplementedError


class Mammal(Animal):
    '''Mammal class'''
    @abstractmethod
    def __init__(self, spec, age, color, habitat):
        # Task 2a: call the constructor of the superclass
        # Task 2b: initialize private property _habitat if habitat is "Land", "Sea", "Air", or "Tree"
        # Task 2c: raise a ValueError is the habitat value is invalid
        raise NotImplementedError


class Parrot(Bird):
    '''Parrot class'''
    def __init__(self, age, color, talking):
        # Task 3a: call the constructor of the superclass with "Parrot" as species and flying set to True
        # Task 3b: initialize private property _talking to talking
        raise NotImplementedError


    def sound(self):
        # Task 3c: if a parrot is talking, return "'Polly wants a cracker'"
        # Task 3d: if a parrot is talking, return "nothing" (word)
        raise NotImplementedError


class Penguin(Bird):
    '''Penguin class'''
    def __init__(self, age_, color_):
        super().__init__("Penguin", age, color, False)

    def sound(self):
        return "nothing"


class Canine(Mammal):
    '''Canine class'''
    @abstractmethod
    def __init__(self, spec, age, color, habitat):
        super().__init__(spec, age, color, habitat)


class Feline(Mammal):
    '''Feline class'''
    @abstractmethod
    def __init__(self, spec, age, color, habitat):
        super().__init__(spec, age, color, habitat)

    def sound(self):
        return "Meow!"


class Dog(Canine):
    '''Dog class'''
    def __init__(self, age_, color_):
        # Task 4a: call the constructor of the superclass with "Dog" as species and habitat set to "Land"
        raise NotImplementedError


    def sound(self):
        # Task 4b: return "Woof!"
        raise NotImplementedError


class HouseCat(Feline):
    '''HouseCat class'''
    def __init__(self, age, color):
        super().__init__("House Cat", age, color, "Land")


class BobCat(Feline):
    '''BobCat class'''
    def __init__(self, age, color, habitat):
        # Task 5a: call the constructor of the superclass with "Bobcat" as species
        raise NotImplementedError


    def __str__(self):
        # Task 5b: return string must include color, habitat, species, and age
        raise NotImplementedError
