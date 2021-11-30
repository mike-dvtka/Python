import math
import unittest


def denominator(a, b):
    return int(abs(a * b / math.gcd(a, b)))


class Frac:
    """Klasa reprezentująca ułamki."""

    def __init__(self, x=0, y=1):
        self.x = x
        self.y = y
        if self.y == 0:
            raise ValueError("Mianownik nie moze byc 0")

    def simple_frac(self):
        if isinstance(self, int):
            return self
        denom = math.gcd(int(self.x), int(self.y))
        return Frac(int(self.x / denom), int(self.y / denom))

    def __str__(self):
        if self.simple_frac().y == 1:
            return str(self.simple_frac().x)
        else:
            string = str(self.x) + "/" + str(self.y)
            return string

    def __repr__(self):
        string = "Frac(" + str(self.simple_frac().x) + ", " + str(self.simple_frac().y) + ")"
        return string

    def __eq__(self, other):
        return (self.simple_frac().x == other.simple_frac().x) and (self.simple_frac().y == other.simple_frac().y)

    def __ne__(self, other):
        return not self.simple_frac() == other.simple_frac()

    def __lt__(self, other):
        denom = denominator(self.y, other.y)
        frac1 = self.x * (denom / self.y)
        frac2 = other.x * (denom / other.y)
        return frac1 < frac2

    def __le__(self, other):
        denom = denominator(self.y, other.y)
        frac1 = self.x * (denom / self.y)
        frac2 = other.x * (denom / other.y)
        return frac1 <= frac2

    def __gt__(self, other):
        denom = denominator(self.y, other.y)
        frac1 = self.x * (denom / self.y)
        frac2 = other.x * (denom / other.y)
        return frac1 > frac2

    def __ge__(self, other):
        denom = denominator(self.y, other.y)
        frac1 = self.x * (denom / self.y)
        frac2 = other.x * (denom / other.y)
        return frac1 >= frac2

    def __add__(self, other):  # frac1+frac2, frac+int
        if isinstance(other, int):
            return Frac(self.y * other + self.x, self.y).simple_frac()
        else:
            denom = denominator(self.y, other.y)
            frac1 = self.x * (denom / self.y)
            frac2 = other.x * (denom / other.y)
            return Frac(int(frac1 + frac2), int(denom)).simple_frac()

    __radd__ = __add__  # int+frac

    def __sub__(self, other):  # frac1-frac2, frac-int
        if isinstance(other, int):
            return Frac(-self.y * other + self.x, self.y).simple_frac()
        else:
            denom = denominator(self.y, other.y)
            frac1 = self.x * (denom / self.y)
            frac2 = other.x * (denom / other.y)
            return Frac(frac1 - frac2, denom).simple_frac()

    def __rsub__(self, other):  # int-frac
        return Frac(self.y * other - self.x, self.y)

    def __mul__(self, other):  # frac1*frac2, frac*int
        if isinstance(other, int):
            return Frac(self.x * other, self.y).simple_frac()
        else:
            return Frac(self.x * other.x, self.y * other.y).simple_frac()

    __rmul__ = __mul__  # int*frac

    def __div__(self, other):  # frac1/frac2, frac/int, Py2
        if isinstance(other, int):
            if other == 0:
                raise ValueError("Nie mozna dzielic przez 0")
            return Frac(self.x, self.y * other).simple_frac()
        else:
            return Frac(self.x * other.y, self.y * other.x).simple_frac()

    def __rdiv__(self, other):  # int/frac, Python 2
        return Frac(other * self.y, self.x).simple_frac()

    def __truediv__(self, other):  # frac1/frac2, frac/int, Py3
        if isinstance(other, int):
            if other == 0:
                raise ValueError("Nie mozna dzielic przez 0")
            return Frac(self.x, self.y * other).simple_frac()
        else:
            return Frac(self.x * other.y, self.y * other.x).simple_frac()

    def __rtruediv__(self, other):  # int/frac, Py3
        return Frac(other * self.y, self.x).simple_frac()

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):  # -frac = (-1)*frac
        if isinstance(self, int):
            return -self
        else:
            return Frac(-self.x, self.y)

    def __invert__(self):  # odwrotnosc: ~frac
        if isinstance(self, int):
            if self != 0:
                return Frac(1, self)
            else:
                return self
        else:
            return Frac(self.y, self.x)

    def __float__(self):  # float(frac)
        return self.x / self.y

    def __hash__(self):
        return hash(float(self))  # immutable fracs
        # assert set([2]) == set([2.0])


class TestFrac(unittest.TestCase):
    def test_str(self):
        self.assertEqual(str(Frac(2, 3)), "2/3")
        self.assertEqual(str(Frac(2, 1)), "2")
        self.assertEqual(str(Frac(-65, 111)), "-65/111")

    def test_repr(self):
        self.assertEqual(repr(Frac(2, 3)), "Frac(2, 3)")
        self.assertEqual(repr(Frac(2, 1)), "Frac(2, 1)")
        self.assertEqual(repr(Frac(-65, 111)), "Frac(-65, 111)")

    def test_eq(self):
        self.assertTrue(Frac(2, 3) == Frac(2, 3))
        self.assertFalse(Frac(1, 2) == Frac(2, 3))
        self.assertTrue(Frac(-1, 5) == Frac(-1, 5))

    def test_ne(self):
        self.assertFalse(Frac(2, 3) != Frac(2, 3))
        self.assertTrue(Frac(1, 2) != Frac(2, 3))
        self.assertFalse(Frac(-1, 5) != Frac(-1, 5))

    def test_lt(self):
        self.assertTrue(Frac(1, 2) < Frac(2, 3))
        self.assertTrue(Frac(-1, 2) < Frac(-1, 3))
        self.assertFalse(Frac(-1, 5) < Frac(-1, 5))

    def test_le(self):
        self.assertTrue(Frac(1, 2) <= Frac(2, 3))
        self.assertTrue(Frac(-1, 2) <= Frac(-1, 3))
        self.assertTrue(Frac(-1, 5) <= Frac(-1, 5))

    def test_gt(self):
        self.assertFalse(Frac(1, 2) > Frac(2, 3))
        self.assertFalse(Frac(-1, 2) > Frac(-1, 3))
        self.assertFalse(Frac(-1, 5) > Frac(-1, 5))

    def test_ge(self):
        self.assertFalse(Frac(1, 2) >= Frac(2, 3))
        self.assertTrue(Frac(-1, 2) >= Frac(-2, 3))
        self.assertFalse(Frac(-1, 5) >= Frac(1, 3))

    def test_add(self):
        self.assertEqual(str(Frac(2, 7) + Frac(1, 9)), str(Frac(25, 63)))
        self.assertEqual(str(Frac(-2, 7) + Frac(1, 9)), str(Frac(-11, 63)))
        self.assertEqual(str(1 + Frac(3,16)), str(Frac(19, 16)))
        self.assertEqual(str(Frac(4, 13) + 9), str(Frac(121, 13)))

    def test_sub(self):
        self.assertEqual(str(Frac(2, 7) - Frac(1, 9)), str(Frac(11, 63)))
        self.assertEqual(str(Frac(-2, 7) - Frac(1, 9)), str(Frac(-25, 63)))
        self.assertEqual(str(1 - Frac(3, 16)), str(Frac(13, 16)))
        self.assertEqual(str(Frac(4, 13) - 9), str(Frac(-113, 13)))

    def test_mul(self):
        self.assertEqual(str(Frac(2, 7) * Frac(1, 9)), str(Frac(2, 63)))
        self.assertEqual(str(Frac(-2, 7) * Frac(1, 9)), str(Frac(-2, 63)))
        self.assertEqual(str(1 * Frac(3, 16)), str(Frac(3, 16)))
        self.assertEqual(str(Frac(4, 13) * 9), str(Frac(36, 13)))

    def test_div(self):
        self.assertEqual(str(Frac(2, 7) / Frac(1, 9)), str(Frac(18, 7)))
        self.assertEqual(str(Frac(-2, 7) / Frac(1, 9)), str(Frac(-18, 7)))
        self.assertEqual(str(1 / Frac(3, 16)), str(Frac(16, 3)))
        self.assertEqual(str(Frac(4, 13) / 9), str(Frac(4, 117)))


if __name__ == '__main__':
    unittest.main()
