#!/usr/bin/python3
"""
Testing the class Account
@authors: Roman Yasinovskyy
@updated: 2019
"""
import pytest
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
            == "Can't instantiate abstract class Account with abstract methods __init__"
        )


if __name__ == "__main__":
    pytest.main(["-v", "test_bank.py"])
