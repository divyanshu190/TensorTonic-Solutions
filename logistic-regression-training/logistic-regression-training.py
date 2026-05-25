import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):

    X = np.array(X)
    y = np.array(y)
    b = 0 # bias
    w = np.zeros(X.shape[1]) # weight matrix

    for i in range(steps):
        z = []
        for row in X:
            s = 0
            for a in range(len(w)):
                s += row[a] * w[a]
            z.append(s+b) # at the place of this nested loop we can also use the '@' opertor this will also do the same work as this nested loop
        z = np.array(z)
        p = _sigmoid(z)
        w_error = (p - y) @ X
        b_error = p - y
        w = w - lr * w_error
        b = b - lr * np.mean(b_error)
    return w, b
    pass


# sigma(-z) = 1 - sigma(z)
# w and b are often zero initially
