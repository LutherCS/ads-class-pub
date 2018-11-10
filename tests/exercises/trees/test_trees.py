"""
Testing the Binary Tree module
Roman Yasinovskyy, 2017
"""

import pytest
from exercises.trees import BinaryTree
from exercises.trees import build_tree_oop
from exercises.trees import build_tree_lst
from exercises.trees import clockwise


class TestBinaryTreeMethods:
    """Testing the Binary Tree module"""

    @pytest.fixture(scope="function", autouse=True)
    def setup_class(self):
        """Setting up"""
        self.tree_as_references = build_tree_oop()
        self.tree_as_lists = build_tree_lst()

    def test_clockwise_lst(self, capsys):
        """Testing clockwise() method"""
        clockwise(self.tree_as_lists)
        out, _ = capsys.readouterr()
        assert out.strip() == "a c f e b d"

    def test_clockwise(self, capsys):
        """Testing clockwise() method"""
        self.tree_as_references.clockwise()
        out, _ = capsys.readouterr()
        assert out.strip() == "a c f e b d"


if __name__ == "__main__":
    pytest.main(["test_trees.py"])
