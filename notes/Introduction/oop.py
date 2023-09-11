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
car8.year = 1923
print(f"Our {car8.color} car was made in {car8.year} and has {car8.wheels} wheels")


class Car:
    def __init__(self) -> None:
        self.wheels = 4
        self.year = 1923
        self.color = "black"


car9 = Car()
print(f"Our {car9.color} car was made in {car9.year} and has {car9.wheels} wheels")
car9.year = 2023
print(f"Our {car9.color} car was made in {car9.year} and has {car9.wheels} wheels")


class Car:
    def __init__(
        self, wheels_param: int = 4, year_param: int = 1923, color_param: str = "black"
    ) -> None:
        self.wheels = wheels_param
        self.year = year_param
        self.color = color_param


car10 = Car()
print(f"Our {car10.color} car was made in {car10.year} and has {car10.wheels} wheels")
car11 = Car(1, 2023, "rainbow")
print(f"Our {car11.color} car was made in {car11.year} and has {car11.wheels} wheels")
car12 = Car(2, 2020)
print(f"Our {car12.color} car was made in {car12.year} and has {car12.wheels} wheels")
car13 = Car(3, "white")
print(f"Our {car13.color} car was made in {car13.year} and has {car13.wheels} wheels")
car14 = Car(wheels_param=3, color_param="white")
print(f"Our {car14.color} car was made in {car14.year} and has {car14.wheels} wheels")


class Car:
    def __init__(self, wheels_param: int, year_param: int, color_param: str) -> None:
        self.wheels = wheels_param
        self.year = year_param
        self.color = color_param


# car15 = Car()
# print(f"Our {car15.color} car was made in {car15.year} and has {car15.wheels} wheels")


class Car:
    def __init__(
        self, wheels_param: int = 4, year_param: int = 1923, color_param: str = "black"
    ) -> None:
        self._wheels = wheels_param
        self._year = year_param
        self._color = color_param

    def get_wheels(self) -> int:
        return self._wheels

    def get_year(self) -> int:
        return self._year

    def get_color(self) -> str:
        return self._color


car15 = Car(wheels_param=3, color_param="white")
print(
    f"Our {car15._color} car was made in {car15._year} and has {car15._wheels} wheels"
)
car15._year = 2023
print(
    f"Our {car15._color} car was made in {car15._year} and has {car15._wheels} wheels"
)
print(
    f"Our {car15.get_color()} car was made in {car15.get_year()} and has {car15.get_wheels()} wheels"
)


class Car:
    def __init__(
        self, wheels_param: int = 4, year_param: int = 1923, color_param: str = "black"
    ) -> None:
        self._wheels = wheels_param
        self._year = year_param
        self._color = color_param

    def get_wheels(self) -> int:
        return self._wheels

    def get_year(self) -> int:
        return self._year

    def get_color(self) -> str:
        return self._color

    def set_wheels(self, new_value: int) -> None:
        self._wheels = new_value

    def set_color(self, new_value: str) -> None:
        self._color = new_value

    wheels = property(get_wheels, set_wheels)
    color = property(get_color, set_color)
    year = property(get_year)


car16 = Car()
print(
    f"Our {car16.get_color()} car was made in {car16.get_year()} and has {car16.get_wheels()} wheels"
)
car16.set_color("green")
print(
    f"Our {car16.get_color()} car was made in {car16.get_year()} and has {car16.get_wheels()} wheels"
)

car17 = Car()
print(f"Our {car17.color} car was made in {car17.year} and has {car17.wheels} wheels")
# car17.year= 2023
# print(f"Our {car17.color} car was made in {car17.year} and has {car17.wheels} wheels")
car17._year = 2023
print(f"Our {car17.color} car was made in {car17.year} and has {car17.wheels} wheels")


class Car:
    def __init__(
        self, wheels_param: int = 4, year_param: int = 1923, color_param: str = "black"
    ) -> None:
        self._wheels = wheels_param
        self._year = year_param
        self._color = color_param

    def get_wheels(self) -> int:
        return self._wheels

    def get_year(self) -> int:
        return self._year

    def get_color(self) -> str:
        return self._color

    def set_wheels(self, new_value: int) -> None:
        self._wheels = new_value

    def set_color(self, new_value: str) -> None:
        self._color = new_value

    wheels = property(get_wheels, set_wheels)
    color = property(get_color, set_color)
    year = property(get_year)

    def paint(self, new_color):
        self._color = new_color


car20 = Car()
print(f"Our {car20.color} car was made in {car20.year} and has {car20.wheels} wheels")
car20.paint("green")
print(f"Our {car20.color} car was made in {car20.year} and has {car20.wheels} wheels")

from functools import total_ordering


@total_ordering
class Car:
    def __init__(
        self, wheels_param: int = 4, year_param: int = 1923, color_param: str = "black"
    ) -> None:
        self._wheels = wheels_param
        self._year = year_param
        self._color = color_param

    def get_wheels(self) -> int:
        return self._wheels

    def get_year(self) -> int:
        return self._year

    def get_color(self) -> str:
        return self._color

    def set_wheels(self, new_value: int) -> None:
        self._wheels = new_value

    def set_color(self, new_value: str) -> None:
        self._color = new_value

    wheels = property(get_wheels, set_wheels)
    color = property(get_color, set_color)
    year = property(get_year)

    def paint(self, new_color):
        self._color = new_color

    def __str__(self) -> str:
        return (
            f"It's a(n) {self.color} car with {self.wheels} wheels made in {self.year}"
        )

    def __repr__(self) -> str:
        return f"Car({self._wheels}, {self._year}, '{self._color}')"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Car):
            raise TypeError("The other thing is not a car!")
        return (
            self._wheels == other.wheels
            and self._color == other.color
            and self._year == other.year
        )

    def __gt__(self, other: object):
        if not isinstance(other, Car):
            raise TypeError("The other thing is not a car!")
        return self._year > other.year

    def __add__(self, other: object) -> "Car":
        if not isinstance(other, Car):
            raise TypeError("The other thing is not a car!")
        return Car(self._wheels + other.wheels, 2023, f"{self._color}-{other.color}")


car21 = Car()
print(f"Our {car21.color} car was made in {car21.year} and has {car21.wheels} wheels")
print(car21)

garage = [car21]
print(garage)
print([str(car) for car in garage])

car22 = eval(repr(car21))
print(car22)
print(car21 == car22)

car23 = (4, 1923, "black")
try:
    print(car21 == car23)
except TypeError as t_err:
    print(t_err)

car24 = Car(8, 2020, "white")
print(car24)
print(car22 > car24)

print(car22 + car24)

print("Done!")
