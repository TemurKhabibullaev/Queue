from LinkedList import SinglyLinkedList
instance = SinglyLinkedList()


class Queues:
    def __init__(self):
        self.head = None
        self.last = None

    def enqueue(self, data):
        instance.add_end(data)

    def dequeue(self):
        instance.del_head()

