#!/usr/bin/env python3
"""
`bank` testing

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
    from src.projects.bank import Account


class TestAccount:
    """Testing class Account"""

    def test_abstract_class_account(self):
        """Testing account instantiation"""
        with pytest.raises(TypeError) as excinfo:
            self.acc = Account(None, 0)  # pylint: disable=abstract-class-instantiated
        exception_msg = excinfo.value.args[0]
        assert (
            exception_msg
            == "Can't instantiate abstract class Account with abstract method __init__"
        )


if __name__ == "__main__":
    pytest.main(["-v", __file__])
