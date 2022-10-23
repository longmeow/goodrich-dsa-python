'''C-1.24 Write a short Python function that counts the number of vowels in a given
character string.'''

def count_vowels(data):
    vowels = {'u', 'e', 'o', 'a', 'i'}
    count = 0
    
    for i in data.lower():
        if i in vowels:
            count += 1
    
    return count 


def main():
    data = input("Type something: ")
    print('Num of vowels: {}'.format(count_vowels(data)))
    

if __name__ == "__main__":
    main()