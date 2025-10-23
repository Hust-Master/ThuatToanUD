'''
Cho các mệnh giá tiền xu: 1, 5, 10, 25, 100 cent. Yêu cầu: hãy tìm cách trả X cent tiền thừa cho khách sao cho số lượng đồng xu đưa khách là ít nhất.

Input: Giá trị X
Output: Số lượng từng đồng xu 1, 5, 10, 25, 100 cents phải đưa trả khách.

Ví dụ:
Input: 289
Output: 4 0 1 3 2
'''

def doi_tien_tham_lam(X):
    menh_gia = [100, 25, 10, 5, 1]  # Duyệt từ lớn đến bé (tham lam)
    ket_qua = [0] * 5  # Lưu số lượng tương ứng với từng mệnh giá (100, 25, 10, 5, 1)

    for i in range(5):
        coin = menh_gia[i]
        count = X // coin
        ket_qua[i] = count
        X -= count * coin

    # Đảo thứ tự để in theo yêu cầu: 1, 5, 10, 25, 100
    return ket_qua[::-1]

# Nhập và chạy
X = int(input())
kq = doi_tien_tham_lam(X)
print(*kq)
