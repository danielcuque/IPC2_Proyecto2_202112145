

from controller.base.NodeForSinglyList import NodeForSinglyList
from controller.base.SinglyLinkedList import SinglyLinkedList


class Stack:
    def __init__(self):
        self.stack = SinglyLinkedList()

    def push(self, data):
        node = NodeForSinglyList(data)
        if self.stack.is_empty():
            self.stack.append(data)
        else:
            node.next = self.stack.head
            self.stack.head = node
            self.stack.size += 1
        return node

    def pop(self):
        if self.stack.is_empty():
            return
        node = self.stack.head
        self.stack.head = self.stack.head.next
        self.stack.size -= 1
        return node.data

    def is_empty(self):
        return self.stack.is_empty()

    def clear(self):
        self.stack.clear()

    def show_stack(self):
        self.stack.show_list()
