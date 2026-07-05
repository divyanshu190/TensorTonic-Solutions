import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    A = np.array(A, dtype = float)
    t = 0
    for i in range(len(A)):
        t += A[i][i]
    return t
    pass
