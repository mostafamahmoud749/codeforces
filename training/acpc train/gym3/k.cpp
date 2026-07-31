#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <tuple>
using namespace std;

const long long INF = 1e18;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;
    while (t--)
    {
        int n, m;
        cin >> n;
        cin >> m;
        vector<vector<string>> a(n, vector<string>(m));

        for (int k = 0; k < n; k++)
        {
            for (int j = 0; j < m; j++)
            {
                cin >> a[k][j];
            }
        }

        vector<vector<long long>> l(n, vector<long long>(m, INF));
        l[0][0] = 0;

        priority_queue<tuple<long long, int, int>, vector<tuple<long long, int, int>>, greater<tuple<long long, int, int>>> q;
        q.push(make_tuple(0, 0, 0));

        vector<pair<int, int>> dir = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        while (!q.empty())
        {
            long long c, i, j;
            tie(c, i, j) = q.top();
            q.pop();

            if (c > l[i][j])
                continue;

            long long nc;
            if (a[i][j] == "2" || a[i][j] == "3")
            {
                nc = c;
            }
            else
            {
                nc = c + 1;
            }

            for (auto u : dir)
            {
                int ni = u.first + i;
                int nj = u.second + j;
                if (0 <= ni && ni <= n - 1 && 0 <= nj && nj <= m - 1 && nc < l[ni][nj])
                {
                    l[ni][nj] = nc;
                    q.push(make_tuple(nc, ni, nj));
                }
            }
        }

        vector<vector<long long>> l2(n, vector<long long>(m, INF));
        l2[n - 1][m - 1] = 0;

        q.push(make_tuple(0, n - 1, m - 1));

        while (!q.empty())
        {
            long long c, i, j;
            tie(c, i, j) = q.top();
            q.pop();

            if (c > l2[i][j])
                continue;

            long long nc;
            if (a[i][j] == "1" || a[i][j] == "3")
            {
                nc = c;
            }
            else
            {
                nc = c + 1;
            }

            for (auto u : dir)
            {
                int ni = u.first + i;
                int nj = u.second + j;
                if (0 <= ni && ni <= n - 1 && 0 <= nj && nj <= m - 1 && nc < l2[ni][nj])
                {
                    l2[ni][nj] = nc;
                    q.push(make_tuple(nc, ni, nj));
                }
            }
        }
        long long res = INF;
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                res = min(res, l[i][j] + l2[i][j]);
            }
        }

        cout << res << '\n';
    }

    return 0;
}