import unittest
import calculations

class CalculationsTest(unittest.TestCase):

    def test_add(self):
        result = calculations.add(20, 5)
        self.assertEqual(result, 25)



if __name__ == '__main__':
    unittest.main()
