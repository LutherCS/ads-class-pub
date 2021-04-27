#!/usr/bin/env python3
"""
`stack` testing

@authors: Roman Yasinovskyy
@version: 2021.4
"""

import importlib
import pathlib
import sys

import pytest

try:
    importlib.util.find_spec(".".join(pathlib.Path(__file__).parts[-3:-1]), "src")
except ModuleNotFoundError:
    sys.path.append(f"{pathlib.Path(__file__).parents[3]}/")
finally:
    from src.projects.interview import Stack, StackError


def test_init():
    """Testing init"""
    the_stack = Stack()
    assert isinstance(the_stack, Stack)


@pytest.mark.parametrize("items", [[], [(1, "a")], ["a", "b"], [1, 2, 3]])
def test_push(items):
    """Testing push"""
    the_stack = Stack()
    for item in items:
        the_stack.push(item)
    assert isinstance(the_stack, Stack)


@pytest.mark.parametrize(
    "items, result",
    [([None], None), ([(1, "a")], (1, "a")), (["a", "b"], "b"), ([1, 2, 3], 3)],
)
def test_pop(items, result):
    """Testing push"""
    the_stack = Stack()
    for item in items:
        the_stack.push(item)
    assert the_stack.pop() == result


@pytest.mark.parametrize("items", [[], [(1, "a")], ["a", "b"], [1, 2, 3]])
def test_pop_error(items):
    """Testing pop error"""
    the_stack = Stack()
    for item in items:
        the_stack.push(item)
    with pytest.raises(StackError) as error:
        for _ in range(999):
            the_stack.pop()
    assert error.value.args[0] == "Cannot pop from an empty stack"


@pytest.mark.parametrize(
    "items, result", [([(1, "a")], (1, "a")), (["a", "b"], "b"), ([1, 2, 3], 3)]
)
def test_peek(items, result):
    """Testing peek"""
    the_stack = Stack()
    for item in items:
        the_stack.push(item)
    assert the_stack.peek() == result


def test_peek_error():
    """Testing peek error"""
    the_stack = Stack()
    with pytest.raises(StackError) as error:
        the_stack.peek()
    assert error.value.args[0] == "Nothing to see here, the stack is empty"


@pytest.mark.parametrize(
    "items, n, result",
    [
        ([], 0, False),
        ([(1, "a")], 1, False),
        ([(1, "a")], 0, True),
        (["a", "b"], 2, False),
        (["a", "b"], 1, True),
        ([1, 2, 3], 3, False),
        ([1, 2, 3], 2, True),
    ],
)
def test_bool(items, n, result):
    """Testing __bool__"""
    the_stack = Stack()
    for item in items:
        the_stack.push(item)
    for _ in range(n):
        the_stack.pop()
    assert bool(the_stack) == result


@pytest.mark.parametrize(
    "items, size", [([], 0), ([(1, "a")], 1), (["a", "b"], 2), ([1, 2, 3], 3)]
)
def test_len(items, size):
    """Testing __len__"""
    the_stack = Stack()
    for item in items:
        the_stack.push(item)
    assert len(the_stack) == size


@pytest.mark.parametrize(
    "items, size",
    [
        ([(1, "a"), (2, "b")], 0),
        (["a", "b"], 0),
        ([1, 2, 3], 1),
        (["a", "b", "c"], 1),
        ([1, 2, 3, False], 2),
        ([True, False, True, False], 2),
        ([None, True, 1, "a", (1, "a")], 3),
        (["a", "b", "c", 1, 2, 3], 4),
    ],
)
def test_operations(items, size):
    """Testing push/pop/peek"""
    the_stack = Stack()
    for item in items:
        the_stack.push(item)
    the_stack.peek()
    the_stack.pop()
    the_stack.pop()
    assert len(the_stack) == size


if __name__ == "__main__":
    pytest.main(["-v", __file__])
