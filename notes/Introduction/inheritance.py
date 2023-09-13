#!/usr/bin/env python3
"""Object-oriented programming: Inheritance"""
from functools import total_ordering
from abc import ABC, abstractmethod


@total_ordering
class Vehicle(ABC):
    """Class Vehicle"""

    @abstractmethod
    def __init__(self, year_param: int = 1923, color_param: str = "black") -> None:
        self._year = year_param
        self._color = color_param

    def get_year(self) -> int:
        return self._year

    def get_color(self) -> str:
        return self._color

    def set_color(self, new_value: str) -> None:
        self._color = new_value

    color = property(get_color, set_color)
    year = property(get_year)

    def paint(self, new_color):
        self._color = new_color

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vehicle):
            raise TypeError("The other thing is not a vehicle!")
        return self._color == other.color and self._year == other.year

    def __gt__(self, other: object):
        if not isinstance(other, Car):
            raise TypeError("The other thing is not a car!")
        return self._year > other.year

    def __str__(self) -> str:
        return f"It's a(n) {self.color} vehicle made in {self.year}"


class Car(Vehicle):
    def __init__(
        self, wheels_param: int = 4, year_param: int = 1923, color_param: str = "black"
    ) -> None:
        super().__init__(year_param, color_param)
        self._wheels = wheels_param

    def get_wheels(self) -> int:
        return self._wheels

    def set_wheels(self, new_value: int) -> None:
        self._wheels = new_value

    wheels = property(get_wheels, set_wheels)

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

    def __add__(self, other: object) -> "Car":
        if not isinstance(other, Car):
            raise TypeError("The other thing is not a car!")
        return Car(self._wheels + other.wheels, 2023, f"{self._color}-{other.color}")


class Boat(Vehicle):
    """Class Boat"""

    def __init__(
        self, year_param: int = 1923, color_param: str = "black", sail_param: int = 0
    ) -> None:
        super().__init__(year_param, color_param)
        self._sail = sail_param

    def __str__(self) -> str:
        return f"It's a boat with {self._sail} sails"


car1 = Car(4, 2003, "brown")
print(car1)

boat1 = Boat(2020, "white", 2)
print(boat1)

# v = Vehicle()
# print(v)
