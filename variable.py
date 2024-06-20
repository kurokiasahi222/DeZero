import numpy
from typing import TypeAlias

Function: TypeAlias = "Function"  # https://docs.python.org/3/library/typing.html

class Variable:
    '''
    Data within Variable class is assumed to be
    numpy ndarray
    '''
    def __init__(self, data: numpy.ndarray) -> None:
        self.data = data
        self.grad = None  # gradient: initial value = None, set it when calculated
        self.creator: Function = None

    def set_creator(self, func) -> None:
        self.creator = func

    def backward(self) -> None:
        # stack based solution
        funcs: list[Function] = [self.creator]
        while funcs:
            f: Function = funcs.pop()  # get the last element
            x: Variable = f.input
            x.grad = f.backward(self.grad)
            funcs.append(x.creator)

    def backward_recursive(self) -> None:  # recursive
        f: Function = self.creator 
        if f is not None:
            x = f.input
            x.grad = f.backward(self.grad)
            x.backward_recursive()

    