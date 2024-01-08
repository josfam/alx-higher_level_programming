#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if (idx >= len(my_list) or idx < 0):  # returns the original list
        return my_list
    new_list = my_list[:]  # copy the original list
    new_list[idx] = element
    return new_list
