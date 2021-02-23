#!/usr/bin/env python3
"""
Exercise `orderedlists` testing

@authors: Roman Yasinovskyy, Karina Hoff
@version: 2021.2
"""

import importlib
import pathlib
import random
import sys

import pytest

try:
    importlib.util.find_spec(".".join(pathlib.Path(__file__).parts[-3:-1]), "src")
except ModuleNotFoundError:
    sys.path.append(f"{pathlib.Path(__file__).parents[3]}/")
finally:
    from src.exercises.orderedlists import Node, OrderedList


class TestOrderedListMethods:
    """Testing module orderedlists"""

    @pytest.fixture(scope="function", autouse=True)
    def setup_class(self):
        """Setting up"""
        self.node_str = Node("Hello")
        self.node_int = Node(1861)
        self.node_float = Node(1.8)
        self.node_comp = Node(1.8j)
        self.ord_lst = OrderedList()
        self.ord_lst2 = OrderedList()
        for val in [1, 8, 6, 1, 2, 0, 1, 9]:
            self.ord_lst2.add(val)

    def test_node_init(self):
        """Test Node __init__ method"""
        assert self.node_str.data
        assert self.node_int.data
        assert self.node_float.data
        assert self.node_comp.data

    def test_node_init_error(self):
        """Test Node __init__ error"""
        with pytest.raises(Exception) as excinfo:
            _ = Node()  # pylint: disable=no-value-for-parameter
        exception_message = excinfo.value.args[0]
        assert (
            exception_message
            == "__init__() missing 1 required positional argument: 'init_data'"
        )

    def test_node_data_getter(self):
        """Test Node data property getter"""
        assert self.node_str.data == "Hello"
        assert isinstance(self.node_str.data, str)

        assert self.node_int.data == 1861
        assert isinstance(self.node_int.data, int)

        assert self.node_float.data == 1.8
        assert isinstance(self.node_float.data, float)

        assert self.node_comp.data == 1.8j
        assert isinstance(self.node_comp.data, complex)

    def test_node_data_setter(self):
        """Test Node data property setter"""
        self.node_str.data = "Goodbye"
        assert self.node_str.data == "Goodbye"
        assert isinstance(self.node_str.data, str)

        self.node_int.data = 2019
        assert self.node_int.data == 2019
        assert isinstance(self.node_int.data, int)

        self.node_float.data = 3.2
        assert self.node_float.data == 3.2
        assert isinstance(self.node_float.data, float)

        self.node_comp.data = 3.2j
        assert self.node_comp.data == 3.2j
        assert isinstance(self.node_comp.data, complex)

    def test_node_data_setter2(self):
        """Test Node data setter with different data types"""
        self.node_str.set_data(2019)
        assert self.node_str.get_data() == 2019
        assert isinstance(self.node_str.get_data(), int)

        self.node_int.set_data(3.2)
        assert self.node_int.get_data() == 3.2
        assert isinstance(self.node_int.get_data(), float)

        self.node_float.set_data(3.2j)
        assert self.node_float.get_data() == 3.2j
        assert isinstance(self.node_float.get_data(), complex)

        self.node_comp.set_data("Luther")
        assert self.node_comp.get_data() == "Luther"
        assert isinstance(self.node_comp.get_data(), str)

    def test_node_next_getter(self):
        """Test Node next property getter"""
        for node in [self.node_str, self.node_int, self.node_float, self.node_comp]:
            assert node.next is None

    def test_node_next_setter(self):
        """Test Node next property setter"""
        self.node_str.next = self.node_int
        assert self.node_str.next == self.node_int

    def test_node_str(self):
        """Test Node __str__ method"""
        assert str(self.node_str) == "Hello"
        assert str(self.node_int) == "1861"
        assert str(self.node_float) == "1.8"
        assert str(self.node_comp) == "1.8j"

    def test_orderedlist_getitem(self):
        """Test OrderedList __getitem__ method"""
        self.ord_lst.append("boo")
        self.ord_lst.append("foo")
        self.ord_lst.append("buzz")
        assert self.ord_lst[1] == "buzz"

    def test_orderedlist_getitem_error(self):
        """Test OrderedList __getitem__ error"""
        with pytest.raises(Exception) as excinfo:
            self.ord_lst.__getitem__()  # pylint: disable=no-value-for-parameter
        exception_message = excinfo.value.args[0]
        assert (
            exception_message
            == "__getitem__() missing 1 required positional argument: 'position'"
        )

        with pytest.raises(Exception) as excinfo:
            self.ord_lst.__getitem__(0)
        exception_message = excinfo.value.args[0]
        assert exception_message == "The list is empty"

    def test_orderedlist_len(self):
        """Test OrderedList __len__"""
        assert len(self.ord_lst) == 0
        assert len(self.ord_lst2) == 8

    def test_orderedlist_str(self):
        """Test OrderedList __str__"""
        assert str(self.ord_lst) == "[]"
        assert str(self.ord_lst2) == "[0, 1, 1, 1, 2, 6, 8, 9]"

    def test_orderedlist_is_empty(self):
        """Test OrderedList is_empty method"""
        assert self.ord_lst.is_empty()
        assert not self.ord_lst2.is_empty()

    def test_orderedlist_size(self):
        """Test OrderedList size method"""
        assert self.ord_lst.size() == 0
        assert self.ord_lst2.size() == 8

    def test_orderedlist_add(self):
        """Test OrderedList add method"""
        for val in [1, 8, 6, 1, 2, 0, 1, 9]:
            self.ord_lst.add(val)
        assert len(self.ord_lst) == 8
        assert str(self.ord_lst) == "[0, 1, 1, 1, 2, 6, 8, 9]"
        assert not self.ord_lst.is_empty()
        assert self.ord_lst.size() == 8

    def test_orderedlist_append(self):
        """Test OrderedList append method"""
        for val in [1, 8, 6, 1, 2, 0, 1, 9]:
            self.ord_lst.append(val)
        assert len(self.ord_lst) == 8
        assert str(self.ord_lst) == "[0, 1, 1, 1, 2, 6, 8, 9]"
        assert not self.ord_lst.is_empty()
        assert self.ord_lst.size() == 8

    def test_orderedlist_insert(self):
        """Test OrderedList insert method"""
        for val in [1, 8, 6, 1, 2, 0, 1, 9]:
            self.ord_lst.insert(random.randint(0, len(self.ord_lst)), val)
        assert len(self.ord_lst) == 8
        assert str(self.ord_lst) == "[0, 1, 1, 1, 2, 6, 8, 9]"
        assert not self.ord_lst.is_empty()
        assert self.ord_lst.size() == 8

    def test_orderedlist_pop(self):
        """Test OrderedList pop method"""
        popped_vals = []
        for _ in range(4):
            popped_vals.append(self.ord_lst2.pop())
        assert popped_vals == [9, 8, 6, 2]
        assert len(self.ord_lst2) == 4
        assert str(self.ord_lst2) == "[0, 1, 1, 1]"
        assert not self.ord_lst2.is_empty()
        assert self.ord_lst2.size() == 4

    def test_orderedlist_pop_error(self):
        """Test OrderedList pop method exceptions"""
        with pytest.raises(ValueError) as excinfo:
            self.ord_lst.pop()
        exception_message = excinfo.value.args[0]
        assert exception_message == "Cannot pop from an empty list"

        with pytest.raises(IndexError) as excinfo:
            self.ord_lst2.pop(-1)
        exception_message = excinfo.value.args[0]
        assert exception_message == "Invalid position for popping an item"

    def test_orderedlist_search(self):
        """Test OrderedList search method"""
        assert not self.ord_lst.search(0)
        assert self.ord_lst2.search(0)
        assert self.ord_lst2.search(1)
        assert not self.ord_lst2.search(23)

    def test_orderedlist_index(self):
        """Test OrderedList index method"""
        assert self.ord_lst.index(0) == -1
        assert self.ord_lst2.index(0) == 0
        assert self.ord_lst.index(23) == -1


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
    pytest.main(["-v", __file__])
