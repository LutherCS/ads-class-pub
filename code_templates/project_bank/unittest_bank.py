'''
Testing the module Banking
Roman Yasinovskyy, 2017
'''

#!/usr/bin/python3

import unittest
from unittest.mock import patch
from io import StringIO
from bank import Address, Customer, Account, CheckingAccount, SavingsAccount


class TestBankingMethods(unittest.TestCase):
    '''Testing module banking'''

    def setUp(self):
        '''Setting up'''
        self.addr1 = Address('700 College Dr', 'Decorah', 'IA', 52101)
        self.addr2 = Address('1 5th Ave', 'New York', 'NY', 12345)
        self.customer = Customer('John Doe', '2017-09-20', self.addr1)
        self.check_acc = CheckingAccount(self.customer, 15, 100)
        self.save_acc = SavingsAccount(self.customer, 8, 200)

    def test_address_str(self):
        '''Testing address.__str__ method'''
        with patch('sys.stdout', new=StringIO()) as output:
            print(self.addr1)
        self.assertEqual(output.getvalue().strip(), '700 College Dr\n' +
                                                    'Decorah, IA 52101')


    def test_address_eq(self):
        '''Testing address.__eq__ method'''
        self.assertNotEqual(self.addr1, self.addr2)

    def test_customer_str(self):
        '''Testing customer.__str__ method'''
        with patch('sys.stdout', new=StringIO()) as output:
            print(self.customer)
        self.assertEqual(output.getvalue().strip(), 'John Doe (2017-09-20)\n' +
                                                    '700 College Dr\n' +
                                                    'Decorah, IA 52101')

    def test_customer_address(self):
        '''Testing customer.addree property'''
        self.assertEqual(self.customer.address, self.addr1)

    def test_customer_move(self):
        '''Testing customer.move method'''
        self.customer.move(self.addr2)
        with patch('sys.stdout', new=StringIO()) as output:
            print(self.customer)
        self.assertEqual(output.getvalue().strip(), 'John Doe (2017-09-20)\n' +
                                                    '1 5th Ave\n' +
                                                    'New York, NY 12345')

    def test_checking_balance(self):
        '''Testing account balance property'''
        self.assertEqual(self.check_acc.balance, 100)
        self.assertEqual(self.save_acc.balance, 200)

    def test_checking_process_check(self):
        '''Testing check processing method'''
        self.assertEqual(self.check_acc.balance, 100)
        self.check_acc.process_check(30)
        self.assertEqual(self.check_acc.balance, 70)
        self.check_acc.process_check(80)
        self.assertEqual(self.check_acc.balance, 55)
        self.check_acc.deposit(60)
        self.assertEqual(self.check_acc.balance, 115)
        self.check_acc.close()
        self.assertEqual(self.check_acc.balance, 0)

    def test_checking_str(self):
        '''Testing checking.__str__ method'''
        with patch('sys.stdout', new=StringIO()) as output:
            print(self.check_acc)
        self.assertEqual(output.getvalue().strip(), 'Checking account\n' +
                                                    'Owner: John Doe (2017-09-20)\n' +
                                                    '700 College Dr\n' +
                                                    'Decorah, IA 52101\n' +
                                                    'Balance: 100')

    def test_savings_yield_interest(self):
        '''Testing check processing method'''
        self.assertEqual(self.save_acc.balance, 200)
        self.save_acc.yield_interest()
        self.assertEqual(self.save_acc.balance, 216)
        self.save_acc.deposit(34)
        self.assertEqual(self.save_acc.balance, 250)
        self.save_acc.close()
        self.assertEqual(self.save_acc.balance, 0)

    def test_savings_str(self):
        '''Testing savings.__str__ method'''
        with patch('sys.stdout', new=StringIO()) as output:
            print(self.save_acc)
        self.assertEqual(output.getvalue().strip(), 'Savings account\n' +
                                                    'Owner: John Doe (2017-09-20)\n' +
                                                    '700 College Dr\n' +
                                                    'Decorah, IA 52101\n' +
                                                    'Balance: 200')

if __name__ == '__main__':
    unittest.main(verbosity=2)
