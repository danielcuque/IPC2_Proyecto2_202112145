from controller.base.NodeForSinglyList import NodeForSinglyList
from controller.base.SinglyLinkedList import SinglyLinkedList


class Queue:

    def __init__(self) -> None:
        self.items = SinglyLinkedList()

    def enqueue(self, data) -> NodeForSinglyList:
        return self.items.insert_at_start(data)

    def dequeue(self) -> NodeForSinglyList or None:
        if self.items.size == 0:
            return None
        return self.items.remove_at_position(self.items.size - 1)

    def traverse(self) -> None:
        count = 0
        node = self.items.head
        while node is not None:
            print(f"{count}: {node.data}")
            node = node.next
            count += 1

    def get_size(self) -> int:
        return self.items.size
