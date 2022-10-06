
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
        self.clients_pending: Queue = Queue()
        self.clients_attended: Queue = Queue()

    # Attention times
    max_time_attention_in_office: float = 0.0
    min_time_attention_in_office: float = 0.0
    average_time_attention_in_office: float = 0.0

    # Waiting times
    max_time_waiting_in_office: float = 0.0
    min_time_waiting_in_office: float = 0.0
    average_time_waiting_in_office: int = 0.0

    # Clients in queue/ out queue
    clients_in_queue: int = 0
    clients_out_queue: int = 0

    # Set desactive desk
    is_active_desk: bool = False

    def __str__(self):
        return f"ID: {self.id_office}, Nombre: {self.name}, Dirección: {self.address}"

    def __repr__(self):
        return f"ID: {self.id_office}, Nombre: {self.name}, Dirección: {self.address}"

    # Add new client

    def add_client(self, client: str) -> NodeForSinglyList:
        self.clients_in_queue += 1
        return self.clients_pending.enqueue(client)

    def remove_client(self) -> NodeForSinglyList or None:
        client_dequeue = self.clients_pending.dequeue()
        if client_dequeue is not None:
            self.clients_out_queue += 1
            self.clients_in_queue -= 1

            self.clients_attended.enqueue(client_dequeue.data)
        return client_dequeue

    # Add active/inactive desk
    def add_active_desk(self, desk: Desk) -> None:
        self.active_desks.push(desk)

    def active_desk_by_algorithm(self) -> Desk:
        desk_inactive: Desk = self.inactive_desks.pop().data
        desk_inactive.is_available_to_receive_clients = True
        self.active_desks.push(desk_inactive)
        return desk_inactive

    def inactive_desk_by_algorithm(self) -> Desk:
        desk_active: Desk = self.active_desks.pop().data
        desk_active.set_as_inactive()
        self.inactive_desks.push(desk_active)
        return desk_active

    def add_inactive_desk(self, desk: Desk) -> None:
        self.inactive_desks.push(desk)

    def calculate_times_variables(self) -> None:
        self.calculate_average_atention()
        self.calculate_min_max_atention()
        self.calculate_average_waiting()
        self.calculate_min_max_waiting()

    def calculate_average_atention(self) -> None:
        if self.clients_out_queue == 0:
            return

        node: NodeForSinglyList = self.active_desks.stack.head
        sum_of_times: int = 0
        count_clients: int = 0

        for i in range(self.active_desks.get_size()):
            desk: Desk = node.data
            sum_of_times += desk.accumulated_time
            count_clients += desk.attend_clients
            node = node.next
        print(f"Suma de tiempos: {sum_of_times}, Cantidad de clientes: {count_clients}")
        self.average_time_attention_in_office = round(
            (sum_of_times / count_clients), 2)

    def calculate_min_max_atention(self):
        if self.clients_out_queue == 0:
            return

        node: NodeForSinglyList = self.active_desks.stack.head
        max_time: int = 0
        min_time: int = 0

        for i in range(self.active_desks.get_size()):
            desk: Desk = node.data
            if self.max_time_attention_in_office == 0 and self.min_time_attention_in_office == 0:
                max_time = desk.max_time_attention
                min_time = desk.min_time_attention
                print(f"Max: {max_time}, Min: {min_time}")
            else:
                if desk.max_time_attention > max_time:
                    max_time = desk.max_time_attention
                if desk.min_time_attention < min_time:
                    min_time = desk.min_time_attention

            node = node.next

        self.max_time_attention_in_office = max_time
        self.min_time_attention_in_office = min_time

    def calculate_average_waiting(self):
        pass

    def calculate_min_max_waiting(self):
        pass

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
        self.clients_pending = clients

    def get_clients(self) -> Queue:
        return self.clients_pending

    def get_head_clients(self) -> NodeForSinglyList:
        return self.clients_pending.items.head

    def get_head_active_desks(self) -> NodeForSinglyList:
        return self.active_desks.stack.head

    def get_head_inactive_desks(self) -> NodeForSinglyList:
        return self.inactive_desks.stack.head

    def get_clients_in_queue(self) -> int:
        return self.clients_pending.get_size()
