from variable import Variable


class Function:
    '''
    Function Interface
    Actual calculation should be done in child classes
    '''
    def __call__(self, input):
        x = input.data
        y = self.forward(x)
        output = Variable(y)
        self.input = input
        return output
    
    def forward(self, x):
        '''
        Forward propagation
        Actual implementation in Child Classes
        '''
        raise NotImplementedError()
    
    def backward(self, gy):
        ''' 
        Back propagation. 
        Actual implementation in Child Classes
        '''
        raise NotImplementedError()