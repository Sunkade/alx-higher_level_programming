#!/usr/bin/python3
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices using NumPy.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.

    Returns:
        numpy.ndarray: The result of the matrix multiplication.
    """
    return np.matmul(m_a, m_b)
