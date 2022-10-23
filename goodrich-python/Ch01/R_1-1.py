'''R-1.1 Write a short Python function, is multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise.'''

import sys


def is_multiple(n, m):
    return n % m == 0


def main():
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    print("n is {}a multiple of m".format('' if is_multiple(n, m) else 'not '))
    
    
if __name__ == "__main__":
    main()