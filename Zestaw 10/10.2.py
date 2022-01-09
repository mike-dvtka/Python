import random


class Stack:

    def __init__(self, size=10):
        self.items = size * [None]
        self.n = 0
        self.size = size

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        if self.is_full():
            raise OverflowError("Blad: przepelniony stos")
        else:
            self.items[self.n] = data
            self.n += 1

    def pop(self):
        if self.is_empty():
            raise OverflowError("Blad: pusty stos")
        else:
            self.n -= 1
            data = self.items[self.n]
            self.items[self.n] = None
            return data


stos = Stack(10)

for i in range(15):
    try:
        n = random.randint(0, 500)
        stos.push(n)
        print("Dodano: ", n)
    except OverflowError as Error:
        print(Error)

for i in range(15):
    try:
        print("Usunieto: ", stos.pop())
    except OverflowError as Error:
        print(Error)

