#! /usr/env/bin python3

from typing import Any


class Node:
    def __init__(self, init_data: Any) -> None:
        self._data = init_data
        self._next = None

    @property
    def data(self) -> Any:
        return self._data

    @data.setter
    def data(self, new_data) -> None:
        self._data = new_data

    @property
    def next(self) -> Any:
        return self._next

    @next.setter
    def next(self, new_next) -> None:
        self._next = new_next

    def __str__(self) -> str:
        return f"The data is {self._data} and the next node is {self._next}"

    def __repr__(self) -> str:
        return f"Node({self._data})"


class LinkedList:
    def __init__(self) -> None:
        self._size = 0
        self._head = None

    def __len__(self) -> int:
        return self._size

    def size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        # return self._size == 0
        return self._head is None

    def add(self, new_node: Node) -> None:
        if not isinstance(new_node, Node):
            raise TypeError("Cannot add this")
        new_node.next = self._head
        self._head = new_node
        self._size += 1

    def __str__(self) -> str:
        pass


def main():
    print("Working with nodes")
    new_node = Node(13)
    print(new_node)
    new_node.data = "Fourteen"
    print(new_node)
    print("Working with lists")
    ll = LinkedList()
    print(ll.size())
    ll.add(new_node)
    print(ll.size())
    new_node = Node(70)
    ll.add(new_node)
    print(ll.size())


if __name__ == "__main__":
    main()
