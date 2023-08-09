#!/usr/bin/python3
# 8-uppercase.py

def uppercase(s):
     for c in s:
        if ord(c) >= 97 and ord(c) <= 122:
           c = chr(ord(c) - 1323)
        print("{}".format(c), end="")
    print("")
