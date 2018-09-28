'''
Testing the module Bank
Roman Yasinovskyy, 2017
'''

#!/usr/bin/python3


import pytest
from projects.bank.bank import Address, Customer, Account, CheckingAccount, SavingsAccount


class TestBankingMethods:
    '''Testing module banking'''

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self):
        '''Setting up'''
        self.addr1 = Address('700 College Dr', 'Decorah', 'IA', '52101')
        self.addr2 = Address('1000 5th Ave', 'New York', 'NY', '10028')
        self.addr3 = Address('700 College Dr', 'Decorah', 'IA', '52101')
        self.customer1 = Customer('John Doe', '1861-09-01', self.addr1)
        self.customer2 = Customer('Jane Doe', '1861-09-02', self.addr1)
        self.check_acc = CheckingAccount(self.customer1, 15.00, 100.00)
        self.save_acc = SavingsAccount(self.customer2, 3.5, 200.00)

    def test_address(self):
        '''Testing address properties'''
        assert self.addr1.street == '700 College Dr'
        assert self.addr1.city == 'Decorah'
        assert self.addr1.state == 'IA'
        assert self.addr1.zip == '52101'

    def test_address_str(self, capsys):
        '''Testing address.__str__ method'''
        print(self.addr1)
        out, err = capsys.readouterr()
        assert out.strip() == ('700 College Dr\nDecorah, IA 52101')

    def test_address_eq(self):
        '''Testing address.__eq__ method'''
        assert self.addr1 != self.addr2
        assert self.addr1 is not self.addr3
        assert self.addr1 == self.addr3

    def test_customer(self):
        '''Testing customer properties'''
        assert self.customer1.name == 'John Doe'
        assert self.customer1.dob == '1861-09-01'
        assert self.customer1.address == Address('700 College Dr', 'Decorah', 'IA', '52101')

    def test_customer_str(self, capsys):
        '''Testing customer.__str__ method'''
        print(self.customer1)
        out, err = capsys.readouterr()
        assert out.strip() == ('John Doe (1861-09-01)\n' +
                              '700 College Dr\nDecorah, IA 52101')

    def test_customer_move(self, capsys):
        '''Testing customer.move method'''
        self.customer1.move(self.addr2)
        assert self.customer1.address == Address('1000 5th Ave', 'New York', 'NY', '10028')
        print(self.customer1)
        out, err = capsys.readouterr()
        assert out.strip() == ('John Doe (1861-09-01)\n' +
                               '1000 5th Ave\n' +
                               'New York, NY 10028')

    #Raises TypeError -- Account is abstract, cannot be instantiated
    def test_abstract_class_Account(self):
        with pytest.raises(TypeError) as excinfo:
            self.acc = Account(self.customer1, 500)
        exception_msg = excinfo.value.args[0]
        assert exception_msg == 'Can\'t instantiate abstract class Account with abstract methods __init__'

    def test_account(self):
        '''Testing account properties'''
        assert self.check_acc.owner == self.customer1
        assert self.save_acc.owner == self.customer2
        assert self.check_acc.balance == pytest.approx(100, 0.01)
        assert self.save_acc.balance == pytest.approx(200, 0.01)

    def test_account_deposit(self):
        '''Testing account.deposit method'''
        self.check_acc.deposit(60)
        assert self.check_acc.balance == pytest.approx(160, 0.01)
        self.save_acc.deposit(60)
        assert self.save_acc.balance == pytest.approx(260, 0.01)

    def test_account_deposit_error(self):
        with pytest.raises(ValueError) as excinfo:
            self.check_acc.deposit(-10)
        exception_msg = excinfo.value.args[0]
        assert exception_msg == 'Must deposit positive amount'

    def test_account_close(self):
        '''Testing account.close method'''
        self.check_acc.close()
        assert self.check_acc.balance == pytest.approx(0, 0.01)
        self.save_acc.close()
        assert self.save_acc.balance == pytest.approx(0, 0.01)

    def test_checking_process_check(self):
        '''Testing check processing method'''
        assert self.check_acc.balance == pytest.approx(100, 0.01)
        self.check_acc.process_check(30)
        assert self.check_acc.balance == pytest.approx(70, 0.01)
        self.check_acc.process_check(80)
        assert self.check_acc.balance == pytest.approx(55, 0.01)

    def test_checking_str(self, capsys):
        '''Testing checking.__str__ method'''
        print(self.check_acc)
        out, err = capsys.readouterr()
        assert out.strip() == ('Checking account\n' +
                               'Owner: John Doe (1861-09-01)\n' +
                               '700 College Dr\n' +
                               'Decorah, IA 52101\n' +
                               'Balance: 100.00')

    def test_savings_yield_interest(self):
        '''Testing check processing method'''
        assert self.save_acc.balance == pytest.approx(200.00, 0.01)
        self.save_acc.yield_interest()
        assert self.save_acc.balance == pytest.approx(207.00, 0.01)

    def test_savings_str(self, capsys):
        '''Testing savings.__str__ method'''
        print(self.save_acc)
        out, err = capsys.readouterr()
        assert out.strip() == ('Savings account\n' +
                               'Owner: Jane Doe (1861-09-02)\n' +
                               '700 College Dr\n' +
                               'Decorah, IA 52101\n' +
                               'Balance: 200.00')

if __name__ == '__main__':
    pytest.main(['test_bank.py'])
