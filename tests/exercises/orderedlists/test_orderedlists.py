#!/usr/bin/python3
"""
Testing the orderedlists module
@authors: Roman Yasinovskyy, Karina Hoff
@updated: 2019
"""

import pytest
from src.exercises.orderedlists import OrderedList


class TestAndGradeOrderedListMethods:
    """Testing and grading module orderedlists"""

    @pytest.mark.parametrize(
        "a_list, expected",
        [
            ([], "[]"),
            ([1, 2, 3], "[1, 2, 3]"),
            (["c", "a", "b"], "[a, b, c]"),
            ([3, 8, 2, 7, 1, 0, 3, 5], "[0, 1, 2, 3, 3, 5, 7, 8]"),
        ],
    )
    def test_append(self, a_list, expected):
        """Testing method append"""
        ol = OrderedList()
        for item in a_list:
            ol.append(item)
        assert str(ol) == expected
        assert (len(ol)) == len(a_list)

    @pytest.mark.parametrize(
        "a_list, expected",
        [
            ([], "[]"),
            ([1, 2, 3], "[1, 2, 3]"),
            (["c", "a", "b"], "[a, b, c]"),
            ([3, 8, 2, 7, 1, 0, 3, 5], "[0, 1, 2, 3, 3, 5, 7, 8]"),
        ],
    )
    def test_insert(self, a_list, expected):
        """Testing method insert"""
        ol = OrderedList()
        for item in a_list:
            ol.insert(0, item)
        assert str(ol) == expected
        assert (len(ol)) == len(a_list)

    @pytest.mark.parametrize(
        "a_list, a_number, expected",
        [
            ([], 3, -1),
            ([1, 2, 3], 3, 2),
            (["c", "a", "b"], "3", -1),
            ([3, 8, 2, 7, 1, 0, 3, 5], 3, 3),
        ],
    )
    def test_index(self, a_list, a_number, expected):
        """Testing method index"""
        ol = OrderedList()
        for item in a_list:
            ol.add(item)
        assert ol.index(a_number) == expected

    @pytest.mark.parametrize(
        "a_list, position, expected",
        [
            ([0], 0, 0),
            ([1, 2, 3], 2, 3),
            (["c", "a", "b"], 0, "a"),
            ([3, 8, 2, 7, 1, 0, 3, 5], 100, 8),
        ],
    )
    def test_pop(self, a_list, position, expected):
        """Testing method pop"""
        ol = OrderedList()
        for item in a_list:
            ol.add(item)
        assert ol.pop(position) == expected
        assert len(ol) == len(a_list) - 1

    @pytest.mark.parametrize(
        "a_list, position, expected",
        [
            ([0], 0, 0),
            ([1, 2, 3], 2, 3),
            (["c", "a", "b"], 0, "a"),
            ([3, 8, 2, 7, 1, 0, 3, 5], 100, 8),
        ],
    )
    def test_getitem(self, a_list, position, expected):
        """Testing method __getitem__"""
        ol = OrderedList()
        for item in a_list:
            ol.add(item)
        assert ol[position] == expected
        assert len(ol) == len(a_list)


if __name__ == "__main__":
    pytest.main(["-v", "test_orderedlists.py"])
