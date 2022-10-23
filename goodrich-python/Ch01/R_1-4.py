'''R-1.4 Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.'''

import sys


def sum_of_squares(max):
    assert isinstance(max, int) and max > 0
    n = max - 1
    return n * (n + 1) * (2 * n + 1) / 6


def main():
    sum = sum_of_squares(int(sys.argv[1]))
    print("Sum = {}".format(sum))
    
    
if __name__ == "__main__":
    main()
