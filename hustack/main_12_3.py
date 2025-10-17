def longest_subsequence(arr, Q):
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


if __name__ == "__main__":
    n, Q = map(int, input().split())
    arr = list(map(int, input().split()))
    print(longest_subsequence(arr, Q))
