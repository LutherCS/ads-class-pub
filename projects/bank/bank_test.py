#!/usr/bin/env python3
"""
`bank` testing

@authors: Roman Yasinovskyy
@version: 2021.9
"""

import pytest

from bank import Account, Address, Customer, CheckingAccount, SavingsAccount

addresses = [
    ("700 College Dr", "Decorah", "IA", "52101"),
    ("520 W Water St", "Decorah", "IA", "52101"),
    ("1000 5th Ave", "New York", "NY", "10028"),
    ("221B Baker Street", "London", "UK", "NW1 6XE"),
]

customers = [
    ("John Doe", "1861-09-01", ("700 College Dr", "Decorah", "IA", "52101")),
    ("Jane Doe", "1861-09-02", ("700 College Dr", "Decorah", "IA", "52101")),
    ("Sherlock Holmes", "1976-07-19", ("221B Baker Street", "London", "UK", "NW1 6XE")),
    ("Dr. John Watson", "1971-09-08", ("221B Baker Street", "London", "UK", "NW1 6XE")),
]

chk_accounts = [
    (("John Doe", "1861-09-01", ("700 College Dr", "Decorah", "IA", "52101")), 15, 100),
    (("Jane Doe", "1861-09-02", ("1000 5th Ave", "New York", "NY", "10028")), 20, 25),
]

svng_accounts = [
    (
        ("John Doe", "1861-09-01", ("700 College Dr", "Decorah", "IA", "52101")),
        3.5,
        200.00,
    ),
    (("Jane Doe", "1861-09-02", ("1000 5th Ave", "New York", "NY", "10028")), 1.5, 100),
]


class TestAccount:
    """Testing class Account"""

    def test_abstract_class_account(self):
        """Testing account instantiation"""
        with pytest.raises(TypeError) as excinfo:
            self.acc = Account(None, 0)  # pylint: disable=abstract-class-instantiated
        exception_msg = excinfo.value.args[0]
        assert (
            exception_msg
            == "Can't instantiate abstract class Account with abstract method __init__"
        )


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
