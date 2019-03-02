#!/usr/bin/python3
"""
Testing the class Customer
@authors: Roman Yasinovskyy
@updated: 2019
"""

import pytest
from src.projects.bank import Address, Customer

addresses = [
    ("700 College Dr", "Decorah", "IA", "52101"),
    ("221B Baker Street", "London", "UK", "NW1 6XE"),
]
customer_attributes = "name, dob, address"
customers = [
    ("John Doe", "1861-09-01", Address(*addresses[0])),
    ("Jane Doe", "1861-09-02", Address(*addresses[0])),
    ("Sherlock Holmes", "1976-07-19", Address(*addresses[1])),
    ("Dr. John Watson", "1971-09-08", Address(*addresses[1])),
]


class TestCustomer:
    """Testing class Customer"""

    @pytest.mark.parametrize(customer_attributes, customers)
    def test_customer_init(self, name, dob, address):
        """Testing customer properties"""
        customer = Customer(name, dob, address)
        assert customer.name == name
        assert customer.dob == dob
        assert customer.address == address

    @pytest.mark.parametrize(customer_attributes, customers)
    def test_customer_str(self, name, dob, address):
        """Testing customer.__str__ method"""
        customer = Customer(name, dob, address)
        assert str(customer) == (f"{name} ({dob})\n{address}")

    @pytest.mark.parametrize(customer_attributes, customers)
    def test_customer_move(self, name, dob, address):
        """Testing customer.move method"""
        customer = Customer(name, dob, address)
        new_address = Address("1000 5th Ave", "New York", "NY", "10028")
        customer.move(new_address)
        assert customer.address == Address("1000 5th Ave", "New York", "NY", "10028")
        assert str(customer) == (f"{name} ({dob})\n{str(new_address)}")


if __name__ == "__main__":
    pytest.main(["-v", "test_bank.py"])
