class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return str(self.data)


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add_end(self, data):
        new_node = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def add_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def del_head(self):
        print(self.head.data)
        self.head = self.head.next

    def del_end(self):
        if self.head is None:
            print("The list has no element to delete")
            return
        if self.head.next is None:
            self.head = None
            return
        n = self.head
        while n.next is not None:
            n = n.next
        n.prev.next = None

    def display(self):
        elems = []
        current = self.head
        elems.append(current.data)
        while current.next:
            current = current.next
            elems.append(current.data)
        print(elems)

