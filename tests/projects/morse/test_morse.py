"""
Testing the module morse
Karina Hoff, 2018
"""
#!/usr/bin/python3

import pytest
from projects.morse import Coder


class TestMorseMethods:
    """Testing module morse"""

    @pytest.fixture(scope="function", autouse=True)
    def setup_class(self):
        """Setting up"""
        self.the_tree = Coder("data/projects/morse/morse.txt")

    def test_init_error(self):
        """Test __init__ error"""
        with pytest.raises(Exception) as excinfo:
            tree = Coder()  # pylint: disable=no-value-for-parameter, unused-variable
        exception_message = excinfo.value.args[0]
        assert (
            exception_message
            == "__init__() missing 1 required positional argument: 'file_in'"
        )

    def test_find_path(self):
        """Test find_path"""
        assert self.the_tree.find_path(self.the_tree.morse_tree, "e", "") == "."
        assert not self.the_tree.find_path(self.the_tree.morse_tree, "$", "")

    def test_follow_and_retrieve(self):
        """Test follow_and_retrieve"""
        assert self.the_tree.follow_and_retrieve("-.-.") == "c"
        assert self.the_tree.follow_and_retrieve("...") == "s"
        assert not self.the_tree.follow_and_retrieve("-.-..") == "ć"
        assert not self.the_tree.follow_and_retrieve("...-...") == "ś"

    def test_follow_and_insert(self):
        """Test follow_and_insert"""
        self.the_tree.follow_and_insert("-.-..", "ć")
        assert self.the_tree.follow_and_retrieve("-.-..") == "ć"
        self.the_tree.follow_and_insert("...-...", "ś")
        assert self.the_tree.follow_and_retrieve("...-...") == "ś"

    def test_follow_and_insert_replacement(self):
        """Test follow_and_insert with replacement"""
        self.the_tree.follow_and_insert(".", "CS160")
        assert self.the_tree.follow_and_retrieve(".") == "CS160"
        assert not self.the_tree.follow_and_retrieve(".") == "e"

    def test_encode(self):
        """Test encoding"""
        assert self.the_tree.encode("sos") == "... --- ... "

    def test_encode_error(self):
        """Test encoding error"""
        with pytest.raises(ValueError) as excinfo:
            self.the_tree.encode("$$")
        exception_message = excinfo.value.args[0]
        assert (
            exception_message
            == "Could not encode $$: $ is not in the tree"
        )

    def test_decode(self):
        """Test decode"""
        assert self.the_tree.decode("... --- ...") == "sos"

    def test_decode_error(self):
        """Test decoding error"""
        with pytest.raises(ValueError) as excinfo:
            self.the_tree.decode("...---...")
        exception_message = excinfo.value.args[0]
        assert (
            exception_message
            == "Could not decode ...---...: ...---... is not in the tree"
        )

if __name__ == "__main__":
    pytest.main(["test_morse.py"])

