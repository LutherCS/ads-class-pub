#!/usr/bin/python3
"""
Testing the class Address
@authors: Roman Yasinovskyy
@updated: 2019
"""

import pytest
from src.projects.bank import Address

address_attributes = "street, city, state, zip_code"
addresses = [
    ("700 College Dr", "Decorah", "IA", "52101"),
    ("520 W Water St", "Decorah", "IA", "52101"),
    ("1000 5th Ave", "New York", "NY", "10028"),
    ("221B Baker Street", "London", "UK", "NW1 6XE"),
]


class TestAddress:
    """Testing class Address"""

    @pytest.mark.parametrize(address_attributes, addresses)
    def test_address_init(self, street, city, state, zip_code):
        """Testing address properties"""
        address = Address(street, city, state, zip_code)
        assert address.street == street
        assert address.city == city
        assert address.state == state
        assert address.zip == zip_code

    @pytest.mark.parametrize(address_attributes, addresses)
    def test_address_str(self, street, city, state, zip_code, capsys):
        """Testing address.__str__ method"""
        address = Address(street, city, state, zip_code)
        print(address)
        out, err = capsys.readouterr()
        assert out.strip() == (f"{street}\n{city}, {state} {zip_code}")
        assert err == ""

    @pytest.mark.parametrize(address_attributes, addresses)
    def test_address_eq(self, street, city, state, zip_code):
        """Testing address.__eq__ method"""
        address1 = Address(street, city, state, zip_code)
        address2 = Address(street, city, state, zip_code)
        assert address1 == address2
        assert address1 is not address2


if __name__ == "__main__":
    pytest.main(["-v", "test_bank_address.py"])
