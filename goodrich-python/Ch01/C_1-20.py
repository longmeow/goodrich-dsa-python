'''C-1.20 Python's random module includes a function shuﬄe(data) that accepts a
list of elements and randomly reorders the elements so that each possi-
ble order occurs with equal probability. The random module includes a
more basic function randint(a, b) that returns a uniformly random integer
from a to b (including both endpoints). Using only the randint function,
implement your own version of the shuﬄe function.'''

from random import randint
import sys


def shuffle_func(data):
    n = len(data)
    
    for i, _ in enumerate(data):
        j = randint(i, n-1)
        data[i], data[j] = data[j], data[i]
    
    return data    


def main():
    print(shuffle_func(list(map(int, sys.argv[1:]))))
    
    
if __name__ == "__main__":
    main()