#!/usr/bin/env python3
"""
`orderedlists` implementation and driver

@authors: Roman Yasinovskyy
@version: 2021.9
"""

from random import randint, seed
from typing import Any, Optional, Union


class Node:
    """Node of a linked list"""

    def __init__(self, init_data: Any) -> None:
        """Initializer"""
        self._data = init_data
        self._next: Optional["Node"] = None

    def get_data(self) -> Any:
        """Get node data"""
        return self._data

    def set_data(self, new_data: Any) -> None:
        """Set node data"""
        self._data = new_data

    data = property(get_data, set_data)

    def get_next(self) -> Union["Node", None]:
        """Get next node"""
        return self._next

    def set_next(self, new_next: "Node") -> None:
        """Set next node"""
        self._next = new_next

    next = property(get_next, set_next)

    def __str__(self) -> str:
        """Convert data to string"""
        return str(self._data)


class OrderedList:
    """Ordered Linked List class"""

    def __init__(self):
        """Initializer"""
        self._head = None
        self._count = 0

    def __getitem__(self, position: int) -> Any:
        """Get item by its position

        :param position: position of an item to get
        :return: item's data
        :raise: `IndexError` if the list is empty
        :raise: `IndexError` if the index is too large
        :raise: `ValueError` if the index is negative
        """
        # TODO: Implement this method
        ...

    def __len__(self) -> int:
        """Get list size

        :return: number of items on the list
        """
        return self._count

    def __str__(self) -> str:
        """List as a string

        :return: list as a string
        """
        list_out = []
        current = self._head
        while current:
            list_out.append(str(current.data))
            current = current.next
        return "[" + ", ".join(list_out) + "]"

    def is_empty(self) -> bool:
        """Check if the list is empty

        :return: `True` if the list is empty, `False` otherwise
        """
        return self._head is None

    def size(self) -> int:
        """Get list size

        :return: number of items on the list
        """
        return self._count

    def add(self, value: Any) -> None:
        """Add a new item to the list

        :param value: value to add to the list
        """
        # TODO: Implement this method
        ...

    def pop(self, position: int = None) -> Any:
        """Remove at item (last one by default) and get its value

        :param position: position to pop
        :return: value of the popped item
        :raise: `IndexError` if the list is empty
        :raise: `IndexError` if the index is too large
        :raise: `ValueError` if the index is negative
        """
        # TODO: Implement this method
        ...

    def append(self, value: Any) -> None:
        """Add a new item to the end of the list

        :param value: value to add to the list
        """
        # TODO: Implement this method
        ...

    def insert(self, position: int, value: Any) -> None:
        """Insert a new item into the list

        :param position: position to insert at. *Ignored*
        :param value: value to add to the list
        """
        # TODO: Implement this method
        ...

    def search(self, value: Any) -> bool:
        """Search for an item in the list

        :param value: value to find
        :return: `True` if the value is in the list, `False` otherwise
        """
        current = self._head
        while current:
            if current.data == value:
                return True
            if current.data > value:
                return False
            current = current.next
        return False

    def index(self, value: Any) -> int:
        """Return position of an item in the list

        :param value: value to find
        :return: first position of the value, -1 if not found
        """
        # TODO: Implement this method
        ...


def print_list_status(lst):
    """Print list status"""
    print(f"The list: {lst}")
    print(f"List is empty: {lst.is_empty()}")
    print(f"Size of the list: {lst.size()}")
    print(f"__len__ of the list: {len(lst)}")
    print(f"160 is in the list: {lst.search(160)}")
    print(f"Position of 160 in the list: {lst.index(160)}")
    position = randint(0, len(lst))
    try:
        print(f"lst[{position}] is ", end="")
        print(f"{lst[position]}")
    except (IndexError, ValueError) as err:
        print(err)
    print("-----")


def main():
    """Main function"""
    print("Working with ordered linked lists")
    ord_lst = OrderedList()
    print_list_status(ord_lst)
    print("Adding 160 to the list")
    ord_lst.add(160)
    print_list_status(ord_lst)
    print("Adding 5 random values to the list")
    for _ in range(5):
        ord_lst.append(randint(100, 200))
    print_list_status(ord_lst)
    print("Inserting 5 random values to the list")
    for _ in range(5):
        position = randint(0, len(ord_lst) - 1)
        ord_lst.insert(position, randint(100, 200))
    print_list_status(ord_lst)
    print("Popping 5 items from random positions")
    for _ in range(5):
        position = randint(0, len(ord_lst) - 1)
        print(f"Popped {ord_lst.pop(position)}")
    print_list_status(ord_lst)
    print("Popping 5 last items")
    for _ in range(5):
        print(f"Popped {ord_lst.pop()}")
    print_list_status(ord_lst)


if __name__ == "__main__":
    seed(42)
    main()
