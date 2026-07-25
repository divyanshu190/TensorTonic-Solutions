import numpy as np

def contrastive_loss(a, b, y, margin=1.0, reduction="mean") -> float:
    """
    a, b: arrays of shape (N, D) or (D,)  (will broadcast to (N,D))
    y:    array of shape (N,) with values in {0,1}; 1=similar, 0=dissimilar
    margin: float > 0
    reduction: "mean" (default) or "sum"
    Return: float
    """
    # Write code here
    a = np.array(a, dtype = float)
    b = np.array(b, dtype = float)
    y = np.array(y, dtype = float)

    if a.ndim == 1:
        a = a[None, :]
    if b.ndim == 1:
        b = b[None, :]
        
    d = np.linalg.norm(a - b, axis = -1)
    l = y * d ** 2 + (1 - y) * (np.maximum(0, margin - d) ** 2)
    if reduction == "mean":
        return np.mean(l)
    elif reduction == "sum":
        return np.sum(l)
    elif reduction == "none":
        return l
    pass