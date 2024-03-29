from variable import Variable

class Function: 
    def __call__(self, input):
        x = input.data
        y = self.forward()
        output = Variable(y)
        return output
    
    def forward(self, x): 
        raise NotImplementedError()