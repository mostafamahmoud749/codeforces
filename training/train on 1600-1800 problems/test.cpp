#include <bits/stdc++.h>
#define ll long long
using namespace std;

int n, ax, ay, bx;
ll by;
    set<int>
        keys;
map<pair<int, ll>, ll> dp;
map<int, vector<int>> goal;
vector<int> keysVec;

ll solve(int indx, ll y)
{
    if (indx == keys.size())
        return llabs(y - by);
    if (dp.count({indx, y}))
        return dp[{indx, y}];
    ll ch1, ch2;
    int key = keysVec[indx];
    int maxy = *max_element(goal[key].begin(), goal[key].end());
    int miny = *min_element(goal[key].begin(), goal[key].end());
    ch1 = llabs(y - maxy) + llabs(miny - maxy) + solve(indx + 1, miny);
    ch2 = llabs(y - miny) + llabs(miny - maxy) + solve(indx + 1, maxy);
    ll res = min(ch1, ch2);
    dp[{indx, y}] = res;
    return res;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int t;
    cin >> t;
    while (t--)
    {
        keys.clear();
        goal.clear();
        dp.clear();
        keysVec.clear();
        cin >> n >> ax >> ay >> bx >> by;
        vector<int> x;
        vector<int> y;
        for (int i = 0; i < n; ++i)
        {
            int v;
            cin >> v;
            x.push_back(v);
        }
        for (int i = 0; i < n; ++i)
        {
            int v;
            cin >> v;
            y.push_back(v);
        }
        for (int i = 0; i < n; i++)
        {
            goal[x[i]].push_back(y[i]);
            keys.insert(x[i]);
        }
        keysVec.assign(keys.begin(), keys.end());
        ll res;
        res = (bx - ax) + solve(0, ay);
        cout << res << "\n";
    }
}
