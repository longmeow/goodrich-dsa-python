'''
Find subarrays with a given sum in an array.
Given an integer array, find subarrays with a given sum in it.
'''

'''
Ý tưởng: duyệt array lần lượt từ trái qua phải và cộng tổng lần
lượt các phần tử, sau đó add vào một dict với key là tổng lần lượt
các phần tử, value là idx của phần tử đó, với mỗi một key ở trong
dict, ta trừ đi given_sum, nếu tồn tại một key khác tức là trong dict
tồn tại 2 key mà hiệu nó là given_sum => subarray cần tìm chính là
subarray nằm giữa 2 key tìm được.  
'''


def find_subarray(nums: list[int], given_sum: int) -> list:
    sum_tracking = {}
    sum_so_far = 0
    # Trong trường hợp subarray thoả mãn bắt đầu từ đầu list
    sum_tracking.setdefault(0, []).append(-1)
    
    for idx, val in enumerate(nums):
        sum_so_far += val
        
        if (sum_so_far - given_sum) in sum_tracking:
            for start in sum_tracking[sum_so_far - given_sum]:
                print(nums[start+1:idx+1])
                
        sum_tracking.setdefault(sum_so_far, []).append(idx)


def main():
    nums = [3, 4, -7, 1, 3, 3, 1, -4]    
    given_sum = 7
    find_subarray(nums, given_sum)
    

if __name__ == "__main__":
    main()