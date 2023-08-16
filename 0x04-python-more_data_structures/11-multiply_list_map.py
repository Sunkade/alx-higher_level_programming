#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    """
    Multiply elements in a list using map and a lambda function.
    """
    return list(map(lambda i: i * number, my_list))
