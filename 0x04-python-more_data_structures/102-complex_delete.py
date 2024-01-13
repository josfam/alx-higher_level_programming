#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    to_delete = []
    # store the keys to delete
    for k, v in a_dictionary.items():
        if v == value:
            to_delete.append(k)
    # delete keys
    for key in to_delete:
        del a_dictionary[key]

    return a_dictionary
