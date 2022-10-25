'''
Decode an array constructed from another array
Given an array constructed from another array A by taking the sum of every distinct pair in it, 
decode it to get the original array A back.
If the original array is A[0], A[1], … , A[n-1], then the input array is
{
  (A[0] + A[1]), (A[0] + A[2]), … (A[0] + A[n-1]),
  (A[1] + A[2]), (A[1] + A[3]), … (A[1] + A[n-1]),
  …
  …
  (A[i] + A[i+1]), (A[i] + A[i+2]), … (A[i] + A[n-1]),
  …
  …
  (A[n-2] + A[n-1])
}
'''


'''
Ý tưởng: Tìm phần tử đầu tiên A[0] rồi sau đó có thể dễ dàng tìm lại được các phần tử còn lại (A[i] = inp[i-1] - A[0])
Gọi dãy đầu vào là inp, số phần tử của dãy đầu vào là m, số phần tử của dãy đầu ra hay dãy gốc là n.
Dễ thấy: m = n(n-1)/2, hay n^2-n-2m = 0 -> n = (1+sqrt(8m+1))/2. Từ đề bài, thấy rằng:
  inp[0] = A[0] + A[1]
  inp[1] = A[0] + A[2]
  inp[n-1] = A[1] + A[2]
=> A[0] = (inp[0] + inp[1] - inp[n-1]) / 2
'''


from math import sqrt


def decode(inp):
    m = len(inp)
    n = int((sqrt(8 * m + 1) + 1) / 2)
    A = [0] * n
    
    if n == 1 or m == 1:
        A[0] = inp[0]
    else:
        A[0] = (inp[0] + inp[1] - inp[n-1]) // 2
 
    for i in range(1, n):
        A[i] = inp[i-1] - A[0]

    print(A)
 
 
if __name__ == '__main__':
    inp = [3, 4, 5, 6, 5, 6, 7, 7, 8, 9]
    decode(inp)