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
    from src.projects.bank import Address, Customer, SavingsAccount

addresses = [
    ("700 College Dr", "Decorah", "IA", "52101"),
    ("1000 5th Ave", "New York", "NY", "10028"),
]
customer_attributes = "name, dob, address"
customers = [
    ("John Doe", "1861-09-01", Address(*addresses[0])),
    ("Jane Doe", "1861-09-02", Address(*addresses[1])),
]
svng_account_attributes = "owner, rate, balance"
svng_accounts = [
    (Customer(*customers[0]), 3.5, 200.00),
    (Customer(*customers[1]), 1.5, 100),
]


class TestSavingsAccount:
    """Testing class SavingsAccount"""

    @pytest.mark.parametrize(svng_account_attributes, svng_accounts)
    def test_savings_account(self, owner, rate, balance):
        """Testing savings account properties"""
        svng_account = SavingsAccount(owner, rate, balance)
        assert svng_account.owner == owner
        assert svng_account.balance == pytest.approx(balance, 0.01)

    @pytest.mark.parametrize(svng_account_attributes, svng_accounts)
    def test_account_deposit(self, owner, rate, balance):
        """Testing account.deposit method"""
        svng_account = SavingsAccount(owner, rate, balance)
        amount_to_deposit = 60
        svng_account.deposit(amount_to_deposit)
        assert svng_account.balance == pytest.approx(balance + amount_to_deposit, 0.01)

    @pytest.mark.parametrize(svng_account_attributes, svng_accounts)
    def test_account_deposit_error(self, owner, rate, balance):
        """Testing account.deposit error"""
        svng_account = SavingsAccount(owner, rate, balance)
        amount_to_deposit = -10
        with pytest.raises(ValueError) as excinfo:
            svng_account.deposit(amount_to_deposit)
        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Must deposit positive amount"

    @pytest.mark.parametrize(svng_account_attributes, svng_accounts)
    def test_account_close(self, owner, rate, balance):
        """Testing account.close method"""
        svng_account = SavingsAccount(owner, rate, balance)
        svng_account.close()
        assert svng_account.balance == pytest.approx(0, 0.01)

    @pytest.mark.parametrize(svng_account_attributes, svng_accounts)
    def test_savings_yield_interest(self, owner, rate, balance):
        """Testing check processing method"""
        svng_account = SavingsAccount(owner, rate, balance)
        assert svng_account.balance == pytest.approx(balance, 0.01)
        svng_account.yield_interest()
        assert svng_account.balance == pytest.approx(balance * (1 + rate / 100), 0.01)

    @pytest.mark.parametrize(svng_account_attributes, svng_accounts)
    def test_savings_str(self, owner, rate, balance, capsys):
        """Testing savings.__str__ method"""
        svng_account = SavingsAccount(owner, rate, balance)
        print(svng_account)
        out, _ = capsys.readouterr()
        assert out.strip() == (
            f"Savings account\n"
            f"Owner: {svng_account.owner}\n"
            f"Balance: {svng_account.balance:.2f}"
        )


if __name__ == "__main__":
    pytest.main(["-v", __file__])
