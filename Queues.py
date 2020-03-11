from LinkedList import SinglyLinkedList


class Queues:
    def __init__(self):
        self.ins = SinglyLinkedList()

    def enqueue(self, data):
        self.ins.adding(data)

    def dequeue(self):
        return self.ins.del_head()

    def display(self):
        return self.ins.display()

