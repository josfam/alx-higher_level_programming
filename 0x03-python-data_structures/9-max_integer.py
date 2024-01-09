#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max = my_list[0]  # start with the first number

    for num in my_list:
        if (num > max):
            max = num
    return max
