from controller.base.SimplyList import SimplyList


class Client:
    def __init__(self, dpi, name):
        self.dpi = dpi
        self.name = name
        self.transactions = SimplyList()

    def get_dpi(self):
        return self.dpi

    def get_name(self):
        return self.name

    def get_transactions(self):
        return self.transactions
