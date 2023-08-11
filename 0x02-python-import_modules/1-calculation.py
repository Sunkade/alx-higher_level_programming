#!/usr/bin/python3

a = 10
b = 5

from calculator_1 import add, subtract, multiply, divide

add_result = add(a, b)
subtract_result = subtract(a, b)
multiply_result = multiply(a, b)
divide_result = divide(a, b)

print(f"{a} + {b} = {add_result}")
print(f"{a} - {b} = {subtract_result}")
print(f"{a} * {b} = {multiply_result}")
print(f"{a} / {b} = {divide_result}")
