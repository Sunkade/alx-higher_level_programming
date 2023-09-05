#!/usr/bin/python3
def matrix_divided(matrix, div):
    """Divide all elements of a matrix by a divisor.

    Args:
        matrix (list of lists): A list of lists containing integers or floats.
        div (int or float): The divisor.

    Raises:
        TypeError: If the matrix contains non-integer or non-float elements.
        TypeError: If the matrix rows have different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.

    Returns:
        list of lists: A new matrix representing the result of the division.
    """
    # Check if matrix is a list of lists containing integers or floats
    if (
        not isinstance(matrix, list)
        or not all(isinstance(row, list) for row in matrix)
        or not all(
            isinstance(element, (int, float))
            for row in matrix
            for element in row
        )
    ):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if all rows in the matrix have the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is an int or float and not 0
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform the division and round to 2 decimal places
    result = [[round(element / div, 2) for element in row] for row in matrix]

    return (result)
