#!/usr/bin/env python3
"""
Exercise `orderedlists` driver

@authors: Roman Yasinovskyy
@version: 2021.2
"""


from random import seed, randint
from orderedlists_classes import OrderedList


def print_list_status(lst):
    """Print list status"""
    print("The list: {}".format(lst))
    print("List is empty: {}".format(lst.is_empty()))
    print("Size of the list: {}".format(lst.size()))
    print("160 is in the list: {}".format(lst.search(160)))
    print("Position of 160 in the list: {}".format(lst.index(160)))
    position = min(len(lst) - 1, randint(0, len(lst)))
    try:
        print("Item at position {}: {}".format(position, lst[position]))
    except Exception as error:
        print(error)
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
        print("Popped {}".format(ord_lst.pop(position)))
    print_list_status(ord_lst)
    print("Popping 5 last items")
    for _ in range(5):
        print("Popped {}".format(ord_lst.pop()))
    print_list_status(ord_lst)


if __name__ == "__main__":
    seed(42)
    main()
