#!/usr/bin/env python3
"""Linked list implementation"""


from typing import Any


class Node:
    def __init__(self, init_value: Any) -> None:
        self._value = init_value
        self._next = None

    def get_data(self) -> Any:
        return self._value

    def set_data(self, new_data) -> None:
        self._value = new_data

    data = property(get_data, set_data)

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, new_next):
        self._next = new_next

    def __str__(self):
        return str(self._value)


class LinkedList:
    def __init__(self):
        self._head = None
        # self._tail = None
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def __str__(self) -> str:
        # list_str = '['
        # current = self._head

        # while current:
        #     list_str += str(current)
        #     if current.next:
        #         list_str += ', '
        #     current = current.next
        # list_str += ']'
        # return list_str
        my_list = []
        current = self._head
        while current:
            my_list.append(current.data)
            current = current.next
        return f"[{', '.join(my_list)}]"

    def is_empty(self) -> bool:
        return self._head is None

    def size(self) -> int:
        # return self._size
        return self.__len__()

    def add(self, new_node: Node) -> None:
        new_node.next = self._head
        self._head = new_node
        self._size += 1

    def search(self, value) -> bool:
        current = self._head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

    def index(self, value) -> int:
        """
        return index of an element

        useful method
        """
        idx = -1
        current = self._head
        while current:
            idx += 1
            if current.data == value:
                return idx
            current = current.next
        return -1

    def append(self, new_node: object) -> None:
        """
        append a new node to the list

        takes Node object as a parameter

        raises a ValueError on Sundays
        """
        if not self._head:
            self._head = new_node
            self._size += 1
            return
        current = self._head
        while current.next:
            current = current.next
        current.next = new_node
        self._size += 1

    def insert(self, pos: int, new_node: Node) -> None:
        current = self._head
        idx = 0
        if pos <= 0:
            self.add(new_node)
            return
        if pos > self._size:
            self.append(new_node)
            return
        while idx < pos - 1:
            idx += 1
            current = current.next

        new_node.next = current.next
        current.next = new_node
        self._size += 1

    def pop(self, idx=None) -> Any:
        if not self._head:
            raise Exception("Cannot pop from an empty list")
        if idx == None:
            idx = self._size
        if idx < 0:
            raise ValueError("Negative")
        current = self._head
        prev = None
        cur_idx = 0
        while current.next and cur_idx < idx:
            prev = current
            current = current.next
            cur_idx += 1
        result = current.data
        if prev:
            prev.next = current.next
        else:
            self._head = current.next
        self._size -= 1
        return result


def main():
    # print('Working with nodes')
    # n = Node('A')
    # print(n.data)
    # print(n.next)
    # print(n)

    # m = Node('B')
    # n.next = m
    # print(n.next)

    print("Working with lists")
    ll = LinkedList()
    print(ll.size())  # 0
    # print(type(ll))  # LinkedList
    print("Printing a list")
    # print(ll)
    ll.add(Node("Q"))
    # print(ll)  # [Q]
    ll.add(Node("A"))
    # print(ll)  # [A, Q]
    ll.add(Node("D"))
    # print(ll)  # [D, A, Q]
    # print(len(ll))
    # print(ll.search('Z'))
    print(ll)  # [D, A, Q]
    # print(len(ll))
    # print(ll.index('Q'))  # 0
    # print(ll)  # [D, A, Q]
    # print(len(ll))
    print(ll.index("Z"))  # -1
    # print(ll)  # [D, A, Q]
    # print(len(ll))
    print("Appending a new node")
    ll = LinkedList()
    ll.append(Node("R"))
    ll.append(Node("Q"))
    ll.append(Node("T"))
    ll.append(Node("S"))
    print(ll)  # [R, Q, T, S]
    # print('Inserting a new node')
    # ll.insert(0, Node('K'))
    # print(ll)  # [K, D, A, Q]
    # print(len(ll))  # 4
    # ll.insert(2, Node('M'))
    # print(ll)  # [K, D, M, A, Q]
    # print(len(ll))  # 5
    # print(ll)  # []
    # print(len(ll))  # 4
    # print(ll.pop(1))  # Q
    # print(ll)  # [R, T, S]
    # print(len(ll))  # 3
    # print(ll.pop())  # S
    # print(ll)  # [R, T]
    # print(len(ll))  # 2
    # print('---')
    # print(ll.pop(0))  # R
    # print(ll)  # [T]
    # print(len(ll))  # 1


if __name__ == "__main__":
    main()
