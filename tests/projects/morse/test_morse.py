#!/usr/bin/env python3
"""
`morse` testing

@authors: Roman Yasinovskyy, Karina Hoff
@version: 2021.4
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
    from src.projects.morse import Coder


@pytest.fixture()
def the_tree():
    """Setting up"""
    return Coder("data/projects/morse/morse.txt")


def test_init():
    """Test __init__ error"""
    the_coder = Coder("data/projects/morse/morse.txt")
    assert isinstance(the_coder, Coder)


def test_init_error():
    """Test __init__ error"""
    with pytest.raises(Exception) as excinfo:
        tree = Coder()  # pylint: disable=no-value-for-parameter, unused-variable
    exception_message = excinfo.value.args[0]
    assert (
        exception_message
        == "__init__() missing 1 required positional argument: 'file_in'"
    )


@pytest.mark.parametrize(
    "code, letter", [("-.-..", "ć"), ("...-...", "ś"), (".", "CS160"), ("-", "-")]
)
def test_follow_and_insert(the_tree: Coder, code: str, letter: str):
    """Test follow_and_insert"""
    the_tree.follow_and_insert(code, letter)
    assert the_tree.follow_and_retrieve(code) == letter


@pytest.mark.parametrize(
    "code, letter", [(".", "e"), ("...", "s"), ("---", "o"), ("-.-.", "c")]
)
def test_follow_and_retrieve(the_tree: Coder, code: str, letter: str):
    """Test follow_and_retrieve"""
    assert the_tree.follow_and_retrieve(code) == letter


@pytest.mark.parametrize("code", ["-.-..", "...-..."])
def test_follow_and_retrieve_error(the_tree: Coder, code: str):
    """Test follow_and_retrieve error"""
    with pytest.raises(ValueError) as excinfo:
        the_tree.follow_and_retrieve(code)
    exception_message = excinfo.value.args[0]
    assert exception_message == f"Could not find {code} in the tree"


@pytest.mark.parametrize(
    "letter, code", [("e", "."), ("s", "..."), ("o", "---"), ("z", "--..")]
)
def test_find_path(the_tree: Coder, letter: str, code: str):
    """Test find_path"""
    assert the_tree.find_path(the_tree.morse_tree, letter, "") == code


@pytest.mark.parametrize("letter", ["$", "%", "@", "#"])
def test_find_path_error(the_tree: Coder, letter: str):
    """Test find_path error"""
    assert not the_tree.find_path(the_tree.morse_tree, letter, "")


@pytest.mark.parametrize(
    "text, code",
    [
        ("sos", "... --- ..."),
        ("logarithms", ".-.. --- --. .- .-. .. - .... -- ..."),
        ("algorithms", ".- .-.. --. --- .-. .. - .... -- ..."),
        ("data structures", "-.. .- - .- ... - .-. ..- -.-. - ..- .-. . ..."),
    ],
)
def test_encode(the_tree: Coder, text: str, code: str):
    """Test encoding"""
    assert the_tree.encode(text) == code


@pytest.mark.parametrize(
    "text, symbol", [("HELLO", "H"), ("$$", "$"), ("m@c", "@"), ("Luther", "L")]
)
def test_encode_error(the_tree: Coder, text: str, symbol: str):
    """Test encoding error"""
    with pytest.raises(ValueError) as excinfo:
        the_tree.encode(text)
    exception_message = excinfo.value.args[0]
    assert exception_message == f"Could not encode {text}: {symbol} is not in the tree"


@pytest.mark.parametrize(
    "code, text",
    [
        ("... --- ...", "sos"),
        (".-.. --- --. .- .-. .. - .... -- ...", "logarithms"),
        (".- .-.. --. --- .-. .. - .... -- ...", "algorithms"),
        ("-.. .- - .- ..--.- ... - .-. ..- -.-. - ..- .-. . ...", "data_structures"),
    ],
)
def test_decode(the_tree: Coder, code: str, text: str):
    """Test decode"""
    assert the_tree.decode(code) == text


@pytest.mark.parametrize(
    "code, symbol",
    [
        ("...---...", "...---..."),
        ("......", "......"),
        ("------", "------"),
        (".-.-.-.-", ".-.-.-.-"),
    ],
)
def test_decode_error(the_tree: Coder, code: str, symbol: str):
    """Test decoding error"""
    with pytest.raises(ValueError) as excinfo:
        the_tree.decode(code)
    exception_message = excinfo.value.args[0]
    assert exception_message == f"Could not decode {code}: {symbol} is not in the tree"


if __name__ == "__main__":
    pytest.main(["-v", __file__])
