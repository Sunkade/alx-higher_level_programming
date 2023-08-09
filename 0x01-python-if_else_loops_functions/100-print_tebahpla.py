#!/usr/bin/python3
# 100-print_tebahpla.py

i = 0
for i in range(ord('z'), ord('a') - 1, -1):
    print(f"{chr(i)}{chr(i-32)}", end='')
