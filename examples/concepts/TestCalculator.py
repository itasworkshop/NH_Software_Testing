import unittest

from Calculator import addition


class TestCalculatorMethods(unittest.TestCase):

    def testAddition(self):
        self.assertEqual(addition(10,20) ,40)

if __name__ == '__main__':
    unittest.main()