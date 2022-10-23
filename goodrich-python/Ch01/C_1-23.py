'''C-1.23 Give an example of a Python code fragment that attempts to write an ele-
ment to a list based on an index that may be out of bounds. If that index
is out of bounds, the program should catch the exception that results, and
print the following error message:
“Don't try buffer overflow attacks in Python!”'''

from random import randint


def write_element(data, idx, sth):
    try:
        data[idx] = sth
    except IndexError:
        print("Don't try buffer overflow attacks in Python!")


def main():
    ex_list = [1, 2, 3, 4, 5]
    write_element(ex_list, randint(len(ex_list)+1, len(ex_list)+10), "longmeow")
    
    
if __name__ == "__main__":
    main()