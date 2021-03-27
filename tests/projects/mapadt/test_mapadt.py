#!/usr/bin/env python3
"""
`mapadt` testing

@authors: Roman Yasinovskyy
@version: 2021.3
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
    from src.projects.mapadt import HashMap


@pytest.fixture
def empty_map():
    return HashMap()


@pytest.fixture
def zoo():
    map = HashMap(11)
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
        map[key] = value
    return map


def test_init():
    """Testing __init__"""
    map = HashMap()
    assert isinstance(map, HashMap)
    assert not map
    map = HashMap(160)
    assert isinstance(map, HashMap)
    assert not map


def test_setitem_new(zoo):
    """Testing __setitem__ to add an item"""
    zoo.put(999, "jackal")
    zoo[998] = "koala"
    assert (
        str(zoo)
        == "{77: 'elephant', 44: 'goat', 20: 'iguana', 55: 'hippo', 26: 'beaver', 93: 'cheetah', 17: 'dolphin', 999: 'jackal', 998: 'koala', 31: 'flamingo', 54: 'aardvark'}"
    )


def test_setitem_update(zoo):
    """Testing __setitem__ to update an item"""
    zoo[999] = "jackal"
    zoo[998] = "koala"
    zoo[999] = "jackalope"
    zoo[998] = "kangaroo"
    assert (
        str(zoo)
        == "{77: 'elephant', 44: 'goat', 20: 'iguana', 55: 'hippo', 26: 'beaver', 93: 'cheetah', 17: 'dolphin', 999: 'jackalope', 998: 'kangaroo', 31: 'flamingo', 54: 'aardvark'}"
    )


def test_setitem_error(zoo):
    """Testing __setitem__ error"""
    with pytest.raises(MemoryError) as excinfo:
        for i in range(10):
            zoo[i] = "zebra"
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "Hash Table is full"


def test_getitem_nokey(zoo):
    """Testing _getitem__ with nonexistent key"""
    assert zoo[999] is None
    assert zoo.get(998) is None


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


@pytest.mark.parametrize(
    "key, result", [(54, True), (55, True), (56, False), (57, False)]
)
def test_contains(zoo, key, result):
    """Testing __contains__"""
    assert (key in zoo) is result


def test_str_empty():
    """Testing __len__ of an empty map"""
    map = HashMap()
    assert str(map) == "{}"


def test_str(zoo):
    """Testing __str__"""
    assert (
        str(zoo)
        == "{77: 'elephant', 44: 'goat', 20: 'iguana', 55: 'hippo', 26: 'beaver', 93: 'cheetah', 17: 'dolphin', 31: 'flamingo', 54: 'aardvark'}"
    )


def test_keys_empty(empty_map):
    """Testing keys method"""
    assert empty_map.keys() == []


def test_keys(zoo):
    """Testing keys method"""
    assert zoo.keys() == [77, 44, 20, 55, 26, 93, 17, 31, 54]


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


if __name__ == "__main__":
    pytest.main(["-v", __file__])
