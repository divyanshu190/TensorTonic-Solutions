import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    # Write code here
    x = np.array(x, dtype = float)
    
    if x.ndim == 1:
        maxi = np.max(x)
        x -= maxi

        x = np.exp(x)
        sumi = np.sum(x)
        x /= sumi
        
        return x
    else:
        for row in range(len(x)):
            maxi = np.max(x[row])
            x[row] -= maxi

            x[row] = np.exp(x[row])
            sumi = np.sum(x[row])
            x[row] /= sumi
        return x
    pass