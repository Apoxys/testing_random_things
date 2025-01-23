#test_math_func

from math_func import math_functions
import unittest

class Test_Func(unittest.TestCase):

    def test_add(self):
        x = math_functions(3, 4)
        self.assertEqual(x.add(), 7)

    def test_mul(self):
        x = math_functions(3, 4)
        self.assertEqual(x.mul(), 12)
