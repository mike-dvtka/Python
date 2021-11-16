def odwracanie_iter(L, left, right):
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1


def odwracanie_rek(L, left, right):
    if left < right:
        L[left], L[right] = L[right], L[left]
        odwracanie_rek(L, left + 1, right - 1)


L = [11, 10, 8, 5, 9, 6, 5, 4, 7, 3, 2, 1]
print("Lista: ", L)
odwracanie_iter(L, 0, 5)
print("Odwrocenie iteracyjne od 0 do 5: ", L)
odwracanie_rek(L, 7, 10)
print("Odwrocenie rekurencyjne od 7 do 10: ", L)
