from controller.classes.Client import Client
from controller.classes.TransactionClient import TransactionClient

from rich.console import Console


class Desk:
    def __init__(self, id_desk: str, correlative: str, employee: str):
        self.id_desk: str = id_desk
        self.correlative: str = correlative.strip()
        self.employee: str = employee.strip()

    # Set a new client to attend
    client_in_attention: Client or None = None

    # Time variables
    attend_clients: int = 0
    accumulated_time: int = 0

    average_time_attention: int = 0
    min_time_attention: int = 0
    max_time_attention: int = 0

    is_available_to_receive_clients: bool = True

    # Is the desk free to attend a new client?
    def is_free(self) -> bool:
        return self.client_in_attention is None

    def attend_client(self, client: Client or None) -> None:
        if client is not None:
            # Add new client attend
            self.attend_clients += 1

            # set variables
            self.set_time_variables(client)
            self.calculate_average_time_attention()
        self.client_in_attention = client

    def set_time_variables(self, client: Client):
        # Set the accumulated time with the value of the first transaction
        total_time_attention_client: float = self.get_sum_time_transaction_for_client(client)
        if self.min_time_attention == 0 and self.max_time_attention == 0:
            self.min_time_attention: int = total_time_attention_client
            self.max_time_attention: int = total_time_attention_client
            self.average_time_attention: int = total_time_attention_client
        else:
            self.set_max_min_time(total_time_attention_client)

    def get_client_in_attention(self) -> Client or None:
        return self.client_in_attention

    def calculate_average_time_attention(self) -> None:
        if self.attend_clients > 0:
            Console().print(
                f"self.accumulated_time:{self.accumulated_time} ", justify="center")
            Console().print(
                f"self.attend_clients: {self.attend_clients}", justify="center")
            self.average_time_attention = self.accumulated_time / self.attend_clients

    def get_sum_time_transaction_for_client(self, client: Client) -> float:
        node = client.get_transactions().head
        sum_time: float = 0
        for i in range(client.get_transactions().get_size()):
            transaction: TransactionClient = node.data
            sum_time += transaction.get_simulation_time()
            node = node.next
        self.accumulated_time += sum_time
        return sum_time

    def set_max_min_time(self, transaction_time: float) -> None:
        if transaction_time < self.min_time_attention:
            self.min_time_attention = transaction_time
        elif transaction_time > self.max_time_attention:
            self.max_time_attention = transaction_time
