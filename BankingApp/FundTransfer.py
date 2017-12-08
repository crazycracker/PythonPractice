class FundTransfer:
    depositHistory = list()
    withDrawHistory = list()
    completeHistory = list()

    def __init__(self):
        pass

    def withDrawTrack(self, message):
        FundTransfer.withDrawHistory.append(message)
        FundTransfer.completeHistory.append(message)

    def depositTrack(self, message):
        FundTransfer.depositHistory.append(message)
        FundTransfer.completeHistory.append(message)

    def getFullHistory(self):
        return FundTransfer.completeHistory

    def getWithDrawHistory(self):
        return FundTransfer.withDrawHistory

    def getDepositHistory(self):
        return FundTransfer.depositHistory
