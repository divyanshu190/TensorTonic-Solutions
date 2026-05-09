import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    y = np.array(y) # this will change the array to numpy array
    if len(y) == 0: return 0.0
    value, count = np.unique(y, return_counts = True) # this will return the value and the it's count 
    prob = count / np.sum(count)
    ans = 0 # final answer
    for i in prob:
        if i == 0:
            continue
        ans -= i * np.log2(i)
    return ans
    pass