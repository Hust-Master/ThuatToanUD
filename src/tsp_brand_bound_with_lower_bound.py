import sys

INF = int(1e9)
MAXN = 21

n = 0
current_cost = 0
best_cost = INF
visited = [0] * MAXN
x_best = [0] * MAXN
x = [0] * MAXN
c = [[0] * MAXN for _ in range(MAXN)]


def enter():
    """Nhập dữ liệu ma trận chi phí"""
    global n, best_cost
    n = int(input())
    # print("Nhập ma trận chi phí:")

    for i in range(1, n + 1):
        row = list(map(int, input().split()))
        for j in range(1, n + 1):
            c[i][j] = row[j - 1]

    # Thành phố xuất phát
    x[1] = 1
    visited[1] = 1
    best_cost = INF


def update_best_solution():
    global best_cost
    total = current_cost + c[x[n]][1]
    if total < best_cost:
        best_cost = total
        # for i in range(1, n + 1):
        #     x_best[i] = x[i]


def estimate_lower_bound():
    """
    Ước lượng cận dưới (Lower Bound)
    = current_cost + (tổng cạnh nhỏ nhất từ mỗi thành phố chưa thăm) / 2
    """
    lb = current_cost
    est = 0
    for k in range(1, n + 1):
        if not visited[k]:
            min_edge = INF
            for t in range(1, n + 1):
                if k != t:
                    min_edge = min(min_edge, c[k][t])
            est += min_edge
    lb += est / 2
    return lb


def branch_and_bound(i, depth=1):
    global current_cost, best_cost

    lb = estimate_lower_bound()
    # print("  " * (depth - 1) + f"- Tại {x[1:i]}, cost={current_cost}, LB≈{lb}, best={best_cost}")

    # Cắt tỉa nếu cận dưới >= best_cost
    if lb >= best_cost:
        # print("  " * depth + "✂️  Cắt nhánh vì LB >= best")
        return

    # Duyệt tất cả thành phố còn lại
    for j in range(2, n + 1):
        if not visited[j]:
            visited[j] = 1
            x[i] = j
            current_cost += c[x[i - 1]][j]

            if i == n:
                update_best_solution()
            else:
                branch_and_bound(i + 1, depth + 1)

            # Quay lui
            visited[j] = 0
            current_cost -= c[x[i - 1]][j]


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    enter()
    # print("\n--- Bắt đầu Branch & Bound ---")
    branch_and_bound(2)
    # print("\n=== Kết quả tốt nhất ===")
    # print("Hành trình:", [x_best[i] for i in range(1, n + 1)] + [1])
    print(best_cost)
