# Form a proper line

Implement classes Address, Customer, Account, CheckingAccount, and SavingsAccount. Your program must be properly formatted (use `pylint`) and pass all the tests provided (use `pytest`).

![Bank Classes](bank.png)

## General requirements for all classes

- Implement `__init__`, `__repr__`, `__str__`, and `__eq__` methods.
- Implement access to data members using `properties` with names of the properties being equal to the data member names without the leading underscore (e.g. property `foo` is used to access data member `_foo`).

## Class-specific requirements

1. Class _Address_ has data members `_street`, `_city`, `_state`, and `_zip`. Two addresses are equal if all 4 data members are equal. Property `street` must be mutable (implement `setter`).

1. Class _Customer_ has data members `_name`, `_dob`, and `_address`. `address` is an object of type _Address_. Two customers are equal if all 3 data members are equal. Customers can change address by invoking method `move` with a new address as an argument.

1. _Abstract_ class _Account_ has data members `_owner` and `_balance`. `_owner` is an object of type _Customer_. `_balance` has initial value of 0 and can be changed by invoking methods `deposit` (add money) or `close` (set balance to 0).

1. Class _CheckingAccount_ inherits from class `Account`, has a data member `_insufficient_funds_fee`, and method `process_check`. Two checking accounts are equal if they have the same owner and balance. If the account balance is sufficient too clear the check, the check's `amount` is subtracted from the `balance`, else `_insufficient_balance_fee` is subtracted from the balance (note that this can make the balance negative).

1. Class _SavingsAccount_ has a member `_annual_interest_rate` and method `yield_interest`. Two savings accounts are equal if they have the same owner and balance. Whenever the `yield_interest` method is called, `balance` increases.

## What to do

`python3` should be `python3.9` or newer.

- Read _projects/bank/bank\_description.md_ (this file).
- Modify and run _projects/bank/bank.py_.
- Test your implementation.

```bash
python3 -m pytest projects/bank/bank_test.py
```
