# Disjoint Segment
[Chapter 3. Disjoint Segment](https://hustack.soict.ai/programming-contest/contest-problem-submission-detail/0199f6c4-d0db-7b08-9b19-7201922d9064)

Given a set of segments X = {(a1, b1), . . . , (an, bn)} in which ai < bi are coordinates of the segment i on a line, i = 1, …, n.  
Find a subset of X having largest cardinality in which no two segments of the subset intersect

Input  
- Line 1: contains a positive integer n (1 <= n <= 100000)
- Line i+1 (i= 1,...,n): contains ai and bi (0 <= ai <= bi <= 1000000)

Output
- Number of segments in the solution found.

Example  
Input
```
6
0 10
3 7
6 14
9 11
12 15
17 19  
```

Output: 
```
4
```


## 🧩 Tóm tắt
Cho n đoạn thẳng trên trục số, mỗi đoạn là (ai, bi) với ai < bi.  
Hãy chọn nhiều đoạn nhất có thể, sao cho không có hai đoạn nào giao nhau (tức là các đoạn rời nhau hoàn toàn).  
→ Kết quả cần tìm là số lượng đoạn chọn được lớn nhất.


Đây là bài toán chọn hoạt động (Activity Selection Problem) — một ví dụ kinh điển của thuật toán tham lam.

Chiến lược chính:
👉 Chọn đoạn kết thúc sớm nhất còn khả thi.


## 💡 Ý tưởng thuật toán (Greedy)
Ta cần chọn nhiều đoạn nhất mà không bị chồng nhau.  
Một cách “tham lam” hợp lý là: **Luôn chọn đoạn kết thúc sớm nhất có thể.**

Lý do:
- Nếu một đoạn kết thúc sớm, ta “mở ra” nhiều cơ hội hơn để chọn các đoạn tiếp theo phía sau nó.
- Nếu ta chọn một đoạn kết thúc muộn, có thể nó sẽ chặn mất nhiều đoạn ngắn và rời nhau khác.


## 📈 Độ phức tạp
- Time: O(n log n)
- Space: O(n)

## ⚙️ Các bước thực hiện
1. Sắp xếp các đoạn theo tọa độ kết thúc (b) tăng dần.
2. Duyệt lần lượt các đoạn đã sắp xếp:
    - Biến end lưu vị trí kết thúc của đoạn cuối cùng đã chọn.
    - Nếu đoạn hiện tại bắt đầu sau khi đoạn trước kết thúc (a > end), thì chọn đoạn này.

## 🧠 Minh họa ví dụ
Input
```
6
0 10
3 7
6 14
9 11
12 15
17 19
```

### Bước 1️⃣ – Sắp xếp theo b:
| Đoạn | (a, b)   |
| ---- | -------- |
| 3    | (3, 7)   |
| 0    | (0, 10)  |
| 9    | (9, 11)  |
| 12   | (12, 15) |
| 6    | (6, 14)  |
| 17   | (17, 19) |

→ Sau khi sắp xếp theo b tăng dần:
`(3,7), (0,10), (9,11), (6,14), (12,15), (17,19)`

### Bước 2️⃣ – Duyệt chọn:
| Đoạn    | a  | b  | Có chọn không? | end (sau khi chọn) |
| ------- | -- | -- | -------------- | ------------------ |
| (3,7)   | 3  | 7  | ✅ (3 > -1)     | 7                  |
| (0,10)  | 0  | 10 | ❌ (0 ≤ 7)      | 7                  |
| (9,11)  | 9  | 11 | ✅ (9 > 7)      | 11                 |
| (6,14)  | 6  | 14 | ❌ (6 ≤ 11)     | 11                 |
| (12,15) | 12 | 15 | ✅ (12 > 11)    | 15                 |
| (17,19) | 17 | 19 | ✅ (17 > 15)    | 19                 |

✅ Các đoạn được chọn:  
→ (3,7), (9,11), (12,15), (17,19)  
→ Tổng cộng: 4 đoạn

## Tham khảo
[ChatGPT](https://chatgpt.com/c/68f9d54f-6538-8321-86b8-cf6d0adf935f)