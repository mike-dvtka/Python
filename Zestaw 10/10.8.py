import random


class RandomQueue:

    def __init__(self, size=5):
        self.size = 0
        self.n = size
        self.items = size * [None]

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.n

    def put(self, data):
        if self.is_full():
            raise OverflowError("Blad: przepelnienie kolejki")
        else:
            self.items[self.size] = data
            self.size += 1

    def get(self):
        if self.is_empty():
            raise OverflowError("Blad: pusta kolejka")
        else:
            self.size -= 1
            elem = random.randint(0, self.size)
            data = self.items[elem]
            self.items[elem] = self.items[self.size]
            self.items[self.size] = None
            return data


losowa_kolejka = RandomQueue(10)

print("\n", losowa_kolejka.items, "\n")

for i in range(15):         # specjalnie wykonuje sie 5 razy wiecej zeby bylo 5 wyjatkow
    try:
        losowa_kolejka.put(random.randint(0, 500))
    except OverflowError as Error:
        print(Error)

print("\n")

for i in range(15):
    print(losowa_kolejka.items)
    try:
        print("Wyciagnieto: ", losowa_kolejka.get())
    except OverflowError as Error:
        print(Error)

print("\n", losowa_kolejka.items, "\n")
