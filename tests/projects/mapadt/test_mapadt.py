#!/usr/bin/env python3
"""
Testing module Map ADT
@authors: Roman Yasinovskyy
@updated: 2019
"""

import pytest
from src.projects.mapadt import HashTable


class TestMap:
    """Testing module map"""

    @pytest.fixture(scope="function", autouse=True)
    def setup_class(self):
        """Setting up"""
        self.the_map = HashTable(11)
        map_test_items = [
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
        for item in map_test_items:
            self.the_map.put(item[0], item[1])

        self.simple_map = HashTable()
        self.simple_map[17] = "a"
        self.simple_map[32] = "b"

        self.empty_map = HashTable(10)

    def test_init(self):
        """Testing __init__"""
        assert self.the_map
        assert self.simple_map
        assert not self.empty_map

    def test_len(self):
        """Testing __len__"""
        assert len(self.the_map) == 9
        assert len(self.simple_map) == 2
        assert not self.empty_map

    def test_getter(self):
        """Testing __getitem__"""
        assert self.the_map[54] == "aardvark"
        assert self.the_map.get(54) == "aardvark"
        assert self.the_map[20] == "iguana"
        assert self.the_map.get(20) == "iguana"

    def test_setter(self):
        """Testing __setitem__ to add an item"""
        self.the_map[21] = "jackal"
        assert self.the_map[21] == "jackal"
        self.the_map.put(18, "koala")
        assert self.the_map.get(18) == "koala"
        assert (
            str(self.the_map)
            == "{77: 'elephant', 44: 'goat', 20: 'iguana', 55: 'hippo', 26: 'beaver', 93: 'cheetah', 17: 'dolphin', 18: 'koala', 21: 'jackal', 31: 'flamingo', 54: 'aardvark'}"
        )

    def test_updater(self):
        """Testing __setitem__ to update an item"""
        self.the_map[54] = "anteater"
        assert self.the_map[54] == "anteater"
        self.the_map.put(55, "hyena")
        assert self.the_map.get(55) == "hyena"
        assert (
            str(self.the_map)
            == "{77: 'elephant', 44: 'goat', 20: 'iguana', 55: 'hyena', 26: 'beaver', 93: 'cheetah', 17: 'dolphin', 31: 'flamingo', 54: 'anteater'}"
        )

    def test_setter_error(self):
        """Testing __setitem__ error"""
        with pytest.raises(Exception) as excinfo:
            self.the_map[160] = "zebra"
            self.the_map[161] = "zebra"
            self.the_map[162] = "zebra"
        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Hash Table is full"
        assert len(self.the_map) == 11

    def test_value_none(self):
        """Testing nonexistent key"""
        assert not self.the_map[99]
        assert not self.the_map.get(99)

    def test_key_found(self):
        """Testing __contains__ success"""
        assert 54 in self.the_map
        assert 55 in self.the_map
        assert 17 in self.the_map
        assert 77 in self.the_map

    def test_key_not_found(self):
        """Testing __contains__ failure"""
        assert 53 not in self.the_map
        assert 56 not in self.the_map
        assert 16 not in self.the_map
        assert 61 not in self.the_map

    def test_str(self):
        """Testing __str__"""
        assert (
            str(self.the_map)
            == "{77: 'elephant', 44: 'goat', 20: 'iguana', 55: 'hippo', 26: 'beaver', 93: 'cheetah', 17: 'dolphin', 31: 'flamingo', 54: 'aardvark'}"
        )
        assert str(self.simple_map) == "{32: 'b', 17: 'a'}"
        assert str(self.empty_map) == "{}"

    def test_keys(self):
        """Testing keys method"""
        assert self.the_map.keys() == [77, 44, 20, 55, 26, 93, 17, 31, 54]
        assert self.simple_map.keys() == [32, 17]
        assert self.empty_map.keys() == []

    def test_values(self):
        """Testing values method"""
        assert self.the_map.values() == [
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
        assert self.simple_map.values() == ["b", "a"]
        assert self.empty_map.keys() == []

    def test_items(self):
        """Testing items method"""
        assert self.the_map.items() == [
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
        assert self.simple_map.items() == [(32, "b"), (17, "a")]
        assert self.empty_map.items() == []


if __name__ == "__main__":
    pytest.main(["-vv", "test_mapadt.py"])
