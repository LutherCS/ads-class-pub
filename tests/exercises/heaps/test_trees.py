"""
Testing the Binary Tree module
Roman Yasinovskyy, 2018
"""

import pytest
from exercises.heaps import BinaryTree


class TestBinaryTreeMethods:
    """Testing the Binary Tree module"""

    @pytest.fixture(scope="function", autouse=True)
    def setup_class(self):
        """Setting up"""
        self.b_movie_tree = BinaryTree("Catwoman")
        self.b_movie_tree.insert_left("Batman")
        self.b_movie_tree.insert_right("Gordon")
        self.b_movie_tree.get_child_left().insert_left("Alfred")
        self.b_movie_tree.get_child_right().insert_left("Dent")
        self.b_movie_tree.get_child_right().insert_right("Robin")
        self.b_movie_tree.get_child_right().get_child_left().insert_right("Frodo")
        self.b_movie_tree.get_child_right().get_child_right().insert_left("Pavel")
        self.b_movie_tree.get_child_right().get_child_left().get_child_right().insert_left(
            "Elfo"
        )

    def test_height(self):
        """Testing height() method"""
        assert self.b_movie_tree.height() == 4

    def test_size(self):
        """Testing size() method"""
        assert self.b_movie_tree.size() == 9

    def test_preorder(self, capsys):
        """Testing preorder() method"""
        self.b_movie_tree.preorder()
        out, err = capsys.readouterr()
        assert (
            out.strip() == "Catwoman Batman Alfred Gordon Dent Frodo Elfo Robin Pavel"
        )

    def test_inorder(self, capsys):
        """Testing inorder() method"""
        self.b_movie_tree.inorder()
        out, err = capsys.readouterr()
        assert (
            out.strip() == "Alfred Batman Catwoman Dent Elfo Frodo Gordon Pavel Robin"
        )

    def test_postorder(self, capsys):
        """Testing postorder() method"""
        self.b_movie_tree.postorder()
        out, err = capsys.readouterr()
        assert (
            out.strip() == "Alfred Batman Elfo Frodo Dent Pavel Robin Gordon Catwoman"
        )


if __name__ == "__main__":
    pytest.main(["test_trees.py"])
