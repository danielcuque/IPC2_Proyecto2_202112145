from controller.base.NodeForSinglyList import NodeForSinglyList


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_at_end(self, data):
        node: NodeForSinglyList = NodeForSinglyList(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1
        return node

    def insert_at_start(self, data):
        node: NodeForSinglyList = NodeForSinglyList(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1
        return node

    def insert_at_position(self, data, position):
        if position < 0 or position > self.size:
            return
        if position == 0:
            return self.insert_at_start(data)
        if position == self.size:
            return self.insert_at_end(data)
        node = NodeForSinglyList(data)
        prev = self.head
        for i in range(position - 1):
            prev = prev.next
        node.next = prev.next
        prev.next = node
        self.size += 1
        return node

    def get_at_position(self, position):
        if position < 0 or position >= self.size:
            return
        node = self.head
        for i in range(position):
            node = node.next
        return node.data

    def get_size(self):
        return self.size

    def remove_at_position(self, position):
        if position < 0 or position >= self.size:
            return
        if position == 0:
            return self.remove_at_start()
        prev = self.head
        for i in range(position - 1):
            prev = prev.next
        node: NodeForSinglyList = prev.next
        prev.next = node.next
        self.size -= 1
        return node.data

    def remove_at_end(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            self.tail = None
            self.size -= 1
            return
        prev = self.head
        while prev.next != self.tail:
            prev = prev.next
        prev.next = None
        self.tail = prev
        self.size -= 1

    def remove_at_start(self):
        if self.head is None:
            return
        node = self.head
        self.head = self.head.next
        self.size -= 1
        return node.data

    def is_empty(self) -> bool:
        return self.head is None

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def show_list(self):
        if self.head is None:
            return
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next
