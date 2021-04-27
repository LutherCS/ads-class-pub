#!/usr/bin/env python3
"""
`stack` implementation

@authors: Roman Yasinovskyy
@version: 2021.4
"""

from queue import SimpleQueue
from typing import Any


class StackError(Exception):
    """Stack errors"""

    def __init__(self, *args, **kwargs):
        """Initializer"""
        Exception.__init__(self, *args, **kwargs)


class Stack:
    """
    LIFO data structure

    Items are added and removed on the same end of the collection
    """

    def __init__(self):
        """Initialize a stack using queue.SimpleQueue"""
        self.items = SimpleQueue()

    def push(self, item: Any) -> None:
        """
        Add a new item to stack

        @param item: a new item to push onto the stack
        """
        raise NotImplementedError

    def pop(self) -> Any:
        """
        Remove an item from the stack

        @return the top element of the stack
        @raise StackError is the stack is empty
        """
        raise NotImplementedError

    def peek(self) -> Any:
        """
        Look at the top item without removing it

        @return the top element of the stack
        @raise StackError is the stack is empty
        """
        raise NotImplementedError

    def __bool__(self) -> bool:
        """
        Evaluate the stack

        @return False if the stack is empty, True otherwise
        """
        raise NotImplementedError

    def __len__(self) -> int:
        """
        Return the number of items in the stack

        @return number of items in the stack (0 if the stack is empty)
        """
        raise NotImplementedError
