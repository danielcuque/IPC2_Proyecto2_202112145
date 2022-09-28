from controller.base.SinglyLinkedList import SinglyLinkedList


class Queue:

    def __init__(self):
        self.items = SinglyLinkedList()
        self.size = 0

    def enqueue(self, data):
        self.items.append(data)
        self.size += 1

    def dequeue(self):
        data = self.items.pop()
        self.size -= 1
        return data

    def traverse(self):
        self.items.show_list()
