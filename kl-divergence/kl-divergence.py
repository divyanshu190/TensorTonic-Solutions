import numpy as np

def kl_divergence(p, q, eps=1e-12):
    """
    Compute KL Divergence D_KL(P || Q).
    """
    # Write code here
    p = np.array(p, dtype = float)
    q = np.array(q, dtype = float)
    return np.sum(p * np.log((p + eps) / (q + eps)))
    pass