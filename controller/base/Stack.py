from controller.base.NodeForSinglyList import NodeForSinglyList
from controller.base.SinglyLinkedList import SinglyLinkedList


class Stack:
    def __init__(self):
        self.stack: SinglyLinkedList = SinglyLinkedList()

    def push(self, data) -> NodeForSinglyList:
        node = NodeForSinglyList(data)
        if self.stack.is_empty():
            self.stack.insert_at_end(data)
        else:
            node.next = self.stack.head
            self.stack.head = node
            self.stack.size += 1
        return node

    def pop(self) -> NodeForSinglyList or None:
        if self.stack.is_empty():
            return
        node = self.stack.head
        self.stack.head = self.stack.head.next
        self.stack.size -= 1
        return node.data

    def is_empty(self) -> bool:
        return self.stack.is_empty()

    def clear(self) -> None:
        self.stack.clear()

    def show_stack(self) -> None:
        self.stack.show_list()
