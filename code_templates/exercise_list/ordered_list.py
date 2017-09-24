'''Ordered List code template'''

#!/usr/bin/env python3

import random
random.seed(160)


class Node:
    '''Node of a linked list'''
    def __init__(self, node_data):
        self._data = node_data
        self._next = None

    def get_data(self):
        '''Get node data'''
        return self._data

    def set_data(self, node_data):
        '''Set node data'''
        self._data = node_data

    data = property(get_data, set_data)

    def get_next(self):
        '''Get next node'''
        return self._next

    def set_next(self, next_node):
        '''Set next node'''
        self._next = next_node

    next = property(get_next, set_next)

    def __str__(self):
        '''Convert data to string'''
        return str(self._data)


class OrderedList:
    '''Ordered Linked List class'''
    def __init__(self):
        # _head is a pointer to a node, not a Node itself
        self._head = None
        self._count = 0

    def __getitem__(self, position):
        '''Get item by its position'''
        # TODO: Task 5: Implement a magic method __getitem__ magic method for the OrderedList class. It allows using a subscript (e.g. my_list[160]) to retrieve a specific item (node) of a list.
        raise NotImplementedError

    def __len__(self):
        '''Get list size'''
        return self._count

    def __str__(self):
        list_out = []
        current = self._head
        while current is not None:
            list_out.append(str(current.data))
            current = current.next
        return '[' + ", ".join(list_out) + ']'

    def is_empty(self):
        '''Check if the list is empty'''
        return self._head is None

    def size(self):
        '''Get list size'''
        return self._count

    def add(self, value):
        '''Add a new item to the list'''
        current = self._head
        prev = None
        stop = False
        while current is not None and not stop:
            if current.data > value:
                stop = True
            else:
                prev = current
                current = current.next
        new_node = Node(value)
        # We are at the begining of the list
        if prev is None:
            new_node.next = self._head
            self._head = new_node
        # We are in the list
        else:
            new_node.next = current
            prev.next = new_node
        self._count = self._count + 1

    def pop(self, position=None):
        '''Remove at item (last one by default) and get its value'''
        # TODO: Task 4: Implement method pop(position) of the OrderedList class to remove the last item and return its value
        raise NotImplementedError

    def append(self, value):
        '''Add a new item to the end of the list'''
        # TODO: Task 1: Implement method append(item) of the OrderedList class to add a new item to the end of the list
        raise NotImplementedError

    def insert(self, value, position):
        '''Insert a new item into the list'''
        # TODO: Task 2: Implement method insert(position, item) of the OrderedList class to insert a new item to the specified position
        raise NotImplementedError

    def search(self, value):
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

    def index(self, value):
        '''Return position of an item in the list'''
        # TODO: Task 3: Implement method index(item) of the OrderedList class to retrieve the position of an item in the list or -1 if not there
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
