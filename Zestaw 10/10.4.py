import random


class Queue:

    def __init__(self, size=5):
        self.n = size + 1
        self.items = size * [None]
        self.head = 0
        self.tail = 0

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.head + self.n - 1) % self.n == self.tail

    def put(self, data):
        if self.is_full():
            raise OverflowError("Blad: przepelnienie kolejki")
        else:
            self.items[self.tail] = data
            self.tail = (self.tail + 1) % self.n

    def get(self):
        if self.is_empty():
            raise OverflowError("Blad: pusta kolejka")
        else:
            data = self.items[self.head]
            self.items[self.head] = None
            self.head = (self.head + 1) % self.n
            return data


kolejka = Queue(10)

print("\n", kolejka.items, "\n")

for i in range(15):         # specjalnie wykonuje sie 5 razy wiecej zeby bylo 5 wyjatkow
    try:
        kolejka.put(random.randint(0, 500))
    except OverflowError as Error:
        print(Error)

print("\n", kolejka.items, "\n")

for i in range(15):
    try:
        print("Wyciagnieto: ", kolejka.get())
    except OverflowError as Error:
        print(Error)

print("\n", kolejka.items, "\n")
