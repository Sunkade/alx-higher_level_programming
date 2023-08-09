#!/usr/bin/python3

for s in range(0, 100):
    if s == 99:
        print("{:02}".format(s))
    else:
        print("{:02}".format(s), end=", ")   
