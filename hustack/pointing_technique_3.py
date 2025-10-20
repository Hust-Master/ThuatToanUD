def longest_subsequence(arr, Q):
    '''
    Given a sequence of positive integers a = a1, a2, . . ., an. 
    A subsequence of a is defined to be a sequence of consecutive elements ai, ai+1, . . ., aj (1 <= i <= j <= n). 
    The weight of a subsequence is the sum of its elements. Given a positive integer Q. 
    A subsequence is said to be feasible if the weight is less than or equal to Q.
    Find a feasible subsequence such that the number of elements of that subsequence is maximal.
    '''
    n = len(arr)
    l = 0
    current_sum = 0
    max_len = 0

    for r in range(n):
        current_sum += arr[r]

        # Thu hẹp cửa sổ nếu vượt quá Q
        while current_sum > Q and l <= r:
            current_sum -= arr[l]
            l += 1

        # Lúc này cửa sổ [l..r] có tổng ≤ Q
        max_len = max(max_len, r - l + 1)

    return max_len if max_len > 0 else -1

'''
Input
    Line 1: contains two positive integers n and Q (1 <= n <= 10^6, 1 <= Q <= 100000)
    Line 2: contains a1, a2, . . ., an (1 <= ai <= 10000).
Output
    Write the number of elements of the subsequence found, or write -1 if no such subsequence exists.
'''
if __name__ == "__main__":
    n, Q = map(int, input().split())
    arr = list(map(int, input().split()))
    print(longest_subsequence(arr, Q))
