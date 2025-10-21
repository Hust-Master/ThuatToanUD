# Học nhanh python


## 🔹 Biến và kiểu dữ liệu
```python
x = 10        # int
y = 3.14      # float
name = "Minh" # string
is_ok = True  # bool
```

## 🔹 Cấu trúc điều khiển
### If
```python
x = 5
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")
```

### For
```python
for i in range(5):       # 0..4
    print(i)

for ch in "hello":       # duyệt chuỗi
    print(ch)

arr = [10, 20, 30]
for idx, val in enumerate(arr):
    print(idx, val)
```

### While
```python
i = 0
while i < 5:
    print(i)
    i += 1
```

## 🔹 Hàm
```python
def add(a, b):
    return a + b
print(add(3, 4))
```

## 🔹 List (tương tự mảng / List<T> trong C#)
```python
arr = [1, 2, 3]

arr.append(4)        # thêm cuối
arr.insert(1, 99)    # chèn tại vị trí
arr.remove(2)        # xóa phần tử đầu tiên có giá trị = 2
print(arr[0])        # truy cập
print(arr[-1])       # truy cập từ cuối
print(len(arr))      # độ dài
print(arr[1:3])      # slicing [start:end)
```

TODO: Còn pop, push ???

## 🔹 Dict - Tương tự Dictionary<TKey, TValue>
```python
d = {"a": 1, "b": 2}

d["c"] = 3
print(d["a"])       # 1
print(d.get("x", 0)) # tránh lỗi key not found
for k, v in d.items():
    print(k, v)
```

## 🔹 Set - Tập hợp không trùng lặp (giống HashSet<T> trong C#).
```python
s = {1, 2, 3}
s.add(2)      # không thêm trùng
s.add(4)
print(s)      # {1,2,3,4}
print(3 in s) # kiểm tra tồn tại
```

## 🔹 toán tử tập hợp
```python
a = {1,2,3}
b = {3,4,5}
print(a | b)   # union {1,2,3,4,5}
print(a & b)   # intersection {3}
print(a - b)   # difference {1,2}
```

## 🔹 Tuple - Tương tự ValueTuple trong C#, immutable (không sửa được).
```python
t = (1, "hello", True)
print(t[0])     # 1
a, b, c = t     # unpacking
print(b)        # hello
```


## 🔹 heapq (priority queue - min heap)
👉 Python có sẵn min-heap.
👉 Nếu muốn max-heap → dùng giá trị âm: heapq.heappush(h, -x).
```python
import heapq

h = []
heapq.heappush(h, 3)
heapq.heappush(h, 1)
heapq.heappush(h, 5)

print(heapq.heappop(h))  # 1 (nhỏ nhất)
print(h)                 # còn lại [3,5]
```

## 🔹 heapify nhanh từ list
```python
arr = [7,2,9,1]
heapq.heapify(arr)
print(heapq.heappop(arr)) # 1
```

## 🔹 Collections - Nhiều cấu trúc hữu ích:
```python
from collections import deque, Counter, defaultdict

# deque = queue 2 đầu (giống LinkedList)
dq = deque([1,2,3])
dq.appendleft(0)
dq.append(4)
print(dq.popleft())   # 0
print(dq.pop())       # 4

# Counter = đếm số lần xuất hiện
cnt = Counter("banana")
print(cnt)        # Counter({'a':3, 'n':2, 'b':1})

# defaultdict = dict có giá trị mặc định
dd = defaultdict(int)   # mặc định = 0
dd["a"] += 1
print(dd["a"], dd["b"]) # 1 0
```

## 🔹 Queue
Có thể dùng deque hoặc queue.Queue.
```python
from collections import deque
q = deque()
q.append(1)
q.append(2)
print(q.popleft())  # 1
```

TODO: Cần thêm ví dụ

## 🔹 Hàm bậc cao: sort, max, filter, map, lambda

```python
#sort
arr = [3,1,4,2]
arr.sort()
print(arr)      # [1,2,3,4]

#max
x = max(4, 5)
print(x)

# lambda = function ngắn
square = lambda x: x*x
print(square(5))   # 25

# map: áp dụng hàm cho từng phần tử
arr = [1,2,3,4]
print(list(map(lambda x: x*2, arr)))  # [2,4,6,8]

# filter: lọc theo điều kiện
print(list(filter(lambda x: x%2==0, arr)))  # [2,4]

# kết hợp
res = list(map(lambda x: x*x, filter(lambda x: x%2==0, arr)))
print(res)  # [4,16]
```

## 🔹 Ép kiểu, Input
```python
x = int(input("Nhập số nguyên bất kỳ: "))
print("Số vừa nhập là:", x)

a, b = map(int, input("Nhập hai số nguyên: ").split())
print("Hai số nguyên vừa nhập:", a, b)

arr = list(map(int, input("Nhập một mảng số nguyên: ").split()))
print("Mảng vừa nhập là:", arr)
```

## Other
```python
# Vô cực âm
float('-inf')

# Vô cực dương
float('int')

# Một số trường hợp khác dùng -10**9 hoặc 10**9 thay cho vô cực âm hoặc vô cực dương
```

TODO: bitmask


## 🔹 Lưu ý về nonlocal đối với biến mutable và immutable

Ngoài nonlocal, còn có global

| **Loại dữ liệu**          | **Ví dụ**             | **Hành động**       | **Có cần `nonlocal` không?**    | **Giải thích**                                |
| ------------------------- | --------------------- | ------------------- | ------------------------------- | --------------------------------------------- |
| `int`                     | `count = 0`           | `count += 1`        | ✅ Cần                           | `int` là immutable → tạo biến mới khi gán lại |
| `float`                   | `total = 1.5`         | `total = total / 2` | ✅ Cần                           | immutable                                     |
| `str`                     | `s = "abc"`           | `s += "x"`          | ✅ Cần                           | immutable                                     |
| `bool`                    | `flag = False`        | `flag = not flag`   | ✅ Cần                           | immutable                                     |
| `tuple`                   | `t = (1,2)`           | `t = t + (3,)`      | ✅ Cần                           | immutable                                     |
| `None`                    | `x = None`            | `x = some_func()`   | ✅ Cần                           | immutable                                     |
| `list`                    | `arr = [1,2,3]`       | `arr[0] = 99`       | ❌ Không                         | Thay đổi nội dung, không gán lại biến         |
| 〃                         | `arr.append(4)`       | ❌ Không             | mutable                         |                                               |
| 〃                         | `arr = [5,6,7]`       | ✅ Cần               | Gán lại biến list mới           |                                               |
| `dict`                    | `d = {'a':1}`         | `d['b'] = 2`        | ❌ Không                         | mutable                                       |
| 〃                         | `d = {'x':10}`        | ✅ Cần               | Gán lại biến dict mới           |                                               |
| `set`                     | `s = {1,2}`           | `s.add(3)`          | ❌ Không                         | mutable                                       |
| 〃                         | `s = {4,5}`           | ✅ Cần               | Gán lại biến set mới            |                                               |
| `object` (class instance) | `obj = Person()`      | `obj.age = 30`      | ❌ Không                         | Chỉ thay đổi thuộc tính                       |
| 〃                         | `obj = OtherPerson()` | ✅ Cần               | Gán lại biến sang instance khác |                                               |
| `function`                | `f = lambda x: x+1`   | `f = other_func`    | ✅ Cần                           | immutable reference                           |

### Tổng quát
- ✅ CẦN nonlocal nếu:
    - Bạn gán lại toàn bộ biến trong hàm con: x = ..., x += ..., x = x + ..., x = func()
    - Biến đó được khai báo trong hàm cha, không phải toàn cục.
- ❌ KHÔNG cần nonlocal nếu:
    - Bạn chỉ thay đổi nội dung bên trong đối tượng (list, dict, set, object).
    - Ví dụ: x.append(), x.pop(), x[0] = ..., x['key'] = ...

Ví dụ 1
```python
def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
    inner()
    print(count)
```

Output
```
1
```

Ví dụ 2
```python
def outer():
    lst = [1, 2, 3]
    count = 0

    def inner():
        # không cần nonlocal
        lst[0] = 99    # thay đổi nội dung
        lst.append(4)

        # cần nonlocal
        nonlocal count
        count += 1

    inner()
    print(lst, count)

outer()
```

Output
```
[99, 2, 3, 4] 1
```