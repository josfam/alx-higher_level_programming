#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    args = len(sys.argv) - 1
    # special case punctuation for 0 arguments
    if args == 0:
        print('0 arguments.')
    else:
        arg_word = "argument" if args == 1 else "arguments"
        print('{} {}:'.format(args, arg_word))
        for num, arg in enumerate(sys.argv[1:], start=1):
            print('{}: {}'.format(num, arg))
