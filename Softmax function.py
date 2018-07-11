
import numpy as np
scores = [5.2, 0.4, 10]

def softmax(x):
    return np.exp(x)/np.sum(np.exp(x),axis = 0)
print(softmax(scores))
