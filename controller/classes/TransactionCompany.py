class TransactionCompany:
    def __init__(self, id_transaction: str, name: str, time: str):
        self.id_transaction: str = id_transaction
        self.name = name.strip()
        self.time = time.strip()

    def get_name(self):
        return self.name

    def get_time(self):
        return self.time
