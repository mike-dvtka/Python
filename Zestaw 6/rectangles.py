from points import Point
import unittest


class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):
        string = "[(" + str(self.pt1.x) + ", " + str(self.pt1.y) + "), ("+str(self.pt2.x) + ", " + str(self.pt2.y) + ")]"
        return string

    def __repr__(self):
        string = "Rectangle(" + str(self.pt1.x) + ", " + str(self.pt1.y) + ", " + str(self.pt2.x) + ", " + str(self.pt2.y) + ")"
        return string

    def __eq__(self, other):
        if (self.pt1 == other.pt1) & (self.pt2 == other.pt2):
            return True
        else:
            return False

    def __ne__(self, other):
        return not self == other

    def center(self):
        center_point = Point((self.pt1.x + self.pt2.x) * 0.5, (self.pt1.y + self.pt2.y) * 0.5)
        return center_point

    def area(self):
        return round(abs(self.pt1.x - self.pt2.x) * abs(self.pt1.y - self.pt2.y), 2)

    def move(self, x, y):
        self.pt1.x += x
        self.pt2.x += x
        self.pt1.y += y
        self.pt2.y += y
        return self


class TestRectangle(unittest.TestCase):
    def test_str(self):
        self.assertEqual(str(Rectangle(5.0, 4.0, 3.0, 2.0)), "[(5.0, 4.0), (3.0, 2.0)]")
        self.assertEqual(str(Rectangle(-12.0, 3.0, 8.5, -32.0)), "[(-12.0, 3.0), (8.5, -32.0)]")
        self.assertEqual(str(Rectangle(0.3, 2.1, 5.0, -9.0)), "[(0.3, 2.1), (5.0, -9.0)]")

    def test_repr(self):
        self.assertEqual(repr(Rectangle(5.0, 4.0, 3.0, 2.0)), "Rectangle(5.0, 4.0, 3.0, 2.0)")
        self.assertEqual(repr(Rectangle(-12.0, 3.0, 8.5, -32.0)), "Rectangle(-12.0, 3.0, 8.5, -32.0)")
        self.assertEqual(repr(Rectangle(0.3, 2.1, 5.0, -9.0)), "Rectangle(0.3, 2.1, 5.0, -9.0)")

    def test_eq(self):
        self.assertTrue(Rectangle(2.0, 1.0, 3.0, 7.0) == Rectangle(2.0, 1.0, 3.0, 7.0))
        self.assertTrue(Rectangle(2.2, 1.0, 3.5, 7.1) == Rectangle(2.2, 1.0, 3.5, 7.1))
        self.assertFalse(Rectangle(4.0, 3.0, 4.0, -7.0) == Rectangle(0.2, 1.3, -5.0, 7.0))
        self.assertFalse(Rectangle(-5.3, -7.3, 1.7, -12.6) == Rectangle(22.5, 5.1, -1.1, 6.9))

    def test_ne(self):
        self.assertFalse(Rectangle(4.0, 3.2, 1.0, -1.0) != Rectangle(4.0, 3.2, 1.0, -1.0))
        self.assertTrue(Rectangle(12.0, 34.0, -4.0, -2.0) != Rectangle(0.7, 11.5, 8.1, 1.0))
        self.assertTrue(Rectangle(-2.6, 6.0, -1.9, -1.6) != Rectangle(2.6, -6.0, 1.9, 1.6))

    def test_center(self):
        self.assertEqual(Rectangle(0.0, 0.0, 9.0, 9.0).center(), Point(4.5, 4.5))
        self.assertEqual(Rectangle(-10.0, -5.0, 5.0, 10.0).center(), Point(-2.5, 2.5))
        self.assertEqual(Rectangle(1.5, -1.5, 12.0, 2.0).center(), Point(6.75, 0.25))

    def test_area(self):
        self.assertEqual(Rectangle(0.0, 0.0, 9.0, 9.0).area(), 81)
        self.assertEqual(Rectangle(-10.0, -5.0, 5.0, 10.0).area(), 225)
        self.assertEqual(Rectangle(1.5, -1.5, 12.0, 2.0).area(), 36.75)

    def test_move(self):
        self.assertEqual(str(Rectangle(0.0, 0.0, 0.0, 0.0).move(2.5, 1.0)), "[(2.5, 1.0), (2.5, 1.0)]")
        self.assertEqual(str(Rectangle(0.0, 0.0, 0.0, 0.0).move(-2.5, -1.0)), "[(-2.5, -1.0), (-2.5, -1.0)]")
        self.assertEqual(str(Rectangle(-4.0, 5.0, -9.0, -12.0).move(-5.9, 3.3)), "[(-9.9, 8.3), (-14.9, -8.7)]")


if __name__ == "__main__":
    unittest.main()
