import numpy as np
def ridge_regression(X, y, lam):
    """
    Compute ridge regression weights using the closed-form solution.
    """
    # Write code here
    X = np.array(X, dtype = float)
    y = np.array(y, dtype = float)

    d = X.shape[1]
    xt = X.T
    i = np.eye(d)
    w = np.linalg.inv(xt @ X + lam * i) @ xt @ y
    return w.tolist()
    