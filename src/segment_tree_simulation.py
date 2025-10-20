"""
https://hustack.soict.ai/programming-contest/student-view-contest-problem-detail/20251ttudchbs/SEGMENT_TREE_SIM

Given a sequence of positive integers a1, a2, . . ., an. Perform a sequence of actions of following types:
    - update  i  v : assign ai = v
    - get-max  i  j : return the maximum value of the subsequence ai, ai+1, . . ., aj

Input
    Line 1: contains a positive integer n (1 <= n <= 100000)
    Line 2: contains a1, a2, . . ., an. (1 <= ai <= 10000)
    Line 3: contains a positive integer m (1 <= m <= 100000) which is the number of actions
    Line i + 3 (i = 1, 2, . . ., m): contains an action described above
Output
    Write in each line the result of the corresponding action of type get-max

Example:
Input
    10
    1 10 9 7 1 4 2 4 8 10
    5
    get-max 5 8
    get-max 5 9
    get-max 3 8
    update 9 20
    get-max 4 10

Ouput
    4
    8
    9
    20

Ý tưởng:
    - Dùng Segment Tree:
    - build: O(n).
    - update(i,v): gán a[i]=v → O(log n).
    - query(i,j): trả về max từ i đến j → O(log n).
"""

import sys

input = sys.stdin.readline


# Build Segment Tree
def build(node, l, r):
    if l == r:
        tree[node] = arr[l]
    else:
        mid = (l + r) // 2
        build(node * 2, l, mid)
        build(node * 2 + 1, mid + 1, r)
        tree[node] = max(tree[node * 2], tree[node * 2 + 1])


# Update ai = v
def update(node, l, r, idx, val):
    if l == r:
        tree[node] = val
    else:
        mid = (l + r) // 2
        if idx <= mid:
            update(node * 2, l, mid, idx, val)
        else:
            update(node * 2 + 1, mid + 1, r, idx, val)
        tree[node] = max(tree[node * 2], tree[node * 2 + 1])


# Query max in [ql, qr]
def query_max(node, l, r, ql, qr):
    if qr < l or r < ql:  # outside
        return -(10**9)
    if ql <= l and r <= qr:  # completely inside
        return tree[node]
    mid = (l + r) // 2
    return max(
        query_max(node * 2, l, mid, ql, qr), query_max(node * 2 + 1, mid + 1, r, ql, qr)
    )


# Query min in [ql, qr]
def query_min(node, l, r, ql, qr):
    if qr < l or r < ql:  # outside
        return float("inf")
    if ql <= l and r <= qr:  # completely inside
        return tree[node]
    mid = (l + r) // 2
    return min(
        query_min(node * 2, l, mid, ql, qr), query_min(node * 2 + 1, mid + 1, r, ql, qr)
    )


# ========================
n = int(input())
arr = [0] + list(map(int, input().split()))  # 1-indexed
tree = [0] * (4 * n)

build(1, 1, n)

m = int(input())
for _ in range(m):
    line = input().split()
    if line[0] == "update":
        i, v = int(line[1]), int(line[2])
        update(1, 1, n, i, v)
    elif line[0] == "get-max":
        i, j = int(line[1]), int(line[2])
        print(query_max(1, 1, n, i, j))
    elif line[0] == "get-min":
        i, j = int(line[1]), int(line[2])
        print(query_min(1, 1, n, i, j))
