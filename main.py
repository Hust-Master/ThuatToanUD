def count_pairs(arr, Q):
    l, r = 0, len(arr) - 1
    M = 0
    while l < r:
        s = arr[l] + arr[r]
        if s == Q:
            M += 1
            l += 1
            r -= 1
        elif s < Q:
            l += 1
        else:
            r -= 1
    return M


if __name__ == "__main__":
    n, Q = map(int, input().split())
    arr = list(map(int, input().split()))
    print(count_pairs(arr, Q))
