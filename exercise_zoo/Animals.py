'''
# Animals class #
Complete the code to simulate a zoo

WARNING: This file compiles with errors without your modifications
'''
#!/usr/bin/env python3
#encoding: UTF-8

from abc import ABC, abstractmethod


class Animal(ABC):
    '''Default animal'''
    @abstractmethod
    def __init__(self, spec_, age_, color_):
        self._spec = spec_
        self._age = age_
        self._color = color_

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
    def __init__(self, spec_, age_, color_, flying_):
        # Task 1a: call the constructor of the superclass
        # Task 1b: initialize private property _flying


    def __str__(self):
        # Task 1c: if a bird is flying, return "Flying" + super().__str__()
        # Task 1d: if a bird if not a flying one, return "Non-flying " + super().__str__()


class Mammal(Animal):
    '''Mammal class'''
    @abstractmethod
    def __init__(self, spec_, age_, color_, habitat_):
        # Task 2a: call the constructor of the superclass
        # Task 2b: initialize private property _habitat if habitat_ is "Land", "Sea", "Air", or "Tree"
        # Task 2c: raise a ValueError is the habitat_ value is invalid


class Parrot(Bird):
    '''Parrot class'''
    def __init__(self, age_, color_, talking_):
        # Task 3a: call the constructor of the superclass with "Parrot" as species and flying set to True
        # Task 3b: initialize private property _talking to talking_


    def sound(self):
        # Task 3c: if a parrot is talking, return "'Polly wants a cracker'"
        # Task 3d: if a parrot is talking, return "nothing" (word)


class Penguin(Bird):
    '''Penguin class'''
    def __init__(self, age_, color_):
        super().__init__("Penguin", age_, color_, False)

    def sound(self):
        return "nothing"


class Canine(Mammal):
    '''Canine class'''
    @abstractmethod
    def __init__(self, spec_, age_, color_, habitat_):
        super().__init__(spec_, age_, color_, habitat_)


class Feline(Mammal):
    '''Feline class'''
    @abstractmethod
    def __init__(self, spec_, age_, color_, habitat_):
        super().__init__(spec_, age_, color_, habitat_)

    def sound(self):
        return "Meow!"


class Dog(Canine):
    '''Dog class'''
    def __init__(self, age_, color_):
        # Task 4a: call the constructor of the superclass with "Dog" as species and habitat set to "Land"


    def sound(self):
        # Task 4b: return "Woof!"


class HouseCat(Feline):
    '''HouseCat class'''
    def __init__(self, age_, color_):
        super().__init__("House Cat", age_, color_, "Land")


class BobCat(Feline):
    '''BobCat class'''
    def __init__(self, age_, color_, habitat_):
        # Task 5a: call the constructor of the superclass with "Bobcat" as species


    def __str__(self):
        # Task 5b: return string must include color, habitat, species, and age
