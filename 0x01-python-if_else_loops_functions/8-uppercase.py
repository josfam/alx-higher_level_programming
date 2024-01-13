#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        # shift by 32 to print the upper-cases
        if (97 <= ord(ch) <= 122):
            to_print = chr(ord(ch) - 32)
        else:
            to_print = ch
        print('{}'.format(to_print), end='')
    print('{}'.format(''))
