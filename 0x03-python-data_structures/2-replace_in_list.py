#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if (idx >= len(my_list) or idx < 0):  # returns the original list
        return my_list
    my_list[idx] = element
    return my_list
