import random


def calc_pi(n=100):
    count = 0
    for _ in range(n):
        x = random.random()
        y = random.random()
        if x ** 2 + y ** 2 < 1:
            count += 1
    return 4 * count / n


for i in range(10):
    print(calc_pi(100))

print("\n")
for i in range(10):
    print(calc_pi(1000))

print("\n")
for i in range(10):
    print(calc_pi(10000))

print("\n")
for i in range(10):
    print(calc_pi(100000))
