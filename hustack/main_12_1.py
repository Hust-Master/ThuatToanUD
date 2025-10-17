# Chapter 1. 2 pointing technique - sum pair of numbers on sorted sequence

def count_pairs (arr, Q):
    '''
    Given the sequence a[1], a[2], . . ., a[n] is sorted in ascending order (distinct elements: no elements with the same value). 
    Given the value Q, count M as the number of pairs of 2 indices i and j such that a[i] + a[j] = Q.
    Args:
        arr (list):  a[1], a[2], . . ., a[n] 
        Q (int): 1 <= n, Q <= 1000000
    Returns:
        M: 
    '''
    l, r = 0, len(arr) - 1
    count = 0
    while l < r:
        currentSum = arr[l] + arr[r]

        if (currentSum == Q):
            count += 1
            l += 1
            r -= 1
        elif (currentSum < Q):
            l += 1
        else:
            r -= 1
    return count

if __name__ == "__main__":
    n, Q = map(int, input().split())
    arr = list(map(int, input().split()))
    print("total pairs:", count_pairs(arr, Q))