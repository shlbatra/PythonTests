import unittest

import calc


class TestCalc(unittest.TestCase):
    # class to create unit test cases for calc functionality
    def test_add(self):
        # naming convention. test_<methodname> for it to run else not recognize as test
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)
        # test for floor and regular division as code has regular division

        self.assertRaises(ValueError, calc.divide, 10, 0)  # Exception,Fn, args
        # better way to call using context manager
        with self.assertRaises(ValueError):  # check number div by 0 then ValueError
            calc.divide(10, 0)


if __name__ == "__main__":  # if run code directly, then run code below
    unittest.main()
# if not have main module here, then run using python3 -m unittest test_calc.py
