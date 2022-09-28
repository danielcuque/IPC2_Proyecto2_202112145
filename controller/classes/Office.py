from controller.base.SinglyLinkedList import SinglyLinkedList
from controller.classes.Desk import Desk

class Office:
    def __init__(self, id, name, direction):
        self.id: int =  id
        self.name: str = name
        self.direction: str =  direction
        self.desks: SinglyLinkedList = SinglyLinkedList()        