import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    x = np.array(x)
    p = np.array(p)
    ans = 0
    sum = 0
    for i in p:
        sum += i
    if not np.isclose(sum, 1.0):
        raise ValueError("Probability sum should be one")
    if x.size != p.size:
        raise ValueError("Vectors must be of the same length")
    siz = x.size
    for i in range(siz):
        ans += x[i]*p[i]
    return ans
    pass
