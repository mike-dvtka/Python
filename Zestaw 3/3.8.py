lista_1 = [1, 2, 1, 3, 4, 5, 7]
lista_2 = [3, 6, 5, 6, 6, 4, 6, 1, 1]

lista_a = []
lista_b = []

for i in lista_1:
    if i in lista_2 and i not in lista_a:
        lista_a.append(i)

for j in [lista_1, lista_2]:
    for i in j:
        if i not in lista_b:
            lista_b.append(i)

print(lista_a)
print(lista_b)
