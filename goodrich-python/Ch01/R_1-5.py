'''R-1.5 Give a single command that computes the sum from Exercise R-1.4, rely-
ing on Python's comprehension syntax and the built-in sum function.'''

import sys


def sum_of_squares(n):
    return sum((i*i for i in range(n)))


def main():
    print("Sum = {}".format(sum_of_squares(int(sys.argv[1]))))


if __name__ == "__main__":
    main()