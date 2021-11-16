def make_ruler(n):
    line_1 = ""
    line_2 = ""
    for i in range(n):
        line_1 = line_1 + "|...."
    line_1 = line_1 + "|"
    for i in range(n + 1):
        if i < 9:
            line_2 = line_2 + str(i) + "    "
        elif i < 99:
            line_2 = line_2 + str(i) + "   "
        elif i < 999:
            line_2 = line_2 + str(i) + "  "
    text = "\n".join([line_1, line_2])
    return text


def make_grid(rows, cols):
    grid = ""
    for k in range(cols):
        grid = grid + "+"
        for i in range(rows):
            grid = grid + "---+"
        grid = grid + "\n"

        grid = grid + "|"
        for j in range(rows):
            grid = grid + "   |"
        grid = grid + "\n"

    grid = grid + "+"
    for m in range(rows):
        grid = grid + "---+"
    grid = grid + "\n"
    return grid


length = int(input("Podaj dlugosc miarki: "))
print(make_ruler(length))

x = int(input("Podaj szerokosc prostokata (x): "))
y = int(input("Podaj wysokosc prostokata (y): "))
print(make_grid(x, y))
