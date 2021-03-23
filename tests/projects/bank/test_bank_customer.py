#!/usr/bin/env python3
"""
`bank` testing

@authors: Roman Yasinovskyy
@version: 2021.3
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
    from src.projects.bank import Address, Customer


customers = [
    ("John Doe", "1861-09-01", ("700 College Dr", "Decorah", "IA", "52101")),
    ("Jane Doe", "1861-09-02", ("700 College Dr", "Decorah", "IA", "52101")),
    ("Sherlock Holmes", "1976-07-19", ("221B Baker Street", "London", "UK", "NW1 6XE")),
    ("Dr. John Watson", "1971-09-08", ("221B Baker Street", "London", "UK", "NW1 6XE")),
]


class TestCustomer:
    """Testing class Customer"""

    @pytest.mark.parametrize("name, dob, address", customers)
    def test_customer_init(self, name, dob, address):
        """Testing customer properties"""
        address = Address(*address)
        customer = Customer(name, dob, address)
        assert customer.name == name
        assert customer.dob == dob
        assert customer.address == address

    @pytest.mark.parametrize("name, dob, address", customers)
    def test_customer_repr(self, name, dob, address):
        """Testing customer.__repr__ method"""
        address = Address(*address)
        customer = Customer(name, dob, address)
        assert repr(customer) == (f"Customer({name}, {dob}, {address})")

    @pytest.mark.parametrize("name, dob, address", customers)
    def test_customer_str(self, name, dob, address):
        """Testing customer.__str__ method"""
        address = Address(*address)
        customer = Customer(name, dob, address)
        assert str(customer) == (f"{name} ({dob})\n{address}")

    @pytest.mark.parametrize("name, dob, address", customers)
    def test_customer_eq(self, name, dob, address):
        """Testing address.__eq__ method"""
        address = Address(*address)
        customer1 = Customer(name, dob, address)
        customer2 = Customer(name, dob, address)
        assert customer1 == customer2
        assert customer1 is not customer2

    @pytest.mark.parametrize("name, dob, address", customers)
    def test_customer_move(self, name, dob, address):
        """Testing customer.move method"""
        address = Address(*address)
        customer = Customer(name, dob, address)
        new_address = Address("1000 5th Ave", "New York", "NY", "10028")
        customer.move(new_address)
        assert customer.address == Address("1000 5th Ave", "New York", "NY", "10028")
        assert str(customer) == (f"{name} ({dob})\n{str(new_address)}")


if __name__ == "__main__":
    pytest.main(["-v", __file__])
