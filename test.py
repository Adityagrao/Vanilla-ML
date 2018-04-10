import numpy as np 

def sigmoid(x):
    return 1/1+np.exp(-x)

x1 = -4
x2 = 5

print(sigmoid(4*x1+5*x2-9))