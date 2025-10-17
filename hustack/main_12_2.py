# Chapter 1. 2 pointing technique - sum pair of numbers on non-sorted sequence

def count_pairs (arr, Q):
    '''
    Given the sequence a[1], a[2], . . ., a[n] in which elements are distinct (no elements with the same value). 
    Given a positive value Q, count the number of pairs of 2 indices iand jsuch that a[i] + a[j] = Q.
    Args:
        arr (list):  a[1], a[2], . . ., a[n] 
        Q (int): 1 <= n, Q <= 1000000
    Returns:
        M (int): the number of pairs of 2 indices i and  j such that a[i] + a[j] = Q
    '''
    seen = set()
    count = 0
    for x in arr:
        if Q - x in seen:
            count += 1
        seen.add(x)
    return count

if __name__ == "__main__":
    n, Q = map(int, input().split())
    arr = list(map(int, input().split()))
    print("total pairs:", count_pairs(arr, Q))