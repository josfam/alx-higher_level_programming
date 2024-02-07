#!/usr/bin/python3

"""Write a script that adds all arguments to a Python list, and then save them
to a file
"""
import sys
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
outfile = 'add_item.json'
list_to_write = []

try:
    f = open(outfile, 'r', encoding='UTF-8')
    f.close()
except FileNotFoundError:
    # create the file and write an empty
    with open(outfile, 'w', encoding='UTF-8') as f:
        f.write(json.dumps(list_to_write))
else:
    # read the list from the file
    with open(outfile, 'r', encoding='UTF-8') as f:
        file_list = json.loads(f.readline())
        # append arguments to list
        for item in sys.argv[1:]:
            file_list.append(item)
    # add the updated list back
    with open(outfile, 'w', encoding='UTF-8') as f:
        f.write(json.dumps(file_list))
