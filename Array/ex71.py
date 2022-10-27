'''
Generate random input from an array according to given probabilities
Write an algorithm to generate any one of the given n numbers according to given probabilities.
'''

'''
Ý tưởng: bài này diễn đạt hơi củ chuối =))) do nó dễ nhưng diễn đạt khó. 
Giả sử có tất cả n số nums = [x1, x2,..., xn] cần được trả về với xác suất là prob = [p1, p2,..., pn]. 
B1: Tạo ra một list, gọi là sum_prob đi, cũng gồm n phần tử, từng phần tử sum_prob[i] sẽ là tổng
của xác suất prob[i] và toàn bộ phần tử trước nó, như vậy phần tử cuối cùng sẽ là 100. Điều này sẽ chia 
sum_prob thành các khoảng theo i có "độ rộng" tương đương với xác suất xuất hiện của phần tử thứ i 
trong dãy nums[n].
B2: Gọi hàm randrange, tạo ra 1 số ngẫu nhiên trong khoảng 1-100, xem nó nằm trong "vùng" - "khoảng" 
nào trong sum[i] thì tương ứng với phần tử nums[i] rồi trả về nums[i]  
'''


from random import randrange


def random(nums: list[int], prob: list[int]) -> int:
    n = len(nums)
    prob_sum = [None] * n
    
    prob_sum[0] = prob[0]
    for i in range(1, n):
        prob_sum[i] = prob_sum[i-1] + prob[i]
    
    r = randrange(1, 100)
    # Xét riêng trường hợp r rơi vào khoảng
    # đầu tiên trong prob_sum
    if r < prob_sum[0]:
        return nums[0]

    for i in range(1, n):
        if prob_sum[i-1] < r < prob_sum[i]:
            return nums[i]
    

def main():
    nums = [1, 2, 3, 4, 5]
    prob = [30, 10, 20, 15, 25]
    
    # Kiểm thử: gọi hàm random nhiều lần để kiểm tra
    # xác suất xuất hiện của các số
    
    freq = {}
    for i in range(10000000):
        val = random(nums, prob)
        freq[val] = freq.get(val, 0) + 1
    
    for i in range(len(nums)):
        print(f'{nums[i]} ~ {freq.get(nums[i]) / 100000.0}%')
        

if __name__ == "__main__":
    main()