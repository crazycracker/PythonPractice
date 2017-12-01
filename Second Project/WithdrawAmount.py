from MinimumBalanceException import *
from InsufficientBalanceException import *
from BankAccount import *

class WithdrawAmount:

    @staticmethod
    def withdraw(account, amount, minimum_balance):
        try:
            if account['balance'] - amount < 0:
                raise InsufficientBalanceException
            if account['balance'] - amount < minimum_balance:
                raise MinimumBalanceException
            else:
                BankAccount.withdraw(amount)
        except InsufficientBalanceException:
            print("Insufficient Balance")
        except MinimumBalanceException:
            print("Sorry , your account has reached the limit")
