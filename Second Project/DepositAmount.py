from InvalidAccountNumberException import *


class DepositAmount:

    @staticmethod
    def deposit(account, balance):
        try:
            account['balance'] += balance
        except InvalidAccountNumberException:
            print("Invalid Account Number")
