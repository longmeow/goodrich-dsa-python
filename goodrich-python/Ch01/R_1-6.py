'''R-1.6 Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n.'''

import sys


def sum_of_odd_squares(n):
    assert n > 0
    return sum((i*i for i in range(n) if not i % 2 == 0))


def main():
    print("Sum of odds = {}".format(sum_of_odd_squares(int(sys.argv[1]))))
    

if __name__ == "__main__":
    main()