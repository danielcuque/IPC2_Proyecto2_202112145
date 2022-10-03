from controller.base.SinglyLinkedList import SinglyLinkedList
from controller.classes.Office import Office
from controller.classes.TransactionCompany import TransactionCompany


class Company:
    def __init__(self, id_company: str, name: str, acronym: str) -> None:
        self.id_company: str = id_company
        self.name: str = name.strip()
        self.acronym: str = acronym.strip()
        self.offices: SinglyLinkedList = SinglyLinkedList()
        self.transactions: SinglyLinkedList = SinglyLinkedList()

    def add_office(self, office: Office) -> None:
        self.offices.insert_at_end(office)

    def add_transaction(self, transaction: TransactionCompany) -> None:
        self.transactions.insert_at_end(transaction)

    def search_office(self, id_office: str) -> Office:
        node = self.offices.head
        while node is not None:
            office: Office = node.data
            if office.id_office == id_office:
                return office
            node = node.next
