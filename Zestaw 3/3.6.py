x = int(input("Podaj szerokosc prostokata (x): "))
y = int(input("Podaj wysokosc prostokata (y): "))

full_string = (("---+" * x) + "\n") * (2 * y + 1)
full_string = full_string.split("\n")
i = 0
prostokat = ''

for line in full_string:
    if i != 0:
        if i % 2 == 0:
            prostokat += "|" + ("   |" * x) + "\n"

        else:
            prostokat += "+" + ("---+" * x) + "\n"
    i += 1
print(prostokat)
