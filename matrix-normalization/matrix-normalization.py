import numpy as np

def matrix_normalization(matrix, axis=None, norm_type='l2'):
    """
    Normalize a 2D matrix along specified axis using specified norm.
    """
    # Write code here
    # L1
    matrix = np.array(matrix, dtype = float)
        
    if matrix.ndim != 2:
    
        return None
    
    if axis not in (None, 0, 1):
    
        return None
    
    if norm_type not in ("l1", "l2", "max"):
    
        return None
    if norm_type == 'l1':
        if axis is None:
            norm = np.sum(np.abs(matrix))
            if norm == 0:
                return matrix
            return matrix / norm
        elif axis == 0:
            norm = np.sum(np.abs(matrix), axis = 0)
            norm[norm == 0] = 1
            return matrix / norm
        elif axis == 1:
            norm = np.sum(np.abs(matrix), axis = 1, keepdims = True)
            norm[norm == 0] = 1
            return matrix / norm

    # L2
    elif norm_type == 'l2':
        if axis is None:
            norm = np.linalg.norm(matrix)
            if norm == 0:
                return matrix
            return matrix / norm
        elif axis == 0:
            norm = np.linalg.norm(matrix, axis = 0)
            norm[norm == 0] = 1
            return matrix / norm
        elif axis == 1:
            norm = np.linalg.norm(matrix, axis = 1, keepdims = True)
            norm[norm == 0] = 1
            return matrix / norm

    # Max Norm
    elif norm_type == 'max':
        if axis is None:
            norm = np.max(np.abs(matrix))
            if norm == 0:
                return matrix
            return matrix / norm    
        elif axis == 0:
            norm = np.max(np.abs(matrix), axis = 0)
            norm[norm == 0] = 1
            return matrix / norm
        elif axis == 1:
            norm = np.max(np.abs(matrix), axis = 1, keepdims = True)
            norm[norm == 0] = 1
            return matrix / norm
    else:
        raise ValueError("norm_type must be 'l1', 'l2', or 'max'")
    pass