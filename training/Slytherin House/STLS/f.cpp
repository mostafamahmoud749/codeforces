#include <bits/stdc++.h>
#define ll long long
using namespace std;

map<int,int>mp;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int l,n,v,el1,el2,s;
    ll res=0;

    priority_queue<int,vector<int>,greater<int>> pq;
    cin>>l>>n;

    for (int i=0;i<n;i++) {
      cin>>v;
      pq.push(v);
    }


    while (pq.size()>1){
      el1=pq.top();
      pq.pop();
      el2=pq.top();
      pq.pop();

      s=el1+el2;
      res+=s;
      pq.push(s);
    }

    cout<<res;

    return 0;
}