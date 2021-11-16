import math


def denominator(a, b):
    return int(abs(a * b / math.gcd(a, b)))  # math.gcd() zastepuje fractions.gcd()


def final_fraction(frac):
    el = math.gcd(int(frac[0]), int(frac[1]))
    frac[0] = frac[0] / el
    frac[1] = frac[1] / el
    return frac


def add_frac(frac1, frac2):
    frac = [0, 0]
    frac[1] = denominator(frac1[1], frac2[1])
    frac[0] = (frac1[0] * denominator(frac1[1], frac2[1]) / frac1[1]) + (frac2[0] * denominator(frac1[1], frac2[1]) / frac2[1])
    return final_fraction(frac)


def sub_frac(frac1, frac2):
    frac = [0, 0]
    frac[1] = denominator(frac1[1], frac2[1])
    frac[0] = (frac1[0] * denominator(frac1[1], frac2[1]) / frac1[1]) - (frac2[0] * denominator(frac1[1], frac2[1]) / frac2[1])
    return final_fraction(frac)


def mul_frac(frac1, frac2):
    frac = [0, 0]
    frac[0] = frac1[0] * frac2[0]
    frac[1] = frac1[1] * frac2[1]
    return final_fraction(frac)


def div_frac(frac1, frac2):
    if is_zero(frac2):
        raise ZeroDivisionError
    frac = [0, 0]
    frac[0] = frac1[0] * frac2[1]
    frac[1] = frac1[1] * frac2[0]
    return final_fraction(frac)


def is_positive(frac):
    if (frac[0] > 0 and frac[1] > 0) or (frac[0] < 0 and frac[1] < 0):
        return True
    return False


def is_zero(frac):
    if frac[0] == 0:
        return True
    return False


def cmp_frac(frac1, frac2):
    frac1[0] *= denominator(frac1[1], frac2[1]) / frac1[1]
    frac2[0] *= denominator(frac1[1], frac2[1]) / frac2[1]
    if frac1[0] == frac2[0]:
        return 0
    if frac2[0] > frac1[0]:
        return -1
    else:
        return 1


def frac2float(frac):
    return float(frac[0] / frac[1])
