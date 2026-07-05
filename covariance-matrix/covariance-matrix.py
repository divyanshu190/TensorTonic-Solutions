import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here
    X = np.array(X, dtype = float)
    mean = np.mean(X, axis = 0)
    x_center = X - mean

    if X.ndim != 2 or X.shape[0] < 2:
        return None
    
    return (1 / (X.shape[0] - 1)) * (x_center.T @ x_center)
    pass