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
    Backtracking

Phân tích:
    Ta xây dựng dãy hoán vị dần dần, từ trái sang phải.
    Tại mỗi bước:
    Duyệt qua tất cả các số từ 1..n.
    Nếu số chưa được chọn (used[i] = False) thì chọn nó (thêm vào dãy hiện tại).
    Gọi đệ quy để xây tiếp phần còn lại.
    Sau khi quay lui, bỏ chọn số đó để thử số khác.
    Khi dãy đạt đủ n phần tử → in ra kết quả.
    Vì ta duyệt số theo thứ tự tăng dần từ 1 → n, nên kết quả sinh ra tự nhiên theo thứ tự từ điển.

Complexity:
    Time: O(n!)
    Space: O(n)
'''

def backtrack(n: int, perm: list, used: list):
    if len(perm) == n:
        print(" ".join(map(str, perm)))
        return

    for i in range(1, n+1):  # duyệt từ 1..n để đảm bảo thứ tự từ điển
        if not used[i]:
            used[i] = True
            perm.append(i)
            backtrack(n, perm, used)
            perm.pop()        # bỏ phần tử cuối cùng (quay lui)
            used[i] = False   # bỏ đánh dấu

def generate_permutations(n: int):
    used = [False] * (n+1)   # mảng đánh dấu
    backtrack(n, [], used)

if __name__ == "__main__":
    n = int(input())
    generate_permutations(n)
