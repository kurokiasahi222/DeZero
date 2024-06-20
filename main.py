from functions import *

def main():
    A: Function = Square()
    B: Function = Exp()
    C: Function = Square()

    x: Variable = Variable(np.array(0.5))
    a: Variable = A(x)
    b: Variable= B(a)
    y: Variable = C(b)

    y.grad = np.array(1)
    y.backward()
    print("final result")
    print(x.grad)
    print("---------")
    y.grad = np.array(1)
    y.backward_recursive()
    print("final result")
    print(x.grad)
    

if __name__ == "__main__":
    main()