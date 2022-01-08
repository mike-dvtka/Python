class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class SingleList:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def count(self):
        return self.length

    def insert_head(self, node):
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):
        if self.head:
            self.tail.next = node
            self.tail = node
        else:
            self.head = self.tail = node
        self.length += 1

    def remove_head(self):
        if self.is_empty():
            raise ValueError("Single list is empty")

        node = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None
        self.length -= 1
        return node

    def remove_tail(self):
        if self.is_empty():
            raise ValueError("Single list is empty")

        node = self.tail
        if self.head is self.tail:
            self.head = self.tail = None
        else:
            it = self.head
            while it.next is not self.tail:
                it = it.next
            it.next = None
            self.tail = it
        self.length -= 1
        return node

    def join(self, other):
        if self is other or other.is_empty():
            return

        if not self.is_empty():
            self.tail.next = other.head
        else:
            self.head = other.head

        self.tail = other.tail
        self.length += other.length
        other.head = other.tail = None
        other.length = 0

    def clear(self):
        self.head = self.tail = None
        self.length = 0


listA = SingleList()
listB = SingleList()

listA.insert_head(Node(15))
listA.insert_tail(Node(2))
listA.insert_head(Node(1))
listA.insert_tail(Node(3))
listA.insert_head(Node(5))
listB.insert_tail(Node(3))
listB.insert_tail(Node(5))
listB.insert_head(Node(9))
listA.join(listB)
listA.remove_tail()
listA.clear()
