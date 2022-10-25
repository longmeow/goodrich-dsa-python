'''
Trapping Rain Water Problem:
Find the maximum amount of water that can be trapped within a given set of bars where each bar's width is 1 unit.
'''

'''
Ý tưởng: Tạo ra 2 biến 'con trỏ' ở 2 đầu của dãy là left và right, sau đó lần lượt so sánh giá trị của left và right,
bên nào lớn (cao) hơn thì lượng nước có-thể-chứa-được chắc chắn nằm bên dưới cột thấp hơn. Sau khi đã so sánh 
được left và right, ta sẽ xét xem bên nào thấp hơn, gọi là lower, so sánh lower với cột cạnh kế bên nó
về phía ngược lại, ví dụ nếu left là lower thì so sánh với cột bên phải và ngược lại. So sánh xem lower và
cột kề nó xem cột nào cao hơn và lượng nước chứa được ở đây sẽ là hiệu cột cao và cột thấp. Sau đó tiếp tục so sánh
2 bên leftmost và rightmost rồi dịch lần lượt về phía ngược lại. Lặp lại quá trình như trên liên tục cho tới khi leftmost
và righmost trùng nhau.  
'''


def trap(heights):
    left = 0
    right = len(heights)-1
    water = 0
    
    max_left = heights[left]
    max_right = heights[right]
    
    while left < right:
        if heights[left] < heights[right]:
            left += 1
            max_left = max(max_left, heights[left])
            water += max_left - heights[left]
        else:
            right -= 1
            max_right = max(max_right, heights[right])
            water += max_right - heights[right]
    
    return water


def main():
    heights = [7, 0, 4, 2, 5, 0, 6, 4, 0, 5]
    print("The maximum amount of water that can be trapped is", trap(heights))
    
    
if __name__ == "__main__":
    main()