#!/usr/bin/python3
# 11-delete_at.py

def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return
    
    new_idx = 0
    for i in range(len(my_list)):
        if i != idx:
            my_list[new_idx] = my_list[i]
            new_idx += 1
    
    del my_list[new_idx:]
