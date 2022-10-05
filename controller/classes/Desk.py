from controller.classes.Client import Client


class Desk:
    def __init__(self, id_desk: str, correlative: str, employee: str):
        self.id_desk: str = id_desk
        self.correlative: str = correlative.strip()
        self.employee: str = employee.strip()

    client_in_attention: Client or None = None

    attend_clients: int = 0
    accumulated_time: int = 0
    transactions_made: int = 0

    average_time_attention: int = 0

    def set_as_active(self) -> None:
        self.is_active = True

    def set_as_inactive(self) -> None:
        self.is_active = False

    def attend_client(self, client: Client or None) -> None:
        if client is not None:
            self.attend_clients += 1
        self.client_in_attention = client

    def get_client_in_attention(self) -> Client or None:
        return self.client_in_attention

    def calculate_average_time_attention(self) -> None:
        if self.attend_clients > 0:
            self.average_time_attention = self.accumulated_time / self.attend_clients