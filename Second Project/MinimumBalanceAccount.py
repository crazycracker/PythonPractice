from WithdrawAmount import *


class MinimumBalanceAccount(BankAccount):
    def __init__(self, minimum_balance):
        BankAccount.__init__(self)
        self.minimum_balance = minimum_balance

    @property
    def minimum_balance(self):
        return self._minimum_balance

    @minimum_balance.setter
    def minimum_balance(self, minimum_balance):
        self._minimum_balance = minimum_balance

    def withdraw(self, amount):
        WithdrawAmount.withdraw(self, amount, minimum_balance=self.minimum_balance)
