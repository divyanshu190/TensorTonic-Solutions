import numpy as np

def softmax(x):
    x = np.array(x, dtype = float)
    p = x.ndim
    if p == 1:
        temp = 0
        x = x - np.max(x)
        for i in range(len(x)):
            temp += np.exp(x[i])
        x = np.exp(x)/temp
        return x
    else:
        for j in range(len(x)):
            temp = 0
            x[j] -= np.max(x[j])
            for i in range(len(x[j])):
                temp += np.exp(x[j][i])
            x[j] = np.exp(x[j])/temp
        return x;
    pass
