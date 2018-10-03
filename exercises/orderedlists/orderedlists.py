'''Ordered List code template'''

#!/usr/bin/env python3

import random
import typing
random.seed(160)


class Node:
    '''Node of a linked list'''
    def __init__(self, init_data: typing.Any):
        self._data = init_data
        self._next = None

    def get_data(self):
        '''Get node data'''
        return self._data

    def set_data(self, new_data: typing.Any) -> None:
        '''Set node data'''
        self._data = new_data

    data = property(get_data, set_data)

    def get_next(self):
        '''Get next node'''
        return self._next

    def set_next(self, new_next: object) -> None:
        '''Set next node'''
        self._next = new_next

    next = property(get_next, set_next)

    def __str__(self) -> str:
        '''Convert data to string'''
        return str(self._data)


class OrderedList:
    '''Ordered Linked List class'''
    def __init__(self):
        self._head = None
        self._count = 0

    def __getitem__(self, position: int):
        '''Get item by its position'''
        raise NotImplementedError

    def __len__(self) -> int:
        '''Get list size'''
        return self._count

    def __str__(self) -> str:
        list_out = []
        current = self._head
        while current is not None:
            list_out.append(str(current.data))
            current = current.next
        return '[' + ', '.join(list_out) + ']'

    def is_empty(self) -> bool:
        '''Check if the list is empty'''
        return self._head is None

    def size(self) -> int:
        '''Get list size'''
        return self._count

    def add(self, value: typing.Any) -> None:
        '''Add a new item to the list'''
        raise NotImplementedError

    def pop(self, position: int=None):
        '''Remove at item (last one by default) and get its value'''
        if position is None:
            position = self._count
        if self._count == 0:
            raise Exception('Cannot pop from an empty list')
        if position < 0:
            raise Exception('Invalid position for popping an item')
        current = self._head
        prev = None
        cur_ind = 0
        while current.next is not None and cur_ind < position:
            prev = current
            current = current.next
            cur_ind = cur_ind + 1
        result = current.data
        self._count = self._count - 1
        if prev is None:  # popping the first item
            self._head = current.next
        else:
            prev.next = current.next
        return result

    def append(self, value: typing.Any) -> None:
        '''Add a new item to the end of the list'''
        raise NotImplementedError

    def insert(self, position: int, value: typing.Any) -> None:
        '''Insert a new item into the list'''
        raise NotImplementedError

    def search(self, value: typing.Any) -> bool:
        '''Search for an item in the list'''
        current = self._head
        while current is not None:
            if current.data == value:
                return True
            elif current.data > value:
                return False
            else:
                current = current.next
        return False

    def index(self, value: typing.Any) -> int:
        '''Return position of an item in the list'''
        raise NotImplementedError


def print_list_status(lst):
    '''Print list status'''
    print('The list: {}'.format(lst))
    print('List is empty: {}'.format(lst.is_empty()))
    print('Size of the list: {}'.format(lst.size()))
    print('160 is in the list: {}'.format(lst.search(160)))
    print('Position of 160 in the list: {}'.format(lst.index(160)))
    position = min(len(lst)-1, random.randint(0, len(lst)))
    try:
        print('Item at position {}: {}'.format(position, lst[position]))
    except Exception as error:
        print(error)
    print('-----')


def main():
    '''Main function'''
    print('Working with ordered linked lists')
    ord_lst = OrderedList()
    print_list_status(ord_lst)
    print('Adding 160 to the list')
    ord_lst.add(160)
    print_list_status(ord_lst)
    print('Adding 5 random values to the list')
    for _ in range(5):
        ord_lst.append(random.randint(100, 200))
    print_list_status(ord_lst)
    print('Inserting 5 random values to the list')
    for _ in range(5):
        position = random.randint(0, len(ord_lst)-1)
        ord_lst.insert(position, random.randint(100, 200))
    print_list_status(ord_lst)
    print('Popping 5 items from random positions')
    for _ in range(5):
        position = random.randint(0, len(ord_lst)-1)
        print('Popped {}'.format(ord_lst.pop(position)))
    print_list_status(ord_lst)
    print('Popping 5 last items')
    for _ in range(5):
        print('Popped {}'.format(ord_lst.pop()))
    print_list_status(ord_lst)


if __name__ == '__main__':
    main()
