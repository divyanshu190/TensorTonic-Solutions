import numpy as np

def chi2_independence(C):
    """
    Compute chi-square test statistic and expected frequencies.
    """
    # Write code here
    C = np.array(C, dtype = float)

    if C.ndim != 2:
        return None
        
    row_sum = np.sum(C, axis = 1, keepdims = True)

    col_sum = np.sum(C, axis = 0, keepdims = True)

    total = np.sum(C)

    if total == 0:
        return None
    exp_freq = (row_sum * col_sum ) / total

    chi = np.sum(((C - exp_freq) ** 2) / exp_freq)

    return chi, exp_freq
    pass