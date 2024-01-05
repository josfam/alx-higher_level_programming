#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        ascii_num = ord(ch)
        # shift by 32 to print the upper-cases
        if (97 <= ascii_num <= 122):
            print('{}'.format(chr(ascii_num - 32)), end='')
        else:
            print('{}'.format(ch), end='')
    print()
