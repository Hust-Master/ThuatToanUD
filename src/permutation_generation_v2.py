'''
Given an integer n, write a program to generate all permutations of 1, 2, ..., n in a lexicalgraphic order 
(elements of a permutation are separated by a SPACE character).

Example
Input 
    3
Output
    1 2 3 
    1 3 2 
    2 1 3 
    2 3 1 
    3 1 2 
    3 2 1 

Ý tưởng:
    Thuật toán sinh lặp (iterative)

Phân tích
    - Tập {1, 2, …, n} có tổng cộng n! hoán vị.
    - Lexicographic order nghĩa là sắp xếp các dãy giống như so sánh từ điển:
        + So sánh phần tử đầu tiên.
        + Nếu bằng nhau thì so tiếp phần tử thứ hai.
        + Cứ thế cho đến hết.
    - Ví dụ với n=3:
        {1,2,3} < {1,3,2} vì ở vị trí thứ 2: 2 < 3.
        {2,1,3} < {2,3,1} vì ở vị trí thứ 2: 1 < 3.
'''

def next_permutation(arr):
    # Tìm i: phần tử giảm đầu tiên từ cuối dãy
    i = len(arr) - 2
    while i >= 0 and arr[i] > arr[i+1]:
        i -= 1
    if i < 0:
        return False  # đã là hoán vị cuối cùng

    # Tìm j: phần tử nhỏ nhất bên phải arr[i] mà lớn hơn arr[i]
    j = len(arr) - 1
    while arr[j] < arr[i]:
        j -= 1

    # Hoán đổi
    arr[i], arr[j] = arr[j], arr[i]

    # Đảo ngược đoạn từ i+1 đến cuối
    arr[i+1:] = reversed(arr[i+1:])
    return True

def generate_permutations(n):
    arr = list(range(1, n+1))
    while True:
        print(" ".join(map(str, arr)))
        if not next_permutation(arr):
            break

if __name__ == "__main__":
    n = int(input("n = "))
    generate_permutations(n)
