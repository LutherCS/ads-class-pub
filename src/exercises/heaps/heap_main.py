#!/usr/bin/env python3
"""
`heaps` driver

@authors: Roman Yasinovskyy
@version: 2021.4
"""

from heapq import heapify

from heaps import BinaryHeapMax


def main():
    """Main function"""
    print("Working with heaps")
    
    print("Turning a list into a min heap")
    lst = [55, 73, 17, 41, 83, 89, 7, 28, 10, 69]
    print(f"Original list : {lst}")
    heapify(lst)
    print(f"Heapified data: {lst}")

    print("Turning a list into a max heap")
    lst = [69, 10, 28, 7, 89, 83, 41, 17, 73, 55]
    print(f"Original list : {lst}")
    max_heap = BinaryHeapMax()
    max_heap.heapify(lst)
    print(f"Heapified data: {max_heap}")


if __name__ == "__main__":
    main()
