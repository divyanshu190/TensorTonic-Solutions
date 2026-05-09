import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    x = np.array(x)
    y = np.array(y)
    if x.size != y.size:
        raise ValueError("Dimenstion of both vector's should be same")
    ans = 0
    for i in range(x.size):
        ans += np.square(x[i] - y[i])
    return np.sqrt(ans)
    pass