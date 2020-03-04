class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Queues:
    def __init__(self):
        self.head = None
        self.last = None

    def enqueue(self, data):
        if self.last is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last = self.last.next

    def dequeue(self):
        ret = self.head.data
        self.head = self.head.next
        return ret

    def display(self):
        elems = []
        current = self.head
        elems.append(current.data)
        while current.next:
            current = current.next
            elems.append(current.data)
        return elems

que_instance = Queues()
que_instance.enqueue(7)
que_instance.enqueue(6)
que_instance.enqueue(5)
que_instance.enqueue(4)
print(que_instance.display())
que_instance.dequeue()
que_instance.dequeue()
print(que_instance.display())
