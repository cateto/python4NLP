import numpy as np

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w*x) +b
    print(tmp) 
    if tmp <=0:
        return 0
    else:
        return 1

print(AND(0.5, 0.5))

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5]) # AND와 가중치만 다름
    b = 0.7
    tmp =np.sum(w*x)+b
    print(tmp)
    if tmp <=0:
        return 0
    else:
        return 1

print(NAND(0.5, 0.5))


def OR(x1, x2):
    x = np.array([x1,x2])
    w = np.array([0.5, 0.5]) # AND와 가중치만 다름
    b = -0.2
    tmp = np.sum(w*x)+b
    print(tmp)
    if tmp <=0:
        return 0
    else:
        return 1

print(OR(0.5, 0.5))