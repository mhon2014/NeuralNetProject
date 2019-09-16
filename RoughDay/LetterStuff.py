import numpy as np

A1 = np.matrix('0 0 1 1 0 0 0; 0 0 0 1 0 0 0; 0 0 0 1 0 0 0; 0 0 1 0 1 0 0; 0 0 1 0 1 0 0; 0 1 1 1 1 1 0; 0 1 0 0 0 1 0; 0 1 0 0 0 1 0; 1 1 1 0 1 1 1')
A2 = np.matrix('0 0 0 1 0 0 0; 0 0 0 1 0 0 0; 0 0 0 1 0 0 0; 0 0 1 0 1 0 0; 0 0 1 0 1 0 0; 0 1 0 0 0 1 0; 0 1 1 1 1 1 0; 0 1 0 0 0 1 0; 0 1 0 0 0 1 0')
A3 = np.matrix('0 0 0 1 0 0 0; 0 0 0 1 0 0 0; 0 0 1 0 1 0 0; 0 0 1 0 1 0 0; 0 1 0 0 0 1 0; 0 1 1 1 1 1 0; 1 0 0 0 0 0 1; 1 0 0 0 0 0 1; 1 1 0 0 0 1 1')
B1 = np.matrix('1 1 1 1 1 1 0; 0 1 0 0 0 0 1; 0 1 0 0 0 0 1; 0 1 0 0 0 0 1; 0 1 1 1 1 1 0; 0 1 0 0 0 0 1; 0 1 0 0 0 0 1; 0 1 0 0 0 0 1; 1 1 1 1 1 1 0')
B2 = np.matrix('1 1 1 1 1 1 0; 1 0 0 0 0 0 1; 1 0 0 0 0 0 1; 1 0 0 0 0 0 1; 1 1 1 1 1 1 0; 1 0 0 0 0 0 1; 1 0 0 0 0 0 1; 1 0 0 0 0 0 1; 1 1 1 1 1 1 0')
B3 = np.matrix('1 1 1 1 1 1 0; 0 1 0 0 0 0 1; 0 1 0 0 0 0 1; 0 1 1 1 1 1 0; 0 1 0 0 0 0 1; 0 1 0 0 0 0 1; 0 1 0 0 0 0 1; 0 1 0 0 0 0 1; 1 1 1 1 1 1 0')
C1 = np.matrix('0 0 1 1 1 1 1; 0 1 0 0 0 0 1; 1 0 0 0 0 0 0; 1 0 0 0 0 0 0; 1 0 0 0 0 0 0; 1 0 0 0 0 0 0; 1 0 0 0 0 0 0; 0 1 0 0 0 0 1; 0 0 1 1 1 1 0')
C2 = np.matrix('0 0 1 1 1 0 0; 0 1 0 0 0 1 0; 1 0 0 0 0 0 1; 1 0 0 0 0 0 0; 1 0 0 0 0 0 0; 1 0 0 0 0 0 0; 1 0 0 0 0 0 1; 0 1 0 0 0 1 0; 0 0 1 1 1 0 0')
C3 = np.matrix('0 0 1 1 1 0 1; 0 1 0 0 0 1 1; 1 0 0 0 0 0 1; 1 0 0 0 0 0 0; 1 0 0 0 0 0 0; 1 0 0 0 0 0 0; 1 0 0 0 0 0 1; 0 1 0 0 0 1 0; 0 0 1 1 1 0 0')
D1 = np.matrix('1 1 1 1 1 0 0; 0 1 0 0 0 1 0; 0 1 0 0 0 0 1; 0 1 0 0 0 0 1; 0 1 0 0 0 0 1; 0 1 0 0 0 0 1; 0 1 0 0 0 0 1; 0 1 0 0 1 0 0; 1 1 1 1 1 0 0')
D2 = np.matrix('1 1 1 1 1 0 0; 1 0 0 0 0 1 0; 1 0 0 0 0 0 1; 1 0 0 0 0 0 1; 1 0 0 0 0 0 1; 1 0 0 0 0 0 1; 1 0 0 0 0 0 1; 1 0 0 0 0 1 0; 1 1 1 1 1 0 0')
D3 = np.matrix('1 1 1 1 1 0 0; 0 1 0 0 0 1 0; 0 1 0 0 0 0 1; 0 1 0 0 0 0 1; 0 1 0 0 0 0 1; 0 1 0 0 0 0 1; 0 1 0 0 0 0 1; 0 1 0 0 1 0 0; 1 1 1 1 1 0 0')
E1 = np.matrix('1 1 1 1 1 1 1; 0 1 0 0 0 0 1; 0 1 0 0 0 0 0; 0 1 0 1 0 0 0; 0 1 1 1 0 0 0; 0 1 0 1 0 0 0; 0 1 0 0 0 0 0; 0 1 0 0 0 0 1; 1 1 1 1 1 1 1')
E2 = np.matrix('1 1 1 1 1 1 1; 1 0 0 0 0 0 0; 1 0 0 0 0 0 0; 1 0 0 0 0 0 0; 1 1 1 1 1 0 0; 1 0 0 0 0 0 0; 1 0 0 0 0 0 0; 1 0 0 0 0 0 0; 1 1 1 1 1 1 1')
E3 = np.matrix('1 1 1 1 1 1 1; 0 1 0 0 0 0 1; 0 1 0 0 1 0 0; 0 1 1 1 1 0 0; 0 1 0 0 1 0 0; 0 1 0 0 0 0 0; 0 1 0 0 0 0 0; 0 1 0 0 0 1 0; 1 1 1 1 1 1 1')
J1 = np.matrix('0 0 0 1 1 1 1; 0 0 0 0 0 1 0; 0 0 0 0 0 1 0; 0 0 0 0 0 1 0; 0 0 0 0 0 1 0; 0 0 0 0 0 1 0; 0 1 0 0 0 1 0; 0 1 0 0 0 1 0; 0 0 1 1 1 0 0')
J2 = np.matrix('0 0 0 0 0 1 0; 0 0 0 0 0 1 0; 0 0 0 0 0 1 0; 0 0 0 0 0 1 0; 0 0 0 0 0 1 0; 0 0 0 0 0 1 0; 0 1 0 0 0 1 0; 0 1 0 0 0 1 0; 0 0 1 1 1 0 0')
J3 = np.matrix('0 0 0 0 1 1 1; 0 0 0 0 0 1 0; 0 0 0 0 0 1 0; 0 0 0 0 0 1 0; 0 0 0 0 0 1 0; 0 0 0 0 0 1 0; 0 0 0 0 0 1 0; 0 1 0 0 0 1 0; 0 0 1 1 1 0 0')
K1 = np.matrix('1 1 1 0 0 1 1; 0 1 0 0 1 0 0; 0 1 0 1 0 0 0; 0 1 1 0 0 0 0; 0 1 1 0 0 0 0; 0 1 0 1 0 0 0; 0 1 0 0 1 0 0; 0 1 0 0 0 1 0; 1 1 1 0 0 1 1')
K2 = np.matrix('1 0 0 0 0 1 0; 1 0 0 0 1 0 0; 1 0 0 1 0 0 0; 1 0 1 0 0 0 0; 1 1 0 0 0 0 0; 1 0 1 0 0 0 0; 1 0 0 1 0 0 0; 1 0 0 0 1 0 0; 1 0 0 0 0 1 0')
K3 = np.matrix('1 1 1 0 0 1 1; 0 1 0 0 1 0 0; 0 1 0 1 0 0 0; 0 1 1 0 0 0 0; 0 1 1 0 0 0 0; 0 1 0 1 0 0 0; 0 1 0 0 1 0 0; 0 1 0 0 0 1 0; 1 1 1 0 0 1 1')


def activationfunction(n):
    pass #if else stuff magic will happen

def hardlimit(x):
    pass

def main():
    print("oops")


if __name__ == "__main__":
    main()
    print(B1)

