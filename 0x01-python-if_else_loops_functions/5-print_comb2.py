#!/usr/bin/python3
sep = ', '
for num in range(100):
    if num == 99:  # don't print a comma after 99
        sep = ''
    print('{:02}{}'.format(num, sep), end='')
