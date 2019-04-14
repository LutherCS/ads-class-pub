#!/usr/bin/env python3
"""
Testing the Binary Tree module
@authors: Roman Yasinovskyy
@updated: 2019
"""

import pytest
from src.exercises.trees import build_tree_oop
from src.exercises.trees import build_tree_lst
from src.exercises.trees import clockwise


class TestBinaryTreeMethods:
    """Testing the Binary Tree module"""

    @pytest.fixture(scope="function", autouse=True)
    def setup_class(self):
        """Setting up"""
        self.tree_as_references = build_tree_oop()
        self.tree_as_lists = build_tree_lst()

    def test_clockwise_ref(self, capsys):
        """Testing clockwise() method"""
        self.tree_as_references.clockwise()
        out, _ = capsys.readouterr()
        assert out.strip() == "a c f e b d"

    def test_clockwise_lst(self, capsys):
        """Testing clockwise() method"""
        clockwise(self.tree_as_lists)
        out, _ = capsys.readouterr()
        assert out.strip() == "a c f e b d"


if __name__ == "__main__":
    pytest.main(["-vv", "test_trees.py"])
