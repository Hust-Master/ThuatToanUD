# Vehicle Routing Problem

Có một tập $K$ chiếc xe tải giống hệt nhau được sử dụng để giao các thùng pepsi đến $n$ khách hàng đánh số $1, 2,..,n$. Biết rằng:
- Mỗi xe đều chỉ trở được tối đa là $Q$ thùng,
- Mỗi khách hàng i muốn mua $d[i]$ thùng.
- Hành trình của mỗi chiếc xe là: xuất phát từ kho hàng (đánh số là 0) để lấy hàng, sau đó đi giao hàng cho một hoặc một số khách hàng trong tập khách hàng, sau đó xe rỗng thì xe quay trở về kho trung tâm và kết thúc hành trình.

Chú ý rằng các điều kiện sau phải thỏa mãn:
- Mỗi khách hàng chỉ được giao hàng đúng $1$ lần (bởi đúng 1 xe)
- Tổng số thùng pepsi mà mỗi xe sẽ đem giao không thể vượt quá $Q$.
- Mỗi xe phải giao hàng cho ít nhất $1$ khách hàng.  

Yêu cầu: Hãy tính $R$ là tổng tất cả các cách giao hàng thỏa mãn yêu cầu của đề bài.  
Chú ý: trình tự các khách hàng mà xe giao là quan trọng, do đó, hành trình $0->1->2->3->0$ là khác với hành trình $0->3->2->1->0$.

Input
- Dòng 1 ghi ba số số nguyên dương $n, K, Q$. And $(2 ≤ n ≤ 10, 1 ≤ K ≤ 5, 1 ≤ Q ≤ 20)$
- Dòng 2 ghi $d1, d2,…,dn$. And $(1 ≤ di ≤ 10)$

Output
- R mod $10^9 + 7$

Example  
| Input | Output|
|:-----| :-----|
|3 2 3 <br> 1 1 1 | 6 |
|4 2 3 <br> 1 1 1 1 | 36 |
| 5 3 5 <br> 1 2 1 1 1 | 120 |
| 8 4 8 <br> 1 2 1 2 1 1 2 1 | 58800 |
|7 3 10 <br> 2 2 3 1 1 1 1 | 12600 |



## 🎯 1. Mục tiêu bài toán
Bài toán là Vehicle Routing Problem (VRP) rút gọn:
- Có n khách hàng, K xe tải, mỗi xe có giới hạn tải trọng Q, và mỗi khách hàng i có nhu cầu d[i].
- Hãy đếm số cách phân phối các khách hàng cho đúng K xe, sao cho tổng tải mỗi xe ≤ Q.
- Thứ tự khách hàng trong cùng một xe có hoán vị riêng (nên phải nhân thêm len(truck)! cho mỗi xe khi tính kết quả).

## 2. Backtracking
Hàm `backtrack(idx, trucks, used)` xử lý khách hàng thứ `idx` (1..n) với:

* `trucks`: danh sách `K` list (mỗi phần tử là danh sách khách của một xe).
* `used`: số xe đã mở (chưa chắc bằng `K`, nhiều nhất là `K`).

Tại từng `idx` ta có hai loại lựa chọn:

1. **Cho khách `idx` vào 1 trong các xe đã mở** (i = 0..used-1) — nếu không vượt `Q`.
2. **Mở xe mới** (nếu `used < K`) và đặt `idx` vào xe đó.

Sau khi `idx` vượt `n` (tức đã xét hết khách), nếu `used == K` thì tính số cách hoán vị do sắp xếp trong từng xe và cộng vào kết quả.

Kỹ thuật `append -> recurse -> pop` là chuẩn của backtracking: thay đổi trạng thái, đi sâu, rồi hoàn nguyên.

---
## 3. Giải thích chi tiết đoạn code trung tâm

Đoạn code cần giải thích:

```python
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
```

**Giải thích từng phần:**

* `for i in range(used)`:

  * Duyệt từng xe đã được mở (chỉ số 0..used-1). Với mỗi xe, thử gán khách `idx` vào đó.

* `total = sum(d[c] for c in trucks[i]) + d[idx]`:

  * Tính tổng tải nếu thêm `idx` vào xe `i`.
  * *Lưu ý hiệu năng*: phép `sum(...)` tính lại từ đầu mỗi lần; với nhiều trạng thái/xe lớn, đây là điểm có thể tối ưu.

* `if total <= Q:`: nếu thoả ràng buộc tải thì tiếp tục.

* `trucks[i].append(idx)` -> `backtrack(...)` -> `trucks[i].pop()`:

  * Thêm khách vào, gọi đệ quy cho khách tiếp theo, rồi hoàn nguyên trạng thái (backtrack).

* `if used < K:` phần mở xe mới:

  * Nếu vẫn còn xe trống (chỉ số `used` chưa được dùng), đặt `idx` vào `trucks[used]` và gọi đệ quy với `used + 1`.
  * Sau khi quay lên, `pop()` để hoàn nguyên.

**Ý nghĩa cao cấp:** phần `for` xử lý mọi khả năng gán vào xe đã mở; phần `if used < K` xử lý việc bắt đầu một xe mới ở vị trí tiếp theo.

---

## 4. Vấn đề quan trọng: Xe được *phân biệt* (có tên)

* `trucks` là một danh sách có thứ tự: `trucks[0]`, `trucks[1]`, ...
* Do đó thuật toán **coi các xe là khác nhau** (Xe0 khác Xe1). Kết quả: cùng một phân phối "về mặt tập khách" nhưng chỉ khác cách gán chỉ số xe sẽ được sinh nhiều lần (đếm trùng).

**Ví dụ ý tưởng:** `XeA:[1,2], XeB:[3]` và `XeA:[3], XeB:[1,2]` được code sinh ra từ hai nhánh khác nhau → bị đếm 2 lần nếu ta coi xe là vô danh.

---

## 5. Ví dụ minh họa chi tiết (ASCII) — `n=3, K=2, Q=10, d=[0,4,5,6]`

Giả sử `d[1]=4, d[2]=5, d[3]=6`. Q = 10 đủ để một vài kết hợp.

Bắt đầu: `idx=1`, `trucks=[[], []]`, `used=0`.

```
idx=1
 └── mở Xe0: trucks = [[1], []], used=1
      ├── idx=2
      │    ├── (i=0) thử thêm vào Xe0: total = 4 + 5 = 9 (<=10)
      │    │    └── trucks = [[1,2], []], used=1
      │    │         └── idx=3
      │    │              ├── thử thêm vào Xe0: total = 9 + 6 = 15 (>10) ❌
      │    │              └── mở Xe1: trucks = [[1,2], [3]], used=2  ✅ 
      │    │
      │    └── (mở Xe1) trucks = [[1], [2]], used=2
      │         └── idx=3
      │              ├── thử thêm vào Xe0: total = 4 + 6 = 10 ✅ → trucks = [[1,3],[2]]
      │              └── thử thêm vào Xe1: total = 5 + 6 = 11 ❌
      │
      └── (hết idx=2 nhánh)

Kết quả hợp lệ thu được (hai leaf nodes):
1) [[1,2], [3]]
2) [[1,3], [2]]

Mỗi cấu hình sẽ tính `ways` = product(len(truck)!) →
- [[1,2],[3]] -> 2! * 1! = 2
- [[1,3],[2]] -> 2! * 1! = 2
Tổng = 4
```

**Quan sát:** nếu coi xe vô danh, hai cấu hình tương đương `[[1,2],[3]]` và `[[1,3],[2]]` có thể trùng khi đổi tên xe — nhưng do thứ tự trong `trucks` khác nhau, code sinh cả hai.

---

## 6. Ví dụ nhỏ nhất để thấy rõ *đếm trùng* (n=2, K=2, Q lớn)

* `d=[0,1,1]`, Q đủ lớn.

Trình duyệt:

```
idx=1 -> mở Xe0:[1]
  └──idx=2 
        │── thêm vào Xe0           => [[1,2], []]
        └── mở và thêm vào Xe1     => [[1], [2]]
```

Nếu có cách khác (trong một thuật toán khác) mở Xe1 trước rồi đặt 1 vào Xe1, ta sẽ sinh [[2],[1]] v.v. Các phân phối đôi khi trùng nhau về tập khách nhưng khác vị trí trong `trucks`.

---

## 7. Cách sửa (muốn coi xe *vô danh*)

Có 3 cách phổ biến:

### Cách A — Buộc mở xe mới chỉ khi các xe trước đã có khách

Chỉ cho phép *mở* `trucks[used]` khi mọi `trucks[0..used-1]` đều không rỗng. Điều này đảm bảo xe được mở theo thứ tự và không tạo ra hoán vị khác do hoán đổi chỉ số xe.

```python
if used < K and all(len(trucks[j]) > 0 for j in range(used)):
    trucks[used].append(idx)
    backtrack(idx+1, trucks, used+1)
    trucks[used].pop()
```

Ưu: dễ hiểu, hiệu quả tốt, không sinh trùng. Nhược: giả sử bạn muốn phép để có xe rỗng giữa các xe (hiếm gặp) thì không phù hợp.

### Cách B — Chuẩn hoá phân phối trước khi cộng kết quả (deduplicate)

Khi tới leaf, chuẩn hoá kiểu `norm = sorted([sorted(t) for t in trucks if t])` rồi dùng `set()` để tránh đếm trùng.

Nhược: tốn bộ nhớ/chi phí so sánh.

### Cách C — Chia cho hoán vị của xe

Nếu bạn biết **mọi** cấu hình luôn dùng đủ `K` xe và các xe thực sự vô danh, có thể chia tổng kết quả cho `K!`. Nhưng hay dễ sai nếu có cấu hình dùng < K xe.

---

## 8. Tối ưu hoá hiệu năng (thực tiễn)

1. **Tránh gọi `sum(...)` mỗi lần**: duy trì mảng `loads = [0]*K` lưu tải hiện tại của từng xe; cập nhật loads khi `append`/`pop`.

```python
loads[i] += d[idx]
backtrack(...)
loads[i] -= d[idx]
```

2. **Duy trì kích thước mỗi xe** (`sizes[i]`) để tính giai thừa `len(truck)!` nhanh hơn hoặc gộp tính khi cần.

3. **Pruning bổ sung**: nếu tổng còn lại của các khách chưa phân > (K-used) * Q thì có thể prune; tuỳ bài toán mà thêm bound.

4. **Sắp xếp khách theo decreasing d[i]** trước khi backtracking thường giúp prune sớm hơn.

---

## 9. Phiên bản cải tiến (mã mẫu, xử lý loads & tránh mở xe trống giữa chừng)

```python
MOD = 10**9 + 7

def solve_vrp():
    n, K, Q = map(int, input().split())
    d = [0] + list(map(int, input().split()))

    result = [0]
    trucks = [[] for _ in range(K)]
    loads = [0]*K

    def backtrack(idx, used):
        if idx == n+1:
            if used == K:
                ways = 1
                for t in trucks:
                    if len(t) > 0:
                        fact = 1
                        for i in range(1, len(t)+1):
                            fact *= i
                        ways = (ways * fact) % MOD
                result[0] = (result[0] + ways) % MOD
            return

        # thử gán vào xe đã mở
        for i in range(used):
            if loads[i] + d[idx] <= Q:
                trucks[i].append(idx)
                loads[i] += d[idx]
                backtrack(idx+1, used)
                loads[i] -= d[idx]
                trucks[i].pop()

        # thử mở xe mới (nhưng chỉ khi các xe trước không rỗng)
        if used < K and all(len(trucks[j]) > 0 for j in range(used)):
            trucks[used].append(idx)
            loads[used] += d[idx]
            backtrack(idx+1, used+1)
            loads[used] -= d[idx]
            trucks[used].pop()

    backtrack(1, 0)
    print(result[0])
```

---

## 10. Kết luận ngắn gọn

* Đoạn `for i in range(used)` + `if used < K` tạo ra mọi khả năng phân phối theo thứ tự xe (xe được phân biệt).
* Nếu muốn coi xe **vô danh**, phải ngăn sinh trùng (ví dụ: chỉ mở xe mới khi các xe trước đã có khách).
* Để tối ưu, duy trì `loads` thay vì `sum(...)` mỗi lần và cân nhắc pruning.

---

## 11. Tài liệu tham khảo & ghi chú

* Đây là dạng bài toán tổ hợp + backtracking mẫu; tuỳ kích thước n, K bài toán có thể rất nặng.
* Các heuristics (sắp xếp giảm d[i], lower/upper bounds) quan trọng để mở rộng bài toán lớn.
* [ChatGPT](https://chatgpt.com/c/68f9854a-a8dc-8321-be70-558eca14a8fa)