# Chapter 1.2 - 2pointing1DarraypairSumQ
def count_pairs (arr, Q):
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
    print(count_pairs(arr, Q))