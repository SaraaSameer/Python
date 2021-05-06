import numpy as np
import math

def Normalization(vect):
    res = []
    for x in range(0, len(vect)):
        num = math.sqrt(np.dot(vect[x],vect[x]))
        res.append(vect[x]/num)

    # Printing Normalized vectors
    for x in res:
        print(x)

def Gram_Schmidt(vect):

    res = [vect[0]]
    for i in range(1, len(vect)):
        v = vect[i]
        for j in range(0, i):
            v = v - np.dot(vect[i], res[j]) / np.dot(res[j], res[j]) * res[j]
        res.append(v)
    return res

# Sample Input
v1 = np.array([1, 2, 2])
v2 = np.array([-1, 0, 2])
v3 = np.array([0, 0, 1])
output = Gram_Schmidt([v1, v2, v3])
Normalization(output)