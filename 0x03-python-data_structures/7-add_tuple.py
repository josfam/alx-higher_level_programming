#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a_left, a_right = None, None
    b_left, b_right = None, None

    if not (len(tuple_a)):
        a_left, a_right = 0, 0
    elif (len(tuple_a) == 1):
        a_left, a_right = tuple_a[0], 0
    else:
        a_left, a_right = tuple_a[0], tuple_a[1]

    if not (len(tuple_b)):
        b_left, b_right = 0, 0
    elif (len(tuple_b) == 1):
        b_left, b_right = tuple_b[0], 0
    else:
        b_left, b_right = tuple_b[0], tuple_b[1]

    return (a_left + b_left, a_right + b_right)
