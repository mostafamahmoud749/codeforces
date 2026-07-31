#include <bits/stdc++.h>
#define ll long long
using namespace std;


int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin>>n;

    vector<int> p(n-1);
    vector<int> s(n);

    for (int i=0;i<n-1;i++){
        cin>>p[i];
    }

    for (int i=0;i<n;i++){
        cin>>s[i];
    }

    vector<vector<int>> adj(n+1);

    for (int i=0;i<n-1;i++){
        adj[i+2].push_back(p[i]);
        adj[p[i]].push_back(i+2);
    }

    vector<ll> val(n+1,-1);
    vector<bool> visited(n+1,false);

    queue<pair<int,ll>> q;
    q.push({1,0});
    visited[1]=true;

    bool pos=true;

    int v,curs;
    while (!q.empty()){
        auto [v,curs]=q.front();
        q.pop();
        ll curv=s[v-1];

        if (curv==-1){
            ll minv=1e18;
            for (auto i:adj[v]){
                if (!visited[i] && s[i-1]!=-1){
                    minv=min(minv,(ll)s[i-1]);
                }
            }
            if (minv==1e18){
                curv=curs;
            }else{
                curv=minv;
            }
        }
        val[v]=curv-curs;

        if (val[v]<0) {
            pos=false;
            break;
        }

        for (auto i:adj[v]){
            if (not visited[i]){
                visited[i]=true;
                q.push({i,curv});
            }
        }
    }

    if (!pos){
        cout<<-1;
        return 0;
    }

    ll res=0;

    for (int i=1;i<n+1;i++){
        res+=val[i];
    }
    cout<<res;

    return 0;
}
