

```python
"""Binary Tree implementation"""


class BinaryTree:
    """Binary Tree implementation as nodes and references"""
    def __init__(self, key):
        self._key = key
        self._child_left = None
        self._child_right = None

    def get_root_val(self):
        """Get root key value"""
        return self._key

    def set_root_val(self, new_key):
        """Set root key value"""
        self._key = new_key

    def get_child_left(self):
        """Get left child"""
        return self._child_left

    def set_child_left(self, new_child_left):
        """Set left child"""
        self._child_left = new_child_left

    def get_child_right(self):
        """Get right child"""
        return self._child_right

    def set_child_right(self, new_child_right):
        """Set right child"""
        self._child_right = new_child_right

    def is_leaf(self):
        """Check if a node is leaf"""
        return (not self._child_left) and (not self._child_right)

    def insert_left(self, new_node):
        """Insert left subtree"""
        new_subtree = BinaryTree(new_node)
        if self._child_left != None:
            new_subtree.set_child_left(self._child_left)
        self._child_left = new_subtree

    def insert_right(self, new_node):
        """Insert right subtree"""
        new_subtree = BinaryTree(new_node)
        if self._child_right != None:
            new_subtree.set_child_right(self._child_right)
        self._child_right = new_subtree

    def preorder(self):
        """Pre-order tree traversal"""
        print(self._key)
        if self._child_left:
            self._child_left.preorder()
        if self._child_right:
            self.child_right.preorder()

    def inorder(self):
        """In-order tree traversal"""
        if self._child_left:
            self._child_left.inorder()
        print(self._key)
        if self._child_right:
            self._child_right.inorder()

    def postorder(self):
        """Post-order tree traversal"""
        if self._child_left:
            self._child_left.postorder()
        if self._child_right:
            self._child_right.postorder()
        print(self._key)

    def height(self):
        """Height of a tree"""
        """THIS IMPLEMENTATION IS INCORRECT - OFF BY 1"""
        if not self._key:
            raise Exception("The tree is empty")
        if self._child_left:
            height_left = self._child_left.height()
        else:
            height_left = 0

        if self._child_right:
            height_right = self._child_right.height()
        else:
            height_right = 0

        return 1 + max(height_left, height_right)

    def count_nodes(self):
        """Count nodes in a tree"""
        if not self._key:
            return 0
        if self._child_left:
            children_left = self._child_left.count_nodes()
        else:
            children_left = 0

        if self._child_right:
            children_right = self._child_right.count_nodes()
        else:
            children_right = 0
        
        return 1 + children_left + children_right

```


```python
tree = BinaryTree('a')
tree.insert_left('b')
print(tree.get_child_left())
print(tree.get_child_left().get_root_val())
```

    <__main__.BinaryTree object at 0x7fe1241e2828>
    b



```python
tree.insert_right('c')
print(tree.get_child_right())
print(tree.get_child_right().get_root_val())
```

    <__main__.BinaryTree object at 0x7fe12415fb70>
    c



```python
tree.get_child_right().set_root_val('hello')
print(tree.get_child_right().get_root_val())
```

    hello



```python
tree.insert_left('d')
print('Getting to "b"')
print(tree.get_child_left().get_child_left().get_root_val())
```

    Getting to "b"
    b



```python
tree = BinaryTree('a')
tree.insert_left('b')
tree.insert_left('c')
tree.insert_left('d')
print('Preorder traversal')
tree.preorder()
```

    Preorder traversal
    a
    d
    c
    b



```python
print('Inorder traversal')
tree.inorder()
```

    Inorder traversal
    b
    c
    d
    a



```python
print('Postorder traversal')
tree.postorder()
```

    Postorder traversal
    b
    c
    d
    a



```python
print("Tree height")
print(tree.height())
```

    Tree height
    4



```python
test_height_tree = BinaryTree('a')
print(test_height_tree.height())
test_height_tree.insert_left('b')
print(test_height_tree.height())
test_height_tree.insert_right('c')
print(test_height_tree.height())
test_height_tree.get_child_right().insert_left('d')
print(test_height_tree.height())
test_height_tree.get_child_right().get_child_left().insert_left('e')
print(test_height_tree.height())
```

    1
    2
    2
    3
    4



```python
print('There are {} nodes in the tree'.format(test_height_tree.count_nodes()))
```

    There are 5 nodes in the tree

