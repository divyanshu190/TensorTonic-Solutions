import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    A = np.array(A)
    m, n = A.shape
    p = np.zeros((n, m))
    for x in range(m):
        for y in range(n):
            p[y, x] = A[x, y]
    return p
    pass
