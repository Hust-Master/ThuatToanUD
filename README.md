# Thuật toán ứng dụng

## Installation
- Vscode
- Python 3.13.2

## 🧪 Test
1. Mở Command Palette: Nhấn Ctrl + Shift + P (hoặc Cmd + Shift + P trên macOS).
2. Chọn "Python: Configure Tests": Gõ "Python: Configure Tests" và chọn nó.
3. Chọn Framework Test: 
   - **pytest**: Thường được khuyên dùng cho các dự án lớn và có nhiều tính năng hơn.
   - **unittest** (hoặc unittest-ng): Framework tích hợp sẵn trong thư viện chuẩn của Python.
4. Chọn pytest hoặc unittest tùy theo dự án.
5. Chọn Thư mục Gốc (Root Directory): Thường là thư mục gốc của workspace (.).
6. Chọn Mẫu Tên File Test (Test File Pattern):
   - Đối với pytest, thường là test_*.py hoặc *_test.py.
   - Đối với unittest, thường là test_*.py.

VS Code sẽ tự động tạo hoặc cập nhật file cấu hình (thường là trong thư mục .vscode/settings.json) để lưu các thiết lập này.


## 🔹 2 Pointing technique (Kỹ thuật hai con trỏ)
- [Chapter 1. 2 pointing technique - sum pair of numbers on sorted sequence](https://hustack.soict.ai/programming-contest/student-view-contest-problem-detail/20251ttudchbs/2pointing1DarrayAsceding)
- [Chapter 1. 2 pointing technique - sum pair of numbers on non-sorted sequence](https://hustack.soict.ai/programming-contest/student-view-contest-problem-detail/20251ttudchbs/2pointing1DarraypairSumQ): Dùng kỹ thuật băm (hash)
- [Chapter 1. 2 pointing technique - longest subsequence](https://hustack.soict.ai/programming-contest/student-view-contest-problem-detail/20251ttudchbs/LONGEST_BOUNDED_MAXSEQ)


## 🔹 Range minium query 
Pending

## 🔹 Segment Tree (Cây phân đoạn)
- [Chapter 1 - Segment Tree Simulation - query Max](https://hustack.soict.ai/programming-contest/student-view-contest-problem-detail/20251ttudchbs/SEGMENT_TREE_SIM): tìm giá trị nhỏ nhất trong một đoạn bất kỳ


## 🔹 Backtracking (Thuật toán quay lui) 
Dùng cho các bài toán liệt kê tổ hợp và tối ưu tổ hợp
- [Chapter 2. Binary sequence generation with condition](https://hustack.soict.ai/programming-contest/student-view-contest-problem-detail/20251ttudchbs/BINARY_GEN_WITHOUT_CONSECUTIVE_11): liệt kê tổ hợp các chuỗi nhị phân
- [Chapter 2. Permutation generation](https://hustack.soict.ai/programming-contest/student-view-contest-problem-detail/20251ttudchbs/PERMUTATION_GEN): liệt kê tất cả các hoán vị theo thứ tự. [-> Chi tiết](./docs/permutation_generation.md)
- [Chapter 2. Permutation with condition](https://hustack.soict.ai/programming-contest/student-view-contest-problem-detail/20251ttudchbs/Midterm_20222-DSAL_1): liệt kê tất cả các hoán vị theo thứ tự, có điều kiện lọc đầu ra [-> Chi tiết](./docs/permutation_generation_with_condition.md) 

## 🔹 Brand and bound (Kỹ thuật nhánh và cận)
Dùng cho các bài toán tối ưu tổ hợp
- [Chapter 2. TSP](https://hustack.soict.ai/programming-contest/student-view-contest-problem-detail/20251ttudchbs/TSP): Bài toán người du lịch [-> Chi tiết](./docs/tsp.md)
- [Chapter 2. CBUS](https://hustack.soict.ai/programming-contest/student-view-contest-problem-detail/20251ttudchbs/CBUS): Bài toán "The bus routing problem" [-> Chi tiết](./src/cbus_brand_bound.py)
- [Chapter 2. Count solutions CVRP](https://hustack.soict.ai/programming-contest/student-view-contest-problem-detail/20251ttudchbs/countcvrp): Delivery truck routing problem


## 🔹 Greedy (Thuật toán tham lam)
Dùng cho các bài toán cần tìm lời giải tối ưu. 
Mỗi lời giải có nhiều thành phần và mỗi thành phần bị giới hạn

- [Chapter 3. Money exchange](https://hustack.soict.ai/programming-contest/student-view-contest-problem-detail/20251ttudchbs/moneyexchange): Bài toán đổi tiền 
- [Chapter 3. Disjoint Segment](https://hustack.soict.ai/programming-contest/student-view-contest-problem-detail/20251ttudchbs/DISJOINT_SEGMENT): Bài toán các đoạn thẳng không giao nhau


## Other
- [Học nhanh python](./docs/python.md)