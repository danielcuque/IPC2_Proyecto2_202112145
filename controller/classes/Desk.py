class Desk:
    def __init__(self, id_desk: str, correlative: str, employee: str):
        self.id_desk: str = id_desk
        self.correlative: str = correlative.strip()
        self.employee: str = employee.strip()
