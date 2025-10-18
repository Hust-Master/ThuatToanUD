# https://hustack.soict.ai/programming-contest/student-view-contest-problem-detail/20251ttudchbs/DISJOINT_SEGMENT

'''
Chapter 3. Disjoint Segment

Given a set of segments X = {(a1, b1), . . . , (an, bn)} in which ai < bi are coordinates of the segment i on a line, i = 1, …, n.  
Find a subset of X having largest cardinality in which no two segments of the subset intersect

Input
    Line 1: contains a positive integer n (1 <= n <= 100000)
    Line i+1 (i= 1,...,n): contains ai and bi (0 <= ai <= bi <= 1000000)
Output
    Number of segments in the solution found.

Example
Input
    6
    0 10
    3 7
    6 14
    9 11
    12 15
    17 19
Output
    4
'''

n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
segments.sort(key=lambda x: x[1])  # sắp xếp theo bi tăng dần

count, end = 0, -1
for a, b in segments:
    if a > end:
        count += 1
        end = b

print(count)
