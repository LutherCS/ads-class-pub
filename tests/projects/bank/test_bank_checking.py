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
    from src.projects.bank import Address, Customer, CheckingAccount


chk_accounts = [
    (("John Doe", "1861-09-01", ("700 College Dr", "Decorah", "IA", "52101")), 15, 100),
    (("Jane Doe", "1861-09-02", ("1000 5th Ave", "New York", "NY", "10028")), 20, 25),
]


class TestCheckingAccount:
    """Testing class CheckingAccount"""

    @pytest.mark.parametrize("owner, fee, balance", chk_accounts)
    def test_checking_account_init(self, owner, fee, balance):
        """Testing checking account properties"""
        address = Address(*owner[2])
        customer = Customer(owner[0], owner[1], address)
        chk_account = CheckingAccount(customer, fee, balance)
        assert chk_account.owner == customer
        assert chk_account.balance == pytest.approx(balance, 0.01)

    @pytest.mark.parametrize("owner, fee, balance", chk_accounts)
    def test_checking_account_repr(self, owner, fee, balance):
        """Testing checking.__repr__ method"""
        address = Address(*owner[2])
        customer = Customer(owner[0], owner[1], address)
        chk_account = CheckingAccount(customer, fee, balance)
        assert repr(chk_account) == f"CheckingAccount({customer}, {fee}, {balance})"

    @pytest.mark.parametrize("owner, fee, balance", chk_accounts)
    def test_checking_account_str(self, owner, fee, balance):
        """Testing checking.__str__ method"""
        address = Address(*owner[2])
        customer = Customer(owner[0], owner[1], address)
        chk_account = CheckingAccount(customer, fee, balance)
        assert str(chk_account) == (
            f"Checking account\n"
            f"Owner: {chk_account.owner}\n"
            f"Balance: {chk_account.balance:.2f}"
        )

    @pytest.mark.parametrize("owner, fee, balance", chk_accounts)
    def test_checking_account_eq(self, owner, fee, balance):
        """Testing checking.__eq__ method"""
        address = Address(*owner[2])
        customer = Customer(owner[0], owner[1], address)
        chk_account1 = CheckingAccount(customer, fee, balance)
        chk_account2 = CheckingAccount(customer, fee, balance)
        assert chk_account1 == chk_account2
        assert chk_account1 is not chk_account2

    @pytest.mark.parametrize("owner, fee, balance", chk_accounts)
    def test_checking_account_deposit(self, owner, fee, balance):
        """Testing account.deposit method"""
        address = Address(*owner[2])
        customer = Customer(owner[0], owner[1], address)
        chk_account = CheckingAccount(customer, fee, balance)
        amount_to_deposit = 60
        chk_account.deposit(amount_to_deposit)
        assert chk_account.balance == pytest.approx(balance + amount_to_deposit, 0.01)

    @pytest.mark.parametrize("owner, fee, balance", chk_accounts)
    def test_checking_account_deposit_error(self, owner, fee, balance):
        """Testing account.deposit error"""
        address = Address(*owner[2])
        customer = Customer(owner[0], owner[1], address)
        chk_account = CheckingAccount(customer, fee, balance)
        amount_to_deposit = -10
        with pytest.raises(ValueError) as excinfo:
            chk_account.deposit(amount_to_deposit)
        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Must deposit positive amount"

    @pytest.mark.parametrize("owner, fee, balance", chk_accounts)
    def test_checking_account_close(self, owner, fee, balance):
        """Testing account.close method"""
        address = Address(*owner[2])
        customer = Customer(owner[0], owner[1], address)
        chk_account = CheckingAccount(customer, fee, balance)
        chk_account.close()
        assert chk_account.balance == pytest.approx(0, 0.01)

    @pytest.mark.parametrize("owner, fee, balance", chk_accounts)
    def test_checking_process_check(self, owner, fee, balance):
        """Testing check processing method"""
        address = Address(*owner[2])
        customer = Customer(owner[0], owner[1], address)
        chk_account = CheckingAccount(customer, fee, balance)
        assert chk_account.balance == pytest.approx(balance, 0.01)
        amount_to_withdraw = 30
        chk_account.process_check(amount_to_withdraw)
        assert chk_account.balance == pytest.approx(
            balance - amount_to_withdraw
            if balance >= amount_to_withdraw
            else balance - fee,
            0.01,
        )


if __name__ == "__main__":
    pytest.main(["-v", __file__])
