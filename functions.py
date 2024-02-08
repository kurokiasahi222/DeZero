from function_interface import Function
from variable import Variable
import numpy as np

'''
Child classes of function_interface
Includes actual implementation of functions to be used
'''
class Square(Function):
    '''
    Squares the input value
    y = x^2
    dy/dx = 2x
    '''
    def forward(self, x):
        return x ** 2
    
    def backward(self, gy):
        x = self.input.data
        gx = 2 * x * gy
        return gx

class Exp(Function):
    '''
    Calculates the exponential of the input value
    §'''
    def forward(self, x): 
        return np.exp(x)
    
    def backward(self, gy):
        x = self.input.data
        gx = np.exp(x) * gy
        return gx
    
def numerical_diff(f: Function, x: Variable, eps=1e-4):
    x0 = Variable(x.data - eps)
    x1 = Variable(x.data + eps)
    y0 = f(x0)
    y1 = f(x1)
    return (y1.data - y0.data) / (2 * eps)
