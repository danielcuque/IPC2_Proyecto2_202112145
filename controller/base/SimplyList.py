from NodeForSimplyList import NodeForSimplyList

class SimplyList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_at_end(self, data):
        node = NodeForSimplyList(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def remove(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return
        node = self.head
        while node.next is not None:
            if node.next.data == data:
                node.next = node.next.next
                self.size -= 1
                return
            node = node.next