'''
There are n cities 1, 2, ..., n. The travel distance from city i to city j is c(i,j), for i,j = 1, 2, ..., n.  A person departs from city 1, visits each city 2, 3, ..., n exactly once and comes back to city 1. Find the itinerary for that person so that the total travel distance is minimal.  

Input
    Line 1: a positive integer n (1 <= n <= 20)
    Line i+1 (i = 1, . . ., n): contains the ith row of the distance matrix x (elements are separated by a SPACE character)  
Output
    Write the total travel distance of the optimal itinerary found.

Example  
- Input:  
    4  
    0 1 1 9  
    1 0 9 3  
    1 9 0 2  
    9 3 2 0  
- Output:  
    7
'''

import sys

INF = int(1e9 + 7)                      # số rất lớn để khởi tạo ban đầu.
MAXN = 21

# Khởi tạo các biến toàn cục
n = 0                                   # tổng số lượng thành phố
current_cost = 0                        # tổng chi phí hiện tại.
best_cost = INF                         # chi phí tối ưu đã tìm được
visited = [0] * MAXN                    # đã đi qua thành phố j hay chưa.
x_best = [0] * MAXN                     # hành trình tối ưu.
x = [0] * MAXN                          # hành trình hiện tại
c = [[0] * MAXN for _ in range(MAXN)]   # c[i][j]: chi phí đi từ thành phố i đến j


def enter():
    global n, best_cost
    n = int(input())

    for i in range(1, n + 1):
        row = list(map(int, input().split()))
        for j in range(1, n + 1):
            c[i][j] = row[j - 1]

    # Thành phố đầu tiên là 1
    x[1] = 1
    visited[1] = 1

    best_cost = INF


def update_best_solution(current_cost):
    global best_cost
    if current_cost + c[x[n]][1] < best_cost:
        best_cost = current_cost + c[x[n]][1]
        for i in range(1, n + 1):
            x_best[i] = x[i]


def branch_and_bound(i):
    global current_cost
    if current_cost >= best_cost:
        return

    for j in range(2, n + 1):
        if not visited[j]:
            visited[j] = 1
            x[i] = j
            current_cost += c[x[i - 1]][j]

            if i == n:
                update_best_solution(current_cost)
            else:
                branch_and_bound(i + 1)

            # Quay lui
            visited[j] = 0
            current_cost -= c[x[i - 1]][j]


if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    enter()
    branch_and_bound(2)
    print(best_cost)
