import unittest


class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        string = "(" + str(self.x) + ", " + str(self.y) + ")"
        return string

    def __repr__(self):
        string = "Point(" + str(self.x) + ", " + str(self.y) + ")"
        return string

    def __eq__(self, other):
        if (self.x == other.x) & (self.y == other.y):
            return True
        else:
            return False

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        tmp_point = Point(0.0, 0.0)
        tmp_point.x, tmp_point.y = self.x + other.x, self.y + other.y
        return tmp_point

    def __sub__(self, other):
        tmp_point = Point(0.0, 0.0)
        tmp_point.x, tmp_point.y = self.x - other.x, self.y - other.y
        return tmp_point

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return (self.x * other.y) - (self.y * other.x)

    def length(self):
        return round(pow(pow(self.x, 2) + pow(self.y, 2), 0.5), 2)

    def __hash__(self):
        return hash((self.x, self.y))


class TestPoint(unittest.TestCase):
    def test_str(self):
        self.assertEqual(str(Point(3.0, 3.00)), "(3.0, 3.0)")
        self.assertEqual(str(Point(14.0000, 3.0)), "(14.0, 3.0)")
        self.assertEqual(str(Point(9.3, 4.0)), "(9.3, 4.0)")

    def test_repr(self):
        self.assertEqual(repr(Point(3.2, 3.200)), "Point(3.2, 3.2)")
        self.assertEqual(repr(Point(14.0000, 3.0)), "Point(14.0, 3.0)")
        self.assertEqual(repr(Point(9.3, 4.0)), "Point(9.3, 4.0)")
        self.assertEqual(repr(Point(9.3, -4.0)), "Point(9.3, -4.0)")

    def test_eq(self):
        self.assertEqual(Point(3.0, 3.0).__eq__(Point(3.0, 3.00)), True)
        self.assertFalse(Point(12.32, 5.555) == Point(3.0, 5.0))
        self.assertTrue(Point(12.32, 5.5) == Point(12.32, 5.5))
        self.assertFalse(Point(3.0, 3.0) == Point(3.0, -3.0))

    def test_ne(self):
        self.assertFalse(Point(4.2, 3.0) != Point(4.2, 3.0))
        self.assertTrue(Point(5.5, -2.0) != Point(5.5, 2.0))
        self.assertFalse(Point(-3.0, 2.0) != Point(-3.0, 2.0))

    def test_add(self):
        self.assertEqual(Point(2.0, 2.0) + Point(0.3, 1.7), Point(2.3, 3.7))
        self.assertEqual(Point(1.0, 3.0) + Point(-2.0, 1.0), Point(-1.0, 4.0))
        self.assertEqual(Point(5, 3) + Point(5, 7), Point(10, 10))

    def test_sub(self):
        self.assertEqual(Point(4.0, 2.0) - Point(1.0, 1.0), Point(3.0, 1.0))
        self.assertEqual(Point(0.0, 0.0) - Point(0.0, 2.0), Point(0.0, -2.0))
        self.assertEqual(Point(-6.0, 10.0) - Point(-2.0, 5.0), Point(-4.0, 5.0))

    def test_mul(self):
        self.assertEqual(Point(3.0, 1.0) * Point(3.0, -4.0), 5.0)
        self.assertEqual(Point(5.5, -1.2) * Point(4.3, 4.9), 17.77)
        self.assertEqual(Point(-3.0, 8.0) * Point(-6.0, 4.0), 50.0)

    def test_cross(self):
        self.assertEqual(Point(1.2, 2.6).cross(Point(-5.5, 3.0)), 17.9)
        self.assertEqual(Point(-3.0, 6.0).cross(Point(2.0, 2.0)), -18.0)
        self.assertEqual(Point(12.0, 45.0).cross(Point(5.0, 5.0)), -165.0)

    def test_length(self):
        self.assertEqual(Point(3.0, 4.0).length(), 5.0)
        self.assertEqual(Point(-3.0, 4.0).length(), 5.0)
        self.assertEqual(Point(-3.0, -4.0).length(), 5.0)
        self.assertEqual(Point(12.0, 14.0).length(), 18.44)


if __name__ == "__main__":
    unittest.main()
