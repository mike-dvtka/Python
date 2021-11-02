L = [3, 5, 4] ; L = L.sort()

# Średnik zamiast nowej linii. Posortowanej listy nie trzeba przypisywać.

x, y = 1, 2, 3

# Nie można tak przypisać, mamy 2 zmienne a 3 wartości.

X = 1, 2, 3 ; X[1] = 4

# Średnik zamiast nowej linii. Krotek nie można modyfikować bo mają z góry ustalony rozmiar.

X = [1, 2, 3] ; X[3] = 4

# Średnik zamiast nowej linii. Mamy listę 3 elementową, a odwołujemy się do elementu z pozycji czwartej.

X = "abc" ; X.append("d")

# String nie ma wbudowanej metody append().

L = list(map(pow, range(8)))

# Metoda pow przyjmuje minimum 2 argumenty.
