import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    # Write code here
    v = np.array(v)
    n = v.size
    ans = np.empty((n, n))
    for i in range(n):
        for j in range(n):
            if i != j: ans[i][j] = 0
            else: ans[i][j] = v[i]
    return ans
    pass
