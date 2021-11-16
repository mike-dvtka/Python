def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    a = 0
    b = 1
    for j in range(1, n):
        a, b = b, a + b
    return b


x = int(input("Podaj liczbe wyrazow: "))
print("Ciag Fibonacciego: ")
for i in range(x):
    print(fibonacci(i), end=" ")
