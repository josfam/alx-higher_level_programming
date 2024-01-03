#!/usr/bin/python3
sep = ', '
for left in range(9):  # left digit from 0 to 8
    for right in range(left + 1, 10):
        if (left == 8 and right == 9):
            sep = ''
        print('{}{}{}'.format(left, right, sep), end='')
print()
