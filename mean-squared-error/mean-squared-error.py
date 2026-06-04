import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    # Write code here
    y_pred = np.array(y_pred)
    y_true = np.array(y_true)
    ans = 0
    for i in range(len(y_true)):
        ans += np.square(y_true[i] - y_pred[i])
    return ans / len(y_pred)
    pass
