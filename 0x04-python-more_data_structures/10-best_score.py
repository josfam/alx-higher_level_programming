#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    # make the first value of the first item the max
    max_key = list(a_dictionary.keys())[0]
    max_val = a_dictionary[max_key]

    for key, val in a_dictionary.items():
        if val > max_val:
            max_key = key
    return max_key
