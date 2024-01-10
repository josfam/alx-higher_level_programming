#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    all_squared = []  # collects squared lists
    for row in matrix:
        one_squared = [x**2 for x in row]
        all_squared.append(one_squared)
    return all_squared
