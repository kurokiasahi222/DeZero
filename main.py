from functions import *

def main():
    A = Square()
    B = Exp()
    C = Square()

    x = Variable(np.array(0.5))
    a = A(x)
    b = B(a)
    y = C(b)

    y.grad = np.array(1)
    y.backward()
    print("final result")
    print(x.grad)

if __name__ == "__main__":
    main()