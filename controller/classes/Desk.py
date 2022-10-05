from controller.classes.Client import Client


class Desk:
    def __init__(self, id_desk: str, correlative: str, employee: str):
        self.id_desk: str = id_desk
        self.correlative: str = correlative.strip()
        self.employee: str = employee.strip()

    client_in_attention: Client or None = None

    def set_as_active(self) -> None:
        self.is_active = True

    def set_as_inactive(self) -> None:
        self.is_active = False

    def attend_client(self, client: Client) -> None:
        self.client_in_attention = client

    def get_client_in_attention(self) -> Client or None:
        return self.client_in_attention
