#!/usr/bin/python3
# 8-uppercase.py

def uppercase(s):
     for c in s:
        if ord('a') <= ord(c) <= ord('z'):
           c = chr(ord(c) - ord('a') + ord('A'))
        print("{}".format(c), end="")
    print("")
