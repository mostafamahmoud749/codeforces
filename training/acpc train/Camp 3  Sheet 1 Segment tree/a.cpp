#include <bits/stdc++.h>
#define ll long long
using namespace std;

#include <vector>
#include <algorithm>

struct SegTree {
    int n;
    std::vector<int> tree;

    // Change these based on the problem requirements
    const int DEFAULT_VALUE = 1e9; // 0 for sum, 1e9 for min, -1e9 for max
    int merge(int a, int b) {
        return min(a,b); // Change to std::min(a, b) or std::max(a, b) if needed
    }

    SegTree(int n) : n(n), tree(4 * n, 0) {}

    void build(const std::vector<int>& arr, int node, int start, int end) {
        if (start == end) {
            tree[node] = arr[start];
            return;
        }
        int mid = start + (end - start) / 2;
        build(arr, 2 * node + 1, start, mid);
        build(arr, 2 * node + 2, mid + 1, end);
        tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2]);
    }

    void update(int node, int start, int end, int idx, int val) {
        if (start == end) {
            tree[node] = val; // Or tree[node] += val depending on problem
            return;
        }
        int mid = start + (end - start) / 2;
        if (idx <= mid) {
            update(2 * node + 1, start, mid, idx, val);
        } else {
            update(2 * node + 2, mid + 1, end, idx, val);
        }
        tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2]);
    }

    int query(int node, int start, int end, int l, int r) {
        if (r < start || end < l) return DEFAULT_VALUE;
        if (l <= start && end <= r) return tree[node];
        int mid = start + (end - start) / 2;
        return merge(query(2 * node + 1, start, mid, l, r),
                     query(2 * node + 2, mid + 1, end, l, r));
    }

    // Easy helper functions to call from main()
    void build(const std::vector<int>& arr) { build(arr, 0, 0, n - 1); }
    void update(int idx, int val) { update(0, 0, n - 1, idx, val); }
    int query(int l, int r) { return query(0, 0, n - 1, l, r); }
};


int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n,q;
    cin>>n>>q;
    vector<int> a(n);
    for (int i=0;i<n;i++){
        cin>>a[i];
    }

    SegTree st(n);
    st.build(a);

    for (int i=0;i<q;i++){
        int t,l,r;
        cin>>t>>l>>r;
        if (t==1){
            st.update(l-1,r);
        }else{
            cout<<st.query(l-1,r-1)<<"\n";
        }
    }
}
