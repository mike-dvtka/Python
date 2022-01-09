def binarne_rek(L, left, right, y):
    """Wyszukiwanie binarne w wersji rekurencyjnej."""

    if left > right:
        return None

    k = (left + right) // 2  # dwa slashe zeby zaokraglalo w dol (od razu mamy int'a)

    if y == L[k]:
        return k
    elif y > L[k]:
        return binarne_rek(L, k + 1, right, y)
    elif y < L[k]:
        return binarne_rek(L, left, k - 1, y)


List = [1, 6, 9, 10, 12, 15, 19, 30, 31, 31, 32, 43, 46, 48, 60, 71, 72, 78, 90, 91, 92, 93, 96, 96, 96, 101]

print("y = 1, index = " + str(binarne_rek(List, 0, len(List), 1)))
print("y = 2, index = " + str(binarne_rek(List, 0, len(List), 2)))
print("y = 10, index = " + str(binarne_rek(List, 0, len(List), 10)))
print("y = 31, index = " + str(binarne_rek(List, 0, len(List), 31)))
print("y = 31, index = " + str(binarne_rek(List, 0, len(List), 31)))
print("y = 101, index = " + str(binarne_rek(List, 0, len(List), 101)))
print("y = 72, index = " + str(binarne_rek(List, 0, len(List), 72)))
print("y = 96, index = " + str(binarne_rek(List, 0, len(List), 96)))

