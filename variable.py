class Variable:
    '''
    Data within Variable class is assumed to be
    numpy ndarray
    '''
    def __init__(self, data):
        self.data = data
        self.grad = None  # gradient: initial value = None, set it when calculated
        self.creator = None

    def set_creator(self, func):
        self.creator = func

    def backward(self):
        f = self.creator  # function
        if f is not None:
            x = f.input
            x.grad = f.backward(self.grad)
            print(x.grad)
            x.backward()