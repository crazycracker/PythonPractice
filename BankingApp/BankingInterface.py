from BankingApp import MinimumBalanceAccount
from BankingApp import Accounts
from BankingApp import WithdrawAmount
from BankingApp import DepositAmount
from BankingApp import FundTransfer


accounts = Accounts()
minimum_balance = 500
fundTransfer = FundTransfer()
global account


def accountCreation():
    global account
    account = MinimumBalanceAccount(minimum_balance)
    accounts.add_account(account)


def withDrawAmount():
    amount = input("Enter the amount to be withdrawn")
    WithdrawAmount.withdraw(account, amount, minimum_balance, fundTransfer)


def depositAmount():
    balance = input("Enter the amount to be deposited")
    DepositAmount.deposit(account, balance, fundTransfer)


def transactionHistory():
    fundTransfer.getFullHistory()

def exitProgram():
    exit()


options = {
    1: accountCreation,
    2: withDrawAmount,
    3: depositAmount,
    4: transactionHistory,
    5: exitProgram
}


class Interface:

    while True:
        print("1. Create an account")
        print("2. Withdraw Amount")
        print("3. Deposit Amount")
        print("4. View Transaction History")
        print("5. Exit")

        choice = int(input())
        options[choice]()
        print("account_balance -----")
        print(account.balance)
        print("minimum_balance -----")
        print(account.minimum_balance)
