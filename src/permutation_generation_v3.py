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

import itertools

def generate_permutations(n):
    arr = list(range(1, n+1))
    for perm in itertools.permutations(arr):
        print(" ".join(map(str, perm)))


if __name__ == "__main__":
    n = int(input())
    generate_permutations(n)
