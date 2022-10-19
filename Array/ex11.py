'''Merge two arrays by satisfying given constraints.
Given two sorted arrays X[] and Y[] of size m and n each where m >= n and X[]
has exactly n vacant cells, merge elements of Y[] in their correct position in array X[],
i.e., merge (X, Y) by keeping the sorted order.'''

''' Về lý thuyết, được gợi ý sử dụng merge sort, do chưa học nên khum bik làm, còn nếu sử
dụng các build-in method của list trong python thì task sẽ được hoàn thành rất nhanh gọn'''


def merge_and_sort(X: list[int], Y: list[int]) -> list:
    return sorted(X+Y)


def main():
    X = [1, 3, 5, 7, 9]
    Y = [2, 4, 6, 8, 10]
    print(merge_and_sort(X, Y))


if __name__ == "__main__":
    main()
