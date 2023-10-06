#! /usr/env/bin python3
"""
Linked list

@author: Roman Yasinovskyy
@version: 2023.10
"""

from typing import Any


class Node:
    """Node of a linked list"""

    def __init__(self, init_data: Any) -> None:
        self._data = init_data
        self._next = None

    @property
    def data(self) -> Any:
        """Data inside the Node"""
        return self._data

    @data.setter
    def data(self, new_data) -> None:
        self._data = new_data

    @property
    def next(self) -> Any:
        """Link to the next Node"""
        return self._next

    @next.setter
    def next(self, new_next) -> None:
        self._next = new_next

    def __str__(self) -> str:
        return f"The data is {self._data} and the next node is {self._next}"

    def __repr__(self) -> str:
        return f"Node({self._data})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Node):
            return False
        return self.data == other.data


class LinkedList:
    """Class Linked list"""

    def __init__(self) -> None:
        self._size: int = 0
        self._head: Node | None = None

    @property
    def head(self):
        """Head of the list"""
        return self._head

    def __len__(self) -> int:
        return self._size

    def __bool__(self) -> bool:
        return self._head is not None

    def __str__(self) -> str:
        ll_str = []
        current = self.head
        while current:
            ll_str.append(current.data)
            current = current.next
        return " -> ".join([str(item) for item in ll_str])

    def add(self, new_node: Node | None) -> None:
        """Add a new node to the beginning of the list"""
        if not isinstance(new_node, Node):
            raise TypeError("Cannot add this")
        new_node.next = self._head
        self._head = new_node
        self._size += 1

    def append(self, new_node: Node | None) -> None:
        """Add a new node to the end of the list"""
        if not self.head:
            self._head = new_node
            self._size += 1
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        self._size += 1

    def insert(self, new_node: Node, pos: int) -> None:
        """Insert a new node in the middle of the list"""
        ...

    def search(self, value: Any) -> bool:
        """Search for a specific value"""
        current = self.head
        while current:
            if current.data == value:
                return True
            if isinstance(value, Node) and (value.data == current.data):
                return True
            current = current.next
        return False

    def index(self, value: Any) -> int:
        """Get position of the Node with a specific value"""
        pos = -1
        current = self.head
        while current:
            pos += 1
            if current.data == value:
                return pos
            current = current.next
        return -1

    def remove(self, node_to_remove: Node) -> None:
        """Remove a Node with a specific value"""
        current = self.head
        if current is None:
            return  # or raise ValueError("Not found")
        if current.data == node_to_remove.data:
            self._head = current.next
        while current.next and (current.next.data != node_to_remove.data):
            current = current.next
        if current.next:
            current.next = current.next.next
        # else:
        #     raise ValueError("Not found")

    def pop(self, pos: int) -> None:
        """Remove a Node at the specified position"""
        ...


def main():
    """Main"""
    print("Working with nodes")
    new_node = Node(13)
    print(new_node)
    new_node.data = "Fourteen"
    print(new_node)
    print("Working with lists")
    ll = LinkedList()
    print(bool(ll))
    print(len(ll))
    ll.add(new_node)
    print(len(ll))
    new_node = Node(70)
    ll.add(new_node)
    print(len(ll))
    print("Traversing the list")
    print(ll)
    ll.add(Node("Cat"))
    print(ll)
    print("Searching")
    print(ll.search(14))
    print(ll.search("Fourteen"))
    print(ll.search(Node("Fourteen")))
    print(ll.search("Dog"))
    print("Index of an item")
    print(ll.index(14))
    print(ll.index("Fourteen"))
    print(ll.index(Node("Fourteen")))
    print(ll.index("Dog"))
    print("Appending")
    ll.append(Node(42))
    print(ll)
    ll2 = LinkedList()
    ll2.append(Node(43))
    print(ll2)
    print("Removing")
    ll.remove(Node(70))
    print(ll)
    ll.remove(Node(70))
    print(ll)
    ll.remove(Node("Cat"))
    print(ll)
    ll.remove(Node(42))
    print(ll)
    ll.remove(Node("Fourteen"))
    print(ll)
    ll.remove(Node("Cat"))
    print(ll)
    # ll.add(Node(12))
    # print(ll)
    # ll.remove(Node(12))
    # print(ll)


if __name__ == "__main__":
    main()
