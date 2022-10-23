'''C-1.21 Write a Python program that repeatedly reads lines from standard input
until an EOFError is raised, and then outputs those lines in reverse order
(a user can indicate end of input by typing ctrl-D).'''

def print_reverse():
    lines = []
    
    while True:
        try:
            line = input()
        except EOFError:
            break
        lines.append(line)
    print("\n")
    
    for line in reversed(lines):
        print(line)
    
    
def main():
    print_reverse()
    
    
if __name__ == "__main__":
    main()