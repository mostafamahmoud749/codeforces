#include <bits/stdc++.h>
#define ll long long
using namespace std;

map<int,int>mp;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int n,m,v,t;
    cin>>n>>m;

    for (int i=0;i<n;i++){
      cin>>v;
      t=m-v;

      if (mp[t]!=0) {
        cout<<i+1<<' '<<mp[t];
        return 0;
      }

      mp[v]=i+1;
    }
    
    cout<<"IMPOSSIBLE";

    return 0;
}