'''C-1.26 Write a short program that takes as input three integers, a, b, and c, from
the console and determines if they can be used in a correct arithmetic
formula (in the given order), like “a + b = c,” “a = b - c,” or “a * b = c.”'''

import sys


def match_arth_expr(a, b, c):
    if a + b == c:
        return "%i + %i = %i" % (a, b, c)
    elif a == b + c:
        return "%i = %i + %i" % (a, b, c)
    elif a - b == c:
        return "%i - %i = %i" % (a, b, c)
    elif a == b - c:
        return "%i = %i - %i" % (a, b, c)
    elif a * b == c:
        return "%i * %i = %i" % (a, b, c)
    elif a == b * c:
        return "%i = %i * %i" % (a, b, c)
    else:
        return "%i, %i, and %i do not match an arithmetic expression." % (a, b, c)


def main():
    a, b, c = map(int, sys.argv[1:4])
    print(match_arth_expr(a, b, c))
    

if __name__ == "__main__":
    main()