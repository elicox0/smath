import numpy as np
import sympy as sy
from typing import Union

def V(*args) -> np.ndarray:
    """
    Shorthand for a vector. Wrapper around
    numpy.array. Works on 1-d arrays with
    individual arguments, or on nd-arrays
    with iterable arguments as axes.
    """
    return np.array(args)

def M(*args) -> sy.Matrix:
    """
    Shorthand for a vector. Wrapper around
    numpy.array. Works on 1-d arrays with
    individual arguments, or on nd-arrays
    with iterable arguments as axes.
    """
    return sy.Matrix(args)

def _scale_row(
        arr : np.ndarray | sy.Matrix,
        row : int,
        c   : int
    ) -> np.ndarray | sy.Matrix:
    arr[row] *= c
    return arr

def _swap_rows(
        arr : np.ndarray | sy.Matrix,
        i   : int,
        j   : int
    ) -> np.ndarray | sy.Matrix:
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr

def _add_i_to_j(
        arr : np.ndarray | sy.Matrix,
        i   : int,
        j   : int,
        c   : int = 1
        ) -> np.ndarray | sy.Matrix:
    arr[j] += c * arr[i]
    return arr

def _get_pivot_col(
        arr : np.ndarray | sy.Matrix,
        row : int
        ) -> int:
    return 0

def _order_rows(
        arr : np.ndarray | sy.Matrix
        ) -> np.ndarray | sy.Matrix:
    i = 0
    while i < arr.shape[1]:
        arr[i :, :] = sorted(arr[i :, :], key=lambda x:x[i]==0)
        

def ref(
        matrix : np.ndarray | sy.Matrix
        ) -> np.ndarray | sy.Matrix:
    """
    Row echelon form of a matrix. NOT reduced or RREF.
    """
    matrix = _order_rows(matrix)
    _add_i_to_j(matrix, 1,2)
    _swap_rows(matrix, 1,2)
    _scale_row(matrix,0,2)
    return matrix
