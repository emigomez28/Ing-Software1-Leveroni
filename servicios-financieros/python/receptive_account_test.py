import unittest
from receptive_account import ReceptiveAccount
from deposit import Deposit
from withdraw import Withdraw

class ReceptiveAccountTest(unittest.TestCase):

    'tests'

    def test01_receptive_account_has_zero_as_balance_when_created(self):
        account = ReceptiveAccount()

        self.assertEqual(0, account.balance())

    def test02_deposit_increases_balance_on_transaction_value(self):
        account = ReceptiveAccount()

        Deposit.register_on(100, account)

        self.assertEqual(100, account.balance())

    def test03_withdraw_decreases_balance_on_transaction_value(self):
        account = ReceptiveAccount()

        Deposit.register_on(100, account)
        Withdraw.register_on(50, account)

        self.assertEqual(50, account.balance())

    def test04_withdraw_value_must_be_positive(self):
        account = ReceptiveAccount()

        withdraw_value = 50

        self.assertEqual(withdraw_value, Withdraw.register_on(withdraw_value, account).value())

    def test05_receptive_accounts_knows_registered_transactions(self):
        account = ReceptiveAccount()

        deposit = Deposit.register_on(100, account)
        withdraw = Withdraw.register_on(50, account)

        self.assertTrue(account.has_registered(deposit))
        self.assertTrue(account.has_registered(withdraw))

    def test06_receptive_account_do_not_know_not_registered_transactions(self):
        account = ReceptiveAccount()

        deposit = Deposit.for_value(100)
        withdraw = Withdraw.for_value(50)

        self.assertFalse(account.has_registered(deposit))
        self.assertFalse(account.has_registered(withdraw))

    def test07_account_knows_its_transactions(self):
        account = ReceptiveAccount()

        deposit = Deposit.register_on(100, account)

        self.assertEqual(1, len(account.transactions()))
        self.assertIn(deposit, account.transactions())

if __name__ == "__main__":
    unittest.main()