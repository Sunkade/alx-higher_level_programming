#!/usr/bin/python3
# 11-delete_at.py

def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return
    
    for i in range(idx, len(my_list) - 1):
        my_list[i] = my_list[i + 1]
    
    my_list.pop()
