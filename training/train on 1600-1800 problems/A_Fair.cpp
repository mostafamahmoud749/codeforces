#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int n,m,k,s;
    cin>>n>>m>>k>>s;

    vector<int> goods(n);
    for (int i=0;i<n;i++){
        cin>>goods[i];
    }

    vector<vector<int>> adj(n+1);
    vector<vector<int>> kt(k+1);

    for (int i=0;i<n;i++){
        kt[goods[i]].push_back(i+1);
    }

    for (int i=0;i<m;i++){
        int x,y;
        cin>>x>>y;
        adj[x].push_back(y);
        adj[y].push_back(x);
    }

    vector<vector<int>> alld(k+1);

    for (int i=1;i<k+1;i++){
        vector<int> ls = kt[i];
        vector<int> l(n+1,-1);

        if (ls.empty()){
            alld[i]=l;
            continue;
        }

        queue<int> q;

        for (int j:ls){
            l[j]=0;
            q.push(j);
        }
        
        while (!q.empty()) {
            int v;
            v=q.front();
            q.pop();

            for (int u:adj[v]){
                if (l[u]==-1) {
                    l[u]=l[v]+1;
                    q.push(u);
                }
            }
        }
        alld[i]=l;
    }

    vector<int> res;
    for (int i=1;i<n+1;i++){
        vector<int> d;
        for (int j=1;j<k+1;j++){
            if (alld[j][i]!=-1){
                d.push_back(alld[j][i]);
            }
        }
        if (d.size()>=s){
            sort(d.begin(),d.end());
            int x=0;
            for (int k=0;k<s;k++){
                x+=d[k];
            }
            res.push_back(x);
        }
    }
    for (int i:res){
        cout<<i<<" "; 
    }

    return 0;
}