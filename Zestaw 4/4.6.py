def sum_seq(sequence):
    result = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            result += sum_seq(item)
        else:
            result += item
    return result


sekwencja = [[], 1, (2, 8), [[[(1, 1)]]], [1, (2, 3, 4)], 8, [9], [1, [1, 1, [1, 2]], (2, 3, 4)]]
print("Lista: ", sekwencja)
print("Suma: ", sum_seq(sekwencja))
