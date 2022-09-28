from controller.base.SinglyLinkedList import SinglyLinkedList


class Client:
    def __init__(self, dpi, name):
        self.dpi = dpi
        self.name = name
        self.transactions = SinglyLinkedList()

    def get_dpi(self):
        return self.dpi

    def get_name(self):
        return self.name

    def get_transactions(self):
        return self.transactions
