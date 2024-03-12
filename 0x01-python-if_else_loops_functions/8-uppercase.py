#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        ord_ch = ord(ch)
        # shift by 32 to print the upper-cases
        if (97 <= ord_ch <= 122):
            print('{}'.format(chr(ord_ch - 32)), end='')
        else:
            print(ch, end='')

