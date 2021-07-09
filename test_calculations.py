import unittest
import calculations

class CalculationsTest(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculations.add(5, 5), 10)
        self.assertEqual(calculations.add(-1, 1), 0)
        self.assertEqual(calculations.add(-1, -1), -2)

    def test_multiply(self):
        self.assertEqual(calculations.multiply(5, 5), 25)
        self.assertEqual(calculations.multiply(-1, 1), -1)
        self.assertEqual(calculations.multiply(-1, -1), 1)

    def test_subtract(self):
        self.assertEqual(calculations.subtract(5, 5), 0)
        self.assertEqual(calculations.subtract(-1, 1), -2)
        self.assertEqual(calculations.subtract(-1, -1), 0)

    def test_divide(self):
        self.assertEqual(calculations.divide(5, 5), 1)
        self.assertEqual(calculations.divide(-1, 1), -1)
        self.assertEqual(calculations.divide(-1, -1), 1)

        # self.assertRaises(ValueError, calculations.divide, 10, 0)
        # or with context manager
        with self.assertRaises(ValueError):
            calculations.divide(10, 0)



if __name__ == '__main__':
    unittest.main()
