import unittest
import calc


class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.addition(6,2), 8)
        self.assertEqual(calc.addition(6,2), 4)
    def test_diff(self):
        self.assertEqual(calc.difference(6,2), 4)
        self.assertEqual(calc.difference(6,2), 9)
    def test_mult(self):
        self.assertEqual(calc.multiplication(6,2), 12)
        self.assertEqual(calc.multiplication(6,2), 1)
    def test_sub(self):
        self.assertEqual(calc.division(6,2), 3)
        self.assertEqual(calc.division(6,2), 8)


if __name__ == "__main__":
    unittest.main()