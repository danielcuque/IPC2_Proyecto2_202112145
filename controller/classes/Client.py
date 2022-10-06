from controller.base.NodeForSinglyList import NodeForSinglyList
from controller.base.SinglyLinkedList import SinglyLinkedList
from controller.classes.TransactionClient import TransactionClient
from controller.classes.TransactionCompany import TransactionCompany


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

    def get_first_transaction_name(self) -> str:
        transaction_company: TransactionCompany = self.transactions.head.data.transaction_company
        return transaction_company.get_name()

    def get_first_transaction(self) -> TransactionClient:
        return self.transactions.head.data

    def get_sum_time_transaction_for_client(self) -> float:
        node: NodeForSinglyList = self.transactions.head
        sum_time: float = 0
        while node is not None:
            transaction_client: TransactionClient = node.data
            sum_time += transaction_client.get_simulation_time()
            node = node.next
        return sum_time
