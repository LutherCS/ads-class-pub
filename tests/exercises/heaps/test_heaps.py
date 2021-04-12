#!/usr/bin/env python3
"""
`heaps` testing

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
    from src.exercises.heaps import BinaryHeapMax


names = [
    "Alfred",
    "Batman",
    "Catwoman",
    "Dent",
    "Elfo",
    "Frodo",
    "Gordon",
    "Pavel",
    "Robin",
]

numbers = [55, 73, 17, 41, 83, 89, 7, 28, 10, 69]


@pytest.mark.parametrize(
    "data, expected_result",
    [
        (
            names,
            [
                "Robin",
                "Pavel",
                "Frodo",
                "Gordon",
                "Catwoman",
                "Batman",
                "Elfo",
                "Alfred",
                "Dent",
            ],
        ),
        (numbers, [89, 73, 83, 41, 69, 17, 7, 28, 10, 55]),
    ],
)
def test_insert(data, expected_result):
    """Testing insert method"""
    heap = BinaryHeapMax()
    for n in data:
        heap.insert(n)
    assert str(heap) == str(expected_result)


@pytest.mark.parametrize(
    "data, expected_result",
    [
        (
            names,
            [
                "Pavel",
                "Gordon",
                "Frodo",
                "Dent",
                "Catwoman",
                "Batman",
                "Elfo",
                "Alfred",
            ],
        ),
        (numbers, [83, 73, 55, 41, 69, 17, 7, 28, 10]),
    ],
)
def test_delete(data, expected_result):
    """Testing delete method"""
    heap = BinaryHeapMax()
    for n in data:
        heap.insert(n)
    heap.delete()
    assert str(heap) == str(expected_result)


@pytest.mark.parametrize(
    "data, expected_result",
    [
        (
            names,
            [
                "Robin",
                "Pavel",
                "Gordon",
                "Dent",
                "Elfo",
                "Frodo",
                "Catwoman",
                "Batman",
                "Alfred",
            ],
        ),
        (numbers, [89, 83, 55, 41, 73, 17, 7, 28, 10, 69]),
    ],
)
def test_heapify(data, expected_result):
    """Testing heapify method"""
    heap = BinaryHeapMax()
    heap.heapify(data)
    assert str(heap) == str(expected_result)


if __name__ == "__main__":
    pytest.main(["-v", __file__])
