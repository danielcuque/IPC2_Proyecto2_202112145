from controller.base.SinglyLinkedList import SinglyLinkedList
from controller.classes.Desk import Desk


class Office:
    def __init__(self, id_office: int, name: str, address: str, desks: SinglyLinkedList):
        self.id_office: int = id_office
        self.name: str = name.strip()
        self.address: str = address.strip()
        self.desks: SinglyLinkedList = desks
