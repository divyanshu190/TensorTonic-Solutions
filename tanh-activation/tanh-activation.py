import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here
    x = np.array(x, dtype = float)
    neg = np.exp(-x)
    pos = np.exp(x)
    return (pos - neg) / (pos + neg)
    pass