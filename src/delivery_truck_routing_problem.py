import sys

# === Dữ liệu đầu vào (Input Data) ===
# Dựa trên ví dụ slide 3: N=3, K=2, Q=4
N = 3  # Số lượng điểm giao hàng (đánh số 1 đến N)
K = 2  # Số lượng xe tải (đánh số 1 đến K)
Q = 4  # Tải trọng tối đa của mỗi xe

# d[i]: Lượng hàng yêu cầu tại điểm i (d[0] không dùng, nhưng ta gán = 0)
# d[1]=3, d[2]=2, d[3]=1
d = [0, 3, 2, 1]

# c[i][j]: Khoảng cách từ điểm i đến điểm j
# 0 là kho, 1, 2, 3 là các điểm giao
# (Tạo ma trận khoảng cách giả định)
c = [
    # 0    1    2    3
    [0,   10,   8,   9],  # Kho 0
    [10,   0,   5,   6],  # Điểm 1
    [8,    5,   0,   4],  # Điểm 2
    [9,    6,   4,   0]   # Điểm 3
]

# Cmin: Tìm khoảng cách nhỏ nhất (khác 0) để dùng cho cận dưới
Cmin = sys.float_info.max
for i in range(N + 1):
    for j in range(N + 1):
        if i != j and c[i][j] < Cmin:
            Cmin = c[i][j]

# === Các biến trạng thái của thuật toán ===

# y[k]: Điểm giao hàng *đầu tiên* của xe k (y[k]=0 nếu xe k không chạy)
y = [0] * (K + 1)
# x[i]: Điểm *tiếp theo* của điểm i (x[i]=0 nếu i là điểm cuối về kho)
x = [0] * (N + 1)
# visited[i]: Điểm i đã được thăm hay chưa
visited = [False] * (N + 1)
# load[k]: Tải trọng hiện tại của xe k
load = [0.0] * (K + 1)
# f: Tổng độ dài lộ trình của phương án đang xét
f = 0.0
# f_best: Tổng độ dài của phương án tốt nhất (kỷ lục)
f_best = sys.float_info.max
# segments: Tổng số chặng đã đi của phương án đang xét
segments = 0
# nbR: Số xe thực sự được sử dụng
nbR = 0

# Lưu trữ lời giải tốt nhất
y_best = [0] * (K + 1)
x_best = [0] * (N + 1)


# === Các hàm kiểm tra (Checks) ===

def checkY(v, k):
    """Kiểm tra xem điểm v có thể là điểm *đầu tiên* cho xe k không."""
    # (Dựa theo pseudocode checkY(v,k) slide 7)
    if v == 0:
        return True
    if visited[v]:
        return False
    # Khi gán điểm đầu tiên, load[k] đang = 0
    if d[v] > Q: 
        return False
    return True

def checkX(v, k):
    """Kiểm tra xem điểm v có thể là điểm *tiếp theo* cho xe k không."""
    # (Dựa theo pseudocode checkX(v,k) slide 7)
    if v > 0: # Nếu v là điểm giao hàng
        if visited[v]:
            return False
        if load[k] + d[v] > Q:
            return False
    # if v == 0 (về kho), luôn hợp lệ
    return True

# === Hàm cập nhật kỷ lục ===

def updateBest():
    """Ghi nhận phương án tốt nhất mới."""
    global f_best, x_best, y_best
    if f < f_best:
        f_best = f
        x_best = x[:] # Sao chép mảng
        y_best = y[:] # Sao chép mảng
        # print(f"  -> Tìm thấy kỷ lục mới: {f_best}") # Dùng để debug

# === Các hàm quay lui (Backtracking) ===

def TRY_X(s, k):
    """
    Thử tìm điểm tiếp theo cho xe k, xuất phát từ điểm s.
    (Dựa theo pseudocode TRY_X(s,k) ở slide 7)
    """
    global f, segments, load, visited

    # (Phần logic `if s == 0` từ pseudocode được xử lý trong hàm TRY_Y
    # bằng cách chỉ gọi TRY_X cho các xe có y[k] > 0)
    
    # Duyệt tất cả các điểm v có thể là điểm tiếp theo (0=kho, 1..N)
    for v in range(N + 1):
        if checkX(v, k):
            # Thử gán s -> v
            x[s] = v
            f += c[s][v]
            segments += 1
            
            if v > 0: # Nếu đi đến điểm giao hàng v
                visited[v] = True
                load[k] += d[v]
                
                # Nhánh và Cận (Branch and Bound)
                bound = f + (N + nbR - segments) * Cmin
                if bound < f_best:
                    TRY_X(v, k) # Đệ quy: tìm điểm tiếp theo từ v
                
                # Quay lui (Backtrack)
                load[k] -= d[v]
                visited[v] = False
            
            else: # Nếu đi về kho (v == 0)
                if k == K: # Nếu đây là xe cuối cùng
                    # Kiểm tra xem đã thăm hết N điểm và đủ số chặng
                    # (N chặng khách-hàng + nbR chặng kho-khách)
                    if segments == N + nbR:
                        updateBest()
                else:
                    # Nhánh và Cận (Branch and Bound)
                    bound = f + (N + nbR - segments) * Cmin
                    if bound < f_best:
                        # Tìm xe tiếp theo (k+1) thực sự được dùng (y[k+1] > 0)
                        next_k = k + 1
                        while next_k <= K and y[next_k] == 0:
                            next_k += 1
                        
                        if next_k <= K:
                            # Bắt đầu duyệt lộ trình cho xe next_k
                            TRY_X(y[next_k], next_k)
                            
            # Quay lui (Backtrack)
            segments -= 1
            f -= c[s][v]
            x[s] = 0 # (Không bắt buộc, nhưng rõ ràng)


def TRY_Y(k):
    """
    Thử gán điểm giao hàng *đầu tiên* (y[k]) cho xe k.
    (Dựa theo pseudocode TRY_Y(k) ở slide 7 và ràng buộc slide 3)
    """
    global f, segments, nbR, load, visited

    # Ràng buộc: y[k] >= y[k-1]
    # và nếu y[k-1] > 0 thì y[k] > y[k-1]
    start_v = 0
    if k > 1 and y[k-1] > 0:
        start_v = y[k-1] + 1
    elif k > 1: # y[k-1] == 0
        start_v = 0

    # Duyệt các giá trị có thể cho y[k] (từ start_v đến N)
    # v=0 nghĩa là xe k không được dùng
    for v in range(start_v, N + 1):
        if checkY(v, k): # checkY đã bao gồm check v=0
            
            y[k] = v
            
            if v > 0: # Nếu xe k được dùng (y[k] > 0)
                visited[v] = True
                load[k] = d[v] # Gán tải trọng ban đầu
                f += c[0][v]   # Cộng chi phí từ kho (0) đến v
                
            if k == K: # Đã gán xong y[k] cho xe cuối cùng
                # Đếm số xe thực sự dùng
                nbR = 0
                for i in range(1, K + 1):
                    if y[i] > 0:
                        nbR += 1
                
                # segments ban đầu bằng số xe được dùng
                segments = nbR
                
                if N == 0: # Trường hợp đặc biệt không có điểm giao
                    updateBest()
                else:
                    # Tìm xe đầu tiên được dùng để bắt đầu TRY_X
                    first_k = -1
                    for i in range(1, K + 1):
                        if y[i] > 0:
                            first_k = i
                            break
                    
                    if first_k != -1:
                        TRY_X(y[first_k], first_k)
            else:
                TRY_Y(k + 1) # Đệ quy: gán y[k+1]
                
            # Quay lui (Backtrack)
            if v > 0:
                f -= c[0][v]
                load[k] = 0 # Reset tải trọng
                visited[v] = False
                y[k] = 0


# === Hàm giải và in kết quả ===

def print_solution():
    """In lộ trình chi tiết của phương án tốt nhất."""
    if f_best == sys.float_info.max:
        print("Không tìm thấy phương án hợp lệ.")
        return

    print(f"Tổng chi phí nhỏ nhất: {f_best}")
    print("Lộ trình chi tiết:")
    
    total_load_check = 0
    
    for k in range(1, K + 1):
        if y_best[k] > 0: # Nếu xe k được sử dụng
            route = [0, y_best[k]]
            current_point = y_best[k]
            truck_load = d[y_best[k]]
            
            while x_best[current_point] != 0:
                current_point = x_best[current_point]
                route.append(current_point)
                truck_load += d[current_point]
                
            route.append(0) # Quay về kho
            total_load_check += truck_load
            
            route_str = " -> ".join(map(str, route))
            print(f"  Xe {k}: {route_str} (Tải trọng: {truck_load})")
            
    print(f"Tổng hàng đã giao: {total_load_check}")


def solve():
    """Hàm chính để bắt đầu giải bài toán."""
    global f, f_best, segments, nbR, visited, load, y, x, d
    
    # Khởi tạo các biến toàn cục
    f = 0.0
    f_best = sys.float_info.max
    segments = 0
    nbR = 0
    visited = [False] * (N + 1)
    load = [0.0] * (K + 1)
    y = [0] * (K + 1)
    x = [0] * (N + 1)
    
    # Đảm bảo d[0] = 0 để logic tính load[k] += d[v] hoạt động khi v=0
    if len(d) <= N: # Nếu mảng d chỉ có N phần tử
        d = [0] + d[1:]
    else:
        d[0] = 0
    
    # Bắt đầu quay lui từ xe 1
    TRY_Y(1)
    
    # In kết quả
    print_solution()

# === Chạy thuật toán ===
print("Bắt đầu giải bài toán lộ trình xe tải (VRP)...")
print(f"Input: N={N}, K={K}, Q={Q}")
print(f"Demands: {d[1:]}")
print("---")
solve()