'''
https://hustack.soict.ai/programming-contest/student-view-contest-problem-detail/20251ttudchbs/BINARY_GEN_WITHOUT_CONSECUTIVE_11

Given an integer n, write a program that generates all binary sequences without consecutive 11 in a lexicographic order.
Input
    Line 1: contains an integer n (1 <= n <= 20)
Output
    Write binary sequences in a lexicographic order, each sequence in a line

Example
Input:
    3
Output:
    000
    001
    010
    100
    101

Ý tưởng
    Ta cần sinh tất cả các chuỗi nhị phân độ dài n không chứa "11".
    Cách tiếp cận: Backtracking / Đệ quy xây dựng chuỗi dần dần.

Chiến lược
    - Bắt đầu từ chuỗi rỗng "".
    - Ở mỗi bước, ta có hai lựa chọn:
    - Thêm '0': luôn hợp lệ, vì thêm '0' không bao giờ tạo ra "11".
    - Thêm '1': chỉ hợp lệ nếu ký tự trước đó không phải '1'.
    - Lặp lại cho đến khi chuỗi đạt độ dài n.
    - In ra chuỗi đó.

Vì sao in ra đúng thứ tự từ điển?
    - Ở mỗi nhánh đệ quy, ta luôn thử '0' trước '1'.
    - Do đó, các chuỗi sẽ được sinh ra giống như khi duyệt từ điển
'''

def generate(n):
    def backtrack(seq, last):
        if len(seq) == n:
            print(seq)
            return
        
        # luôn có thể thêm '0'
        backtrack(seq + "0", '0')

        # chỉ thêm '1' nếu ký tự trước không phải '1'
        if last != '1':
            backtrack(seq + "1", '1')

    backtrack("", '0')


if __name__ == "__main__":
    n = int(input())
    generate(n)
