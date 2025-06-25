import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Create a calculator instance for each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test addition of various number types."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-3, -7), -10)
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)
        self.assertAlmostEqual(self.calc.add(1.111, 2.222), 3.333, places=3)

    def test_subtract(self):
        """Test subtraction with positive, negative and float numbers."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(5.5, 2.2), 3.3)
        self.assertAlmostEqual(self.calc.subtract(3.333, 1.111), 2.222, places=3)

    def test_multiply(self):
        """Test multiplication including zero and negative numbers."""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 5), -10)
        self.assertEqual(self.calc.multiply(-3, -3), 9)
        self.assertEqual(self.calc.multiply(0, 10), 0)
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)

    def test_divide(self):
        """Test division and handle division by zero."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-9, 3), -3)
        self.assertAlmostEqual(self.calc.divide(7.5, 2.5), 3.0)
        self.assertIsNone(self.calc.divide(5, 0))  # Division by zero
        self.assertEqual(self.calc.divide(0, 3), 0)

    def test_divide_float_precision(self):
        """Test float precision in division."""
        result = self.calc.divide(10, 3)
        self.assertAlmostEqual(result, 3.3333333, places=6)

if __name__ == "__main__":
    unittest.main()
