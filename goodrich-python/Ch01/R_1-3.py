'''R-1.3 Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution.'''

import sys


def minmax(data):
    min = data[0]
    max = data[0]
    
    for i in data:
        if i < min: 
            min = i
        elif i > max:
            max = i 
            
    return min, max


def main():
    # min, max = minmax([sys.argv[i] for i in range(1, len(sys.argv))])
    min, max = minmax(list(map(int, sys.argv[1:])))
    print("The smallest and largest numbers are {} and {}".format(min, max))


if __name__ == "__main__":
    main()