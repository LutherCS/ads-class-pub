#!/usr/bin/env python3
"""Object-oriented programming"""
# tuple
car1 = (3, "green-yellow", 2008)
print(f"Our {car1[1]} car was made in {car1[2]} and has {car1[0]} wheels")

# named tuple
from collections import namedtuple

Car = namedtuple("Car", ["wheels", "color", "year"])
car2 = Car(wheels=4, color="silver", year=2023)
print(f"Our {car2[1]} car was made in {car2[2]} and has {car2[0]} wheels")
print(f"Our {car2.color} car was made in {car2.year} and has {car2.wheels} wheels")
car3 = Car(4, "black", year=1930)
print(f"Our {car3.color} car was made in {car3.year} and has {car3.wheels} wheels")
car4 = Car("white", 1930, 4)
print(f"Our {car4.color} car was made in {car4.year} and has {car4.wheels} wheels")
car5 = Car(color="white", year=3930, wheels=4)
print(f"Our {car5.color} car was made in {car5.year} and has {car5.wheels} wheels")

# dictionary
car6 = {"wheels": 7, "year": 2015, "color": "yellow"}
print(
    f"Our {car6['color']} car "
    + f"was made in {car6['year']} and "
    + f"has {car6['wheels']} wheels"
)
car7 = {"wheels": 8, "year": 2020}
print(
    f"Our {car7.get('color', 'red')} car "
    + f"was made in {car7.get('year', 1861)} and "
    + f"has {car7.get('wheels', 5)} wheels"
)

from dataclasses import dataclass


@dataclass
class Car:
    """dataclass Car"""

    wheels: int
    color: str
    year: int


car8 = Car(5, "pink", "2023")
print(f"Our {car8.color} car was made in {car8.year} and has {car8.wheels} wheels")
