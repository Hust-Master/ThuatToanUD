'''
There are n passengers 1, 2, …, n. The passenger i want to travel from point i to point i + n (i = 1,2,…,n). 
There is a bus located at point 0 and has k places for transporting the passengers (it means at any time, there are at most k passengers on the bus). 
You are given the distance matrix c in which c(i,j) is the traveling distance from point i to point j (i, j = 0,1,…, 2n). 
Compute the shortest route for the bus, serving n passengers and coming back to point 0. 

Input
    Line 1 contains n and k (1≤n≤11,1≤k≤10)
    Line i+1 (i=1,2,…,2n+1) contains the (i−1)th
    Line of the matrix c (rows and columns are indexed from 0,1,2,..,2n).
Output
    Unique line contains the length of the shortest route.

Example
Input
    3  2
    0  8  5  1  10  5  9
    9  0  5  6  6  2  8
    2  2  0  3  8  7  2
    5  3  4  0  3  2  7
    9  6  8  7  0  9  10
    3  8  10  6  5  0  2
    3  4  4  5  2  2  0
Output
    25
'''

def solve():
    n, k = map(int, input().split())
    size = 2 * n + 1
    c = [list(map(int, input().split())) for _ in range(size)]

    INF = 10**12
    full_mask = (1 << (2*n)) - 1

    # dp[mask][pos][load] = minimal cost to reach pos with visited mask and load passengers onboard
    from collections import defaultdict, deque
    dp = {}
    start = (0, 0, 0)  # mask, pos, load
    dp[start] = 0
    ans = INF
    q = deque([start])

    while q:
        mask, pos, load = q.popleft()
        cost = dp[(mask,pos,load)]
        if mask == full_mask and pos == 0 and load == 0:
            ans = min(ans, cost)
            continue
        # try go to next point
        for nxt in range(1, 2*n+1):
            if (mask >> (nxt-1)) & 1: 
                continue
            newload = load
            if nxt <= n:  # pickup
                if load == k: 
                    continue
                newload += 1
            else:  # dropoff
                pid = nxt - n
                if ((mask >> (pid-1)) & 1) == 0:
                    continue
                newload -= 1
            newmask = mask | (1 << (nxt-1))
            newcost = cost + c[pos][nxt]
            state = (newmask, nxt, newload)
            if newcost < dp.get(state, INF):
                dp[state] = newcost
                q.append(state) # type: ignore
        # allow returning to depot only if all served
        if mask == full_mask and load == 0 and pos != 0:
            newcost = cost + c[pos][0]
            state = (mask, 0, 0)
            if newcost < dp.get(state, INF):
                dp[state] = newcost
                q.append(state)

    print(ans)

if __name__ == "__main__":
    solve()


