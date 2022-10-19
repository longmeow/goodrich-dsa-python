'''Find majority element (Boyer-Moore Majority Vote Algorithm).
Given an integer array containing duplicates, return the majority element if present. 
A majority element appears more than n/2 times, where n is the array size.
For example, the majority element is 2 in array {2, 8, 7, 2, 2, 5, 2, 3, 1, 2, 2}.'''

'''Ý tưởng: sử dụng dictionary, một cấu trúc tương đương với hashmap gồm key-value, trong đó
key là các giá trị unique trong list và value là số lần xuất hiện của key'''


import sys 
        
        
def find_majarity_element(data: list[int]) -> int:
    dict_unique = {}
    for i in data:
        dict_unique[i] = dict_unique.get(i, 0) + 1
    
    for key, value in dict_unique.items():
        if value > len(data)/2:
            return key 


def main():
    data = list(map(int, sys.argv[1:]))
    print("The majority element is: {}".format(find_majarity_element(data)))
    

if __name__ == "__main__":
    main()


                
        
            