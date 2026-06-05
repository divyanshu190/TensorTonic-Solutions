import numpy as np

def gini(y):
    classes, freq = np.unique(y, return_counts = True)
    prob = freq/len(y)
    gini = 1 - np.sum(prob ** 2)
    return gini
    
def gini_impurity(y_left, y_right):
    """
    Compute weighted Gini impurity for a binary split.
    """
    # Write code here
    y_left = np.array(y_left)
    y_right = np.array(y_right)

    # total sample 
    total_sample = len(y_left) + len(y_right)
    if total_sample == 0:
        return 0.0
    
    #weight of classes 
    left_weight = len(y_left) / total_sample
    right_weight = len(y_right) / total_sample

    # gini impurity
    gini_split = gini(y_left) * left_weight + gini(y_right) * right_weight

    return gini_split
    pass