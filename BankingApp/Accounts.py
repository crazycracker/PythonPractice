from BankingApp import InvalidAccountNumberException


class Accounts:
    accounts = list()

    @staticmethod
    def add_account(account):
        Accounts.accounts.append(account)

    @staticmethod
    def get_account(account):
        try:
            for x in Accounts.accounts:
                if x.account_number == account.account_number:
                    return True
            raise InvalidAccountNumberException
        except InvalidAccountNumberException:
            print("Invalid Account Number")
