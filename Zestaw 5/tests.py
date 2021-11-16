import fracs
import unittest


class TestFractions(unittest.TestCase):
    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(fracs.add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(fracs.add_frac([3, 4], [2, 9]), [35, 36])

    def test_sub_frac(self):
        self.assertEqual(fracs.sub_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(fracs.sub_frac([1, 3], [1, 2]), [-1, 6])
        self.assertEqual(fracs.sub_frac([5, 8], [4, 9]), [13, 72])

    def test_mul_frac(self):
        self.assertEqual(fracs.mul_frac([12, 12], [13, 12]), [13, 12])
        self.assertEqual(fracs.mul_frac([9, 2], [2, 9]), [1, 1])
        self.assertEqual(fracs.mul_frac([2, 5], [13, 17]), [26, 85])
        self.assertEqual(fracs.mul_frac([-3, 7], [2, 5]), [-6, 35])

    def test_div_frac(self):
        self.assertEqual(fracs.div_frac([3, 8], [1, 6]), [9, 4])
        self.assertEqual(fracs.div_frac([1, 11], [5, 7]), [7, 55])
        self.assertEqual(fracs.div_frac([1, 2], [-1, 3]), [3, -2])
        try:
            fracs.div_frac([4, 7], [0, 4])
        except ZeroDivisionError:
            pass
        except Exception:
            self.fail('Exception')

    def test_is_positive(self):
        self.assertEqual(fracs.is_positive([3, 8]), True)
        self.assertEqual(fracs.is_positive([2, -1]), False)
        self.assertEqual(fracs.is_positive([-1, 2]), False)
        self.assertEqual(fracs.is_positive([12, 9]), True)

    def test_is_zero(self):
        self.assertEqual(fracs.is_zero([2, 1]), False)
        self.assertEqual(fracs.is_zero([0, 2]), True)

    def test_cmp_frac(self):
        self.assertEqual(fracs.cmp_frac([3, 8], [1, 3]), 1)
        self.assertEqual(fracs.cmp_frac([1, 2], [2, 5]), 1)
        self.assertEqual(fracs.cmp_frac([2, 5], [1, 2]), -1)
        self.assertEqual(fracs.cmp_frac([9, 9], [9, 9]), 0)

    def test_frac2float(self):
        self.assertEqual(fracs.frac2float([1, 2]), 0.5)
        self.assertEqual(fracs.frac2float([1, 8]), 0.125)
        self.assertEqual(fracs.frac2float([-3, 8]), -0.375)
        self.assertEqual(fracs.frac2float([1, -10]), -0.1)

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()
