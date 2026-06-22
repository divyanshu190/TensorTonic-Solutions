import numpy as np

def conv2d(x, W, b):
    """
    Simple 2D convolution layer forward pass.
    Valid padding, stride=1.
    """
    # Write code here
    n, Cin, h, win = x.shape
    Cout, _, kh, kw = W.shape
    hout = h - kh + 1
    wout = win - kw + 1
    out = np.zeros((n, Cout, hout, wout))
    for n in range(n):
        for cout in range(Cout):
            for i in range(hout):
                for j in range(wout):
                    total = 0
                    for cin in range(Cin):
                        for u in range(kh):
                            for v in range(kw):
                                total += x[n, cin, i + u, j + v] * W[cout, cin, u, v] 
                    out[n, cout, i, j] = total + b[cout]
    return out
    pass