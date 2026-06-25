import numpy as np
def average_pooling_2d(X, pool_size):
    """
    Apply 2D average pooling with non-overlapping windows.
    """
    # Write code here
    X = np.array(X, dtype = float)

    if X.ndim != 2 or pool_size <= 0:
        return None

    h, w = X.shape

    if h % pool_size != 0 or w % pool_size != 0:
        return None
    out_h = h // pool_size
    out_w = w // pool_size

    output = np.zeros((out_h, out_w))

    for i in range(out_h):
        for j in range(out_w):
            total = 0
            for r in range(pool_size):
                for c in range(pool_size):
                    total += X[i * pool_size + r][j * pool_size + c]
            output[i][j] = total / (pool_size ** 2)
                
    return output.tolist()