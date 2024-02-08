class Variable:
    '''
    Data within Variable class is assumed to be
    numpy ndarray
    '''
    def __init__(self, data):
        self.data = data
        self.grad = None  # gradient: initial value = None, set it when calculated