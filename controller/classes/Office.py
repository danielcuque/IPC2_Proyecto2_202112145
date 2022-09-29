from controller.base.Queue import Queue
from controller.base.SinglyLinkedList import SinglyLinkedList
from controller.base.Stack import Stack


class Office:
    def __init__(self, id_office: int, name: str, address: str):
        self.id_office: int = id_office
        self.name: str = name.strip()
        self.address: str = address.strip()
        self.active_desks: Stack = Stack()
        self.inactive_desk: Stack = Stack()
        self.clients: Queue = Queue()

