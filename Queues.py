

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Queues:
    def __init__(self):
        self.head = None
        self.last = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

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


