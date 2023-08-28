#!/usr/bin/python3

def safe_print_division(a, b):
    """
    Returns the division of a by b.

    Args:
        a (float or int): The dividend.
        b (float or int): The divisor.

    Returns:
        The result of the division, or None on exception.
    """
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)
