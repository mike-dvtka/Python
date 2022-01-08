global_dict = {}


def dynamic_func(func_dict, i, j):
    if i == 0 and j == 0:
        return 0.5
    elif i == 0:
        return 1.0
    elif j == 0:
        return 0.0

    if (i, j) not in func_dict:
        func_dict[(i, j)] = 0.5 * (dynamic_func(func_dict, i - 1, j) + dynamic_func(func_dict, i, j - 1))

    return func_dict[(i, j)]


for i in range(0, 5):
    print("P("+str(i)+", 0) = "+str(dynamic_func(global_dict, i, 0)))

print("\n")
for j in range(0, 5):
    print("P(0, " + str(i) + ") = " + str(dynamic_func(global_dict, 0, j)))

print("\n")
for i in range(0, 5):
    for j in range(0, 5):
        print("P(" + str(i) + ", "+str(j)+") = " + str(dynamic_func(global_dict, i, j)))


