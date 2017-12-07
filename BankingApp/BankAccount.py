import random


class BankAccount:
    account_number = random.randint(1000000000000000, 9999999999999999)

    def __init__(self, balance):
        self.balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        self._balance = balance
