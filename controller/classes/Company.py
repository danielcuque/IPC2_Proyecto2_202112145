from controller.base.SinglyLinkedList import SinglyLinkedList

class Company:
    def __init__(self, id_company, name, acronym):
        self.id_company: int = id_company
        self.name: str = name
        self.acronym: str = acronym
        self.offices: SinglyLinkedList = SinglyLinkedList()
        