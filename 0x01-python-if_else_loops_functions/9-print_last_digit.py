#!/usr/bin/python3
# 9-print_last_digit.py

def print_last_digit(number):
    last_digit = number % 10
    print(last_digit)
    return last_digit
last_digit = print_last_digit(12345)
print("Last digit:", last_digit)
