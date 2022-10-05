
from controller.base.NodeForSinglyList import NodeForSinglyList
from controller.base.Queue import Queue
from controller.base.Stack import Stack
from controller.classes.Desk import Desk


class Office:
    def __init__(self, id_office: str, name: str, address: str):
        self.id_office: str = id_office.strip()
        self.name: str = name.strip()
        self.address: str = address.strip()
        self.active_desks: Stack = Stack()
        self.inactive_desks: Stack = Stack()
        self.clients: Queue = Queue()

    def __str__(self):
        return f"ID: {self.id_office}, Nombre: {self.name}, Dirección: {self.address}"

    def __repr__(self):
        return f"ID: {self.id_office}, Nombre: {self.name}, Dirección: {self.address}"

    # Add new client

    def add_client(self, client: str) -> NodeForSinglyList:
        return self.clients.enqueue(client)

    def remove_client(self) -> NodeForSinglyList:
        return self.clients.dequeue()

    # Add active/inactive desk
    def add_active_desk(self, desk: Desk) -> None:
        self.active_desks.push(desk)

    def active_desk_by_algorithm(self) -> Desk:
        desk_inactive_node: NodeForSinglyList = self.inactive_desks.pop()
        self.active_desks.push(desk_inactive_node)
        return desk_inactive_node.data

    
    def inactive_desk_by_algorithm(self) -> Desk:
        desk_active_node: NodeForSinglyList = self.active_desks.pop().data
        self.inactive_desks.push(desk_active_node)
        return desk_active_node.data


    def add_inactive_desk(self, desk: Desk) -> None:
        self.inactive_desks.push(desk)

    def search_desk_by_id(self, id_desk: str, is_active: bool = False) -> Desk:
        list_of_desks: Stack = self.active_desks if is_active else self.inactive_desks

        if list_of_desks.is_empty():
            return None

        node: NodeForSinglyList = list_of_desks.stack.head
        while node is not None:
            desk: Desk = node.data
            if desk.id_desk == id_desk:
                return desk
            node = node.next

    def get_index_of_desk(self, desk: Desk, is_active: bool = False) -> int:
        count = 0
        list_of_desks: Stack = self.active_desks if is_active else self.inactive_desks
        node: NodeForSinglyList = list_of_desks.stack.head

        while node is not None:
            if node.data == desk:
                return count
            count += 1
            node = node.next


    # Getters and setters
    def get_active_desks(self) -> Stack:
        return self.active_desks

    def get_inactive_desks(self) -> Stack:
        return self.inactive_desks

    def set_active_desks(self, active_desks: Stack) -> None:
        self.active_desks = active_desks

    def set_inactive_desks(self, inactive_desk: Stack) -> None:
        self.inactive_desks = inactive_desk

    def set_clients(self, clients: Queue) -> None:
        self.clients = clients

    def get_clients(self) -> Queue:
        return self.clients

    def get_head_clients(self) -> NodeForSinglyList:
        return self.clients.items.head

    def get_head_active_desks(self) -> NodeForSinglyList:
        return self.active_desks.stack.head

    def get_head_inactive_desks(self) -> NodeForSinglyList:
        return self.inactive_desks.stack.head
