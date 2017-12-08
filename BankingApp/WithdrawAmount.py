from BankingApp import InsufficientBalanceException
from BankingApp import MinimumBalanceException


class WithdrawAmount:

    @staticmethod
    def withdraw(account, amount, minimum_balance, fundTransfer):
        try:
            if account.balance - int(amount) < 0:
                raise InsufficientBalanceException
            if account.balance - int(amount) < minimum_balance:
                raise MinimumBalanceException
            else:
                fundTransfer.withDrawHistory("Amount withdrawn %d" % int(amount))
                account.balance -= int(amount)
        except InsufficientBalanceException:
            fundTransfer.withDrawHistory("Insufficient Balance")
            print("Insufficient Balance")
        except MinimumBalanceException:
            fundTransfer.withDrawHistory("Sorry, account limit has reached")
            print("Sorry , your account has reached the limit")
