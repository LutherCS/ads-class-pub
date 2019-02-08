"""
trees import statement
"""
name = "trees"

from .trees import BinaryTree
from .trees import build_tree_oop
from .treeslst import build_tree_lst
from .treeslst import clockwise

__all__ = ["BinaryTree", "clockwise"]
