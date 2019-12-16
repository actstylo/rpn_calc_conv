import unittest
from rpn_calculator import calculate  

class TestRpnCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculate(['1', '2', '+']), [3.0])

    def test_division(self):
        self.assertEqual(calculate(['4', '2', '/']), [2.0])
