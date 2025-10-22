"""
There are n passengers 1, 2, …, n. The passenger i want to travel from point i to point i + n (i = 1,2,…,n).
There is a bus located at point 0 and has k places for transporting the passengers (it means at any time, there are at most k passengers on the bus).
You are given the distance matrix c in which c(i,j) is the traveling distance from point i to point j (i, j = 0,1,…, 2n).
Compute the shortest route for the bus, serving n passengers and coming back to point 0.

Input
    Line 1 contains n and k (1≤n≤11,1≤k≤10)
    Line i+1 (i=1,2,…,2n+1) contains the (i−1)th
    Line of the matrix c (rows and columns are indexed from 0,1,2,..,2n).
Output
    Unique line contains the length of the shortest route.

Example
Input
    3  2
    0  8  5  1  10  5  9
    9  0  5  6  6  2  8
    2  2  0  3  8  7  2
    5  3  4  0  3  2  7
    9  6  8  7  0  9  10
    3  8  10  6  5  0  2
    3  4  4  5  2  2  0
Output
    25
"""

import sys

# Tăng giới hạn đệ quy của Python, vì backtracking có thể cần độ sâu lớn
# 2*n có thể lên tới 22, cộng thêm các lời gọi hàm
sys.setrecursionlimit(3000)

# --- Khai báo các biến toàn cục ---
# Chúng ta sẽ sử dụng biến toàn cục để mô phỏng hành vi của code C++
n, K = 0, 0  # n: số khách, K: sức chứa
c = []  # Ma trận chi phí
X = []  # Mảng lưu lộ trình hiện tại (1-indexed)
visited = []  # Mảng đánh dấu điểm đã thăm (1-indexed)
load = 0  # Tải trọng hiện tại
f = 0  # Chi phí hiện tại (từ X[0] đến X[k])
f_best = float("inf")  # Chi phí tốt nhất (vô cùng lớn ban đầu)
Cmin = float("inf")  # Cmin = giá trị nhỏ nhất (khác 0) trong toàn bộ ma trận chi phí c


def isValid(v):
    """
    Kiểm tra xem việc gán điểm v cho bước hiện tại có hợp lệ không.
    Hàm này chỉ *đọc* các biến toàn cục, không cần khai báo 'global'.
    """

    # 1. Điểm v đã được thăm
    if visited[v]:
        return False

    # 2. Nếu v là điểm trả khách (v > n)
    if v > n:
        # Phải thăm điểm đón (v-n) trước đó
        if not visited[v - n]:
            return False
    # 3. Nếu v là điểm đón khách (v <= n)
    else:
        # Phải kiểm tra tải trọng
        if load + 1 > K:
            return False

    # Nếu qua được tất cả kiểm tra
    return True


#  Cập nhật kết quả tốt nhất (f_best) nếu tìm thấy lộ trình tốt hơn.
def updateBest():
    global f_best

    # Thêm chi phí từ điểm cuối cùng X[2*n] quay về 0
    # f, c, X được *đọc* từ global scope
    current_cost = f + c[X[2 * n]][0]

    if current_cost < f_best:
        f_best = current_cost
        # print(X)
        # print(f_best)


def Try(k):
    """
    Hàm đệ quy quay lui (backtracking) để thử các lộ trình.
    k: Bước hiện tại (xây dựng điểm X[k]).
    """
    # Khai báo các biến global sẽ bị *gán giá trị* (thay đổi)
    global f, load, visited, X

    # Thử tất cả các điểm v (từ 1 đến 2n) cho vị trí k
    # range(1, 2 * n + 1) sẽ duyệt từ 1 đến 2*n
    for v in range(1, 2 * n + 1):
        if isValid(v):
            # 1. Gán X[k] = v
            X[k] = v

            # 2. Cập nhật các biến trạng thái
            f += c[X[k - 1]][v]  # Cộng chi phí di chuyển
            visited[v] = True
            if v <= n:
                load += 1  # Đón khách
            else:
                load -= 1  # Trả khách

            # 3. Kiểm tra điều kiện dừng (Base Case) HOẶC đệ quy
            if k == 2 * n:
                # Đã đi hết 2n điểm, cập nhật kết quả
                updateBest()
            else:
                # 4. Nhánh và cận (Branch and Bound)
                # (2*n - k) chặng còn lại + 1 chặng về 0
                remaining_cost_estimate = Cmin * (2 * n - k + 1)

                # Nếu chi phí hiện tại + ước tính < f_best thì mới đi tiếp
                if f + remaining_cost_estimate < f_best:
                    Try(k + 1)

            # 5. --- Quay lui (Backtrack) ---
            # Hoàn trả lại trạng thái *trước khi* thử v
            if v <= n:
                load -= 1
            else:
                load += 1
            visited[v] = False
            f -= c[X[k - 1]][v]


def main():
    global n, K, c, X, visited, f_best, Cmin, f, load

    n, K = map(int, input().split())

    for i in range(2 * n + 1):
        row = list(map(int, input().split()))
        c.append(row)

        for j in range(2 * n + 1):
            if i != j and row[j] < Cmin:
                Cmin = row[j]

    # 3. Khởi tạo các mảng/biến trạng thái
    X = [0] * (2 * n + 1)
    visited = [False] * (2 * n + 1)

    X[0] = 0                # Bắt đầu từ điểm 0
    f = 0                   # Chi phí ban đầu
    f_best = float("inf")   # Kết quả tốt nhất ban đầu
    load = 0                # Tải trọng ban đầu

    Try(1)                  # Bắt đầu thử từ điểm đầu tiên của lộ trình (X[1])
    print(f_best)


if __name__ == "__main__":
    main()
