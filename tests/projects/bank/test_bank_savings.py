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
    from src.projects.bank import Address, Customer, SavingsAccount


svng_accounts = [
    (
        ("John Doe", "1861-09-01", ("700 College Dr", "Decorah", "IA", "52101")),
        3.5,
        200.00,
    ),
    (("Jane Doe", "1861-09-02", ("1000 5th Ave", "New York", "NY", "10028")), 1.5, 100),
]


class TestSavingsAccount:
    """Testing class SavingsAccount"""

    @pytest.mark.parametrize("owner, rate, balance", svng_accounts)
    def test_savings_account_init(self, owner, rate, balance):
        """Testing savings account properties"""
        address = Address(*owner[2])
        customer = Customer(owner[0], owner[1], address)
        svng_account = SavingsAccount(customer, rate, balance)
        assert svng_account.owner == customer
        assert svng_account.balance == pytest.approx(balance, 0.01)

    @pytest.mark.parametrize("owner, rate, balance", svng_accounts)
    def test_savings_account_repr(self, owner, rate, balance):
        """Testing savings.__repr__ method"""
        address = Address(*owner[2])
        customer = Customer(owner[0], owner[1], address)
        svng_account = SavingsAccount(customer, rate, balance)
        assert repr(svng_account) == f"SavingsAccount({customer}, {rate}, {balance})"

    @pytest.mark.parametrize("owner, rate, balance", svng_accounts)
    def test_savings_account_str(self, owner, rate, balance):
        """Testing savings.__str__ method"""
        address = Address(*owner[2])
        customer = Customer(owner[0], owner[1], address)
        svng_account = SavingsAccount(customer, rate, balance)
        assert str(svng_account) == (
            f"Savings account\n"
            f"Owner: {svng_account.owner}\n"
            f"Balance: {svng_account.balance:.2f}"
        )

    @pytest.mark.parametrize("owner, rate, balance", svng_accounts)
    def test_savings_account_eq(self, owner, rate, balance):
        """Testing savings.__eq__ method"""
        address = Address(*owner[2])
        customer = Customer(owner[0], owner[1], address)
        svng_account1 = SavingsAccount(customer, rate, balance)
        svng_account2 = SavingsAccount(customer, rate, balance)
        assert svng_account1 == svng_account2
        assert svng_account1 is not svng_account2

    @pytest.mark.parametrize("owner, rate, balance", svng_accounts)
    def test_savings_account_deposit(self, owner, rate, balance):
        """Testing account.deposit method"""
        address = Address(*owner[2])
        customer = Customer(owner[0], owner[1], address)
        svng_account = SavingsAccount(customer, rate, balance)
        amount_to_deposit = 60
        svng_account.deposit(amount_to_deposit)
        assert svng_account.balance == pytest.approx(balance + amount_to_deposit, 0.01)

    @pytest.mark.parametrize("owner, rate, balance", svng_accounts)
    def test_savings_account_deposit_error(self, owner, rate, balance):
        """Testing account.deposit error"""
        address = Address(*owner[2])
        customer = Customer(owner[0], owner[1], address)
        svng_account = SavingsAccount(customer, rate, balance)
        amount_to_deposit = -10
        with pytest.raises(ValueError) as excinfo:
            svng_account.deposit(amount_to_deposit)
        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Must deposit positive amount"

    @pytest.mark.parametrize("owner, rate, balance", svng_accounts)
    def test_savings_account_close(self, owner, rate, balance):
        """Testing account.close method"""
        address = Address(*owner[2])
        customer = Customer(owner[0], owner[1], address)
        svng_account = SavingsAccount(customer, rate, balance)
        svng_account.close()
        assert svng_account.balance == pytest.approx(0, 0.01)

    @pytest.mark.parametrize("owner, rate, balance", svng_accounts)
    def test_savings_account_yield_interest(self, owner, rate, balance):
        """Testing check processing method"""
        address = Address(*owner[2])
        customer = Customer(owner[0], owner[1], address)
        svng_account = SavingsAccount(customer, rate, balance)
        assert svng_account.balance == pytest.approx(balance, 0.01)
        svng_account.yield_interest()
        assert svng_account.balance == pytest.approx(balance * (1 + rate / 100), 0.01)


if __name__ == "__main__":
    pytest.main(["-v", __file__])
