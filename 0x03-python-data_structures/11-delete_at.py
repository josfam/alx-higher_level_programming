#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx >= len(my_list) or idx < 0:
        return my_list
    new_list = []
    for i, num in enumerate(my_list):
        if not (i == idx):
            new_list.append(num)
    my_list = new_list
    return my_list
