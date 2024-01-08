#!/usr/bin/python3
def no_c(my_string):
    new_string = []
    for ch in my_string:
        if ch not in ('C', 'c'):
            new_string.append(ch)
    return ''.join(new_string)
