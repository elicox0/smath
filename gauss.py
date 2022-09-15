import numpy as np

def _pivot(A : np.ndarray, pivot_row : int, pivot_col : int) -> np.ndarray:
    """
    Pivots A around given pivot_row and pivot_column (entry). Returns a row equivalent
    matrix where the j-th column is the elementary basis vector e_i
    (i being the pivot row and j being the pivot column).
    """
    m, _ = A.shape
    # divide pivot_row i by A[i,j] so that A[i,j] is 1
    A[pivot_row, :] /= A[pivot_row, pivot_col]

    for row in range(m):
        if row == pivot_row:
            continue # Avoid zeroing out the pivot pivot_row
        # pivot_row i has A[i,j]*A[pivot_row] subtracted from it (thus zeroing out A[i,j])
        A[row] -= A[row, pivot_col] * A[pivot_row]
    return A

def gauss(A : np.ndarray) -> np.ndarray:
    """
    Row reduces  A.
    """
    m, n = A.shape
    for diag in range(min(m,n)):
        A = _pivot(A, diag, diag)
    return A

