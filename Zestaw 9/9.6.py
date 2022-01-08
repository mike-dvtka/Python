class Node:
    def __init__(self, data=None, right=None, left=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


def count_leaves(top):
    if top is None:
        return 0
    if top.left is None and top.right is None:
        return 1
    else:
        return count_leaves(top.left) + count_leaves(top.right)


def count_total(top):
    if top is None:
        return 0
    if top.left is None and top.right is None:
        return top.data
    else:
        return top.data + count_total(top.left) + count_total(top.right)


lisc = Node(12)
lisc.left = Node(7)
lisc.right = Node(9)
lisc.left.left = Node(4)
lisc.left.right = Node(3)
lisc.left.right.left = Node(2)
lisc.left.right.right = Node(1)

print("Liczba lisci: %d" % (count_leaves(lisc)))
print("Wartosc drzewa: %d" % (count_total(lisc)))
