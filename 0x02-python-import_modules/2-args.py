#!/usr/bin/python3

if __name__ == "__main__":
    """Handle basic arithmetic operations."""
from calculator_1 import add, sub, mul, div
import sys

def print_arguments(argv):
    num_arguments = len(argv)

    if num_arguments == 0:
        print("0 arguments.")
        return

    print(f"{num_arguments} {'argument' if num_arguments == 1 else 'arguments'}:", end=' ')

    if num_arguments == 1:
        print(argv[0])
    else:
        print(', '.join(argv))

    print(":")

    for i, arg in enumerate(argv, start=1):
        print(f"{i}: {arg}")

if __name__ == "__main__":
    print_arguments(sys.argv[1:])
