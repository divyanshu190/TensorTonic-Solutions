import numpy as np

# def d(a, p):
#     total = 0
#     for i in range(len(a)):
#         total += (a[i] - p[i]) ** 2
#     return total
def triplet_loss(anchor, positive, negative, margin=1.0):
    """
    Compute Triplet Loss for embedding ranking.
    """
    # Write code here
    anchor = np.array(anchor, dtype = float)
    positive = np.array(positive, dtype = float)
    negative = np.array(negative, dtype = float)

    ap = np.sum((anchor - positive) ** 2, axis = -1)
    an = np.sum((anchor - negative) ** 2, axis = -1)

    loss = np.maximum(0.0, ap - an + margin)
    return np.mean(loss)
    pass