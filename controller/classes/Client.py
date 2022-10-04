from controller.base.SinglyLinkedList import SinglyLinkedList
from controller.classes.TransactionClient import TransactionClient


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

    def add_transaction_for_client(self, transaction: TransactionClient):
        self.transactions.insert_at_end(transaction)
