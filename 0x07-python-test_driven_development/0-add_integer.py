#!/usr/bin/python3
def add_integer(a, b=98):
    """Return the integer addition of a and b.

    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number (default is 98).

    Returns:
        int: The integer addition of a and b.

    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    return int(a) + int(b)
