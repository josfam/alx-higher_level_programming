#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        ascii_num = ord(ch)
        # shift by 32 to print the upper-cases
        new_ch = chr(ascii_num - 32) if (97 <= ascii_num <= 122) else ch
        print('{}'.format(new_ch), end='')
    print()
