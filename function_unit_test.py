import unittest
import numpy as np
from variable import Variable
from functions import *

# Assuming Function, Square, and Exp are in the same file or properly imported

class TestSquareFunction(unittest.TestCase):
    def test_square_of_positive_number(self):
        input_data = Variable(np.array(2.0))
        square_function = Square()
        result = square_function(input_data)
        self.assertAlmostEqual(result.data, 4.0)

    def test_square_of_negative_number(self):
        input_data = Variable(np.array(-3.0))
        square_function = Square()
        result = square_function(input_data)
        self.assertAlmostEqual(result.data, 9.0)

    def test_square_of_zero(self):
        input_data = Variable(np.array(0.0))
        square_function = Square()
        result = square_function(input_data)
        self.assertAlmostEqual(result.data, 0.0)

class TestNumericalDiff(unittest.TestCase): 
    def test_positive_number(self):
        f = Square()
        x = Variable(np.array(2.0))
        dy = numerical_diff(f, x)
        self.assertAlmostEqual(dy, 4.0)
        
class TestExpFunction(unittest.TestCase):
    def test_exp_of_zero(self):
        input_data = Variable(np.array(0.0))
        exp_function = Exp()
        result = exp_function(input_data)
        self.assertAlmostEqual(result.data, 1.0)

    def test_exp_of_one(self):
        input_data = Variable(np.array(1.0))
        exp_function = Exp()
        result = exp_function(input_data)
        self.assertAlmostEqual(result.data, np.exp(1.0))

    def test_exp_of_negative_number(self):
        input_data = Variable(np.array(-1.0))
        exp_function = Exp()
        result = exp_function(input_data)
        self.assertAlmostEqual(result.data, np.exp(-1.0))

if __name__ == '__main__':
    unittest.main()
