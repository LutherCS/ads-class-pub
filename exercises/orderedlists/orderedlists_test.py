#!/usr/bin/env python3
"""
`orderedlists` testing

@authors: Roman Yasinovskyy, Karina Hoff
@version: 2021.9
"""

import pytest

from orderedlists import Node, OrderedList


@pytest.mark.skip("Textbook implementation")
@pytest.mark.parametrize("value", ["Hello", 1861, 18.61, 18.61j])
def test_node_init(value):
    """Testing Node constructor"""
    a_node = Node(value)
    assert a_node is not None


@pytest.mark.skip("Textbook implementation")
def test_node_init_error():
    """Test Node constructor error"""
    with pytest.raises(Exception) as excinfo:
        _ = Node()  # pylint: disable=no-value-for-parameter
    exception_message = excinfo.value.args[0]
    assert (
        exception_message
        == "__init__() missing 1 required positional argument: 'init_data'"
    )


@pytest.mark.skip("Textbook implementation")
@pytest.mark.parametrize("value", ["Hello", 1861, 18.61, 18.61j])
def test_node_data_getter(value):
    """Test Node data property getter"""
    a_node = Node(value)
    assert a_node.data == value


@pytest.mark.skip("Textbook implementation")
@pytest.mark.parametrize(
    "value, new_value",
    [("Hello", "Luther"), (1861, 2021), (18.61, 20.21), (18.61j, 20.21j)],
)
def test_node_data_setter(value, new_value):
    """Test Node data property setter"""
    a_node = Node(value)
    a_node.data = new_value
    assert a_node.data == new_value


@pytest.mark.skip("Textbook implementation")
@pytest.mark.parametrize("value", ["Hello", 1861, 18.61, 18.61j])
def test_node_next_getter(value):
    """Test Node next property getter"""
    a_node = Node(value)
    assert a_node.next is None


@pytest.mark.skip("Textbook implementation")
@pytest.mark.parametrize("value", ["Hello", 1861, 18.61, 18.61j])
def test_node_next_setter(value):
    """Test Node next property setter"""
    a_node = Node(value)
    next_node = Node(None)
    a_node.next = next_node
    assert a_node.next == next_node


@pytest.mark.skip("Textbook implementation")
@pytest.mark.parametrize(
    "value, str_value",
    [("Hello", "Hello"), (1861, "1861"), (18.61, "18.61"), (18.61j, "18.61j")],
)
def test_node_str(value, str_value):
    """Test Node __str__ method"""
    a_node = Node(value)
    assert str(a_node) == str_value


@pytest.fixture
def an_empty_list():
    l = OrderedList()
    return l


@pytest.fixture
def the_list():
    l = OrderedList()
    for val in [1, 8, 6, 1, 2, 0, 2, 1]:
        l.add(val)
    return l


@pytest.mark.skip("Textbook implementation")
def test_list_init():
    """Test OrderedList constructor"""
    l = OrderedList()
    assert l is not None


@pytest.mark.skip("Textbook implementation")
def test_len(an_empty_list, the_list):
    """Test OrderedList __len__"""
    assert len(an_empty_list) == 0
    assert len(the_list) == 8


@pytest.mark.skip("Textbook implementation")
def test_str(an_empty_list, the_list):
    """Test OrderedList __str__"""
    assert str(an_empty_list) == "[]"
    assert str(the_list) == "[0, 1, 1, 1, 2, 2, 6, 8]"


@pytest.mark.skip("Textbook implementation")
def test_is_empty(an_empty_list, the_list):
    """Test OrderedList is_empty method"""
    assert an_empty_list.is_empty() == True
    assert the_list.is_empty() == False


@pytest.mark.skip("Textbook implementation")
def test_size(an_empty_list, the_list):
    """Test OrderedList size method"""
    assert an_empty_list.size() == 0
    assert the_list.size() == 8


@pytest.mark.skip("Other methods call this one")
def test_add():
    """Test OrderedList add method"""
    lst = OrderedList()
    for val in [1, 8, 6, 1, 2, 0, 2, 1]:
        lst.add(val)
    assert len(lst) == 8
    assert str(lst) == "[0, 1, 1, 1, 2, 2, 6, 8]"
    assert lst.is_empty() is False
    assert lst.size() == 8


@pytest.mark.skip("Textbook implementation")
@pytest.mark.parametrize(
    "value, result", [(0, True), (2, True), (3, False), (160, False)]
)
def test_orderedlist_search(the_list, value, result):
    """Test OrderedList search method"""
    assert the_list.search(value) == result


@pytest.mark.parametrize(
    "a_list, expected",
    [
        ([], "[]"),
        ([1, 2, 3], "[1, 2, 3]"),
        (["c", "a", "b"], "[a, b, c]"),
        ([3, 8, 2, 7, 1, 0, 3, 5], "[0, 1, 2, 3, 3, 5, 7, 8]"),
    ],
)
def test_append(a_list, expected):
    """Testing method append"""
    ol = OrderedList()
    for item in a_list:
        ol.append(item)
    assert str(ol) == expected
    assert len(ol) == len(a_list)


@pytest.mark.parametrize(
    "a_list, expected",
    [
        ([], "[]"),
        ([1, 2, 3], "[1, 2, 3]"),
        (["c", "a", "b"], "[a, b, c]"),
        ([3, 8, 2, 7, 1, 0, 3, 5], "[0, 1, 2, 3, 3, 5, 7, 8]"),
    ],
)
def test_insert(a_list, expected):
    """Testing method insert"""
    ol = OrderedList()
    for item in a_list:
        ol.insert(0, item)
    assert str(ol) == expected
    assert len(ol) == len(a_list)


@pytest.mark.parametrize(
    "a_list, a_number, expected",
    [
        ([], 3, -1),
        ([1, 2, 3], 3, 2),
        (["c", "a", "b"], "3", -1),
        ([3, 8, 2, 7, 1, 0, 3, 5], 3, 3),
    ],
)
def test_index(a_list, a_number, expected):
    """Testing method index"""
    ol = OrderedList()
    for item in a_list:
        ol.add(item)
    assert ol.index(a_number) == expected


@pytest.mark.parametrize(
    "a_list, expected",
    [([1, 2, 3], 3), ([3, 2, 1], 3), (["a", "c", "b"], "c"), (["b", "c", "a"], "c")],
)
def test_pop_last(a_list, expected):
    """Test pop method"""
    ol = OrderedList()
    for item in a_list:
        ol.add(item)
    assert ol.pop() == expected


def test_pop_error_1(an_empty_list):
    """Test OrderedList pop errors"""
    with pytest.raises(IndexError) as excinfo:
        an_empty_list.pop()
    exception_message = excinfo.value.args[0]
    assert exception_message == "The list is empty"


def test_pop_error_2(an_empty_list):
    """Test OrderedList pop errors"""
    with pytest.raises(IndexError) as excinfo:
        an_empty_list.pop(10)
    exception_message = excinfo.value.args[0]
    assert exception_message == "The list is empty"


def test_pop_error_3(the_list):
    """Test OrderedList pop errors"""
    with pytest.raises(IndexError) as excinfo:
        the_list.__getitem__(10)
    exception_message = excinfo.value.args[0]
    assert exception_message == "List index out of range: too large"


def test_pop_error_4(the_list):
    """Test OrderedList pop errors"""
    with pytest.raises(ValueError) as excinfo:
        the_list.__getitem__(-1)
    exception_message = excinfo.value.args[0]
    assert exception_message == "Invalid position: negative index"


@pytest.mark.parametrize(
    "a_list, position, expected",
    [
        ([0], 0, 0),
        ([1, 2, 3], 2, 3),
        (["c", "a", "b"], 0, "a"),
        ([3, 8, 2, 7, 1, 0, 3, 5], 7, 8),
    ],
)
def test_pop(a_list, position, expected):
    """Testing method pop"""
    ol = OrderedList()
    for item in a_list:
        ol.add(item)
    assert ol.pop(position) == expected
    assert len(ol) == len(a_list) - 1


@pytest.mark.parametrize("index, value", [(0, 0), (1, 1), (2, 1), (7, 8)])
def test_getitem_simple(the_list, index, value):
    """Test __getitem__ method on the_list"""
    assert the_list[index] == value


def test_getitem_error_1(the_list):
    """Test OrderedList __getitem__ error"""
    with pytest.raises(Exception) as excinfo:
        the_list.__getitem__()  # pylint: disable=no-value-for-parameter
    exception_message = excinfo.value.args[0]
    assert (
        exception_message
        == "__getitem__() missing 1 required positional argument: 'position'"
    )


def test_getitem_error_2(an_empty_list):
    """Test OrderedList __getitem__ errors"""
    with pytest.raises(IndexError) as excinfo:
        an_empty_list.__getitem__(0)
    exception_message = excinfo.value.args[0]
    assert exception_message == "The list is empty"


def test_getitem_error_3(the_list):
    """Test OrderedList __getitem__ errors"""
    with pytest.raises(IndexError) as excinfo:
        the_list.__getitem__(10)
    exception_message = excinfo.value.args[0]
    assert exception_message == "List index out of range: too large"


def test_getitem_error_4(the_list):
    """Test OrderedList __getitem__ errors"""
    with pytest.raises(ValueError) as excinfo:
        the_list.__getitem__(-1)
    exception_message = excinfo.value.args[0]
    assert exception_message == "Invalid position: negative index"


@pytest.mark.parametrize(
    "a_list, position, expected",
    [
        ([0], 0, 0),
        ([1, 2, 3], 2, 3),
        (["c", "a", "b"], 0, "a"),
        ([3, 8, 2, 7, 1, 0, 3, 5], 7, 8),
    ],
)
def test_getitem(a_list, position, expected):
    """Testing method __getitem__"""
    ol = OrderedList()
    for item in a_list:
        ol.add(item)
    assert ol[position] == expected
    assert len(ol) == len(a_list)


if __name__ == "__main__":
    pytest.main(["-v", __file__])
