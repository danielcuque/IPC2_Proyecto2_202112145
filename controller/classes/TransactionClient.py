from controller.classes.TransactionCompany import TransactionCompany


class TransactionClient:
    def __init__(self, transaction_company: TransactionCompany, quantity: str):
        self.transaction_company: TransactionCompany = transaction_company
        self.quantity: str = quantity
        self.simuation_time: float = (
            float(transaction_company.time)*float(quantity))

    def get_transaction_company(self):
        return self.transaction_company

    def get_quantity(self) -> str:
        return self.quantity

    def get_simulation_time(self) -> float:
        return self.simuation_time

    def set_quantity(self, quantity: str):
        self.quantity = quantity

    def set_simulation_time(self, simulation_time: float):
        self.simuation_time = simulation_time

    # Time in seconds

    def go_to_next_step_in_time(self):
        self.simuation_time -= 1
