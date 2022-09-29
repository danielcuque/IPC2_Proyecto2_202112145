from controller.base.SinglyLinkedList import SinglyLinkedList


class Company:
    def __init__(self, id_company: int, name: str, acronym: str, offices: SinglyLinkedList,
                 transactions: SinglyLinkedList):
        self.id_company: int = id_company
        self.name: str = name.strip()
        self.acronym: str = acronym.strip()
        self.offices: SinglyLinkedList = offices
        self.transactions: SinglyLinkedList = transactions
    
