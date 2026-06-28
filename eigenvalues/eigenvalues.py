import numpy as np

def calculate_eigenvalues(matrix):
    """
    Calculate eigenvalues of a square matrix.
    """
    try:
        matrix = np.array(matrix, dtype=float)

        # Check if matrix is square
        if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
            return None

        return np.linalg.eigvals(matrix)

    except Exception:
        return None