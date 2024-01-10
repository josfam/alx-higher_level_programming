#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    twos_dict = dict()
    for k, v in a_dictionary.items():
        twos_dict.update({k: v*2})
    return twos_dict
