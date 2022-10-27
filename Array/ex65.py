'''
Find the count of distinct elements in every subarray of size `k`
Given an array and an integer k, find the count of distinct elements in every subarray of size k.
'''

'''
Ý tưởng: Duyệt toàn bộ các subarray từ trái qua phải, sau đó chuyển thành set rồi đếm các 
phần tử trong set
'''


def count_distinct(nums: list[int], k: int) -> None:
    for idx in range(len(nums)-k+1):
        # Chuyển subarray vào set rồi đếm số phần tử
        num_distinct = len(set(nums[idx:idx+k]))
        print("The count of distinct elements in subarray {} is {}".format(nums[idx:idx+k], num_distinct))


def main():
    nums = [2, 1, 2, 3, 2, 1, 4, 5]
    k = 5
    count_distinct(nums, k)


if __name__ == "__main__":
    main()