from InvalidAccountNumberException import *


class DepositAmount:

    @staticmethod
    def deposit(account, balance):
        try:
            account.balance += int(balance)
        except InvalidAccountNumberException:
            print("Invalid Account Number")
