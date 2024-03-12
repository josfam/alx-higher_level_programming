#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        # shift by 32 to print the upper-cases
        if (97 <= ord(ch) <= 122):
            print('{}'.format(chr(ord(ch) - 32)), end='')
        else:
            print('{}'.format(ch), end='')
    print()
