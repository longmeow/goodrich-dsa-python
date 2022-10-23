'''C-1.28 The p-norm of a vector v = (v1 , v2 , . . . , vn ) in n-dimensional space is de-
ﬁned as ||v||. Give an implementation of a function named norm such that norm(v, p) returns the p-norm
value of v and norm(v) returns the Euclidean norm of v. You may assume that v is a list of numbers.
'''
import sys


def norm(v, p):
    sum_elements = sum(map(lambda x: x**p, v))
    return sum_elements**(1/p)


def main():
    v = list(map(int, sys.argv[2:]))
    p = int(sys.argv[1])
    print("||v|| with p = {} is {}".format(p, norm(v, p)))
    

if __name__ == "__main__":
    main()