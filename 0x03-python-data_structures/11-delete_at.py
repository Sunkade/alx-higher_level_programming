#!/usr/bin/python3
# 11-delete_at.py

def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return
    
    new_idx = 0
    new_list = []
    for i in range(len(my_list)):
        if i != idx:
            new_list.append(my_list[i])
            new_idx += 1
    
    my_list.clear()
    my_list.extend(new_list)
