'''
Find two odd occurring elements in an array without using any extra space.
Given an integer array, duplicates appear in it an even number of times except for two elements,
which appear an odd number of times. Find both odd appearing elements without using any extra memory.
'''

'''
Ý tưởng: tạo ra một dict rồi cho các phần tử của dãy vào làm keys với values là số lần xuất hiện bắt
đầu từ 0. Xác định thêm số lần xuất hiện là chẵn hay lẻ.
'''


def find_odd_occuring(nums):
    count_dict = {i: 0 for i in nums}
    for num in nums:
        if num in count_dict:
            count_dict[num] += 1
    
    odd_tracking = list()
    for key, value in count_dict.items():
        if value % 2 != 0:
            odd_tracking.append(key)
    
    return odd_tracking


def main():
    nums = [4, 3, 6, 2, 4, 2, 3, 4, 3, 3]
    odd_list = find_odd_occuring(nums)
    print('The odd occurring elements are {} and {}'.format(odd_list[0], odd_list[1]))


if __name__ == "__main__":
    main()        