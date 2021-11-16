def factorial(n):
    if n <= 1:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


x = int(input("Podaj liczbe: "))
print("Silnia z", x, "to", factorial(x))
