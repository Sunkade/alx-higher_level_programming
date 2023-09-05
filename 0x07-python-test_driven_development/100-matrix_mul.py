#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    """Multiply two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.

    Raises:
        TypeError: If either m_a or m_b is not a list of lists of ints/floats.
        TypeError: If either m_a or m_b is empty.
        TypeError: If either m_a or m_b has different-sized rows.
        ValueError: If m_a and m_b cannot be multiplied.

    Returns:
        list of lists: A new matrix representing the multiplication of m_a by m_b.
    """

    # Check if m_a and m_b are empty
    if not m_a or not m_b:
        raise ValueError("m_a and m_b can't be empty")

    # Check if m_a and m_b are lists
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a and m_b must be lists")

    # Check if m_a and m_b are lists of lists
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a and m_b must be lists of lists")

    # Check if m_a and m_b contain only integers or floats
    if not all(isinstance(num, (int, float)) for row in m_a for num in row) or not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_a and m_b should contain only integers or floats")

    # Check if all rows of m_a have the same size
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must have the same size")

    # Check if all rows of m_b have the same size
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must have the same size")

    # Check if m_a and m_b can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b cannot be multiplied")

    # Perform matrix multiplication
    result_matrix = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            product = 0
            for k in range(len(m_b)):
                product += m_a[i][k] * m_b[k][j]
            row.append(product)
        result_matrix.append(row)

    return (result_matrix)
