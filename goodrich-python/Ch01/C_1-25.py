'''C-1.25 Write a short Python function that takes a string s, representing a sentence,
and returns a copy of the string with all punctuation removed. For exam-
ple, if given the string "Let's try, Mike.", this function would return
"Lets try Mike".'''

def remove_punc(data):
    punc = "[!\"#$%&'()*+,./:;<=>?@\^_`{|}~-]"
    result = []
    
    for char in data:
        if char not in punc:
            result.append(char)
            
    return ''.join(result)


def main():
    data = input("Type something: ")
    print(remove_punc(data))
    
    
if __name__ == "__main__":
    main()