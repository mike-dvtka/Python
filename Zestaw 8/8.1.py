"""
Problem: Obliczenie rozwiązania równania liniowego a x + b y + c = 0

Dane:
a – współczynnik przy X
b – współczynnik przy Y
c - wyraz wolny

Wynik:
x - obliczona wartość X
y - obliczona wartość Y
"""
def solve1(a, b, c):
    """Rozwiązywanie równania liniowego a x + b y + c = 0."""
    print(f"Rownanie {a}x{b:+}y{c:+} ma:")
    if a == 0 and b == 0:
        if c == 0:
            print("Nieskonczenie wiele rozwiazan")
        else:
            print("Brak rozwiazan")
    elif a == 0:
        print(f"{{x: x, y: {-c / b}}}")
    elif b == 0:
        print(f"{{x: {-c / a}, y: y}}")
    else:
        print(f"{{x: x, y: {-a / b}*x{-c / b:+}}}")


solve1(0, 3, 7)
solve1(0, 0, 8)
solve1(0, 0, 0)
solve1(5, 0, 6)
solve1(7, 0, 6)
solve1(7, 6, 6)
solve1(3, 1, 4)
solve1(-3, 1, -4)
