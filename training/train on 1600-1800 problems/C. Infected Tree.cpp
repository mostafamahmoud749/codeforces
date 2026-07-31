#include <bits/stdc++.h>
#define ll long long
using namespace std;

int n;
vector<vector<int>> adj;
vector<int> dp;

int solve(int v,int p=0){
    int ch=adj[v].size()-(p!=0);
    if (ch==0) return 1;
    if (ch==1) return 2;
    if (dp[v]!=-1) return dp[v];

    int res=1e9;
    for (auto i:adj[v]){
        if (i!=p){
            res=min(res,solve(i,v));
        }
    }

    return dp[v]=2+res;
}


int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t;
    cin>>t;
    while (t--){
        cin>>n;
        adj.assign(n+1,vector<int>());
        dp.assign(n+1,-1);

        for (int i=0;i<n-1;i++){
            int x,y;
            cin>>x>>y;
            adj[x].push_back(y);
            adj[y].push_back(x);
        }

        cout<<n-solve(1)<<"\n";
    }
    return 0;
}
