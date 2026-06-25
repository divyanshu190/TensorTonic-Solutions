import numpy as np

def focal_loss(p, y, gamma=2.0):
    """
    Compute Focal Loss for binary classification.
    """
    # Write code here
    p = np.array(p, dtype = float)
    y = np.array(y, dtype = float)
    pt = np.where(y == 1, p, 1 - p)
    loss = -((1 - pt) ** gamma) * np.log(pt)
    return np.mean(loss)
    pass