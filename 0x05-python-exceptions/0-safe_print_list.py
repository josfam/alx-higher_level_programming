#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    for i in range(x):
        try:
            print(my_list[i], end='')
            my_list[i+1]  # try to access the next element
        except IndexError:
            break
    print()
    return i + 1
