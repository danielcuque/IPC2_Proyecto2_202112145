
class NodeForSinglyList:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

    def get_next(self):
        return self.next
    
    def set_next(self, next):
        self.next = next