'''C-1.22 Write a short Python program that takes two arrays a and b of length n
storing int values, and returns the dot product of a and b. That is, it returns
an array c of length n such that c[i] = a[i] · b[i], for i = 0, . . . , n - 1.'''

def array_product(a, b):
    return [i * j for i, j in zip(a, b)]


def main():
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = array_product(a, b)
    print(c)
    

if __name__ == "__main__":
    main()