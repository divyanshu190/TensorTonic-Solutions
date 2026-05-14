import numpy as np

def dropout(x, p=0.5, rng=None):
    """
    Apply dropout to input x with probability p.
    Return (output, dropout_pattern).
    """
    # Write code here
    if rng is None:
        rng = np.random.default_rng()
    x = np.array(x)
    mask = (rng.random(x.shape) > p).astype(float)
    
    pattern = mask/(1-p)

    output = x*pattern
    
    return output, pattern
    
    pass