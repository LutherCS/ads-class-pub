'''
zoo import statement
'''
name = "zoo"

from .zoo import Animal, Bird, Mammal, Parrot, Penguin, Canine, Feline, Dog, HouseCat, BobCat

__all__ = ['Animal', 'Bird', 'Mammal', 'Parrot', 'Penguin', 'Canine', 'Feline', 'Dog', 'HouseCat', 'BobCat']
