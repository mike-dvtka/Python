from points import Point
import unittest


class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        if x1 >= x2 or y1 >= y2:
            raise ValueError("Chcemy, aby x1 < x2, y1 < y2")
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):
        string = "[(" + str(self.pt1.x) + ", " + str(self.pt1.y) + "), (" + str(self.pt2.x) + ", " + str(
            self.pt2.y) + ")]"
        return string

    def __repr__(self):
        string = "Rectangle(" + str(self.pt1.x) + ", " + str(self.pt1.y) + ", " + str(self.pt2.x) + ", " + str(
            self.pt2.y) + ")"
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
        return abs(self.pt1.x - self.pt2.x) * abs(self.pt1.y - self.pt2.y)

    def move(self, x, y):
        self.pt1.x += x
        self.pt2.x += x
        self.pt1.y += y
        self.pt2.y += y
        return self

    def intersection(self, other):
        d_x2 = min(self.pt2.x, other.pt2.x)
        d_x1 = max(self.pt1.x, other.pt1.x)
        d_y2 = min(self.pt2.y, other.pt2.y)
        d_y1 = max(self.pt1.y, other.pt1.y)
        dx = d_x2 - d_x1
        dy = d_y2 - d_y1
        if (dx >= 0) and (dy >= 0):
            return Rectangle(d_x1, d_y1, d_x2, d_y2)
        else:
            raise ValueError("Prostokaty nie przecinaja sie")

    def cover(self, other):
        array_x = [self.pt1.x, self.pt2.x, other.pt1.x, other.pt2.x]
        array_y = [self.pt1.y, self.pt2.y, other.pt1.y, other.pt2.y]
        return Rectangle(min(array_x), min(array_y), max(array_x), max(array_y))

    def make4(self):
        rect_1 = Rectangle(self.pt1.x, self.pt1.y, self.center().x, self.center().y)
        rect_2 = Rectangle(self.pt1.x, self.center().y, self.center().x, self.pt2.y)
        rect_3 = Rectangle(self.center().x, self.center().y, self.pt2.x, self.pt2.y)
        rect_4 = Rectangle(self.center().x, self.pt1.y, self.pt2.x, self.center().y)
        tuple4small = (rect_1, rect_2, rect_3, rect_4)
        return tuple4small


class TestRectangle(unittest.TestCase):
    def test_str(self):
        self.assertEqual(str(Rectangle(2.0, 3.0, 2.1, 5.0)), "[(2.0, 3.0), (2.1, 5.0)]")
        self.assertEqual(str(Rectangle(-12.0, -32.0, 8.5, -31.0)), "[(-12.0, -32.0), (8.5, -31.0)]")
        self.assertEqual(str(Rectangle(0.3, -2.1, 5.0, 9.0)), "[(0.3, -2.1), (5.0, 9.0)]")

    def test_repr(self):
        self.assertEqual(repr(Rectangle(2.0, 3.0, 2.1, 5.0)), "Rectangle(2.0, 3.0, 2.1, 5.0)")
        self.assertEqual(repr(Rectangle(-12.0, -32.0, 8.5, -31.0)), "Rectangle(-12.0, -32.0, 8.5, -31.0)")
        self.assertEqual(repr(Rectangle(0.3, -2.1, 5.0, 9.0)), "Rectangle(0.3, -2.1, 5.0, 9.0)")

    def test_eq(self):
        self.assertTrue(Rectangle(2.0, 1.0, 3.0, 7.0) == Rectangle(2.0, 1.0, 3.0, 7.0))
        self.assertTrue(Rectangle(2.2, 1.0, 3.5, 7.1) == Rectangle(2.2, 1.0, 3.5, 7.1))
        self.assertFalse(Rectangle(2.9, 3.0, 4.0, 17.0) == Rectangle(-0.2, 1.3, 5.0, 7.0))
        self.assertFalse(Rectangle(-5.3, -12.6, 1.7, -7.3) == Rectangle(-22.5, 5.1, -1.1, 6.9))

    def test_ne(self):
        self.assertFalse(Rectangle(-4.0, -3.2, 1.0, -1.0) != Rectangle(-4.0, -3.2, 1.0, -1.0))
        self.assertTrue(Rectangle(-12.0, -34.0, -4.0, -2.0) != Rectangle(0.7, 11.5, 8.1, 21.0))
        self.assertTrue(Rectangle(-2.6, 6.0, -1.9, 11.6) != Rectangle(-2.6, -6.0, 1.9, 1.6))

    def test_center(self):
        self.assertEqual(Rectangle(0.0, 0.0, 9.0, 9.0).center(), Point(4.5, 4.5))
        self.assertEqual(Rectangle(-10.0, -5.0, 5.0, 10.0).center(), Point(-2.5, 2.5))
        self.assertEqual(Rectangle(1.5, -1.5, 12.0, 2.0).center(), Point(6.75, 0.25))

    def test_area(self):
        self.assertEqual(Rectangle(0.0, 0.0, 9.0, 9.0).area(), 81)
        self.assertEqual(Rectangle(-10.0, -5.0, 5.0, 10.0).area(), 225)
        self.assertEqual(Rectangle(1.5, -1.5, 12.0, 2.0).area(), 36.75)

    def test_move(self):
        self.assertEqual(str(Rectangle(0.0, 0.0, 0.1, 0.1).move(2.5, 1.0)), "[(2.5, 1.0), (2.6, 1.1)]")
        self.assertEqual(str(Rectangle(0.0, 0.0, 0.1, 0.1).move(-2.5, -1.0)), "[(-2.5, -1.0), (-2.4, -0.9)]")
        self.assertEqual(str(Rectangle(-9.0, -5.0, -4.0, 12.0).move(-5.9, 3.3)),
                         "[(-14.9, -1.7000000000000002), (-9.9, 15.3)]")

    def test_intersection(self):
        self.assertEqual(Rectangle(2.0, 1.0, 11.0, 6.0).intersection(Rectangle(4.0, 2.0, 9.0, 5.0)), Rectangle(4.0, 2.0, 9.0, 5.0))
        self.assertEqual(Rectangle(4.0, 2.0, 9.0, 5.0).intersection(Rectangle(2.0, 1.0, 11.0, 6.0)), Rectangle(4.0, 2.0, 9.0, 5.0))
        self.assertEqual(Rectangle(1.0, 1.0, 8.0, 4.0).intersection(Rectangle(5.0, 2.0, 16.0, 7.0)), Rectangle(5.0, 2.0, 8.0, 4.0))
        self.assertEqual(Rectangle(5.0, 2.0, 16.0, 7.0).intersection(Rectangle(1.0, 1.0, 8.0, 4.0)), Rectangle(5.0, 2.0, 8.0, 4.0))
        self.assertEqual(Rectangle(2.0, 2.0, 7.0, 7.0).intersection(Rectangle(2.0, 2.0, 7.0, 7.0)), Rectangle(2.0, 2.0, 7.0, 7.0))
        self.assertEqual(Rectangle(-2.0, -2.0, 2.0, 2.0).intersection(Rectangle(-2.0, -1.0, 7.0, 7.0)), Rectangle(-2.0, -1.0, 2.0, 2.0))

    def test_cover(self):
        self.assertEqual(Rectangle(0.0, 0.0, 2.0, 2.0).cover(Rectangle(1.0, 1.0, 5.0, 5.0)), Rectangle(0.0, 0.0, 5.0, 5.0))
        self.assertEqual(Rectangle(-2.0, -2.0, 2.0, 2.0).cover(Rectangle(5.0, 5.0, 10.0, 10.0)), Rectangle(-2.0, -2.0, 10.0, 10.0))
        self.assertEqual(Rectangle(-5.0, -5.0, 20.0, 20.0).cover(Rectangle(1.0, 1.0, 5.0, 5.0)), Rectangle(-5.0, -5.0, 20.0, 20.0))

    def test_make4(self):
        tuple1 = (Rectangle(0.0, 0.0, 5.0, 5.0), Rectangle(0.0, 5.0, 5.0, 10.0), Rectangle(5.0, 5.0, 10.0, 10.0), Rectangle(5.0, 0.0, 10.0, 5.0))
        tuple2 = (Rectangle(-5.0, -5.0, 0.0, 0.0), Rectangle(-5.0, 0.0, 0.0, 5.0), Rectangle(0.0, 0.0, 5.0, 5.0), Rectangle(0.0, -5.0, 5.0, 0.0))
        tuple3 = (Rectangle(10.0, 5.0, 15.0, 7.5), Rectangle(10.0, 7.5, 15.0, 10.0), Rectangle(15.0, 7.5, 20.0, 10.0), Rectangle(15.0, 5.0, 20.0, 7.5))
        self.assertEqual(Rectangle(0.0, 0.0, 10.0, 10.0).make4(), tuple1)
        self.assertEqual(Rectangle(-5.0, -5.0, 5.0, 5.0).make4(), tuple2)
        self.assertEqual(Rectangle(10.0, 5.0, 20.0, 10.0).make4(), tuple3)


if __name__ == "__main__":
    unittest.main()
