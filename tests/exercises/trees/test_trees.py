#!/usr/bin/env python3
"""
Exercise `trees` testing

@authors: Roman Yasinovskyy
@version: 2021.2
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
    from src.exercises.trees import (
        BinaryTree,
        build_tree_oop,
        build_tree_lst,
        preorder,
        inorder,
        postorder,
        clockwise,
    )


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
        self.tree_as_references = build_tree_oop()
        self.tree_as_lists = build_tree_lst()

    def test_height(self):
        """Testing height() method"""
        assert self.b_movie_tree.height() == 4

    def test_size(self):
        """Testing size() method"""
        assert self.b_movie_tree.size() == 9

    def test_preorder(self, capsys):
        """Testing preorder() method"""
        self.b_movie_tree.preorder()
        out, _ = capsys.readouterr()
        assert (
            out.strip() == "Catwoman Batman Alfred Gordon Dent Frodo Elfo Robin Pavel"
        )

    def test_preorder_ref(self, capsys):
        """Testing preorder() method"""
        self.tree_as_references.preorder()
        out, _ = capsys.readouterr()
        assert out.strip() == "a b d c e f"

    def test_preorder_lst(self, capsys):
        """Testing preorder() method"""
        preorder(self.tree_as_lists)
        out, _ = capsys.readouterr()
        assert out.strip() == "a b d c e f"

    def test_inorder(self, capsys):
        """Testing inorder() method"""
        self.b_movie_tree.inorder()
        out, _ = capsys.readouterr()
        assert (
            out.strip() == "Alfred Batman Catwoman Dent Elfo Frodo Gordon Pavel Robin"
        )

    def test_inorder_ref(self, capsys):
        """Testing inorder() method"""
        self.tree_as_references.inorder()
        out, _ = capsys.readouterr()
        assert out.strip() == "b d a e c f"

    def test_inorder_lst(self, capsys):
        """Testing inorder() method"""
        inorder(self.tree_as_lists)
        out, _ = capsys.readouterr()
        assert out.strip() == "b d a e c f"

    def test_postorder(self, capsys):
        """Testing postorder() method"""
        self.b_movie_tree.postorder()
        out, _ = capsys.readouterr()
        assert (
            out.strip() == "Alfred Batman Elfo Frodo Dent Pavel Robin Gordon Catwoman"
        )

    def test_postorder_ref(self, capsys):
        """Testing postorder() method"""
        self.tree_as_references.postorder()
        out, _ = capsys.readouterr()
        assert out.strip() == "d b e f c a"

    def test_postorder_lst(self, capsys):
        """Testing postorder() method"""
        postorder(self.tree_as_lists)
        out, _ = capsys.readouterr()
        assert out.strip() == "d b e f c a"

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

    def test_levelorder(self, capsys):
        """Testing levelorder() method"""
        self.tree_as_references.levelorder()
        out, _ = capsys.readouterr()
        assert out.strip() == "a b c d e f"

    def test_invert(self, capsys):
        """Testing invert() method"""
        self.tree_as_references.invert()
        self.tree_as_references.inorder()
        out, _ = capsys.readouterr()
        assert out.strip() == "f c e a d b"


if __name__ == "__main__":
    pytest.main(["-v", __file__])
