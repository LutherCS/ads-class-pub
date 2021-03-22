#!/usr/bin/env python3
"""
Exercise `trees` implementation

@author:
"""


def BinaryTree(r):
    return [r, [], []]


def insert_child_left(root, new_branch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root


def insert_child_right(root, new_branch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [], []])
    return root


def get_root_val(root):
    return root[0]


def set_root_val(root, new_val):
    root[0] = new_val


def get_child_left(root):
    return root[1]


def get_child_right(root):
    return root[2]


def preorder(root):
    """Pre-order tree traversal"""
    raise NotImplementedError


def inorder(root):
    """In-order tree traversal"""
    raise NotImplementedError


def postorder(root):
    """Post-order tree traversal"""
    raise NotImplementedError


def clockwise(root):
    """Clockwise tree traversal"""
    print(get_root_val(root), end=" ")
    if get_child_right(root):
        clockwise(get_child_right(root))
    if get_child_left(root):
        clockwise(get_child_left(root))


def build_tree_lst() -> list:
    """Build a tree and return it"""
    raise NotImplementedError
