'''C-1.13 Write a pseudo-code description of a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than they
were before, and compare this method to an equivalent Python function
for doing the same thing.'''

import sys


def reverse_list(data):
    result = []
    
    for i in data:
        result.insert(0, i)
    return result


def main():
    print(reverse_list(sys.argv[1:]))


if __name__ == "__main__":
    main()