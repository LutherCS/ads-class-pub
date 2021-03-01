# Form a proper line

Implement classes Address, Customer, Account, CheckingAccount, and SavingsAccount. Your program must be properly formatted (use pylint) and pass all the tests provided (use pytest).

![Bank Classes](bank.png)

## General requirements for all classes

- Implement `__init__` and `__str__` methods.

- Implement all data members as properties.

## Class-specific requirements

1. Class _Address_ has members `_street`, `_city`, `_state`, `_zip`, and `__eq__`. Two addresses are equal if all 4 properties are equal.

1. Class _Customer_ has members `_name`, `_dob`, and `_address`. The `_address` is an object of type _Address_. Customers can change address by invoking method `move`.

1. Class _Account_ is **abstract** and has members `_owner` and `_balance`. The `_owner` is an object of type _Customer_. The `_balance` has initial value of 0 and can be changed by invoking methods `deposit` (add money) or `close` (set balance to 0).

1. Class _CheckingAccount_ has a member `_insufficient_funds_fee` and method `process_check`. If the account balance is too low to clear the check, the `_insufficient_balance_fee` is subtracted from the balance (note that the balance can be negative).

1. Class _SavingsAccount_ has a member `_annual_interest_rate` and method `yield_interest`.

## What to do

`python3` should be `python3.9` or newer.

- Read _src/projects/bank/description.md_ (this file).
- Modify _src/projects/bank/bank_classes.py_.
- Test your implementation.

```bash
python3 -m pytest tests/projects/bank/test_bank_account.py
python3 -m pytest tests/projects/bank/test_bank_address.py
python3 -m pytest tests/projects/bank/test_bank_checking.py
python3 -m pytest tests/projects/bank/test_bank_customer.py
python3 -m pytest tests/projects/bank/test_bank_savings.py
```
