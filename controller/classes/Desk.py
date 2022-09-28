class Desk:
    def __init__(self, id_desk, correlative: str, employee: str):
        self.id_desk: int = id_desk
        self.correlative: str = correlative.strip()
        self.employee: str = employee.strip()
