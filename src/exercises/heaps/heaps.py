#!/usr/bin/env python3
"""
`heaps` implementation

@author:
"""


from typing import Any, List


class BinaryHeapMax:
    """Heap class implementation"""

    def __init__(self):
        """Initializer"""
        self.heap: List[Any] = []
        self.size = 0

    def perc_up(self, cur_idx: int):
        """Move a node up"""
        raise NotImplementedError

    def perc_down(self, cur_idx: int):
        """Move a node down"""
        raise NotImplementedError

    def insert(self, item: Any):
        """Add a new item"""
        raise NotImplementedError

    def delete(self) -> Any:
        """Remove an item from the heap"""
        raise NotImplementedError

    def heapify(self, not_a_heap: List[Any]) -> None:
        """Turn a list into a heap"""
        raise NotImplementedError

    def __len__(self) -> int:
        """Get heap size"""
        return self.size

    def __str__(self) -> str:
        """Heap as a string """
        return str(self.heap)
