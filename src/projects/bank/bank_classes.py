#!/usr/bin/env python3
"""
`bank` implementation

@author:
"""

from abc import ABC, abstractmethod


class Address:
    """Address class"""

    def __init__(
        self, street_init: str, city_init: str, state_init: str, zip_init: str
    ):
        """__init__"""
        raise NotImplementedError

    # TODO: Implement data members as properties

    def __eq__(self, other: object):
        """Compare 2 addresses"""
        raise NotImplementedError

    def __str__(self):
        """__str method"""
        raise NotImplementedError


class Customer:
    """Customer class"""

    def __init__(self, name_init: str, dob_init: str, address_init: object):
        """Constructor"""
        raise NotImplementedError

    # TODO: Implement data members as properties

    def move(self, new_address: object):
        """Change address"""
        raise NotImplementedError

    def __str__(self):
        """__str"""
        raise NotImplementedError


class Account(ABC):
    """Account class"""

    @abstractmethod
    def __init__(self, owner_init: object, balance_init: float = 0):
        """Constructor"""
        raise NotImplementedError

    # TODO: Implement data members as properties

    def deposit(self, amount: float):
        """Add money"""
        raise NotImplementedError

    def close(self):
        """Close account"""
        raise NotImplementedError

    def __str__(self):
        """__str__"""
        raise NotImplementedError


class CheckingAccount(Account):
    """CheckingAccount class"""

    def __init__(self, owner_init: object, fee_init: float, balance_init: float = 0):
        """Constructor"""
        raise NotImplementedError

    def process_check(self, amount: float):
        """Process a check"""
        raise NotImplementedError

    def __str__(self):
        """__str__"""
        raise NotImplementedError


class SavingsAccount(Account):
    """CheckingAccount class"""

    def __init__(
        self, owner_init: object, interest_rate_init: float, balance_init: float = 0
    ):
        """Constructor"""
        raise NotImplementedError

    def yield_interest(self):
        """Yield annual interest"""
        raise NotImplementedError

    def __str__(self):
        """__str__"""
        raise NotImplementedError
