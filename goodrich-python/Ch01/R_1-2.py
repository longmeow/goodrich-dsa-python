'''R-1.2 Write a short Python function, is even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators.'''

import sys


def is_even(k):
    return k & 1 == 0


def main():
    k = int(sys.argv[1])
    print("k is {}".format('even' if is_even(k) else 'odd'))


if __name__ == "__main__":
    main()