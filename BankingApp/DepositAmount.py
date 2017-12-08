from BankingApp import InvalidAccountNumberException

class DepositAmount:

    @staticmethod
    def deposit(account, balance, fundTransfer):
        try:
            account.balance += int(balance)
            fundTransfer.depositHistory("Amount deposited %d" % int(balance))
        except InvalidAccountNumberException:
            print("Invalid Account Number")
