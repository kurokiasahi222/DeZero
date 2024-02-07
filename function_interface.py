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
        return output
    
    def forward(self, x): 
        raise NotImplementedError()