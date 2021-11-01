#!/usr/bin/env python3
"""
`sorting` driver

@authors: Roman Yasinovskyy
@version: 2021.11
"""

import pathlib
import sys

sys.path.append(f"{pathlib.Path(__file__).parents[2]}/")
from notes.sorting.sorting_algs import (
    bubble_sort,
    select_sort,
    insert_sort,
    shell_sort,
    merge_sort_opt,
    quick_sort,
    heap_sort,
)


def main():
    print("Sorting a list")
    lst_0 = [594, 850, 281, 952, 129, 348, 264, 972, 598, 758]
    print("---Bubble Sort---")
    lst_to_sort = lst_0[:]
    print(lst_to_sort)
    bubble_sort(lst_to_sort, show_details=True)
    print(lst_to_sort)
    print("---Insertion Sort---")
    lst_to_sort = lst_0[:]
    print(lst_to_sort)
    insert_sort(lst_to_sort, show_details=True)
    print(lst_to_sort)
    print("---Selection Sort---")
    lst_to_sort = lst_0[:]
    print(lst_to_sort)
    select_sort(lst_to_sort, show_details=True)
    print(lst_to_sort)
    print("---Shell Sort---")
    lst_to_sort = lst_0[:]
    print(lst_to_sort)
    shell_sort(lst_to_sort, show_details=True)
    print(lst_to_sort)
    print("---Merge Sort---")
    lst_to_sort = lst_0[:]
    print(lst_to_sort)
    merge_sort_opt(lst_to_sort, show_details=True)
    print(lst_to_sort)
    print("---Quick Sort---")
    lst_to_sort = lst_0[:]
    print(lst_to_sort)
    quick_sort(lst_to_sort, show_details=True)
    print(lst_to_sort)
    print("---Heap Sort---")
    lst_to_sort = lst_0[:]
    print(lst_to_sort)
    heap_sort(lst_to_sort, show_details=True)
    print(lst_to_sort)


if __name__ == "__main__":
    main()
