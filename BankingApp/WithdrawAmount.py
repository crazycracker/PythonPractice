from MinimumBalanceException import *
from InsufficientBalanceException import *
from MinimumBalanceAccount import *


class WithdrawAmount:

    @staticmethod
    def withdraw(account, amount, minimum_balance):
        try:
            if account.balance - int(amount) < 0:
                raise InsufficientBalanceException
            if account.balance - int(amount) < minimum_balance:
                raise MinimumBalanceException
            else:
                account.balance -= int(amount)
        except InsufficientBalanceException:
            print("Insufficient Balance")
        except MinimumBalanceException:
            print("Sorry , your account has reached the limit")
