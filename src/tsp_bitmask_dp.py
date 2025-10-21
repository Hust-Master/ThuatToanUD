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

def solve():
    data = input.split()
    it = iter(data)
    n = int(next(it))
    c = [[int(next(it)) for _ in range(n)] for __ in range(n)]

    INF = 10**12
    # dp[mask][i]: minimal cost to visit cities in mask and end at i
    size = 1 << n
    dp = [[INF] * n for _ in range(size)]
    dp[1][0] = 0  # start from city 0

    for mask in range(size):
        for i in range(n):
            if dp[mask][i] == INF:
                continue
            for j in range(n):
                if mask & (1 << j): 
                    continue
                newmask = mask | (1 << j)
                dp[newmask][j] = min(dp[newmask][j], dp[mask][i] + c[i][j])

    full = (1 << n) - 1
    ans = min(dp[full][i] + c[i][0] for i in range(n))
    print(ans)

if __name__ == "__main__":
    solve()
