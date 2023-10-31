#!/usr/bin/env python3
"""
`mapadt` testing

@authors: Roman Yasinovskyy
@version: 2023.10
"""

import pytest

from mapadt import HashMap


@pytest.fixture(name="empty_map")
def fixture_empty_map():
    """Empty map"""
    return HashMap()


@pytest.fixture(name="zoo")
def fixture_zoo():
    """Fixture zoo"""
    a_map = HashMap(11)
    map_items = [
        (54, "aardvark"),
        (26, "beaver"),
        (93, "cheetah"),
        (17, "dolphin"),
        (77, "elephant"),
        (31, "flamingo"),
        (44, "goat"),
        (55, "hippo"),
        (20, "iguana"),
    ]
    for key, value in map_items:
        a_map[key] = value
    return a_map


@pytest.fixture(name="edge")
def fixture_edge():
    """Edge case map"""
    a_map = HashMap(101)
    a_map.put(0, "Audi")
    a_map.put(100, "Bentley")
    a_map.put(200, "Chevy")
    a_map.put(300, None)
    a_map.put(400, False)
    return a_map


@pytest.mark.skip("Textbook implementation")
def test_init():
    """Testing __init__"""
    a_map = HashMap()
    assert isinstance(a_map, HashMap)
    assert not a_map
    a_map = HashMap(160)
    assert isinstance(a_map, HashMap)
    assert not a_map


def test_setitem_new(zoo):
    """Testing __setitem__ to add an item"""
    zoo.put(999, "jackal")
    zoo[998] = "koala"
    assert (
        str(zoo)
        == "{77: 'elephant', 44: 'goat', 20: 'iguana', 55: 'hippo', 26: 'beaver', "
        + "93: 'cheetah', 17: 'dolphin', 999: 'jackal', 998: 'koala', 31: 'flamingo', "
        + "54: 'aardvark'}"
    )


def test_setitem_update(zoo):
    """Testing __setitem__ to update an item"""
    zoo[999] = "jackal"
    zoo[998] = "koala"
    zoo[999] = "jackalope"
    zoo[998] = "kangaroo"
    assert (
        str(zoo)
        == "{77: 'elephant', 44: 'goat', 20: 'iguana', 55: 'hippo', 26: 'beaver', "
        + "93: 'cheetah', 17: 'dolphin', 999: 'jackalope', 998: 'kangaroo', "
        + "31: 'flamingo', 54: 'aardvark'}"
    )


def test_setitem_error(zoo):
    """Testing __setitem__ error"""
    assert len(zoo) == 9
    with pytest.raises(MemoryError) as excinfo:
        for i in range(20):
            zoo[i] = "zebra"
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "Hash Table is full"


def test_getitem_nokey(zoo):
    """Testing _getitem__ with nonexistent key"""
    with pytest.raises(KeyError) as excinfo:
        zoo[998]  # pylint: disable=pointless-statement
    assert excinfo.value.args[0] == "There is no such key in the map: 998."
    with pytest.raises(KeyError) as excinfo:
        zoo.get(999)
    assert excinfo.value.args[0] == "There is no such key in the map: 999."


def test_getitem_validkey(zoo):
    """Testing __getitem__"""
    assert zoo[54] == "aardvark"
    assert zoo.get(54) == "aardvark"


def test_len_empty(empty_map):
    """Testing __len__ of an empty map"""
    assert len(empty_map) == 0


def test_len(zoo):
    """Testing __len__"""
    assert len(zoo) == 9
    zoo[999] = "panda"
    assert len(zoo) == 10


def test_len_edge(edge):
    """Testing __len__"""
    assert len(edge) == 5


@pytest.mark.parametrize(
    "key, result", [(54, True), (55, True), (56, False), (57, False)]
)
def test_contains(zoo, key, result):
    """Testing __contains__"""
    assert (key in zoo) is result


def test_contains_edge(edge):
    """Testing __contains__"""
    assert edge.get(0) == "Audi"


def test_str_empty():
    """Testing __str__ of an empty map"""
    a_map = HashMap()
    assert str(a_map) == "{}"


def test_str(zoo):
    """Testing __str__"""
    assert (
        str(zoo)
        == "{77: 'elephant', 44: 'goat', 20: 'iguana', "
        + "55: 'hippo', 26: 'beaver', 93: 'cheetah', "
        + "17: 'dolphin', 31: 'flamingo', 54: 'aardvark'}"
    )


def test_keys_empty(empty_map):
    """Testing keys method"""
    assert empty_map.keys() == []


def test_keys(zoo):
    """Testing keys method"""
    assert zoo.keys() == [77, 44, 20, 55, 26, 93, 17, 31, 54]


def test_keys_edge(edge):
    """Testing keys method"""
    assert edge.keys() == [0, 400, 300, 200, 100]


def test_values_empty(empty_map):
    """Testing values method"""
    assert empty_map.values() == []


def test_values(zoo):
    """Testing values method"""
    assert zoo.values() == [
        "elephant",
        "goat",
        "iguana",
        "hippo",
        "beaver",
        "cheetah",
        "dolphin",
        "flamingo",
        "aardvark",
    ]


def test_values_edge(edge):
    """Testing values method"""
    assert edge.values() == ["Audi", False, None, "Chevy", "Bentley"]


def test_items_empty(empty_map):
    """Testing items method"""
    assert empty_map.items() == []


def test_items(zoo):
    """Testing items method"""
    assert zoo.items() == [
        (77, "elephant"),
        (44, "goat"),
        (20, "iguana"),
        (55, "hippo"),
        (26, "beaver"),
        (93, "cheetah"),
        (17, "dolphin"),
        (31, "flamingo"),
        (54, "aardvark"),
    ]


def test_items_edge(edge):
    """Testing items method"""
    assert edge.items() == [
        (0, "Audi"),
        (400, False),
        (300, None),
        (200, "Chevy"),
        (100, "Bentley"),
    ]


if __name__ == "__main__":
    pytest.main(["-v", __file__])
