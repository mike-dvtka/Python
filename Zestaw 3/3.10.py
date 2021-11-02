rom_int_dict1 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}    # klasyczna inicjalizacja

keys_list = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
values_list = [1, 5, 10, 50, 100, 500, 1000]
rom_int_dict2 = dict(zip(keys_list, values_list))    # z dwoch list

keys_tuple = ('I', 'V', 'X', 'L', 'C', 'D', 'M')
values_tuple = (1, 5, 10, 50, 100, 500, 1000)
rom_int_dict3 = dict(zip(keys_tuple, values_tuple))    # z dwoch krotek

keys_values_tuple = (('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100), ('D', 500), ('M', 1000))
rom_int_dict4 = dict(keys_values_tuple)    # z jednej krotki

rom_int_dict5 = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)    # za pomoca wbudowanej metody

def roman2int(num):
    int_val = 0
    for i in range(len(num)):
        if i > 0 and rom_int_dict1[num[i]] > rom_int_dict1[num[i - 1]]:
            int_val += rom_int_dict1[num[i]] - 2 * rom_int_dict1[num[i - 1]]
        else:
            int_val += rom_int_dict1[num[i]]
    return int_val

number=input("Podaj liczbe w formacie rzymskim:")
try:
    print(roman2int(number.upper()))
except:
    print("Nieprawidlowa liczba")

