import numpy as np

def root(a):
    ans = 0
    for i in a:
        ans += i**2
    return np.sqrt(ans)
    pass
def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    a = np.array(a)
    b = np.array(b)
    a_mag = root(a)
    b_mag = root(b)
    product = a_mag*b_mag
    if product == 0:
        return 0.0
    siz = a.size
    dot = 0
    for i in range(siz):
        dot += a[i]*b[i]
    return dot/product
    pass