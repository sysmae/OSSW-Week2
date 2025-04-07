import unittest
from src.operations.subtract import subtract

class TestSubtract(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_negative_numbers(self):
        self.assertEqual(subtract(-5, -10), 5)

    def test_zero(self):
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(5, 0), 5)

    def test_mixed_signs(self):
        self.assertEqual(subtract(5, -5), 10)
        self.assertEqual(subtract(-5, 5), -10)

if __name__ == '__main__':
    unittest.main()