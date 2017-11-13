"""Morse code project"""

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

"""Morse code encoder and decoder"""
class Coder:
    """Encoder"""
    def __init__(self, file_in):
        self.morse_tree = BinaryTree('')

        with open(file_in) as morse_file:
            for line in morse_file:
                letter, code = line.split()
                self.follow_and_insert(code, letter)

    def follow_and_insert(self, code_str, letter):
        """Follow the tree and insert a letter"""
        current = self.morse_tree
        for symbol in code_str:
            # TODO: Follow the algorithm to build a tree of letters
            """if _dot_, go to to the left child, else go to the right child"""
            """create empty placeholder nodes (value of '') if necessary"""
            raise NotImplementedError
        """set the current node value to _letter_"""

    def follow_and_retrieve(self, code_str):
        """Follow the tree and retrieve a letter"""
        current = self.morse_tree
        for symbol in code_str:
            # TODO: Follow the branches of the tree until
            """if _dot_, go to to the left child, else go to the right child"""
            raise NotImplementedError
        """return the current node value"""

    def find_path(self, tree, letter, path):
        """Find a key"""
        """Recursive function"""
        """Base case 1: letter found - return path"""
        """Base case 2: reached the end of a tree - return False"""
        """General case: update (extend) the path and search the left and/or right subtree"""
        raise NotImplementedError

    def encode(self, msg):
        """Encode a message and return Morse code"""
        code = ''
        for word in msg.split():
            for letter in word:
                # TODO: encode a letter
                raise NotImplementedError
        return code

    def decode(self, code):
        """Decode a message and return a word"""
        msg = ''
        for letter in code.split():
            # TODO: decode each letter/symbol
            raise NotImplementedError
        return msg


if __name__ == '__main__':
    '''Main function'''
    path = 'code_templates/project_morse/'  # change it to fit your IDE
    morse_coder = Coder(path + 'morse.txt')
    print('Encoding "sos"')
    print('Expected: ... --- ...')
    print('Encoding: %s' % morse_coder.encode('sos'))
    print('Encoding "data structures"')
    print('Expected: -.. .- - .- ... - .-. ..- -.-. - ..- .-. . ... ')
    print('Encoding: %s' % morse_coder.encode('data structures'))
    print('Encoding "$$"')
    print('Expected: Error message or none')
    print('Encoding: %s' % morse_coder.encode('$$'))
    print('Decoding ".... . .-.. .-.. --- --..-- -.-. ... .---- -.... -----"')
    print('Expected: hello,cs160')
    print('Decoding: %s' % morse_coder.decode('.... . .-.. .-.. --- --..-- -.-. ... .---- -.... -----'))
