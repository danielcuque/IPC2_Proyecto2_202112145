from controller.base.NodeForSinglyList import NodeForSinglyList


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        node: NodeForSinglyList = NodeForSinglyList(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1
        return node

    def remove(self):
        if self.head is None:
            return
        node = self.head
        self.head = self.head.next
        self.size -= 1
        return node.data

    def is_empty(self):
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
