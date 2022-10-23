'''C-1.15 Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other (that is, they are distinct).'''

import sys


def is_distinct(data):
    temp = set()
    
    for i in data:
        temp.add(i)
        
    return len(temp) == len(data)


def main():
    print("All elements in list are {}distinct".format("" if is_distinct(list(map(int, sys.argv[1:]))) else 'not '))


if __name__ == "__main__":
    main()
    