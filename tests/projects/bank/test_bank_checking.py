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
    from src.projects.bank import Address, Customer, CheckingAccount

addresses = [
    ("700 College Dr", "Decorah", "IA", "52101"),
    ("1000 5th Ave", "New York", "NY", "10028"),
]
customer_attributes = "name, dob, address"
customers = [
    ("John Doe", "1861-09-01", Address(*addresses[0])),
    ("Jane Doe", "1861-09-02", Address(*addresses[1])),
]
chk_account_attributes = "owner, fee, balance"
chk_accounts = [(Customer(*customers[0]), 15, 100), (Customer(*customers[1]), 20, 25)]


class TestCheckingAccount:
    """Testing class CheckingAccount"""

    @pytest.mark.parametrize(chk_account_attributes, chk_accounts)
    def test_checking_account(self, owner, fee, balance):
        """Testing checking account properties"""
        chk_account = CheckingAccount(owner, fee, balance)
        assert chk_account.owner == owner
        assert chk_account.balance == pytest.approx(balance, 0.01)

    @pytest.mark.parametrize(chk_account_attributes, chk_accounts)
    def test_account_deposit(self, owner, fee, balance):
        """Testing account.deposit method"""
        chk_account = CheckingAccount(owner, fee, balance)
        amount_to_deposit = 60
        chk_account.deposit(amount_to_deposit)
        assert chk_account.balance == pytest.approx(balance + amount_to_deposit, 0.01)

    @pytest.mark.parametrize(chk_account_attributes, chk_accounts)
    def test_account_deposit_error(self, owner, fee, balance):
        """Testing account.deposit error"""
        chk_account = CheckingAccount(owner, fee, balance)
        amount_to_deposit = -10
        with pytest.raises(ValueError) as excinfo:
            chk_account.deposit(amount_to_deposit)
        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Must deposit positive amount"

    @pytest.mark.parametrize(chk_account_attributes, chk_accounts)
    def test_account_close(self, owner, fee, balance):
        """Testing account.close method"""
        chk_account = CheckingAccount(owner, fee, balance)
        chk_account.close()
        assert chk_account.balance == pytest.approx(0, 0.01)

    @pytest.mark.parametrize(chk_account_attributes, chk_accounts)
    def test_checking_process_check(self, owner, fee, balance):
        """Testing check processing method"""
        chk_account = CheckingAccount(owner, fee, balance)
        assert chk_account.balance == pytest.approx(balance, 0.01)
        amount_to_withdraw = 30
        chk_account.process_check(amount_to_withdraw)
        assert chk_account.balance == pytest.approx(
            balance - amount_to_withdraw
            if balance >= amount_to_withdraw
            else balance - fee,
            0.01,
        )

    @pytest.mark.parametrize(chk_account_attributes, chk_accounts)
    def test_checking_str(self, owner, fee, balance, capsys):
        """Testing checking.__str__ method"""
        chk_account = CheckingAccount(owner, fee, balance)
        print(chk_account)
        out, _ = capsys.readouterr()
        assert out.strip() == (
            f"Checking account\n"
            f"Owner: {chk_account.owner}\n"
            f"Balance: {chk_account.balance:.2f}"
        )


if __name__ == "__main__":
    pytest.main(["-v", __file__])
