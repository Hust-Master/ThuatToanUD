#include <bits/stdc++.h>
#define int long long
#define task "tsp."
#define inf 1e9 + 7

using namespace std;

const int maxn = 21;
int n, current_cost, best_cost;
int visited[maxn], x_best[maxn], x[maxn], c[maxn][maxn];

void enter()
{
    cin >> n;

    for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= n; ++j)
            cin >> c[i][j];

    // Khởi tạo trước thành phố đầu tiên là 1, đồng thời đánh dấu nó đã thăm.
    x[1] = 1;
    visited[1] = 1;

    // Khởi tạo chi phí tối ưu bằng +oo, giả sử phương án hiện tại đang rất tệ.
    best_cost = inf;
}

// Cập nhật kết quả tốt nhất.
void update_best_solution(int current_cost)
{
    if (current_cost + c[x[n]][1] < best_cost)
    {
        best_cost = current_cost + c[x[n]][1];

        for (int i = 1; i <= n; ++i)
            x_best[i] = x[i];
    }
}

// In ra phương án tốt nhất tìm được.
void print_best_solution()
{
     cout << best_cost << endl;

    //  for (int i = 1; i <= n; ++i)
    //     cout << x_best[i] << "->";
    //  cout << 1;
}

// Giải thuật nhánh và cận.
void branch_and_bound(int i)
{
    if (current_cost >= best_cost)
        return;

    for (int j = 2; j <= n; ++j)
        if (!visited[j])
        {
            visited[j] = 1;
            x[i] = j;
            current_cost += c[x[i - 1]][j];

            // Đã sinh xong một cấu hình, cập nhật chi phí tốt nhất.
            if (i == n)
                update_best_solution(current_cost);
            // Chưa sinh xong, tiếp tục sinh thành phần tiếp theo với chi phí tăng thêm.
            else
                branch_and_bound(i + 1);

            visited[j] = 0;
            current_cost -= c[x[i - 1]][j];
        }
}

main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    enter();
    branch_and_bound(2);
    print_best_solution();

    return 0;
}
