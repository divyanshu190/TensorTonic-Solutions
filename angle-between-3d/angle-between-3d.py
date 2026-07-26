import numpy as np

def angle_between_3d(v, w):
    """
    Compute the angle (in radians) between two 3D vectors.
    """
    # Your code here
    v = np.array(v, dtype = float)
    w = np.array(w, dtype = float)
    norm_v = np.sqrt(np.sum(v ** 2))
    norm_w = np.sqrt(np.sum(w ** 2))

    if norm_v == 0 or norm_w == 0:
        return np.nan
    angle = np.dot(v, w) / (norm_v * norm_w)
    angle = np.clip(angle, -1.0, 1.0)
    return np.arccos(angle)
    pass