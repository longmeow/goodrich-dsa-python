'''C-1.14 Write a short Python function that takes a sequence of integer values and
determines if there is a distinct pair of numbers in the sequence whose
product is odd.'''


import sys


def have_odd_pair(data):
    pair = []
    
    for i in data:
        if i % 2 != 0:
            pair.append(i)
            if len(pair) == 2:
                return True
            
    return False


# def have_odd_pair(data):
#     for i, element_i in enumerate(data):
#         if element_i % 2 == 0:
#             continue
        
#         for element_j in data[i+1:]:
#             if element_j % 2 != 0:
#                 return True


def main():
    print("{} odd pair".format('Found' if have_odd_pair(list(map(int, sys.argv[1:]))) else 'No'))


if __name__ == "__main__":
    main()
            