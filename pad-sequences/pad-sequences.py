import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    if max_len == None:
        maxi = 0
        for row in seqs:
            temp = len(row)
            maxi = max(maxi, temp)
        matrix = np.full((len(seqs), maxi), pad_value)
        for j in range(len(seqs)):
            for i in range(len(seqs[j])):
                matrix[j][i] = seqs[j][i]
        return matrix
    
    matrix = np.full((len(seqs), max_len), pad_value)
    for j in range(len(seqs)):
        for i in range(len(seqs[j])):
            if i >= max_len:
                continue
            matrix[j][i] = seqs[j][i]
    return matrix    
    pass