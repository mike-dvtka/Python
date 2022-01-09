import random

n = 100
k = 10


def linearSearch(listArg, x):
    result = []
    for i in range(0, len(listArg)):
        if listArg[i] == x:
            result.append(i)
    return result


list = n * [None]
for i in range(n):
    list[i] = random.randint(0, k - 1)

print(list)
y = random.randint(0, k - 1)
print("Wylosowane y = "+str(y)+" jest na indeksach: ")
index = linearSearch(list, y)
print(index)
