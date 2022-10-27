'''
Print all triplets in an array with a sum less than or equal to a given number.
Given an unsorted integer array, print all triplets in it with sum less than 
or equal to a given number.
'''

'''
Ý tưởng:
B1: Sắp xếp list theo thứ tự tăng dần
B2: Duyệt toàn bộ list và kiểm tra từ phần tử i và subarray [i+1,...n] có thoả mãn bộ
3 < given_sum. Cụ thể hơn, với biến i, tạo ra 2 biến low có idx = i+1 và high có idx = len(data),
vì đã sắp xếp nên chỉ cần kiểm tra tổng của i, low và high có thoả mãn đk hay không, nếu không thì
giảm idx của high đi 1 rồi tiếp tục kiểm tra tới khi thoả mãn, khi đó, tất cả các bộ 3 thoả mãn đk
bắt đầu từ idx, low và toàn bộ các phần tử từ low -> high. Tiếp tục tăng i trong vòng for cho tới 
khi nào high = low.  
'''


def find_triples(nums: list[int], given_sum: int) -> None:
    # sort the list
    nums.sort()
    # len(nums) -2 vì sau i còn low và high
    for i in range(len(nums)-2): 
        # tạo ra 2 biến low và high để kiểm tra xem bộ 3 có thoả
        # mãn điều kiện không
        low = i+1
        high = len(nums)-1
        
        while low < high:
            # giảm idx của high đi 1 nếu tổng idx i, low và high 
            # không thoả mãn đk
            if nums[i] + nums[low] + nums[high] > given_sum:
                high -= 1
            else:
                # nếu high thoả mãn điều kiện thì in ra toàn bộ
                # các bộ 3 thoả mãn đk, là các bộ gồm idx i, low
                # và khoảng từ low -> high thoả mãn đk
                for j in range(low+1, high+1):
                    print((nums[i], nums[low], nums[j]))
                # sau đó tăng low lên 1 đến khi hết vòng while rồi
                # tiếp tục tăng i đến khi duyệt toàn bộ list
                low += 1


def main():
    nums = [2, 7, 4, 9, 5, 1, 3]
    given_sum = 10
    find_triples(nums, given_sum)


if __name__ == "__main__":
    main()