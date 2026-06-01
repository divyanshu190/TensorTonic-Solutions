import numpy as np

def batch_norm_forward(x, gamma, beta, eps=1e-5):
    """
    Forward-only BatchNorm for (N,D) or (N,C,H,W).
    """
    # Write code here
    x = np.asarray(x)
    gamma = np.asarray(gamma)
    beta = np.asarray(beta)
    if len(x.shape) == 2:
        mean = np.mean(x, axis = 0, keepdims = True)
        var = np.var(x, axis = 0, keepdims = True)
        x_cap = (x - mean) / np.sqrt(
            var + eps
        )
        return x_cap * gamma + beta
    else:
        mean = np.mean(x,axis = (0, 2, 3), keepdims = True)
        var = np.var(x, axis = (0, 2, 3), keepdims = True)
        x_cap = (x - mean) / np.sqrt(
            var + eps
        )
        gamma = gamma.reshape(1, -1, 1, 1)
        beta = beta.reshape(1, -1, 1, 1)
        return x_cap * gamma + beta
    pass