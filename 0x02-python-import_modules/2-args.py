#!usr/bin/python3

import sys

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if len(sys.argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)

ops = {"+": add, "-": sub, "*": mul, "/": div}
operator = sys.argv[2]

if operator not in ops:
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)

try:
    a = int(sys.argv[1])
    b = int(sys.argv[3])
except ValueError:
    print("Invalid input. <a> and <b> must be integers.")
    sys.exit(1)

try:
    result = ops[operator](a, b)
    print("{} {} {} = {}".format(a, operator, b, result))
except Exception as e:
    print("An error occurred:", str(e))
