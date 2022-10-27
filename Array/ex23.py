'''Print continuous subarray with maximum sum.
Given an integer array, find and print a contiguous subarray with the maximum sum in it.'''

'''Trước hết cần giải quyết bài toán tìm ra subarray có tổng lớn nhất
Sử dụng 2 phương pháp để giải quyết:
1. Brute-force
2. Kadane's Algs 
'''


import argparse
import time
import logging
import sys


def brute_force_o3(data: list[int]) -> None:
    '''
    Duyệt lần lượt qua toàn bộ các phần tử data,
    bắt đầu bằng phần tử bên trái cùng.
    
    Giữ cố định phần tử bên trái làm mốc, duyệt phần tử
    bên phải cùng của subarray đó tới khi hết data thì dừng
    
    Tính tổng tất cả các thành phần từ left tới right
    trong 2 vòng lặp trên, có thể thử dụng built-in function
    là list().sum() để giảm về O(n^2) nhưng không fair      

    So sánh subarray_sum của từng subarray một với global max_sum 
    rồi trả về trả trị lớn nhất
    '''
    max_sum = float('-inf')
    n = len(data)
    
    for left in range(n):
        for right in range(left, n):
            subarray_sum = 0
            
            for k in range(left, right+1):
                subarray_sum += data[k]

            max_sum = max(subarray_sum, max_sum)
            
    print(max_sum)


'''Có thể cải tiến brute_force về O(n^2): trong quá trình tính tổng
của các subarray, có nhiều subarray đã được tính toán từ trước, vì vậy
nếu có thể tận dụng lại thì sẽ không mất thêm 1 vòng lặp for để dành 
riêng cho việc tính tổng của từng subarray một'''


def brute_force_o2(data: list[int]) -> None:
    '''
    Duyệt lần lượt qua toàn bộ các phần tử data,
    bắt đầu bằng phần tử bên trái cùng.
    
    Giữ cố định phần tử bên trái làm mốc, duyệt phần tử
    bên phải cùng của subarray đó tới khi hết data thì dừng 
    
    Tính tổng tất cả các thành phần từ left tới right
    trong 2 vòng lặp trên, thay vì dùng thêm 1 vòng lặp
    for để tính như trên, chúng ta có thể tận dụng các kết 
    quả đã tính từ trước và chỉ cần "append" thêm phần tử bên
    cạnh là được. 

    So sánh running_sum của từng subarray một với global max_sum 
    rồi trả về trả trị lớn nhất
    '''
    max_sum = float('-inf')
    n = len(data)
    
    for left in range(n):
        running_sum = 0
        
        for right in range(left, n):
            '''
            Liên tục so sánh từng subarray với idx từ left 
            cho tới right, như vậy sẽ không cần phải dùng thêm
            vòng for để tính tổng lại từ đầu
            '''
            running_sum += data[right]
            max_sum = max(running_sum, max_sum)
            
    print(max_sum)


def kadane(data: list[int]) -> None:
    """
    Xét lần lượt từ trái qua phải, ta chia bài toán con được phát biểu như sau:
    "Tại mỗi idx, dãy con kết thúc tại đó có tổng lớn nhất là bao nhiêu?"
    Khi đó, chúng ta sẽ so sánh, max_so_far tại idx đó với max_so_far + giá trị ô
    liền kề nó và có 2 khả năng:
    1. Extend dãy tốt nhất có thể, tức là "append" idx đó vào chuỗi hiện tại
    2. Cắt đứt chuỗi hiện tại và bắt đầu chuối mới tại idx tiếp theo
    Sau khi hoàn thành tất cả các subproblems sẽ nhận được 1 dãy mà tại đó, mỗi thành phần i
    là tổng subarray tốt nhất mà array data[:i] có thể đạt được. Chọn phần tử lớn nhất, đó 
    chính là global max_so_far.
    
        Example:
    index     0  1   2  3   4  5  6   7  8
    Input: [ -2, 1, -3, 4, -1, 2, 1, -5, 4 ]
                -2, 1, -2, 4,  3, 5, 6,  1, 5    'max_ending_here' at each point
    """
    
    max_so_far = data[0]
    max_ending_here = data[0]
        
    for i in range(1, len(data)):

        max_ending_here = max(max_ending_here + data[i], data[i])
        max_so_far = max(max_ending_here, max_so_far)

    print(max_so_far)


def kadane_list(data: list[int]) -> None:
    '''Modify kadane() to print out the list'''
    
    max_so_far = data[0]
    max_ending_here = data[0]
        
    start = 0
    end = 0
    begin = 0
    
    for i in range(1, len(data)):
        max_ending_here = max_ending_here + data[i]
        
        if max_ending_here < data[i]:
            max_ending_here = data[i]
            begin = i
            
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = begin
            end = i
            
    print("The contiguous sublist with the largest sum is", data[start: end + 1])


def main():
    logging.basicConfig(level=logging.DEBUG)
    start = time.perf_counter()
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--complexity',
                        type = str,
                        help="complexity of algs, 'on', 'on2' or 'on3")
    parser.add_argument('-m', '--mode',
                        type = str,
                        help="'test' or 'mesure'")
    args = parser.parse_args()

    if args.mode is not None and args.complexity is not None:
        if args.mode == 'test':
            data = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        elif args.mode == 'mesure':
            data = list(range(-500,500))
    else:
        logging.critical('Choose your mode and complexity to run, ma fr!\nTry -h for more info')
        sys.exit(1)

    if args.complexity == 'on3':
        logging.info("Running on brute-force alg with complexity of {}...".format(args.complexity))
        brute_force_o3(data)
    elif args.complexity == 'on2':
        logging.info("Running on brute-force alg with complexity of {}...".format(args.complexity))
        brute_force_o2(data)
    elif args.complexity == 'on1':
        logging.info("Running on kadane alg with complexity of {}...".format(args.complexity))
        kadane(data)
    else:
        logging.info("Running on kadane alg with complexity of {}...".format(args.complexity))
        kadane_list(data)

    total = (time.perf_counter() - start) 
    logging.info('Running time: {}'.format(total))


if __name__ == "__main__":
    main() 