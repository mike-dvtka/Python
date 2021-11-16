def flatten(sequence):
    result = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


sekwencja = [[], 1, (2, 8), [[[(1, 1)]]], [1, (2, 3, 4)], 8, [9], [1, [1, 1, [1, 2]], (2, 3, 4)]]
print("Before:", sekwencja)
print("After:", flatten(sekwencja))
