# Money Exchange

Cho các mệnh giá tiền xu: 1, 5, 10, 25, 100 cent.  
Yêu cầu: hãy tìm cách trả X cent tiền thừa cho khách sao cho số lượng đồng xu đưa khách là ít nhất.

Input: Giá trị X  
Output: Số lượng từng đồng xu 1, 5, 10, 25, 100 cents phải đưa trả khách.

Ví dụ:  
Input: 289  
Output: 4 0 1 3 2

## Greedy (Thuật toán tham lam)
### Complexity
Với n là số mệnh giá
- Time: O(n)
- Space: O(n)

### Ý tưởng
Nguyên tắc tham lam:
- Luôn chọn đồng xu có mệnh giá lớn nhất có thể dùng được tại mỗi bước.
- Giảm phần còn lại (X) và lặp lại với mệnh giá nhỏ hơn.
- Tiếp tục cho đến khi số tiền còn lại bằng 0.

Lý do “tham lam” đúng trong hệ tiền này
- Hệ mệnh giá [1, 5, 10, 25, 100] là hệ "chuẩn Mỹ", có tính chất:
- Mỗi mệnh giá là bội số hoặc kết hợp hợp lý của các mệnh giá nhỏ hơn.