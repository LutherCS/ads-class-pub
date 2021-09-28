#!/usr/bin/env python3
"""
`bank` implementation and driver

@authors: Roman Yasinovskyy
@version: 2021.9
"""

from abc import ABC, abstractmethod
from decimal import Decimal


class Address:
    """Class Address"""

    def __init__(self, street: str, city: str, state: str, zip_code: str) -> None:
        """Initializer"""
        # TODO: Implement this method
        ...

    # TODO: Implement data members as properties
    ...

    def __repr__(self) -> str:
        """Address representation"""
        # TODO: Implement this method
        ...

    def __str__(self) -> str:
        """Address as a string"""
        # TODO: Implement this method
        ...

    def __eq__(self, other: object) -> bool:
        """Address comparison"""
        # TODO: Implement this method
        ...


class Customer:
    """Class Customer"""

    def __init__(self, name_init: str, dob_init: str, address_init: Address) -> None:
        """Initializer"""
        # TODO: Implement this method
        ...

    # TODO: Implement data members as properties
    ...

    def __repr__(self) -> str:
        """Customer representation"""
        # TODO: Implement this method
        ...

    def __str__(self) -> str:
        """Customer as a string"""
        # TODO: Implement this method
        ...

    def __eq__(self, other: object) -> bool:
        """Customer comparison"""
        # TODO: Implement this method
        ...

    def move(self, new_address: Address) -> None:
        """Change address"""
        # TODO: Implement this method
        ...


class Account(ABC):
    """Class Account"""

    @abstractmethod
    def __init__(self, owner: Customer, balance: Decimal = Decimal(0)):
        """Initializer"""
        # TODO: Implement this method
        ...

    # TODO: Implement data members as properties
    ...

    def __repr__(self) -> str:
        """Account representation"""
        # TODO: Implement this method
        ...

    def __str__(self) -> str:
        """Account as a string"""
        # TODO: Implement this method
        ...

    def __eq__(self, other: object) -> bool:
        """Accounts comparison"""
        # TODO: Implement this method
        ...

    def deposit(self, amount: Decimal) -> None:
        """Add money"""
        # TODO: Implement this method
        ...

    def close(self) -> None:
        """Close account"""
        # TODO: Implement this method
        ...


class CheckingAccount(Account):
    """Class CheckingAccount"""

    def __init__(self, owner: Customer, fee: Decimal, balance: Decimal = Decimal(0)):
        """Initializer"""
        # TODO: Implement this method
        ...

    # TODO: Implement data members as properties
    ...

    def __repr__(self) -> str:
        """Checking account representation"""
        # TODO: Implement this method
        ...

    def __str__(self):
        """Checking account as a string"""
        # TODO: Implement this method
        ...

    def __eq__(self, other: object) -> bool:
        """Checking accounts comparison"""
        # TODO: Implement this method
        ...

    def process_check(self, amount: Decimal) -> None:
        """Processing a check"""
        # TODO: Implement this method
        ...


class SavingsAccount(Account):
    """Class SavingsAccount"""

    def __init__(
        self, owner: Customer, interest_rate: Decimal, balance: Decimal = Decimal(0)
    ):
        """Initializer"""
        # TODO: Implement this method
        ...

    # TODO: Implement data members as properties
    ...

    def yield_interest(self) -> None:
        """Yield annual interest"""
        # TODO: Implement this method
        ...

    def __repr__(self) -> str:
        """Savings account representation"""
        # TODO: Implement this method
        ...

    def __str__(self):
        """Savings account as a string"""
        # TODO: Implement this method
        ...

    def __eq__(self, other: object) -> bool:
        """Savings accounts comparison"""
        # TODO: Implement this method
        ...


def main():
    """Entry point"""
    addr1 = Address("700 College Dr", "Decorah", "IA", "52101")
    addr2 = Address("100 Water St", "Decorah", "IA", "52101")

    print("Customer")
    cust = Customer("John Doe", "2021-03-11", addr1)
    print(cust)
    print("Customer moved")
    cust.move(addr2)
    print(cust)
    print("Address changed")
    addr2._street = "100 Short St"
    print(cust)


if __name__ == "__main__":
    main()
