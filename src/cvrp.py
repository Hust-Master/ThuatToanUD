'''
Có một tập K chiếc xe tải giống hệt nhau được sử dụng để giao các thùng pepsi đến n khách hàng đánh số 1, 2,..,n. Biết rằng:
- Mỗi xe đều chỉ trở được tối đa là Q thùng,
- Mỗi khách hàng i muốn mua d[i] thùng.
- Hành trình của mỗi chiếc xe là: xuất phát từ kho hàng (đánh số là 0) để lấy hàng, sau đó đi giao hàng cho một hoặc một số khách hàng trong tập khách hàng, sau đó xe rỗng thì xequay trở về kho trung tâm và kết thúc hành trình.

Chú ý rằng các điều kiện sau phải thỏa mãn:
- Mỗi khách hàng chỉ được giao hàng đúng 1 lần (bởi đúng 1 xe)
- Tổng số thùng pepsi mà mỗi xe sẽ đem giao không thể vượt quá Q.
- Mỗi xe phải giao hàng cho ít nhất 1 khách hàng.

Yêu cầu: Hãy tính R là tổng tất cả các cách giao hàng thỏa mãn yêu cầu của đề bài.
Chú ý: trình tự các khách hàng mà xe giao là quan trọng, do đó, hành trình0->1->2->3->0 là khác với hành trình0->3->2->1->0.

Input
    - Dòng 1 ghi ba số số nguyên dương n, K, Q (2 ≤ n ≤ 10, 1 ≤ K ≤ 5, 1 ≤ Q ≤ 20)
    - Dòng 2 ghi d1, d2,…,dn (1 ≤ di ≤ 10)
Output
    - R mod 10^9 + 7
'''

def solve_vrp():
    MOD = 10**9 + 7
    n, K, Q = map(int, input().split())
    d = [0] + list(map(int, input().split()))
    
    result = [0]
    
    def backtrack(idx, trucks, used):
        """
        idx: khách hàng đang xét (1..n)
        trucks: danh sách các xe, mỗi xe là list các khách hàng đã phân
        used: số xe đã sử dụng
        """
        if idx == n + 1:  # Đã xét hết khách hàng
            if used == K:  # Đúng K xe
                # Tính số "Hoán vị giữa các khách hàng trong cùng một xe" = tích giai thừa size mỗi xe
                ways = 1
                for truck in trucks:
                    if len(truck) > 0:
                        fact = 1
                        for i in range(1, len(truck) + 1):
                            fact *= i
                        ways = (ways * fact) % MOD
                result[0] = (result[0] + ways) % MOD
            return
        
        # Thử phân khách hàng idx cho các xe đã dùng
        for i in range(used):
            total = sum(d[c] for c in trucks[i]) + d[idx]
            if total <= Q:
                trucks[i].append(idx)
                backtrack(idx + 1, trucks, used)
                trucks[i].pop()
        
        # Thử phân khách hàng idx cho xe mới (nếu còn xe)
        if used < K:
            trucks[used].append(idx)
            backtrack(idx + 1, trucks, used + 1)
            trucks[used].pop()
    
    trucks = [[] for _ in range(K)]
    backtrack(1, trucks, 0)
    print(result[0])

solve_vrp()

