import numpy as np

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    x = np.array(x)
    y = np.array(y)
    ans = 0
    for i in range(x.size):
        ans += abs(x[i] - y[i])
    return float(ans)
    pass