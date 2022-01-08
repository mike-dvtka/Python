import math


def heron(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Dlugosci bokow nie spelniaja warunku trojkata")
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


try:
    print("Pole trojkata o bokach 4, 5, 6 = "+str(heron(4, 5, 6)))
    print("Pole trojkata o bokach 4, 5, 10 = " + str(heron(4, 5, 10)))
except ValueError as error:
    print(error)
