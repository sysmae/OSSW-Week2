import unittest
from src.operations.multiply import multiply

class TestMultiply(unittest.TestCase):
    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(5, 4), 20)

    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply(-2, -3), 6)
        self.assertEqual(multiply(-5, -4), 20)

    def test_multiply_positive_and_negative(self):
        self.assertEqual(multiply(2, -3), -6)
        self.assertEqual(multiply(-5, 4), -20)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(5, 0), 0)

if __name__ == '__main__':
    unittest.main()