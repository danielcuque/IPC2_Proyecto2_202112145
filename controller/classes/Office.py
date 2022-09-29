
from controller.base.Queue import Queue
from controller.base.Stack import Stack


class Office:
    def __init__(self, id_office: int, name: str, address: str):
        self.id_office: int = id_office
        self.name: str = name.strip()
        self.address: str = address.strip()
        self.active_desks: Stack = Stack()
        self.inactive_desk: Stack = Stack()
        self.clients: Queue = Queue()

    def __str__(self):
        return f"ID: {self.id_office}, Nombre: {self.name}, Dirección: {self.address}"

    def __repr__(self):
        return f"ID: {self.id_office}, Nombre: {self.name}, Dirección: {self.address}"

    def get_active_desks(self) -> Stack:
        return self.active_desks

    def get_inactive_desks(self) -> Stack:
        return self.inactive_desk

    def set_active_desks(self, active_desks: Stack) -> None:
        self.active_desks = active_desks

    def set_inactive_desks(self, inactive_desk: Stack) -> None:
        self.inactive_desk = inactive_desk

    def set_clients(self, clients: Queue) -> None:
        self.clients = clients
