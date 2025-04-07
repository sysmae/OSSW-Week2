import unittest
from src.operations.divide import divide

class TestDivide(unittest.TestCase):

    def test_divide_positive_numbers(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_negative_numbers(self):
        self.assertEqual(divide(-10, -2), 5)

    def test_divide_mixed_signs(self):
        self.assertEqual(divide(10, -2), -5)
        self.assertEqual(divide(-10, 2), -5)

    def test_divide_by_one(self):
        self.assertEqual(divide(10, 1), 10)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()