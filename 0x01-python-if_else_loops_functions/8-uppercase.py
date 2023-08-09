#!/usr/bin/python3
# 8-uppercase.py

def uppercase(s):
    result = ""
    for c in s:
        if ord('a') <= ord(c) <= ord('z'):
            result += chr(ord(c) - ord('a') + ord('A'))
        else:
            result += c
    print(result)
