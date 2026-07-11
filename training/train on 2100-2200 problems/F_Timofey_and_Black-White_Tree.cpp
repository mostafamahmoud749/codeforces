#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin>>t;
    while(t--){
        int n,s;
        cin>>n>>s;

        vector<int> a(n-1);
        for (int i=0;i<n-1;i++){
            cin>>a[i];
        }

        vector<vector<int>> adj(n+1);
        vector<int> l(n+1,1e9);
        l[s]=0;

        for (int i=0;i<n-1;i++){
            int x,y;
            cin>>x>>y;
            adj[x].push_back(y);
            adj[y].push_back(x);
        }

        int res=1e9;


        queue<int> q;
        q.push(s);

        while (!q.empty()) {
            int v;
            v=q.front();
            q.pop();

            for (int u:adj[v]){
                if (l[v]+1<l[u]) {
                    l[u]=l[v]+1;
                    q.push(u);
                }
            }
        }

        for (int i:a) {
            res=min(res,l[i]);
            queue<int> q;
            q.push(i);
            l[i]=0;

            while (!q.empty()) {
                int v;
                v=q.front();
                q.pop();

                for (int u:adj[v]){
                    if (l[v]+1<l[u] and l[v]+1<res) {
                        l[u]=l[v]+1;
                        q.push(u);
                    }
                }
            }
            cout<<res<<" ";
        }
        cout<<"\n";
    }

    return 0;
}