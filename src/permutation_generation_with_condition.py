'''
Let the set N = {1, 2, 3, ..., n}. Each n-element permutation of the set N is represented by the array {a[1], a[2],..., a[n]}.   
An n-element permutation of the set N is perfect if each element a[i] (with i = 1, 2, .., n) in the permutation satisfies one of the following two conditions: 
1. a[i] is divisible by i;
2. i is divisible by a[i].

Input: a positive integer n (1 <= n <= 15).  
Output: Number of perfect permutations including n elements created from the set N = {1, 2, ..., n}.

Example 1:  
- Input: 1  
- Output: 1

Example 2:  
- Input: 5  
- Output: 10
'''

def count_perfect_permutations(n: int) -> int:
    used = [False] * (n + 1)
    count = 0

    def backtrack(i: int):
        nonlocal count
        if i > n:  # đã xếp hết vị trí
            count += 1
            return
        for ai in range(1, n + 1):
            if not used[ai] and (ai % i == 0 or i % ai == 0):
                used[ai] = True
                backtrack(i + 1)
                used[ai] = False

    backtrack(1)
    return count


if __name__ == "__main__":
    n = int(input().strip())
    print(count_perfect_permutations(n))
