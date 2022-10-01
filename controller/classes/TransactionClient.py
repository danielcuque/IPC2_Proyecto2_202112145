class TransactionClient:
    def __init__(self, id_transaction: str, quantity):
        self.id_transaction: str = id_transaction
        self.quantity: int = quantity

    def get_id_transaction(self):
        return self.id_transaction

    def get_quantity(self):
        return self.quantity
