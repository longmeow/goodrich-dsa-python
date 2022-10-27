'''
Find a subarray having the given sum in an integer array
'''


'''
Ý tưởng: Duyệt list lần lượt từ trái qua phải, tính tổng các phần
tử đã duyệt qua và lưu nó vào một dict với bộ key-value là 
sum_at_current_cell_to_the_very_left - index_of_cell, sau mỗi lần 
tính tổng, tức là cộng thêm phần tử kế tiếp vào chuối hiện tại, ta 
kiểm tra xem liệu sum_at_current_cell_to_the_leftmost - given_sum
có ở trong dict hay không, nếu có thì subarray đó chính là subarray
có tổng bằng given_sum với start_idx = idx_of(sum_at_current_cell_to_the_leftmost - given_sum)
và stop_idx = current_cell
'''


import sys


def find_subarray_with_given_sum(data: list[int], given_sum: int) -> None:
    sum_tracking = {}
    sum_so_far = 0
    # Trong trường hợp array cần tìm start tại idx = 0
    sum_tracking[0] = -1
    
    for idx, element in enumerate(data):
        sum_so_far += element
        
        if (sum_so_far - given_sum) in sum_tracking:
            print('Subarray having the given sum: {}'.format(data[sum_tracking[sum_so_far - given_sum]+1 : idx+1]))
            sys.exit(0)
            # return
        
        sum_tracking[sum_so_far] = idx


def main():
    data = [0, 5, -7, 1, -4, 7, 6, 1, 4, 1, 10]
    given_sum = 15
    find_subarray_with_given_sum(data, given_sum)
    
    
if __name__ == "__main__":
    main()