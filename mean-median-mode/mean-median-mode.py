import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    x = np.array(x, dtype = float)
    mean = np.sum(x) / len(x)

    x = np.sort(x)
    mid = len(x) // 2
    median = 0
    if len(x) % 2 == 0:
        median = (x[mid] + x[mid-1]) / 2
    else:
        median = x[mid]

    f = {}
    for i in x:
        if i in f:
            f[i] += 1
        else:
            f[i] = 1
    mode = None
    maxi = 0
    for num , count in f.items():
        if count > maxi:
            maxi = count
            mode = num
    return mean, median, mode
    pass