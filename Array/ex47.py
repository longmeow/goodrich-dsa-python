'''
Maximum Product Subset Problem
Given an integer array, find the maximum product of its elements among all its subsets.
'''

'''
Ý tưởng: Tương tự như kadane, bài toán có 2 hướng tiếp cận:
1. Brute-force: duyệt tất cả các subset có thể (không sử dụng)
2. Linear-time solution: Đếm số lượng số âm và dương trong list rồi nhân lại, nếu là 0 thì
bỏ qua, nếu số số âm là chẵn thì nhân trực tiếp, nếu số lượng số âm là lẻ thì chia kết quả 
cho số âm có abs nhỏ nhất.
'''


def find_max_product(nums):
    n = len(nums)
    # Base case
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    
    product = 1
    
    # Tracking số âm có abs nhỏ nhất để loại trừ trong trường hợp số lượng số âm là lẻ
    abs_min_so_far = float('inf')
    
    negative = 0
    positive = 0
    
    contains_zero = False
    
    for idx in range(n):
        # Tracking nums of negative and positive number
        if nums[idx] < 0:
            negative += 1
            abs_min_so_far = min(abs_min_so_far, abs(nums[idx]))
        elif nums[idx] > 0:
            positive += 1
            
        if nums[idx] == 0:
            contains_zero = True
        else:
            product *= nums[idx]
    
    if negative % 2 != 0:
        product = product // -abs_min_so_far

    # special case – nếu trong list chỉ có số âm và 0
    if negative == 1 and positive == 0 and contains_zero:
        product = 0
 
    # special case – trong list chỉ toàn 0
    if negative == 0 and positive == 0 and contains_zero:
        product = 0
    
    return product


def main():
    nums = [-6, 4, -5, 8, -10, 0, 8]
    print('The maximum product of a subset is', find_max_product(nums))
    
    
if __name__ == '__main__':
    main()
