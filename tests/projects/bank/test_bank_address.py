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
    pytest.main(["-v", __file__])
