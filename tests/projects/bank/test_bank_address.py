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
    from src.projects.bank import Address

addresses = [
    ("700 College Dr", "Decorah", "IA", "52101"),
    ("520 W Water St", "Decorah", "IA", "52101"),
    ("1000 5th Ave", "New York", "NY", "10028"),
    ("221B Baker Street", "London", "UK", "NW1 6XE"),
]


class TestAddress:
    """Testing class Address"""

    @pytest.mark.parametrize("street, city, state, zip_code", addresses)
    def test_address_init(self, street, city, state, zip_code):
        """Testing address constructor"""
        address = Address(street, city, state, zip_code)
        assert isinstance(address, Address)

    @pytest.mark.parametrize("street, city, state, zip_code", addresses)
    def test_address_members(self, street, city, state, zip_code):
        """Testing address properties"""
        address = Address(street, city, state, zip_code)
        assert address.street == street
        assert address.city == city
        assert address.state == state
        assert address.zip == zip_code

    @pytest.mark.parametrize("street, city, state, zip_code", addresses)
    def test_address_repr(self, street, city, state, zip_code):
        """Testing address.__repr__ method"""
        address = Address(street, city, state, zip_code)
        assert repr(address) == f"Address({street}, {city}, {state}, {zip_code})"

    @pytest.mark.parametrize("street, city, state, zip_code", addresses)
    def test_address_str(self, street, city, state, zip_code):
        """Testing address.__str__ method"""
        address = Address(street, city, state, zip_code)
        assert str(address) == f"{street}\n{city}, {state} {zip_code}"

    @pytest.mark.parametrize("street, city, state, zip_code", addresses)
    def test_address_eq(self, street, city, state, zip_code):
        """Testing address.__eq__ method"""
        address1 = Address(street, city, state, zip_code)
        address2 = Address(street, city, state, zip_code)
        assert address1 == address2
        assert address1 is not address2

    @pytest.mark.parametrize("street, city, state, zip_code", addresses)
    def test_address_street_setter(self, street, city, state, zip_code):
        """Testing address.set_street method"""
        address = Address(street, city, state, zip_code)
        assert address.street == street
        address.street = "1861 College Dr"
        assert address.street == "1861 College Dr"


if __name__ == "__main__":
    pytest.main(["-v", __file__])
