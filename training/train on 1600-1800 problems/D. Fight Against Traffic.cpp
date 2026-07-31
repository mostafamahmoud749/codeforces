#include <bits/stdc++.h>
#define ll long long
using namespace std;


int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n,m,s,t;
    cin>>n>>m>>s>>t;

    vector<set<int>> adj(n+1);

    for (int i=0;i<m;i++){
        int x,y;
        cin>>x>>y;
        adj[x].insert(y);
        adj[y].insert(x);
    }

    vector<int> l(n+1,-1);
    l[s]=0;
    queue<int> q;
    q.push(s);

    while (!q.empty()){
        int v;
        v=q.front();
        q.pop();

        for (auto i:adj[v]){
            if (l[i]==-1){
                l[i]=l[v]+1;
                q.push(i);
            }
        }
    }

    vector<int> l2(n+1,-1);
    l2[t]=0;
    q.push(t);

    while (!q.empty()){
        int v;
        v=q.front();
        q.pop();

        for (auto i:adj[v]){
            if (l2[i]==-1){
                l2[i]=l2[v]+1;
                q.push(i);
            }
        }
    }

    int d=l[t];
    int res=0;

    for (int i=1;i<n+1;i++){
        for (int j=i+1;j<n+1;j++){
            if (adj[i].count(j)) continue;
            if (l[i]+1+l2[j]>=d && l[j]+1+l2[i]>=d) res++;
        }
    }

    cout<<res;
    return 0;
}
