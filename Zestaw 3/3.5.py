x = int(input("Podaj dlugosc miarki: "))

for i in range(x):
    print("|....", end="")
print("|")
for i in range(x+1):
    if i < 9:
        print(i, end="    ")
    elif i < 99:
        print(i, end="   ")
    elif i < 999:
        print(i, end="  ")
