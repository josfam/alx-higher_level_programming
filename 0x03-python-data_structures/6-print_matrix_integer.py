#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return
    for row in matrix:
        sep = ' '
        row_len = len(row)
        for index, num in enumerate(row):
            if index == row_len - 1:
                sep = ''
            print('{:d}{}'.format(num, sep), end='')
        print()
