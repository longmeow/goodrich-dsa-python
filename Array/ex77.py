'''
Replace every array element with the least greater element on its right.
Given an array of distinct integers, replace every element with the least
greater element on its right or with -1 if there are no greater elements.
'''

'''
Ý tưởng: Duyệt 2 vòng for thông qua biến i và j, kiểm tra xem số nào lớn 
hơn nó "nhỏ nhất" trong dãy còn lại về bên phải thông qua 1 biến trung gian
'''


def replace(nums: list[int]) -> None:
    for i in range(len(nums)):
        # Biến diff để track xem phần tử nào là least_greater
        # trong các phần tử còn lại bên phải của dãy
        diff = float('inf')
        greater_to_be = -1
        
        for j in range(i+1, len(nums)):
            if nums[i] < nums[j] and nums[j] - nums[i] < diff:
                greater_to_be = nums[j]
                diff = nums[j] - nums[i]
        
        nums[i] = greater_to_be

    print(nums) 
    

def main():
    nums = [10, 100, 93, 32, 35, 65, 80, 90, 94, 6]
    replace(nums)


if __name__ == "__main__":
    main()