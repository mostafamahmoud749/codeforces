#include <bits/stdc++.h>
#define ll long long
using namespace std;

map<int,int>mp;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n,t,v;
    string a;
    ll res=0;
    queue<pair<string,int>> q;

    cin>>n>>t;

    for (int i=0;i<n;i++){
      cin>>a>>v;
      q.push({a,v});
    }


    while (!q.empty()) {
      res+=min({q.front().second,t});
      if (q.front().second<=t) {
        cout<<q.front().first<<" "<<res<<"\n";
      } else {
        q.push({q.front().first,q.front().second-t});
      }
      q.pop();
    }

    return 0;
}