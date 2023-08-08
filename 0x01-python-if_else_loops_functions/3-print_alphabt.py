#!/usr/bin/python3
# 3-print_alphabet.py


"""Print the alphabet in lowercase, not followed by a new line."""
for f in range(97, 123):
    if f != 101 and f != 113:
    print("{}".format(chr(f)), end="")
